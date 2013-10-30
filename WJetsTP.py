import os
import sys
sys.argv.append("-b")
from ROOT import *
# Directory where root files are kept and the tree you want to get root files from. Normal is for standard analysis, the jet rescaling, jet smearing, muon PT rescaling ,and muon PT smearing. 
from datetime import datetime

startTime = datetime.now()

afsdir = '/afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_4_2_8/src/WJetsAnalysis/'
NormalDirectory = afsdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Sept2_2013_09_02_16_51_14/SummaryFiles"
		
from ROOT import *

Z = NormalDirectory+'/ZJets_MG.root'
D = NormalDirectory+'/SingleMuData.root'


# Basic event filters
filters = '*(pass_HBHENoiseFilter*pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'

# Placeholder to require additional jet
j1="*(Pt_pfjet1>30.0)*(abs(Eta_pfjet1)<2.4)"
j2="*(Pt_pfjet2>30.0)*(abs(Eta_pfjet2)<2.4)"
j3="*(Pt_pfjet3>30.0)*(abs(Eta_pfjet3)<2.4)"
j4="*(Pt_pfjet4>30.0)*(abs(Eta_pfjet4)<2.4)"
j5="*(Pt_pfjet5>30.0)*(abs(Eta_pfjet5)<2.4)"
j6="*(Pt_pfjet6>30.0)*(abs(Eta_pfjet6)<2.4)"

# Basic selection for reco-level plots
basic_selection = '(Pt_muon1>25)*(RelIso_muon1<0.15)*(Pt_muon2>25.0)*(abs(Eta_muon1)<2.1)*(abs(Eta_muon2)<2.1)*(IsoMu24Pass>0)'
basic_selection += '*(PFJet30TCHEMCountCentral<0.5)*(M_muon1muon2> 80)*(M_muon1muon2< 100)'
basic_selection += filters
basic_selection += j1

full_selection = basic_selection +'*(RelIso_muon2<0.15)'

tZ = TFile.Open(Z).Get("PhysicalVariables")
tD = TFile.Open(D).Get("PhysicalVariables")

print tZ.GetEntries()
print tD.GetEntries()

from array import array
def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset
# Small function to clean up a TLegend style
def FixDrawLegend(legend):
	legend.SetTextFont(42)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend
# Make basic TH1D for a branch. Projects branch to histo for given binning and selection. 
def CreateHisto(name,legendname,tree,variable,binning,selection,style,label):
	print name,legendname
	# tmpfile = TFile.Open('tmp'+str(random.randint(0,100000000))+str(random.randint(0,100000000))+'.root',"RECREATE")
	# print 'Creating histo for ',name, legendname,
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	# print '   ... bins created.'
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	# print '   ... histo initialized.'
	tree.Project(name,variable,selection) # Project from branch to histo
	# print '   ... projection complete.'
	
	# Below is all style. Style is list of arguments passed:
	# [FillStyle, MarkerStyle, MarkerSize, Global Color]
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetMaximum(2.0*hout.GetMaximum()) # Better looking maximum

	# label is a list [XLabel, YLabel]
	hout.GetXaxis().SetTitle(label[0]) 
	hout.GetYaxis().SetTitle(label[1])

	# Good old-fashioned times new roman.
	hout.GetXaxis().SetTitleFont(42)
	# print '  ... set title font x'
	hout.GetYaxis().SetTitleFont(42)
	# print '  ... set title font y'
	hout.GetXaxis().SetLabelFont(42)
	# print '  ... set label font x'
	hout.GetYaxis().SetLabelFont(42)
	# print '  ... set label font y'

	# print '   ... style modified.'
	# os.system('sleep 1')
	# print '   ... Histogram complete:',name, legendname
	# tmpfile.Write()
	# tmpfile.Close()

	return hout


gROOT.SetStyle('Plain')  # Plain white default for plots
gStyle.SetOptTitle(0) # No titles

presentationbinning = [25,30,35,40,50,70,90,200]
presentationbinning = [25,35,55,200]
print presentationbinning

weight = '*weight_pu_central*4955'
selection = basic_selection
WStackStyle=[3007,20,.00001,2,6]
TTStackStyle=[3005,20,.00001,2,4]
ZStackStyle=[1001,20,.00001,2,2]
DiBosonStackStyle=[3006,20,.00001,2,3]
StopStackStyle=[3008,20,.00001,2,9]
QCDStackStyle=[3013,20,.00001,2,15]

DataRecoStyle=[0,20,1.0,1,1]

Label = ["Pt(#mu)","Entries/Bin"]


##################################
######   1 JET SELECTION   #######
##################################


hZ_all_1=CreateHisto('hZ_all_1','Z+Jets (1+ jets)',tZ,'Pt_muon2',presentationbinning,selection+weight,ZStackStyle,Label)
hD_all_1=CreateHisto('hD_all_1','Data (1+ jets)',tD,'Pt_muon2',presentationbinning,selection,DataRecoStyle,Label)

