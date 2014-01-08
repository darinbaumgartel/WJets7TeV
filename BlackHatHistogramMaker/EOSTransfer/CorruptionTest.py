import sys
from ROOT import *
import os

eosdir  = '/store/group/phys_smp/WPlusJets/BHSNtuplesV2'

print 'Reading list of files in ', eosdir
files = [afile.replace('\n','').split()[-1] for afile in os.popen('cmsLs -R '+eosdir+' | grep root').readlines()]
print '\n Starting corruption tests...\n' 
gEnv.GetValue("TFile.Recover", 0)

def CorruptionTest(afile):
	isGood = True
	f = TFile.Open('root://eoscms//eos/cms'+afile)
	print ' --> ',str(f)
	isGood = '0x(nil)' not in str(f)
	if isGood==True:
		f.Close()
	else:
		print '                      ---> Corruption Detected'
	return [afile,isGood]
n = 0
CorrectedFileContent = []
for f in files:
	n+=1
	print n,'of',len(files),'tested.' 
	CorrectedFileContent.append(CorruptionTest(f))
print '\n\n'+'-'*100+'\n\n'

for c in CorrectedFileContent:
	if c[1]==False:
		print 'Corrupt:', c[0]
print '\n\n'+'-'*100+'\n\n'

