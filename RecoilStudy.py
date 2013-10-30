import os
import sys
(sys.argv).append('-b')
from ROOT import *
from array import array
import math 

gROOT.SetStyle('Plain')
gStyle.SetOptTitle(0)



binning = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,110,120,130,140,150,170,200,250,400]
binning = [0,5,10,15,20,25,30,35,40,45,50]
binning = [0 + (n)*10 for n in range(8)]
binning = [0,5,10,15,20,25,30,35,40,50,60,70,80,100]
print binning

binpairs = [ [binning[n], binning[n+1]]  for n in range(len(binning)-1) ]

bincenters = [ 0.5*(binning[n] + binning[n+1])   for n in range(len(binning)-1) ]

print binpairs
print bincenters

fz = 'NTupleAnalyzer_V00_02_06_WPlusJets_RecoilTest2_2013_07_08_23_05_38/SummaryFiles/ZJets_MG.root'
fd = 'NTupleAnalyzer_V00_02_06_WPlusJets_RecoilTest2_2013_07_08_23_05_38/SummaryFiles/SingleMuData.root'
fw = 'NTupleAnalyzer_V00_02_06_WPlusJets_RecoilTest2_2013_07_08_23_05_38/SummaryFiles/WJets_MG.root'
# fz = 'NTupleAnalyzer_V00_02_06_WPlusJets_RecoilTest_2013_07_08_21_13_05/NTupleAnalyzer_V00_02_06_WPlusJets_DYJetsToLL_TuneZ2_M_50_7TeV_madgraphpart70of84.root'


selection_z = '(Pt_muon1>25)*(abs(Eta_muon1)<2.1)*(Pt_muon2>25)*(abs(Eta_muon2)<2.1)*(IsoMu24Pass>0)'
selection_w = '(Pt_muon1>25)*(abs(Eta_muon1)<2.1)*(Pt_muon2<0.0001)*(abs(Eta_muon2)<2.1)*(IsoMu24Pass>0)'


tz = TFile.Open(fz,"READ").Get("PhysicalVariables")
td = TFile.Open(fd,"READ").Get("PhysicalVariables")
tw = TFile.Open(fw,"READ").Get("PhysicalVariables")


to = TFile.Open("RecoilStudy.root","RECREATE")

# tz = _tz.CopyTree(selection_z)
# td = _td.CopyTree(selection_z)
# tw = _tw.CopyTree(selection_z)

print ' -- Entry Breakdown --'
print '    Z: ',tz.GetEntries()
print ' Data: ',td.GetEntries()
print '    W: ',tw.GetEntries()

rU1 = ("1.33223-0.917782*x")
rU2 = ("-0.013")
sU1 = ("11.1566+0.0654529*x+0.000124436*x*x")
sU2 = ("11.1235+0.0449872*x-6.39822e-5*x*x")
rMCU1 = ("1.26247-0.950094*x")
rMCU2 = ("-0.00544907")
sMCU1 = ("10.6449+0.0436475*x+3.07554e-5*x*x")
sMCU2 = ("10.5649+0.0225853*x-5.81371e-5*x*x")

MariaD = [rU1,sU1,rU2,sU2]
MariaZ = [rMCU1,sMCU1,rMCU2,sMCU2]


