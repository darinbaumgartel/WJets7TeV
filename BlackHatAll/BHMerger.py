import os
import sys

dirs = [x.replace('\n','') for x in os.popen('ls -1 . | grep hists').readlines()]

print dirs

files = [x.replace('\n','') for x in os.popen('find . | grep all').readlines()]

tags = [str(n)+'j' for n in [1,2,3,4]]

for d in dirs:
	for t in tags:
		hadd = 'hadd '+d+"/W"+t+"_all.root "
		for f in files:
			if d in f and t in f:
				hadd += ' '+f
		print hadd
		if '--do' in sys.argv:
			os.system(hadd)
