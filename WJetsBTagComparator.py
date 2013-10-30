import os


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

# The main function, called at the end of the script after all other function definitions. If just running analysis on a variable, modify only here.
def main():

	# MadGraphSubStyle=[3254,21,.7,1,4]

	# [grat,[gratup,gratdown]] = DivideTGraphs(Meas_verbose,Exp_verbose,MadGraphSubStyle)

	tchptfiles = [x.replace('\n','') for x in os.popen('ls -1 pyplotsTCHPT | grep TGraphContent ').readlines()]
	ssvhptfiles = [x.replace('\n','') for x in os.popen('ls -1 pyplotsSSVHPT | grep TGraphContent ').readlines()]
	jptfiles = [x.replace('\n','') for x in os.popen('ls -1 pyplotsJPT | grep TGraphContent ').readlines()]

	# print tchptfiles
	# print ssvhptfiles
	# print jptfiles

	finalfiles = []
	for f in tchptfiles:
		if f in ssvhptfiles and f in jptfiles:
			finalfiles.append('pyplotsTCHPT/'+f)


	ftmp = TFile.Open('fjunkbtagcomp.root','RECREATE')


	for f in finalfiles:
		t_dat = ((os.popen('cat '+f+' | grep Meas').readlines())[0]).split('=')[-1]
		# print f_dat
		s = f.replace('TCHPT','SSVHPT')
		j = f.replace('TCHPT','JPT')
		s_dat = ((os.popen('cat '+s+' | grep Meas').readlines())[0]).split('=')[-1]
		j_dat = ((os.popen('cat '+j+' | grep Meas').readlines())[0]).split('=')[-1]

		exec('t_inf = '+t_dat)
		exec('s_inf = '+s_dat)
		exec('j_inf = '+j_dat)

		# print t_dat
		# print t_inf
		MakeOutputPlot(f,t_inf,s_inf,j_inf)


	os.system("convert pyplotsTCHPT/*Count*btagComparison.png pyplotsTCHPT/AllFinalCountCompPlots.pdf")
	os.system("convert pyplotsTCHPT/*XSec*btagComparison.png pyplotsTCHPT/AllFinalXSecCompPlots.pdf")



####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

##########################################################################
########            Import libraries                              ########
##########################################################################

import sys
import math
sys.argv.append( '-b' )  # Batch mode - no XWindows - much faster
from ROOT import * # Load root
from glob import * # For table parsing
import csv         # For table parsing
from itertools import izip  # More for table parsing
from array import array    
import numpy
import random

##########################################################################
########              CleanUp/SetUp ROOT                          ########
##########################################################################
gROOT.ProcessLine("gErrorIgnoreLevel = 2001;") # Suppress warnings
TFormula.SetMaxima(100000,1000,1000000) # Allow big strings for tcuts
rnd= TRandom3() # Using TRandom3 for random numbers - no profound impact
gROOT.SetStyle('Plain')  # Plain white default for plots
gStyle.SetOptTitle(0) # No titles
# Below is for setting TH2D color plots to red-blue heat spectrum
NCont = 50
NRGBs = 5
stops = array("d",[ 0.00, 0.34, 0.61, 0.84, 1.00])
red= array("d",[ 0.00, 0.00, 0.87, 1.00, 0.51 ])
green= array("d",[ 0.00, 0.81, 1.00, 0.20, 0.00 ])
blue= array("d",[ 0.51, 1.00, 0.12, 0.00, 0.00 ])
TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
gStyle.SetNumberContours(NCont)
##########################################################################
##########################################################################

# Small function to clean up a TLegend style
def FixDrawLegend(legend):
	legend.SetTextFont(132)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend

# All binning is passed as variable binning. This converts constant to variable.
def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset

# Make basic TH1D for a branch. Projects branch to histo for given binning and selection. 
def CreateHisto(name,legendname,tree,variable,binning,selection,style,label):
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	tree.Project(name,variable,selection) # Project from branch to histo
	
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
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	return hout

