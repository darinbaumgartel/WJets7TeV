import os
import sys

files = ['hists/'+x.replace('\n','') for x in os.popen('ls -1 hists').readlines()]

filetypes = []

for f in files:
	f = f.replace('real','*')
	f = f.replace('loop','*')
	f = f.replace('born','*')
	f = f.replace('vsub','*')

	for x in range(len(f)-6):
		if f[x:x+4] == 'list':
			numtag =  f[x+4:x+7]
			# print numtag
			f = f.replace(numtag,'*')
	if f not in filetypes:
		filetypes.append(f)
	# print f
for f in filetypes:
	outfile = f.replace('*.list*','_')
	outfile = outfile.replace('.root','_all.root')
	for x in range(10):
		outfile = outfile.replace('__','_')
	print './combineHistograms.exe -outfile '+outfile+' '+f
	os.system('./combineHistograms.exe -outfile '+outfile+' '+f)

os.system('rm -r MergedHistos')
os.system('mkdir MergedHistos')
os.system('mv hists/*all.root MergedHistos/')


mfiles = files = ['MergedHistos/'+x.replace('\n','') for x in os.popen('ls -1 MergedHistos').readlines()]

folders = {}
for x in mfiles:
	if '.root' not in x:
		continue
	f = x.split('j_')[-1]
	f = f.replace('_all.root','')
	f = f.replace('.LHgrid','')
	f = 'MergedHistos/hists_'+f
	if f not in folders:
		folders[f]=[x]
	else:
		folders[f].append(x)

for f in folders:
	os.system('mkdir '+f)
	print f, folders[f]
	for x in ['1j', '2j', '3j','4j']:
		haddfiles = ''
		for subfile in folders[f]:
				if x in subfile:
					haddfiles += subfile + ' '
		outfile = f+'/W'+x+'_all.root'
		hadd = 'hadd '+outfile+' '+haddfiles
		print hadd
		os.system(hadd)
	print ' '

print ' --------- Results Combined ----------'
for x in os.popen('ls  MergedHistos/hists*').readlines():
	print x.replace('\n','')