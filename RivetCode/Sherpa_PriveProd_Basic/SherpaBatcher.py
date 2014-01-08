import os
import sys

os.system('rm -r outdir')
os.system('mkdir outdir')
pwd = (os.popen('pwd').readlines()[0]).replace('\n','')
src = pwd.split('RivetCode')[0] + 'RivetCode/CMSSW_6_0_1/src'


fdir1 = '/store/group/phys_exotica/darinb/SherpaTest/'
fdir2 = '/store/group/phys_smp/WPlusJets/Sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000'

dircont = os.popen('cmsLs '+fdir1).readlines()+ os.popen('cmsLs '+fdir2).readlines()
#dircont = [line for line in open('dircont.txt','r')]

def MakeConfig(inputconfig,inputfile,outputfile):
	ic = open(inputconfig,'r')
	ocname = inputfile.replace('.root','')
	ocname = '_'+ocname.split('_')[-3]+'_'+ocname.split('_')[-2]+'_'+ocname.split('_')[-1]
	ocname = 'outdir/'+inputconfig.replace('.py',ocname+'.py')
	oc = open(ocname,'w')

	for line in ic:
		
		if 'fileNames' in line:
			fname = line.split('\'')[1]
			line = line.replace(fname, inputfile)
		oc.write(line)
	oc.close()
	bname  = (ocname.replace('outdir/','outdir/subber_')).replace('.py','.tcsh')
	batcher = open(bname,'w')
	batcher.write('#!/bin/tcsh\n\ncd '+src+'\ncmsenv\ncd -\ncp '+pwd+'/'+ocname+' .\n')
	qfile = outputfile.split('/')[-1]
	batcher.write('cmsRun '+ocname.split('/')[-1]+'\n')
	batcher.write('mv rivetTree.root '+qfile+'\ncp '+qfile+' '+pwd+'/outdir/\n\n')
	batcher.close()
	bsub = 'bsub -q 1nh -e /dev/null -J '+  (qfile.split('.')[-2]).split('GEN_')[-1]+' <  '+bname
	return bsub
bsubs = []
for line in dircont:
	# print line
	if 'root' not in line:
		continue
	line = line.replace('\n','')
	line = line.split()
	size = int(line[1])
	if size == 0:
		continue
	f = line[-1]
	n = int(((os.popen('edmFileUtil '+f).readlines()[1]).split())[5])
	fout = f.replace('.root','_rivetTree_N_'+str(n)+'.root')
	bsub = MakeConfig('Rivet_WJets_FromCentralGen.py',f,fout)

	bsubs.append(bsub)
	print bsub
	os.system(bsub)