# Converts ugly histo to pretty histo, or can change style of any histo.
def BeautifyHisto(histo,style,label,newname):
	histo.SetTitle(newname)	# New legend name

	# And the same style setup as above.
	histo.SetFillStyle(style[0])
	histo.SetMarkerStyle(style[1])
	histo.SetMarkerSize(style[2])
	histo.SetLineWidth(style[3])
	histo.SetMarkerColor(style[4])
	histo.SetLineColor(style[4])
	histo.SetFillColor(style[4])
	histo.SetFillColor(style[4])
	histo.GetXaxis().SetTitle(label[0])
	histo.GetYaxis().SetTitle(label[1])
	histo.GetXaxis().SetTitleFont(132)
	histo.GetYaxis().SetTitleFont(132)
	histo.GetXaxis().SetLabelFont(132)
	histo.GetYaxis().SetLabelFont(132)
	return histo

# Cleans up a stacked histogram
def BeautifyStack(stack,label):
	# Fix Font
	stack.GetHistogram().GetXaxis().SetTitleFont(132)
	stack.GetHistogram().GetYaxis().SetTitleFont(132)
	stack.GetHistogram().GetXaxis().SetLabelFont(132)
	stack.GetHistogram().GetYaxis().SetLabelFont(132)
	#Fix Label
	stack.GetHistogram().GetXaxis().SetTitle(label[0])
	stack.GetHistogram().GetYaxis().SetTitle(label[1])
	return stack

def Create2DHisto(name,legendname,tree,variable1,variable2,binning,selection,label):
	binset=ConvertBinning(binning) # Variable binning
	n = len(binset)-1 # Carry the 1
	hout= TH2D(name,legendname,n,array('d',binset),n,array('d',binset)) # Declare empty histo
	hout.Sumw2() # Store sum of squares
	tree.Project(name,variable1+":"+variable2,selection) # Project branch1:branch2 with selection 
	# Clean up font and labels.
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	
	return hout



def GetIntErr(histograms):
	Int = 0
	Err = 0
	for h in histograms:
		ii = h.Integral()
		Int += ii
		if ii < 0.001:
			continue
		Err += ii*ii/h.GetEntries()
	Err = math.sqrt(Err)
	return [Int,Err]