def GetBins(t,_type):

	if _type!= 'Z' and _type!='W' and _type!='D':
		print ' Must specify either Z/D or W mode of computation.'
		sys.exit()

	N = t.GetEntries()
	if N > 100000:
		N = 100000
	UInfo = []
	for n in range(N):

		if n%1000==0:
			print 'Procesing event',n, 'of', N # where we are in the loop...		
		t.GetEntry(n)

		if _type=='Z' or _type=='D':
			if t.Pt_muon1 <25.0: continue
			if t.Pt_muon2 <1.0: continue
			# if t.Pt_pfjet2 < 30.0: continue
			if abs(t.Eta_muon1)>2.1: continue 
			if abs(t.Eta_muon2)>2.1: continue 
			if t.IsoMu24Pass < 1: continue
			if t.M_muon1muon2 <80.0: continue
			if t.M_muon1muon2 > 110: continue
			UInfo.append([t.Pt_Z,t.U1_Z,t.U2_Z])

		if _type=='W':
			if t.Pt_muon1 <25.0: continue
			if t.Pt_muon2 >.01: continue
			# if t.Pt_pfjet2 < 30.0: continue			
			if abs(t.Eta_muon1)>2.1: continue 
			if t.IsoMu24Pass < 1: continue
			if t.MT_muon1MET < 50.0: continue
			UInfo.append([t.Pt_W,t.U1_W,t.U2_W])


	means1 = []
	widths1 = []
	means2 = []
	widths2 = []

	for b in binpairs:
		print 'Processing bin:',b,
		_u1 = []
		_u2 = []
		for iu in UInfo:
			if iu[0] >= b[0]:
				if iu[0] <= b[1]:
					_u1.append(iu[1])
					_u2.append(iu[2])
		h1 = TH1F('h1','h1',100,min(_u1),max(_u1))
		h2 = TH1F('h2','h2',100,min(_u2),max(_u2))



		for v in _u1:
			h1.Fill(v)
		for v in _u2:
			h2.Fill(v)

		print '  -- ', len(_u1),' events.'


		c1 = TCanvas("c1","",1500,700)
		c1.Divide(2,1)

		c1.cd(1)
		h1.Draw()
		f1 = TF1("f1","gaus",min(_u1),max(_u1))
		h1.Fit("f1")

		c1.cd(2)
		f2 = TF1("f2","gaus",min(_u2),max(_u2))
		h2.Fit("f2")

		binmarg = ('__'+str(b[0])+'__'+str(b[1])).replace('.','p')
		c1.Print('recoilplots/Gaus'+_type+binmarg+'.pdf')

		print '   U1  Mean: ',([f1.GetParameter(1), f1.GetParError(1)])
		print '   U1 Width: ',([f1.GetParameter(2), f1.GetParError(2)])
		print '   U2  Mean: ',([f2.GetParameter(1), f2.GetParError(1)])
		print '   U2 Width: ',([f2.GetParameter(2), f2.GetParError(2)])

		means1.append([f1.GetParameter(1), f1.GetParError(1)])
		widths1.append([f1.GetParameter(2), f1.GetParError(2)])
		means2.append([f2.GetParameter(1), f2.GetParError(1)])
		widths2.append([f2.GetParameter(2), f2.GetParError(2)])


	return [means1,widths1,means2,widths2]





# All binning is passed as variable binning. This converts constant to variable.
def ConvertBinning(_binning):
	binset=[]
	if len(_binning)==3:
		for x in range(binning[0]+1):
			binset.append(((_binning[2]-_binning[1])/(1.0*_binning[0]))*x*1.0+_binning[1])
	else:
		binset=_binning
	return binset


# Take a given binning, and means with errors, and create a TGraphAsymErrors output.
def CreateHistoFromLists(name, ylabel,xlabel, content, style):

	binset=ConvertBinning(binning)
	n = len(binset)-1
	htest= TH1D('htest','htest',n,array('d',binset))

	mean = []
	up = []
	down = []

	for a in range(len(content)):
		mean.append(content[a][0])
		up.append(content[a][1])
		down.append(content[a][1])

	X = []
	Y = []
	Xplus=[]
	Xminus=[]
	Yplus=[]
	Yminus=[]

	N=1.0

	for x in range(len(binset)-1):
		c = htest.GetBinCenter(x+1)
		d = 0.5*htest.GetBinWidth(x+1)
		center = mean[x]
		upper = up[x]
		lower=down[x]
		
		# test fix
		if abs(center) < 0.0000001:
			center = 999999999

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
	hout.GetXaxis().SetTitle(xlabel)
	hout.GetYaxis().SetTitle(ylabel)
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

	return hout




