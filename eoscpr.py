import os
import sys

eosmain = '/store/group/phys_smp/WPlusJets/AnalyzerOutput/'

adir = sys.argv[1]

eosmain = '/store/group/phys_smp/WPlusJets/AnalyzerOutput/'+adir+'/'
for x in range(4):
	eosmain = eosmain.replace('//','/')

dcont = [x.replace('\n','') for x in os.popen('find NTup*'+adir+'*').readlines()]

dcont = [''] + dcont
dcont.sort(key=len)


dirs = []
files = []


for x in dcont:
	if '.' not in x:
		dirs.append(x)
	else:
		files.append(x)

mkdirs = ['cmsMkdir '+eosmain+d for d in dirs]

cps = ['cmsStageOut '+f+' '+eosmain+f for f in files]

F = ('transfer_'+adir+'.do')
f = open(F,'w')

for m in mkdirs:
	f.write('echo "Making Dir: '+m+'"\n')
	f.write(m+'\n')
f.write('\n')
for c in cps:
	f.write('echo "Transferring: '+c+'"\n')
	f.write(c+' & \nsleep 20\n')
f.close()
os.system('chmod 755 '+F)

print ' Finished building. Run ',F,'for transfer.'