# Take a given binning, and means with errors, and create a TGraphAsymErrors output.
def CreateHistoFromLists(binning, name, label, mean, up, down, style,normalization,plottype):

	binset=ConvertBinning(binning)
	n = len(binset)-1
	htest= TH1D('htest','htest',n,array('d',binset))

	for a in range(len(mean)):
		mean[a] = abs(mean[a])
	for a in range(len(up)):
		up[a] = abs(up[a])
	for a in range(len(down)):
		down[a] = abs(down[a])


	X = []
	Y = []
	Xplus=[]
	Xminus=[]
	Yplus=[]
	Yminus=[]

	if normalization==0:
		N=1.0
	else:
		N=normalization

	for x in range(len(binset)-1):
		c = htest.GetBinCenter(x+1)
		d = 0.5*htest.GetBinWidth(x+1)
		center = mean[x]
		upper = up[x]
		lower=down[x]
		
		X.append(c)
		Xplus.append(abs(d))
		Xminus.append(abs(d))
		
		Y.append(center/N)
		Yplus.append(abs(upper)/N)
		Yminus.append(abs(lower)/N)
			
	X = array("d", X)
	Xplus = array("d", Xplus)
	Xminus = array("d", Xminus)


	Y = array("d", Y)
	Yplus = array("d", Yplus)
	Yminus = array("d", Yminus)	

	hout = TGraphAsymmErrors(n,X,Y,Xminus,Xplus,Yminus,Yplus)
	
	hout.SetTitle(name)
	
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	#hout.SetMaximum(2.0*hout.GetMaximum())
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)

	if plottype=="TopPlot":
		hout.GetYaxis().SetTitleFont(132);
		hout.GetXaxis().SetTitleSize(.06);
		hout.GetYaxis().SetTitleSize(.06);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();
		hout.GetXaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetLabelSize(.05);
		hout.GetXaxis().SetLabelSize(.05);


	if plottype=="SubPlot":
		hout.GetYaxis().SetTitleFont(132);
		hout.GetXaxis().SetTitleSize(.13);
		hout.GetYaxis().SetTitleSize(.13);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();		
		hout.GetXaxis().SetTitleOffset(.28);
		hout.GetYaxis().SetTitleOffset(.28);
		hout.GetYaxis().SetLabelSize(.09);
		hout.GetXaxis().SetLabelSize(.09);

	return [hout,[mean,up,down,binset]]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, nmadgraph, quantity, WRenormalizationForRivet):

	frivet = TFile.Open(rivetfile)
	trivet = frivet.Get("RivetTree")
	Name = "MadGraph"*("MadGraph" in rivetfile) + "Pythia"*("Pythia" in rivetfile) + "PROBLEM"*("MadGraph" not in rivetfile and "Pythia" not in rivetfile) + "Sherpa"*("Sherpa" in rivetfile)
	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
	# print 'Total Entries: ', trivet.GetEntries()
	print ' hrivet stats:    ', hrivet.GetEntries(), hrivet.Integral(), 
	print ' In Madgraph:  ', nmadgraph
	acceptance = (1.0*(hrivet.Integral()))/(1.0*original_events)
	# print 'Acceptance: ', acceptance,
	scalefactor = (4980.0*31314.0)*acceptance
	# print 'Scale: ', scalefactor
	if hrivet.Integral()>0:
		hrivet.Scale(1.0/hrivet.Integral())
	means=[]
	errs=[]
	if (scalefactor <=0):
		scalefactor=1
	rivetscale = nmadgraph/(scalefactor)

	if True:
		scalefactor=nmadgraph

	for x in range(len(binning)-1):
		means.append(scalefactor*(hrivet.GetBinContent(x+1)))
		errs.append(scalefactor*(hrivet.GetBinError(x+1)))
		# print binning[x],'-',binning[x+1],'  ', means[x], '+-',errs[x]

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, 'd#sigma/d'+quantity+' [pb/GeV]']


	RivetOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	return [RivetOutputHisto,rivetscale]

def SherpaHisto(sherpafile, sherpavariable, binning,sel, label, style,original_events,normalization, nmadgraph, quantity, WRenormalizationForSherpa):

	# print sherpafile
	fsherpa = TFile.Open(sherpafile)
	tsherpa = fsherpa.Get("PhysicalVariables")
	# print "Sherpa Entries: ",tsherpa.GetEntries()
	# print "WRenorm:  ",WRenormalizationForSherpa, '--'
	Name = "MadGraph"*("MadGraph" in sherpafile) + "Pythia"*("Pythia" in sherpafile) +"Sherpa"*("Sherpa" in sherpafile)+ "PROBLEM"*("MadGraph" not in sherpafile and "Pythia" not in sherpafile)
	# print "LABELS: ", label
	# print "Label Check: ", label[0]
	# print "Var: ", sherpavariable
	if 'jet1' in sherpavariable:
		sel += j1
		print "Adding selection:",j1
	if 'jet2' in sherpavariable:
		sel += j2
		print "Adding selection:",j2
	if 'jet3' in sherpavariable:
		sel += j3
		print "Adding selection:",j3
	if 'jet4' in sherpavariable:
		sel += j4
		print "Adding selection:",j4
	if 'jet5' in sherpavariable:
		sel += j5							
		print "Adding selection:",j5
	hsherpa = CreateHisto(Name,Name,tsherpa,sherpavariable,binning,sel+'*(Pt_genmuon1>1.0)*weight_pu_central*4980*0.92*'+WRenormalizationForSherpa,style,label)
	# print 'Using Selection For Sherpa: ',sel+'*weight_pu_central*4980*0.92*'+WRenormalizationForSherpa, sherpavariable
	# print hsherpa.Integral()

	means=[]
	errs=[]
	
	sherpascale = nmadgraph/hsherpa.Integral()
	# sherpascale=1.0
	
	for x in range(len(binning)-1):
		means.append(sherpascale*(hsherpa.GetBinContent(x+1)))
		errs.append(sherpascale*(hsherpa.GetBinError(x+1)))
		# print binning[x],'-',binning[x+1],'  ', means[x], '+-',errs[x]

	if normalization==0:
		label = [label[0], 'Events/Bin']
	else:
		label = [label[0], 'd#sigma/d'+quantity+' [pb/GeV]']


	SherpaOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	return [SherpaOutputHisto,sherpascale]