def FourPlot( variables, labels, xlabel, figtitle,compfigs ):

	docomp = False
	if len(compfigs)>1:
		docomp = True
		[Mu1m,Mu1s,Mu2m,Mu2s] = compfigs

	[u1m,u1s,u2m,u2s] = variables
	[Lu1m,Lu1s,Lu2m,Lu2s] = labels


	style=[1,21,1.0,1,4]

	hu1m = CreateHistoFromLists('hu1m', Lu1m, xlabel, u1m, style)
	hu1s = CreateHistoFromLists('hu1s', Lu1s, xlabel, u1s, style)
	hu2m = CreateHistoFromLists('hu2m', Lu2m, xlabel, u2m, style)
	hu2s = CreateHistoFromLists('hu2s', Lu2s, xlabel, u2s, style)

	fu1m = TF1("fu1m","([0] +[1]*x)",binning[0],binning[-1])
	fu1s = TF1("fu1s","([0] +[1]*x +[2]*x*x)",binning[0],binning[-1])
	fu2m = TF1("fu2m","([0])",binning[0],binning[-1])
	fu2s = TF1("fu2s","([0] +[1]*x +[2]*x*x)",binning[0],binning[-1])

	if docomp:
		Fu1m = TF1("Fu1m",Mu1m,binning[0],binning[-1])
		Fu1s = TF1("Fu1s",Mu1s,binning[0],binning[-1])
		Fu2m = TF1("Fu2m",Mu2m,binning[0],binning[-1])
		Fu2s = TF1("Fu2s",Mu2s,binning[0],binning[-1])
		Fu1m.SetLineColor(8)
		Fu1m.SetLineStyle(2)
		Fu1s.SetLineColor(8)
		Fu1s.SetLineStyle(2)
		Fu2m.SetLineColor(8)
		Fu2m.SetLineStyle(2)
		Fu2s.SetLineColor(8)
		Fu2s.SetLineStyle(2)

	c1 = TCanvas("c1","",1500,1000)
	c1.Divide(2,2)


	c1.cd(1)
	hu1m.Draw("AP")
	hu1m.Fit("fu1m")
	if docomp: Fu1m.Draw("SAME")
	lu1m=TLatex()
	lu1m.SetTextAlign(12)
	lu1m.SetTextFont(42)
	lu1m.SetNDC()
	lu1m.SetTextSize(0.05)
	lu1m.DrawLatex(0.15,0.85,' Y = ('+str(round(fu1m.GetParameter(0),5))+') + ('+str(round(fu1m.GetParameter(1),5))+')X')
	lu1m_func = '('+str(round(fu1m.GetParameter(0),5))+') + ('+str(round(fu1m.GetParameter(1),5))+')*x'

	c1.cd(2)
	hu1s.Draw("AP")
	hu1s.Fit("fu1s")
	if docomp: Fu1s.Draw("SAME")	
	lu1s=TLatex()
	lu1s.SetTextAlign(12)
	lu1s.SetTextFont(42)
	lu1s.SetNDC()
	lu1s.SetTextSize(0.05)
	lu1s.DrawLatex(0.15,0.85,' Y = ('+str(round(fu1s.GetParameter(0),5))+') + ('+str(round(fu1s.GetParameter(1),5))+')X + ('+str(round(fu1s.GetParameter(2),5))+')X^{2}' )
	lu1s_func = '('+str(round(fu1s.GetParameter(0),5))+') + ('+str(round(fu1s.GetParameter(1),5))+')*x + ('+str(round(fu1s.GetParameter(2),5))+')*x*x' 

	c1.cd(3)
	hu2m.Draw("AP")
	hu2m.Fit("fu2m")
	if docomp: Fu2m.Draw("SAME")	
	lu2m=TLatex()
	lu2m.SetTextAlign(12)
	lu2m.SetTextFont(42)
	lu2m.SetNDC()
	lu2m.SetTextSize(0.05)
	lu2m.DrawLatex(0.15,0.85,' Y = ('+str(round(fu2m.GetParameter(0),5))+')')
	lu2m_func = '('+str(round(fu2m.GetParameter(0),5))+')'

	c1.cd(4)
	hu2s.Draw("AP")
	hu2s.Fit("fu2s")
	if docomp: Fu2s.Draw("SAME")	
	lu2s=TLatex()
	lu2s.SetTextAlign(12)
	lu2s.SetTextFont(42)
	lu2s.SetNDC()
	lu2s.SetTextSize(0.05)
	lu2s.DrawLatex(0.15,0.85,' Y = ('+str(round(fu2s.GetParameter(0),5))+') + ('+str(round(fu2s.GetParameter(1),5))+')X + ('+str(round(fu2s.GetParameter(2),5))+')X^{2}')
	lu2s_func = '('+str(round(fu2s.GetParameter(0),5))+') + ('+str(round(fu2s.GetParameter(1),5))+')*x + ('+str(round(fu2s.GetParameter(2),5))+')*x*x'

	c1.Print('recoilplots/'+figtitle+'.pdf')
	c1.Print('recoilplots/'+figtitle+'.png')

	return [lu1m_func,lu1s_func,lu2m_func,lu2s_func]


