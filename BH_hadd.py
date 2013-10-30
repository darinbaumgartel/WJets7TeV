import os
import sys

dirtag = sys.argv[1]

alldirs =  [x.replace('\n','')  for x in os.popen('find '+dirtag+' | grep -v root').readlines()]

dirs = []
for a in alldirs:
	if len(a.replace(dirtag,''))<3:
		continue
	dirs.append(a)

pairs = []
tots = []
for n in ['1','2','3','4'] :
	pairs.append(['W'+t+n+'j_all.root' for t in ['m','p']])
	tots.append('W'+n+'j_all.root')

hadds = []
for d in dirs:
	for p in range(len(pairs)):
		hadd = 'hadd '+d+'/'+tots[p]
		for f in pairs[p]:
			hadd += ' '+d+'/'+f
		hadds.append(hadd)

for h in hadds:
	print h
	os.system(h)