# There is no built-in division for tgraphs. This does the trick. 
# For now, errors are converted into symetric errors conservatively, as one must make a choice of handling such errors. 
def DivideTGraphs_naively(gv1, gv2,style):

	[mean1,up1,down1,binset1]=gv1
	[mean2,up2,down2,binset2]=gv2

	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr = []

	for x in range(len(binset)-1):
		m1=mean1[x]
		m2=mean2[x]
		u1=up1[x]
		u2=up2[x]
		d1=down1[x]
		d2=down2[x]

		if m2 != 0:
			rat = m1/m2
		else: 
			rat = 1.0 
		if m1==0:
			rat = 1

		err_1 = max([u1,d1])
		err_2 = max([u2,d2])

		frac1 = 0
		if m1 !=0:
			frac1 = err_1/m1


		frac2 = 0
		if m2 !=0:
			frac2 = err_2/m2

		err = rat*( math.sqrt( (frac1)**2 + (frac2)**2  ))

		ratmean.append(rat)
		raterr.append(err)

		# print  m1,m2,' || ',u1,u2,' || ', d1,d2, ' || ', rat, err, ' || ',err_1, err_2,' || ', frac1, frac2


	n = 0

	return CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr,raterr,style,1.0,"SubPlot")[0]

# Using basic asymmetric errors.
def DivideTGraphs(gv1, gv2,style):
	# print gv1
	# for x in gv1:
	# 	print x
	[mean1,up1,down1,binset1]=gv1
	[mean2,up2,down2,binset2]=gv2

	# Quick hack for sys uncertainties on first dist only
	for x in range(len(up2)):
		up2[x] = 0

	for x in range(len(down2)):
		down2[x] = 0

	print  ' '
	print binset1
	print binset2
	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean1[x]
		m2=mean2[x]
		u1=up1[x]
		u2=up2[x]
		d1=down1[x]
		d2=down2[x]

		if m2 != 0:
			rat = m1/m2
		else: 
			rat = 1.0 
		if m1==0:
			rat = 1

		# print '-'*66


		u1 = m1 +u1
		u2 = m2 +u2
		d1 = m1 -d1
		d2 = m2 -d2

		if u1<0.0001:  u1 = 0.0001
		if u2<0.0001:  u2 = 0.0001
		if d1<0.0001:  d1 = 0.0001
		if d2<0.0001:  d2 = 0.0001


		possible_window_values = [u1/u2,u1/d2,d1/u2,d1/d2]
		window = [abs(rat-max(possible_window_values)), abs(rat-min(possible_window_values))]
		# print window
		# if window[1] > rat: window[1]=rat
		# if window[0] > 5: window[0]=5
		# print window
		# print rat, window
		ratmean.append(rat)
		raterr_up.append(window[0])
		raterr_down.append(window[1])
		# print rat
		# print [rat+window[0],rat-window[1]]
		
		yvalues+= [rat+window[0],rat-window[1]]


	yup = round((1.2*max(yvalues)),2)
	ydown = round((0.8*min(yvalues)),2)
	if yup>5: yup=5
	# print ratmean
	# print raterr_up
	# print raterr_down

	# print yvalues
	# print [yup,ydown]

	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]


