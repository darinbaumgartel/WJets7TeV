import os
import sys
import random

randchars = [x for x in '0123456789qwertyuiopsdfghjklzxcvbnm']
user = (os.popen('whoami').readlines()[0]).replace('\n','')

def GetBJobCount():
	_c = os.popen('bjobs -w | grep '+user+' | grep list |wc -l ').readlines()[0]
	_c = _c.replace('\n','')
	_c = int(_c)
	return _c


n = GetBJobCount()
os.system('sleep 1')
def migratefiles(forcemove):
	allfiles = [x.replace('\n','') for x in os.popen('ls -1 hists')]
	allrootfiles = []
	for x in allfiles:
		if "root" in x:
			allrootfiles.append(x)
	if len(allrootfiles)> 200 or forcemove==True:
		aranddir = 'hists/subdir_'
		lranddir = 'logs/subdir_'

		for nn in range(20):
			cc = random.choice(randchars)
			aranddir+=cc
			lranddir+=cc
		os.system('mkdir '+aranddir)
		os.system('mkdir '+lranddir)

		for r in allrootfiles:
			print('mv hists/'+r+' '+aranddir+'/'+r)			
			os.system('mv hists/'+r+' '+aranddir+'/'+r)
		print('mv logs/*.*'+' '+lranddir+'/')			
		os.system('mv logs/*.*'+' '+lranddir+'/')			


while n > 300:
	print 'Waiting for bjobs to be less than 300. Current bjobs count:',n
	n = GetBJobCount()
	migratefiles(False)
	os.system('sleep 60')


if len(sys.argv)>1:
	if '--done' in sys.argv:
		while n != 0:
			print 'Waiting for all bjobs to finish...'
			n = GetBJobCount()
			os.system('sleep 60')

		migratefiles(True)
		print 'All bjobs finished and files migrated'

print 'Bjobs reduced sufficiently. Moving on....'
