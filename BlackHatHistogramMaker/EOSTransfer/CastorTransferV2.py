# Directory where you want the castor directory mirrored.
ndir = '/store/group/phys_smp/WPlusJets/BHSNtuplesV2'

if ndir[-1] != '/':
	ndir += '/'

import os
import sys
import random
from time import sleep
import subprocess, datetime, os, time, signal


CastorDirs = ['/castor/cern.ch/user/d/dmaitre/BHSNtuples/W'+x+'j/7TeV' for x in ['m1','m2','m3','m4','p1','p2','p3','p4']]

def nsls(cdir):
	print cdir
	info = os.popen('xrd castorcms dirlist '+cdir)
	output = []

	for ii in info:
		ii = ii.split()
		if len(ii)<2:
			continue
		print ii
		output.append(ii[-1])
	return output

def GetCastorFiles(dirs):
	allfiles = []
	for d in dirs:
		subdirs = nsls(d)
		for s in subdirs:
			allfiles += nsls(s)

			print allfiles
	allfiles.sort()
	f = open('DirectoriesToTransferV2.txt','w')
	for a in allfiles:
		print a
		f.write(a+'\n')
	f.close()

# GetCastorFiles(CastorDirs)

def CreateEOSDirs():
	eosdirs = [ndir+'/']
	def getdirsfromfile(afile):
		f = afile.split('BHSNtuples/')[-1]
		f = f.split('/')
		subdirs = []
		thisdir = ndir
		for x in f:
			if x =='/' or '.root' in x:
				continue
			thisdir += x+'/'
			if thisdir not in eosdirs:
				eosdirs.append(thisdir.replace('//','/')) 


	for line in open('DirectoriesToTransferV2.txt','r'):
		getdirsfromfile(line)
	eosdirs.sort()

	eoscont = str(os.popen('cmsLs -R '+ndir).readlines())
	for e in eosdirs:
		esparse = e.replace('//','/')
		if esparse[-1]=='/':
			esparse = esparse[:-1]
		# print esparse
		# print eoscont
		if esparse not in eoscont:
			print 'cmsMkdir '+e.replace('//','/')
			# os.system('cmsMkdir '+e.replace('//','/'))
	return [eosdirs,eoscont]

[eosdirs,eoscont] = CreateEOSDirs()

cpcommands = []

for f in open('DirectoriesToTransferV2.txt','r'):
	e = f.replace('/castor/cern.ch/user/d/dmaitre/BHSNtuples',ndir)
	# st = 'stager_get -M '
	cp = 'xrdcp "root://castorcms/'+f.replace('\n','')+'" root://eoscms//eos/cms'+e + ' '
	e = e.replace('//','/').replace('\n','')
	if e not in eoscont:
		# print eoscont
		# print e
		# sys.exit()
		if '--stage' in sys.argv:
			os.system('stager_get -M '+f.replace('\n','') +' & ')
			os.system('sleep 0.1')
		cpcommands.append(cp)

print len(cpcommands)

if '--stage' in sys.argv:
	sys.exit()

necessarycps = cpcommands





os.system('rm -r BatchJobs')
os.system('mkdir  BatchJobs')

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

cpgroups = chunks(necessarycps,20)

subs = []

for xx in range(len(cpgroups)):
	f = open('BatchJobs/CP_'+str(xx)+'.tcsh','w')
	subs.append(['BatchJobs/CP_'+str(xx)+'.tcsh','eos_copy_job_'+str(xx)])
	f.write('#!/bin/tcsh\n\n')
	for cp in cpgroups[xx]:
		f.write(cp+'\n\n')
	f.close()

for s in subs:
	os.system('chmod 755 '+s[0])
	if '--submit' in sys.argv:
		os.system('bsub -q 1nh  -e /dev/null -J '+s[1] +' < '+s[0])

	print 'bsub -q 1nh -e /dev/null -J '+s[1] +' < '+s[0]


# print 'Total Files: ',len(castorfiles)
print 'Files requiring copy:',len(necessarycps)
print ' '
if len(necessarycps) == 0:
	print "There are no files which require copying. Transfer is complete!"


# cmsMkdir /store/group/phys_smp/WPlusJets/BHSNtuplesV2/Wp2j/
# cmsMkdir /store/group/phys_smp/WPlusJets/BHSNtuplesV2/Wp2j/7TeV/