# This creates the final "results"-style plot!
def FinalHisto(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalization,sel):

	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.53, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.28, 1.0, 0.50 )
	pad3 = TPad( 'pad3', 'pad3', 0.0, 0.03, 1.0, 0.25 )


	pad1.Draw()
	pad2.Draw()
	pad3.Draw()

	pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	gStyle.SetOptStat(0)
	MadGraphStyle=[1001,20,.00001,1,4]
	MadGraphSubStyle=[3254,21,.7,1,4]

	MadGraphRivetSubStyle=[0*3004+3254,21,.7,1,6]

	SherpaStyle=[0*3004+1001,20,.00001,1,6]

	SherpaRivetStyle=[0*3004+1001,20,.00001,1,6]

	MadGraphRivetStyle=[0*3004+1001,20,.00001,1,6]

	DataRecoStyle=[0,20,.7,1,1]	
	
	rivetname = (filename.split('/')[-1]).split('FINAL')[0]
	standardname= (filename.split('/')[-1]).split('FINAL')[0]
	# print "USING  VARIABLE:  ",standardname

	for x in RivetBranchMap:
		if x[0] in rivetname:
			rivetname = rivetname.replace(x[0],x[1])

	for x in GenBranchMap:
		if x[0] in standardname:
			standardname=standardname.replace(x[0],x[1])
	
	madgraph_NOriginal = float(((RIVETMadGraph.split('/')[-1]).split('NEvents_')[-1]).split('.root')[0])
	sherpa_NOriginal   = float(((RIVETSherpa.split('/')[-1]).split('NEvents_')[-1]).split('.root')[0])

	# print 'Rivet Origianl Events: '  , madgraph_NOriginal
	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1' or rivetname=='etajet1':
	# 	print 'NJET FOUND ' + '*'*50
	
	rivetlabel=label	
	
	Max = max(measurement)*10
	Min = min(measurement)*.5
	
	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, 'd#sigma/d'+quantity+' [pb/GeV]']
		Max=Max/normalization
		Min=Min/normalization
	
	for x in range(len(expectation_names)):
		name = expectation_names[x]
		mean_value = expectation_means[x]
		plus_errors = expectation_errors[x]
		minus_errors = expectation_errors[x]
		style=MadGraphStyle
		[Exp,Exp_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")

		Exp.SetMaximum(Max)
		Exp.SetMinimum(Min)

		if x==0:
			Exp.Draw("A2")
		else:
			Exp.Draw("2")
	nmadgraph = sum(Exp_verbose[0])


	# print 'MG: ',nmadgraph

	# print Exp_verbose[0]
	# [[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,"(ptmuon>45)*(abs(etamuon)<2.1)",rivetlabel,MadGraphRivetStyle,madgraph_NOriginal,normalization,nmadgraph,quantity,WRenormalization)

	# sel = "1"


	for nn in range(6):
		nn+=2
		if 'pfjet'+str(nn) in standardname:
			exec ('sel+=j'+str(nn-1))


	# print "Using Sel",sel
	# print 'Starting with WRenorm: ',WRenormalization
	# if 'Count' in standardname:
	# 	nmadgraph -= Exp_verbose[0][0]
	# print 'MG: ',nmadgraph

	# [[Sherpa_Result,Sherpa_Result_verbose], sherparescale]                = SherpaHisto(SHERPAFILE,standardname,binning,sel,label,SherpaStyle,madgraph_NOriginal,normalization,nmadgraph,quantity,WRenormalization)
	[[Rivet_Sherpa_Result,Rivet_Sherpa_Result_verbose], sherparescale]     = RivetHisto(RIVETSherpa,rivetname,binning,"(evweight)*(mt_mumet>50)*(ptmuon>45)*(abs(etamuon)<2.1)",rivetlabel,SherpaRivetStyle,sherpa_NOriginal,normalization,nmadgraph,quantity,WRenormalization)

	
	name="Measured"
	mean_value = measurement
	plus_errors=measurement_error_up
	minus_errors=measurement_error_down
	style=DataRecoStyle
	[Meas,Meas_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")
	# print Meas_verbose[0]

	fplot = TFile.Open(filename+'root',"RECREATE")
	Meas.Write("Meas")
	Exp.Write("Exp")
	fplot.Close()

	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1'or rivetname=='etajet1':
	Rivet_Sherpa_Result.Draw("2")
	Meas.Draw("P")

	# FixDrawLegend(c1.cd(1).BuildLegend())

	leg = TLegend(0.63,0.68,0.89,0.88,"","brNDC");
	leg.SetTextFont(132);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(Meas,"Data (Unfolded)");
	leg.AddEntry(Exp,"MadGraph (From AOD)");
	# leg.AddEntry(Rivet_MadGraph_Result,"MadGraph (Rivet)");
	leg.AddEntry(Rivet_Sherpa_Result,"Sherpa (GEN/RIVET)");


	leg.Draw()

	
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2011  "+sqrts)
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.08)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.6,0.60,"PRELIMINARY")
	if True:
		# l2.DrawLatex(0.6,0.50,"R_{Rivet} = "+ str(round(rivetrescale,3)))
		l2.DrawLatex(0.6,0.50,"R_{Sherpa} = "+ str(round(sherparescale,3)))



	pad2.cd()
	pad2.SetGrid()
	pad2.Draw()

	[grat,[gratup,gratdown]] = DivideTGraphs(Meas_verbose,Exp_verbose,MadGraphSubStyle)
	unity=TLine(grat.GetXaxis().GetXmin(), 1.0 , grat.GetXaxis().GetXmax(),1.0)

	grat.SetMinimum(gratdown)
	grat.SetMaximum(gratup)


	grat.Draw("ap2SAME")


	unity.Draw("SAME")

	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1'or rivetname=='etajet1':

	pad3.cd()
	pad3.SetGrid()
	pad3.Draw()

	# grat2 = DivideTGraphs(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)

	[grat2,[grat2up,grat2down]] = DivideTGraphs(Meas_verbose,Rivet_Sherpa_Result_verbose,MadGraphRivetSubStyle)


	grat2.SetMinimum(grat2down)
	grat2.SetMaximum(grat2up)
	grat2.Draw("ap2")
	unity.Draw("SAME")

	c1.Print(filename+'pdf')
	c1.Print(filename+'png')

	# if 'jet1' in filename:
	# sys.exit()