[UZ1_m, UZ1_s, UZ2_m, UZ2_s] = GetBins(tz,'Z')
[UD1_m, UD1_s, UD2_m, UD2_s] = GetBins(td,'D')
[UW1_m, UW1_s, UW2_m, UW2_s] = GetBins(tw,'W')


_zfunc = FourPlot([UZ1_m, UZ1_s, UZ2_m, UZ2_s],['U_{1}^{Z MC} Response (GeV)','U_{1}^{Z MC} Resolution (GeV)','U_{2}^{Z MC} Response (GeV)','U_{2}^{Z MC} Resolution (GeV)'],"p_{T}^{Z} (GeV)","Z_MC_Recoil",MariaZ)
_dfunc = FourPlot([UD1_m, UD1_s, UD2_m, UD2_s],['U_{1}^{Z Data} Response (GeV)','U_{1}^{Z Data} Resolution (GeV)','U_{2}^{Z Data} Response (GeV)','U_{2}^{Z Data} Resolution (GeV)'],"p_{T}^{Z} (GeV)","Z_Data_Recoil",MariaD)
_wfunc = FourPlot([UW1_m, UW1_s, UW2_m, UW2_s],['U_{1}^{W MC} Response (GeV)','U_{1}^{W MC} Resolution (GeV)','U_{2}^{W MC} Response (GeV)','U_{2}^{W MC} Resolution (GeV)'],"p_{T}^{W} (GeV)","W_MC_Recoil",[])



def CompPlot( _maria_d, _maria_z, _darin_d, _darin_z ):

	
	[Mu1m_z,Mu1s_z,Mu2m_z,Mu2s_z] = _maria_z
	[Mu1m_d,Mu1s_d,Mu2m_d,Mu2s_d] = _maria_d
	[Du1m_z,Du1s_z,Du2m_z,Du2s_z] = _darin_z
	[Du1m_d,Du1s_d,Du2m_d,Du2s_d] = _darin_d

	Mu1m = '('+Mu1m_d+')/('+Mu1m_z+')'
	Du1m = '('+Du1m_d+')/('+Du1m_z+')'

	Mu1s = '('+Mu1s_d+')/('+Mu1s_z+')'
	Du1s = '('+Du1s_d+')/('+Du1s_z+')'

	Mu2m = '('+Mu2m_d+')/('+Mu2m_z+')'
	Du2m = '('+Du2m_d+')/('+Du2m_z+')'

	Mu2s = '('+Mu2s_d+')/('+Mu2s_z+')'
	Du2s = '('+Du2s_d+')/('+Du2s_z+')'


	style=[1,21,1.0,1,4]



	Fu1m = TF1("Fu1m",Mu1m,binning[0],binning[-1])
	Fu1s = TF1("Fu1s",Mu1s,binning[0],binning[-1])
	Fu2m = TF1("Fu2m",Mu2m,binning[0],binning[-1])
	Fu2s = TF1("Fu2s",Mu2s,binning[0],binning[-1])
	Fu1m.SetLineColor(8)
	Fu1m.SetLineStyle(2)
	Fu1s.SetLineColor(8)
	Fu1s.SetLineStyle(2)
	Fu2m.SetLineColor(8)
	Fu2m.SetLineStyle(2)
	Fu2s.SetLineColor(8)
	Fu2s.SetLineStyle(2)


	Gu1m = TF1("Gu1m",Du1m,binning[0],binning[-1])
	Gu1s = TF1("Gu1s",Du1s,binning[0],binning[-1])
	Gu2m = TF1("Gu2m",Du2m,binning[0],binning[-1])
	Gu2s = TF1("Gu2s",Du2s,binning[0],binning[-1])
	# Gu1m.SetLineColor(8)
	# Gu1m.SetLineStyle(2)
	# Gu1s.SetLineColor(8)
	# Gu1s.SetLineStyle(2)
	# Gu2m.SetLineColor(8)
	# Gu2m.SetLineStyle(2)
	# Gu2s.SetLineColor(8)
	# Gu2s.SetLineStyle(2)

	c1 = TCanvas("c1","",1500,1000)
	c1.Divide(2,2)


	c1.cd(1)
	Gu1m.Draw("")
	Gu1m.GetHistogram().SetMinimum(0.5)
	Gu1m.GetHistogram().SetMaximum(1.5)

	Fu1m.Draw("SAME")
	lu1m=TLatex()
	lu1m.SetTextAlign(12)
	lu1m.SetTextFont(42)
	lu1m.SetNDC()
	lu1m.SetTextSize(0.05)
	lu1m.DrawLatex(0.15,0.85,' U1 Recoil SF ')

	c1.cd(2)
	Gu1s.Draw("")
	Gu1s.GetHistogram().SetMinimum(0.7)
	Gu1s.GetHistogram().SetMaximum(1.5)	
	Fu1s.Draw("SAME")	
	lu1s=TLatex()
	lu1s.SetTextAlign(12)
	lu1s.SetTextFont(42)
	lu1s.SetNDC()
	lu1s.SetTextSize(0.05)
	lu1s.DrawLatex(0.15,0.85,' U1 Resolution SF ' )

	c1.cd(3)
	Gu2m.Draw("")
	Gu2m.GetHistogram().SetMinimum(-9.1)
	Gu2m.GetHistogram().SetMaximum(9.1)	
	Fu2m.Draw("SAME")	
	lu2m=TLatex()
	lu2m.SetTextAlign(12)
	lu2m.SetTextFont(42)
	lu2m.SetNDC()
	lu2m.SetTextSize(0.05)
	lu2m.DrawLatex(0.15,0.85,' U2 Recoil SF ')

	c1.cd(4)
	Gu2s.Draw("")
	Gu2s.GetHistogram().SetMinimum(0.8)
	Gu2s.GetHistogram().SetMaximum(2.0)	
	Fu2s.Draw("SAME")	
	lu2s=TLatex()
	lu2s.SetTextAlign(12)
	lu2s.SetTextFont(42)
	lu2s.SetNDC()
	lu2s.SetTextSize(0.05)
	lu2s.DrawLatex(0.15,0.85,' U2 Resolution SF ')

	c1.Print('recoilplots/SFComparison.pdf')
	c1.Print('recoilplots/SFComparison.png')