hZ_sel_1=CreateHisto('hZ_sel_1','Z+Jets (1+ jets)',tZ,'Pt_muon2',presentationbinning,full_selection+weight,ZStackStyle,Label)
hD_sel_1=CreateHisto('hD_sel_1','Data (1+ jets)',tD,'Pt_muon2',presentationbinning,full_selection,DataRecoStyle,Label)

##################################
######   2 JET SELECTION   #######
##################################

selection += j2
full_selection += j2

hZ_all_2=CreateHisto('hZ_all_2','Z+Jets (2+ jets)',tZ,'Pt_muon2',presentationbinning,selection+weight,ZStackStyle,Label)
hD_all_2=CreateHisto('hD_all_2','Data (2+ jets)',tD,'Pt_muon2',presentationbinning,selection,DataRecoStyle,Label)

hZ_sel_2=CreateHisto('hZ_sel_2','Z+Jets (2+ jets)',tZ,'Pt_muon2',presentationbinning,full_selection+weight,ZStackStyle,Label)
hD_sel_2=CreateHisto('hD_sel_2','Data (2+ jets)',tD,'Pt_muon2',presentationbinning,full_selection,DataRecoStyle,Label)


##################################
######   3 JET SELECTION   #######
##################################

selection += j3
full_selection += j3

hZ_all_3=CreateHisto('hZ_all_3','Z+Jets (3+ jets)',tZ,'Pt_muon2',presentationbinning,selection+weight,ZStackStyle,Label)
hD_all_3=CreateHisto('hD_all_3','Data (3+ jets)',tD,'Pt_muon2',presentationbinning,selection,DataRecoStyle,Label)

hZ_sel_3=CreateHisto('hZ_sel_3','Z+Jets (3+ jets)',tZ,'Pt_muon2',presentationbinning,full_selection+weight,ZStackStyle,Label)
hD_sel_3=CreateHisto('hD_sel_3','Data (3+ jets)',tD,'Pt_muon2',presentationbinning,full_selection,DataRecoStyle,Label)


##################################
######   4 JET SELECTION   #######
##################################

selection += j4
full_selection += j4

hZ_all_4=CreateHisto('hZ_all_4','Z+Jets (4+ jets)',tZ,'Pt_muon2',presentationbinning,selection+weight,ZStackStyle,Label)
hD_all_4=CreateHisto('hD_all_4','Data (4+ jets)',tD,'Pt_muon2',presentationbinning,selection,DataRecoStyle,Label)

hZ_sel_4=CreateHisto('hZ_sel_4','Z+Jets (4+ jets)',tZ,'Pt_muon2',presentationbinning,full_selection+weight,ZStackStyle,Label)
hD_sel_4=CreateHisto('hD_sel_4','Data (4+ jets)',tD,'Pt_muon2',presentationbinning,full_selection,DataRecoStyle,Label)


##################################
######   DRAWING   #######
##################################
hZ_sel_1.Divide(hZ_all_1)
hD_sel_1.Divide(hD_all_1)

hZ_sel_2.Divide(hZ_all_2)
hD_sel_2.Divide(hD_all_2)

hZ_sel_3.Divide(hZ_all_3)
hD_sel_3.Divide(hD_all_3)

hZ_sel_4.Divide(hZ_all_4)
hD_sel_4.Divide(hD_all_4)

hZ_sel_1.SetMaximum(1.05)
hD_sel_1.SetMaximum(1.05)

hZ_sel_2.SetMaximum(1.05)
hD_sel_2.SetMaximum(1.05)

hZ_sel_3.SetMaximum(1.05)
hD_sel_3.SetMaximum(1.05)

hZ_sel_4.SetMaximum(1.05)
hD_sel_4.SetMaximum(1.05)


hZ_sel_1.SetMinimum(0.85)
hD_sel_1.SetMinimum(0.85)

hZ_sel_2.SetMinimum(0.85)
hD_sel_2.SetMinimum(0.85)

hZ_sel_3.SetMinimum(0.85)
hD_sel_3.SetMinimum(0.85)

hZ_sel_4.SetMinimum(0.85)
hD_sel_4.SetMinimum(0.85)






##################################
######  BASIC HISTOGRAMS   #######
##################################

hD_sel_1.GetYaxis().SetTitle("Pass/Fail Rate")
hD_sel_2.GetYaxis().SetTitle("Pass/Fail Rate")
hD_sel_3.GetYaxis().SetTitle("Pass/Fail Rate")
hD_sel_4.GetYaxis().SetTitle("Pass/Fail Rate")