# def GetTGraphContent(g):
# 	n =  g.GetN()
# 	for x in range(n):
# 		print ' *  ',g.GetX(n)

# 	return 0

def MakeOutputPlot(F,T,S,J):
	c1 = TCanvas("c1","",500,500)
	print '\n\n'
	print F
	print T
	print S
	print J

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.55, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.05, 1.0, 0.5 )
	MadGraphSubStyle=[3254,21,.7,1,4]

	unity=TLine(T[-1][0], 1.0 , T[-1][-1],1.0)

	xlabel = 'testlabel'

	if 'DeltaPhi_pfjet1muon1' in F: xlabel =  "Deltaphi(jet_{1},#mu)"
	if 'DeltaPhi_pfjet2muon1' in F: xlabel =  "Deltaphi(jet_{2},#mu)"
	if 'DeltaPhi_pfjet3muon1' in F: xlabel =  "Deltaphi(jet_{3},#mu)"
	if 'DeltaPhi_pfjet4muon1' in F: xlabel =  "Deltaphi(jet_{4},#mu)"
	if 'DeltaPhi_pfjet5muon1' in F: xlabel =  "Deltaphi(jet_{5},#mu)"
	if 'Pt_pfjet1' in F: xlabel =  "p_{T}(jet_{1})[GeV]"
	if 'Pt_pfjet2' in F: xlabel =  "p_{T}(jet_{2})[GeV]"
	if 'Pt_pfjet3' in F: xlabel =  "p_{T}(jet_{3})[GeV]"
	if 'Pt_pfjet4' in F: xlabel =  "p_{T}(jet_{4})[GeV]"
	if 'Pt_pfjet5' in F: xlabel =  "p_{T}(jet_{5})[GeV]"
	if 'PFJet30Count' in F: xlabel =  "N_{Jet}"
	if 'MT_muon1MET' in F: xlabel =  "M_{T}(#mu,E_{T}^{miss})[GeV]"
	if 'Pt_MET' in F: xlabel =  "E_{T}^{miss}[GeV]"
	if 'Eta_pfjet1' in F: xlabel =  "eta(jet_{1})"
	if 'Eta_pfjet2' in F: xlabel =  "eta(jet_{2})"
	if 'Eta_pfjet3' in F: xlabel =  "eta(jet_{3})"
	if 'Eta_pfjet4' in F: xlabel =  "eta(jet_{4})"
	if 'Eta_pfjet5' in F: xlabel =  "eta(jet_{5})"


	pad1.Draw()
	pad2.Draw()

	pad1.SetGrid()
	# pad1.SetLogy()
	pad1.cd()

	# T.Print()
	[grat,[gratup,gratdown]] = DivideTGraphs(T,S,MadGraphSubStyle)
	grat.GetYaxis().SetTitle('TCHPT / SSVHPT')
	grat.GetXaxis().SetTitle(xlabel)


	grat.GetYaxis().SetTitleFont(132);
	grat.GetXaxis().SetTitleSize(.08);
	grat.GetYaxis().SetTitleSize(.08);
	grat.GetXaxis().CenterTitle();
	grat.GetYaxis().CenterTitle();		
	grat.GetXaxis().SetTitleOffset(.85);
	grat.GetYaxis().SetTitleOffset(.5);
	grat.GetYaxis().SetLabelSize(.06);
	grat.GetXaxis().SetLabelSize(.06);

	grat.SetMaximum(gratup)
	grat.SetMinimum(gratdown)

	grat.Draw("ap2SAME")
	unity.Draw("SAME")

	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2011  "+sqrts)
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.08)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.7,0.94,"PRELIMINARY")



	pad2.SetGrid()
	# pad2.SetLogy()
	pad2.cd()

	[grat2,[gratup2,gratdown2]] = DivideTGraphs(T,J,MadGraphSubStyle)
	grat2.GetYaxis().SetTitle('TCHPT / JPT')
	grat2.GetXaxis().SetTitle(xlabel)

	grat2.GetYaxis().SetTitleFont(132);
	grat2.GetXaxis().SetTitleSize(.08);
	grat2.GetYaxis().SetTitleSize(.08);
	grat2.GetXaxis().CenterTitle();
	grat2.GetYaxis().CenterTitle();		
	grat2.GetXaxis().SetTitleOffset(.85);
	grat2.GetYaxis().SetTitleOffset(.5);
	grat2.GetYaxis().SetLabelSize(.06);
	grat2.GetXaxis().SetLabelSize(.06);
	grat2.SetMaximum(gratup2)
	grat2.SetMinimum(gratdown2)
	grat2.Draw("ap2SAME")
	unity.Draw("SAME")

	F=F.replace('.','_')
	F=F.replace('_txt','.txt')
	F=F.replace('_TGraphContent','')
	outname = F.replace('.txt','_btagComparison.png')
	outname = F.replace('.txt','_btagComparison.pdf')

	c1.Print(outname)


main()


