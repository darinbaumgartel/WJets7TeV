import os
import sys

ndir = '/store/group/phys_smp/WPlusJets/BHSNtuplesV2'

allfiles = [x.split()[-1].replace('\n','').replace(ndir,'BHSNtuplesV2') for x in os.popen('cmsLs -R '+ndir+' | grep root').readlines()]

for a in allfiles:
	print a

ftypes = []
for x in ['m','p']:
	for n in ['1','2','3','4']:
		for d in ['born','loop','real','vsub']:
			ftypes.append('W'+x+n+'j_'+d+'.list')


fdict = {}

uniqfiles = []
for a in allfiles:
	x = 'x'
	n = 'n'
	d = 'none'
	if 'Wm' in a:
		x = 'm'
	if 'Wp' in a:
		x = 'p'

	for _n in ['1','2','3','4']:
		if _n+'j_' in a:
			n = _n 

	if 'B0' in a:
		d = 'born'
	if 'V0' in a:
		d = 'loop'
	if 'I0' in a:
		d = 'vsub'
	if 'R0' in a:
		d = 'real'

	corresfile = 'W'+x+n+'j_'+d+'.list'

	fdict[a] = corresfile
	if corresfile not in uniqfiles:
		uniqfiles.append(corresfile)
	print a,corresfile

# udict = {}
for u in uniqfiles:
	f = open(u,'w')
	for a in allfiles:
		if fdict[a] == u:
			f.write(a+'\n')
	f.close()