hZ_sel_1.GetYaxis().SetTitle("Pass/Fail Rate")
hZ_sel_2.GetYaxis().SetTitle("Pass/Fail Rate")
hZ_sel_3.GetYaxis().SetTitle("Pass/Fail Rate")
hZ_sel_4.GetYaxis().SetTitle("Pass/Fail Rate")

c1 = TCanvas("c1","",1200,900)
c1.Divide(2,2)
gStyle.SetOptStat(0)

c1.cd(1)
c1.cd(1).SetLogy()
hZ_all_1.Draw("")
hD_all_1.Draw("EPSAME")
FixDrawLegend(c1.cd(1).BuildLegend())

c1.cd(2)
c1.cd(2).SetLogy()
hZ_all_2.Draw("")
hD_all_2.Draw("EPSAME")
FixDrawLegend(c1.cd(2).BuildLegend())

c1.cd(3)
c1.cd(3).SetLogy()
hZ_all_3.Draw("")
hD_all_3.Draw("EPSAME")
FixDrawLegend(c1.cd(3).BuildLegend())

c1.cd(4)
c1.cd(4).SetLogy()
hZ_all_4.Draw("")
hD_all_4.Draw("EPSAME")
FixDrawLegend(c1.cd(4).BuildLegend())


c1.Print('TPResults/Results_HIST.pdf')
c1.Print('TPResults/Results_HIST.png')


##################################
######  RATIO HISTOGRAMS   #######
##################################

c2 = TCanvas("c2","",1200,900)
c2.Divide(2,2)
gStyle.SetOptStat(0)

c2.cd(1)
hZ_sel_1.Draw("")
hD_sel_1.Draw("E1PSAME")
FixDrawLegend(c2.cd(1).BuildLegend())

c2.cd(2)
hZ_sel_2.Draw("")
hD_sel_2.Draw("E1PSAME")
FixDrawLegend(c2.cd(2).BuildLegend())

c2.cd(3)
hZ_sel_3.Draw("")
hD_sel_3.Draw("E1PSAME")
FixDrawLegend(c2.cd(3).BuildLegend())

c2.cd(4)
hZ_sel_4.Draw("")
hD_sel_4.Draw("E1PSAME")
FixDrawLegend(c2.cd(4).BuildLegend())


c2.Print('TPResults/Results_RAT.pdf')
c2.Print('TPResults/Results_RAT.png')


##################################
######  SCALE HISTOGRAMS   #######
##################################

hD_sel_1.GetYaxis().SetTitle("Data/MC")
hD_sel_2.GetYaxis().SetTitle("Data/MC")
hD_sel_3.GetYaxis().SetTitle("Data/MC")
hD_sel_4.GetYaxis().SetTitle("Data/MC")

hD_sel_1.SetMaximum(1.1)
hD_sel_2.SetMaximum(1.1)
hD_sel_3.SetMaximum(1.1)
hD_sel_4.SetMaximum(1.1)

hD_sel_1.SetMinimum(0.9)
hD_sel_2.SetMinimum(0.9)
hD_sel_3.SetMinimum(0.9)
hD_sel_4.SetMinimum(0.9)

c3 = TCanvas("c3","",1200,900)
c3.Divide(1,1)
gStyle.SetOptStat(0)


hD_sel_1.Divide(hZ_sel_1)
hD_sel_2.Divide(hZ_sel_2)
hD_sel_3.Divide(hZ_sel_3)
hD_sel_4.Divide(hZ_sel_4)

hD_sel_1.SetTitle("Data/MC (1+ jet)")
hD_sel_2.SetTitle("Data/MC (2+ jet)")
hD_sel_3.SetTitle("Data/MC (3+ jet)")
hD_sel_4.SetTitle("Data/MC (4+ jet)")

hD_sel_1.SetLineColor(1)
hD_sel_2.SetLineColor(2)
hD_sel_3.SetLineColor(3)
hD_sel_4.SetLineColor(4)

hD_sel_1.SetMarkerColor(1)
hD_sel_2.SetMarkerColor(2)
hD_sel_3.SetMarkerColor(3)
hD_sel_4.SetMarkerColor(4)

c3.cd(1)
# hZ_sel_1.Draw("")
hD_sel_1.Draw("E1P")
# FixDrawLegend(c3.cd(1).BuildLegend())

# c3.cd(2)
# hZ_sel_2.Draw("")
hD_sel_2.Draw("E1PSAME")
# FixDrawLegend(c3.cd(2).BuildLegend())

# c3.cd(3)
# hZ_sel_3.Draw("")
hD_sel_3.Draw("E1PSAME")
# FixDrawLegend(c3.cd(3).BuildLegend())

# c3.cd(4)
# hZ_sel_4.Draw("")
hD_sel_4.Draw("E1PSAME")
FixDrawLegend(c3.cd(1).BuildLegend())


c3.Print('TPResults/Results_SF.pdf')
c3.Print('TPResults/Results_SF.png')
