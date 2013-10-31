import os
import sys


# RIVETSherpa='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Sherpa_tree_NEvents_941000.root'
# from ROOT import *
# f = TFile.Open(RIVETSherpa)
# t = f.Get('RivetTree')
# n_w = 0.0
# n_0 = 0.0

# for ev in t:
# 	n_0 += 1.0
# 	n_w += ev.evweight

# print n_0
# print n_w
# sys.exit()

sf = 0.1617

rfiles = [x.replace('\n','') for x in os.popen('ls -1 outdir | grep root ').readlines()]

N = 0
for f in rfiles:
	print f
	n = int((f.split('_')[-1]).replace('.root',''))
	N += n

N = round(sf*(1.0*N))

hadd = 'hadd Rivet_Sherpa_N_'+str(N)+'.root outdir/*herpa*rivetTree*root'

print N
os.system(hadd)

