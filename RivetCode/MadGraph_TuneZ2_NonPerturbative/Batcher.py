import os
import sys

os.system('rm -r outdir')
os.system('mkdir outdir')
pwd = (os.popen('pwd').readlines()[0]).replace('\n','')
cmssrc = pwd.split('RivetCode')[0] + 'RivetCode/CMSSW_5_3_5/src'

flist = 'lhefiles.txt'

def MakeConfig(inputconfig,num,NN,files):
	ic = open(inputconfig,'r')
	ocname = '_'+str(num)
	outputfile = 'RivetTree_output'+ocname+'_'+str(NN)+'.root'
	ocname = 'outdir/'+inputconfig.replace('.py',ocname+'.py')
	oc = open(ocname,'w')

	for line in ic:
		
		if 'fileNames' in line:
			fname = line.split('\'')[1]
			line = line.replace(fname, files)
			line = line.replace('\'', '')

		oc.write(line)
	oc.close()
	bname  = (ocname.replace('outdir/','outdir/subber_')).replace('.py','.tcsh')
	batcher = open(bname,'w')
	batcher.write('#!/bin/tcsh\n\ncd '+cmssrc+'\ncmsenv\ncd -\ncp '+pwd+'/'+ocname+' .\n')
	qfile = outputfile
	batcher.write('cmsRun '+ocname.split('/')[-1]+'\n')
	batcher.write('echo "running completed"\nmv rivetTree.root '+qfile+'\necho "renaming completed"\ncp '+qfile+' '+pwd+'/outdir/\necho "copy completed"\n\n')
	batcher.close()
	bsub = 'bsub -q 2nd -e /dev/null -J job_'+str(num)  +' <  '+bname
	return bsub

filesets = []
nn = 0
nmax =3 
fileset = ''
for line in open(flist):
	if len(line)<4: continue
	nn += 1
	fileset += '"'+line.replace('\n','')+'",'
	if nn >= nmax :
		fileset += '\n'
		filesets.append(fileset)
		fileset = ''
		nn=0
if len(fileset)>0:
	filesets.append(fileset)

num = 1
print 'Jobs: ', len(filesets)
for line in (filesets):
	num += 1
	line = line.replace(',\n','')
	n = 100000*nmax
	bsub = MakeConfig('Rivet_WJets_FromCentralGen.py',num,n,line)
	print bsub
	os.system(bsub)
	os.system('sleep 0.4')

