import os
import sys
from glob import glob
import math

def quadsum(values, bvalues):
	I = 0.0
	E = 0.0
	for ind in range(len(values)):
		v = values[ind]
		b = bvalues[ind].split(' - ')
		width = float(b[1]) - float(b[0])
		# print b
		[_i, _e] = [float(x)*width for x in v.split('+-')]
		I += _i
		E += _e*_e
	E  = math.sqrt(E)
	return [I,E]

def indivsums(values):
	output = []
	for v in values:
		[_i, _e] = [float(x) for x in v.split('+-')]
		output.append([_i, _e])
	
	return output

def IntegralFromFile(afile):
	dvals = []
	bvals = []
	if 'PFJet30' not in afile:
		for line in open(afile,'r'):
			# line = line.replace(' ','')
			line = line.split('|')
			# print line[0], line[1], line[2], line[3]
			if 'Bin' not in str(line):
				dvals.append(line[3])
				bvals.append(line[1])
		return quadsum(dvals,bvals)
	else:	
		for line in open(afile,'r'):
			line = line.replace(' ','')
			line = line.split('|')
			# print line[0], line[1], line[2], line[3]
			if 'Bin' not in str(line):
				dvals.append(line[3])
		return indivsums(dvals)
def GetFiles(adir):
	allfiles = glob(adir+'/pyplotsTCHEM/*.txt')
	bfiles = []
	for x in allfiles:
		if 'TGraph' not in x and 'Tex' not in x:
			bfiles.append(x)
	bfiles.sort()
	fileoutput = []
	for b in bfiles:
		# print b, IntegralFromFile(b)
		fileoutput.append([b,IntegralFromFile(b)])
		# IntegralFromFile(b)
	# return bfiles
	return fileoutput


filedata = GetFiles(sys.argv[1])

EtaData = []
PtData = []
DPhiData = []
HTData = []
MultData = []

jtags = ['jet1','jet2','jet3','jet4']
for jtag in jtags:
	for f in filedata:
		# print jtag, jtag in f[0], f[0]
		# print f
		if jtag not in f[0]:
			continue
		if 'Eta' in f[0]:
			EtaData.append(f[-1])
		if 'Pt' in f[0]:
			PtData.append(f[-1])
		if 'Delta' in f[0]:
			DPhiData.append(f[-1])

jtags = ['inc1','inc2','inc3','inc4']
for jtag in jtags:
	for f in filedata:
		if jtag not in f[0]:
			continue
		if 'HT' in f[0]:
			HTData.append(f[-1])

for f in filedata:
	if 'preexc' not in f[0]:
		continue
	MultData = f[-1][:4]

# print EtaData
# print PtData
# print HTData
# print DPhiData
# print MultData


sys.argv.append('-b')
from ROOT import *
gROOT.SetStyle('Plain')  # Plain white default for plots
gStyle.SetOptTitle(0) # No titles

c0 = TCanvas("c1","",1200,900)
gStyle.SetOptStat(0)

hM = TH1F('hM','hM',4,0.5,4.5)
hD = TH1F('hD','hD',4,0.5,4.5)
hE = TH1F('hE','hE',4,0.5,4.5)
hP = TH1F('hP','hP',4,0.5,4.5)
hH = TH1F('hH','hH',4,0.5,4.5)

print PtData
print MultData
print ' --------------------------------- '
for bin in [1,2,3,4]:
	j = bin-1
	# print hM.GetBinCenter(bin)
	hM.SetBinContent(bin,MultData[j][0]/MultData[j][0])
	hM.SetBinError(bin,MultData[j][1]/MultData[j][0])	

	hD.SetBinContent(bin,DPhiData[j][0]/MultData[j][0])
	hD.SetBinError(bin,DPhiData[j][1]/DPhiData[j][0])

	hE.SetBinContent(bin,EtaData[j][0]/MultData[j][0])
	hE.SetBinError(bin,EtaData[j][1]/EtaData[j][0])
	print '----',bin,'-----'
	print j, PtData[j], MultData[j]
	hP.SetBinContent(bin,PtData[j][0]/MultData[j][0])
	hP.SetBinError(bin,PtData[j][1]/PtData[j][0])

	hH.SetBinContent(bin,HTData[j][0]/MultData[j][0])	
	hH.SetBinError(bin,HTData[j][1]/HTData[j][0])

hM.SetLineColor(18)
hM.SetMarkerColor(18)
hM.SetFillColor(18)
hM.GetXaxis().SetTitle("Inclusive Jet Multiplicity")
hM.GetYaxis().SetTitle("Integral w.r.t. Inclusive Multiplicity Bin")
hM.SetMinimum(0.90)
hM.SetMaximum(1.10)
hM.Draw('E2')

hH.SetMarkerColor(1)
hP.SetMarkerColor(2)
hE.SetMarkerColor(4)
hD.SetMarkerColor(6)

hH.SetLineColor(1)
hP.SetLineColor(2)
hE.SetLineColor(4)
hD.SetLineColor(6)

hH.SetLineStyle(0)
hP.SetLineStyle(0)
hE.SetLineStyle(0)
hD.SetLineStyle(0)

hH.SetMarkerStyle(24)
hP.SetMarkerStyle(25)
hE.SetMarkerStyle(26)
hD.SetMarkerStyle(32)

hH.SetMarkerSize(2)
hP.SetMarkerSize(2)
hE.SetMarkerSize(2)
hD.SetMarkerSize(2)

hH.Draw('E1PSAME')
hP.Draw('E1PSAME')
hE.Draw('E1PSAME')
hD.Draw('E1PSAME')
ratunity=TLine(0.5, 1.0 , 4.5,1.0)
ratunity.SetLineStyle(3)

ratunity.Draw("SAME")

leg = TLegend(0.14,0.7,0.35,0.87,"","brNDC")
leg.SetTextFont(42)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.SetTextSize(.03)
leg.AddEntry(hM, "Inclusive Mult w/ Unfolding Unc.")
leg.AddEntry(hH, "H_{T}(jet) Integrals")
leg.AddEntry(hP, "p_{T}(jet) Integrals")
leg.AddEntry(hE, "#eta(jet) Integrals")
leg.AddEntry(hD, "#Delta#phi (#mu, jet) Integrals")

leg.Draw()

c0.Print(sys.argv[1]+'/InclusiveBinContentComparison.png')
c0.Print(sys.argv[1]+'/InclusiveBinContentComparison.pdf')