CompPlot(MariaD,MariaZ,_dfunc,_zfunc)













# def SimpleVector(pt,phi):
# 	v = TLorentzVector()
# 	v.SetPtEtaPhiM(pt,0.0,phi,0.0)
# 	return v

# def GetRecoils(atree):
# 	info = []
# 	for n in range(atree.GetEntries()):
# 		atree.GetEntry(n)

# 		l1 = TLorentzVector(atree.Pt_muon1, atree.Phi_muon1)
# 		l2 = TLorentzVector(atree.Pt_muon2, atree.Phi_muon2)
# 		met = TLorentzVector(atree.Pt_MET, atree.Phi_MET)
# 		zero = SimpleVector(0.0,0.0)
# 		U = (zero - met - l1 -l2)
# 		Z = (l1 + l2)

# 		dphi = U.DeltaPhi(Z)
# 		u1 = U.Pt()*cos(dphi)
# 		u2 = U.Pt()*sin(dphi)
# 		info.append( [u1,u2,Z.Pt()] )
# 	return info

# def TGraphFromList(inlist,xplace,yplace,name,xname,yname,f0,f1,f2,globalscale):
# 	n = 0
# 	X = []
# 	Y = []
# 	for m in range(len(inlist)):
# 		n += 1
# 		_xx = 1.0*inlist[m][xplace]
# 		_yy = 1.0*inlist[m][yplace]
# 		yy = f0 + f1*_xx + f2*_xx*_xx
# 		yy = abs(yy - _yy)
# 		yy *= globalscale
# 		_yy *= globalscale

# 		X.append(_xx)
# 		if 'res' in name:
# 			Y.append(yy)
# 		else:
# 			Y.append(_yy)

# 	X = array("d", X)
# 	Y = array("d", Y)
# 	hout = TGraph(n,X,Y)
# 	hout.SetTitle(name)

# 	style = [0,1,1,0,1]

# 	hout.SetFillStyle(style[0])
# 	hout.SetMarkerStyle(style[1])
# 	# hout.SetMarkerSize(style[2])
# 	hout.SetLineWidth(style[3])
# 	hout.SetMarkerColor(style[4])
# 	hout.SetLineColor(style[4])
# 	hout.SetFillColor(style[4])
# 	hout.SetFillColor(style[4])
# 	hout.GetXaxis().SetTitle(xname)
# 	hout.GetYaxis().SetTitle(yname)
# 	hout.GetXaxis().SetTitleFont(42)
# 	hout.GetYaxis().SetTitleFont(42)
# 	hout.GetXaxis().SetLabelFont(42)
# 	hout.GetYaxis().SetLabelFont(42)

# 	return hout

# print 'Compiling MC Lists'
# mc = GetRecoils(tz)
# print 'Compiling data Lists'
# data = GetRecoils(td)

# print 'Getting U1 Data'
# u1data = TGraphFromList(data,2,0,'u1data',"Z p_{T} (GeV)","U_{1} (GeV) [Data]",0.,1.,0.,1.)
# print 'Getting U2 Data'
# u2data = TGraphFromList(data,2,1,'u2data',"Z p_{T} (GeV)","U_{2} (GeV) [Data]",0.,1.,0.,1.)
# print 'Getting U1 MC'
# u1mc = TGraphFromList(mc,2,0,'u1mc',"Z p_{T} (GeV)","U_{1} (GeV) [Z MC]",0.,1.,0.,1.)
# print 'Getting U1 MC'
# u2mc = TGraphFromList(mc,2,1,'u2mc',"Z p_{T} (GeV)","U_{2} (GeV) [Z MC]",0.,1.,0.,1.)




# def UDrawFit(scatter):
# 	ft = TF1("ft","[1]*x + [0]", 0,1000 ) 
# 	scatter.Draw("AP")
# 	scatter.Fit("ft")
# 	scatter.GetFunction("ft").SetLineColor(2)
# 	scatter.GetFunction("ft").SetLineWidth(1)
# 	print str(ft.GetParameter(0))+' + '+str(ft.GetParameter(1))+'*x'
# 	return [ft.GetParameter(0),ft.GetParameter(1)]

# def UDrawFit2(scatter):
# 	ft2 = TF1("ft2","[2]*x*x + [1]*x + [0]", 0,1000 ) 
# 	scatter.Draw("AP")
# 	scatter.Fit("ft2")
# 	scatter.GetFunction("ft2").SetLineColor(2)
# 	scatter.GetFunction("ft2").SetLineWidth(1)
# 	print str(ft2.GetParameter(0))+' + '+str(ft2.GetParameter(1))+'*x + '+str(ft2.GetParameter(2))+'*x*x'

# 	return [ft2.GetParameter(0),ft2.GetParameter(1),ft2.GetParameter(2)]

# c1 = TCanvas("c1","",1500,1000)
# c1.Divide(2,2)
# c1.cd(1)
# u1datafit =  UDrawFit(u1data)
# c1.cd(2)
# u1mcfit =  UDrawFit(u1mc)
# c1.cd(3)
# u2datafit =  UDrawFit(u2data)
# c1.cd(4)
# u2mcfit =  UDrawFit(u2mc)
# c1.Print('recoilplots/recoil.pdf')
# c1.Print('recoilplots/recoil.png')


# constant = 0.5*(math.sqrt(2.0*3.1415926))

# print 'Getting U1 Data Resolution'
# u1datares = TGraphFromList(data,2,0,'u1datares',"Z p_{T} (GeV)","U_{1} #sigma (GeV) [Data]",u1datafit[0],u1datafit[1],0.,constant)
# print 'Getting U2 Data Resolution'
# u2datares = TGraphFromList(data,2,1,'u2datares',"Z p_{T} (GeV)","U_{2} #sigma (GeV) [Data]",u2datafit[0],u2datafit[1],0.,constant)
# print 'Getting U1 MC Resolution'
# u1mcres = TGraphFromList(mc,2,0,'u1mcres',"Z p_{T} (GeV)","U_{1} #sigma (GeV)  [Z MC]",u1mcfit[0],u1mcfit[1],0.,constant)
# print 'Getting U1 MC Resolution'
# u2mcres = TGraphFromList(mc,2,1,'u2mcres',"Z p_{T} (GeV)","U_{2} #sigma (GeV) [Z MC]",u2mcfit[0],u2mcfit[1],0.,constant)


# c2 = TCanvas("c2","",1500,1000)
# c2.Divide(2,2)
# c2.cd(1)
# u1datafitres =  UDrawFit2(u1datares)
# c2.cd(2)
# u1mcfitres =  UDrawFit2(u1mcres)
# c2.cd(3)
# u2datafitres =  UDrawFit2(u2datares)
# c2.cd(4)
# u2mcfitres =  UDrawFit2(u2mcres)
# c2.Print('recoilplots/recoilres.pdf')
# c2.Print('recoilplots/recoilres.png')
