import os
from glob import glob
# Directory where root files are kept and the tree you want to get root files from. Normal is for standard analysis, the jet rescaling, jet smearing, muon PT rescaling ,and muon PT smearing. 
from datetime import datetime

startTime = datetime.now()

#Current AFS Working Directory and eos directory for ntuples
afsdir = '/afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_4_2_8/src/WJetsAnalysis/'
eosdir = '/store/group/phys_smp/WPlusJets/AnalyzerOutput/Nov30/'
eosdir = '/store/group/phys_smp/WPlusJets/AnalyzerOutput/Jan31BTagFix/'

# Set of all ntuples

# NormalDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov29_2013_11_29_02_23_44/SummaryFiles"
# JetScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov29_JetScaleDown_2013_11_29_03_30_30/SummaryFiles"
# JetScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov29_JetScaleUp_2013_11_29_02_59_03/SummaryFiles"
# JetSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct9_JetSmear_2013_10_09_23_57_33/SummaryFiles"
# PhiCorrDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct9_MetPhiMod_2013_10_10_00_54_16/SummaryFiles"
# MuScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct9_MuScaleDown_2013_10_09_23_15_51/SummaryFiles"
# MuScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct9_MuScaleUp_2013_10_09_22_53_04/SummaryFiles"
# MuSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct9_MuSmear_2013_10_10_00_35_04/SummaryFiles"

# NormalDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_2013_11_29_20_25_02/SummaryFiles"
# JetScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_JetScaleDown_2013_11_30_00_18_41/SummaryFiles"
# JetScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_JetScaleUp_2013_11_29_23_33_26/SummaryFiles"
# JetSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_JetSmear_2013_11_30_12_56_44/SummaryFiles"
# PhiCorrDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_MetPhiMod_2013_11_30_02_32_32/SummaryFiles"
# MuScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_MuScaleDown_2013_11_30_07_11_13/SummaryFiles"
# MuScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_MuScaleUp_2013_11_30_01_18_47/SummaryFiles"
# MuSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Nov30_MuSmear_2013_11_30_13_13_00/SummaryFiles"


NormalDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_2014_01_31_21_06_37/SummaryFiles"
JetScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_JetScaleDown_2014_02_01_15_49_42/SummaryFiles"
JetScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_JetScaleUp_2014_02_01_13_57_06/SummaryFiles"
JetSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_JetSmear_2014_02_02_04_56_44/SummaryFiles"
PhiCorrDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_MetPhiMod_2014_02_02_06_31_00/SummaryFiles"
MuScaleDownDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_MuScaleDown_2014_02_02_04_20_41/SummaryFiles"
MuScaleUpDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_MuScaleUp_2014_02_02_02_45_47/SummaryFiles"
MuSmearDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_MuSmear_2014_02_02_05_32_40/SummaryFiles"
NormalDirectory = eosdir+"NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Jan31BTagFix_2014_02_03_18_34_19/SummaryFiles"


# for x in [NormalDirectory,JetScaleDownDirectory,JetScaleUpDirectory,JetSmearDirectory,PhiCorrDirectory,MuScaleDownDirectory,MuScaleUpDirectory,MuSmearDirectory]:
# 	print x
# 	os.system('cmsLs '+x)
# 	print ' '
# sys.exit()

# This is the Rivet NTuple for MadGraph
# RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Madgraph_treeV3Dressed_NEvents_93671821.root'
RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Madgraph_treeV3Dressed_NEvents_93536026.root'
# RIVETMadGraphNonHad = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_ModB_treeV3Dressed_NEvents_92216218.root'
RIVETMadGraphNonHad = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_ModB_treeV3Dressed_NEvents_92213415.root'
RIVETSherpa='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Sherpa_treeV3Dressed_NEvents_685972.root'


# This maps the LQAnalyzer branch names to the Rivet branch names due to my total lack of foresight.
RivetBranchMap=[  ]

RivetBranchMap.append(['_pt20',''])
RivetBranchMap.append(['_eta2p5',''])
RivetBranchMap.append(['Eta_pfjet','etajet'])
RivetBranchMap.append(['Pt_pfjet','ptjet'])

# RivetBranchMap.append(['Phi_pfjet','phijet'])
RivetBranchMap.append(['Eta_muon1','etamuon'])
RivetBranchMap.append(['Pt_muon1','ptmuon'])
# RivetBranchMap.append(['Phi_muon1','phimuon'])
# RivetBranchMap.append(['DeltaPhi_pfjet1muon1','dphijet1muon'])
RivetBranchMap.append(['DeltaPhi_pfjet1muon1','dphijet1muon'])
RivetBranchMap.append(['DeltaPhi_pfjet2muon1','dphijet2muon'])
RivetBranchMap.append(['DeltaPhi_pfjet3muon1','dphijet3muon'])
RivetBranchMap.append(['DeltaPhi_pfjet4muon1','dphijet4muon'])
RivetBranchMap.append(['DeltaPhi_pfjet5muon1','dphijet5muon'])

# RivetBranchMap.append(['HT_pfjets','(ptjet1*(ptjet1>0))+(ptjet2*(ptjet2>0))+(ptjet3*(ptjet3>0))+(ptjet4*(ptjet4>0))'])
RivetBranchMap.append(['HT_pfjets','htjets'])


# RivetBranchMap.append(['pfjet','jet'])
# RivetBranchMap.append(['muon1','muon'])
RivetBranchMap.append(['PFJet30Count_preexc','njet_WMuNu'])
RivetBranchMap.append(['PFJet30Count','njet_WMuNu'])
RivetBranchMap.append(['MT_muon1METR','mt_mumet'])
RivetBranchMap.append(['Pt_MET','ptmet'])

# This maps the LQAnalyzer branch names to the Rivet branch names due to my total lack of foresight.
GenBranchMap=[  ]
GenBranchMap.append(['Eta_pfjet','Eta_genjet'])
GenBranchMap.append(['Pt_pfjet','Pt_genjet'])
GenBranchMap.append(['PFJet40Count','GenJet40Count'])
GenBranchMap.append(['MT_muon1METR','MT_genmuon1genMET'])
GenBranchMap.append(['Pt_MET','Pt_genMET'])

RivetGenBranchMap = []

RivetGenBranchMap.append(['HT_genjets','htjets'])
RivetGenBranchMap.append(['MT_genmuon1genMET','mt_mumet'])
RivetGenBranchMap.append(['GenJet30Count_preexc','njet_WMuNu'])
RivetGenBranchMap.append(['GenJet30Count','njet_WMuNu'])
RivetGenBranchMap.append(['Pt_genMET','ptmet'])
RivetGenBranchMap.append(['Eta_','eta'])
RivetGenBranchMap.append(['Pt_','pt'])
RivetGenBranchMap.append(['DeltaPhi_','dphi'])
RivetGenBranchMap.append(['Phi_','phi'])
RivetGenBranchMap.append(['genjet','jet'])
RivetGenBranchMap.append(['genmuon','muon'])
RivetGenBranchMap.append(['muon1','muon'])
RivetGenBranchMap.append(['weight_pu_central*4955','evweight'])



RivetGenBareBranchMap = []
RivetGenBareBranchMap.append(['HT_genjets','htjets'])
RivetGenBareBranchMap.append(['MT_genmuon1genMET_bare','mt_mumet'])
RivetGenBareBranchMap.append(['Pt_genjet1_bare','ptjet1'])
RivetGenBareBranchMap.append(['Pt_genjet2_bare','ptjet2'])
RivetGenBareBranchMap.append(['Pt_genjet3_bare','ptjet3'])
RivetGenBareBranchMap.append(['Pt_genjet4_bare','ptjet4'])
RivetGenBareBranchMap.append(['Eta_genjet1_bare','etajet1'])
RivetGenBareBranchMap.append(['Eta_genjet2_bare','etajet2'])
RivetGenBareBranchMap.append(['Eta_genjet3_bare','etajet3'])
RivetGenBareBranchMap.append(['Eta_genjet4_bare','etajet4'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet1genmuon1_bare','dphijet1muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet2genmuon1_bare','dphijet2muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet3genmuon1_bare','dphijet3muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet4genmuon1_bare','dphijet4muon1'])
RivetGenBareBranchMap.append(['Pt_genMET','ptmet'])
RivetGenBareBranchMap.append(['weight_pu_central*4955','evweight'])
RivetGenBareBranchMap.append(['Pt_genmuon1_bare','ptmuon'])
RivetGenBareBranchMap.append(['Eta_genmuon1_bare','etamuon'])



# Handy shortcuts for the tree name and common cuts used in selections
TreeName = "PhysicalVariables"

IsoMuCond = '*(IsoMu24Pass>0.5)'


#################################################################################
#############      DEFINE SELECTIONS FOR PLOTS and RESPONSE        ##############
#################################################################################

# Basic event filters
filters = '*(pass_HBHENoiseFilter*pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'
# filters = '*(pass_HBHENoiseFilter)*(N_GoodVertices>0.5)'
# filters = '*(pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'

# filters = '*(N_GoodVertices>0.5)'


# Placeholder to require additional jet
j1="*(Pt_pfjet1>30.0)*(abs(Eta_pfjet1)<2.4)"
j2="*(Pt_pfjet2>30.0)*(abs(Eta_pfjet2)<2.4)"
j3="*(Pt_pfjet3>30.0)*(abs(Eta_pfjet3)<2.4)"
j4="*(Pt_pfjet4>30.0)*(abs(Eta_pfjet4)<2.4)"
j5="*(Pt_pfjet5>30.0)*(abs(Eta_pfjet5)<2.4)"
j6="*(Pt_pfjet6>30.0)*(abs(Eta_pfjet6)<2.4)"

j1_pt20="*(Pt_pfjet1_pt20>20.0)"
j2_pt20="*(Pt_pfjet2_pt20>20.0)"
j3_pt20="*(Pt_pfjet3_pt20>30.0)"
j4_pt20="*(Pt_pfjet4_pt20>30.0)"
j5_pt20="*(Pt_pfjet5_pt20>30.0)"
j6_pt20="*(Pt_pfjet6_pt20>30.0)"

j1_le="*(abs(Eta_pfjet1_eta2p5)>0)*(abs(Eta_pfjet1_eta2p5)<2.5)"
j2_le="*(abs(Eta_pfjet2_eta2p5)>0)*(abs(Eta_pfjet2_eta2p5)<2.5)"
j3_le="*(abs(Eta_pfjet3_eta2p5)>0)*(abs(Eta_pfjet3_eta2p5)<2.5)"
j4_le="*(abs(Eta_pfjet4_eta2p5)>0)*(abs(Eta_pfjet4_eta2p5)<2.5)"
j5_le="*(abs(Eta_pfjet5_eta2p5)>0)*(abs(Eta_pfjet5_eta2p5)<2.5)"

# Placeholder to require additional barejet
gj1="*(Pt_genjet1>30.0)*(abs(Eta_genjet1)<2.4)"
gj2="*(Pt_genjet2>30.0)*(abs(Eta_genjet2)<2.4)"
gj3="*(Pt_genjet3>30.0)*(abs(Eta_genjet3)<2.4)"
gj4="*(Pt_genjet4>30.0)*(abs(Eta_genjet4)<2.4)"
gj5="*(Pt_genjet5>30.0)*(abs(Eta_genjet5)<2.4)"
gj6="*(Pt_genjet6>30.0)*(abs(Eta_genjet6)<2.4)"


# QCD: Same as basic, but no isolation or MT cut. 
_qcd_selection = '(PFJet30TCHEMCountCentral<0.5)*(Pt_muon2<0.000001)*(Pt_muon1>25)*(abs(Eta_muon1)<2.1)'
# _qcd_selection+= '*(pass_HBHENoiseFilter*pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'
_qcd_selection += filters
_qcd_selection += j1


# Basic selection for reco-level plots
basic_selection = '(Pt_muon1>25)*(RelIso_muon1<0.15)*(Pt_muon2<0.000001)*(abs(Eta_muon1)<2.1)*(IsoMu24Pass>0)'
basic_selection += '*(MT_muon1METR>50)*(PFJet30TCHEMCountCentral<0.5)'
basic_selection += filters

# Systematic variations with PFJet30TCHEMCountCountEffUp or PFJet30TCHEMCountCountEffDown  ## Do not remove this comment 

# Gen selection for xini (bare) distribution. 
baregen_selection = '(MT_genmuon1genMET>50)*(Eta_genmuon1>-2.1)*(Eta_genmuon1<2.1)*(Pt_genmuon1>25)'
baregen_selection += gj1

_ttbar_selection = basic_selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountCentral>1.5)')
_z_selection = basic_selection.replace('(Pt_muon2<0.000001)','(Pt_muon2>25)')


###################
## DISTRIBUTIONS ##
###################

# Selections are as follows:
# Sels_*_reco = [ Full reco-level selection applies to data and MC, 
#                 Minimal reco-level selection (not yet used)]
# Sels_*_gen  = [ Full gen selection used in final distributions, 
#                 Minimal gen requirements for forming response matrix]


# Jet count - Normal Sel plus one reco jet. Gen level needs nothing extra!
Sel_PFJet30Count_reco = basic_selection+j1
Sel_PFJet30Count_gen = baregen_selection+gj1

# MET - Same as jet count!
Sel_Pt_MET_reco = basic_selection+j1
Sel_Pt_MET_gen = baregen_selection

Sel_ZCont1_Pt_MET_reco = _z_selection+j1
Sel_ZCont1_Pt_MET_gen = baregen_selection

Sel_ZCont2_Pt_MET_reco = _z_selection+j2
Sel_ZCont2_Pt_MET_gen = baregen_selection

Sel_ZCont3_Pt_MET_reco = _z_selection+j3
Sel_ZCont3_Pt_MET_gen = baregen_selection

Sel_ZCont4_Pt_MET_reco = _z_selection+j4
Sel_ZCont4_Pt_MET_gen = baregen_selection

Sel_TCont1_Pt_MET_reco = _ttbar_selection+j1
Sel_TCont1_Pt_MET_gen = baregen_selection

Sel_TCont2_Pt_MET_reco = _ttbar_selection+j2
Sel_TCont2_Pt_MET_gen = baregen_selection

Sel_TCont3_Pt_MET_reco = _ttbar_selection+j3
Sel_TCont3_Pt_MET_gen = baregen_selection

Sel_TCont4_Pt_MET_reco = _ttbar_selection+j4
Sel_TCont4_Pt_MET_gen = baregen_selection


# Muon-related variables with no jet - gen level needs just that muon exists.
Sel_Pt_muon1_reco = basic_selection+j1
Sel_Pt_muon1_gen = baregen_selection

Sel_Eta_muon1_reco = basic_selection+j1
Sel_Eta_muon1_gen = baregen_selection

Sel_MT_genmuon1genMET_reco = basic_selection+j1
Sel_MT_genmuon1genMET_gen = baregen_selection

# Variables with 1 jet
Sel_Pt_pfjet1_reco = basic_selection+j1_pt20
Sel_Pt_pfjet1_gen = baregen_selection

Sel_Eta_pfjet1_reco = basic_selection+j1_le
Sel_Eta_pfjet1_gen = baregen_selection

Sel_DeltaPhi_pfjet1muon1_reco = basic_selection+j1
Sel_DeltaPhi_pfjet1muon1_gen = baregen_selection

# Variables with 2 jet
Sel_Pt_pfjet2_reco = basic_selection+j1+j2_pt20
Sel_Pt_pfjet2_gen = baregen_selection+gj2

Sel_Eta_pfjet2_reco = basic_selection+j1+j2_le
Sel_Eta_pfjet2_gen = baregen_selection+gj2

Sel_DeltaPhi_pfjet2muon1_reco = basic_selection+j2
Sel_DeltaPhi_pfjet2muon1_gen = baregen_selection+gj2


# Variables with 3 jet
Sel_Pt_pfjet3_reco = basic_selection+j2+j3_pt20
Sel_Pt_pfjet3_gen = baregen_selection+gj3

Sel_Eta_pfjet3_reco = basic_selection+j2+j3_le
Sel_Eta_pfjet3_gen = baregen_selection+gj3

Sel_DeltaPhi_pfjet3muon1_reco = basic_selection+j3
Sel_DeltaPhi_pfjet3muon1_gen = baregen_selection+gj3


# Variables with 4 jet
Sel_Pt_pfjet4_reco = basic_selection+j3+j4_pt20
Sel_Pt_pfjet4_gen = baregen_selection+gj4

Sel_Eta_pfjet4_reco = basic_selection+j3+j4_le
Sel_Eta_pfjet4_gen = baregen_selection+gj4

Sel_DeltaPhi_pfjet4muon1_reco = basic_selection+j4
Sel_DeltaPhi_pfjet4muon1_gen = baregen_selection+gj4


# Variables with inclusive jets

Sel_HT_pfjets_1_reco = basic_selection+j1
Sel_HT_pfjets_1_gen = baregen_selection+gj1

Sel_HT_pfjets_2_reco = basic_selection+j2
Sel_HT_pfjets_2_gen = baregen_selection+gj2

Sel_HT_pfjets_3_reco = basic_selection+j3
Sel_HT_pfjets_3_gen = baregen_selection+gj3

Sel_HT_pfjets_4_reco = basic_selection+j4
Sel_HT_pfjets_4_gen = baregen_selection+gj4



Sel_Pt_pfjet5_reco = basic_selection+j4+'*(PFJet30Count>4.5)'
Sel_Pt_pfjet6_reco = basic_selection+j4+'*(PFJet30Count>5.5)'


triggerweight = '*( (abs(Eta_muon1 +1.85)<0.25)*1.0344 + '
triggerweight += '(abs(Eta_muon1 +1.4)<0.2)*1.0550 + '
triggerweight += '(abs(Eta_muon1 +1.05)<0.15)*0.9858 + ' 
triggerweight += '(abs(Eta_muon1 +0.75)<0.15)*0.9876 + '
triggerweight += '(abs(Eta_muon1 +0.45)<0.15)*0.9837 + '
triggerweight += '(abs(Eta_muon1 +0.25)<0.05)*0.9597 + '
triggerweight += '(abs(Eta_muon1 -0)<0.2)*0.9815 + '
triggerweight += '(abs(Eta_muon1 -0.25)<0.05)*0.9630 + '
triggerweight += '(abs(Eta_muon1 -0.45)<0.15)*0.9847 + '
triggerweight += '(abs(Eta_muon1 -0.75)<0.15)*0.9932 + '
triggerweight += '(abs(Eta_muon1 -1.05)<0.15)*0.9776 + '
triggerweight += '(abs(Eta_muon1 -1.4)<0.2)*1.0402 + '
triggerweight += '(abs(Eta_muon1 -1.85)<0.25)*1.0623 )'


idisoweight = '*('
idisoweight += '(abs(Eta_muon1)<1.2)*('
idisoweight += '(abs(Pt_muon1-15)<5)*0.9400+'
idisoweight += '(abs(Pt_muon1-25)<5)*0.9754+'
idisoweight += '(abs(Pt_muon1-35)<5)*0.9897+'
idisoweight += '(abs(Pt_muon1-45)<5)*0.9928+'
idisoweight += '(abs(Pt_muon1-55)<5)*0.9922+'
idisoweight += '(abs(Pt_muon1-70)<10)*0.9843+'
idisoweight += '(abs(Pt_muon1-880)<800)*0.9903'
idisoweight += ')'
idisoweight += '+(abs(Eta_muon1)>=1.2)*('
idisoweight += '(abs(Pt_muon1-15)<5)*0.9963+'
idisoweight += '(abs(Pt_muon1-25)<5)*0.9883+'
idisoweight += '(abs(Pt_muon1-35)<5)*0.9899+'
idisoweight += '(abs(Pt_muon1-45)<5)*0.9910+'
idisoweight += '(abs(Pt_muon1-55)<5)*0.9862+'
idisoweight += '(abs(Pt_muon1-70)<10)*0.9886+'
idisoweight += '(abs(Pt_muon1-880)<800)*0.9720'
idisoweight += ')'
idisoweight += ')'


idisosysweight = '*('
idisosysweight += '(abs(Eta_muon1)<1.2)*('
idisosysweight += '(abs(Pt_muon1-15)<5)*0.9493+'
idisosysweight += '(abs(Pt_muon1-25)<5)*0.9775+'
idisosysweight += '(abs(Pt_muon1-35)<5)*0.9907+'
idisosysweight += '(abs(Pt_muon1-45)<5)*1.0109+'
idisosysweight += '(abs(Pt_muon1-55)<5)*0.9936+'
idisosysweight += '(abs(Pt_muon1-70)<10)*0.9872+'
idisosysweight += '(abs(Pt_muon1-880)<800)*0.9935'
idisosysweight += ')'
idisosysweight += '+(abs(Eta_muon1)>=1.2)*('
idisosysweight += '(abs(Pt_muon1-15)<5)*1.0028+'
idisosysweight += '(abs(Pt_muon1-25)<5)*0.9903+'
idisosysweight += '(abs(Pt_muon1-35)<5)*0.9910+'
idisosysweight += '(abs(Pt_muon1-45)<5)*0.9914+'
idisosysweight += '(abs(Pt_muon1-55)<5)*0.9888+'
idisosysweight += '(abs(Pt_muon1-70)<10)*0.9937+'
idisosysweight += '(abs(Pt_muon1-880)<800)*0.9778'
idisosysweight += ')'
idisosysweight += ')'


# Define baic weight - including PU, trigger, int lumi, and id/iso SF

weight = '*weight_pu_central*4955'
#weight = '*weight_pu_sysplus*4955'
#weight = '*weight_pu_sysminus*4955'


weight += triggerweight + idisoweight


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################



# The main function, called at the end of the script after all other function definitions. If just running analysis on a variable, modify only here.
def main():

	WRenorm = "(1.0)"
	# CleanUpAndMakeTables()
	# sys.exit()
	# ParseTablesToFinalResults(WRenorm,basic_selection)	
	# ParseTablesToRecoHistograms()	
	# ParseTablesToRecoHistograms()	
	# ParseTablesToFinalResults(WRenorm,basic_selection)	
	# CleanUpAndMakeTables()
	CleanUpAndMakeTables()

	sys.exit()

	htunfbinningB1 = [55,30,1680]
	htunfbinningB2 = [54,60,1680]
	htunfbinningB3 = [53,90,1680]
	htunfbinningB4 = [26,120,1680]
	# htunfbinningB1 = [53,30,1620]
	# htunfbinningB2 = [52,60,1620]see
	# htunfbinningB3 = [51,90,1620]
	# htunfbinningB4 = [25,120,1620]
	
	htbinningB = [30,60,90,120,180,240,300,360,420,510,600,720,870,1110,1590]
	htbinningB = [30,60,90,120,180,240,300,360,420,540,660,840,1680]

	_zmetbins = [0,2.5,5.0,7.5,10.0,12.5,15.0,17.5,20.0,22.5,25.0,30,35,40,45,50,60,70,80,100,135,200]
	_zmetbins = [0,2,4,6,8,10,12,14,16,18,20,23,27,33,43,61,95,161,300]
	_zuubins = [70,72.5,75,77.5,80,82.5,85,87.5,90,92.5,95,97.5,100,102.5,105,107.5,110]


	# F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","inc1"],[40,30,1030],[40,30,1030],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[14,14])
	# F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","inc2"],[40,30,1030],[40,30,1030],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[14,14])
	# F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","inc3"],[40,30,1030],[40,30,1030],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	# F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","inc4"],[40,30,1030],[40,30,1030],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[14,14])


	# sys.exit()
	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j1"],[100,0,500],_zuubins,Sels_ZCont1_Pt_MET_reco,Sels_ZCont1_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j1"],[100,0,500],_zmetbins,Sels_ZCont1_Pt_MET_reco,Sels_ZCont1_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j1"],[100,0,500],[50,0,200],Sels_TCont1_Pt_MET_reco,Sels_TCont1_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j2"],[100,0,500],_zmetbins,Sels_ZCont2_Pt_MET_reco,Sels_ZCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j3"],[100,0,500],_zmetbins,Sels_ZCont3_Pt_MET_reco,Sels_ZCont3_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j4"],[100,0,500],_zmetbins,Sels_ZCont4_Pt_MET_reco,Sels_ZCont4_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j2"],[100,0,500],[50,0,200],Sels_TCont2_Pt_MET_reco,Sels_TCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j3"],[100,0,500],[50,0,200],Sels_TCont3_Pt_MET_reco,Sels_TCont3_Pt_MET_gen,weight,'c',22)
	# F#llAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j4"],[100,0,500],[50,0,200],Sels_TCont4_Pt_MET_reco,Sels_TCont4_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j2"],[100,0,500],_zuubins,Sels_ZCont2_Pt_MET_reco,Sels_ZCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j3"],[100,0,500],_zuubins,Sels_ZCont3_Pt_MET_reco,Sels_ZCont3_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j4"],[100,0,500],_zuubins,Sels_ZCont4_Pt_MET_reco,Sels_ZCont4_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[4,4])



	# F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","nouflow"],[44,30,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco+j1, Sel_Pt_pfjet1_gen,weight,'c',[14,14])
	# F#ullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","nouflow"],[59,30,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco+j2, Sel_Pt_pfjet2_gen,weight,'c',[15,15])
	# F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","nouflow"],[49,30,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco+j3, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	# F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","nouflow"],[39,30,420],[30,50,70,90,350],Sel_Pt_pfjet4_reco+j4, Sel_Pt_pfjet4_gen,weight,'c',[5,5])




	FullAnalysisWithUncertainty(['GenJet30Count','GenJet30Count'],'PFJet30Count',-1,["N_{Jet}",""],[11,-.5,10.5],[6 ,0.5,6.5],Sel_PFJet30Count_reco,Sel_PFJet30Count_gen,weight,'c',[5,5])	
	FullAnalysisWithUncertainty(['GenJet30Count','GenJet30Count'],'PFJet30Count',-1,["N_{Jet}","_preexc"],[11,-.5,10.5],[8 ,0.5,8.5],Sel_PFJet30Count_reco,Sel_PFJet30Count_gen,weight,'c',[5,5])	


	FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]",""],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[14,19])
	FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]",""],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[15,16])
	FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]",""],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,7])
	FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]",""],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[4,5])



	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[13,18])
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[15,17])
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[8,7])
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[7,10])


	#F#ullAnalysisWithUncertainty(['Eta_genjet1','Eta_genjet1'],'Eta_pfjet1_eta2p5',-2.5,["#eta(jet_{1}) ",""],[50,-2.5,2.5],[24,-2.4,2.4],Sel_Eta_pfjet1_reco, Sel_Eta_pfjet1_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Eta_genjet2','Eta_genjet2'],'Eta_pfjet2_eta2p5',-2.5,["#eta(jet_{2}) ",""],[50,-2.5,2.5],[24,-2.4,2.4],Sel_Eta_pfjet2_reco, Sel_Eta_pfjet2_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Eta_genjet3','Eta_genjet3'],'Eta_pfjet3_eta2p5',-2.5,["#eta(jet_{3}) ",""],[50,-2.5,2.5],[8,-2.4,2.4],Sel_Eta_pfjet3_reco, Sel_Eta_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Eta_genjet4','Eta_genjet4'],'Eta_pfjet4_eta2p5',-2.5,["#eta(jet_{4}) ",""],[50,-2.5,2.5],[6,-2.4,2.4],Sel_Eta_pfjet4_reco, Sel_Eta_pfjet4_gen,weight,'c',[5,5])

	FullAnalysisWithUncertainty(['abs(Eta_genjet1)','abs(Eta_genjet1)'],'Eta_pfjet1_eta2p5',-2.5,["|#eta(jet_{1})|",""],[25,0.0,2.5],[24,0.0,2.4],Sel_Eta_pfjet1_reco, Sel_Eta_pfjet1_gen,weight,'c',[8,8])
	FullAnalysisWithUncertainty(['abs(Eta_genjet2)','abs(Eta_genjet2)'],'Eta_pfjet2_eta2p5',-2.5,["|#eta(jet_{2})|",""],[25,0.0,2.5],[24,0.0,2.4],Sel_Eta_pfjet2_reco, Sel_Eta_pfjet2_gen,weight,'c',[7,7])
	FullAnalysisWithUncertainty(['abs(Eta_genjet3)','abs(Eta_genjet3)'],'Eta_pfjet3_eta2p5',-2.5,["|#eta(jet_{3})|",""],[25,0.0,2.5],[8,0.0,2.4],Sel_Eta_pfjet3_reco, Sel_Eta_pfjet3_gen,weight,'c',[5,5])
	FullAnalysisWithUncertainty(['abs(Eta_genjet4)','abs(Eta_genjet4)'],'Eta_pfjet4_eta2p5',-2.5,["|#eta(jet_{4})|",""],[25,0.0,2.5],[6,0.0,2.4],Sel_Eta_pfjet4_reco, Sel_Eta_pfjet4_gen,weight,'c',[3,3])

	FullAnalysisWithUncertainty(['DeltaPhi_genjet1genmuon1','DeltaPhi_genjet1genmuon1'],'DeltaPhi_pfjet1muon1',-0.05,["#Delta#phi(jet_{1},#mu) [GeV]",""],[22,-.15707963,3.1415927+.15707963],[20,0,3.1415927],Sel_DeltaPhi_pfjet1muon1_reco,Sel_DeltaPhi_pfjet1muon1_gen,weight,'c',[6,6])
	FullAnalysisWithUncertainty(['DeltaPhi_genjet2genmuon1','DeltaPhi_genjet2genmuon1'],'DeltaPhi_pfjet2muon1',-0.05,["#Delta#phi(jet_{2},#mu) [GeV]",""],[17,-0.20943950,3.1415927+0.20943950],[15,0,3.1415927],Sel_DeltaPhi_pfjet2muon1_reco,Sel_DeltaPhi_pfjet2muon1_gen,weight,'c',[4,4])
	FullAnalysisWithUncertainty(['DeltaPhi_genjet3genmuon1','DeltaPhi_genjet3genmuon1'],'DeltaPhi_pfjet3muon1',-0.05,["#Delta#phi(jet_{3},#mu) [GeV]",""],[12,-0.31415926,3.1415927+0.31415926],[10,0,3.1415927],Sel_DeltaPhi_pfjet3muon1_reco,Sel_DeltaPhi_pfjet3muon1_gen,weight,'c',[3,3])
	FullAnalysisWithUncertainty(['DeltaPhi_genjet4genmuon1','DeltaPhi_genjet4genmuon1'],'DeltaPhi_pfjet4muon1',-0.05,["#Delta#phi(jet_{4},#mu) [GeV]",""],[8,-0.523598766,3.1415927+0.523598766],[6,0,3.1415927],Sel_DeltaPhi_pfjet4muon1_reco,Sel_DeltaPhi_pfjet4muon1_gen,weight,'c',[3,3])

	#F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]",""],[15,50,200],[50,60,70,80,90,100,115,130,150,170,200],Sel_Pt_MET_reco,Sel_Pt_MET_gen,weight,'c',[12,12])
	FullAnalysisWithUncertainty(['MT_genmuon1genMET','MT_genmuon1genMET'],'MT_muon1METR',25,["M_{T}(#mu,E_{T}^{miss}) [GeV]",""],[30,0,150],[20,50,150],Sel_MT_genmuon1genMET_reco,Sel_MT_genmuon1genMET_gen,weight,'c',[15,17])
	FullAnalysisWithUncertainty(['Pt_genmuon1','Pt_genmuon1'],'Pt_muon1',0,["p_{T}(#mu_{1}) [GeV]",""],[55,25,300],[55,25,300],Sel_Pt_muon1_reco,Sel_Pt_muon1_gen,weight,'c',[8,16])
	#F#ullAnalysisWithUncertainty(['abs(Eta_genmuon1)','abs(Eta_genmuon1)'],'Eta_muon1',0,["|#eta (#mu_{1})| [GeV]",""],[92,-2.3,2.3],[42,-2.1,2.1],Sel_Eta_muon1_reco,Sel_Eta_muon1_gen,weight,'c',[12,12])

	#FullAnalysisWithUncertainty(['N_GoodVertices','N_GoodVertices'],'N_GoodVertices',0,["N_GoodVertices",""],[51,-1,50],[40,0,40],Sel_Eta_muon1_reco,Sel_Eta_muon1_gen,weight,'c',[6,10])


	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r3"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r4"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r5"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r6"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r7"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r8"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r9"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r10"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r11"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r12"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r13"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r14"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r15"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r16"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r17"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r18"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r19"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r20"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r21"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r22"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r23"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r24"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r25"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r26"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r27"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r28"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[28,28])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r29"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r30"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r31"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r32"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r33"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r34"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r35"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[35,35])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r36"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[36,36])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r37"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[37,37])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r38"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[38,38])
	#FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","_r39"],[45,10,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco, Sel_Pt_pfjet1_gen,weight,'c',[39,39])

	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r3"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r4"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r5"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r6"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r7"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r8"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r9"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r10"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r11"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r12"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r13"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r14"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r15"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r16"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r17"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r18"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r19"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r20"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r21"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r22"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r23"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r24"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r25"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r26"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r27"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r28"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[28,28])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r29"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r30"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r31"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r32"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r33"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r34"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r35"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[35,35])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r36"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[36,36])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r37"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[37,37])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r38"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[38,38])
	#FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","_r39"],[60,20,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco, Sel_Pt_pfjet2_gen,weight,'c',[39,39])

	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r3"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r4"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r5"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r6"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r7"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r8"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r9"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r10"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r11"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r12"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r13"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r14"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r15"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","_r16"],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])

	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r3"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r4"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r5"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r6"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r7"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r8"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","_r9"],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[9,9])



	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_30GeV_pt450_reg"+str(2)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_30GeV_pt450_reg"+str(3)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_30GeV_pt450_reg"+str(4)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_30GeV_pt450_reg"+str(5)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_30GeV_pt450_reg"+str(6)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_30GeV_pt450_reg"+str(7)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_30GeV_pt450_reg"+str(8)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_30GeV_pt450_reg"+str(9)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_30GeV_pt450_reg"+str(10)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_30GeV_pt450_reg"+str(11)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_30GeV_pt450_reg"+str(12)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_30GeV_pt450_reg"+str(13)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_30GeV_pt450_reg"+str(14)],[17,0,510],[30,60,90,120,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])


	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(2),"force_30GeV_pt450_reg"+str(2)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(3),"force_30GeV_pt450_reg"+str(3)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(4),"force_30GeV_pt450_reg"+str(4)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(5),"force_30GeV_pt450_reg"+str(5)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(6),"force_30GeV_pt450_reg"+str(6)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(7),"force_30GeV_pt450_reg"+str(7)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV] reg:"+str(8),"force_30GeV_pt450_reg"+str(8)],[10,0,300],[30,60,90,210],Sel_Pt_pfjet4_reco, Sel_Pt_pfjet4_gen,weight,'c',[8,8])



	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_10GeV_pt250_orig_"+str(2)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_10GeV_pt250_orig_"+str(3)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_10GeV_pt250_orig_"+str(4)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_10GeV_pt250_orig_"+str(5)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_10GeV_pt250_orig_"+str(6)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_10GeV_pt250_orig_"+str(7)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_10GeV_pt250_orig_"+str(8)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_10GeV_pt250_orig_"+str(9)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_10GeV_pt250_orig_"+str(10)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_10GeV_pt250_orig_"+str(11)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_10GeV_pt250_orig_"+str(12)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_10GeV_pt250_orig_"+str(13)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_10GeV_pt250_orig_"+str(14)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(15),"force_10GeV_pt250_orig_"+str(15)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(16),"force_10GeV_pt250_orig_"+str(16)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(17),"force_10GeV_pt250_orig_"+str(17)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[17,17])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(18),"force_10GeV_pt250_orig_"+str(18)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[18,18])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(19),"force_10GeV_pt250_orig_"+str(19)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[19,19])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(20),"force_10GeV_pt250_orig_"+str(20)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[20,20])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(21),"force_10GeV_pt250_orig_"+str(21)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[21,21])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(22),"force_10GeV_pt250_orig_"+str(22)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[22,22])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(23),"force_10GeV_pt250_orig_"+str(23)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[23,23])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(24),"force_10GeV_pt250_orig_"+str(24)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[24,24])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(25),"force_10GeV_pt250_orig_"+str(25)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[25,25])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(26),"force_10GeV_pt250_orig_"+str(26)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[26,26])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(27),"force_10GeV_pt250_orig_"+str(27)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[27,27])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(28),"force_10GeV_pt250_orig_"+str(28)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[28,28])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(29),"force_10GeV_pt250_orig_"+str(29)],[50,20,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[29,29])

	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_10GeV_pt250_origmorebin_"+str(2)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_10GeV_pt250_origmorebin_"+str(3)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_10GeV_pt250_origmorebin_"+str(4)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_10GeV_pt250_origmorebin_"+str(5)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_10GeV_pt250_origmorebin_"+str(6)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_10GeV_pt250_origmorebin_"+str(7)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_10GeV_pt250_origmorebin_"+str(8)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_10GeV_pt250_origmorebin_"+str(9)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_10GeV_pt250_origmorebin_"+str(10)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_10GeV_pt250_origmorebin_"+str(11)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_10GeV_pt250_origmorebin_"+str(12)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_10GeV_pt250_origmorebin_"+str(13)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_10GeV_pt250_origmorebin_"+str(14)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(15),"force_10GeV_pt250_origmorebin_"+str(15)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(16),"force_10GeV_pt250_origmorebin_"+str(16)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(17),"force_10GeV_pt250_origmorebin_"+str(17)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[17,17])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(18),"force_10GeV_pt250_origmorebin_"+str(18)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[18,18])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(19),"force_10GeV_pt250_origmorebin_"+str(19)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[19,19])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(20),"force_10GeV_pt250_origmorebin_"+str(20)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[20,20])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(21),"force_10GeV_pt250_origmorebin_"+str(21)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[21,21])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(22),"force_10GeV_pt250_origmorebin_"+str(22)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[22,22])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(23),"force_10GeV_pt250_origmorebin_"+str(23)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[23,23])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(24),"force_10GeV_pt250_origmorebin_"+str(24)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[24,24])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(25),"force_10GeV_pt250_origmorebin_"+str(25)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[25,25])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(26),"force_10GeV_pt250_origmorebin_"+str(26)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[26,26])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(27),"force_10GeV_pt250_origmorebin_"+str(27)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[27,27])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(28),"force_10GeV_pt250_origmorebin_"+str(28)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[28,28])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(29),"force_10GeV_pt250_origmorebin_"+str(29)],[70,20,720],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[29,29])

	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_10GeV_pt250_origlessbin_"+str(2)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_10GeV_pt250_origlessbin_"+str(3)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_10GeV_pt250_origlessbin_"+str(4)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_10GeV_pt250_origlessbin_"+str(5)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_10GeV_pt250_origlessbin_"+str(6)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_10GeV_pt250_origlessbin_"+str(7)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_10GeV_pt250_origlessbin_"+str(8)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_10GeV_pt250_origlessbin_"+str(9)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_10GeV_pt250_origlessbin_"+str(10)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_10GeV_pt250_origlessbin_"+str(11)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_10GeV_pt250_origlessbin_"+str(12)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_10GeV_pt250_origlessbin_"+str(13)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_10GeV_pt250_origlessbin_"+str(14)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(15),"force_10GeV_pt250_origlessbin_"+str(15)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(16),"force_10GeV_pt250_origlessbin_"+str(16)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(17),"force_10GeV_pt250_origlessbin_"+str(17)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[17,17])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(18),"force_10GeV_pt250_origlessbin_"+str(18)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[18,18])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(19),"force_10GeV_pt250_origlessbin_"+str(19)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[19,19])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(20),"force_10GeV_pt250_origlessbin_"+str(20)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[20,20])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(21),"force_10GeV_pt250_origlessbin_"+str(21)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[21,21])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(22),"force_10GeV_pt250_origlessbin_"+str(22)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[22,22])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(23),"force_10GeV_pt250_origlessbin_"+str(23)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[23,23])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(24),"force_10GeV_pt250_origlessbin_"+str(24)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[24,24])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(25),"force_10GeV_pt250_origlessbin_"+str(25)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[25,25])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(26),"force_10GeV_pt250_origlessbin_"+str(26)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[26,26])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(27),"force_10GeV_pt250_origlessbin_"+str(27)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[27,27])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(28),"force_10GeV_pt250_origlessbin_"+str(28)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[28,28])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(29),"force_10GeV_pt250_origlessbin_"+str(29)],[45,20,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[29,29])


	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_20GeV_pt470_reg"+str(2)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_20GeV_pt470_reg"+str(3)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_20GeV_pt470_reg"+str(4)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_20GeV_pt470_reg"+str(5)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_20GeV_pt470_reg"+str(6)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_20GeV_pt470_reg"+str(7)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_20GeV_pt470_reg"+str(8)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_20GeV_pt470_reg"+str(9)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_20GeV_pt470_reg"+str(10)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_20GeV_pt470_reg"+str(11)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_20GeV_pt470_reg"+str(12)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_20GeV_pt470_reg"+str(13)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_20GeV_pt470_reg"+str(14)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(15),"force_20GeV_pt470_reg"+str(15)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(16),"force_20GeV_pt470_reg"+str(16)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(17),"force_20GeV_pt470_reg"+str(17)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[17,17])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(18),"force_20GeV_pt470_reg"+str(18)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[18,18])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(19),"force_20GeV_pt470_reg"+str(19)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[19,19])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(20),"force_20GeV_pt470_reg"+str(20)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[20,20])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(21),"force_20GeV_pt470_reg"+str(21)],[23,10,470],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[21,21])



	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(2),"force_20GeV_pt610_reg"+str(2)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[2,2])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(3),"force_20GeV_pt610_reg"+str(3)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[3,3])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(4),"force_20GeV_pt610_reg"+str(4)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[4,4])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(5),"force_20GeV_pt610_reg"+str(5)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[5,5])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(6),"force_20GeV_pt610_reg"+str(6)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(7),"force_20GeV_pt610_reg"+str(7)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[7,7])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(8),"force_20GeV_pt610_reg"+str(8)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[8,8])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(9),"force_20GeV_pt610_reg"+str(9)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[9,9])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(10),"force_20GeV_pt610_reg"+str(10)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[10,10])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(11),"force_20GeV_pt610_reg"+str(11)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[11,11])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(12),"force_20GeV_pt610_reg"+str(12)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[12,12])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(13),"force_20GeV_pt610_reg"+str(13)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[13,13])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(14),"force_20GeV_pt610_reg"+str(14)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(15),"force_20GeV_pt610_reg"+str(15)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(16),"force_20GeV_pt610_reg"+str(16)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[16,16])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(17),"force_20GeV_pt610_reg"+str(17)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[17,17])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(18),"force_20GeV_pt610_reg"+str(18)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[18,18])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(19),"force_20GeV_pt610_reg"+str(19)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[19,19])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(20),"force_20GeV_pt610_reg"+str(20)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[20,20])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(21),"force_20GeV_pt610_reg"+str(21)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[21,21])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(22),"force_20GeV_pt610_reg"+str(22)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[22,22])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(23),"force_20GeV_pt610_reg"+str(23)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[23,23])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(24),"force_20GeV_pt610_reg"+str(24)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[24,24])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV] reg:"+str(25),"force_20GeV_pt610_reg"+str(25)],[30,10,610],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco, Sel_Pt_pfjet3_gen,weight,'c',[25,25])


	#F#ullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1'],'Pt_pfjet1_pt20',0,["p_{T}(jet_{1}) [GeV]","nouflow"],[44,30,910],[30,50,70,90,110,150,190,250,310,430,850],Sel_Pt_pfjet1_reco+j1, Sel_Pt_pfjet1_gen,weight,'c',[14,14])
	#F#ullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2'],'Pt_pfjet2_pt20',0,["p_{T}(jet_{2}) [GeV]","nouflow"],[59,30,620],[30,50,70,90,110,150,190,250,550],Sel_Pt_pfjet2_reco+j2, Sel_Pt_pfjet2_gen,weight,'c',[15,15])
	#F#ullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3'],'Pt_pfjet3_pt20',0,["p_{T}(jet_{3}) [GeV]","nouflow"],[49,30,520],[30,50,70,90,110,150,210,450],Sel_Pt_pfjet3_reco+j3, Sel_Pt_pfjet3_gen,weight,'c',[6,6])
	#F#ullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4'],'Pt_pfjet4_pt20',0,["p_{T}(jet_{4}) [GeV]","nouflow"],[39,30,420],[30,50,70,90,350],Sel_Pt_pfjet4_reco+j4, Sel_Pt_pfjet4_gen,weight,'c',[5,5])



	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r03"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r04"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r05"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r06"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r07"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r08"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r09"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r10"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r11"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r12"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r13"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r14"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r15"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r16"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r17"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r18"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r19"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r20"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r21"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r22"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r23"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r24"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r25"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r26"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r27"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r28"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r29"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r30"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r31"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r32"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r33"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r34"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1_r35"],htunfbinningB1,htbinningB[0:],Sel_HT_pfjets_1_reco, Sel_HT_pfjets_1_gen,weight,'c',[35,35])

	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r03"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r04"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r05"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r06"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r07"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r08"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r09"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r10"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r11"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r12"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r13"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r14"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r15"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r16"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r17"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r18"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r19"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r20"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r21"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r22"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r23"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r24"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r25"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r26"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r27"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r28"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r29"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r30"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r31"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r32"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r33"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r34"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2_r35"],htunfbinningB2,htbinningB[1:],Sel_HT_pfjets_2_reco, Sel_HT_pfjets_2_gen,weight,'c',[35,35])

	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r03"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r04"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r05"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r06"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r07"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r08"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r09"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r10"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r11"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r12"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r13"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r14"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r15"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r16"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r17"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r18"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r19"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r20"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r21"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r22"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r23"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r24"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r25"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r26"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r27"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r28"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r29"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r30"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r31"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r32"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r33"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r34"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3_r35"],htunfbinningB3,htbinningB[2:],Sel_HT_pfjets_3_reco, Sel_HT_pfjets_3_gen,weight,'c',[35,35])


	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r03"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[3,3])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r04"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[4,4])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r05"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[5,5])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r06"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[6,6])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r07"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[7,7])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r08"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[8,8])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r09"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[9,9])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r10"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[10,10])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r11"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[11,11])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r12"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[12,12])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r13"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[13,13])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r14"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[14,14])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r15"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[15,15])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r16"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[16,16])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r17"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[17,17])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r18"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[18,18])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r19"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[19,19])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r20"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[20,20])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r21"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[21,21])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r22"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[22,22])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r23"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[23,23])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r24"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[24,24])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r25"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[25,25])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r26"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[26,26])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r27"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[27,27])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r28"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r29"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[29,29])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r30"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[30,30])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r31"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[31,31])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r32"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[32,32])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r33"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[33,33])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r34"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[34,34])
	#FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4_r35"],htunfbinningB4,htbinningB[3:],Sel_HT_pfjets_4_reco, Sel_HT_pfjets_4_gen,weight,'c',[35,35])

	# ParseTablesToRecoHistograms()	
	# ParseTablesToFinalResults(WRenorm,basic_selection)	
	# CleanUpAndMakeTables()

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

##########################################################################
########            Import libraries                              ########
##########################################################################

import sys
import math
sys.argv.append( '-b' )  # Batch mode - no XWindows - much faster
# sys.argv.append('--quickplots')

print 'LOADING ROOT...'
from ROOT import * # Load root
print 'Looading RooUnfold'
gSystem.Load('/afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_4_2_8/src/WJetsAnalysis/RooUnfold/libRooUnfold.so')
from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from ROOT import RooUnfoldSvd
from ROOT import RooUnfoldTUnfold
from ROOT import RooUnfoldBinByBin


from glob import * # For table parsing
import csv         # For table parsing
from itertools import izip  # More for table parsing
from array import array    
import numpy
import random


##########################################################################
########              CleanUp/SetUp ROOT                          ########
##########################################################################
gROOT.ProcessLine("gErrorIgnoreLevel = 3001;") # Suppress warnings
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
	legend.SetTextFont(42)
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
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

	return hout

def RebinnedHisto(name,legendname,inputhisto,binning,style,label):
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	# print '   ... bins created.'
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
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
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)


	# print '='*50

	outmeans = [0.0  for x in range(len(binset)+2)]
	outerrs2 = [0.0 for x in range(len(binset)+2)]

	for x in range(inputhisto.GetNbinsX()):
		nbin = x+1
		halfwidth = 0.5*inputhisto.GetBinWidth(nbin)
		center = inputhisto.GetBinCenter(nbin)
		lhs = center - halfwidth
		rhs = center + halfwidth
		cont = inputhisto.GetBinContent(nbin)
		err = inputhisto.GetBinError(nbin)
		# print lhs,rhs,cont,err

		for nn in range(len(binset)+2):
			_halfwidth = 0.5*hout.GetBinWidth(nn)
			_center = hout.GetBinCenter(nn)
			_lhs = _center - _halfwidth
			_rhs = _center + _halfwidth			
			# print center,_lhs,_rhs

			if center>_lhs and center < _rhs:
				outmeans[nn] += cont
				outerrs2[nn] += err*err 

	outerrs = [math.sqrt(x) for x in outerrs2]

	for nn in range(len(outmeans)):
		hout.SetBinContent(nn,outmeans[nn])
		hout.SetBinError(nn,outerrs[nn])
	for x in range(hout.GetNbinsX()):
		nbin = x+1
		halfwidth = 0.5*hout.GetBinWidth(nbin)
		center = hout.GetBinCenter(nbin)
		lhs = center - halfwidth
		rhs = center + halfwidth
		cont = hout.GetBinContent(nbin)
		err = hout.GetBinError(nbin)

	return hout



# Make basic TH1D for a branch. Projects branch to histo for given binning and selection. 
def NullHisto(name,legendname,binning,style,label):
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	
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

	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

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
	histo.GetXaxis().SetTitleFont(42)
	histo.GetYaxis().SetTitleFont(42)
	histo.GetXaxis().SetLabelFont(42)
	histo.GetYaxis().SetLabelFont(42)
	return histo

# Cleans up a stacked histogram
def BeautifyStack(stack,label):
	# Fix Font
	stack.GetHistogram().GetXaxis().SetTitleFont(42)
	stack.GetHistogram().GetYaxis().SetTitleFont(42)
	stack.GetHistogram().GetXaxis().SetLabelFont(42)
	stack.GetHistogram().GetYaxis().SetLabelFont(42)
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
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)
	
	return hout

def MakeInclusiveBinInfo(bininfo):

	outputinfo = []

	inputinfo = []
	_cont = []
	_err = []
	_bin = []
	for x in bininfo:
		_bin.append(x[0])
		hcont = x[1].split('+-')
		_cont.append(float(hcont[0]))
		_err.append(float(hcont[1]))

	def CumulativeSum(_alist,_flag_quadrature):
		if _flag_quadrature == 'linear':
			_do_quadrature = False
		elif _flag_quadrature == 'quadrature':
			_do_quadrature = True
		else:
			print 'Incorrect flag for quadrature!'
			sys.exit()
		_out_alist = []
		for _x in range(len(_alist)):
			x = _alist[_x]
			bintot = 0.0
			for _y in range(len(_alist)):
				y = _alist[_y]
				if _y >=_x:
					bintot_addon = 1.0*y
					if _do_quadrature:
						bintot_addon *= y
					bintot += bintot_addon
			if _do_quadrature:
				bintot = math.sqrt(bintot)
			_out_alist.append(bintot)
		return _out_alist

	_newcont = CumulativeSum(_cont,'linear')
	_newerr = CumulativeSum(_err,'quadrature')
	for _x in range(len(_bin)):
		_thisinfo = []
		_thisinfo.append(_bin[_x])
		_thisinfo.append(str(_newcont[_x]) + ' +- '+str(_newerr[_x]))
		outputinfo.append(_thisinfo)

	return outputinfo



# Function to take data histogram and subtract list of background histograms.
def BackgroundSubtractedHistogram(data,backgrounds):
	for b in backgrounds:
		b.Scale(-1)
		data.Add(b)
		b.Scale(-1)
	return data

# This will take a weight MC histogram and create an unweighted data-like histogram. 
# Used for closure test on Madgraph MC. 
def PseudoDataHisto(histo,newname,binning):
	# Convert to var binning
	binset=ConvertBinning(binning)
	# print binset
	N = len(binset)+1
	# Make new histogram
	hout= TH1D(newname,"",N-2,array('d',binset))	
	for n in range(N):
		binval = histo.GetBinCenter(n)
		bincont = int(round(histo.GetBinContent(n)))
		# print n,binval,bincont
		tot = 0
		for ii in range(bincont):
			hout.Fill(binval)
			tot += 1
		# print tot
	return hout


# This is the "Smart" SVD - optimizes tau on the fly. This version is not used. Pseudoexperiments are used.
def GetSmartSVD(data_histo,Params, binning,forcetau,software,forcemethod,isitmcunf):

	doNoProp = False
	systype = int(forcemethod)
	if forcemethod ==4:
		doNoProp = True
		systype = 3

	if software == 'TSVD' or software== 'AutoBin' or software=='TSVDNoCov':
		# Clone data histogram and get binning
		data=data_histo.Clone()
		binset=ConvertBinning(binning)
		n = len(binset)-1

		# Declare and fill covariance
		statcov = TH2D("statcov", "covariance matrix", n, array('d',binset),n,array('d',binset))	
		for i in range(data.GetNbinsX()):
			statcov.SetBinContent(i,i,data.GetBinError(i)*data.GetBinError(i)) 

			print 'Statcov Bin:Cont',i,data.GetBinError(i)*data.GetBinError(i)
		
		# Do an initial unfolding.	 	
		if software=='TSVDNoCov':
			tsvdunf_prep= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] )
		else:
			tsvdunf_prep= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )


		tsvdunf_prep.SetNormalize( kFALSE ) 
		unfres_prep = tsvdunf_prep.Unfold( 1 )	

		# Get the distribution of the d to cross check the regularization
		# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
		ddist_prep = tsvdunf_prep.GetD()
		svdist_prep = tsvdunf_prep.GetSV()

		# 
		OptTau=1
		OptI=1
		OptSV=1
		for i in range(ddist_prep.GetNbinsX()):
			if i<1:
				continue
			if ddist_prep.GetBinContent(i)<1.0:
				OptI=i-2
				OptSV=svdist_prep.GetBinContent(OptI)
				OptTau=int(round(svdist_prep.GetBinContent(OptI)*svdist_prep.GetBinContent(OptI)))
				#OptTau=OptI
				if OptTau==0:
					OptTau=1
				break

		if forcetau>0:
			OptTau=forcetau
		
		if software=='TSVDNoCov':			
			tsvdunf= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] )
		else:
			tsvdunf= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )

		tsvdunf.SetNormalize( kFALSE ) 
		unftau = int(OptTau)
		if software=='AutoBin':
			OptTau=123456
		if OptTau==123456:
			unftau = 2
		unfres = tsvdunf.Unfold( unftau )	
		print 'TABULATING A BIN-BY-BIN RESCALING!!'
		num = Params[1].Clone()
		denom = Params[0].Clone()
		num.Divide(denom)
		unfres_mod = data_histo.Clone()
		unfres_mod.Sumw2()
		unfres_mod.Multiply(num) 
		print 'bin-by-bin rescaling complete'
		# Get the distribution of the d to cross check the regularization
		# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
		ddist = tsvdunf.GetD()
		ddist.SetTitle("Diagonal Values")
			
		# Get the distribution of the singular values
		svdist = tsvdunf.GetSV()
		svdist.SetTitle("Singular Values")
		print 'got D/SV dists'
		# Compute the error matrix for the unfolded spectrum using toy MC
		# using the measured covariance matrix as input to generate the toys
		# 100 toys should usually be enough
		# The same method can be used for different covariance matrices separately.
		ustatcov = tsvdunf.GetUnfoldCovMatrix( statcov, 100 )	
		# Now compute the error matrix on the unfolded distribution originating
		# from the finite detector matrix statistics
		uadetcov = tsvdunf.GetAdetCovMatrix( 100 )	
		# Sum up the two (they are uncorrelated)
		ustatcov.Add( uadetcov )
		#Get the computed regularized covariance matrix (always corresponding to total uncertainty passed in constructor) and add uncertainties from finite MC statistics. 
		utaucov = tsvdunf.GetXtau()
		utaucov.Add( uadetcov )
		#Get the computed inverse of the covariance matrix
		uinvcov = tsvdunf.GetXinv()
		print 'Got covariances'
		# Errors on unfolding result.
		for i in range(unfres.GetNbinsX()):
			# if OptTau == 123456:
			# 	continue
			unfres.SetBinError(i, math.sqrt(utaucov.GetBinContent(i,i)))
		print 'errors set, returning...'
		if OptTau != 123456:
			return [unfres,ddist,svdist,OptTau,OptI]
		else:
			return [unfres_mod,ddist,svdist,OptTau,OptI]

	if software =='RooUnfoldSvdUncTest':

		response = RooUnfoldResponse (Params[0], Params[1], Params[2])
		binset=ConvertBinning(binning)
		n = len(binset)-1

		bb= RooUnfoldBayes(response, data_histo, 4)
		bb.IncludeSystematics()
		hb= bb.Hreco()

		for x in range((n-3)):
			ntest = x+2
			print ' ---------- SVD TEST N=',ntest,' ------------'
			print 'Center','WRT Bayes'
			uu = RooUnfoldSvd(response,data_histo,ntest)
			uu.IncludeSystematics()

			hh = uu.Hreco(systype)
			hh.Divide(hb)
			for nb in range((hh.GetNbinsX())):
				herr = 0
				derr = 0
				if data_histo.GetBinContent(nb) > 0:
					derr = data_histo.GetBinError(nb)/data_histo.GetBinContent(nb)
				if hh.GetBinContent(nb) > 0:
					herr =  hh.GetBinError(nb)/hh.GetBinContent(nb)
				comperr = 0
				if derr > 0:
					comperr = herr/derr
				# print hh.GetBinCenter(nb),data_histo.GetBinCenter(nb),' --> ', herr, derr, comperr
				print hh.GetBinCenter(nb),hh.GetBinContent(nb)
		print 'Verbose error for unfold only. Exiting.'
		sys.exit()


	if software == 'RooUnfoldSvd':

		response = RooUnfoldResponse (Params[0], Params[1], Params[2])
		OptTau = 1
		if forcetau>0:
			OptTau=forcetau
		binset=ConvertBinning(binning)
		n = len(binset)-1

		print " ----------- STANDARD UNFOLDING --------------"
		# unfold= RooUnfoldSvd(response, data_histo, OptTau)

		# if isitmcunf == False:
		# 	# unfold= RooUnfoldSvd(response, data_histo, OptTau)

		# 	unfold.IncludeSystematics(0)		# Data Only
		# 	unfres= unfold.Hreco(3)   # Toy method
		# 	unfres.Sumw2()
		# else: 


		for nm in range(500):
			print ' --------------------------------- >> Trial ',nm
			unfold= RooUnfoldSvd(response, data_histo, OptTau)

			if isitmcunf == True:
				unfold.IncludeSystematics(2) # MC Response only
			if isitmcunf == False:
				unfold.IncludeSystematics(0) # MC Response only
			isgood = True
			unfres= unfold.Hreco(3) # Toy Method 
			unfres.Sumw2()
			isgood = True
			for nb in range((unfres.GetNbinsX())+1):
				print unfres.GetBinCenter(nb),unfres.GetBinContent(nb), unfres.GetBinError(nb)
				binline = str(unfres.GetBinCenter(nb)) +'  '+ str(unfres.GetBinContent(nb)) +'  '+ str( unfres.GetBinError(nb))
				print '    Interpreted line:',binline
				if 'nan' in binline:
					print 'BAD BIN DETECTED'
					isgood = False

				if (unfres.GetBinError(nb) > 100*(unfres.GetBinContent(nb))):
					print 'BAD ERROR DETECTED'
					isgood = False
					
			if isgood ==True:
				print '   ... Good Unfolding detected (no nans). Moving on.'
				break

		if isitmcunf == True:
			for ibin in range(unfres.GetNbinsX()+1):
				unfres.SetBinContent(ibin,unfres.GetBinContent(ibin)+unfres.GetBinError(ibin))



		hdd = unfres.Clone()
		hdd.Divide(unfres)
		hsv = hdd.Clone()
		for nb in range((unfres.GetNbinsX())+1):
			print unfres.GetBinCenter(nb),unfres.GetBinContent(nb), unfres.GetBinError(nb)

		return [unfres,hdd,hsv,OptTau,0]


	if software == 'RooUnfoldBayes':

		response = RooUnfoldResponse (Params[0], Params[1], Params[2])
		unfold= RooUnfoldBayes(response, data_histo, 4)
		if isitmcunf == False:
			unfold.IncludeSystematics(0)		
			unfres= unfold.Hreco(systype)
			unfres.Sumw2()
		else: 
			unfold.IncludeSystematics(2)
			unfres= unfold.Hreco(3)
			unfres.Sumw2()
			for ibin in range(unfres.GetNbinsX()+1):
				unfres.SetBinContent(ibin,unfres.GetBinContent(ibin)+unfres.GetBinError(ibin))

		hdd = unfres.Clone()
		hdd.Divide(unfres)
		hsv = hdd.Clone()
		return [unfres,hdd,hsv,4,0]

	if software == 'RooUnfoldBin':

		response = RooUnfoldResponse (Params[0], Params[1], Params[2])
		unfold= RooUnfoldBinByBin (response, data_histo)
		if isitmcunf == False:
			unfold.IncludeSystematics(0)		
			unfres= unfold.Hreco(systype)
			unfres.Sumw2()
		else: 
			unfold.IncludeSystematics(2)
			unfres= unfold.Hreco(3)
			unfres.Sumw2()
			for ibin in range(unfres.GetNbinsX()+1):
				unfres.SetBinContent(ibin,unfres.GetBinContent(ibin)+unfres.GetBinError(ibin))

		hdd = unfres.Clone()
		hdd.Divide(unfres)
		hsv = hdd.Clone()
		return [unfres,hdd,hsv,4,0]



# Here we convert a constant bin structure like 5 bins from 0 to 5 i.e. [5,0,5]
# to a variable binning structure i.e. [0,1,2,3,4,5]
# This is just so we can use variable binning everywhere.	
def GetConstBinStructure(binning):
	# If it is already variably binned, return the binning itself.
	if len(binning)>3:
		return binning
	# Otherwise, return a variably binned structure.
	Width=(1.0*(binning[2]-binning[1]))/(1.0*binning[0])
	outputbins=[]
	for x in range(binning[0]+1):
		outputbins.append(binning[1]+Width*x)
	return outputbins

# The purpose of GetRescaling is to take two histograms (histo1 and histo2), given their binning, and return
# a string which can be used to rescale the histo2 to histo1, with errors.
def GetRescaling(histo1, histo2,binning,variable):
	# Initial lists to store histo information
	bincontent1=[]
	bincontent2=[]
	scalefactors=[]
	errors = []
	bindown=[]
	binup=[]

	# Convert binning to vairable binning
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	# Clone histo1 to the division histogram hdiv, and divide by histo2
	hdiv= histo1.Clone()
	hdiv.Sumw2()
	hdiv.Divide(histo2)
	scalefactors2=[]
	
	# Get the scale factors an errors
	for x in range(histo1.GetNbinsX()+1):
		if x==0:
			continue
		# histo1 and histo2 content
		bincontent1.append(histo1.GetBinContent(x))
		bincontent2.append(histo2.GetBinContent(x))
		# print histo1.GetBinCenter(x), histo2.GetBinCenter(x)
		# print histo1.GetBinContent(x), histo2.GetBinContent(x)
		# print ' ------------------------------------------- '
		scalefactors.append(1.0)
		# Relative errors for hdiv
		if hdiv.GetBinContent(x)>0:
			errors.append(hdiv.GetBinError(x)/hdiv.GetBinContent(x))
		else:
			errors.append(0.0)
		# Scale factors are just hdiv bins
		scalefactors2.append(hdiv.GetBinContent(x))
		if (bincontent2[x-1]>0.0):
			scalefactors[x-1]=(1.0*bincontent1[x-1])/(1.0*bincontent2[x-1])

		# Bin edges	
		bindown.append(histo1.GetBinLowEdge(x))
		binup.append(histo1.GetBinLowEdge(x)+histo1.GetBinWidth(x))
	
	# initiate the rescaling nad error strings
	scalestring='(0.0'	
	errorstring='(0.0'
	for x in range(len(bincontent1)):
		#print str(bindown[x]) + '<' +variable+'<'+ str(binup[x])+' : weight = '+str(round(scalefactors[x],4))+' +- '+str(round(errors[x],4))
		scalestring+=' + '+str(scalefactors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
		errorstring+=' + '+str(errors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
	scalestring+=')'
	errorstring+=')'
			
	return [scalestring,errorstring]


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

def DivWithErr(a,b):
	av = a[0]
	ae = a[1]
	bv = b[0]
	be = b[1]
	div = av/bv
	err = math.sqrt( (ae/av)**2 + (be/bv)**2 )
	err = err*div
	return [div,err]


def DivWithErr(a,b):
	av = a[0]
	ae = a[1]
	bv = b[0]
	be = b[1]
	div = av/bv
	err = math.sqrt( (ae/av)**2 + (be/bv)**2 )
	err = err*div
	return [div,err]


def GetSF(histolist,_d,_m,_o):

	_c = [[__h.GetBinContent(1),__h.GetBinError(1)] for __h in histolist]

	_D = _c[_d]
	_M = _c[_m]
	_OList = [_c[x] for x in _o]
	_O = []
	_O.append(sum([x[0] for x in _OList]))
	_O.append(math.sqrt(sum([x[1]*x[1] for x in _OList])))

	num = _D[0] - _O[0]
	num_err = math.sqrt(_D[1]*_D[1] + _O[1]*_O[1])
	denom = _M[0]
	denom_err = _M[1]

	sf = num/denom
	sf_err = sf*(  (num_err/num)**2.0 + (denom_err/denom)**2 )

	_SF = str(round(sf,4)) + ' +- '+str(round(sf_err,4))

	return [[sf,sf_err],_SF]

def IntWithError(histo):
	i1 = histo.Integral()
	i2 = 0.0
	e2 = 0.0
	for n in range(histo.GetNbinsX()+2):
		cont = histo.GetBinContent(n)
		err = histo.GetBinError(n)
		if cont>0:
			i2 += cont
			e2+= err*err	
	e2 = math.sqrt(e2)
	return [i1,i2,e2]


def MakeUnfoldedPlots(genvariables,recovariable, default_value, labelmods, binning,presentationbinning,recoselections,genselections,weight,optvar,FileDirectory,file_override,tau_override,tagname):

	##############################################################################
	#######     Basic setup - Get the files and trees, designate styles    #######
	##############################################################################
	eosroot = 'root://eoscms//eos/cms'

	JESTag = ('JetScale' in FileDirectory) and ('NoJESTag' not in 'pyplots')
	PHITag = 'PhiCorr' in FileDirectory
	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [(x.split('/')[-1]).replace('\n','') for x in os.popen('cmsLs '+FileDirectory+"| grep \".root\" | awk '{print $5}'").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		if 'Scale' in f or 'Match' in f or 'out' in f:
			continue
		fin = f.replace('\n','')
		fin_orig = f.replace('\n','')
		if 'altunf' in tagname:
			print '-'*35+' SHERPA '+'-'*35
			if 'WJets_MG' in fin:
				fin = fin.replace('WJets_MG','WJets_Sherpa')

		if 'powunf' in tagname:
			print '-'*35+' Powheg '+'-'*35
			if 'WJets_MG' in fin:
				fin = fin.replace('WJets_MG','WJets_Powheg')

		if JESTag==True:

			if 'Data' not in fin :
				print('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				if 'WJets_MG' in fin:
					print("t_MG = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	
					exec("t_MG = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	

			else:
				print('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

		elif PHITag==True:

			if True:
				print('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

				if 'WJets_MG' in fin:
					print("t_MG = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	
					exec("t_MG = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	

		else:
			if 'Data' not in fin:
				print('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

				if 'WJets_MG' in fin_orig:
					print("t_MG = TFile.Open(\""+eosroot+FileDirectory+"/"+fin_orig+"\")"+".Get(\""+TreeName+"\")")	
					exec("t_MG = TFile.Open(\""+eosroot+FileDirectory+"/"+fin_orig+"\")"+".Get(\""+TreeName+"\")")	

			else:
				print('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+eosroot+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")



	######################################
	## Some hacking for memory management
	######################################

	if True:
		# Get a list of open TTrees
		ListOfTrees = []
		staticlocals = locals()
	 	for lv in staticlocals:
	 		if 'TTree' in str(type(staticlocals[lv])):
	 			ListOfTrees.append(staticlocals[lv])

	 	# Get a list of open branches
		branches = [bb.GetName() for bb in  ListOfTrees[0].GetListOfBranches()]
		
		# Read this code into one long string
		vitaltext =  str(os.popen('cat '+sys.argv[0]).readlines())
		
		# Find branches not mentioned in the code, and compile them in a blacklist
		blacklist = []
		for b in branches:
			if b not in vitaltext:
				blacklist.append(b)

		# Loop over trees, and turn off branches in the blacklist. 		
		for atree in ListOfTrees:
			print ' ---------', atree, ' ------------'
			atree.SetBranchStatus('*',1)
			for b in branches:
				if b in blacklist:
					t_WJets_MG.SetBranchStatus(b,0)
				# print b, t_WJets_MG.GetBranchStatus(b)
		# sys.exit()

	######################################
	######################################
	######################################

	print 'Is the new modified JES being used (Data not unf Matrix?):', JESTag
	print 'Is the new Phi-Corrected MET Used:', PHITag

	print 'Using BTagging Algorithm: TCHEM'

	##############################################################################
	#######   Define selections and weights for normal, qcd, and unfolding #######
	##############################################################################

	if 'hltidiso' in tagname:
		weight = weight.replace(idisoweight,idisosysweight)
		weight += '*1.002'

	selection = recoselections
	gen_selection = genselections

	# QCDScale_Central = '(0)'
	print ' ###',selection
	qcdselection = selection.replace('IsoMu24Pass','1')
	print '     ###',qcdselection
	# return [0,0,0]
	qcdselection = qcdselection.replace('MT_muon1METR','99999')
	qcdselection = qcdselection.replace('RelIso_muon1','0.0')

	[genvariable,baregenvariable] = genvariables
	[xlabel,namelabel] = labelmods

	recomodvariable = recovariable	
	genmodvariable = genvariable
	if 'Eta' in recovariable:
		recomodvariable = 'abs('+recovariable+')'

	rivetselection = str(gen_selection).replace('_bare','')
	rivetmodvariable = str(genmodvariable.replace('_bare',''))

	varbinning=GetConstBinStructure(binning)

	## Always comment this - check for maximal bin with content!
	if False:
		binning = [700,0,7000]
		varbinning = GetConstBinStructure(binning)
		h_normrec_Data_test=CreateHisto('h_normrec_Data_test','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection+IsoMuCond,[0,20,1.0,1,1],[xlabel,"Events/bin"])
		maxbinwithcontent = []
		print 'Finding Maximal Bin Information'
		for x in range((h_normrec_Data_test.GetNbinsX())-2):
			cc = h_normrec_Data_test.GetBinContent(x+1)
			bb = h_normrec_Data_test.GetBinCenter(x+1)
			if cc > 0:
				maxbinwithcontent = [bb,cc]
			print bb, cc
		print 'Max Bin with content:',maxbinwithcontent, 'for recomodvariable:',recomodvariable
		sys.exit()

	##############################################################################
	#######   Preparation and stylistic modifications below                #######
	##############################################################################

	tmpname = "pyplots/tmp"+str(random.randint(0,1000000))+".root"
	tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	# Create Canvas
	c0 = TCanvas("c1","",1200,900)
	gStyle.SetOptStat(0)

	# These are the style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,20,1.0,1,1]
	DataCompStyle=[0,21,0.5,1,6]
	BlankRecoStyle=[0,21,.00001,1,0]
	DataUnfoldedStyle_2=[0,25,1,1,3]

	DataUnfoldedStyle=[0,21,1,1,1]
	DataUnfoldedStyle_b=[0,24,1,1,4]

	DataUnfoldedStyle_pseudo=[0,27,1,1,42]
	DataUnfoldedStyle_pseudoSG=[0,24,1,1,7]

	DataUnfoldedStyle_pseudo2=[0,26,1,1,2]
	DataUnfoldedStyle_pseudo2SG=[0,32,1,1,6]


	# X and Y axis labels for plot
	Label=[xlabel,"Events/bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]

	# Convert to variable binning.
	presentationbinning=ConvertBinning(presentationbinning)
	if 'bayes' in tagname:
		varbinning = presentationbinning


	##############################################################################
	#######      Matching Study                                            #######
	##############################################################################

	if False:
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(DeltaPhi_pfjet1muon1_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(DeltaPhi_pfjet2muon1_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(DeltaPhi_pfjet3muon1_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(DeltaPhi_pfjet4muon1_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(DeltaPhi_pfjet5muon1_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(Pt_pfjet1_pt20_hasgenmatch);   BRANCH(Eta_pfjet1_eta2p5_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(Pt_pfjet2_pt20_hasgenmatch);   BRANCH(Eta_pfjet2_eta2p5_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(Pt_pfjet3_pt20_hasgenmatch);   BRANCH(Eta_pfjet3_eta2p5_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(Pt_pfjet4_pt20_hasgenmatch);   BRANCH(Eta_pfjet4_eta2p5_hasgenmatch);
		# NTupleAnalyzer_V00_02_06_WPlusJets.C:	BRANCH(Pt_pfjet5_pt20_hasgenmatch);   BRANCH(Eta_pfjet5_eta2p5_hasgenmatch);


		# mcanvas Setup
		mc2 = TCanvas("mc2","",700,700)
		mcpad1 = TPad( 'mcpad1', 'mcpad1', 0.0, 0.31, 1.0, 1.0 )#divide mcanvas into pads
		mcpad2 = TPad( 'mcpad2', 'mcpad2', 0.0, 0.02, 1.0, 0.31 )
		# mcpad1.SetBottomMargin(0.0)
		# mcpad1.SetTopMargin(0.1)
		# mcpad1.SetLeftMargin(0.12)
		# mcpad1.SetRightMargin(0.1)
		# mcpad2.SetBottomMargin(0.3)
		# mcpad2.SetTopMargin(0.0)
		# mcpad2.SetLeftMargin(0.12)
		# mcpad2.SetRightMargin(0.1)
		mcpad1.Draw()
		mcpad2.Draw()
		mcpad1.SetLogy(1)
		mcpad1.cd()

		# +'*('+recomodvariable+'_hasgenmatch>0)'
		h_rec_WJets_moff=CreateHisto('h_rec_WJets_moff','W+Jets [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight,MCRecoStyle,Label)
		h_rec_WJets_mon=CreateHisto('h_rec_WJets_mon','W+Jets [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight+'*('+recomodvariable+'_hasgenmatch>0.5)',MCRecoStyle,Label)

		hs_rec_WJets_moff=RebinnedHisto("hs_rec_WJets_moff",'W+Jets (No Matching)',h_rec_WJets_moff,presentationbinning,WStackStyle,Label)
		hs_rec_WJets_mon=RebinnedHisto("hs_rec_WJets_mon",'W+Jets (Matching)',h_rec_WJets_mon,presentationbinning,WStackStyle,Label)

		hs_rec_WJets_moff.SetLineColor(1)
		hs_rec_WJets_moff.SetFillColor(1)
		hs_rec_WJets_moff.SetFillStyle(0)

		# print '*('+recomodvariable+'_hasgenmatch>0.5)'

		# for nn in range(100):
		# 	t_WJets_MG.GetEntry(nn)
		# 	print t_WJets_MG.Pt_pfjet1_pt20_hasgenmatch
		# print selection+weight+'*('+recomodvariable+'_hasgenmatch>0.5)'
		# h_rec_WJets_moff.Print('range')
		# hs_rec_WJets_moff.Print('range')
		# print h_rec_WJets_mon.Print('range')
		# print h_rec_WJets_moff.Print('range')

		# h_rec_WJets_mon.Print('range')
		# hs_rec_WJets_mon.Print('range')

		hs_rec_WJets_mon.SetLineColor(2)
		hs_rec_WJets_mon.SetFillColor(2)
		hs_rec_WJets_mon.SetFillStyle(0)

		hs_rec_WJets_mon.SetMarkerStyle(21)
		hs_rec_WJets_mon.SetMarkerSize(1)
		hs_rec_WJets_mon.SetMarkerColor(2)

		mmax = 10*(max([hs_rec_WJets_mon.GetBinContent(n) for n in range(hs_rec_WJets_mon.GetNbinsX()+1)] + [hs_rec_WJets_moff.GetBinContent(n) for n in range(hs_rec_WJets_moff.GetNbinsX()+1)]))
		hs_rec_WJets_mon.SetMaximum(mmax)
		hs_rec_WJets_moff.SetMaximum(mmax)

		hs_rec_WJets_moff.Draw("EHIST")
		hs_rec_WJets_mon.Draw("EPSAME")


		FixDrawLegend(mcpad1.BuildLegend( 0.6,  0.72,  0.9,  0.88,'' ))

		mcpad2.cd()

		matchrat = hs_rec_WJets_mon.Clone()
		matchrat.Divide(hs_rec_WJets_moff)
		matchrat.Print('range')
		matchrat.GetYaxis().SetTitle("Match Eff")

		mrmax = 1.01*(max([matchrat.GetBinContent(n+1) + matchrat.GetBinError(n+1)  for n in range(matchrat.GetNbinsX()) ]))
		mrmin = 0.99*(min([matchrat.GetBinContent(n+1) - matchrat.GetBinError(n+1) for n in range(matchrat.GetNbinsX()) ]))
		print [matchrat.GetBinContent(n+1)   for n in range(matchrat.GetNbinsX()+1) ]
		print [matchrat.GetBinError(n+1)  for n in range(matchrat.GetNbinsX()+1) ]

		print [matchrat.GetBinContent(n+1) + matchrat.GetBinError(n+1)  for n in range(matchrat.GetNbinsX()+1) ]
		print [matchrat.GetBinContent(n+1) - matchrat.GetBinError(n+1) for n in range(matchrat.GetNbinsX()+1) ]
		mrdelta = max([abs(1.-mrmax),abs(1.-mrmin)])
		mrmax = 1 + mrdelta
		mrmin = 1-mrdelta
		print mrmin,mrmax
		matchrat.SetMarkerStyle(21)
		matchrat.SetMarkerSize(1)
		matchrat.SetMarkerColor(2)
		matchrat.SetMinimum(mrmin)
		matchrat.SetMaximum(mrmax)
		matchrat.Draw("EP")
		munity=TLine(hs_rec_WJets_moff.GetXaxis().GetXmin(), 1.0 , hs_rec_WJets_moff.GetXaxis().GetXmax(),1.0)
		munity.Draw("SAME")

		mc2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_matchinghisto.png')
		mc2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_matchinghisto.pdf')



		# if ('--breaker' in sys.argv):
		if True:
			return [0,0,0]
		


	##############################################################################
	#######   Get Data-Driven Scale Factors                                #######
	##############################################################################


	scalefactoron = 'BGSFOn' in 'pyplots'

	if scalefactoron == True:

		if 'Count' in recovariable or len(varbinning)<=6:
			_sfbinning = varbinning

		else:
			# _sfbinning = [6,varbinning[0], varbinning[-1]]
			_sfbinning = [varbinning[0]]+presentationbinning[1:-1]+[varbinning[-1]]
			_sfbinning = ConvertBinning(_sfbinning)


		ttbar_selection = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(1.0424)*(PFJet30TCHEMCountCentral>1.5)')

		ttbar_selection1 = ttbar_selection.replace('PFJet30TCHEMCountCentral','PFJet30TCHEMCountEffDown')
		ttbar_selection2 = ttbar_selection.replace('PFJet30TCHEMCountCentral','PFJet30TCHEMCountEffUp')
		ttbar_selection3 = ttbar_selection.replace('PFJet30TCHEMCountCentral','PFJet30TCHEMCountMisDown')
		ttbar_selection4 = ttbar_selection.replace('PFJet30TCHEMCountCentral','PFJet30TCHEMCountMisUp')


		w_selection = selection
		z_selection = selection.replace('(Pt_muon2<0.000001)','(Pt_muon2>25)')

		LabelDD=[xlabel,"Data-Driven SF"]

		# Z
		__Z_h_rec_Data=CreateHisto('__Z_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,z_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__Z_h_rec_WJetsMG=CreateHisto('__Z_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,z_selection+weight,MCRecoStyle,LabelDD)
		__Z_h_rec_DiBoson=CreateHisto('__Z_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,z_selection+weight,DiBosonStackStyle,LabelDD)
		__Z_h_rec_ZJets=CreateHisto('__Z_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,z_selection+weight,ZStackStyle,LabelDD)
		__Z_h_rec_TTBar=CreateHisto('__Z_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,z_selection+weight,TTStackStyle,LabelDD)
		__Z_h_rec_SingleTop=CreateHisto('__Z_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,z_selection+weight,StopStackStyle,LabelDD)

		#W
		__W_h_rec_Data=CreateHisto('__W_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,w_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__W_h_rec_WJetsMG=CreateHisto('__W_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,w_selection+weight,MCRecoStyle,LabelDD)
		__W_h_rec_DiBoson=CreateHisto('__W_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,w_selection+weight,DiBosonStackStyle,LabelDD)
		__W_h_rec_ZJets=CreateHisto('__W_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,w_selection+weight,ZStackStyle,LabelDD)
		__W_h_rec_TTBar=CreateHisto('__W_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,w_selection+weight,TTStackStyle,LabelDD)
		__W_h_rec_SingleTop=CreateHisto('__W_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,w_selection+weight,StopStackStyle,LabelDD)

		#TTBar
		__T_h_rec_Data=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection+weight,StopStackStyle,LabelDD)

		#TTBar Variations
		__T_h_rec_Data1=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection1+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG1=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection1+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson1=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection1+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets1=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection1+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar1=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection1+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop1=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection1+weight,StopStackStyle,LabelDD)

		__T_h_rec_Data2=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection2+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG2=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection2+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson2=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection2+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets2=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection2+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar2=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection2+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop2=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection2+weight,StopStackStyle,LabelDD)

		__T_h_rec_Data3=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection3+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG3=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection3+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson3=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection3+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets3=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection3+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar3=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection3+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop3=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection3+weight,StopStackStyle,LabelDD)


		__T_h_rec_Data4=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection4+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG4=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection4+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson4=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection4+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets4=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection4+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar4=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection4+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop4=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection4+weight,StopStackStyle,LabelDD)



		__Z_histos = [__Z_h_rec_Data,	__Z_h_rec_WJetsMG,	__Z_h_rec_DiBoson,	__Z_h_rec_ZJets,	__Z_h_rec_TTBar,	__Z_h_rec_SingleTop]
		__W_histos = [__W_h_rec_Data,	__W_h_rec_WJetsMG,	__W_h_rec_DiBoson,	__W_h_rec_ZJets,	__W_h_rec_TTBar,	__W_h_rec_SingleTop]
		__T_histos = [__T_h_rec_Data,	__T_h_rec_WJetsMG,	__T_h_rec_DiBoson,	__T_h_rec_ZJets,	__T_h_rec_TTBar,	__T_h_rec_SingleTop]


		__T_histos1 = [__T_h_rec_Data1,	__T_h_rec_WJetsMG1,	__T_h_rec_DiBoson1,	__T_h_rec_ZJets1,	__T_h_rec_TTBar1,	__T_h_rec_SingleTop1]
		__T_histos2 = [__T_h_rec_Data2,	__T_h_rec_WJetsMG2,	__T_h_rec_DiBoson2,	__T_h_rec_ZJets2,	__T_h_rec_TTBar2,	__T_h_rec_SingleTop2]
		__T_histos3 = [__T_h_rec_Data3,	__T_h_rec_WJetsMG3,	__T_h_rec_DiBoson3,	__T_h_rec_ZJets3,	__T_h_rec_TTBar3,	__T_h_rec_SingleTop3]
		__T_histos4 = [__T_h_rec_Data4,	__T_h_rec_WJetsMG4,	__T_h_rec_DiBoson4,	__T_h_rec_ZJets4,	__T_h_rec_TTBar4,	__T_h_rec_SingleTop4]

		# [_zz,zz] = GetSF(__Z_histos,0,3,[1,2,4,5])
		# [_ww,ww] = GetSF(__W_histos,0,1,[2,3,4,5])
		# [_tt,tt] = GetSF(__T_histos,0,4,[1,2,3,5])
		# tt1 = GetSF(__T1_histos,0,4,[1,2,3,5])


		print " --------  Z REGION TABLE INFO -----------"
		_z_b = 'Bin '
		_z_d = 'Data '
		_z_z = 'Z '
		_z_tt = '$t \overline{t}$ '
		_z_w = 'W '
		_z_o = 'Other '


		_ra = range(__Z_h_rec_Data.GetNbinsX())
		if 'Count' in recovariable:
			_ra = [1,2,3,4,5,6] 
		for _nn in _ra:
			_nn += 1
			_z_b+= ' & '+str((round(__Z_h_rec_Data.GetBinCenter(_nn) ,4)))
			_z_d+= ' & '+str(int(round(__Z_h_rec_Data.GetBinContent(_nn) ,0)))
			_z_w+= ' & '+str(int(round(__Z_h_rec_WJetsMG.GetBinContent(_nn) ,0)))
			_z_z+= ' & '+str(int(round(__Z_h_rec_ZJets.GetBinContent(_nn) ,0)))
			_z_tt+= ' & '+str(int(round(__Z_h_rec_TTBar.GetBinContent(_nn) ,0)))
			_z_o+= ' & '+str(int(round(__Z_h_rec_SingleTop.GetBinContent(_nn) +__Z_h_rec_DiBoson.GetBinContent(_nn) ,0)))

		print _z_b
		print _z_d
		print _z_w
		print _z_z
		print _z_tt
		print _z_o

		print " -------- TT REGION TABLE INFO -----------"
		_t_b = 'Bin '
		_t_d = 'Data '
		_t_z = 'Z '
		_t_tt = '$t \overline{t}$ '
		_t_w = 'W '
		_t_o = 'Other '

		for _nn in _ra:
			_nn += 1
			_t_b+= ' & '+str((round(__T_h_rec_Data.GetBinCenter(_nn) ,4)))
			_t_d+= ' & '+str(int(round(__T_h_rec_Data.GetBinContent(_nn) ,0)))
			_t_w+= ' & '+str(int(round(__T_h_rec_WJetsMG.GetBinContent(_nn) ,0)))
			_t_z+= ' & '+str(int(round(__T_h_rec_ZJets.GetBinContent(_nn) ,0)))
			_t_tt+= ' & '+str(int(round(__T_h_rec_TTBar.GetBinContent(_nn) ,0)))						
			_t_o+= ' & '+str(int(round(__T_h_rec_SingleTop.GetBinContent(_nn) +__T_h_rec_DiBoson.GetBinContent(_nn) ,0)))

		print _t_b
		print _t_d
		print _t_w
		print _t_z
		print _t_tt
		print _t_o



		# Data Minus BG
		__Z_h_rec_Data.Add(__Z_h_rec_WJetsMG,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_DiBoson,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_TTBar,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_SingleTop,-1)

		# Data Minus BG
		__W_h_rec_Data.Add(__W_h_rec_ZJets,-1)
		__W_h_rec_Data.Add(__W_h_rec_DiBoson,-1)
		__W_h_rec_Data.Add(__W_h_rec_TTBar,-1)
		__W_h_rec_Data.Add(__W_h_rec_SingleTop,-1)

		# Data Minus BG
		__T_h_rec_Data.Add(__T_h_rec_WJetsMG,-1)
		__T_h_rec_Data.Add(__T_h_rec_DiBoson,-1)
		__T_h_rec_Data.Add(__T_h_rec_ZJets,-1)
		__T_h_rec_Data.Add(__T_h_rec_SingleTop,-1)

		__T_h_rec_Data1.Add(__T_h_rec_WJetsMG1,-1)
		__T_h_rec_Data1.Add(__T_h_rec_DiBoson1,-1)
		__T_h_rec_Data1.Add(__T_h_rec_ZJets1,-1)
		__T_h_rec_Data1.Add(__T_h_rec_SingleTop1,-1)

		__T_h_rec_Data2.Add(__T_h_rec_WJetsMG2,-1)
		__T_h_rec_Data2.Add(__T_h_rec_DiBoson2,-1)
		__T_h_rec_Data2.Add(__T_h_rec_ZJets2,-1)
		__T_h_rec_Data2.Add(__T_h_rec_SingleTop2,-1)

		__T_h_rec_Data3.Add(__T_h_rec_WJetsMG3,-1)
		__T_h_rec_Data3.Add(__T_h_rec_DiBoson3,-1)
		__T_h_rec_Data3.Add(__T_h_rec_ZJets3,-1)
		__T_h_rec_Data3.Add(__T_h_rec_SingleTop3,-1)		

		__T_h_rec_Data4.Add(__T_h_rec_WJetsMG4,-1)
		__T_h_rec_Data4.Add(__T_h_rec_DiBoson4,-1)
		__T_h_rec_Data4.Add(__T_h_rec_ZJets4,-1)
		__T_h_rec_Data4.Add(__T_h_rec_SingleTop4,-1)

		# Data / MC
		__Z_h_rec_Data.Divide(__Z_h_rec_ZJets)
		__W_h_rec_Data.Divide(__W_h_rec_WJetsMG)
		__T_h_rec_Data.Divide(__T_h_rec_TTBar)

		__T_h_rec_Data1.Divide(__T_h_rec_TTBar1)
		__T_h_rec_Data2.Divide(__T_h_rec_TTBar2)
		__T_h_rec_Data3.Divide(__T_h_rec_TTBar3)
		__T_h_rec_Data4.Divide(__T_h_rec_TTBar4)


		# Sum MC For Purity
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_DiBoson)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_TTBar)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_SingleTop)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_ZJets)


		# Sum MC For Purity
		__T_h_rec_WJetsMG.Add(__T_h_rec_DiBoson)
		__T_h_rec_WJetsMG.Add(__T_h_rec_TTBar)
		__T_h_rec_WJetsMG.Add(__T_h_rec_SingleTop)
		__T_h_rec_WJetsMG.Add(__T_h_rec_ZJets)
			
		__T_h_rec_WJetsMG1.Add(__T_h_rec_DiBoson1)
		__T_h_rec_WJetsMG1.Add(__T_h_rec_TTBar1)
		__T_h_rec_WJetsMG1.Add(__T_h_rec_SingleTop1)
		__T_h_rec_WJetsMG1.Add(__T_h_rec_ZJets1)

		__T_h_rec_WJetsMG2.Add(__T_h_rec_DiBoson2)
		__T_h_rec_WJetsMG2.Add(__T_h_rec_TTBar2)
		__T_h_rec_WJetsMG2.Add(__T_h_rec_SingleTop2)
		__T_h_rec_WJetsMG2.Add(__T_h_rec_ZJets2)

		__T_h_rec_WJetsMG3.Add(__T_h_rec_DiBoson3)
		__T_h_rec_WJetsMG3.Add(__T_h_rec_TTBar3)
		__T_h_rec_WJetsMG3.Add(__T_h_rec_SingleTop3)
		__T_h_rec_WJetsMG3.Add(__T_h_rec_ZJets3)

		__T_h_rec_WJetsMG4.Add(__T_h_rec_DiBoson4)
		__T_h_rec_WJetsMG4.Add(__T_h_rec_TTBar4)
		__T_h_rec_WJetsMG4.Add(__T_h_rec_SingleTop4)
		__T_h_rec_WJetsMG4.Add(__T_h_rec_ZJets4)						
			

		# Sum MC For Purity
		__W_h_rec_TTBar.Add(__W_h_rec_DiBoson)
		__W_h_rec_TTBar.Add(__W_h_rec_ZJets)
		__W_h_rec_TTBar.Add(__W_h_rec_SingleTop)
		__W_h_rec_TTBar.Add(__W_h_rec_WJetsMG)



		# Divide MC by BG for Purity	
		__Z_h_rec_ZJets.Divide(__Z_h_rec_WJetsMG)
		__T_h_rec_TTBar.Divide(__T_h_rec_WJetsMG)
		__W_h_rec_WJetsMG.Divide(__W_h_rec_TTBar)


		__T_h_rec_TTBar1.Divide(__T_h_rec_WJetsMG1)
		__T_h_rec_TTBar2.Divide(__T_h_rec_WJetsMG2)
		__T_h_rec_TTBar3.Divide(__T_h_rec_WJetsMG3)
		__T_h_rec_TTBar4.Divide(__T_h_rec_WJetsMG4)


		# Fill Style Fix
		__Z_h_rec_Data.SetFillStyle(0)
		__W_h_rec_Data.SetFillStyle(0)
		__T_h_rec_Data.SetFillStyle(0)

		__Z_h_rec_ZJets.SetFillStyle(0)
		__T_h_rec_TTBar.SetFillStyle(0)
		__W_h_rec_WJetsMG.SetFillStyle(0)

		# Color Fix
		__Z_h_rec_Data.SetMarkerStyle(22)
		__W_h_rec_Data.SetMarkerStyle(21)
		__T_h_rec_Data.SetMarkerStyle(23)	
		__Z_h_rec_Data.SetMarkerSize(2)
		__W_h_rec_Data.SetMarkerSize(2)
		__T_h_rec_Data.SetMarkerSize(2)	
		__Z_h_rec_Data.SetMarkerColor(2)
		__W_h_rec_Data.SetMarkerColor(6)
		__T_h_rec_Data.SetMarkerColor(4)
		__Z_h_rec_Data.SetFillColor(2)
		__W_h_rec_Data.SetFillColor(6)
		__T_h_rec_Data.SetFillColor(4)
		__Z_h_rec_Data.SetLineColor(2)
		__W_h_rec_Data.SetLineColor(6)
		__T_h_rec_Data.SetLineColor(4)


		__Z_h_rec_ZJets.SetLineColor(2)
		__Z_h_rec_ZJets.SetLineStyle(2)
		__Z_h_rec_ZJets.SetMarkerColor(2)
		__Z_h_rec_ZJets.SetFillColor(2)



		__T_h_rec_TTBar.SetLineStyle(3)
		__T_h_rec_TTBar.SetLineColor(4)
		__T_h_rec_TTBar.SetMarkerColor(4)
		__T_h_rec_TTBar.SetFillColor(4)


		__W_h_rec_WJetsMG.SetLineStyle(6)
		__W_h_rec_WJetsMG.SetLineColor(6)
		__W_h_rec_WJetsMG.SetMarkerColor(6)
		__W_h_rec_WJetsMG.SetFillColor(6)


		__Z_h_rec_Data.SetMaximum(2.0)
		__Z_h_rec_Data.SetMinimum(0.0)

		__Z_h_rec_Data.Draw("EP")
		__Z_h_rec_ZJets.Draw("EHISTSAME")

		# __W_h_rec_Data.Draw("EPSAME")
		# __W_h_rec_WJetsMG.Draw("EHISTSAME")

		# Fix TTBar Error Bands
		print '------------ TTBAR SF BREAKDOWN -----------'
		for ibin in range((__T_h_rec_Data.GetNbinsX())+1):
			_t = __T_h_rec_Data.GetBinContent(ibin)
			_t1 = __T_h_rec_Data1.GetBinContent(ibin)
			_t2 = __T_h_rec_Data2.GetBinContent(ibin)
			_t3 = __T_h_rec_Data3.GetBinContent(ibin)
			_t4 = __T_h_rec_Data4.GetBinContent(ibin)

			_te = __T_h_rec_Data.GetBinError(ibin)
			_e1 = (_t1 - _t)
			_e2 = (_t2 - _t)
			_e3 = (_t3 - _t)
			_e4 = (_t4 - _t)
			_err1 = max([abs(_e1),abs(_e2)])
			_err2 = max([abs(_e3),abs(_e4)])

			_errsigma = .0465*_t
			_errstat = __T_h_rec_Data.GetBinError(ibin)

			print ibin, _t, _t1, _t2, _t3, _t4, [[_e1, _e2], [_e3, _e4]]
			_toterr = math.sqrt(_errsigma**2 + _errstat**2 + _err1**2 + _err2**2)

			print '    Error Transform:',_errstat,' --> ',_toterr

			__T_h_rec_Data.SetBinError(ibin,_toterr)



		__T_h_rec_Data.Draw("EPSAME")
		__T_h_rec_TTBar.Draw("EHISTSAME")

		leg = TLegend(0.19,0.76,0.35,0.93,"","brNDC")
		leg.SetTextFont(42)
		leg.SetFillColor(0)
		leg.SetBorderSize(0)
		leg.SetTextSize(.03)
		leg.AddEntry(__Z_h_rec_Data,"Z+Jets SF")
		leg.AddEntry(__T_h_rec_Data,"TTBar SF")
		# leg.AddEntry(__W_h_rec_Data,"W+Jets SF")
		leg.Draw()

		leg2 = TLegend(0.36,0.76,0.52,0.93,"","brNDC")
		leg2.SetTextFont(42)
		leg2.SetFillColor(0)
		leg2.SetBorderSize(0)
		leg2.SetTextSize(.03)
		leg2.AddEntry(__Z_h_rec_ZJets,"Z+Jets Pur")
		leg2.AddEntry(__T_h_rec_TTBar,"TTBar Pur")
		# leg2.AddEntry(__W_h_rec_WJetsMG,"W+Jets Pur")
		leg2.Draw()


		_zres = '*('
		_zres_unc = '*('


		print " -------- SF VALUES TABLE INFO -----------"
		_s_b = ' Bin '
		_s_z = ' Z SF '
		_s_t = ' $t \overline{t} $ '


		for xx in range(__Z_h_rec_Data.GetNbinsX()):
			_n = xx+1
			_halfwidth = 0.5*__Z_h_rec_Data.GetBinWidth(_n)
			_center = __Z_h_rec_Data.GetBinCenter(_n)
			_lhs = _center - _halfwidth
			_rhs = _center + _halfwidth
			_cont = __Z_h_rec_Data.GetBinContent(_n)
			_err = __Z_h_rec_Data.GetBinError(_n)
			_cut = '('+recomodvariable+'>='+str(round(_lhs,3))+')*('+recomodvariable+'<'+str(round(_rhs,3))+')'
			_vsf = '*'+str(round(_cont,3))
			_ver = '*'+str(round(_err,3))
			_zres += _cut+_vsf	
			_zres_unc += _cut+_ver

			if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):
				_s_b += str(round(_center,4))
				_s_z += ' & '+ str(round(_cont,3)) + '$ \\pm $ '+str(round(_err,3))

			if xx != range(__Z_h_rec_Data.GetNbinsX())[-1]:
				_zres += ' + '
				_zres_unc += ' + '		
		_zres += ')'
		_zres_unc += ')'


		_tres = '*('
		_tres_unc = '*('

		for xx in range(__T_h_rec_Data.GetNbinsX()):
			_n = xx+1
			_halfwidth = 0.5*__T_h_rec_Data.GetBinWidth(_n)
			_center = __T_h_rec_Data.GetBinCenter(_n)
			_lhs = _center - _halfwidth
			_rhs = _center + _halfwidth
			_cont = __T_h_rec_Data.GetBinContent(_n)
			_err = __T_h_rec_Data.GetBinError(_n)
			_cut = '('+recomodvariable+'>='+str(round(_lhs,3))+')*('+recomodvariable+'<'+str(round(_rhs,3))+')'
			_vsf = '*'+str(round(_cont,3))
			_ver = '*'+str(round(_err,3))
			_tres += _cut+_vsf	
			_tres_unc += _cut+_ver

			if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):

				_s_t += ' & '+ str(round(_cont,3)) + '$ \\pm $ '+str(round(_err,3))

			if xx != range(__T_h_rec_Data.GetNbinsX())[-1]:
				_tres += ' + '
				_tres_unc += ' + '		
		_tres += ')'
		_tres_unc += ')'

		print _s_b
		print _s_z
		print _s_t

		print " -------- CONTORL REGION TABLES COMPLETE -----------"


		sfunity=TLine(__T_h_rec_Data.GetXaxis().GetXmin(), 1.0 , __T_h_rec_Data.GetXaxis().GetXmax(),1.0)
		sfunity.Draw("SAME")
		c0.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_sfhisto.png')
		c0.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_sfhisto.pdf')

		# return [0,0,0]
		# sys.exit()

	fW = '*(1.0)'
	fZ = '*(1.0)'
	fT = '*(1.0424)'
	fsT = '*(1.0)'
	fV = '*(1.0)'



	if scalefactoron == True:
		fZ = _zres
		fT = _tres

	print 'Z SF:',fZ
	print 'TTBar SF:',fT

	print 'Scale factor derivation complete!'


	if 'bgnorm_plus' in tagname:
		print 'REASSIGNING BACKGROUD NORMALIZATION - POSITIVE MODIFICATIONS'
		fZ += '*(1.04331)'
		fT += '*(1.0465)' 
		fsT += '*(1.06)'
		fV += '*(1.04)'



	if 'bgnorm_minus' in tagname:
		print 'REASSIGNING BACKGROUD NORMALIZATION - NEGATIVE MODIFICATIONS'
		fZ += '*(0.95669)'
		fT += '*(0.9535)' 
		fsT += '*(0.94)'
		fV += '*(0.96)'


	# sys.exit()





	##############################################################################
	#######     Top Right - Background Subtracted Distributions            #######
	##############################################################################


	# tmpname = "pyplots/tmp"+str(random.randint(0,1000000))+".root"
	# tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	# Create Canvas
	c1 = TCanvas("c1","",1200,900)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)


	c1.cd(2)

	# The selection for the reco variable, constrained to the range the final distribution will be shown.
	# selection+='*('+recovariable+'<'+str(presentationbinning[-1])+')*('+recovariable+'>'+str(presentationbinning[0])+')'
	# The selection for the gen variable. Larger range for the underflow/overflow. '(Pt_genmuon1>1.0)' also demands that a gen-muon is present. 
	# The trees should otherwise be skimmed for a reco muon to be present.

	# print rivetselection
	for x in RivetGenBranchMap:
		if x[0] in rivetselection:
			rivetselection = rivetselection.replace(x[0],x[1])
		if x[0] in rivetmodvariable:
			rivetmodvariable = rivetmodvariable.replace(x[0],x[1])

	
	nrivet = (RIVETMadGraph.split('_')[-1]).replace('.root','')+'.0'
	rivetselection = 'evweight*(31314*4955.0/'+nrivet+')*'+rivetselection
	t_rivet = TFile.Open(RIVETMadGraph,'READ').Get('RivetTree')


	nvbin = len(varbinning)
	vbinmin = 1
	vbinmax = nvbin-1

	npbin = len(presentationbinning)
	pbinmin = 1
	pbinmax = npbin-1

	gtag = 'MadGraph'
	if 'altunf' in tagname:
		gtag = 'Sherpa'

	if 'powunf' in tagname:
		gtag = 'Powheg'

	selection_norm = selection+"*(MT_muon1METR>50.0)"
	gen_selection_norm = gen_selection+"*(MT_muon1METR>50.0)"

	print 'baregenvariable:',baregenvariable
	print 'recomodvariable:',recomodvariable
	print 'selection_norm+weight+fW',selection_norm+weight+fW

	h_normgen_WJets=CreateHisto('h_normgen_WJets','W+Jets MG [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection_norm+'*weight_gen*4955',MCGenStyle,Label)
	h_normrec_WJets=CreateHisto('h_normrec_WJets','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection_norm+weight+fW,MCRecoStyle,Label)
	h_normrec_WJetsMG=CreateHisto('h_normrec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,selection_norm+weight+fW,MCRecoStyle,Label)

	# Data
	h_normrec_Data=CreateHisto('h_normrec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection_norm+IsoMuCond,DataRecoStyle,Label)
	# Other Backgrounds
	h_normrec_DiBoson=CreateHisto('h_normrec_DiBoson','DiBoson [Pythia]',t_DiBoson,recomodvariable,varbinning,selection_norm+weight+fV,DiBosonStackStyle,Label)

	h_normrec_ZJets=CreateHisto('h_normrec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,selection_norm+weight+fZ,ZStackStyle,Label)
	h_normrec_TTBar=CreateHisto('h_normrec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,selection_norm+weight+fT,TTStackStyle,Label)
	h_normrec_SingleTop=CreateHisto('h_normrec_SingleTop','SingleTop [Powheg]',t_SingleTop,recomodvariable,varbinning,selection_norm+weight+fsT,StopStackStyle,Label)

	print 'D:',h_normrec_Data.Integral()
	print 'Z:',h_normrec_ZJets.Integral()
	print 'T:',h_normrec_TTBar.Integral()
	print 'V:',h_normrec_DiBoson.Integral()
	print 'S:',h_normrec_SingleTop.Integral()
	print 'W:',h_normrec_WJets.Integral() 



	###############################################################################################
	############### MULTIPLE ITERATION QCD DETERMINATION METHOD  ##################################
	###############################################################################################

	###############################################################################################

	print ' -------- QCD ITERATIVE METHOD -----------'
	# Get initial W scale factors with MT>50 using no QCD
	_wsf   = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() ) / (	h_normrec_WJets.Integral() )
	_wsfMG   = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() ) / (	h_normrec_WJetsMG.Integral() )

	wsfoff = 'WSFOFF' in 'pyplots'
	if wsfoff == True:
		_wsf   = 1.0
		_wsfMG = 1.0
	fW = '*('+str(round(_wsf,4))+')'
	fWMG = '*('+str(round(_wsfMG,4))+')'


	# W + Jets Contributions (Normalized for display)
	# h_gen_WJets=CreateHisto('h_gen_WJets_aod','W+Jets '+gtag+' [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955',MCGenStyle,Label)
	h_gen_WJets1=CreateHisto('h_gen_WJets1','W+Jets MG [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955'+fW,MCGenStyle,Label)

	print '-'*50+'\n'+rivetmodvariable+'\n'+rivetselection+'\n'+'-'*50+'\n'	
	# h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# print '-'*50+'\n'+recomodvariable+'\n'+selection+weight+'\n'+'-'*50+'\n'	
	h_rec_WJets1=CreateHisto('h_rec_WJets1','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight+fW,MCRecoStyle,Label)
	h_rec_WJetsMG1=CreateHisto('h_rec_WJetsMG1','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,selection+weight+fWMG,MCRecoStyle,Label)

	# Data
	h_rec_Data=CreateHisto('h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection+IsoMuCond,DataRecoStyle,Label)
	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','DiBoson [Pythia]',t_DiBoson,recomodvariable,varbinning,selection+weight+fV,DiBosonStackStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,selection+weight+fZ,ZStackStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,selection+weight+fT,TTStackStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','SingleTop [Powheg]',t_SingleTop,recomodvariable,varbinning,selection+weight+fsT,StopStackStyle,Label)

	print ' W: ',h_rec_WJets1.Integral()
	print ' Z: ',h_rec_ZJets.Integral()
	print ' TT:',h_rec_TTBar.Integral()
	print ' VV:',h_rec_DiBoson.Integral()
	print ' t: ',h_rec_SingleTop.Integral()
	print ' D: ',h_rec_Data.Integral()
	# sys.exit()

	# QCD Setup
	selection_nomt = selection.replace('MT_muon1METR','99999')
	nonisotrees = [t_TTBar,t_SingleTop,t_DiBoson,t_ZJets_MG]
	nonisotreenames = ['t_TTBarNonIso','t_SingleTopNonIso','t_DiBosonNonIso','t_ZJets_MGNonIso']
	treesf = [fT,fsT,fV,fZ]

	regtrees = [t_TTBar,t_SingleTop,t_DiBoson,t_ZJets_MG]
	regtreenames = ['t_TTBar','t_SingleTop','t_DiBoson','t_ZJets_MG']

	# Initial MT<50 Iso and NonIso histos using the data
	__h_noniso_qcd=CreateHisto('__h_noniso_qcd','QCD',t_SingleMuData,recomodvariable,varbinning,qcdselection+'*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*(MT_muon1METR<50)',QCDStackStyle,Label)
	__h_iso_reg=CreateHisto('__h_iso_reg','__h_iso_reg',t_SingleMuData,recovariable,varbinning,selection_nomt+'*(MT_muon1METR<50)*(IsoMu24Pass>0.5)',WStackStyle,Label)


	# Subtract non-W background from the MT<50 Iso and NonIso data histos
	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]
		print nonisotreenames[tn], __sf
		tmpname = '__h_noniso_mc'+str(random.randint(0,1000000))
		__h_noniso_qcd.Add(CreateHisto(tmpname,tmpname,tt,recomodvariable,varbinning,qcdselection+weight+'*(RelIso_muon1>0.15)*(MT_muon1METR<50)*(-1)'+__sf,QCDStackStyle,Label))
		tmpname = '__h_iso_mc'+str(random.randint(0,1000000))
		__h_iso_reg.Add(CreateHisto(tmpname,tmpname,regtrees[tn],recovariable,varbinning,qcdselection+'*(RelIso_muon1<0.15)'+weight+'*(-1)*(IsoMu24Pass>0.5)*(MT_muon1METR<50)'+__sf,WStackStyle,Label))
		tn += 1

	# Use scale-factor adjusted W to subtract from MT<50 Iso and NonIso histos
	__h_noniso_w =CreateHisto('__h_noniso_w','__h_noniso_w',t_WJets_MG,recovariable,varbinning,qcdselection+weight+'*(RelIso_muon1>0.15)*(MT_muon1METR<50)*(-1)',WStackStyle,Label) 
	__h_iso_w =CreateHisto('__h_iso_w','__h_iso_w',t_WJets_MG,recovariable,varbinning,qcdselection+'*(RelIso_muon1<0.15)'+weight+'*(-1)*(IsoMu24Pass>0.5)*(MT_muon1METR<50)',WStackStyle,Label) 

	__h_noniso_w.Scale(_wsf)
	__h_iso_w.Scale(_wsf)

	__h_noniso_qcd.Add(__h_noniso_w)
	__h_iso_reg.Add(__h_iso_w)


	# In case of jet multiplicity, need binwise scale-factors
	dovariableqcd = ('VariableQCD' in 'pyplots') or ('PFJet30Count' in recomodvariable)

	# Get basic QCDSF fake rate
	if __h_noniso_qcd.GetEntries()>0:
		QCDSF = __h_iso_reg.Integral()/__h_noniso_qcd.Integral()

	else:
		QCDSF = 0.02

	# Fix for bin-wise scale factors
	if dovariableqcd == True:
		QCDSF  = 1.0
		qcdsfhisto = __h_iso_reg.Clone()
		qcdsfhisto.Divide(__h_noniso_qcd)

	else:
		qcdsfhisto = __h_iso_reg.Clone()
		for xx in range(qcdsfhisto.GetNbinsX()):
			_n = xx+1
			qcdsfhisto.SetBinContent(_n,1.0)
			qcdsfhisto.SetBinError(_n,0.0)


	# Now the actual QCD measurement with MT>50
	h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD',t_SingleMuData,recomodvariable,varbinning,qcdselection+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*('+str(QCDSF)+')',QCDStackStyle,Label)
	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]

		tmpname = 'h_noniso_mc'+str(random.randint(0,1000000))
		h_rec_QCDMu.Add(CreateHisto(tmpname,tmpname,tt,recomodvariable,varbinning,qcdselection+weight+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')'+__sf,QCDStackStyle,Label))
		tn += 1

	# Subtract SF-adjusted W from QCD Measurement
	__h_reg_noniso_w =CreateHisto('__h_reg_iso_w','__h_iso_w',t_WJets_MG,recovariable,varbinning,qcdselection+weight+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')',QCDStackStyle,Label) 
	__h_reg_noniso_w.Scale(_wsf)
	h_rec_QCDMu.Add(__h_reg_noniso_w)
	h_rec_QCDMu.Multiply(qcdsfhisto)


	# Finally, use the above histos and tools to iterate several times, correcting the WSF and QCD until they equilibriate

	for hh in [__h_reg_noniso_w, __h_noniso_w, __h_iso_w, __h_noniso_qcd, __h_iso_reg]:
		for xx in range(hh.GetNbinsX()):
			_n = xx+1
			hh.SetBinError(_n,0.0)

	print ' ====== QCD ITERATIVE METHOD ====== '
	print 'Iteration  fW  QCDSF  QCDErr'
	for x in range(15):
		# print ' ---   QCD ITERATION ',x,' ---'
		# print "Iterative QCD, W SF:", _wsf
		# print "Iterative QCD, QCD SF", QCDSF
		# print "Int error QCD,",IntWithError(h_rec_QCDMu)

		print x, _wsf, QCDSF, IntWithError(h_rec_QCDMu)

		# New W Scale Factor
		_wsf_new   = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() + h_rec_QCDMu.Integral() ) / (	h_normrec_WJets.Integral() )
		_wsfMG_new   = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() + h_rec_QCDMu.Integral() ) / (	h_normrec_WJetsMG.Integral() )

		if wsfoff == True:
			_wsf_new   = 1.0
			_wsfMG_new = 1.0
		fW = '*('+str(round(_wsf_new,4))+')'
		fWMG = '*('+str(round(_wsf_new,4))+')'


		# Remove W from Iso and NonIso MT <50 Histos
		__h_noniso_w.Scale(-1)
		__h_iso_w.Scale(-1)

		__h_noniso_qcd.Add(__h_noniso_w)
		__h_iso_reg.Add(__h_iso_w)


		# Scale W Iso and Non Iso MT<50 Histos to new Scale Factor
		__h_noniso_w.Scale(-1*_wsf_new/_wsf)
		__h_iso_w.Scale(-1*_wsf_new/_wsf)	


		# Modify QCD Iso and Non Iso MT<50 histos for new W contribution
		__h_noniso_qcd.Add(__h_noniso_w)
		__h_iso_reg.Add(__h_iso_w)

		# Get new QCDSF 
		if __h_noniso_qcd.Integral()>0:
			QCDSF_new = __h_iso_reg.Integral()/__h_noniso_qcd.Integral()

		else:
			QCDSF_new = 0.02

		for xx in range(qcdsfhisto.GetNbinsX()):
			_n = xx+1
			qcdsfhisto.SetBinError(_n,0.0)

		if dovariableqcd == True:
			QCDSF_new  = 1.0
			qcdsfhisto_new = __h_iso_reg.Clone()
			qcdsfhisto_new.Divide(__h_noniso_qcd)
			for xx in range(qcdsfhisto_new.GetNbinsX()):
				_n = xx+1
				qcdsfhisto_new.SetBinError(_n,0.0)
		else:
			qcdsfhisto_new = __h_iso_reg.Clone()

			for xx in range(qcdsfhisto_new.GetNbinsX()):
				_n = xx+1
				qcdsfhisto_new.SetBinContent(_n,1.0)
				qcdsfhisto_new.SetBinError(_n,0.0)

		# Remove W from noniso MT>50 QCD histo
		__h_reg_noniso_w.Scale(-1)
		h_rec_QCDMu.Add(__h_reg_noniso_w)

		# Scale MT>50 QCD histo to new QCD SF
		h_rec_QCDMu.Scale(QCDSF_new/QCDSF)
		h_rec_QCDMu.Multiply(qcdsfhisto_new)
		h_rec_QCDMu.Divide(qcdsfhisto)


		# Modify new W MT>50 contribution for new WSF and QCD SF
		__h_reg_noniso_w.Scale(-1*(QCDSF_new/QCDSF)*(_wsf_new/_wsf))
		__h_reg_noniso_w.Multiply(qcdsfhisto_new)
		__h_reg_noniso_w.Divide(qcdsfhisto)


		# Add W MT>50 contribution back to QCD MT>50 histo
		h_rec_QCDMu.Add(__h_reg_noniso_w)

		# Reset Scale Factors for next iteration

		QCDSF = QCDSF_new
		_wsf = _wsf_new
		qcdsfhisto = qcdsfhisto_new.Clone()



	# print ' ---- EVENT BREAKDOWN ----'
	# print ' W: ',h_rec_WJets1.Integral()
	# print ' Z: ',h_rec_ZJets.Integral()
	# print ' TT:',h_rec_TTBar.Integral()
	# print ' VV:',h_rec_DiBoson.Integral()
	# print ' t: ',h_rec_SingleTop.Integral()
	# print ' D: ',h_rec_Data.Integral()
	# print ' Q: ',h_rec_QCDMu.Integral()
	# print ' Perc Q: ', h_rec_QCDMu.Integral()/( h_rec_WJets1.Integral() + h_rec_ZJets.Integral() + h_rec_TTBar.Integral() + h_rec_DiBoson.Integral() + h_rec_SingleTop.Integral() + h_rec_QCDMu.Integral())


	# print '\n ---- Unc BREAKDOWN Bin (jj) [Content, Error] ----'

	# for jj in range(h_rec_WJets1.GetNbinsX()+2):
	# 	print '\n ---- Unc BREAKDOWN Bin (',jj,') [Content, Error] ----'
	# 	print ' (',jj,') Bin Center: ',h_rec_WJets1.GetBinCenter(jj)
	# 	print ' (',jj,') Err W: ',h_rec_WJets1.GetBinContent(jj),h_rec_WJets1.GetBinError(jj)
	# 	print ' (',jj,') Err Z: ',h_rec_ZJets.GetBinContent(jj),h_rec_ZJets.GetBinError(jj)
	# 	print ' (',jj,') Err TT:',h_rec_TTBar.GetBinContent(jj),h_rec_TTBar.GetBinError(jj)
	# 	print ' (',jj,') Err VV:',h_rec_DiBoson.GetBinContent(jj),h_rec_TTBar.GetBinError(jj)
	# 	print ' (',jj,') Err t: ',h_rec_SingleTop.GetBinContent(jj),h_rec_SingleTop.GetBinError(jj)
	# 	print ' (',jj,') Err D: ',h_rec_Data.GetBinContent(jj),h_rec_Data.GetBinError(jj)
	# 	print ' (',jj,') Err Q: ',h_rec_QCDMu.GetBinContent(jj),h_rec_QCDMu.GetBinError(jj)
	# 	print ' (',jj,') Err Perc Q: ', h_rec_QCDMu.GetBinContent(jj)/( 0.00001+h_rec_WJets1.GetBinContent(jj) + h_rec_ZJets.GetBinContent(jj) + h_rec_TTBar.GetBinContent(jj) + h_rec_DiBoson.GetBinContent(jj) + h_rec_SingleTop.GetBinContent(jj) + h_rec_QCDMu.GetBinContent(jj)), h_rec_QCDMu.GetBinError(jj)/( 0.00001+h_rec_WJets1.GetBinError(jj) + h_rec_ZJets.GetBinError(jj) + h_rec_TTBar.GetBinError(jj) + h_rec_DiBoson.GetBinError(jj) + h_rec_SingleTop.GetBinError(jj) + h_rec_QCDMu.GetBinError(jj))

	print '\n ---- QCD BREAKDOWN Bin (jj) [Content, Error] ----'

	for jj in range(h_rec_QCDMu.GetNbinsX()+2):
		ibin = h_rec_QCDMu.GetBinCenter(jj)
		ic = h_rec_QCDMu.GetBinContent(jj)
		ie = h_rec_QCDMu.GetBinError(jj)
		print ibin, ic, ie



	# print '\n ---- Unc BREAKDOWN Bin (2) ----'
	# print ' (2) Err W: ',h_rec_WJets1.GetBinContent(2),h_rec_WJets1.GetBinError(2)
	# print ' (2) Err Z: ',h_rec_ZJets.GetBinContent(2),h_rec_ZJets.GetBinError(2)
	# print ' (2) Err TT:',h_rec_TTBar.GetBinContent(2),h_rec_TTBar.GetBinError(2)
	# print ' (2) Err VV:',h_rec_DiBoson.GetBinContent(2),h_rec_TTBar.GetBinError(2)
	# print ' (2) Err t: ',h_rec_SingleTop.GetBinContent(2),h_rec_SingleTop.GetBinError(2)
	# print ' (2) Err D: ',h_rec_Data.GetBinContent(2),h_rec_Data.GetBinError(2)
	# print ' (2) Err Q: ',h_rec_QCDMu.GetBinContent(2),h_rec_QCDMu.GetBinError(2)
	# print ' (2) Err Perc Q: ', h_rec_QCDMu.GetBinContent(2)/( 0.00001+h_rec_WJets1.GetBinContent(2) + h_rec_ZJets.GetBinContent(2) + h_rec_TTBar.GetBinContent(2) + h_rec_DiBoson.GetBinContent(2) + h_rec_SingleTop.GetBinContent(2) + h_rec_QCDMu.GetBinContent(2)), h_rec_QCDMu.GetBinError(2)/( 0.00001+h_rec_WJets1.GetBinError(2) + h_rec_ZJets.GetBinError(2) + h_rec_TTBar.GetBinError(2) + h_rec_DiBoson.GetBinError(2) + h_rec_SingleTop.GetBinError(2) + h_rec_QCDMu.GetBinError(2))




	# print '\n ---- Unc BREAKDOWN Bin (3) ----'
	# print ' (3) Err W: ',h_rec_WJets1.GetBinContent(3),h_rec_WJets1.GetBinError(3)
	# print ' (3) Err Z: ',h_rec_ZJets.GetBinContent(3),h_rec_ZJets.GetBinError(3)
	# print ' (3) Err TT:',h_rec_TTBar.GetBinContent(3),h_rec_TTBar.GetBinError(3)
	# print ' (3) Err VV:',h_rec_DiBoson.GetBinContent(3),h_rec_TTBar.GetBinError(3)
	# print ' (3) Err t: ',h_rec_SingleTop.GetBinContent(3),h_rec_SingleTop.GetBinError(3)
	# print ' (3) Err D: ',h_rec_Data.GetBinContent(3),h_rec_Data.GetBinError(3)
	# print ' (3) Err Q: ',h_rec_QCDMu.GetBinContent(3),h_rec_QCDMu.GetBinError(3)
	# print ' (3) Err Perc Q: ', h_rec_QCDMu.GetBinContent(3)/( 0.00001+h_rec_WJets1.GetBinContent(3) + h_rec_ZJets.GetBinContent(3) + h_rec_TTBar.GetBinContent(3) + h_rec_DiBoson.GetBinContent(3) + h_rec_SingleTop.GetBinContent(3) + h_rec_QCDMu.GetBinContent(3)), h_rec_QCDMu.GetBinError(3)/( 0.00001+h_rec_WJets1.GetBinError(3) + h_rec_ZJets.GetBinError(3) + h_rec_TTBar.GetBinError(3) + h_rec_DiBoson.GetBinError(3) + h_rec_SingleTop.GetBinError(3) + h_rec_QCDMu.GetBinError(3))




	# sys.exit()

	###############################################################################################
	###############                         END OF QCD                        #####################
	###############################################################################################


	# W + Jets Contributions (Normalized for display)
	# h_gen_WJets=CreateHisto('h_gen_WJets_aod','W+Jets '+gtag+' [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955',MCGenStyle,Label)
	h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets MG [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955'+fW,MCGenStyle,Label)

	print '-'*50+'\n'+rivetmodvariable+'\n'+rivetselection+'\n'+'-'*50+'\n'	
	# h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# print '-'*50+'\n'+recomodvariable+'\n'+selection+weight+'\n'+'-'*50+'\n'	
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight+fW,MCRecoStyle,Label)
	h_rec_WJetsMG=CreateHisto('h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,selection+weight+fWMG,MCRecoStyle,Label)


	h_rec_WJets_noscale=CreateHisto('h_rec_WJets_noscale','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight,MCRecoStyle,Label)


	if 'Pt_muon2>25' in selection:
		QCDSF = 0.0
		print 'Z SELECTION -- SETTING QCD SCALE TO ZERO'



	# Pseudo-Data for Unfolding (ALWAYS FROM MADGRAPH)
	h_rec_Data_pseudo=PseudoDataHisto(h_rec_WJetsMG,'h_rec_PseudoData',varbinning)
	h_rec_Data_pseudoSG=PseudoDataHisto(h_rec_WJets,'h_rec_PseudoDataSG',varbinning)


	## Draw W+Jets Gen and Reco
	h_gen_WJets.Draw("HIST")	
	h_rec_WJets.Draw("HISTSAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend( 0.5,  0.6,  0.9,  0.88,'' ))


	##############################################################################
	#######      Independent Plot - Normal Stacked Distributions           #######
	##############################################################################

	# Canvas Setup
	c2 = TCanvas("c2","",1000,1000)
	cpad1 = TPad( 'cpad1', 'cpad1', 0.0, 0.31, 1.0, 1.0 )#divide canvas into pads
	cpad2 = TPad( 'cpad2', 'cpad2', 0.0, 0.02, 1.0, 0.31 )
	cpad1.SetBottomMargin(0.0)
	cpad1.SetTopMargin(0.1)
	cpad1.SetLeftMargin(0.12)
	cpad1.SetRightMargin(0.1)
	cpad2.SetBottomMargin(0.3)
	cpad2.SetTopMargin(0.0)
	cpad2.SetLeftMargin(0.12)
	cpad2.SetRightMargin(0.1)
	cpad1.Draw()
	cpad2.Draw()
	cpad1.SetLogy(1)
	cpad1.cd()


	# pbin = array('d',presentationbinning)
	# npbin = len(presentationbinning) -1


	hs_rec_WJets=RebinnedHisto("hs_rec_WJets",'W+Jets '+gtag+' [Reco]',h_rec_WJets,presentationbinning,WStackStyle,Label)
	hs_rec_WJets_noscale=RebinnedHisto("hs_rec_WJets_noscale",'W+Jets '+gtag+' [Reco]',h_rec_WJets_noscale,presentationbinning,WStackStyle,Label)	
	hs_rec_Data=RebinnedHisto("hs_rec_Data",'Data, 5/fb [Reco]',h_rec_Data,presentationbinning,DataRecoStyle,Label)
	hs_rec_DiBoson=RebinnedHisto("hs_rec_DiBoson",'DiBoson [Pythia]',h_rec_DiBoson,presentationbinning,DiBosonStackStyle,Label)
	hs_rec_ZJets=RebinnedHisto("hs_rec_ZJets",'Z+Jets [MadGraph]',h_rec_ZJets,presentationbinning,ZStackStyle,Label)
	hs_rec_TTBar=RebinnedHisto("hs_rec_TTBar",'t#bar{t} [MadGraph]',h_rec_TTBar,presentationbinning,TTStackStyle,Label)
	hs_rec_SingleTop=RebinnedHisto("hs_rec_SingleTop",'SingleTop [Powheg]',h_rec_SingleTop,presentationbinning,StopStackStyle,Label)
	hs_rec_QCDMu=RebinnedHisto("hs_rec_QCDMu",'QCD',h_rec_QCDMu,presentationbinning,QCDStackStyle,Label)

	print '------- REBINNED HISTOS --------'
	print ' W: ',hs_rec_WJets.Integral()
	print ' Z: ',hs_rec_ZJets.Integral()
	print ' TT:',hs_rec_TTBar.Integral()
	print ' VV:',hs_rec_DiBoson.Integral()
	print ' t: ',hs_rec_SingleTop.Integral()
	print ' D: ',hs_rec_Data.Integral()

	qcdmin = 9999
	stopmin = 9999
	datmax = 0.1
	for xx in range((hs_rec_Data.GetNbinsX())):
		_nd = hs_rec_Data.GetBinContent(xx+1)
		_nq = hs_rec_QCDMu.GetBinContent(xx+1)
		_ns = hs_rec_SingleTop.GetBinContent(xx+1)
		if _nq < qcdmin:
			qcdmin = _nq
		if _ns < stopmin:
			stopmin = _ns
		if _nd > datmax:
			datmax = _nd

	plotmin = qcdmin
	if qcdmin < 0.001:
		plotmin =stopmin
	plotmin = 0.5*plotmin
	if plotmin < 0.1:
		plotmin = 0.1
	# plotmax = 100*hs_rec_Data.GetMaximum()
	plotmax = datmax*100.0

	# Declare the MC Stack
	MCStack = THStack ("MCStack","")
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)
	print 'Declared stack from ',plotmin, 'to ',plotmax




	print " -------- SIGNAL REGION TABLE INFO -----------"
	_w_b = 'Bin '
	_w_d = 'Data '
	_w_z = 'Z '
	_w_tt = '$t \overline{t}$ '
	_w_w = 'W '
	_w_q = 'QCD '
	_w_o = 'Other '

	for _nn in range(hs_rec_Data.GetNbinsX()):
		_nn += 1
		_center = hs_rec_Data.GetBinCenter(_nn)
		if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):

			_w_b+= ' & '+str(round(hs_rec_Data.GetBinCenter(_nn) ,3))
			_w_d+= ' & '+str(int(round(hs_rec_Data.GetBinContent(_nn) ,0)))
			_w_w+= ' & '+str(int(round(hs_rec_WJets_noscale.GetBinContent(_nn) ,0)))
			_w_z+= ' & '+str(int(round(hs_rec_ZJets.GetBinContent(_nn) ,0)))
			_w_tt+= ' & '+str(int(round(hs_rec_TTBar.GetBinContent(_nn) ,0)))
			_w_o+= ' & '+str(int(round(hs_rec_SingleTop.GetBinContent(_nn) +hs_rec_DiBoson.GetBinContent(_nn) ,0)))
			_w_q+= ' & '+str(int(round(hs_rec_QCDMu.GetBinContent(_nn) ,0)))


	print _w_b
	print _w_d
	print _w_w
	print _w_z
	print _w_tt
	print _w_o
	print _w_q

	print " -------- SIGNAL REGION TABLE COMPLETE -----------"

	# For tables only
	# sys.exit()



	# List of MC Histos
	SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	SM_noscale=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets_noscale]

	hlog = 'pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.hlog'
	_hlog = open(hlog,'w')
	print '\nBin','W','TTbar'

	for _nn in range(hs_rec_WJets_noscale.GetNbinsX()+1):
		nn = _nn+1
		logline = ''
		totsm = 0.0
		totsmerr = 0.0

		bincent = hs_rec_WJets_noscale.GetBinCenter(nn)
		binlhs = bincent - 0.5*hs_rec_WJets_noscale.GetBinWidth(nn)
		binrhs = bincent + 0.5*hs_rec_WJets_noscale.GetBinWidth(nn)
		logline += str(binlhs)+','+str(binrhs)+';'

		fac = 1.0
		
		if 'lumi_plus' in tagname:
			fac = fac * 1.022
		if 'lumi_minus' in tagname:
			fac = fac * 1.022

		for ss in SM_noscale:
			totsm += fac*(ss.GetBinContent(nn))
			totsmerr += (fac*(ss.GetBinError(nn)))**2
			logline += str(fac*(ss.GetBinContent(nn)))+ ','+str(fac*(ss.GetBinError(nn)))+';'
		totsmerr = math.sqrt(totsmerr)


		# print hs_rec_WJets.GetBinCenter(nn),hs_rec_WJets.GetBinContent(nn), hs_rec_TTBar.GetBinContent(nn), totsm
		logline +=str(totsm)+','+str(totsmerr)+';' 
		logline +=str(hs_rec_Data.GetBinContent(nn))+'\n'
		_hlog.write(logline)
	_hlog.close()


	# sys.exit()
	# Set attributes
	for x in SM + [hs_rec_Data]:
		x.GetYaxis().SetTitleOffset(0.9)
		x.SetMaximum(plotmax)

	# Build stack
	for x in SM:
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw()
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)
	MCStack.GetYaxis().SetTitleOffset(0.9)
	MCStack.Draw("HIST")
	cpad1.SetLogy()
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)
	cpad1.Update()
	MCStack=BeautifyStack(MCStack,Label)

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")
	
	leg = TLegend(0.60,0.61,0.86,0.86,"","brNDC");
	leg.SetTextFont(42);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.03)
	leg.AddEntry(hs_rec_Data)
	ind = -1
	for s in SM:
		leg.AddEntry(SM[ind])
		ind += -1

	leg.Draw()

	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	l1.DrawLatex(0.22,0.94,"CMS 2011  "+sqrts+" ")

	gPad.RedrawAxis()


	############################
	### GO TO SUBPLOT        ###
	############################
	cpad2.cd()
	cpad2.Draw()

	hs_rec_total=CreateHisto('hs_rec_total','total',t_WJets_MG,recovariable,presentationbinning,selection+weight+fW,WStackStyle,Label)
	hs_rec_total.Sumw2()
	for s in [hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]:
		hs_rec_total.Add(s)

	hs_rec_ratio=CreateHisto('hs_rec_ratio','Data Ratio',t_SingleMuData,recovariable,presentationbinning,selection+IsoMuCond,DataRecoStyle,Label)
	hs_rec_ratio.Sumw2()

	hs_rec_ratio.Divide(hs_rec_total)


	hs_rec_pur_num=CreateHisto('hs_rec_pur_num','W Purity',t_SingleMuData,recovariable,presentationbinning,"(0)",WStackStyle,Label)
	hs_rec_pur_den=CreateHisto('hs_rec_pur_den','W Purity Den',t_SingleMuData,recovariable,presentationbinning,"(0)",WStackStyle,Label)
	hs_rec_pur_num.Sumw2()
	hs_rec_pur_den.Sumw2()



	hs_rec_pur_num.Add(hs_rec_WJets)
	hs_rec_pur_den.Add(hs_rec_WJets)
	for s in [hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]:
		hs_rec_pur_den.Add(s)

	hs_rec_pur_num.Divide(hs_rec_pur_den)



	unity=TLine(hs_rec_WJets.GetXaxis().GetXmin(), 1.0 , hs_rec_WJets.GetXaxis().GetXmax(),1.0)

	ratmin = 0
	ratmax = 2

	posvals = []
	for b in range(hs_rec_ratio.GetNbinsX()+1):
		if b == 0:
			continue
		val = hs_rec_ratio.GetBinContent(b)
		dev = hs_rec_ratio.GetBinError(b)
		posvals.append(val + dev)
		posvals.append(val-dev)

	if 0.9*min(posvals) >ratmin:
		ratmin = min(posvals) *0.9	
	if 1.1*max(posvals) <ratmax:
		ratmax = 1.1*max(posvals)

	ratmin = round(ratmin,2)
	ratmax = round(ratmax,2)
	hs_rec_ratio.SetMaximum(2.0)
	hs_rec_ratio.SetMinimum(0.0)


	alabel = Label[0]

	for ni in [1,2,3,4]:
		nis = str(ni)
		if 'inc'+nis in namelabel:
			alabel += ' (#geq '+nis+' jets)'

	hs_rec_ratio.GetXaxis().SetTitle(alabel)
	hs_rec_ratio.GetYaxis().SetTitle("Data / MC")
	hs_rec_ratio.GetXaxis().SetTitleOffset(.73);

	hs_rec_ratio.GetYaxis().SetTitleFont(42);
	hs_rec_ratio.GetXaxis().SetTitleSize(.12);
	hs_rec_ratio.GetYaxis().SetTitleSize(.12);
	hs_rec_ratio.GetXaxis().CenterTitle(0);
	hs_rec_ratio.GetYaxis().CenterTitle(1);
	hs_rec_ratio.GetXaxis().SetTitleOffset(0.88);
	hs_rec_ratio.GetYaxis().SetTitleOffset(0.45);
	hs_rec_ratio.GetYaxis().SetLabelSize(.1);
	hs_rec_ratio.GetXaxis().SetLabelSize(.1);

	hs_rec_pur_num.GetXaxis().SetTitle(Label[0])
	hs_rec_pur_num.GetXaxis().SetTitleOffset(.73);

	hs_rec_pur_num.GetYaxis().SetTitleFont(42);
	hs_rec_pur_num.GetXaxis().SetTitleSize(.12);
	hs_rec_pur_num.GetYaxis().SetTitleSize(.12);
	hs_rec_pur_num.GetXaxis().CenterTitle(0);
	hs_rec_pur_num.GetYaxis().CenterTitle(1);
	hs_rec_pur_num.GetXaxis().SetTitleOffset(0.88);
	hs_rec_pur_num.GetYaxis().SetTitleOffset(0.45);
	hs_rec_pur_num.GetYaxis().SetLabelSize(.1);
	hs_rec_pur_num.GetXaxis().SetLabelSize(.1);


	hs_rec_pur_num.SetFillStyle(0)
	hs_rec_pur_num.SetLineStyle(1)
	hs_rec_ratio.Draw("EP")
	# hs_rec_pur_num.GetYaxis().SetTitle("W Purity")

	# hs_rec_pur_num.Draw("EHIST")

	
	unity.Draw("SAME")



	c2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.png')
	c2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.pdf')











	if ('--quickplots' in sys.argv):
		return [0,0,0]

	# sys.exit()


	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)

	mcdatascalepres = (1.0*(hs_rec_Data.Integral(pbinmin,pbinmax)))/(sum([k.Integral(pbinmin,pbinmax) for k in SM]))

	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend(0.7,  0.6,  0.92,  0.88,''))
	gPad.RedrawAxis()


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)




	matchingselection = '1'
	if 'matchsel' in tagname:
		for nametype in ['DeltaPhi_pfjetXmuon1','Pt_pfjetX_pt20','Eta_pfjetX_eta2p5']:
			for jetmult in ['1','2','3','4','5']:
				if nametype.replace('X',jetmult) in recomodvariable:
					matchingselection = recomodvariable+'_hasgenmatch>0.5'	

	print 'Matching Check: recomodvariable',recomodvariable,'matchingselection:',matchingselection


	# This is the normal situation, unfolding with MadGraph response
	if 'altunf' not in tagname:

		t_WJets_MG_G = t_WJets_MG.CopyTree(gen_selection)
		t_WJets_MG_R = t_WJets_MG.CopyTree(selection)
		t_WJets_MG_RG = t_WJets_MG.CopyTree('('+gen_selection+')*('+selection+')*('+matchingselection+')')



		# W + Jets Contributions (Rivet and GEN)
		h_gen_WJets_flatRIVET=CreateHisto('h_gen_WJets_flatRIVET','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
		h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets MadGraph [Truth]',t_WJets_MG_G,baregenvariable,varbinning,'(weight_pu_central*4955)'+fW,MCGenStyle,Label)

		# Reco histograms (MadGraph and Other) 
		h_rec_WJets_flat=CreateHisto('h_rec_WJets_flat','W+Jets '+gtag+' [Reco]',t_WJets_MG_R,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW, MCRecoStyle,Label)	
		# h_rec_WJets_flatMG=CreateHisto('h_rec_WJets_flatMG','W+Jets '+gtag+' MG [Reco]',t_MG_R,recomodvariable,varbinning,'(weight_pu_central*4955)'+fWMG, MCRecoStyle,Label)

		# Response Matrix 
		h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG_RG,baregenvariable,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW,[xlabel+" Reco",xlabel+" Truth"])



	# Here we are unfolding with a Sherpa response, adjusting the sherpa for the btag veto efficiency in W+Jets MC
	else:

		# New Selection without B Veto
		selection_nobtag = str(selection)
		selection_nobtag = selection_nobtag.replace('PFJet30TCHEMCountCentral','0.0')
		selection_nobtag = selection_nobtag.replace('PFJet30TCHEMCountEffDown','0.0')
		selection_nobtag = selection_nobtag.replace('PFJet30TCHEMCountEffUp','0.0')
		selection_nobtag = selection_nobtag.replace('PFJet30TCHEMCountMisDown','0.0')
		selection_nobtag = selection_nobtag.replace('PFJet30TCHEMCountMisUp','0.0')

		# Sherpa trees without b veto
		t_WJets_MG_G = t_WJets_MG.CopyTree(gen_selection)
		t_WJets_MG_R = t_WJets_MG.CopyTree(selection_nobtag)
		t_WJets_MG_RG = t_WJets_MG.CopyTree('('+gen_selection+')*('+selection_nobtag+')*('+matchingselection+')')

		# MadGraph Trees with and without btag veto
		t_MG_R               = t_MG.CopyTree(selection)
		t_MG_R_nobtag        = t_MG.CopyTree(selection_nobtag)

		t_MG_RG              = t_MG.CopyTree('('+gen_selection+')*('+selection+')*('+matchingselection+')')
		t_MG_RG_nobtag       = t_MG.CopyTree('('+gen_selection+')*('+selection_nobtag+')*('+matchingselection+')')



		# W + Jets Contributions (Rivet and GEN)
		h_gen_WJets_flatRIVET=CreateHisto('h_gen_WJets_flatRIVET','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
		h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets MadGraph [Truth]',t_WJets_MG_G,baregenvariable,varbinning,'(weight_pu_central*4955)'+fW,MCGenStyle,Label)

		# Reco histograms (MadGraph and Other) 
		h_rec_WJets_flat=CreateHisto('h_rec_WJets_flat','W+Jets '+gtag+' [Reco]',t_WJets_MG_R,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW, MCRecoStyle,Label)	

		# Response Matrix 
		h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG_RG,baregenvariable,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW,[xlabel+" Reco",xlabel+" Truth"])



		# 1 Dimensional Scale Factors

		presentationbinning_exp = presentationbinning
		if varbinning[0] not in presentationbinning_exp:
			presentationbinning_exp = [varbinning[0]]+presentationbinning_exp
		if varbinning[-1] not in presentationbinning_exp:
			presentationbinning_exp = presentationbinning_exp + [varbinning[-1]]

		print 'Using rescaling binning', presentationbinning_exp

		h_rec_WJets_flatMG_wbtag=CreateHisto('h_rec_WJets_flatMG_wbtag','W+Jets '+gtag+' MG [Reco]',t_MG_R,recomodvariable,presentationbinning_exp,'(weight_pu_central*4955)'+fWMG, MCRecoStyle,Label)
		h_rec_WJets_flatMG_nobtag=CreateHisto('h_rec_WJets_flatMG_nobtag','W+Jets '+gtag+' MG [Reco]',t_MG_R_nobtag,recomodvariable,presentationbinning_exp,'(weight_pu_central*4955)'+fWMG, MCRecoStyle,Label)

		[BtagRescalingString,BtagErrorString] = GetRescaling(h_rec_WJets_flatMG_wbtag,h_rec_WJets_flatMG_nobtag,presentationbinning_exp,recomodvariable)

		# h_bscale = h_rec_WJets_flatMG_wbtag.Clone()
		# h_bscale.Divide(h_rec_WJets_flatMG_nobtag)

		# 2 Dimensional Scale Factors
		# h_response_WJetsMG_wbtag=Create2DHisto('h_response_WJetsMG_nobtag','ResponseMatrix',t_MG_RG,baregenvariable,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW,[xlabel+" Reco",xlabel+" Truth"])
		# h_response_WJetsMG_nobtag=Create2DHisto('h_response_WJetsMG_nobtag','ResponseMatrix',t_MG_RG_nobtag,baregenvariable,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW,[xlabel+" Reco",xlabel+" Truth"])

		# h2_bscale = h_response_WJetsMG_wbtag.Clone()
		# h2_bscale.Divide(h_response_WJetsMG_nobtag)

		# print '------------------ Original Sherpa -------------------'
		# h_rec_WJets_flat.Print("range")


		# h_rec_WJets_flat.Multiply(h_bscale)
		# h_response_WJets.Multiply(h2_bscale)


		print 'Creating rescaled sherpa btag veto hists with:  ',BtagRescalingString
		# Reco histograms (MadGraph and Other) 
		h_rec_WJets_flat=CreateHisto('h_rec_WJets_flat','W+Jets '+gtag+' [Reco]',t_WJets_MG_R,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW+'*'+BtagRescalingString, MCRecoStyle,Label)	

		# Response Matrix 
		h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG_RG,baregenvariable,recomodvariable,varbinning,'(weight_pu_central*4955)'+fW+'*'+BtagRescalingString,[xlabel+" Reco",xlabel+" Truth"])


		# print '------------------ RESCALED Sherpa -------------------'
		# h_rec_WJets_flat.Print("range")


		# print '------------------ MG BTAG ON -------------------'
		# h_rec_WJets_flatMG_wbtag.Print("range")

		# print '------------------ MG BTAG OFF -------------------'
		# h_rec_WJets_flatMG_nobtag.Print("range")

		# print '------------------ GEN SHERPA -------------------'
		# h_gen_WJets_flat.Print("range")


	h_response_WJets.Draw("COLZ") # Draw it with color scheme
	l_bottom=TLine(binning[1], presentationbinning[0] ,binning[2],presentationbinning[0])
	l_top=TLine(binning[1], presentationbinning[-1] ,binning[2],presentationbinning[-1])
	l_left=TLine(presentationbinning[0], binning[1] ,presentationbinning[0],binning[2])
	l_right=TLine(presentationbinning[-1], binning[1] ,presentationbinning[-1],binning[2])
	bounds = [l_bottom,l_top,l_right,l_left]
	
	for x in bounds:
		x.SetLineStyle(2)
		x.Draw("SAME")
	# sys.exit()

	print 'baregenvariable', baregenvariable
	print 'recomodvariable', recomodvariable
	print 'genmodvariable', genmodvariable
	# print 'gen_selection_minimal',gen_selection_minimal
	print 'Xini:',h_gen_WJets_flat.Integral()
	print 'Bini:',h_rec_WJets_flat.Integral()
	print 'Adet:',h_response_WJets.Integral()
	print 'Pseu:',h_rec_Data_pseudo.Integral()


	##############################################################################
	#######      Top Right Addition  - UnFolded Distribution               #######
	##############################################################################	
	c1.cd(2)
	# Subtract other backgrounds from Data using the BackgroundSubtractedHistogram function.
	h_rec_Data2= h_rec_Data.Clone()
	print ' ----------- DATA MINUS BACKGROUND SUBRACTION UNCERTAINTY SUMMARY '
	print ' DATA BINS : ',[h_rec_Data2.GetBinCenter(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]	
	print ' DATA CONT : ',[h_rec_Data2.GetBinContent(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]
	print ' DATA ERRS : ',[h_rec_Data2.GetBinError(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]
	print ' DiBo ERRS : ',[h_rec_DiBoson.GetBinError(nn+1) for nn in range(h_rec_DiBoson.GetNbinsX())]
	print ' ZJet ERRS : ',[h_rec_ZJets.GetBinError(nn+1) for nn in range(h_rec_DiBoson.GetNbinsX())]
	print ' TTbr ERRS : ',[h_rec_TTBar.GetBinError(nn+1) for nn in range(h_rec_DiBoson.GetNbinsX())]
	print ' Sing ERRS : ',[h_rec_SingleTop.GetBinError(nn+1) for nn in range(h_rec_DiBoson.GetNbinsX())]
	print ' QCDm ERRS : ',[h_rec_QCDMu.GetBinError(nn+1) for nn in range(h_rec_DiBoson.GetNbinsX())]

	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu])

	print ' DSUB CONT : ',[h_rec_Data2.GetBinContent(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]
	print ' DSUB HASNEG : ',[h_rec_Data2.GetBinContent(nn+1)<0.0 for nn in range(h_rec_Data2.GetNbinsX())]

	print ' DSUB ERRS : ',[h_rec_Data2.GetBinError(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]
	print ' ----------- DATA MINUS BACKGROUND SUBRACTION UNCERTAINTY SUMMARY '

	os.system('sleep 5')
	h_rec_Data2 = BeautifyHisto(h_rec_Data2,DataCompStyle,Label,"Data, 5/fb [Reco]")

	print 'Data Int:', h_rec_Data2.Integral()

	# These are the paramters for the unfolding [reco, gen, response]
	Params = [ h_rec_WJets_flat, h_gen_WJets_flat, h_response_WJets]

	# Tau is calculated only for the real unfolding. Systematics use that tau. This allows an overridee of the tau value as an argument.
	if tau_override>0:
		tau=tau_override
	else:
		#tau=2  # For quick tests only!
		tau = FindOptimalTauWithDIVals(Params,h_rec_Data2,varbinning) # Get the optimal tau value.

	# Perform the unfolding. Returns unfolded data histo, some unfolding parameters not currently used
	software_implementation = 'RooUnfoldSvd'


	if 'roounfsvd' in tagname:
		software_implementation = 'RooUnfoldSvd'
	if 'roounfbayes' in tagname or 'BAYES' in 'pyplots':
		software_implementation = 'RooUnfoldBayes'
	if 'roounfbin' in tagname:
		software_implementation = 'RooUnfoldBin'
	if 'autobin' in tagname:
		software_implementation = 'AutoBin'
	if 'tsvd' in tagname or 'Tsvd' in 'pyplots':
		software_implementation = 'TSVD'
	if 'SvdUnc' in 'pyplots':
		software_implementation = 'RooUnfoldSvdUncTest'

	# Quick fix for DI stuff
	# software_implementation = 'TSVD'

	if False:
		for ibin in range(h_rec_Data2.GetNbinsX() +2):
			if h_rec_Data2.GetBinContent(ibin) < 0.0:
				h_rec_Data2.SetBinContent(ibin,0.0)

		print 'Manual forcing of non-zero bins! -------------------------'
		print ' DSUB CONT : ',[h_rec_Data2.GetBinContent(nn+1) for nn in range(h_rec_Data2.GetNbinsX())]
		print ' DSUB HASNEG : ',[h_rec_Data2.GetBinContent(nn+1)<0.0 for nn in range(h_rec_Data2.GetNbinsX())]
		print 'Manual forcing of non-zero bins! -------------------------'


	sys_imp = 0
	if 'standard' in tagname:
		sys_imp = 3
	ismcunf = False
	if 'mcunf' in tagname:
		ismcunf = True



	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau,software_implementation,sys_imp,ismcunf)

	[h_unf_Data_b,h_dd_b,h_sv_b,optimal_tau_b,optimal_i_b] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau,'RooUnfoldBayes',sys_imp,ismcunf)

	# Samme as above, but using pseudo-data from the WJets MC - this is the closure test! Always using MadGraph!
	[h_unf_Data_pseudo,h_dd,h_sv_pseudo,optimal_tau_pseudo,optimal_i_pseudo] = GetSmartSVD(h_rec_Data_pseudo,Params, varbinning,tau,software_implementation,sys_imp,ismcunf)
	# Samme as above, but using same generator used for unfolding!
	[h_unf_Data_pseudoSG,h_dd,h_sv_pseudo,optimal_tau_pseudoSG,optimal_i_pseudoSG] = GetSmartSVD(h_rec_Data_pseudoSG,Params, varbinning,tau,software_implementation,sys_imp,ismcunf)


	print 'Unfolded Data', h_unf_Data.Integral()
	print 'Unfolded PseudoData', h_unf_Data_pseudo.Integral()

	# How much would you have to scale the unfolded data to meet the reco data? Should be ~1.
	UnfScale=(h_rec_Data2.Integral(vbinmin,vbinmax)/h_unf_Data.Integral(vbinmin,vbinmax))
	UnfScale_pseudo=(h_rec_Data_pseudo.Integral(vbinmin,vbinmax)/h_unf_Data_pseudo.Integral(vbinmin,vbinmax))
	UnfScale_pseudoSG=(h_rec_Data_pseudoSG.Integral(vbinmin,vbinmax)/h_unf_Data_pseudoSG.Integral(vbinmin,vbinmax))

	# Creates plots, with extra label giving the optimal tau and unfolding scale above.
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_b = BeautifyHisto(h_unf_Data_b,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_pseudo = BeautifyHisto(h_unf_Data_pseudo,DataUnfoldedStyle_pseudo,Label,"WJets MadGraph Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale_pseudo,2))+"]")
	h_unf_Data_pseudoSG = BeautifyHisto(h_unf_Data_pseudoSG,DataUnfoldedStyle_pseudoSG,Label,"WJets "+gtag+" Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale_pseudoSG,2))+"]")

	# Using the unfolded data and reeco data, get a rescaling string to convert between the two types of binning.
	[DataRescalingString,DataErrorString] = GetRescaling(h_unf_Data,h_rec_Data2,varbinning,recovariable)
	# Same as above, but for the closure test.
	[DataRescalingString_pseudo,DataErrorString_pseudo] = GetRescaling(h_unf_Data_pseudo,h_rec_Data_pseudo,varbinning,recovariable)
	[DataRescalingString_pseudoSG,DataErrorString_pseudoSG] = GetRescaling(h_unf_Data_pseudoSG,h_rec_Data_pseudoSG,varbinning,recovariable)

	print ' -------------------- BAYESIAN ----------------------', tagname
	h_unf_Data_b.Print("range")

	print "DataRescaling:", DataRescalingString
	print "PseudoData Rscaling:" , DataRescalingString_pseudo

	print "Error DataRescaling:", DataErrorString
	print "Error PseudoData Rscaling:" , DataErrorString_pseudo

	# Draw the unfolded data, reco data, and pseudo (closure) data
	h_unf_Data.Draw("EPSAME")
	h_rec_Data2.Draw("EPSAME")
	h_unf_Data_pseudo.Draw("EPSAME")

	# Legend
	FixDrawLegend(c1.cd(2).BuildLegend(0.5,  0.6,  0.9,  0.88,''))

	# This is just a fancy way of getting decent plot axis dimensions
	CompMin = 99999999999999
	CompMax= 0
	for x in range(h_gen_WJets.GetNbinsX()):
		v = h_gen_WJets.GetBinContent(x+1)
		if x>=(h_gen_WJets.GetNbinsX() -1):
			continue
		if v<0.1:
			continue
		if v>999999999:
			continue
		if v<CompMin:
			CompMin=v
		if v>CompMax:
			CompMax=v

	CompMin = 0.8*CompMin
	CompMax = 1.3*CompMax
	if "Eta" in recovariable or 'Count' in recovariable:
		CompMax = 10*CompMax	
	if "DeltaPhi" in recovariable:
		CompMax = 10*CompMax
	
	leftborder =  TLine( presentationbinning[0],CompMin,presentationbinning[0],CompMax )
	rightborder =  TLine( presentationbinning[-1],CompMin,presentationbinning[-1],CompMax )
	leftborder.SetLineStyle(2)
	rightborder.SetLineStyle(2)
	h_gen_WJets.SetMaximum(CompMax)
	h_gen_WJets.SetMinimum(CompMin)
	leftborder.Draw("SAME")
	rightborder.Draw("SAME")	
	if (optvar=="v" or optvar=="V" or optvar=="c"):
		c1.cd(2).SetLogy()
	
	c1.cd(3).Update()


	##############################################################################
	#######      Bottom Right - More legible ratio plots                   #######
	##############################################################################	
	c1.cd(4)
	#c1.cd(4).SetLogy()

	genpres_selection = ''
	for ll in gen_selection:
		genpres_selection += ll


	unfgenpres_selection = genpres_selection


	h_pres_rec_WJets=RebinnedHisto("h_pres_rec_WJets",'W+Jets '+gtag+' [Reco]',h_rec_WJets,presentationbinning,MCRecoStyle,Label)
	h_pres_rec_WJetsMG = RebinnedHisto("h_pres_rec_WJetsMG",'W+Jets MADGRAPH [Reco]',h_rec_WJetsMG,presentationbinning,MCRecoStyle,Label)


	# WJets Gen + Reco
	h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets '+gtag+' [Truth/Reco]',t_WJets_MG,baregenvariable,presentationbinning,gen_selection+'*weight_pu_central*4955'+fW,MCRecoStyle,Label)
	h_pres_gen_WJetsMG=CreateHisto('h_pres_gen_WJetsMG','W+Jets MadGraph [Truth/Reco]',t_MG,baregenvariable,presentationbinning,gen_selection+'*weight_pu_central*4955'+fWMG,MCRecoStyle,Label)

	h_pres_unf_Data=RebinnedHisto("h_pres_unf_Data",'Data, 5/fb [Unfolded/Reco]',h_unf_Data,presentationbinning,DataUnfoldedStyle,Label)

	h_pres_unf_Data_b=RebinnedHisto("h_pres_unf_Data_b",'Data, 5/fb Unf[SVD/Bayes]',h_unf_Data_b,presentationbinning,DataUnfoldedStyle_b,Label)


	h_pres_rec_Data=RebinnedHisto("h_pres_rec_Data",'Data, 5/fb [Unfolded/Reco]',h_rec_Data2,presentationbinning,DataCompStyle,Label)

	h_pres_unf_Data_2=RebinnedHisto("h_pres_unf_Data_2",'Unf. Data/ '+gtag+' Truth',h_unf_Data,presentationbinning,DataUnfoldedStyle_2,Label)


	h_pres_unf_Data_pseudo=RebinnedHisto("h_pres_unf_Data_pseudo",'MadGraph [Unf. Reco/ Gen]',h_unf_Data_pseudo,presentationbinning,DataUnfoldedStyle_pseudo2,Label)
	h_pres_unf_Data_pseudoSG=RebinnedHisto("h_pres_unf_Data_pseudoSG",gtag+'[Unf. Reco/ Gen]',h_unf_Data_pseudoSG,presentationbinning,DataUnfoldedStyle_pseudo2SG,Label)



	print ' -------------------- BAYESIAN Rebinned ----------------------', tagname
	h_unf_Data_b.Print("range")

	DataBinInfo=[]
	MCBinInfo=[]

	# Loop to get the data and MC bin info as lists - need for tables and so forth.

	lumifactor = 1.0
	if 'lumi_plus' in tagname:
		lumifactor = lumifactor * 1.022
	if 'lumi_minus' in tagname:
		lumifactor = lumifactor / 1.022

	dodiff = True

	for x in range(h_pres_rec_Data.GetNbinsX()+1):
		if x==0:
			continue
		# if h_pres_unf_Data.GetBinContent(x) != 0:
		# 	h_pres_unf_Data.SetBinError(x,h_pres_unf_Data_err.GetBinContent(x)/h_pres_unf_Data.GetBinContent(x))
		# else: 
		# 	h_pres_unf_Data.SetBinError(x,0)
		width = h_pres_unf_Data.GetBinWidth(x)
		lhs=h_pres_unf_Data.GetBinCenter(x)-0.5*(h_pres_unf_Data.GetBinWidth(x))
		rhs=h_pres_unf_Data.GetBinCenter(x)+0.5*(h_pres_unf_Data.GetBinWidth(x))
		content=lumifactor*h_pres_unf_Data.GetBinContent(x)
		error=lumifactor*h_pres_unf_Data.GetBinError(x)
		if dodiff: [content,error] = [content/width,error/width]
		lhs=str(lhs)
		rhs=str(rhs)
		content=str(round(content,2))
		error=str(round(error,2))
		DataBinInfo.append([lhs+' - '+str(rhs),content+' +- '+error])

		width = h_pres_gen_WJets.GetBinWidth(x)
		lhs=h_pres_gen_WJets.GetBinCenter(x)-0.5*(h_pres_gen_WJets.GetBinWidth(x))
		rhs=h_pres_gen_WJets.GetBinCenter(x)+0.5*(h_pres_gen_WJets.GetBinWidth(x))
		content=lumifactor*h_pres_gen_WJets.GetBinContent(x)
		error=lumifactor*h_pres_gen_WJets.GetBinError(x)
		lhs=str(lhs)
		rhs=str(rhs)
		if dodiff: [content,error] = [content/width,error/width]
		content=str(round(content,2))
		error=str(round(error,2))
		MCBinInfo.append([lhs+' - '+rhs,content+' +- '+error])
		

	# For closure test, divide by MC to convert to a ratio plot
	h_pres_unf_Data_2.Divide(h_pres_gen_WJets)
	h_pres_unf_Data_pseudo.Divide(h_pres_gen_WJetsMG)
	h_pres_unf_Data_pseudoSG.Divide(h_pres_gen_WJets)


	print ' -------------------- BAYESIAN Denominator data ----------------------', tagname
	h_pres_unf_Data_b.Print("range")


	h_pres_unf_Data_b.Divide(h_pres_unf_Data)


	print ' -------------------- BAYESIAN Ratio ----------------------', tagname
	h_pres_unf_Data_b.Print("range")


	## Divide gen by reco for MC, and unfolded by reco for data.
	h_pres_gen_WJets.Divide(h_pres_rec_WJets)
	h_pres_unf_Data.Divide(h_pres_rec_Data)


	# Dashed line at unity for closure test
	l_one=TLine(presentationbinning[0], 1 ,presentationbinning[-1],1)
	l_one.SetLineStyle(2)
	

	RelMin = 0.0
	RelMax = 5.0
	h_pres_gen_WJets.GetYaxis().SetTitle("Ratio")
	h_pres_gen_WJets.SetMarkerSize(0.000001)
	h_pres_gen_WJets.SetLineStyle(1)
	h_pres_gen_WJets.SetLineWidth(1)

	h_pres_gen_WJets.Draw("HIST")
	h_pres_gen_WJets.SetMaximum(RelMax)
	h_pres_gen_WJets.SetMinimum(RelMin)

	# Do the drawing
	h_pres_unf_Data.GetYaxis().SetTitle("Ratio")
	h_pres_unf_Data_2.GetYaxis().SetTitle("Ratio")
	h_pres_unf_Data_pseudo.GetYaxis().SetTitle("Ratio")
	h_pres_unf_Data_pseudoSG.GetYaxis().SetTitle("Ratio")

	h_pres_unf_Data_b.GetYaxis().SetTitle("Ratio")


	h_pres_unf_Data.Draw("EPHISTSAME")
	h_pres_unf_Data_pseudo.Draw("EPHISTSAME")
	if 'altunf' in tagname:
		h_pres_unf_Data_pseudoSG.Draw("EPHISTSAME")
	if 'powunf' in tagname:
		h_pres_unf_Data_pseudoSG.Draw("EPHISTSAME")

	h_pres_unf_Data_b.Draw("EPSAME")
	h_pres_unf_Data_2.Draw("EPHISTSAME")


	# Create Legend
	FixDrawLegend(c1.cd(4).BuildLegend(0.6,  0.6,  0.93,  0.93,''))
	l_one.Draw("SAME")



	# Finally, print the plots as pdf and png
	c1.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'.pdf')
	c1.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'.png')


	c3 = TCanvas("c3","",700,500)
	c3pad1 = TPad( 'c3pad1', 'c3pad1', 0.0, 0.0, 1.0, 1.0 )#divide canvas into pads
	c3pad1.Draw()
	c3pad1.SetLogy()
	c3pad1.cd()
	h_dd.GetXaxis().SetTitle('Bin of '+Label[0]+' dist.')
	h_dd.GetYaxis().SetTitle('d_{i}')
	h_dd.Draw("")
	l_oneB=TLine(0, 1 ,len(varbinning),1)



	l_tauB=TLine(1.0*float(tau), h_dd.GetMinimum() ,1.0*float(tau),h_dd.GetMaximum())
	l_tauB.SetLineStyle(2)
	l_tauB.SetLineWidth(2)

	l_oneB.Draw("SAME")

	l_tauB.Draw("SAME")


	l1B=TLatex()
	l1B.SetTextAlign(12)
	l1B.SetTextFont(42)
	l1B.SetNDC()
	l1B.SetTextSize(0.05)
	l1B.DrawLatex(0.22,0.85,recovariable+' '+namelabel)


	# clear tmp file
	os.system("rm "+tmpname)
	c3.Print('pyplots/DI_'+recovariable+'_'+tagname+namelabel+'.pdf')
	c3.Print('pyplots/DI_'+recovariable+'_'+tagname+namelabel+'.png')



	if 'preexc' in namelabel:
		DataBinInfo = MakeInclusiveBinInfo(DataBinInfo)
		MCBinInfo = MakeInclusiveBinInfo(MCBinInfo)


	# Clear the memory!
	gDirectory.GetList().Delete()

	#return the optimal dau, the bin-by-bin unfolded data and MC.
	return [tau,DataBinInfo,MCBinInfo]




# FullAnalysisWithUncertainty just runs MakeUnfoldedPlots several times for each systematic variation. The goal is to return final distributions.
def FullAnalysisWithUncertainty(genvariable,recovariable,default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,prefab_tau_vec):

	# prefab_tau = 123456
	# prefab_tau = -10

	if 'BinByBin' in 'pyplots':
		prefab_tau = 123456

	# This is the standard plot. here we get the optimal tau value. 

	prefab_tau = prefab_tau_vec[0]
	if len(prefab_tau_vec)==2:
		prefab_tau_sh = prefab_tau_vec[1]
	else:
		prefab_tau_sh = prefab_tau_vec[0]

	_tau = -1
	if prefab_tau > -1:
		_tau = prefab_tau
	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',_tau,'standard')
	# [tau,data_forcenoprop,mc_forcenoprop]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',_tau,'forcenoprop')

	taush = tau
	if prefab_tau > -1:
		tau = prefab_tau
		taush = prefab_tau_sh

	# if ('--quickplots') in sys.argv:
	# 	return 0

	# Replacing with ScaleUp/ScaleDown samples. 
	# [null,data_scale_plus,mc_scale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleUp',tau,'scaleup')
	# [null,data_scale_minus,mc_scale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleDown',tau,'scaledown')
	# [null,data_match_plus,mc_match_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchUp',tau,'matchup')
	# [null,data_match_minus,mc_match_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchDown',tau,'matchdown')
	
	if ('NoSys' not in 'pyplots'):

		[null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',taush,'altunf')
		[null,data_mcunf,mc_mcunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'mcunf')

		# Plleup variations
		[null,data_pileup_plus,mc_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('weight_pu_central','weight_pu_sysplus'),optvar,NormalDirectory,'',tau,'pileup_plus')
		[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('weight_pu_central','weight_pu_sysminus'),optvar,NormalDirectory,'',tau,'pileup_minus')

		[null,data_bgnorm_plus,mc_bgnorm_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'bgnorm_plus')
		[null,data_bgnorm_minus,mc_bgnorm_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'bgnorm_minus')


		# Integrated luminosity up/down
		# [null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','5064'),optvar,NormalDirectory,'',tau,'lumi_plus')
		# [null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','4848'),optvar,NormalDirectory,'',tau,'lumi_minus')

		[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'lumi_plus')
		[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'lumi_minus')


		# Jet energy scale up/down, and smeared
		[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
		[null,data_jetscale_minus,mc_jetscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleDownDirectory,'',tau,'jetscale_minus')
		[null,data_jetsmear,mc_jetsmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetSmearDirectory,'',tau,'jetsmear')

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleUpDirectory,'',tau,'muscale_plus')
		[null,data_muscale_minus,mc_muscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleDownDirectory,'',tau,'muscale_minus')
		[null,data_musmear,mc_musmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuSmearDirectory,'',tau,'musmear')	
		[null,data_phicorr,mc_phicorr]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,PhiCorrDirectory,'',tau,'phicorr')	


		# BTag Efficiency Up/Down
		if 'UnCorr' not in selection[0]:
			[null,data_btag_plus,mc_btag_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('TCHEMCountCentral','TCHEMCountEffUp'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_plus')
			[null,data_btag_minus,mc_btag_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('TCHEMCountCentral','TCHEMCountEffDown'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_minus')
			[null,data_btag_misplus,mc_btag_misplus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('TCHEMCountCentral','TCHEMCountMisUp'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_misplus')
			[null,data_btag_misminus,mc_btag_misminus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('TCHEMCountCentral','TCHEMCountMisDown'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_misminus')

		else:
			[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
			[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]
			[null,data_btag_misplus,mc_btag_misplus]=[tau,data_standard,mc_standard]
			[null,data_btag_misminus,mc_btag_misminus]=[tau,data_standard,mc_standard]

			
		# [null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]
		# [null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',-1,'altunf')

		[null,data_hltidiso,mc_hltidiso]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'hltidiso')
		
		[null,data_roounfbayes,mc_roounfbayes]=[tau,data_standard,mc_standard]
		[null,data_roounfbin,mc_roounfbin]=[tau,data_standard,mc_standard]

		[null,data_matchsel,mc_matchsel]=[tau,data_standard,mc_standard]
		# [null,data_tsvd,mc_tsvd]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'tsvd')
		[null,data_tsvd,mc_tsvd]=[tau,data_standard,mc_standard]

	# QUICK FIX FOR NO SYSTEMATICS
	if ('NoSys' in 'pyplots'):
		[null,data_pileup_plus,mc_pileup_plus]= [tau,data_standard,mc_standard]
		[null,data_pileup_minus,mc_pileup_minus]= [tau,data_standard,mc_standard]

		[null,data_bgnorm_plus,mc_bgnorm_plus]= [tau,data_standard,mc_standard]
		[null,data_bgnorm_minus,mc_bgnorm_minus]= [tau,data_standard,mc_standard]

		# Integrated luminosity up/down
		[null,data_lumi_plus,mc_lumi_plus]=[tau,data_standard,mc_standard]
		[null,data_lumi_minus,mc_lumi_minus]=[tau,data_standard,mc_standard]

		# Jet energy scale up/down, and smeared
		[null,data_jetscale_plus,mc_jetscale_plus]=[tau,data_standard,mc_standard]
		[null,data_jetscale_minus,mc_jetscale_minus]=[tau,data_standard,mc_standard]
		[null,data_jetsmear,mc_jetsmear]=[tau,data_standard,mc_standard]

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=[tau,data_standard,mc_standard]
		[null,data_muscale_minus,mc_muscale_minus]=[tau,data_standard,mc_standard]
		[null,data_musmear,mc_musmear]=[tau,data_standard,mc_standard]
		[null,data_phicorr,mc_phicorr]=[tau,data_standard,mc_standard]


		# BTag Efficiency Up/Down
		[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
		[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]
		[null,data_btag_misplus,mc_btag_misplus]=[tau,data_standard,mc_standard]
		[null,data_btag_misminus,mc_btag_misminus]=[tau,data_standard,mc_standard]
		[null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]
		# [null,data_roounfbayes,mc_roounfbayes]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'roounfbayes')

		# [null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',taush,'altunf')
		# [null,data_mcunf,mc_mcunf]=[tau,data_standard,mc_standard]
		[null,data_mcunf,mc_mcunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'mcunf')

		# [null,data_mcunf,mc_mcunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',taush,'mcunf')

		# [null,data_powunf,mc_powunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'powunf')

		[null,data_hltidiso,mc_hltidiso]=[tau,data_standard,mc_standard]

		# [null,data_roounfsvd,mc_roounfsvd]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'roounfsvd')

		# [null,data_roounfbayes,mc_roounfbayes]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'roounfbayes')
		[null,data_roounfbayes,mc_roounfbayes]=[tau,data_standard,mc_standard]
		# [null,data_roounfbin,mc_roounfbin]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'roounfbin')
		[null,data_roounfbin,mc_roounfbin]=[tau,data_standard,mc_standard]
		# [null,data_autobin,mc_autobin]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'autobin')

		# [null,data_tsvd,mc_tsvd]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'tsvd')
		[null,data_tsvd,mc_tsvd]=[tau,data_standard,mc_standard]
		#[null,data_matchsel,mc_matchsel]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'matchsel')
		[null,data_matchsel,mc_matchsel]=[tau,data_standard,mc_standard]

		# [null,data_tsvdnocov,mc_tsvdnocov]=[tau,data_standard,mc_standard]



	# Here we make a vary verbose table.	
	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU(+)','PU(-)','|','BG(+)','BG(-)','|','Lumi(+)','Lumi(-)','|','BEff(+)','BEff(-)','|','BMis(+)','BMis(-)','|','JScale(+)','JScale(-)','JetSmear','|','MuScale(+)','MuScale(-)','MuSmear','|','Generator(+)','Generator(-)','|','MCToy(+)','MCToy(-)','|','HLTIDISO(+)','HLTIDISO(-)','|','METPHI','|','ROOBAY','ROOBIN','JMATCH','|']]#,'|','Scale(+)','Scale(-)','Match(+)','Match(-)','|']]
	for x in range(len(data_standard)): # Loop over bins of the original output table
		thisbin=(data_standard[x])[0]    # this is the bin X1--X2
		center = (data_standard[x])[1]   # The is the central value of the unfolded data
		prediction = (mc_standard[x])[1] # This is the MC prediction

		# everything below are values of the data unfolded for the various systematic variations
		# scale_up = (data_scale_plus[x])[1]
		# scale_down = (data_scale_minus[x])[1]
		# match_up = (data_match_plus[x])[1]
		# match_down = (data_match_minus[x])[1]				

		pu_up = (data_pileup_plus[x])[1]
		pu_down = (data_pileup_minus[x])[1]

		bg_up = (data_bgnorm_plus[x])[1]
		bg_down = (data_bgnorm_minus[x])[1]

		lumi_up = (data_lumi_plus[x])[1]
		lumi_down = (data_lumi_minus[x])[1]

		btag_up = (data_btag_plus[x])[1]
		btag_down = (data_btag_minus[x])[1]

		btag_misup = (data_btag_misplus [x])[1]
		btag_misdown = (data_btag_misminus[x])[1]

		
		jet_up = (data_jetscale_plus[x])[1]
		jet_down = (data_jetscale_minus[x])[1]
		jet_smear = (data_jetsmear[x])[1]
		
		mu_up = (data_muscale_plus[x])[1]
		mu_down = (data_muscale_minus[x])[1]
		mu_smear = (data_musmear[x])[1]
		met_phicorr = (data_phicorr[x])[1]

		unf_bay = (data_roounfbayes[x])[1]
		# unf_svd = (data_roounfsvd[x])[1]	
		unf_bin = (data_roounfbin[x])[1]
		# man_bin = (data_autobin[x])[1]
		# tsvdnocov = (data_tsvdnocov[x])[1]

		unf_mat = (data_matchsel[x])[1]


		# GENERATOR AND MC TOY ERRORS

		generator= data_altunf[x][1]
		mctoy= data_mcunf[x][1]

		centval = float(center.split("+-")[0])
		alt = float(generator.split("+-")[0])
		mcu = float(mctoy.split("+-")[0])


		# MAKE GENERATOR SYMMETRIC
		if alt>0 and centval:
			if alt>centval:
				gen_factor = alt/centval
			else:
				gen_factor = centval/alt
		else:
			gen_factor = 1.0
		gen_1 = centval*gen_factor
		gen_2 = centval/gen_factor

		gens = [gen_1,gen_2]
		gens.sort()
		gen_down = str(round(gens[0],2)) + '+-'+generator.split('+-')[-1]
		gen_up = str(round(gens[1],2)) + '+-'+generator.split('+-')[-1]


		# MAKE MC TOY SYMMETRIC
		if mcu>0 and centval:
			if mcu>centval:
				toy_factor = mcu/centval
			else:
				toy_factor = centval/mcu
		else:
			toy_factor = 1.0
		toy_1 = centval*toy_factor
		toy_2 = centval/toy_factor

		toys = [toy_1,toy_2]
		toys.sort()
		toy_down = str(round(toys[0],2)) + '+-'+mctoy.split('+-')[-1]
		toy_up = str(round(toys[1],2)) + '+-'+mctoy.split('+-')[-1]



		# MUON ID and ISO
		muoneff= data_hltidiso[x][1]
		id_1 = float(muoneff.split("+-")[0])
		centval = float(center.split("+-")[0])
		id_2 = centval - (id_1-centval)
		ids = [id_1,id_2]
		ids.sort()
		id_down = str(round(ids[0],2)) + '+-'+muoneff.split('+-')[-1]
		id_up = str(round(ids[1],2)) + '+-'+muoneff.split('+-')[-1]




		# Strip out the +- statistical uncertainty for the various systematics. We will only consider statistical uncertainties on the central values. 
		for v in ['pu_up','pu_down','bg_up','bg_down','jet_up','jet_down','jet_smear','mu_up','mu_down','mu_smear','lumi_up','lumi_down','btag_up','btag_down','btag_misup','btag_misdown','gen_down','gen_up','toy_down','toy_up','id_up','id_down','met_phicorr','unf_bay','unf_bin','unf_mat']:
			exec(v+'='+v+'.split("+-")[0]')
		
		# Add a line to the data table.
		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|',bg_up,bg_down,'|',lumi_up,lumi_down,'|',btag_up,btag_down,'|',btag_misup,btag_misdown,'|',jet_up,jet_down,jet_smear,'|',mu_up,mu_down,mu_smear,'|',gen_up,gen_down,'|',toy_up,toy_down,'|',id_up,id_down,'|',met_phicorr,'|',unf_bay,unf_bin,unf_mat,'|'])#,'|',scale_up,scale_down,match_up,match_down,'|'])
	
	# Here we print a cleaned-up table.
	f = open('table_tmp.txt','w')
	print ' GETTING READY TO PRINT TABLE!!!'
	for line in data_table:
		print 'OUTPUT TABLE PRINTING HERE...'
		line=str(line)
		line=line.replace('[','')
		line=line.replace(']','')
		line=line.replace('\'','')
		line=line.replace('\t',' ')
		#line=line.replace('|','-')

		for x in range(10):
			line=line.replace('  ',' ')

		f.write(line+'\n')
	f.close()
	
	# Save the table to a txt file.
	fvarname = recovariable+xlabel[-1]
	fvarname = fvarname.replace(')','')
	fvarname = fvarname.replace('(','')
	# os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+recovariable+xlabel[-1]+'.txt')
	os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+fvarname+'.txt')

	os.system('rm table_tmp.txt')


# This is a quick utility to take a table from above, and return it as a python list which is more easy to handle.
def tabletolist(table):
	output=[]
	Nvertical=0
	Nhorizontal=0
	
	for line in open(table,'r'): # Loop on lines in the text table

		# Remove characters to make the table space-delimited
		line=line.replace('|','')
		line=line.replace('\t',' ')
		line=line.replace(' +- ','+-')
		line=line.replace(' - ','TO')
		line=line.replace('\n','')
		for x in range(20):
			line=line.replace('  ',' ')
			if line[0]==' ':
				line=line[1:]
			if line[-1]==' ':
				line=line[:-1]

		# Split space-delimited line into list
		line=line.split(' ')
		# Add line to the list output
		output.append(line)
		# Add one to the verticle dimension (number of lines)
		Nvertical += 1
	# Horizontal dimension is the number of columns
	Nhorizontal = len(output[0])
	
	# returned output is the Vertical and horizontal dimension, and the output itself.
	return [Nvertical,Nhorizontal,output]

# Quickly get a cell from a tabletolist type of table.
def getcell(listedtable,V,H):
	# Vertical and horizontal dimension
	Nvertical = listedtable[0]
	Nhorizontal=listedtable[1]
	# This is the "output" of tabletolist, or the actual table content
	table=listedtable[2]
	# Sanity check that the dimensions are ok
	if V>=Nvertical or H>=Nhorizontal:
		return 'NA'
	# Get the cell content
	content = table[V][H]
	return content

# This loops on a "tabletolist" type of table, and returns the binning on text or TeX formmat
def getbinning(listedtable):
	element = ''
	contents=[]
	n=0
	# While loop over rows. 
	while True:
		n+= 1
		# The binning is the first (zeroth) element.
		element =getcell(listedtable,n,0) 
		if element=='NA': # Problem with the table or dimensions
			break
		# Add the binning value to the list of elements.
		contents.append(element)
	binning = []
	# Here we convert the binning to a real numerical list
	for c in contents:
		edges=c.split('TO')
		for e in edges:
			if float(e) not in binning:
				binning.append(float(e))
	# Also convert to LaTeX style
	texcontents = ['$ '+ c+ ' $' for c in contents]
	return [texcontents,binning]

# Here we can get an entire column of a "tabletolist" tpe of table, and return as a latex entry or list of means and errors.
def getcolumn(listedtable,column):
	element = ''
	contents=[]
	n=0
	# print ' ***********'
	# print listedtable
	while True:
		n+= 1
		element =getcell(listedtable,n,column)

		if element=='NA':
			break
		contents.append(element)	
	mean = []
	error=[]
	for c in contents:
		if '+-' in c:
			m,e = float(c.split('+-')[0]), float(c.split('+-')[1])
		else:
			m,e = float(c),0.0
		mean.append(m)
		error.append(e)
	texcontents=[ '$ ' +c.replace('+-', '\pm')+' $' for c in contents]
	return [texcontents,mean,error]

# Here we get the measurement (data unfolded column) of a table as tex and mean with assym errors.
def getmeasurement(listedtable):
	[meas_tex, meas_mean, meas_staterr] = getcolumn(listedtable,2)
	m=3
	variations=[]
	while True:
		[null, variation, variation_staterr] = getcolumn(listedtable,m)
		#print variation
		if 'NA' in str(variation) or len(str(variation)) < 5:
			break
		variations.append(variation)
		m+=1

	print variations[-1]
	print variations[-2]
	print variations[-3]
	print variations[-4]

	num = len(variations[0])
	
	tex = []
	means=[]
	err_plus=[]
	err_minus=[]
	verbose_errors = []
	for n in range(num):
		plus_err = []
		minus_err = []
		mean = meas_mean[n]
		errors=[]
		rel_err = 0
		for v in range(len(variations)):
			if mean>0 and variations[v][n] > 0:
				errors.append((variations[v][n] - mean)/mean)
				rel_err = (meas_staterr[n])/(meas_mean[n])
			else: 
				errors.append(0)
		#print mean,errors
		
		filtered_errors=[]
		def filter_pair(values):
			output = []
			if values[0] * values[1] < 0:
				return values
			else:
				if abs(values[0]) > abs(values[1]):
					return [values[0]]
				else:
					return [values[1]]
		
		PUerrors = filter_pair([errors[0],errors[1]])
		BGerrors = filter_pair([errors[2],errors[3]])

		LUMIerrors=filter_pair([errors[4],errors[5]])
		BTAGerrors=filter_pair([errors[6],errors[7]])
		BTAGMerrors=filter_pair([errors[8],errors[9]])



		JESerrors=filter_pair([errors[10],errors[11]])
		JERerrors=[errors[12]]
		MESerrors=filter_pair([errors[13],errors[14]])
		MERerrors=[errors[15]]
		GENerrors = [errors[16],errors[17]]
		TOYerrors = [errors[18],errors[19]]

		IDerrors = [errors[20],errors[21]]
		METerrors = [errors[22]]

		BAYerrors = [errors[23]]
		# SVDNOCOVerrors = [errors[20]]
		# SVDerrors = [errors[21]]
		# BINBYBINerrors = [errors[22]]
		ROOBINBYBINerrors = [errors[24]]
		MATerrors = [errors[25]]
		# print MATerrors
		# print ' *** ',len(errors)
		# SCALEerrors=filter_pair([errors[12],errors[13]])
		# MATCHerrors=filter_pair([errors[14],errors[15]])
		STATerrors=[rel_err, -rel_err]
		
		allerrors=PUerrors+BGerrors+LUMIerrors+BTAGerrors+BTAGMerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors+GENerrors+TOYerrors+IDerrors+METerrors+BAYerrors+ROOBINBYBINerrors+MATerrors #SCALEerrors+MATCHerrors+STATerrors
		# Quick hack to ignore shape systematics
		# allerrors=PUerrors+LUMIerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors

		standard_errorset = [PUerrors,BGerrors,LUMIerrors,BTAGerrors,BTAGMerrors,JESerrors,JERerrors,MESerrors,MERerrors,STATerrors,GENerrors,TOYerrors,IDerrors,METerrors,BAYerrors,ROOBINBYBINerrors,MATerrors]#SCALEerrors,MATCHerrors,STATerrors]

		def verbose_errorset(errset):
			outerrs = []
			for e in errset:
				maxerr = 0
				for error in e:
					if abs(error) > maxerr:
						maxerr = abs(error)
				maxerr = 100*maxerr
				maxerr = str(round(maxerr,2))
				outerrs.append(maxerr)
			return outerrs

		verbose_errors.append(verbose_errorset(standard_errorset))

		pos_error = 0
		neg_error = 0
		for x in allerrors:
			if abs(x)>10*mean:
				continue
			if x>0:
				pos_error += x*x
			if x<0:
				neg_error += x*x
		pos_error = float(str(round(mean*math.sqrt(pos_error),2)))
		neg_error = float(str(round(-mean*math.sqrt(neg_error),2)))
		
		#print  mean, pos_error,neg_error
		
		tex.append('$ ' + str(mean) +'_{'+ str(neg_error) +'}'+'^{+'+str(pos_error)  +'}'  ' $')
		means.append(mean)
		err_plus.append(pos_error)
		err_minus.append(neg_error) 
	
	verbose_errors_out = zip(*verbose_errors)

	return [tex,means,err_plus, err_minus,verbose_errors_out]

def roundnumbers(astring,nround):

	nums='.0123456789'

	allnumstrings = []

	numstring = ''
	for x in astring:
		if x in nums:
			numstring += (x)
		else:
			numstring += ','
	for z in range(20):
		numstring = numstring.replace(',,',',')
	numstring = numstring.split(',')
	# print numstring
	converts = []
	for n in numstring:
		if len(n)>2:
			n_in = n
			n_out = str(round((float(n)),nround))
			converts.append([n_in,n_out])
	# maxdec = 0

	# for c in converts:
	# 	if len(c[1])>maxdec:
	# 		maxdec = len(c[1])
	# for n in range(5):
	# 	for c in range(len(converts)):
	# 		if len(converts[c][1])<maxdec:
	# 			converts[c][1] += '0'
	for c in converts:
		astring = astring.replace(c[0],c[1])


	return astring


# Here we can convert a nummber of colums to a latex  style table.
def TexTableFromColumns(columns):
	global_length = len(columns[0])
	for c in columns:
		if len(c) != global_length:
			return 'ERROR: Columns not of equal length!!!'
	table = '\n'
	for x in range(global_length):
		line=''
		for c in columns:
			line+=c[x] + ' ,& '
			
		line+='\n'
		line=line.replace('TO',' -- ')
		line=line.replace('& \n',' \\\\\n')
		table+= line
	table+='\n'
	table = roundnumbers(table,3)
	return table	

# Quickly write a python string to a text file, creating neat spacing with whatever spacer character
def StringToFile(string,afile, spacer):
	f = open(afile,'w')
	for line in string:
		f.write(line)
	f.close()
	
	if spacer != '':
		os.system('cat '+afile+' | column -t -s"'+spacer+'" > '+afile+'edit')
		os.system('mv '+afile+'edit '+afile)
		
	print 'File ', file, ' has been written.'

# Normalize all numbers in a text file with a given norm factor. Useful for dividing by the integrated luminosity
# to get a table of cross-sections instead of event counts. 
def NormalizeTexTable(file,norm):
	nums='.0123456789'
	
	def IsNumber(Character):
		if Character in nums:
			return True
		else:
			return False
	newtable=''
	for line in open(file):
		line=line.split('&')
		#print line
		newline = ''
		for element in range(len(line)):
			if element==0:
				newline += line[element]
				continue
			element = line[element]
			isnumber=False
			runningnumber=''
			
			for x in element:
				isnumber = IsNumber(x)
				if (isnumber):
					runningnumber+=x
				else: 
					if runningnumber!='':
						runningnumber = str(round(float(runningnumber)/norm,2))
						newline+=runningnumber
						runningnumber=''
						newline += x
					else:
						newline+=x
						#print newline
				#print newline
			newline += ' ,& '
		newline = newline.replace('\n ,& ','\n')
		newtable += newline
	return newtable

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
	#hout.SetMaximum(2.0*hout.GetMaximum())
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

	if plottype=="TopPlot":
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.05)
		hout.GetYaxis().SetTitleSize(.05)
		# hout.GetXaxis().CenterTitle()
		# hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(0.9)
		hout.GetYaxis().SetTitleOffset(1.15)
		hout.GetYaxis().SetLabelSize(.05)
		hout.GetXaxis().SetLabelSize(.05)
		hout.GetYaxis().SetNdivisions(508)


	if plottype=="SubPlot":
		hout.GetYaxis().SetNdivisions(307,True)
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.13)
		hout.GetYaxis().SetTitleSize(.13)
		# hout.GetXaxis().CenterTitle()
		# hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetLabelSize(.09)
		hout.GetXaxis().SetLabelSize(.09)

	return [hout,[mean,up,down,binset]]


def CreateWindowFromVerbse(_verbs,Name,label,style,norm,plottype,symmetrize):
	meansets = []
	for L in _verbs:
		# print L
		meansets.append(L[0])
	_mins = []
	_maxs = []
	_centers = []
	_ups = []
	_downs = []
	binrange = range(len(meansets[0]))


	for m in binrange:
		entries = [_means[m] for _means in meansets]
		_mins.append(min(entries))
		_maxs.append(max(entries))
		_centers.append(  meansets[0][m] )
		_iup = abs(_maxs[-1] - _centers[-1])
		_idown = abs(_mins[-1] - _centers[-1])

		if symmetrize: 
			_ierr = max([_iup,_idown])
			_iup = _ierr
			_idown = _ierr


		_ups.append(_iup)
		_downs.append(_idown )
		# print   ' --------------------------'
		# print _centers[-1], _ups[-1], _downs[-1]
		if 'ct10' in Name:
			# print ' ------ Mod Window by 1.645 for 1 sigma band'
			_ups[-1] = _ups[-1]/1.645
			_downs[-1] = _downs[-1]/1.645
			# print _centers[-1], _ups[-1], _downs[-1]


	binning = _verbs[0][-1]
	OutputHisto = CreateHistoFromLists(binning, Name,label, _centers, _ups,_downs, style,norm,plottype)

	return OutputHisto

def addlists(L1,L2,sign):
	L3 = []
	for x in range(len(L1)):
		L3.append(L1[x]+sign*L2[x])
	return L3
def CreateWindowFromVerbseWindows(_verbs,Name,label,style,norm,plottype,symmetrize):
	meansets = []
	for L in _verbs:
		meansets.append(L[0])
		if L != _verbs[0]:
			meansets.append( addlists(L[0],L[1],1) )
			meansets.append( addlists(L[0],L[2],-1) )
		# print L
	_mins = []
	_maxs = []
	_centers = []
	_ups = []
	_downs = []
	binrange = range(len(meansets[0]))


	for m in binrange:
		entries = [_means[m] for _means in meansets]
		_mins.append(min(entries))
		_maxs.append(max(entries))
		_centers.append(  meansets[0][m] )
		_iup = abs(_maxs[-1] - _centers[-1])
		_idown = abs(_mins[-1] - _centers[-1])

		if symmetrize: 
			_ierr = max([_iup,_idown])
			_iup = _ierr
			_idown = _ierr


		_ups.append(_iup)
		_downs.append(_idown )
		# print   ' --------------------------'
		# print _centers[-1], _ups[-1], _downs[-1]

	binning = _verbs[0][-1]
	OutputHisto = CreateHistoFromLists(binning, Name,label, _centers, _ups,_downs, style,norm,plottype)

	return OutputHisto



def MergeErrorsFromVerbse(_verbs,Name,label,style,norm,plottype,symmetrize):
	meansets = []
	upsets = []
	downsets = []
	for L in _verbs:
		meansets.append(L[0])
		upsets.append(L[1])
		downsets.append(L[2])

	_mins = []
	_maxs = []
	_centers = []
	_ups = []
	_downs = []
	binrange = range(len(meansets[0]))
	for m in binrange:
		meanentries = [contents[m] for contents in meansets]
		upentries = [contents[m] for contents in upsets]
		downentries = [contents[m] for contents in downsets]


		_centers.append(  meansets[0][m] )

		_iup = 0.0
		_idown = 0.0

		for xx in upentries:
			_iup += xx*xx		
		for xx in downentries:
			_idown += xx*xx		
		_iup = math.sqrt(_iup)
		_idown = math.sqrt(_idown)


		if symmetrize: 
			_ierr = max([_iup,_idown])
			_iup = _ierr
			_idown = _ierr

		_ups.append(_iup)
		_downs.append(_idown )



	binning = _verbs[0][-1]

	# print 'Binning:',binning
	# print 'Name:',Name
	# print 'Label:',label
	# print 'Centers:',_centers
	# print 'Ups:',_ups
	# print 'Downs:',_downs
	# print 'Style:',style
	# print 'PlotType:',plottype
	OutputHisto = CreateHistoFromLists(binning, Name,label, _centers, _ups,_downs, style,norm,plottype)

	return OutputHisto


# Take a given binning, and means with errors, and create a TGraphAsymErrors output.
def CreateBandHistoFromLists(binning, name, label, mean, up, down, style,normalization,plottype):

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
	# print X
	# print Xplus
	# print Xminus
	# hout.GetXaxis().SetRangeUser(X[0],X[-1])
	# hout.GetXaxis().SetLimits(X[0],X[-1])

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
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

	if plottype=="TopPlot":
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.05)
		hout.GetYaxis().SetTitleSize(.05)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		# hout.GetXaxis().SetTitleOffset(0.9)
		# hout.GetYaxis().SetTitleOffset(1.15)
		hout.GetYaxis().SetLabelSize(.05)
		hout.GetXaxis().SetLabelSize(.05)


	if plottype=="SubPlot":
		hout.GetYaxis().SetNdivisions(308,True)
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.13)
		hout.GetYaxis().SetTitleSize(.13)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		# hout.GetXaxis().SetTitleOffset(.48)
		hout.GetYaxis().SetTitleOffset(.43)
		hout.GetYaxis().SetLabelSize(.09)
		hout.GetXaxis().SetLabelSize(.09)

	return [hout,[mean,up,down,binset]]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, ncompare, quantity, WRenormalizationForRivet):

	# print ' ------> ',rivetvariable
	frivet = TFile.Open(rivetfile)
	if 'SummaryFile' not in rivetfile:
		trivet = frivet.Get("RivetTree")
	else:
		trivet = frivet.Get("PhysicalVariables")

	if 'eta' in rivetvariable:
		rivetvariable = 'abs('+rivetvariable+')'
	Name = "MadGraph"*("Madgraph" in rivetfile)+"MadGraphAOD"*("MG.root" in rivetfile) + "Pythia"*("Pythia" in rivetfile)  + "Sherpa"*("Sherpa" in rivetfile) + ("PROBLEM")*(("Madgraph" not in rivetfile)*("Pythia" not in rivetfile)*("Sherpa" not in rivetfile))
	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
	hrivet.Scale(4955.0*31314.0/(1.0*original_events))



	if 'njet_WMuNu' in rivetvariable and len(binning) > 7:
	
		print 'Converting',rivetfile,':',rivetvariable,' to integrated histo.'

		for _n in range(hrivet.GetNbinsX()):
			__cont = 0.0
			__err = 0.0
			for __n in range(hrivet.GetNbinsX()):
				if __n >= _n:
					__cont += hrivet.GetBinContent(__n) 
					__err += hrivet.GetBinError(__n) **2.0
					# print  ' --------------------', hrivet.GetBinError(__n), hrivet.GetBinError(__n) **2.0
			__err = math.sqrt(__err)
			# print '  ||||||||| ',__cont, __err, hrivet.GetBinContent(_n), hrivet.GetBinError(_n)
			hrivet.SetBinContent(_n,__cont)
			hrivet.SetBinError(_n,__err)

		binning = ConvertBinning([6 ,0.5,6.5])

	# print 'RIVETSELECTION: ',selection+'*'+WRenormalizationForRivet
	# print 'RIvet histo: ',rivetfile, rivetvariable, binning
	means=[]
	errs=[]
	if hrivet.Integral() > 0 :
		rivetscale = ncompare/(hrivet.Integral())
	else: 
		rivetscale = 1.0
	# hrivet.Scale(rivetscale)
	scalefactor=1.0


	# Fix for differential
	for x in range(len(binning)-1):
		means.append(scalefactor*(hrivet.GetBinContent(x+1))/(hrivet.GetBinWidth(x+1)))
		errs.append(scalefactor*(hrivet.GetBinError(x+1))/(hrivet.GetBinWidth(x+1)))

	# for x in range(len(binning)-1):
	# 	means.append(scalefactor*(hrivet.GetBinContent(x+1)))
	# 	errs.append(scalefactor*(hrivet.GetBinError(x+1)))

	if normalization==0:
		label = [label, 'Events/bin']
	else:
		label = [label, '#sigma [pb]']


	# print ' ***',means

	RivetOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	RivetOutputHisto[0].GetXaxis().SetTitle(label[0])
	RivetOutputHisto[0].GetYaxis().SetTitle(label[1])
	RivetOutputHisto[0].GetXaxis().SetTitleFont(42)
	RivetOutputHisto[0].GetYaxis().SetTitleFont(42)
	RivetOutputHisto[0].GetXaxis().SetLabelFont(42)
	RivetOutputHisto[0].GetYaxis().SetLabelFont(42)

	RivetOutputHisto[0].GetYaxis().SetTitleFont(42);
	RivetOutputHisto[0].GetXaxis().SetTitleSize(.1);
	RivetOutputHisto[0].GetYaxis().SetTitleSize(.1);
	RivetOutputHisto[0].GetXaxis().CenterTitle();
	RivetOutputHisto[0].GetYaxis().CenterTitle();
	RivetOutputHisto[0].GetXaxis().SetTitleOffset(1.1);
	RivetOutputHisto[0].GetYaxis().SetTitleOffset(1.1);
	RivetOutputHisto[0].GetYaxis().SetLabelSize(.1);
	RivetOutputHisto[0].GetXaxis().SetLabelSize(.1);
	return [RivetOutputHisto,rivetscale]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def BlackHatHisto(rivetvariable, binning, standard_name, label, style, quantity, ncompare, normalization,hadhisto,nonhadhisto,dohadrenorm,bhdir):

	# bhdir = 'hists5/hists_CT10/'

	# print 'BlackhatHisto:',standard_name,'/',rivetvariable, 'from',bhdir

	bhdir += '/'
	Name = 'BlackHat'	
	bhfile = bhdir+'W1j_all.root'
	bhfiles = [bhdir+'W'+str(nn)+'j_all.root' for nn in [0,1,2,3,4]]


	if 'njet_WMuNu' in rivetvariable and len(binning) > 6:
		binning = ConvertBinning([4 ,0.5,4.5])

	if 'jet1' in standard_name:
		bhfile = bhfiles[1]
	if 'jet2' in standard_name:
		bhfile = bhfiles[2]
	if 'jet3' in standard_name:
		bhfile = bhfiles[3]
	if 'jet4' in standard_name:
		bhfile = bhfiles[4]			



	# print 'For - ',rivetvariable, ' -- using: ',bhfile
	# print "  BH ------->  ",rivetvariable, " --> ",rivetvariable.replace('htjets','ht')
	fblackhat = TFile.Open(bhfile)
	hblackhat = fblackhat.Get(rivetvariable.replace('htjets','ht'))

	# print ' BLACKHAT LOG '
	# hblackhat.Print('range')

	if type(hblackhat) != TH1D:
		print ' Histogram problems - ignoring this one!'


	print 'BH Histo:', hblackhat, bhfile, rivetvariable.replace('htjets','ht')
	hblackhat.Print('range')

	# print hblackhat
	# print hblackhat.GetEntries()
	# sys.exit()
	# print "    --- > int ---> ",hblackhat.GetEntries(),hblackhat.Integral()
	# print 'Blackhat histo for ',rivetvariable, 'with binning',binning

	# for nn in range((hblackhat.GetNbinsX())+2):
	# 	print hblackhat.GetBinCenter(nn) - hblackhat.GetBinWidth(nn)*0.5

	means=[]
	errs=[]
	scalefactor = 1.0
	# for x in range(len(binning)-1):
	# 	means.append(scalefactor*(hblackhat.GetBinContent(x+1)))
	# 	errs.append(scalefactor*(hblackhat.GetBinError(x+1)))

	if 'Count' in standard_name:
		# hblackhat = TH1D('hblackhat','hblackhat',6,array('d',[0.5,1.5,2.5,3.5,4.5,5.5,6.5]))
		for nn in [1,2,3,4]:
			bhindex = 0
			newbhfile = bhfiles[nn]
			lhs = 99
			for nb in range(hblackhat.GetNbinsX()+2):	
				lhs = hblackhat.GetBinCenter(nb) - hblackhat.GetBinWidth(nb)*0.5
				lhs = int(lhs)
				if lhs == nn:
					bhindex = nb

			bhfile = TFile.Open(newbhfile)
			bhsource = bhfile.Get(rivetvariable)

			# bhsource = TFile.Open(newbhfile).Get(rivetvariable)

			if type(bhsource) != TH1D:
				print ' Histogram problems - ignoring this one!'				
				return [[None,None],[None]]

			bhsourceindex = 0
			for nb in range(bhsource.GetNbinsX()+2):	
				lhs = bhsource.GetBinCenter(nb) - bhsource.GetBinWidth(nb)*0.5
				lhs = int(lhs)
				if lhs == nn:
					bhsourceindex = nb

			binloc = bhsource.GetBinCenter(bhsourceindex) - 0.5					
			binloc2 = hblackhat.GetBinCenter(bhindex) - 0.5					

			newcont = bhsource.GetBinContent(bhsourceindex)			
			newerr = bhsource.GetBinError(bhsourceindex)

			if ('preexc' in standard_name) and (nn <4):
				newcont += bhsource.GetBinContent(bhsourceindex+1)
				newerr *= newerr
				newerr += (bhsource.GetBinError(bhsourceindex+1))**2.0
				newerr = math.sqrt(newerr)

			bhindex = bhindex -1 
			hblackhat.SetBinContent(bhindex,newcont)
			hblackhat.SetBinError(bhindex,newerr)

			bhfile.Close()



	bhscale = (4955.0/1000.0)
	hblackhat.Scale(bhscale)

	# print binning
	bhbinning = []
	rhs = 0.0
	hadsfs = []
	# print hadhisto
	# print nonhadhisto
	# print len(hadhisto)
	# print hadhisto
	for x in range(len(binning)-1):

		_x = x

		if 'ht_jet1' in standard_name:
			_x += 0
		if 'ht_jet2' in standard_name:
			_x += 1
		if 'ht_jet3' in standard_name:
			_x += 2
		if 'ht_jet4' in standard_name:
			_x += 3

		hadsf = 1.0
		if (hadhisto[0][x] > 0.0) and  (nonhadhisto[0][x]> 0.0):
			hadsf = hadhisto[0][x]/nonhadhisto[0][x]

		# hadsf = 1.0 # QUICK FIX!	
		hadsfs.append(hadsf)

		meanval = scalefactor*(hblackhat.GetBinContent(_x+1))

		means.append( meanval*hadsf )
		bhbinning.append( hblackhat.GetBinCenter(_x+1) - 0.5*hblackhat.GetBinWidth(_x+1) )
		rhs = (hblackhat.GetBinCenter(_x+1) + 0.5*hblackhat.GetBinWidth(_x+1))
		# errs.append(means[-1]*0.05)
		errs.append(hadsf*scalefactor*(hblackhat.GetBinError(_x+1)) )		

		# print means[-1], errs[-1], hblackhat.GetBinCenter(_x+1), errs[-1]/means[-1]
	# print ' --------------- blackhat sfs and logs ----------------'
	# print hadsfs
	# print means
	# print ' --------------- blackhat sfs and logs ----------------'

	# sys.exit()
	# print '  d'
	bhbinning.append(rhs)
	if 'Count' in standard_name:
		for iii in range(2):
			binning.append(binning[-1]+1.0)
			means.append(0.0)
			errs.append(0.0)


	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']

	# print 'd2'
	blackhatscale = ncompare/(hblackhat.Integral())
	# print 'd3'
	# print 'BH:',means
	BlackHatOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")
	# print 'd4'
	BlackHatOutputHisto[0].GetXaxis().SetTitle(label[0])
	BlackHatOutputHisto[0].GetYaxis().SetTitle(label[1])
	BlackHatOutputHisto[0].GetXaxis().SetTitleFont(42)
	BlackHatOutputHisto[0].GetYaxis().SetTitleFont(42)
	BlackHatOutputHisto[0].GetXaxis().SetLabelFont(42)
	BlackHatOutputHisto[0].GetYaxis().SetLabelFont(42)

	BlackHatOutputHisto[0].GetYaxis().SetTitleFont(42);
	BlackHatOutputHisto[0].GetXaxis().SetTitleSize(.1);
	BlackHatOutputHisto[0].GetYaxis().SetTitleSize(.1);
	BlackHatOutputHisto[0].GetXaxis().CenterTitle();
	BlackHatOutputHisto[0].GetYaxis().CenterTitle();
	BlackHatOutputHisto[0].GetXaxis().SetTitleOffset(1.3);
	BlackHatOutputHisto[0].GetYaxis().SetTitleOffset(1.3);
	BlackHatOutputHisto[0].GetYaxis().SetLabelSize(.1);
	BlackHatOutputHisto[0].GetXaxis().SetLabelSize(.1);
	# print '  e'
	fblackhat.Close()


	# print means
	# print errs
	# print BlackHatOutputHisto

	return [BlackHatOutputHisto,blackhatscale]


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

	[mean1,up1,down1,binset1]=gv2
	[mean2,up2,down2,binset2]=gv1

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
		ratmean.append(rat)
		raterr_up.append(window[0])
		raterr_down.append(window[1])
		
		yvalues+= [rat+window[0],rat-window[1]]


	yup = round((1.2*max(yvalues)),2)
	ydown = round((0.8*min(yvalues)),2)
	if yup>5: yup=5
	if ydown<-5: ydown=-5
	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]



# Using basic asymmetric errors.
def HadRatioPlot(gv1, gv2,XName,binning,fname):

	binset = ConvertBinning(binning)
	style = [0,20,.7,1,1]

	[mean1,up1,down1,binset]=gv1
	[mean2,up2,down2,binset]=gv2

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []
	print '1'
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
			rat = 1.0
		ratmean.append(rat)

		raterr = math.sqrt(abs(u1 - m1)**2.0 + abs(u2-m2)**2.0)


		raterr_up.append(raterr)
		raterr_down.append(raterr)
		
	print '2'
	[res,[null,null2,null3,null4]] = CreateHistoFromLists(binset, "example",[XName,"Ratio"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")
	print '3'
	cp = TCanvas("cp","",500,800)
	print '4a'
	pad1a = TPad( 'pad1a', 'pad1a', 0.0, 0.0, 1.0, 1.0 )#divide canvas into pads
	print '4b'
	res.Draw("EP")
	outname = ('HadronizationPlots/'+fname+'_HadComp').replace('.','_')
	print '4c', outname
	cp.Print(outname+'.png')
	print 5
	cp.Print(outname+'.pdf')
	print 6


# Using basic asymmetric errors.
def DivideTGraphsFlatRel(gv1, gv2,style):

	# Inverted to flip ratios!
	[mean1,up1,down1,binset1]=gv2
	[mean2,up2,down2,binset2]=gv1

	print gv1
	print gv2

	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean1[x] # mc
		m2=mean2[x] # Dat
		u1=up1[x]   # mc 
		u2=up2[x]   # Dat
		d1=down1[x] # mc
		d2=down2[x] # dat


		rat = 5.0
		ratup = rat
		ratdown = rat

		if m2 != 0:
			# print m2,d2
			rat = m1/m2
			ratmax = (m1+abs(u1))/m2
			ratmin = (m1-abs(d1))/m2
			ratup = ratmax - rat
			ratdown = rat-ratmin


		if m1==0:
			rat = 5.0

		ratmean.append(rat)
		raterr_down.append(ratdown)
		raterr_up.append(ratup)
		
	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[2,0]]


# # Using basic asymmetric errors.
# def DivideTGraphsFlatRel(gv1, gv2,style):

# 	# Inverted to flip ratios!
# 	[mean1,up1,down1,binset1]=gv2
# 	[mean2,up2,down2,binset2]=gv1

# 	print gv1
# 	print gv2

# 	if binset1!=binset2:
# 		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
# 		sys.exit()
# 	binset=binset1

# 	ratmean = []
# 	raterr_up = []
# 	raterr_down = []

# 	yvalues = []

# 	for x in range(len(binset)-1):
# 		m1=mean1[x]
# 		m2=mean2[x]
# 		u1=up1[x]
# 		u2=up2[x]
# 		d1=down1[x]
# 		d2=down2[x]


# 		rat = 5.0
# 		ratup = rat
# 		ratdown = rat

# 		if m2 != 0:
# 			# print m2,d2
# 			rat = m1/m2
# 			ratup = m1/(m2 + u2)
# 			if m2 != d2:
# 				ratdown = m1/(m2 - d2)
# 			else:
# 				ratdown = 99

# 		if m1==0:
# 			rat = 5.0

# 		window = [0,0]


# 		window = [ratup - rat, ratdown - rat]
# 		window.sort()

# 		print rat, window

# 		ratmean.append(rat)
# 		raterr_down.append(abs(window[0]))
# 		raterr_up.append(abs(window[1]))
		
# 		# print rat, ratup, ratdown, window

# 		# raterr_up.append(window[0])
# 		# raterr_down.append(window[1])



# 	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[2,0]]


# Using basic asymmetric errors.
# def DivideTGraphsFlatRel(gv1, gv2,style):

# 	# Inverted to flip ratios!
# 	[mean1,up1,down1,binset1]=gv2
# 	[mean2,up2,down2,binset2]=gv1

# 	print gv1
# 	print gv2

# 	if binset1!=binset2:
# 		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
# 		sys.exit()
# 	binset=binset1

# 	ratmean = []
# 	raterr_up = []
# 	raterr_down = []

# 	yvalues = []

# 	for x in range(len(binset)-1):
# 		m1=mean1[x]
# 		m2=mean2[x]
# 		u1=up1[x]
# 		u2=up2[x]
# 		d1=down1[x]
# 		d2=down2[x]


# 		rat = 5.0

# 		if m2 != 0:
# 			rat = m1/m2


# 		ratmean.append(rat)
# 		raterr_down.append(abs(window[0]))
# 		raterr_up.append(abs(window[1]))
		
# 		# print rat, ratup, ratdown, window

# 		# raterr_up.append(window[0])
# 		# raterr_down.append(window[1])



# 	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[2,0]]




# Using basic asymmetric errors.
def CentralRatioBand(gv, style):

	[mean,up,down,binset]=gv


	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean[x]
		u1=up[x]
		d1=down[x]

		# print binset[x],m1,u1,d1

		uval = 0.0
		dval = 0.0
		if m1 > 0:
			uval = u1/m1
			dval = d1/m1
		ratmean.append(1.0)
		raterr_down.append(dval)
		raterr_up.append(uval)
		# print uval,dval
		# yvalues+= [1.0-uval,1.0+dval]
		yvalues+= [1.0-dval,1.0+uval] # Mod for inverted ratios


	yup = round((1.0*max(yvalues)),2)
	ydown = round((1.0*min(yvalues)),2)



	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]

def AbridgeHistoList(h,nbins):
	[a,b,c,d] = h
	_a = []
	_b = []
	_c = []
	_d = []
	for x in range(nbins):
		_a.append(a[x])
		_b.append(b[x])
		_c.append(c[x])
		_d.append(d[x])
	_d.append(d[range(nbins)[-1]+1])
	return [_a,_b,_c,_d]

# This creates the final "results"-style plot!
def FinalHisto(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalization,sel,dobhonly):

	# c1 = TCanvas("c1","",700,800)
	c1 = TCanvas("c1","",200, 100, 600, 800)
	pad1 = TPad( 'pad1', 'pad1', 0.01, 0.55, 0.99, 0.99 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.01, 0.39, 0.99, 0.55 )
	pad3 = TPad( 'pad3', 'pad3', 0.01, 0.23, 0.99, 0.39 )
	pad4 = TPad( 'pad4', 'pad4', 0.01, 0.01, 0.99, 0.23 )

	pad1.SetBottomMargin(0.0)
	pad1.SetTopMargin(0.1)
	# pad1.SetLeftMargin(0.12)
	pad1.SetRightMargin(0.1)

	pad2.SetBottomMargin(0.0)
	pad2.SetTopMargin(0.0)
	# pad2.SetLeftMargin(0.12)
	pad2.SetRightMargin(0.1)

	pad3.SetBottomMargin(0.0)
	pad3.SetTopMargin(0.0)
	# pad3.SetLeftMargin(0.12)
	pad3.SetRightMargin(0.1)


	pad4.SetBottomMargin(0.3)
	pad4.SetTopMargin(0.0)
	# pad4.SetLeftMargin(0.12)
	pad4.SetRightMargin(0.1)


	# pad1.SetTopMargin(0)

	# pad2.SetBottomMargin(0)
	# pad2.SetTopMargin(0)


	pad1.Draw()
	pad2.Draw()
	pad3.Draw()
	pad4.Draw()


	# pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	gStyle.SetOptStat(0)
	MadGraphStyle=[3254,21,.5,1,4]
	MadGraphSubStyle=[3254,21,.5,1,4]

	SherpaStyle=[3254+1001,26,.0000005,1,kGreen+4]

	SherpaRivetStyle=[3254,26,.0000005,1,kGreen+4]
	# SherpaRivetSubStyle=[3254,22,.9,1,2]
	SherpaRivetSubStyle=[0,26,1.0,1,kGreen+4]
	BlackHatSubStyle=[0,24,1.0,1,kBlue]

	BlackHatSubStyle_cteq=[0,24,1.0,1,kBlue]
	BlackHatSubStyle_nnpd=[0,27,1.0,1,kBlue]
	BlackHatSubStyle_mstw=[0,32,1.0,1,kBlue]

	BlackHatSubStyle_nnpd_comp=[0,25,1.0,1,kRed]
	BlackHatSubStyle_mstw_comp=[0,32,1.0,1,kBlue]

	# MadGraphRivetSubStyle=[3245,21,.9,1,4]
	MadGraphRivetSubStyle=[0,25,1.0,1,2]

	MadGraphAODSubStyle=[0,27,1.0,1,6]

	MadGraphRivetStyle=[3245,21,.5,1,4]

	DataRecoStyle=[0,20,1.0,1,1]	

	# CentralBandStyle = [3001,20,1,1,8]
	# CentralBandStyle = [3001,20,1,1,33]
	CentralBandStyle = [3004,20,1,1,1]
	# CentralBandStyle = [1001,20,0.00001,1,3]

	
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

	rivetlabel=label	
	
	nzm = []
	for __m in measurement:
		if __m > 0.000001:
			# print len(nzm)
			if 'preexc' in filename and len(nzm) >= 6:
				continue
			nzm.append(__m) 
			# print nzm

	Max = max(nzm)*3.5
	Min = min(nzm)*.7
	# print Min

	tlatalign = 0.20

	units = ''
	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		undervar ="var"
		units = '[uu/uu]'
		if "Pt" in filename:
			undervar = "p_{T}"
			units = '[pb/GeV]'
			Min = 0.007*Min
		if 'Eta' in filename:
			undervar = '|#eta|'
			units = '[pb]'
			Max *= 1.11
			Min = Min/1.5
			# tlatalign = 0.45
		if 'HT' in filename:
			undervar = "H_{T}"	
			units = '[pb/GeV]'
			Min = 0.02*Min

		if "Delta" in filename:
			undervar = "#Delta#phi"	
			units = '[pb]'
			Max *= 2.0
			Min = Min/1.6
			tlatalign = 0.55
		label0 = label
		injet = 1
		for posj in [1,2,3,4]:
			if 'jet'+str(posj) in filename or 'inc'+str(posj) in filename:
				injet = posj
		label = [label, 'd#sigma(W(#rightarrowl#nu)+#geq '+str(injet)+' jet)/d'+undervar+' '+units]


		if "Count" in filename:
			charequiv = '+'
			if 'pre' in filename:
				charequiv = '+#geq'
			label = ['N_{jet}', '#sigma(W(#rightarrowl#nu)'+charequiv+' N_{jet}) [pb]']
			units = '[pb]'
			Min = Min/3.0

		Max=Max/normalization
		Min=Min/normalization

	# print "MIN", Min	

	print 'HERE 1'
	# MadGraph AOD Quick
	name = expectation_names[0]
	mean_value = expectation_means[0]
	plus_errors = expectation_errors[0]
	minus_errors = expectation_errors[0]
	style=MadGraphAODSubStyle
	[Exp,Exp_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")


	arange = Exp_verbose[-1][-1]-Exp_verbose[-1][0]
	allbins = Exp_verbose[-1]
	minbin = 9999999
	for ibin in range(len(allbins)-1):
		dbin = allbins[ibin+1] - allbins[ibin] 
		dbin = abs(dbin)
		if dbin<minbin:
			minbin=dbin

	neffbins = int(round(float(arange)/float(minbin)))
	opt_n1 = neffbins
	opt_n2 = 0
	opt_n3 = 0
	opt_ndiv = 100*opt_n1+10*opt_n2+1*opt_n3

	# print arange
	# sys.exit()

	for nn in range(6):
		nn+=2
		if 'pfjet'+str(nn) in standardname:
			sel+='j'+str(nn-1)
	
	# Get Measured Histo
	name="Measured"
	mean_value = measurement
	plus_errors=measurement_error_up
	minus_errors=measurement_error_down
	style=DataRecoStyle
	[Meas,Meas_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
	ndataunf = sum(Meas_verbose[0])

	if 'preexc' in filename:
		# print "ABRIDGING LISTS"
		Meas_verbose = AbridgeHistoList(Meas_verbose,6)
		Exp_verbose = AbridgeHistoList(Exp_verbose,6)
		# Get Measured Histo
		name="Measured"
		mean_value = measurement
		plus_errors=measurement_error_up
		minus_errors=measurement_error_down
		[Meas,Meas_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
		# Min = 0.1*min(mean_value)
		# MadGraph AOD Quick
		name = expectation_names[0]
		mean_value = expectation_means[0]
		plus_errors = expectation_errors[0]
		minus_errors = expectation_errors[0]
		[Exp,Exp_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")



	Exp.SetMaximum(Max)
	Exp.SetMinimum(Min)


	rivetsel = '(evweight)*(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)*(ptjet1>30)'

	if 'jet1' in standardname or 'inc1' in standardname:
		rivetsel += '*(ptjet1>30)'
	if 'jet2' in standardname or 'inc2' in standardname:
		rivetsel += '*(ptjet2>30)'
	if 'jet3' in standardname or 'inc3' in standardname:
		rivetsel += '*(ptjet3>30)'
	if 'jet4' in standardname or 'inc4' in standardname:
		rivetsel += '*(ptjet4>30)'

	if 'inc' in rivetname:
		standardname = 'ht_jet'+rivetname.split('_inc')[1]
		rivetname = rivetname.split('_inc')[0]

	# print 'ME:',Meas_verbose, [len(aa) for aa in Meas_verbose]

	# print rivetsel

	aodsel = str(rivetsel)
	aodname = str(rivetname)
	for x in RivetGenBareBranchMap:
		aodsel = aodsel.replace(x[1],x[0])
		aodname = aodname.replace(x[1],x[0])

	# print aodsel
	# print aodname



	# AOD Histo
	# [[AOD_MadGraph_Result,AOD_MadGraph_Result_verbose], aodrescale] = RivetHisto(NormalDirectory+'/WJets_MG.root',aodname,binning,aodsel,rivetlabel,MadGraphAODSubStyle,4955.0*31314.0,normalization,1.0,quantity,WRenormalization)

	# sys.exit()
	# Get Rivet Histos
	print 'HERE 2'

	[[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)
	[[Rivet_MadGraphNonHad_Result,Rivet_MadGraphNonHad_Result_verbose], rivetrescalenonhad] = RivetHisto(RIVETMadGraphNonHad,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)

	# HadRatioPlot(Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,rivetlabel,binning,filename)
	[[Rivet_Sherpa_Result,Rivet_Sherpa_Result_verbose], sherparescale]    = RivetHisto(RIVETSherpa,  rivetname,binning,rivetsel,rivetlabel,  SherpaRivetSubStyle,sherpa_NOriginal  ,normalization,ndataunf,quantity,WRenormalization)
	print 'HERE 3'

	[[Blackhat_Result,Blackhat_Result_verbose], blackhatrescale]    =                      BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_CT10_r1.0_f1.0_m0')
	[[Blackhat_Result_nocorr,Blackhat_Result_verbose_nocorr], blackhatrescale_nocorr]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraph_Result_verbose,True,afsdir+'MergedHistos/hists_CT10_r1.0_f1.0_m0')

	[Blackhat_Result_hadwindow,Blackhat_Result_verbose_hadwindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_nocorr],"BlackhatHadCorr",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	


	[[Blackhat_Result_sup,Blackhat_Result_verbose_sup], blackhatrescale_sup]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_CT10_r2.0_f2.0_m0')
	[[Blackhat_Result_sdown,Blackhat_Result_verbose_sdown], blackhatrescale_sdown]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_CT10_r0.5_f0.5_m0')

	[[Blackhat_Result_mstw,Blackhat_Result_verbose_mstw], blackhatrescale_mstw]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_MSTW2008nlo68cl_r1.0_f1.0_m0')
	[[Blackhat_Result_nnpdf,Blackhat_Result_verbose_nnpdf], blackhatrescale_nnpdf]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_NNPDF21_100_r1.0_f1.0_m0')


	CT10Histos = []
	MSTWHistos = []
	NNPDHistos = []
	print 'HERE 4'


	print ' -------------- PDF WINDOWS -----------------'
	for nn in range(200):
		# print ' --> ',nn
		snn = str(nn)
		if nn <=52:
			print '  CT'
			_CT = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_CT10_r1.0_f1.0_m'+snn)[0][1]
			if _CT!=None:
				CT10Histos.append( _CT )
		if nn <=40:
			print '  MS'
			_MS = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_MSTW2008nlo68cl_r1.0_f1.0_m'+snn)[0][1]	
			if _MS!=None:
				MSTWHistos.append( _MS )
		if nn <=99:
			print '  NN', nn
			_NN = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,afsdir+'MergedHistos/hists_NNPDF21_100_r1.0_f1.0_m'+snn)[0][1]
			if _NN != None:
				NNPDHistos.append( _NN  )

	print ' -------------- Gather windows -----------------'


	print ' ------- CT10'
	[Blackhat_Result_ct10window,Blackhat_Result_verbose_ct10window] = CreateWindowFromVerbse(CT10Histos,"Blackhatct10window",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	iii = 0
	for c in CT10Histos:
		print c[0],iii
		iii+=1
	print 'WC:',Blackhat_Result_verbose_ct10window[0]
	print 'WU:',Blackhat_Result_verbose_ct10window[1]
	print 'WD:',Blackhat_Result_verbose_ct10window[2]

	print ' ------- MSTW'
	[Blackhat_Result_mstwwindow,Blackhat_Result_verbose_mstwwindow] = CreateWindowFromVerbse([CT10Histos[0]]+MSTWHistos,"Blackhatmstwwindow",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	iiii=0
	for c in MSTWHistos:
		print c[0],iiii
		iiii+=1
	print 'WC:',Blackhat_Result_verbose_mstwwindow[0]
	print 'WU:',Blackhat_Result_verbose_mstwwindow[1]
	print 'WD:',Blackhat_Result_verbose_mstwwindow[2]

	print ' ------- NNPD'
	[Blackhat_Result_nnpdwindow,Blackhat_Result_verbose_nnpdwindow] = CreateWindowFromVerbse([CT10Histos[0]]+NNPDHistos,"Blackhatnnpdwindow",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	ii = 0
	for c in NNPDHistos:
		print c[0], ii
		ii += 1

	print 'WC:',Blackhat_Result_verbose_nnpdwindow[0]
	print 'WU:',Blackhat_Result_verbose_nnpdwindow[1]
	print 'WD:',Blackhat_Result_verbose_nnpdwindow[2]		

	print ' ------- SCALE'


	print Blackhat_Result_verbose_sup
	print Blackhat_Result_verbose_sdown



	print ' ------- MSTW --- CentralMod'
	[Blackhat_Result_mstwcentwindow,Blackhat_Result_verbose_mstwcentwindow] = CreateWindowFromVerbse(MSTWHistos,"Blackhatmstwcentwindow",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	print ' ------- NNPD --- CentralMod'
	[Blackhat_Result_nnpdcentwindow,Blackhat_Result_verbose_nnpdcentwindow] = CreateWindowFromVerbse(NNPDHistos,"Blackhatnnpdcentwindow",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	


	print ' -------------- PDF WINDOWS DONE -----------------'
	# [[Blackhat_Result_cteq6,Blackhat_Result_verbose_cteq6], blackhatrescale_cteq6]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_cteq6m_r1.0_f1.0')

	[Blackhat_Result_scalewindow,Blackhat_Result_verbose_scalewindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_sup,Blackhat_Result_verbose_sdown],"BlackhatScale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	


	print ' ====================== OLD PDF METHOD =========================='
	[Blackhat_Result_pdf,Blackhat_Result_verbose_pdf] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_mstw, Blackhat_Result_verbose_nnpdf],"BlackhatPDF",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	

	print ' ====================== NEW PDF METHOD =========================='

	[Blackhat_Result_pdfV2,Blackhat_Result_verbose_pdfV2] = CreateWindowFromVerbseWindows([Blackhat_Result_verbose, Blackhat_Result_verbose_ct10window, Blackhat_Result_verbose_mstwwindow, Blackhat_Result_verbose_nnpdwindow],"BlackhatPDFV2",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	print ' ====================== BHOnly MultiPDF =========================='

	[Blackhat_Result_pdfV2_cteq,Blackhat_Result_verbose_pdfV2_cteq] = CreateWindowFromVerbseWindows([Blackhat_Result_verbose, Blackhat_Result_verbose_ct10window],"BlackhatPDFV2_cteq",rivetlabel,BlackHatSubStyle_cteq,normalization,"TopPlot",False)	
	[Blackhat_Result_pdfV2_mstw,Blackhat_Result_verbose_pdfV2_mstw] = CreateWindowFromVerbseWindows([Blackhat_Result_verbose_mstw, Blackhat_Result_verbose_mstwwindow],"BlackhatPDFV2_mstw",rivetlabel,BlackHatSubStyle_mstw,normalization,"TopPlot",False)	
	[Blackhat_Result_pdfV2_nnpd,Blackhat_Result_verbose_pdfV2_nnpd] = CreateWindowFromVerbseWindows([Blackhat_Result_verbose_nnpdf, Blackhat_Result_verbose_nnpdwindow],"BlackhatPDFV2_nnpd",rivetlabel,BlackHatSubStyle_nnpd,normalization,"TopPlot",False)	


	for v in [Blackhat_Result_verbose, Blackhat_Result_verbose_ct10window, Blackhat_Result_verbose_mstwwindow, Blackhat_Result_verbose_nnpdwindow]:
		print 'VC:',v[0]
		print 'VU:',v[1]
		print 'VD:',v[2]

	if False:
		print ' ====================== Defaulting to non-PDF4LHC Method =========================='		
		[Blackhat_Result_pdfV2,Blackhat_Result_verbose_pdfV2] = [Blackhat_Result_pdf,Blackhat_Result_verbose_pdf]

	# Removing window of hadronization correction
	# [Blackhat_Result_basic,Blackhat_Result_verbose_basic] = MergeErrorsFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_pdf, Blackhat_Result_verbose_hadwindow],"BlackhatBasic",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	
	[Blackhat_Result_basic,Blackhat_Result_verbose_basic] = MergeErrorsFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_pdfV2],"BlackhatBasic",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	[Blackhat_Result_basicplusscale,Blackhat_Result_verbose_basicplusscale] = MergeErrorsFromVerbse([Blackhat_Result_verbose_basic, Blackhat_Result_verbose_scalewindow],"BlackhatBasicplusscale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	


	print ' ====================== PDF COMPLETE =========================='

	# print 'BH:',Blackhat_Result_verbose_basicplusscale, [len(aa) for aa in Blackhat_Result_verbose_basicplusscale]

	# print "MADGRAPH   INT:",Rivet_MadGraph_Result.Integral()
	# print "SHERPA     INT:",Rivet_Sherpa_Result.Integral()
	# print "BLACKHAT   INT:",Blackhat_Result.Integral()
	# print Blackhat_Result_verbose

	# Storing stuff...
	fplot = TFile.Open(filename+'root',"RECREATE")

	# Meas.GetYaxis().SetTitleFont(42);
	Meas.GetXaxis().SetTitleSize(.25);
	Meas.GetXaxis().SetTitleOffset(1.);

	# Meas.GetYaxis().SetTitleSize(0.5*Meas.GetYaxis().GetTitleSize());
	# Meas.GetYaxis().SetTitleSize(.14);
	# Meas.GetXaxis().CenterTitle(0);
	# Meas.GetYaxis().CenterTitle(1);
	# Meas.GetYaxis().SetTitle("")
	Meas.GetXaxis().SetTitle("")

	Meas.Write("Meas")
	# Exp.Write("Exp")
	fplot.Close()

	flog = open(filename+'_TGraphContent.txt','w')
	flog.write('\n,Meas_verbose = '+str(Meas_verbose)+'\n')
	# flog.write('\n,Exp_verbose = '+str(Exp_verbose)+'\n')
	flog.close()

	# print '----  TABLE: ',rivetname
	# print Rivet_MadGraph_Result_verbose
	# print Meas_verbose
	# print ' ------ '
	# Draw Two Rivet Histos and one Measured Histo
	Meas.SetMaximum(Max)
	Meas.SetMinimum(Min)
	Rivet_MadGraph_Result.SetMaximum(Max)
	Rivet_MadGraph_Result.SetMinimum(Min)
	
	# AOD_MadGraph_Result.SetMaximum(Max)
	# AOD_MadGraph_Result.SetMinimum(Min)	

	Rivet_Sherpa_Result.SetMaximum(Max)
	Rivet_Sherpa_Result.SetMinimum(Min)		
	# print 'USING MIN',Min
	Blackhat_Result_basicplusscale.SetMinimum(Min)		
	Blackhat_Result_basicplusscale.SetMaximum(Max)		


	print ' --------------------------------------- '
	print label[0]
	print ' '
	print 'Measured:',Meas_verbose
	print 'Blackhat:',Blackhat_Result_verbose_basicplusscale
	print 'Sherpa:',Rivet_Sherpa_Result_verbose
	print 'Madgraph:',Rivet_MadGraph_Result_verbose
	print ' '
	print filename+'_papertable.tex'
	print ' '
	def verbose_to_string(_verbose):
		_output = []
		if normalization>0:
			_normalization = normalization
		else:
			_normalization = 1.0
		for v in range(len(_verbose[0])):
			if '30Count' not in filename:
				_bin = str(round(float(_verbose[-1][v]),6)) +' $-$ ' +str(round(float(_verbose[-1][v+1]),6) )
			else:
				if 'pre' not in filename:
					_bin = str( int(  round( 0.5*float(_verbose[-1][v]) + 0.5*float(_verbose[-1][v+1])  )) )			
				else:
					_bin = ' $\\geq$'+str( int(round( 0.5*float(_verbose[-1][v]) + 0.5*float(_verbose[-1][v+1])  )) )			
			_mean = str(round(_verbose[0][v]/_normalization,6))
			_errp = str(round(_verbose[1][v]/_normalization,6))
			_errm = str(round(_verbose[2][v]/_normalization,6))
			_output.append([_bin,_mean,_errp,_errm])
		return _output
	def check_compatibility(_verbose_sets):
		_binsets = []
		for v in _verbose_sets:
			_binsets.append(v[-1])
		for _b in range(len(_binsets)-1):
			if _binsets[_b] != _binsets[_b+1]:
				print 'Compatibility error!'
				print _binsets[_b]
				print _binsets[_b+1]
				sys.exit()

	check_compatibility([Meas_verbose,Blackhat_Result_verbose_basicplusscale,Rivet_Sherpa_Result_verbose,Rivet_MadGraph_Result_verbose])
	check_compatibility([Meas_verbose,Blackhat_Result_verbose_pdfV2_cteq,Rivet_Sherpa_Result_verbose,Rivet_MadGraph_Result_verbose])
	check_compatibility([Meas_verbose,Blackhat_Result_verbose_pdfV2_mstw,Rivet_Sherpa_Result_verbose,Rivet_MadGraph_Result_verbose])
	check_compatibility([Meas_verbose,Blackhat_Result_verbose_pdfV2_nnpd,Rivet_Sherpa_Result_verbose,Rivet_MadGraph_Result_verbose])

	__D = verbose_to_string(Meas_verbose)
	__B = verbose_to_string(Blackhat_Result_verbose_basicplusscale)
	__S = verbose_to_string(Rivet_Sherpa_Result_verbose)
	__M = verbose_to_string(Rivet_MadGraph_Result_verbose)



	vmap = []
	vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
	vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
	vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
	vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
	vmap.append(["Eta_pfjet1","$|\\eta(jet_1)|$"])
	vmap.append(["Eta_pfjet2","$|\\eta(jet_2)|$"])
	vmap.append(["Eta_pfjet3","$|\\eta(jet_3)|$"])
	vmap.append(["Eta_pfjet4","$|\\eta(jet_4)|$"])
	vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
	vmap.append(["PFJet30Count","Exc Jet Mult"])
	vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
	vmap.append(["Pt_MET","$E_T^{miss}$"])
	vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
	vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
	vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
	vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
	vmap.append(["Pt_muon1","$p_T(\\mu)$"])
	vmap.append(["Eta_muon1","$\eta(\\mu)$"])
	vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
	vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
	vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
	vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

	var = 'Bin'
	for v in vmap:
		if v[0] in str(filename):
			var = v[1]



	_table = ['\\begin{table}[htb]']
	_table.append('\\caption{Bin-by-bin data and uncertainties for the final '+var+' distribution. Uncertainties on the Blackhat+Sherpa predictions contain PDF and factorization/renormalization scale uncertainty.}')
	_table.append('\\begin{center}')
	_table.append('\\begin{tabular}{|l|l|lll|}\\hline')

	rawunits = ' '
	if 'GeV' in units:
		rawunits = '[GeV]'
	_table.append(var +' & Measurement & Blackhat+Sherpa  & Sherpa  & MadGraph+Pythia  \\\\ \\relax ')
	_table.append(rawunits +' & '+units+' & '+units+' & '+units+' &  '+units+' \\\\ \\hline')

	for x in range(len(__D)):
		__d = __D[x]
		# print '\n'
		# print __d
		# sys.exit()
		__b = __B[x]
		__s = __S[x]
		__m = __M[x]
		aline = __d[0]
		aline += ' & '+BeautifiedEntry([__d[1] ,__d[2],__d[3]])
		aline += ' & '+BeautifiedEntry([__b[1] ,__b[2],__b[3]])		
		aline += ' & '+BeautifiedEntry([__s[1] ,__s[2],__s[3]])
		aline += ' & '+BeautifiedEntry([__m[1] ,__m[2],__m[3]])
		aline += ' \\\\ '
		_table.append(aline)
	_table.append('\\hline')
	_table.append('\\end{tabular}')
	_table.append('\\end{center}')
	_table.append( ('\\label{tab:'+filename+'}').replace('.','').replace('/','__') )	
	_table.append('\\end{table}')
	_table.append('')
	__tab = open(filename+'_papertable.tex','w')
	for tline in _table:
		# print tline
		__tab.write(tline+'\n')
	__tab.close()

	# print ' '
	# print ' --------------------------------------- '
	# sys.exit()

	XRANGE = [Meas_verbose[-1][0],Meas_verbose[-1][-1]]
	Meas.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	

	# Meas.SetMarkerSize(0.0001)
	# Meas.SetLineColor(1)
	Meas.GetXaxis().SetNdivisions(110)
	Meas.SetMarkerColor(1)
	Meas.Draw("A2")
	Meas.Draw("PX")

	# Meas.GetYaxis().SetTitle(" func test ")
	Meas.GetYaxis().SetTitleOffset(1.0);
	Meas.GetYaxis().SetTitleSize(.06);
	Meas.GetYaxis().SetLabelSize(.06);

	Meas.GetXaxis().SetTitleOffset(1.1);
	Meas.GetXaxis().SetTitleSize(.05);
	Meas.GetXaxis().SetLabelSize(.00);

	Rivet_MadGraph_Result.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	
	Rivet_Sherpa_Result.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	
	Blackhat_Result_basicplusscale.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	
	Blackhat_Result_pdfV2_cteq.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])
	Blackhat_Result_pdfV2_mstw.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])
	Blackhat_Result_pdfV2_nnpd.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])

	if dobhonly == False:
		Rivet_MadGraph_Result.Draw("P")
		# AOD_MadGraph_Result.Draw("P")
		Rivet_Sherpa_Result.Draw("P")
		Blackhat_Result_basicplusscale.Draw("P")
	else:
		Blackhat_Result_pdfV2_cteq.Draw("P")
		Blackhat_Result_pdfV2_mstw.Draw("P")
		Blackhat_Result_pdfV2_nnpd.Draw("P")

	# print 'MEAS:',Meas_verbose[-1]
	# print 'MG:', Rivet_MadGraph_Result_verbose[-1]
	# print 'Sherpa', Rivet_Sherpa_Result_verbose[-1]
	# print 'BH:', Blackhat_Result_verbose_basicplusscale[-1]
	# Blackhat_Result_basicplusscale.Draw("2")

	# Blackhat_Result_basic.Draw("||")

	# gPad.Update()
	Blackhat_Result_mstw.SetLineStyle(2)
	Blackhat_Result_nnpdf.SetLineStyle(2)

	# Blackhat_Result_mstw.Draw("L")
	# Blackhat_Result_cteq6.Draw("L")
	# Exp.Draw("P")

	Rivet_MadGraph_Result_L=Rivet_MadGraph_Result.Clone()
	Rivet_Sherpa_Result_L=Rivet_Sherpa_Result.Clone()
	Blackhat_Result_L=Blackhat_Result.Clone()

	Blackhat_Result_cteq_L=Blackhat_Result_pdfV2_cteq.Clone()
	Blackhat_Result_mstw_L=Blackhat_Result_pdfV2_mstw.Clone()
	Blackhat_Result_nnpd_L=Blackhat_Result_pdfV2_nnpd.Clone()


	Rivet_MadGraph_Result_L.SetFillColor(kOrange-3)
	Rivet_Sherpa_Result_L.SetFillColor(kGreen-8)
	Blackhat_Result_L.SetFillColor(kBlue-10)

	Blackhat_Result_cteq_L.SetFillColor(kBlue-10)
	Blackhat_Result_mstw_L.SetFillColor(kBlue-10)
	Blackhat_Result_nnpd_L.SetFillColor(kBlue-10)


	Rivet_MadGraph_Result_L.SetFillStyle(1001)
	Rivet_Sherpa_Result_L.SetFillStyle(1001)
	Blackhat_Result_L.SetFillStyle(1001)	

	Blackhat_Result_cteq_L.SetFillStyle(1001)	
	Blackhat_Result_mstw_L.SetFillStyle(1001)	
	Blackhat_Result_nnpd_L.SetFillStyle(1001)	

	if dobhonly == False:
		# leg = TLegend(0.42,0.75,1.0,1.00,"","brNDC")
		leg = TLegend(0.52,0.75,1.0,1.00,"","brNDC")

	else:
		leg = TLegend(0.5,0.64,0.99,0.89,"","brNDC")

	leg.SetTextFont(42)
	leg.SetFillColor(0)
	leg.SetFillColor(1001)
	leg.SetBorderSize(0)
	leg.SetTextSize(.055)
	leg.SetBorderSize(1)
	# leg.SetHeader("W #rightarrow #mu#nu + jets");	
	leg.AddEntry(Meas,"Unfolded Data");
	# leg.AddEntry(AOD_MadGraph_Result,"MadGraph AOD")
	# leg.AddEntry(Exp,"MadGraph AOD");
	if dobhonly == False:
		leg.AddEntry(Blackhat_Result_L,"BlackHat+Sherpa (NLO)")
		leg.AddEntry(Rivet_Sherpa_Result_L,"Sherpa (LO+PS)")
		leg.AddEntry(Rivet_MadGraph_Result_L,"MadGraph+Pythia (LO+PS)")
	else:
		leg.AddEntry(Blackhat_Result_cteq_L,"BlackHat+Sherpa (CT10)")
		leg.AddEntry(Blackhat_Result_mstw_L,"BlackHat+Sherpa (MSTW)")
		leg.AddEntry(Blackhat_Result_nnpd_L,"BlackHat+Sherpa (NNPDF)")

	leg.Draw()




	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	# l1.DrawLatex(0.15,0.90,"CMS Preliminary                         "+sqrts+"                        L_{int} = 5.0 fb^{-1}")
	# l1.DrawLatex(0.4,0.78,"CMS ")
	l1.DrawLatex(0.15,0.94,"CMS, "+sqrts+", L_{int}= 5.0 fb^{-1}")

	# Labels
	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(42)
	l2.SetNDC()
	l2.SetTextSize(0.05)
	# l2.SetTextAngle(45);	
	# l2.DrawLatex(0.64,0.60,"PRELIMINARY")
	if False:
		# l2.DrawLatex(0.6,0.50,"R_{Rivet} = "+ str(round(rivetrescale,3)))
		l2.DrawLatex(0.64,0.65,"Data/MadGraph = "+ str(round(rivetrescale,3)))
		l2.DrawLatex(0.64,0.57,"Data/Sherpa   = "+ str(round(sherparescale,3)))


	l3=TLatex()
	l3.SetTextAlign(12)
	l3.SetTextFont(42)
	l3.SetNDC()
	l3.SetTextSize(0.06)
	l3.DrawLatex(tlatalign,0.23,"anti-k_{T} (R = 0.5) Jets")
	l3.DrawLatex(tlatalign,0.15,"p_{T}^{jet}>30 GeV, |#eta^{jet}|<2.4")
	l3.DrawLatex(tlatalign,0.07,"W#rightarrow#mu#nu channel")


	############################
	### GO TO SUBPLOT        ###
	############################
	pad4.cd()
	# pad2.SetGridy()
	pad4.Draw()

	[cent1,[cent2up,cent2down]] = CentralRatioBand(Meas_verbose, CentralBandStyle)
	cent1.GetXaxis().SetNdivisions(110)
	cent1.GetYaxis().SetNdivisions(505)




	[grat2,[grat2up,grat2down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_Sherpa_Result_verbose,SherpaRivetSubStyle)
	unity=TLine(XRANGE[0], 1.0 , XRANGE[-1],1.0)
	unity.SetLineStyle(7)

	# print 'Dividing Meas/MG RIVET'
	[grat3,[grat3up,grat3down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)
	# [grat3aod,[grat3upaod,grat3downaod]] = DivideTGraphsFlatRel(Meas_verbose,AOD_MadGraph_Result_verbose,MadGraphAODSubStyle)

	print '~~~~~~~~~~~~~~ BLACKHAT SUB PLOT ~~~~~~~~~~~~'
	[grat4,[grat4up,grat4down]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_basicplusscale,BlackHatSubStyle)

	[grat4_cteq,[grat4up_cteq,grat4down_cteq]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_pdfV2_cteq,BlackHatSubStyle_cteq)
	[grat4_mstw,[grat4up_mstw,grat4down_mstw]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_pdfV2_mstw,BlackHatSubStyle_mstw)
	[grat4_nnpd,[grat4up_nnpd,grat4down_nnpd]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_pdfV2_nnpd,BlackHatSubStyle_nnpd)

	## Get the blackhat ratio plots

	grat4window = grat4.Clone()
	grat4window.SetFillColor(kBlue-10)
	grat4window.SetFillStyle(1001)

	grat4window_cteq = grat4_cteq.Clone()
	grat4window_cteq.SetFillColor(kBlue-10)
	grat4window_cteq.SetFillStyle(1001)

	grat4window_mstw = grat4_mstw.Clone()
	grat4window_mstw.SetFillColor(kBlue-10)
	grat4window_mstw.SetFillStyle(1001)

	grat4window_nnpd = grat4_nnpd.Clone()
	grat4window_nnpd.SetFillColor(kBlue-10)
	grat4window_nnpd.SetFillStyle(1001)	

	print '~~~~~~~~~~~~~~ BLACKHAT SUB PLOT ~~~~~~~~~~~~'

	# print Meas_verbose
	# print XRANGE
	# sys.exit()

	## Get the blackhat ratio plots


	# Get axis range
	# if cent2up > 1.5 or cent2down < 0.5:
	# 	grat2down = 0.2
	# 	grat2up = 0.8	

	# if grat2up > 1.5 or grat2down < 0.5:
	# 	grat2down = -.24
	# 	grat2up = 2.24	

	# if grat3up > 1.5 or grat3down < 0.5:
	# 	grat2down = -.24
	# 	grat2up = 2.24	

	# if grat4up > 1.5 or grat4down < 0.5:
	# 	grat2down = -.24
	# 	grat2up = 2.24			
	
	grat2down = 0.20
	grat2up = 1.80



	cent1.SetMaximum(grat2up)
	cent1.SetMinimum(grat2down)
	cent1.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	
	cent1.GetYaxis().CenterTitle()
	cent1.GetXaxis().SetTitle(label[0])
	cent1.GetYaxis().SetTitle("MC/Data")
	cent1.GetYaxis().SetTitleSize(0.16)
	cent1.GetXaxis().SetTitleOffset(1.2);
	cent1.GetYaxis().SetTitleOffset(.4);
	cent1.GetYaxis().SetLabelSize(0.14)



	cent1.GetYaxis().SetTitleFont(42);
	cent1bh = cent1.Clone()
	cent1bh.GetYaxis().SetTitle("NLO/Data")
	cent1bh.GetXaxis().SetTitleOffset(1.1);
	cent1bh.GetYaxis().SetTitleOffset(.4);

	cent1bh.GetYaxis().SetTitleFont(42);

	cent1lower = cent1.Clone()
	cent1lower.GetXaxis().SetTitleOffset(0.9);
	cent1lower.GetYaxis().SetTitleSize(0.115)

	cent1lower.GetYaxis().SetTitleOffset(0.56);

	cent1lower.GetYaxis().SetTitleFont(42);
	cent1lower.GetYaxis().SetLabelSize(0.10)

	# print Meas_verbose
	modbinning = Meas_verbose[-1]
	# sys.exit()
	cent1lowerh= TH1D('cent1lowerh','cent1lowerh',len(modbinning)-1,array('d',modbinning))
	for pbin in range(cent1lowerh.GetNbinsX()):
		cent1lowerh.GetXaxis().SetBinLabel(pbin+1,'#geq '+str(pbin+1))
		blab = cent1lowerh.GetXaxis().GetBinLabel(pbin+1)
		print pbin,blab



	# sys.exit()
		# newblab = '#geq'+str(blab)
		# cent1lower.GetHistogram().GetXaxis().SetBinLabel(pbin,newblab)
		# if pbin>3:
		# 	break
		# l2timevschain->GetHistogram()->GetXaxis()->SetBinLabel(k+1,names[k].c_str())
	# sys.exit()
	# lowersize = 0.16*(float(pad4.GetWh()*pad4.GetAbsHNDC()))/float((pad3.GetWh()*pad3.GetAbsHNDC()))
	# lowersize = 0.16*(float(pad4.GetAbsHNDC()))/(float(pad3.GetAbsHNDC()))

	# cent1lower.GetYaxis().SetTitleSize(0.115)
	# cent1lower.GetYaxis().SetTitleSize(lowersize)
	# print "LOWERSIZE",lowersize
	# sys.exit()

	################################################################################################
	## FOR THIRD SUBPLOT
	grat2.SetMinimum(grat2down)
	grat2.SetMaximum(grat2up)
	grat3.SetMinimum(grat2down)
	grat3.SetMaximum(grat2up)


	cent1lowerh.SetMaximum(grat2up)
	cent1lowerh.SetMinimum(grat2down)
	cent1lowerh.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])                    	
	cent1lowerh.GetYaxis().CenterTitle()
	cent1lowerh.GetXaxis().SetTitle(label[0])
	cent1lowerh.GetYaxis().SetTitle("MC/Data")
	cent1lowerh.GetYaxis().SetTitleSize(0.16)
	cent1lowerh.GetYaxis().SetTitleOffset(.4);
	cent1lowerh.GetYaxis().SetLabelSize(0.1)
	cent1lowerh.GetYaxis().SetTitleSize(0.115)
	cent1lowerh.GetYaxis().SetTitleOffset(0.56);
	cent1lowerh.GetYaxis().SetTitleFont(42);
	# cent1lowerh.GetYaxis().SetLabelSize(0.20)
	cent1lowerh.GetYaxis().SetNdivisions(505)
	cent1lowerh.GetXaxis().SetNdivisions(110)

	cent1lowerh.GetXaxis().SetTitleOffset(0.9);
	cent1lowerh.GetXaxis().SetTitleSize(0.13);
	cent1lowerh.GetXaxis().SetLabelSize(0.13);


	grat2.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])          
	grat3.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])          

	cent1lowerh.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])          
	cent1lowerh.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])        

	grat3window = grat3.Clone()

	grat3window.SetFillColor(kOrange-2)
	grat3window.SetFillStyle(1001)


	if dobhonly == False:
		if 'preexc' in filename:
			cent1lowerh.Draw("")
		else:
			cent1lower.Draw("A2")

		grat3window.Draw("2")
		grat3.Draw("p")
		cent1lower.Draw("2")
		unity.Draw("SAME")
		lb2=TLatex()
		lb2.SetTextAlign(12)
		lb2.SetTextFont(42)
		lb2.SetNDC()
		lb2.SetTextSize(0.08)
		lb2.DrawLatex(0.20,0.38,"MadGraph+Pythia (LO+PS), normalized to #sigma_{NNLO}")
	else:
		cent1bh.Draw("A2")

		grat4window_nnpd.GetYaxis().SetTitle("NLO/Data")
		grat4_nnpd.GetYaxis().SetTitle("NLO/Data")
		grat4window_nnpd.Draw("2")
		grat4_nnpd.Draw("p")
		cent1bh.Draw("2")
		unity.Draw("SAME")

		lb2=TLatex()
		lb2.SetTextAlign(12)
		lb2.SetTextFont(42)
		lb2.SetNDC()
		lb2.SetTextSize(0.08)
		lb2.DrawLatex(0.20,0.38,"Blackhat+Sherpa (#leq 4 jets NLO, NNPDF with PDF Unc.)")	# Stamp on top

	pad4.RedrawAxis()

	################################################################################################
	## FOR SECOND SUBPLOT

	pad3.cd()

	grat2window = grat2.Clone()

	grat2window.SetFillColor(kGreen-8)
	grat2window.SetFillStyle(1001)

	if dobhonly == False:
		cent1.Draw("A2")

		grat2window.Draw("2")
		grat2.Draw("p")
		cent1.Draw("2")
		unity.Draw("SAME")


		lb3=TLatex()
		lb3.SetTextAlign(12)
		lb3.SetTextFont(42)
		lb3.SetNDC()
		lb3.SetTextSize(0.11)
		lb3.DrawLatex(0.20,0.13,"Sherpa (LO+PS), normalized to #sigma_{NNLO}")

	else:
		cent1bh.Draw("A2")

		grat4window_mstw.GetYaxis().SetTitle("NLO/Data")
		grat4_mstw.GetYaxis().SetTitle("NLO/Data")

		grat4window_mstw.Draw("2")
		grat4_mstw.Draw("p")
		cent1bh.Draw("2")
		unity.Draw("SAME")

		lb3=TLatex()
		lb3.SetTextAlign(12)
		lb3.SetTextFont(42)
		lb3.SetNDC()
		lb3.SetTextSize(0.11)
		lb3.DrawLatex(0.20,0.13,"Blackhat+Sherpa (#leq 4 jets NLO, MSTW with PDF unc.)")

	pad3.RedrawAxis()


	################################################################################################
	## FOR FIRST SUBPLOT
	pad2.cd()


	if dobhonly == False:
		cent1bh.Draw("A2")
		grat4window_mstw.GetYaxis().SetTitle("NLO/Data")
		grat4_mstw.GetYaxis().SetTitle("NLO/Data")
		grat4window.Draw("2")
		grat4.Draw("p")
		cent1bh.Draw("2")
		unity.Draw("SAME")

		lb4=TLatex()
		lb4.SetTextAlign(12)
		lb4.SetTextFont(42)
		lb4.SetNDC()
		lb4.SetTextSize(0.11)
		lb4.DrawLatex(0.20,0.13,"Blackhat+Sherpa (#leq 4 jets NLO, with PDF and ren./fac. scale unc.)")
	else:
		cent1bh.Draw("A2")

		grat4window_cteq.GetYaxis().SetTitle("NLO/Data")
		grat4_cteq.GetYaxis().SetTitle("NLO/Data")		
		grat4window_cteq.Draw("2")
		grat4_cteq.Draw("p")
		cent1bh.Draw("2")
		unity.Draw("SAME")

		lb4=TLatex()
		lb4.SetTextAlign(12)
		lb4.SetTextFont(42)
		lb4.SetNDC()
		lb4.SetTextSize(0.11)
		lb4.DrawLatex(0.20,0.13,"Blackhat+Sherpa (#leq 4 jets NLO, CT10 with PDF Unc.)")


	# cent1.GetXaxis().SetTitleSize(.14);
	# cent1.GetYaxis().SetTitleSize(.14);

	# cent1bh.GetXaxis().SetTitleSize(.12);
	# cent1bh.GetYaxis().SetTitleSize(.10);	
	pad2.RedrawAxis()
	################################################################################################

	# Do Drawing
	if dobhonly == True:
		filename = filename[:-1]+'_BHMultPdf.'
	print 'Creating: ',filename+'pdf/png'
	c1.Print(filename+'pdf')
	c1.Print(filename+'png')


	if dobhonly == False:

		c2 = TCanvas("c2","",200, 100, 600, 450)

		c2pad1 = TPad( 'c2pad1', 'c2pad1', 0.01, 0.01, 0.99, 0.99 )#divide canvas into pads
		c2pad1.SetBottomMargin(0.2)
		c2pad1.SetTopMargin(0.1)
		# c2pad1.SetRightMargin(0.1)
		c2pad1.Draw()
		c2pad1.cd()

		


		[cteqband,null] = CentralRatioBand(Blackhat_Result_verbose_pdfV2_cteq,CentralBandStyle)

		if '30Count' in filename:
			XRANGE[-1] = 4.5
			cteqband.GetXaxis().SetNdivisions(106)
		else:
			cteqband.GetXaxis().SetNdivisions(110)
		unityc=TLine(XRANGE[0], 1.0 , XRANGE[-1],1.0)
		unityc.SetLineStyle(7)

		cteqband.GetXaxis().SetLimits(XRANGE[0],XRANGE[-1])
		cteqband.GetXaxis().SetTitle(cent1.GetXaxis().GetTitle())
		cteqband.GetYaxis().SetTitle("Ratio to CT10")
		cteqband.GetYaxis().SetTitleSize(0.07)
		cteqband.GetXaxis().SetTitleSize(0.07)
		cteqband.GetYaxis().SetTitleOffset(0.9)
		cteqband.GetXaxis().SetTitleOffset(0.9)
		cteqband.GetYaxis().SetLabelSize(0.05)
		cteqband.GetXaxis().SetLabelSize(0.05)
		cteqband.SetMaximum(2.0)
		cteqband.SetMinimum(0.5)
		# CentralRatioBand.GetYaxis().SetTitle("")


	# 	# [gcomp_cteq,[gcompup_cteq,gcompdown_cteq]] = DivideTGraphsFlatRel(Blackhat_Result_verbose_pdfV2_cteq,CT10Histos[0][0][1], BlackHatSubStyle_cteq)
		[gcomp_mstw,[gcompup_mstw,gcompdown_mstw]] = DivideTGraphsFlatRel(CT10Histos[0],Blackhat_Result_verbose_pdfV2_mstw, BlackHatSubStyle_mstw_comp)
		[gcomp_nnpd,[gcompup_nnpd,gcompdown_nnpd]] = DivideTGraphsFlatRel(CT10Histos[0],Blackhat_Result_verbose_pdfV2_nnpd, BlackHatSubStyle_nnpd_comp)
		# [gcomp_nnpd,[gcompup_nnpd,gcompdown_nnpd]] = DivideTGraphsFlatRel(Blackhat_Result_verbose_pdfV2_cteq,CT10Histos[0], BlackHatSubStyle_nnpd)
		[gcomp_data,[gcompup_data,gcompdown_data]] = DivideTGraphsFlatRel(CT10Histos[0],Meas_verbose, CentralBandStyle)
		gcomp_data.SetFillColor(0)
		gcomp_data.SetFillStyle(0)


	# 	gcompwindow_mstw = gcomp_mstw.Clone()
	# 	gcompwindow_mstw.SetFillColor(kBlue-10)
	# 	gcompwindow_mstw.SetFillStyle(1001)

	# 	gcompwindow_nnpd = gcomp_nnpd.Clone()
	# 	gcompwindow_nnpd.SetFillColor(kBlue-10)
	# 	gcompwindow_nnpd.SetFillStyle(1001)	


		cteqband.Draw("A2")
		gcomp_mstw.Draw("ep")
		gcomp_nnpd.Draw("ep")
		gcomp_data.Draw("ep")

		unityc.Draw("SAME")

		leg = TLegend(0.53,0.68,0.95,0.86,"","brNDC")
		# leg.AddEntry(cteqband,"Sherpa (CT10)")
		leg.AddEntry(gcomp_data,"Data")
		leg.AddEntry(gcomp_mstw,"BlackHat+Sherpa (MSTW)")
		leg.AddEntry(gcomp_nnpd,"BlackHat+Sherpa (NNPDF)")

		leg.SetTextFont(42)
		leg.SetFillColor(0)
		leg.SetFillColor(1001)
		leg.SetBorderSize(0)
		leg.SetTextSize(.04)
		leg.SetBorderSize(1)
		leg.Draw()
		compfilename = filename[:-1]+'_pdfcomparison.'
	
		l1c=TLatex()
		l1c.SetTextAlign(12)
		l1c.SetTextFont(42)
		l1c.SetNDC()
		l1c.SetTextSize(0.05)
		# l1.DrawLatex(0.15,0.90,"CMS Preliminary                         "+sqrts+"                        L_{int} = 5.0 fb^{-1}")
		l1c.DrawLatex(0.22,0.83,"CMS ")
		l1c.DrawLatex(0.16,0.94,sqrts+", L_{int} = 5.0 fb^{-1}")
		print compfilename

		c2.Print(compfilename+'pdf')
		c2.Print(compfilename+'png')



		print "X LABEL", Meas.GetXaxis().GetTitle()
		print "X LABEL", cent1.GetXaxis().GetTitle()

	gDirectory.GetList().Delete()
	# sys.exit()

def round_sigfigs(num, sig_figs):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0
def BeautifiedEntry(entry):
	# print '---------------------------------'
	# print entry
	entry = [format(float(u), '.66f') for u in entry]
	# print entry
	# print ' --------------'
	# print ' entry:',entry
	# print ' flent:',float(entry[0])
	if float(entry[0])==0.0:
		return '--'
	rentry =  [str(round_sigfigs(float(e),2)) for e in entry]

	# print rentry
	# print 'clean rentry:',rentry
	newrentry = []
	for u in rentry:
		newu = u
		if 'e' in u:
			# print rentry
			# print ' *',(u.split('e')[-1])
			# print ' **',int(u.split('e')[-1])
			dim = int(u.split('e')[-1])
			# print dim
			newu = u.split('e')[0]
			if dim<0:
				nzeros = abs(dim)-1
				newu = '0.'+'0'*nzeros+newu.replace('.','')
			if dim>0:
				nzeros = abs(dim) - len(newmu.split('.')[-1])
				newu =  newu.replace('.','') + '0'*nzeros

		newrentry.append(newu)


	# print ' !! ',newrentry
	rentry = newrentry

	# print ' zmod:',rentry

	# print rentry
	uncertainties = rentry[1:]
	# print uncertainties
	NL = 999
	NR = 0
	for u in uncertainties:
		# u = format(float(u), '.66f')

		nl = len(u.split('.')[0])
		nr = 0
		if (len(u.split('.')) > 1):
			if float('.'+u.split('.')[1]) == float(u):
				nl = 0
			nr = len(u.split('.')[1])
		if nl < NL:
			NL = nl
		if nr > NR:
			NR = nr
	rplace = 9999
	# print 'nl', NL
	if NL <rplace:
		rplace = -NL+2
	# print 'rplace', rplace
	if NL <= 0:
		rplace = 1*NR
	# print 'rplace', rplace


	decimal = 10**rplace
	# print 'd', decimal

	entry = [str(round(float(e) * 1.0*decimal) / (1.0*decimal)) for e in entry]

	# print 'sigmod:', entry

	newentry = []
	for u in entry:
		newu = u
		if 'e' in u:
			# print ' -- '
			# print entry
			# print u
			# print u.split('e')
			dim = int(u.split('e')[-1])
			# print dim
			newu = u.split('e')[0]
			if dim<0:
				nzeros = abs(dim)-1
				newu = '0.'+'0'*nzeros+newu.replace('.','')
			if dim>0:
				nzeros = abs(dim) - len(newmu.split('.')[-1])
				newu =  newu.replace('.','') + '0'*nzeros

		newentry.append(newu)
	entry = newentry

	# print 'dimmod ', entry
	outentry = []

	ap0 = True

	for e in entry:
		rhs = e.split('.')[1]
		while len(rhs) <NR:
			rhs+='0'
		e = e.split('.')[0]+'.'+rhs
		outentry.append(e)
		if e[-1] !='0' or e[-2]!='.':
			ap0 = False
		
	if ap0==True:
		outentry = [e[:-2] for e in outentry]

	# print 'outent', outentry
	outtex = ''
	if len(outentry)==3:
		if outentry[1]!=outentry[2]:
			outtex = outentry[0] +'$^{+'+outentry[1]+'}_{-'+outentry[2]+'}$'
		else:
			outtex = outentry[0] +' $\\pm$ '+outentry[1]
	elif len(outentry)==2:
		outtex = outentry[0] +' $\\pm$ '+outentry[1]
	elif len(outentry)==1:
		outtex = outentry[0]
	else:
		print ' Too many uncertaities to parse for TeX!'
		sys.exit()

	print outtex
	return outtex











def HArrayFromHlog(hlog):
	harray = []
	for line in open(hlog,'r'):
		line = line.replace(';',',')
		line = line.split(',')
		for x in range(len(line)):
			if 'ROOT' in line[x]:
				line[x] = '100'
		fline = [float(x) for x in line]
		harray.append(fline)
	harray = harray[0:-1]
	return harray

def quadsum(_list):
	ss = 0.0
	for a in _list:
		ss += a*a
	ss = math.sqrt(ss)
	return ss


def ParseTablesToRecoHistograms():
	# print 'HERE'
	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]
	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,20,1.0,1,1]
	DataCompStyle=[0,21,1.0,1,6]
	BlankRecoStyle=[0,21,.00001,1,0]
	DataUnfoldedStyle=[0,21,1,1,1]
	DataUnfoldedStyle_pseudo=[0,25,1,1,9]
	DataUnfoldedStyle_pseudoSG=[0,24,1,1,7]

	DataUnfoldedStyle_pseudo2=[0,26,1,1,2]
	DataUnfoldedStyle_pseudo2SG=[0,32,1,1,6]

	# nstart = 8
	# nint = -1
	# print nstart
	# WStackStyle=[1001,20,.00001,1,nstart+nint*5]
	# TTStackStyle=[1001,20,.00001,1,nstart+nint*4]
	# ZStackStyle=[1001,20,.00001,1,nstart+nint*3]
	# DiBosonStackStyle=[1001,20,.00001,1,nstart+nint*2]
	# StopStackStyle=[1001,20,.00001,1,nstart+nint*1]
	# QCDStackStyle=[1001,20,.00001,1,nstart+nint*0]
	# MCGenStyle=[0,20,.00001,1,2]
	# MCGenSmearStyle=[0,20,.00001,1,9]
	# MCRecoStyle=[0,21,.00001,1,4]
	# DataRecoStyle=[0,20,1.0,1,1]
	# DataCompStyle=[0,21,1.0,1,6]
	# BlankRecoStyle=[0,21,.00001,1,0]
	# DataUnfoldedStyle=[0,21,0.5,1,1]
	# DataUnfoldedStyle_pseudo=[0,20,0.5,1,9]
	# DataUnfoldedStyle_pseudo2=[0,20,0.5,1,2]




	bgbandstyle=[3253,20,.00001,0,14]
	bgbandstyle=[3004,20,.00001,0,1]

	relabels = []
	relabels.append(['Pt_pfjet1','Leading jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_muon1','Muon p_{T} [GeV]','p_{T}'])
	relabels.append(['N_GoodVertices','N_{Vertices}','N_{Vertices}'])
	relabels.append(['Pt_pfjet2','Second leading jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet3','Third leading jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet4','Fourth leading jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet5','Fifth leading jet p_{T} [GeV]','p_{T}'])



	relabels.append(['Eta_pfjet1','Leading jet |#eta|','|#eta|'])
	relabels.append(['Eta_pfjet2','Second leading jet |#eta|','|#eta|'])
	relabels.append(['Eta_pfjet3','Third leading jet |#eta|','|#eta|'])
	relabels.append(['Eta_pfjet4','Fourth leading jet |#eta|','|#eta|'])
	relabels.append(['Eta_pfjet5','Fifth leading jet |#eta|','|#eta|'])
	relabels.append(['preexc','N_{Jet}','N_{Jet}'])
	relabels.append(['PFJet30Count','N_{Jet}','N_{Jet}'])
	# if 'BTagOff' in 'pyplots':
	# 	relabels[-1][1]+=' (No b-tag veto)'
	# else:
	# 	relabels[-1][1]+=' (With b-tag veto)'		
	relabels.append(['MT_muon1METR','M_{T}(#mu,E_{T}^{miss}) [GeV]','M_{T}'])
	relabels.append(['Pt_MET','E_{T}^{miss} [GeV]','E_{T}^{miss}'])
	relabels.append(['DeltaPhi_pfjet1muon1','#Delta #phi(jet_{1},#mu)'	,'#Delta #phi(jet_{1},#mu)'])
	relabels.append(['DeltaPhi_pfjet2muon1','#Delta #phi(jet_{2},#mu)'	,'#Delta #phi(jet_{2},#mu)'])
	relabels.append(['DeltaPhi_pfjet3muon1','#Delta #phi(jet_{3},#mu)'	,'#Delta #phi(jet_{3},#mu)'])
	relabels.append(['DeltaPhi_pfjet4muon1','#Delta #phi(jet_{4},#mu)'	,'#Delta #phi(jet_{4},#mu)'])
	relabels.append(['DeltaPhi_pfjet5muon1','#Delta #phi(jet_{5},#mu)'	,'#Delta #phi(jet_{5},#mu)'])

	filesets = []

	allfiles = glob('pyplots/*hlog')
	usedfiles = []
	# print allfiles
	for rl in relabels:
		fset = []
		for a in allfiles:
			if rl[0] in a and 'standard' in a and a not in usedfiles:
				fset.append(a)
				print a
		for a in allfiles:
			if rl[0] in a and 'standard' not in a and a not in usedfiles:
				fset.append(a)
		newfset = []
		for a in fset:
			if 'nouflow' not in a and 'altunf' not in a:
				newfset.append(a)

		if len(fset)>0:
			newfset.append([rl[1],"Events/bin"])
			filesets.append(newfset)
		usedfiles = []
		for x in filesets:
			for y in x:
				usedfiles.append(y)

	htrelabels = []
	htrelabels.append(['HT_pfjets','inc1','H_{T} (#geq 1 jet) [GeV]', 'H_{T}'])
	htrelabels.append(['HT_pfjets','inc2','H_{T} (#geq 2 jets) [GeV]','H_{T}'])
	htrelabels.append(['HT_pfjets','inc3','H_{T} (#geq 3 jets) [GeV]','H_{T}'])
	htrelabels.append(['HT_pfjets','inc4','H_{T} (#geq 4 jets) [GeV]','H_{T}'])


	for rl in htrelabels:
		fset = []
		for a in allfiles:
			if rl[0] in a and rl[1] in a and 'standard' in a and a not in usedfiles:
				fset.append(a)
				print a
		for a in allfiles:
			if rl[0] in a and rl[1] in a and 'standard' not in a and a not in usedfiles:
				fset.append(a)

		newfset = []
		for a in fset:
			if 'nouflow' not in a and 'altunf' not in a:
				newfset.append(a)

		if len(newfset)>0:
			newfset.append([rl[2],"Events/bin"])
			filesets.append(newfset)
		usedfiles = []
		for x in filesets:
			for y in x:
				usedfiles.append(y)
	# print filesets
	# sys.exit()

	# print filesets

	for f in filesets:

		_inclu = 'pre' in str(f) 
		# print f
		# if 'pre' in str(f):
		# 	sys.exit()
		# if 'MT' not in str(f):
		# 	continue
		# for a in f:
		# 	print a
		c1 = TCanvas("c1","",600,800)
		cpad1 = TPad( 'cpad1', 'cpad1', 0.0, 0.35, 1.0, 1.0 )#divide canvas into pads
		cpad1.SetRightMargin(0.1)
		cpad1.SetTopMargin(0.15)
		cpad1.SetBottomMargin(0.0)


		cpad2 = TPad( 'cpad2', 'cpad2', 0.0, 0.1, 1.0, 0.35 )#divide canvas into pads
		cpad2.SetRightMargin(0.1)
		cpad2.SetTopMargin(0.0)
		cpad2.SetBottomMargin(0.3)


		dolinear = False
		if 'MT' in str(f):
			dolinear=True
		dolinear = False
		if (dolinear == False):
			cpad1.SetLogy()

		cpad1.Draw()
		cpad2.Draw()

		cpad1.cd()

		# print harray
		_binning = []

		entries = []
		plotmin = 99999.9
		plotmax = 0.1


		def fixarray(anharray,todo):
			if todo == False:
				return anharray
			else:
				newharray = []
				for h in anharray:
					print h
				for _n1 in range(len(anharray)):
					if _n1>5:
						break	
					entry = anharray[_n1]
					[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
					eq *= eq
					es *= es
					ev *= ev
					ez *= ez
					et *= et
					ew *= ew
					eT *= eT
					for _n2 in range(len(anharray)):
						if _n2 <= _n1:
							continue
						_entry = anharray[_n2]

						[_lhs,_rhs,_q,_eq,_s,_es,_v,_ev,_z,_ez,_t,_et,_w,_ew,_T,_eT,_D] = _entry	
						q += _q
						s += _s
						v += _v
						z += _z
						t += _t
						w += _w
						T += _T
						D += _D
						eq += _eq*_eq
						es += _es*_es
						ev += _ev*_ev
						ez += _ez*_ez
						et += _et*_et
						ew += _ew*_ew
						eT += _eT*_eT
					eq = math.sqrt(eq)
					es = math.sqrt(es)
					ev = math.sqrt(ev)
					ez = math.sqrt(ez)
					et = math.sqrt(et)
					ew = math.sqrt(ew)
					eT = math.sqrt(eT)
					newharray.append([lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D])
				return newharray
			# print ' -------------------------- '
			# harray = newharray
			# for h in harray:
			# 	print h

			# sys.exit()

		# harray = HArrayFromHlog(f[0])

		harray = fixarray(HArrayFromHlog(f[0]),_inclu)
		for entry in harray:
			# print entry
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
			# print lhs, rhs
			_plotpoints = [q,s,v,z,t,w,T,D]
			plotpoints = []
			for p in _plotpoints:
				if p>0.0001:
					plotpoints.append(p)
			entries.append(entry)
			_binning.append(lhs)
			if len(plotpoints)==0:
				continue
			_plotmin = 10.9*min(plotpoints)
			_plotmax = 4.0*max(plotpoints)
			if _plotmin < plotmin: plotmin = _plotmin
			if _plotmax > plotmax: plotmax = _plotmax


		if plotmin <0.1: plotmin = 0.1
		if dolinear:
			plotmin = 0
			plotmax = 0.25*plotmax*1.2
		_binning.append(rhs)
		# print _binning
		presentationbinning= _binning

		if 'MT' in str(f):
			presentationbinning = []
			for b in _binning:
				if b <=150:
					presentationbinning.append(b)
			print presentationbinning
			# sys.exit()
			plotmax *= 10
			plotmin *= 5

		Label = f[-1]


		hs_rec_WJets=NullHisto('hs_rec_WJets','W+Jets',presentationbinning,WStackStyle,Label)
		hs_rec_Data=NullHisto('hs_rec_Data','Data',presentationbinning,DataRecoStyle,Label)
		hs_rec_DiBoson=NullHisto('hs_rec_DiBoson','DiBoson',presentationbinning,DiBosonStackStyle,Label)
		hs_rec_ZJets=NullHisto('hs_rec_ZJets','Z+Jets',presentationbinning,ZStackStyle,Label)
		hs_rec_TTBar=NullHisto('hs_rec_TTBar','t#bar{t}',presentationbinning,TTStackStyle,Label)
		hs_rec_SingleTop=NullHisto('hs_rec_SingleTop','Single t',presentationbinning,StopStackStyle,Label)
		hs_rec_QCDMu=NullHisto('hs_rec_QCDMu','Multijet',presentationbinning,QCDStackStyle,Label)


		# Declare the MC Stack
		MCStack = THStack ("MCStack","")
		plotmax *=5.0
		plotmin *=.5

		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)

		# List of MC Histos
		SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]

		# for x in SM:
		# 	x.SetLineColor(1)
		xoffset = 1.1
		_nbin = 0
		for entry in entries:
			_nbin += 1
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry			
			# print hs_rec_WJets.GetBinCenter(_nbin) - 0.5*hs_rec_WJets.GetBinWidth(_nbin)

			hs_rec_WJets.SetBinContent(_nbin,w)
			hs_rec_Data.SetBinContent(_nbin,D)
			hs_rec_DiBoson.SetBinContent(_nbin,v)
			hs_rec_ZJets.SetBinContent(_nbin,z)
			hs_rec_TTBar.SetBinContent(_nbin,t)
			hs_rec_SingleTop.SetBinContent(_nbin,s)
			hs_rec_QCDMu.SetBinContent(_nbin,q)

		# Build stack
		for x in SM:
			# print x.Integral()
			# x.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
			# x.GetXaxis().SetLimits(_binning[0],_binning[-1])
			x.SetMaximum(plotmax)
			x.SetMaximum(plotmin)
			x.GetXaxis().SetTitleOffset(xoffset)

			MCStack.Add(x)
		# MCStack.GetHistogram().GetXaxis().SetRangeUser(_binning[0],_binning[-1])		
		# hs_rec_Data.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
		# hs_rec_Data.GetXaxis().SetLimits(_binning[0],_binning[-1])


		hs_rec_Data_ratio=NullHisto('hs_rec_Data_ratio','Data,',presentationbinning,DataRecoStyle,Label)


		# hs_rec_Data_ratio = hs_rec_Data.Clone()

		hs_rec_MC_ratio = hs_rec_WJets.Clone()
		hs_rec_MC_ratio.Add(hs_rec_DiBoson)
		hs_rec_MC_ratio.Add(hs_rec_ZJets)
		hs_rec_MC_ratio.Add(hs_rec_TTBar)
		hs_rec_MC_ratio.Add(hs_rec_SingleTop)
		hs_rec_MC_ratio.Add(hs_rec_QCDMu)

		hs_rec_Data_ratio.Add(hs_rec_MC_ratio)
		hs_rec_Data_ratio.Divide(hs_rec_Data)


		hs_rec_Data_ratio.GetYaxis().SetTitle("MC/Data")

		centlog = f[0]
		syslogs = (f[1:-1])

		_centralvals = []
		_datavals = []
		_staterrs = []
		_syserrsup = []
		_syserrsdown = []

		_variations = []


		for entry in fixarray(HArrayFromHlog(centlog),_inclu):
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
			_centralvals.append(T)
			_datavals.append(D)
			_staterrs.append(eT)

		for syslog in syslogs:
			_sysvals = []
			_wvals = []
			for entry in fixarray(HArrayFromHlog(syslog),_inclu):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T)
				_wvals.append(w)
			# print syslog, _wvals[0:3]

			_variations.append(_sysvals)
		# sys.exit()
		for syslog in [centlog]:
			_sysvals = []
			_wvals = []
			for entry in fixarray(HArrayFromHlog(syslog),_inclu):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T+w*0.047)
				_wvals.append(w)
			_variations.append(_sysvals)

		for syslog in [centlog]:
			_sysvals = []
			_wvals = []
			for entry in fixarray(HArrayFromHlog(syslog),_inclu):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T-w*0.047)
				_wvals.append(w)
			_variations.append(_sysvals)

		for syslog in [centlog]:
			_sysvals = []
			_wvals = []
			for entry in fixarray(HArrayFromHlog(syslog),_inclu):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T*1.022)
				_wvals.append(w)
			_variations.append(_sysvals)

		for syslog in [centlog]:
			_sysvals = []
			_wvals = []
			for entry in fixarray(HArrayFromHlog(syslog),_inclu):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T*0.978)
				_wvals.append(w)
			_variations.append(_sysvals)


		# print f
		for _c in range(len(_centralvals)):
			c = _centralvals[_c]
			_staterr = _staterrs[_c]
			_upvars = []
			_downvars = []
			for _v in _variations:
				_val = _v[_c]
				if _val > c:
					_upvars.append(_val - c)
				if _val < c:
					_downvars.append(c-_val)
			_upvars.append(_staterr)
			_downvars.append(_staterr)
			# print c, _upvars,_downvars				
			__sup = quadsum(_upvars)
			__sdown = quadsum(_downvars)
			_syserrsup.append(__sup)
			_syserrsdown.append(__sdown)

		# print _centralvals
		# print _staterrs
		# print _syserrsup
		# print _syserrsdown

		_centralvals_rat = []
		_syserrsdown_rat = []
		_syserrsup_rat = []

		for n in range(len(_centralvals)):
			_c = _centralvals[n]
			_data = _datavals[n]
			_d = _syserrsdown[n]
			_u = _syserrsup[n]
			if _data > 0:
				_centralvals_rat.append(_c/_data)
			else:
				_centralvals.append(1.0)
			if _data > 0.0:
				_u = _u/_data
				_d = _d/_data
			else:
				_u = 0.0
				_d = 0.0
			# print _u, _d

			_syserrsup_rat.append( abs((abs(1.0/(1.0-_d)))-1.0) )
			_syserrsdown_rat.append( abs( 1.0- 1.0/(1.0+_u) ) )


		# print 'WINDOW', presentationbinning, plotmin
		[ErrorWindow,null] = CreateBandHistoFromLists(presentationbinning, "",Label, _centralvals, _syserrsup, _syserrsdown, bgbandstyle,1.0,"TopPlot")

		[ErrorWindow_rat,null_rat] = CreateBandHistoFromLists(presentationbinning, "",Label, _centralvals_rat, _syserrsup_rat, _syserrsdown_rat, bgbandstyle,1.0,"SubPlot")

		# print presentationbinning
		# print _centralvals
		# [ErrorWindow,null] = CreateHistoFromLists([100.0,110.0,120.0,130.0], "",Label, [10000.0,10000.0,10000.0], [1000.0,1000.0,1000.0], [10000.0,10000.0,10000.0] , bgbandstyle,1.0,"TopPlot")
		# print null

		ErrorWindow.SetMaximum(plotmax)
		ErrorWindow.SetMinimum(plotmin)

		ErrorWindow.GetHistogram().GetYaxis().CenterTitle(0)
		# ErrorWindow.GetHistogram().GetXaxis().CenterTitle(0)

		ErrorWindow.GetXaxis().SetRangeUser(presentationbinning[0], presentationbinning[-1])

		ErrorWindow_rat.GetYaxis().SetTitle("MC/Data")
		# ErrorWindow_rat.GetXaxis().SetTitle("")


		ErrorWindow.GetHistogram().GetXaxis().SetNdivisions(110)


		ErrorWindow.Draw("a2")
		# ErrorWindow.GetXaxis().SetMinimum(presentationbinning[0])
		# ErrorWindow.GetXaxis().SetMaximum(presentationbinning[-1])
		# ErrorWindow.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
		# ErrorWindow.GetXaxis().SetLimits(_binning[0],_binning[-1])
		ErrorWindow.SetMaximum(plotmax)
		ErrorWindow.SetMinimum(plotmin)
		ErrorWindow.GetXaxis().SetTitleOffset(xoffset)

		# ErrorWindow.Draw("a2")
		# cpad1.Update()


		MCStack.Draw("SAME")
		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)
		MCStack.GetXaxis().SetTitleOffset(xoffset)
		MCStack.GetYaxis().SetTitleOffset(0.9)
		MCStack.Draw("HISTSAME")

		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)
		cpad1.Update()
		MCStack=BeautifyStack(MCStack,Label)

		# Draw the data.
		for _dbin in range(hs_rec_Data.GetNbinsX()+2):
			if hs_rec_Data.GetBinContent(_dbin) > 0:
				hs_rec_Data.SetBinError(_dbin,math.sqrt(hs_rec_Data.GetBinContent(_dbin)))
		# hs_rec_Data.Print("range")

		# sys.exit()
		# if _inclu == True:
		# 	for pbin in range(hs_rec_Data.GetNbinsX()):
		# 		hs_rec_Data.GetXaxis().SetBinLabel(pbin+1,'#geq '+str(pbin+1))
		# 		blab = hs_rec_Data.GetXaxis().GetBinLabel(pbin+1)
		# 		print pbin,blab

		hs_rec_Data.Draw("EPSAME")		
		# ErrorWindow.Draw("2")

		leg = TLegend(0.69,0.52,0.9,0.82,"","brNDC");
		leg.SetTextFont(42);
		leg.SetFillColor(0);
		leg.SetBorderSize(0);
		leg.SetTextSize(.04)
		leg.AddEntry(hs_rec_Data)
		ind = -1
		SM.reverse()
		for s in SM:
			ind += 1
			leg.AddEntry(SM[ind])

		SM.reverse()
		leg.Draw()

		# Stamp on top
		sqrts = "#sqrt{s} = 7 TeV";
		l1=TLatex()
		l1.SetTextAlign(12)
		l1.SetTextFont(42)
		l1.SetNDC()
		l1.SetTextSize(0.05)
		l1.DrawLatex(0.16,0.9,sqrts+"           L_{int} = 5.0 fb^{-1}             CMS ")


		tlatalign = 0.32
		l3=TLatex()
		l3.SetTextAlign(12)
		l3.SetTextFont(42)
		l3.SetNDC()
		l3.SetTextSize(0.04)
		l3.DrawLatex(tlatalign,0.78,"anti-k_{T} (R = 0.5) Jets")
		l3.DrawLatex(tlatalign,0.73,"p_{T}^{jet}>30 GeV, |#eta^{jet}|<2.4")
		l3.DrawLatex(tlatalign,0.68,"W#rightarrow#mu#nu channel")
		if 'BTagOff' not in 'pyplots':
			l3.DrawLatex(tlatalign,0.63,"No events with #geq 1 b-jets")

		gPad.RedrawAxis()
		

		cpad2.cd()

		ratunity=TLine(presentationbinning[0], 1.0 , presentationbinning[-1],1.0)


		ErrorWindow_rat.SetMaximum(1.8)
		ErrorWindow_rat.SetMinimum(0.2)

		ErrorWindow_rat.GetXaxis().SetNdivisions(110)
		ErrorWindow_rat.GetYaxis().SetNdivisions(505)

		ErrorWindow_rat.GetXaxis().SetRangeUser(presentationbinning[0], presentationbinning[-1])

		if _inclu == True:
			cent1lowerh= TH1D('cent1lowerh','cent1lowerh',len(presentationbinning)-1,array('d',presentationbinning))
			for pbin in range(cent1lowerh.GetNbinsX()):
				cent1lowerh.GetXaxis().SetBinLabel(pbin+1,'#geq '+str(pbin+1))
				blab = cent1lowerh.GetXaxis().GetBinLabel(pbin+1)
				print pbin,blab

			cent1lowerh.SetMaximum(1.8)
			cent1lowerh.SetMinimum(0.2)

			cent1lowerh.GetXaxis().SetNdivisions(110)
			cent1lowerh.GetYaxis().SetNdivisions(505)
			cent1lowerh.GetXaxis().SetTitle(ErrorWindow_rat.GetHistogram().GetXaxis().GetTitle())
			cent1lowerh.GetYaxis().SetTitle(ErrorWindow_rat.GetHistogram().GetYaxis().GetTitle())
			cent1lowerh.GetXaxis().SetTitleSize(0.13)
			cent1lowerh.GetXaxis().SetLabelSize(0.18)
			cent1lowerh.GetYaxis().SetTitleSize(0.13)
			cent1lowerh.GetYaxis().SetLabelSize(0.12)
			cent1lowerh.GetYaxis().SetTitleOffset(0.5)
			cent1lowerh.GetYaxis().CenterTitle(1)

			cent1lowerh.Draw()


			ErrorWindow_rat.Draw("2")
		else:
			ErrorWindow_rat.Draw("a2")

		# print "TITLE:",ErrorWindow_rat.GetHistogram().GetXaxis().GetTitle()

		# ErrorWindow_rat.GetHistogram().GetYaxis().CenterTitle(0)
		ErrorWindow_rat.GetHistogram().GetXaxis().CenterTitle(0)
		ErrorWindow_rat.GetHistogram().GetYaxis().SetTitleOffset(0.5)


		ErrorWindow_rat.GetHistogram().GetXaxis().SetLabelSize(.12);
		ErrorWindow_rat.GetHistogram().GetYaxis().SetLabelSize(.12);
		ratunity.SetLineStyle(2)
		ratunity.Draw("SAME")
		hs_rec_Data_ratio.SetMinimum(0.2)
		hs_rec_Data_ratio.SetMaximum(1.8)

		hs_rec_Data_ratio.GetXaxis().SetNdivisions(110)
		hs_rec_Data_ratio.GetYaxis().SetNdivisions(505)



		hs_rec_Data_ratio.Draw("][SAME")

		fname = f[0].replace('.hlog','_reco.')
		

		print fname
		c1.Print(fname+'png')
		c1.Print(fname+'pdf')





def ParseTablesToFinalResults(WRenorm,sel):
	allfiles = glob('pyplots/*txt')
	for f in allfiles:
		print ' Present:',f
		if 'FINAL' in f:
			continue
		# if 'MET' in f and ('phi' in f or 'Phi' in f):
		# 	continue
		if 'MT' in f:
			continue
		continue
		# if 'Eta_mu' not in f:
		# 	continue
		# if "Delta" not in f or 'et3' not in f:
		# 	continue
		# if 'HT' not in f and 'inc1' not in f : 
		# 	continue
		# if 'inc4' not in f:
		# 	continue
		# if 'Pt_pfjet4' not in f:
		# 	continue
		# if 'Count' not in f:
		# 	continue
		# if 'Pt_pfjet2' not in f:
		# 	continue
		# print f
		# if 'PFJet30Count' not in f:
		# 	continue
		# continue
		# if ('Pt_pf' not in f and 'Count' not in f) and 'pre' not in f:
		# 	continue
		# if 'Del' not in f or 'jet3' not in f:
		# 	continue
		# if 'Vert' in f:
		# 	continue
		# if 'Eta' not in f or 'jet4' not in f:
		# 	continue
		# if 'pre' not in f:
		# 	continue
		# if "HT" not in f:
		# 	continue
		# if 'Pt_pf' not in f and 'Count' not in f:
		# 	continue
		print '\n\nAnalyzing table: ',f
		# continue
		output = f.replace('.txt','FINAL.')
		table = tabletolist(f)

		[tablebinning,rootbinning] = getbinning(table)
		[pred_tex, pred_mean, pred_err] = getcolumn(table,1)
		[meas_tex, meas_mean, meas_err_plus, meas_err_minus,meas_err_verbose] = getmeasurement(table)
		print ' ---------'
		# print f
		# for t in table:
		# 	print t
		# print '-----'
		# print tablebinning
		# print '-----'
		# print pred_tex
		# print '-----'
		# print pred_mean
		# print '-----'
		# print meas_err_plus
		# print '-----'
		# print meas_err_verbose				
		# print '-----'


		StringToFile(TexTableFromColumns([tablebinning,pred_tex,meas_tex]), output+'TexCount.txt', ',') 

		systablesetup = [tablebinning]
		for x in meas_err_verbose:
			systablesetup.append(x)
			# print x

		StringToFile(TexTableFromColumns(systablesetup), output+'TexVerboseError.txt', ',') 

		# sys.exit()
		StringToFile(NormalizeTexTable(output+'TexCount.txt',4955.0), output+'TexXSec.txt',',')

		prediction_means = [pred_mean]
		prediction_errors = [pred_err]
		prediction_names = ['MADGRAPH']
		
		label = f.split('/')[-1]
		label = label.split('.')[0]
		
		label = label.replace('_pt20','')
		label = label.replace('_eta2p5','')


		quantity = ' BLANK '
		
		if label=='Pt_pfjet1':
			label = 'Leading jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_muon1':
			label = 'Muon p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Eta_muon1':
			label = 'Muon #eta '
			quantity = '#eta'

		if label=='HT_pfjets_inc1':
			label = 'H_{T} (#geq 1 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc2':
			label = 'H_{T} (#geq 2 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc3':
			label = 'H_{T} (#geq 3 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc4':
			label = 'H_{T} (#geq 4 jet) [GeV]'
			quantity = 'H_{T}'						

		if label=='Pt_pfjet2':
			label = 'Second leading jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet3':
			label = 'Third leading jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet4':
			label = 'Fourth leading jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet5':
			label = 'Fifth leading jet p_{T} [GeV]'
			quantity = 'p_{T}'			
			
		if label=='Eta_pfjet1':
			label = 'Leading Jet |#eta|'
			quantity = '|#eta|'
			
		if label=='Eta_pfjet2':
			label = 'Second leading jet |#eta|'
			quantity = '|#eta|'						

		if label=='Eta_pfjet3':
			label = 'Third leading jet |#eta|'
			quantity = '|#eta|'	

		if label=='Eta_pfjet4':
			label = 'Fourth leading jet |#eta|'
			quantity = '|#eta|'	

		if label=='Eta_pfjet5':
			label = 'Fifth leading jet |#eta|'
			quantity = '|#eta|'				

		if label=='PFJet30Count':
			label = 'Exclusive jet multiplicity'
			quantity = 'N_{Jet}'

		if label=='PFJet30Count_preexc':
			label = 'Inclusive jet multiplicity'
			quantity = 'N_{Jet}'

		if label=='MT_muon1METR':
			label = 'M_{T}(#mu,E_{T}^{miss}) [GeV]'
			quantity = 'M_{T}'

		if label=='Pt_MET':
			label = 'E_{T}^{miss} [GeV]'
			quantity = 'E_{T}^{miss}'

		if label=='DeltaPhi_pfjet1muon1':
			label = '#Delta #phi(jet_{1},#mu)'	
			quantity = '#Delta #phi(jet_{1},#mu)'

		if label=='DeltaPhi_pfjet2muon1':
			label = '#Delta #phi(jet_{2},#mu)'	
			quantity = '#Delta #phi(jet_{2},#mu)'

		if label=='DeltaPhi_pfjet3muon1':
			label = '#Delta #phi(jet_{3},#mu)'	
			quantity = '#Delta #phi(jet_{3},#mu)'

		if label=='DeltaPhi_pfjet4muon1':
			label = '#Delta #phi(jet_{4},#mu)'	
			quantity = '#Delta #phi(jet_{4},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{5},#mu)'	
			quantity = '#Delta #phi(jet_{5},#mu)'

		
		# print "USING W RENORMALIZATION: ",WRenorm
		# print " -"*40
		# FinalHisto(rootbinning,label,quantity, output+'PlotCount.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,0,WRenorm,sel)
		FinalHisto(rootbinning,label,quantity, output+'PlotXSec.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,4955.0,WRenorm,sel,False)
		# FinalHisto(rootbinning,label,quantity, output+'PlotXSec.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,4955.0,WRenorm,sel,True)
		# sys.exit()

		#os.system('cat pyplots/Pt_pfjet1FINAL.TexCount.txt')

def setTDRStyle():

	# For the canvas:
	gStyle.SetCanvasBorderMode(0)
	gStyle.SetCanvasColor(0) # must be kWhite but I dunno how to do that in PyROOT
	gStyle.SetCanvasDefH(600) #Height of canvas
	gStyle.SetCanvasDefW(600) #Width of canvas
	gStyle.SetCanvasDefX(0)   #POsition on screen
	gStyle.SetCanvasDefY(0)


	# For the Pad:
	gStyle.SetPadBorderMode(0);
	# gStyle.SetPadBorderSize(Width_t size = 1);
	gStyle.SetPadColor(0); # kWhite
	gStyle.SetPadGridX(0); #false
	gStyle.SetPadGridY(0); #false
	gStyle.SetGridColor(0);
	gStyle.SetGridStyle(3);
	gStyle.SetGridWidth(1);

	# For the frame:
	gStyle.SetFrameBorderMode(0);
	gStyle.SetFrameBorderSize(1);
	gStyle.SetFrameFillColor(0);
	gStyle.SetFrameFillStyle(0);
	gStyle.SetFrameLineColor(1);
	gStyle.SetFrameLineStyle(1);
	gStyle.SetFrameLineWidth(1);

	# For the histo:
	# gStyle.SetHistFillColor(1);
	# gStyle.SetHistFillStyle(0);
	gStyle.SetHistLineColor(1);
	gStyle.SetHistLineStyle(0);
	gStyle.SetHistLineWidth(1);
	# gStyle.SetLegoInnerR(Float_t rad = 0.5);
	# gStyle.SetNumberContours(Int_t number = 20);

	gStyle.SetEndErrorSize(2);
	#gStyle.SetErrorMarker(20);   #/ I COMMENTED THIS OUT
	gStyle.SetErrorX(0.);

	gStyle.SetMarkerStyle(20);

	#For the fit/function:
	gStyle.SetOptFit(0);
	gStyle.SetFitFormat("5.4g");
	gStyle.SetFuncColor(2);
	gStyle.SetFuncStyle(1);
	gStyle.SetFuncWidth(1);

	#For the date:
	gStyle.SetOptDate(0);
	# gStyle.SetDateX(Float_t x = 0.01);
	# gStyle.SetDateY(Float_t y = 0.01);

	# For the statistics box:
	gStyle.SetOptFile(0);
	gStyle.SetOptStat(0); # To display the mean and RMS:   SetOptStat("mr");
	gStyle.SetStatColor(0); # kWhite
	gStyle.SetStatFont(42);
	gStyle.SetStatFontSize(0.025);
	gStyle.SetStatTextColor(1);
	gStyle.SetStatFormat("6.4g");
	gStyle.SetStatBorderSize(1);
	gStyle.SetStatH(0.1);
	gStyle.SetStatW(0.15);
	# gStyle.SetStatStyle(Style_t style = 1001);
	# gStyle.SetStatX(Float_t x = 0);
	# gStyle.SetStatY(Float_t y = 0);

	# Margins:
	gStyle.SetPadTopMargin(0.05);
	gStyle.SetPadBottomMargin(0.13);
	gStyle.SetPadLeftMargin(0.16);
	#gStyle.SetPadRightMargin(0.12);
	gStyle.SetPadRightMargin(0.02);

	# For the Global title:

	gStyle.SetOptTitle(0);
	gStyle.SetTitleFont(42);
	gStyle.SetTitleColor(1);
	gStyle.SetTitleTextColor(1);
	gStyle.SetTitleFillColor(10);
	gStyle.SetTitleFontSize(0.05);
	# gStyle.SetTitleH(0); # Set the height of the title box
	# gStyle.SetTitleW(0); # Set the width of the title box
	# gStyle.SetTitleX(0); # Set the position of the title box
	# gStyle.SetTitleY(0.985); # Set the position of the title box
	# gStyle.SetTitleStyle(Style_t style = 1001);
	# gStyle.SetTitleBorderSize(2);

	# For the axis titles:

	gStyle.SetTitleColor(1, "XYZ");
	gStyle.SetTitleFont(42, "XYZ");
	gStyle.SetTitleSize(0.06, "XYZ");
	# gStyle.SetTitleXSize(Float_t size = 0.02); # Another way to set the size?
	# gStyle.SetTitleYSize(Float_t size = 0.02);
	gStyle.SetTitleXOffset(0.9);
	gStyle.SetTitleYOffset(1.25);
	# gStyle.SetTitleOffset(1.1, "Y"); # Another way to set the Offset

	# For the axis labels:

	gStyle.SetLabelColor(1, "XYZ");
	gStyle.SetLabelFont(42, "XYZ");
	gStyle.SetLabelOffset(0.007, "XYZ");
	gStyle.SetLabelSize(0.05, "XYZ");

	# For the axis:

	gStyle.SetAxisColor(1, "XYZ");
	gStyle.SetStripDecimals(1); # True
	gStyle.SetTickLength(0.03, "XYZ");
	gStyle.SetNdivisions(510, "XYZ");
	gStyle.SetPadTickX(1);  # To get tick marks on the opposite side of the frame
	gStyle.SetPadTickY(1);

	# Change for log plots:
	gStyle.SetOptLogx(0);
	gStyle.SetOptLogy(0);
	gStyle.SetOptLogz(0);

	# Postscript options:
	gStyle.SetPaperSize(20.,20.);
	# gStyle.SetLineScalePS(Float_t scale = 3);
	# gStyle.SetLineStyleString(Int_t i, const char* text);
	# gStyle.SetHeaderPS(const char* header);
	# gStyle.SetTitlePS(const char* pstitle);

	# gStyle.SetBarOffset(Float_t baroff = 0.5);
	# gStyle.SetBarWidth(Float_t barwidth = 0.5);
	# gStyle.SetPaintTextFormat(const char* format = "g");
	# gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
	# gStyle.SetTimeOffset(Double_t toffset);
	# gStyle.SetHistMinimumZero(True);

def CleanUpAndMakeTables():
	allfiles = glob('pyplots/*.*')
	for f in allfiles:
		if 'btag' in f:
			continue
		# print f
		newfile=''
		count=0
		if f.count('.')>=2:
			for x in f:
				if x=='.':
					count += 1
					if count!=f.count('.'):
						x='_'
				newfile += (x)
			print ( f + ' -> ' + newfile)

			os.system(' mv ' + f + ' ' + newfile)
			

	cont = ['pyplots'+'/' + x.replace('\n','') for x in os.listdir('pyplots')]

	tables = []
	systables = []

	for c in cont:
		if "FINAL" in c and 'Tex' in c and 'Verbose' not in c:
			tables.append(c)

	for c in cont:
		if "FINAL" in c and 'Tex' in c and 'Verbose'  in c:
			systables.append(c)

	for t in tables:
		print t
	for s in systables:
		print s

	pairs = []
	for t in tables:
		if "TexCount" not in t:
			continue
		p = []
		p.append(t)
		for tt in tables:
			if tt == t.replace('TexCount','TexXSec'):
				p.append(tt)
		if len(p)==2:
			pairs.append(p)


	def TexTableFromPair(pair):
		
		for p in pair:
			if 'TexCount' in p:
				outfile = open(pair[0].replace('TexCount.txt','All.tex'),'w')

		alllines=[]
		for p in pair:	
			for line in open(p):
				line=line.replace('--','-')
				line=line.replace('&','')
				line=line.replace('\\','')
				line=line.replace('pm','\\pm')
				newline = ''
				dcount = 0
				for c in line:
					newline +=(c)
					if c == "$":
						dcount +=1
					if dcount ==2:
						dcount=0
						newline += '&' 
				newline = newline.split("&")
				alllines.append(newline)

		newtable = []
		for a in range(len(alllines)/2):
			c = alllines[a]
			x = alllines[a+len(alllines)/2]
			div = ' & '
			bin = c[0]
			bin = bin.replace('-','')
			bin = bin.replace('$','')
			bin = bin.split()
			outbin = '$'
			outbin += str(round(float(bin[0]),2))
			outbin += '-'
			outbin += str(round(float(bin[1]),2))
			outbin += "$"
			outbin = outbin.replace("$ 0.5 - 1.5 $","1")
			outbin = outbin.replace("$ 1.5 - 2.5 $","2")
			outbin = outbin.replace("$ 2.5 - 3.5 $","3")
			outbin = outbin.replace("$ 3.5 - 4.5 $","4")
			outbin = outbin.replace("$ 4.5 - 5.5 $","5")
			outbin = outbin.replace("$ 5.5 - 6.5 $","6")
			outbin = outbin.replace("$ 6.5 - 7.5 $","7")
			outbin = outbin.replace("$ 7.5 - 8.5 $","8")
			outbin=outbin.replace("$0.5-1.5$","1")
			outbin=outbin.replace("$1.5-2.5$","2")
			outbin=outbin.replace("$2.5-3.5$","3")
			outbin=outbin.replace("$3.5-4.5$","4")
			outbin=outbin.replace("$4.5-5.5$","5")
			outbin=outbin.replace("$5.5-6.5$","6")
			outbin=outbin.replace("$6.5-7.5$","7")
			outbin=outbin.replace("$7.5-8.5$","8")

			newtable.append(outbin+div+c[1]+div+c[2]+div+x[1]+div+x[2]+' \\\\')
		# for n in newtable:
		# 	print n


		vmap = []
		vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
		vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
		vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
		vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
		vmap.append(["Eta_pfjet1","$|\\eta(jet_1)|$"])
		vmap.append(["Eta_pfjet2","$|\\eta(jet_2)|$"])
		vmap.append(["Eta_pfjet3","$|\\eta(jet_3)|$"])
		vmap.append(["Eta_pfjet4","$|\\eta(jet_4)|$"])
		vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
		vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
		vmap.append(["PFJet30Count","Exc Jet Mult"])
		vmap.append(["Pt_MET","$E_T^{miss}$"])
		vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
		vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
		vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
		vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
		vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
		vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
		vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
		vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

		vmap.append(["Pt_muon1","$p_T(\\mu)$"])
		vmap.append(["Eta_muon1","$\eta(\\mu)$"])

		var = 'Bin'
		for v in vmap:
			if v[0] in str(pair):
				var = v[1]
		outfile.write('\\begin{table}[htb]\n\caption{Bin-by-bin data and uncertainties for the final '+var+' distribution.}\n')
		outfile.write("\\begin{center}\n\\begin{tabular}{|l|ll|ll|}\\hline\n "+var+"     & Predicted Events  & Measured Events & Predicted $\\sigma$ & Measured $\\sigma$ \\\\ \\hline \\hline\n")
		for n in newtable:
			outfile.write(n+'\n')
		outfile.write('\\hline\n\\end{tabular}\n\\end{center}\\end{table}\n')

		outfile.close()

	def systablefromfile(sysfile):


		vmap = []
		vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
		vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
		vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
		vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
		vmap.append(["Eta_pfjet1","$|\\eta(jet_1)|$"])
		vmap.append(["Eta_pfjet2","$|\\eta(jet_2)|$"])
		vmap.append(["Eta_pfjet3","$|\\eta(jet_3)|$"])
		vmap.append(["Eta_pfjet4","$|\\eta(jet_4)|$"])
		vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
		vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
		vmap.append(["PFJet30Count","Exc Jet Mult"])
		vmap.append(["Pt_MET","$E_T^{miss}$"])
		vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
		vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
		vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
		vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
		vmap.append(["Pt_muon1","$p_T(\\mu)$"])
		vmap.append(["Eta_muon1","$\eta(\\mu)$"])
		vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
		vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
		vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
		vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

		print sysfile
		var = 'Bin'
		for v in vmap:
			if v[0] in str(sysfile):
				var = v[1]

		outfile = open(sysfile.replace('TexVerboseError.txt','AllSys.tex'),'w')
		outfile.write('\\begin{scriptsize}\n\\begin{table}[htb]\n\caption{Bin-by-bin percent systematic uncertainties on the measured result for the final '+var+' distribution.}\n')
		outfile.write("\\begin{center}\n\\begin{tabular}{|l|ccccccccccccccccc|}\\hline\n "+var+"     &PU    & BG & Lumi   & bEff & BMis   & JES    & JER     & MES    & MER   & Stat  & Gen & MC & Evt & MET & Bay & BBB &Mat  \\\\ \\hline \\hline\n")
		for line in open(sysfile,'r'):
			outfile.write(line.replace('--','-'))
		outfile.write('\\hline\n\\end{tabular}\n\\end{center}\n\\end{table}\n\\end{scriptsize}\\\n')
		outfile.close()


	for pair in pairs:
		TexTableFromPair(pair)

	for s in systables:
		systablefromfile(s)


	print ' -------------- '

	cont = ['pyplots/' + x.replace('\n','') for x in os.popen('ls -1 pyplots |grep Sys| grep -v Tables | grep tex ')]
	cont.sort()
	latdoc = 'pyplots/Tables.tex'
	os.system('rm pyplots/Tables.*')


	doccont = '\\documentclass[8pt,a4paper]{article}\n\\usepackage[margin=0.25in]{geometry} \n\\begin{document}\n'

	for c in cont:
		name = c.split('/')[-1]
		name = name.split('.')[0]
		print name
		# doccont += name.replace('_','\\_') +'\\\\\n'
		doccont += '\\include{'+name+'}\n'
		if 'Sys' in name:
			doccont += '\\clearpage\n\n'

	doccont += '\n\\end{document}\n\n'

	print doccont

	x = open(latdoc,'w')
	x.write(doccont)
	x.close()

	exe = open('mtex.sh','w')
	exe.write("#!/bin/sh\n\ncd pyplots\n"+"\npdflatex Tables.tex"*2)
	exe.close()
	os.system('chmod 777 mtex.sh')
	os.system('./mtex.sh')
	os.system('rm mtex.sh')

	tdir = 'pyplots'

	files = glob(tdir+'/*AllSys.tex')
	print files

	def FixDrawLegend(legend):
		legend.SetTextFont(42)
		legend.SetTextSize(.04)

		legend.SetFillColor(0)
		legend.SetBorderSize(0)
		legend.Draw()
		return legend

	print ' '

	def quadsum(vals):
		_s = .0
		for v in vals:
			_s += v*v
		_s = math.sqrt(_s)
		return _s 


	def setTDRStyle2():

		# For the canvas:
		gStyle.SetCanvasBorderMode(0)
		gStyle.SetCanvasColor(0) # must be kWhite but I dunno how to do that in PyROOT
		gStyle.SetCanvasDefH(600) #Height of canvas
		gStyle.SetCanvasDefW(600) #Width of canvas
		gStyle.SetCanvasDefX(0)   #POsition on screen
		gStyle.SetCanvasDefY(0)


		# For the Pad:
		gStyle.SetPadBorderMode(0);
		# gStyle.SetPadBorderSize(Width_t size = 1);
		gStyle.SetPadColor(0); # kWhite
		gStyle.SetPadGridX(0); #false
		gStyle.SetPadGridY(0); #false
		gStyle.SetGridColor(0);
		gStyle.SetGridStyle(3);
		gStyle.SetGridWidth(1);

		# For the frame:
		gStyle.SetFrameBorderMode(0);
		gStyle.SetFrameBorderSize(1);
		gStyle.SetFrameFillColor(0);
		gStyle.SetFrameFillStyle(0);
		gStyle.SetFrameLineColor(1);
		gStyle.SetFrameLineStyle(1);
		gStyle.SetFrameLineWidth(1);

		# For the histo:
		# gStyle.SetHistFillColor(1);
		# gStyle.SetHistFillStyle(0);
		gStyle.SetHistLineColor(1);
		gStyle.SetHistLineStyle(0);
		gStyle.SetHistLineWidth(1);
		# gStyle.SetLegoInnerR(Float_t rad = 0.5);
		# gStyle.SetNumberContours(Int_t number = 20);

		gStyle.SetEndErrorSize(2);
		#gStyle.SetErrorMarker(20);   #/ I COMMENTED THIS OUT
		gStyle.SetErrorX(0.);

		gStyle.SetMarkerStyle(20);

		#For the fit/function:
		gStyle.SetOptFit(0);
		gStyle.SetFitFormat("5.4g");
		gStyle.SetFuncColor(2);
		gStyle.SetFuncStyle(1);
		gStyle.SetFuncWidth(1);

		#For the date:
		gStyle.SetOptDate(0);
		# gStyle.SetDateX(Float_t x = 0.01);
		# gStyle.SetDateY(Float_t y = 0.01);

		# For the statistics box:
		gStyle.SetOptFile(0);
		gStyle.SetOptStat(0); # To display the mean and RMS:   SetOptStat("mr");
		gStyle.SetStatColor(0); # kWhite
		gStyle.SetStatFont(42);
		gStyle.SetStatFontSize(0.025);
		gStyle.SetStatTextColor(1);
		gStyle.SetStatFormat("6.4g");
		gStyle.SetStatBorderSize(1);
		gStyle.SetStatH(0.1);
		gStyle.SetStatW(0.15);
		# gStyle.SetStatStyle(Style_t style = 1001);
		# gStyle.SetStatX(Float_t x = 0);
		# gStyle.SetStatY(Float_t y = 0);

		# Margins:
		gStyle.SetPadTopMargin(0.05);
		gStyle.SetPadBottomMargin(0.13);
		gStyle.SetPadLeftMargin(0.16);
		#gStyle.SetPadRightMargin(0.12);
		gStyle.SetPadRightMargin(0.02);

		# For the Global title:

		gStyle.SetOptTitle(0);
		gStyle.SetTitleFont(42);
		gStyle.SetTitleColor(1);
		gStyle.SetTitleTextColor(1);
		gStyle.SetTitleFillColor(10);
		gStyle.SetTitleFontSize(0.05);
		# gStyle.SetTitleH(0); # Set the height of the title box
		# gStyle.SetTitleW(0); # Set the width of the title box
		# gStyle.SetTitleX(0); # Set the position of the title box
		# gStyle.SetTitleY(0.985); # Set the position of the title box
		# gStyle.SetTitleStyle(Style_t style = 1001);
		# gStyle.SetTitleBorderSize(2);

		# For the axis titles:

		gStyle.SetTitleColor(1, "XYZ");
		gStyle.SetTitleFont(42, "XYZ");
		gStyle.SetTitleSize(0.06, "XYZ");
		# gStyle.SetTitleXSize(Float_t size = 0.02); # Another way to set the size?
		# gStyle.SetTitleYSize(Float_t size = 0.02);
		gStyle.SetTitleXOffset(0.9);
		gStyle.SetTitleYOffset(1.25);
		# gStyle.SetTitleOffset(1.1, "Y"); # Another way to set the Offset

		# For the axis labels:

		gStyle.SetLabelColor(1, "XYZ");
		gStyle.SetLabelFont(42, "XYZ");
		gStyle.SetLabelOffset(0.007, "XYZ");
		gStyle.SetLabelSize(0.05, "XYZ");

		# For the axis:

		gStyle.SetAxisColor(1, "XYZ");
		gStyle.SetStripDecimals(1); # True
		gStyle.SetTickLength(0.03, "XYZ");
		gStyle.SetNdivisions(510, "XYZ");
		gStyle.SetPadTickX(1);  # To get tick marks on the opposite side of the frame
		gStyle.SetPadTickY(1);

		# Change for log plots:
		gStyle.SetOptLogx(0);
		gStyle.SetOptLogy(0);
		gStyle.SetOptLogz(0);

		# Postscript options:
		gStyle.SetPaperSize(20.,20.);
		# gStyle.SetLineScalePS(Float_t scale = 3);
		# gStyle.SetLineStyleString(Int_t i, const char* text);
		# gStyle.SetHeaderPS(const char* header);
		# gStyle.SetTitlePS(const char* pstitle);

		# gStyle.SetBarOffset(Float_t baroff = 0.5);
		# gStyle.SetBarWidth(Float_t barwidth = 0.5);
		# gStyle.SetPaintTextFormat(const char* format = "g");
		# gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
		# gStyle.SetTimeOffset(Double_t toffset);
		# gStyle.SetHistMinimumZero(True);

	setTDRStyle2()



	def AnalyzeFile(afile):
		relabels = []
		relabels.append(['Pt_pfjet1','Leading Jet p_{T} [GeV]','p_{T}'])
		relabels.append(['Pt_muon1','Muon p_{T} [GeV]','p_{T}'])
		relabels.append(['N_GoodVertices','N_{Vertices}','N_{Vertices}'])
		relabels.append(['Pt_pfjet2','Second Leading Jet p_{T} [GeV]','p_{T}'])
		relabels.append(['Pt_pfjet3','Third Leading Jet p_{T} [GeV]','p_{T}'])
		relabels.append(['Pt_pfjet4','Fourth Leading Jet p_{T} [GeV]','p_{T}'])
		relabels.append(['Pt_pfjet5','Fifth Leading Jet p_{T} [GeV]','p_{T}'])
		relabels.append(['|#eta|_pfjet1','Leading Jet #|#eta|','#|#eta|'])
		relabels.append(['|#eta|_pfjet2','Second Leading Jet #|#eta|','#|#eta|'])
		relabels.append(['|#eta|_pfjet3','Third Leading Jet #|#eta|','#|#eta|'])
		relabels.append(['|#eta|_pfjet4','Fourth Leading Jet #|#eta|','#|#eta|'])
		relabels.append(['|#eta|_pfjet5','Fifth Leading Jet #|#eta|','#|#eta|'])
		relabels.append(['preexc','Jet Multiplicity (Inclusive)','N_{Jet}'])
		relabels.append(['PFJet30Count','N_{Jet}','N_{Jet}'])
		relabels.append(['MT_muon1METR','M_{T}(#mu,E_{T}^{miss}) [GeV]','M_{T}'])
		relabels.append(['Pt_MET','E_{T}^{miss} [GeV]','E_{T}^{miss}'])
		relabels.append(['DeltaPhi_pfjet1muon1','#Delta #phi(jet_{1},#mu)'	,'#Delta #phi(jet_{1},#mu)'])
		relabels.append(['DeltaPhi_pfjet2muon1','#Delta #phi(jet_{2},#mu)'	,'#Delta #phi(jet_{2},#mu)'])
		relabels.append(['DeltaPhi_pfjet3muon1','#Delta #phi(jet_{3},#mu)'	,'#Delta #phi(jet_{3},#mu)'])
		relabels.append(['DeltaPhi_pfjet4muon1','#Delta #phi(jet_{4},#mu)'	,'#Delta #phi(jet_{4},#mu)'])
		relabels.append(['DeltaPhi_pfjet5muon1','#Delta #phi(jet_{5},#mu)'	,'#Delta #phi(jet_{5},#mu)'])

		label = ''
		for x in relabels:
			if x[0] in afile:
				label = x[1]
		f = open(afile,'r')
		
		headers = ''
		contents = []
		for line in f:
			line = line.replace('hline','')
			line = line.replace('\\','')

			# print line
			if 'Lumi' in line:
				headers = line
			else:
				if '&' in line:
					contents.append(line)

		print ' '
		# print headers
		# for c in contents:
		# 	print c
		nbins = []

		vcont  = []
		for c in contents:
			dolastbin = False
			if c == contents[-1]:
				dolastbin = True
			v = [float(x) for x in c.replace('\n','').split('&')[1:]]
			c = c.split('&')[0]
			c = c.replace('$','')
			c = c.split(' - ')
			nbins.append(float(c[0]))
			vcont.append(v)
			if  dolastbin == True:
				nbins.append(float(c[1]))
		# print nbins

		binset = nbins
		n = len(binset)-1
		T = TH1D('T','Total',n,array('d',binset))
		JJ = TH1D('JJ','JES, JER',n,array('d',binset))
		MM = TH1D('MM','MES, MER, Muon Sel',n,array('d',binset))
		BG = TH1D('BG','Background',n,array('d',binset))
		UN = TH1D('UN','Statistical',n,array('d',binset))
		Gen = TH1D('Gen','Generator',n,array('d',binset))
		BT = TH1D('BT','BTagging',n,array('d',binset))
		OT = TH1D('OT','All other',n,array('d',binset))
		BB = TH1D('BB','Bayes/Bin',n,array('d',binset))
		MCT = TH1D('MCT','MC Stat',n,array('d',binset))
		allvals = []
		for x in range(len(binset)-1):
			[pu,bg,lu,bt,btm,js,jr,ms,mr,st,gn,mct,hl,mt,by,bb,ma] = vcont[x]
			nbin = x+1
			_T = math.sqrt(sum([aa*aa for aa in [pu,bg,lu,bt,btm,js,jr,ms,mr,st,gn,mct,hl,mt]]))
			T.SetBinContent(nbin,_T)
			
			_JJ = math.sqrt(js*js+jr*jr)
			_MM = math.sqrt(ms*ms+mr*mr+hl*hl)
			_BB = math.sqrt(by*by+bb*bb)
			_BG = bg
			_UN = st
			_Gen = gn
			_MCT = mct
			_BT = math.sqrt(bt*bt+btm*btm)
			# _OT = math.sqrt(lu*lu+pu*pu+hl*hl+mt*mt)

			_OT = quadsum([pu,bg,lu,bt,btm,ms,mr,hl,mt])


			JJ.SetBinContent(nbin,_JJ)
			MM.SetBinContent(nbin,_MM)
			BG.SetBinContent(nbin,_BG)
			UN.SetBinContent(nbin,_UN)
			Gen.SetBinContent(nbin,_Gen)
			BT.SetBinContent(nbin,_BT)
			OT.SetBinContent(nbin,_OT)
			BB.SetBinContent(nbin,_BB)
			MCT.SetBinContent(nbin,_MCT)
			# allvals+= [_JJ,_MM,_BG,_UN,_Gen,_BT,_OT]

			allvals += [_JJ,_Gen,_UN,_MCT,_OT,_T]
		colors = [1,2,4,6,28,7,8,9]
		styles = [1,2,4,5,3,6,7,8]

		# histos = [T,JJ,MM,BG,UN,Gen,BT,OT]
		histos = [T,JJ,Gen,UN,MCT,OT]

		# gROOT.SetStyle('Plain')  # Plain white default for plots
		gStyle.SetOptTitle(0) # No titles
		gStyle.SetOptStat(0) # No titles


		c1 = TCanvas("c1","",700,800)
		c1.cd(1).SetTopMargin(0.1)

		plotmin = min(allvals)*0.8
		print plotmin
		if plotmin < 0.1:
			plotmin = 0.1
		plotmax = max(allvals)
		plotmax *= 50
		c1.cd(1).SetLogy()


		for x in range(len(histos)):
			histos[x].SetLineColor(colors[x])
			histos[x].SetMarkerColor(colors[x])
			histos[x].SetLineStyle(styles[x])
			histos[x].GetXaxis().SetTitle(label)
			histos[x].SetMarkerSize(0.0)
			histos[x].GetYaxis().SetTitle("Uncertainty [%]")
			histos[x].SetMinimum(plotmin)
			histos[x].SetMaximum(plotmax)
			histos[x].SetLineWidth(2)
			histos[x].GetXaxis().SetNdivisions(110)
			
			histos[x].Draw("HIST"+"SAME"*(x!=0))



		FixDrawLegend(c1.cd(1).BuildLegend( 0.7,  0.64,  0.95,  0.88,'' ))

		sqrts = "#sqrt{s} = 7 TeV";
		l1=TLatex()
		l1.SetTextAlign(12)
		l1.SetTextFont(42)
		l1.SetNDC()
		l1.SetTextSize(0.05)
		# l1.DrawLatex(0.15,0.90,"CMS Preliminary                         "+sqrts+"                        L_{int} = 5.0 fb^{-1}")
		# l1.DrawLatex(0.2,0.84,"CMS ")
		l1.DrawLatex(0.18,0.94,"CMS        "+sqrts+"         L_{int} = 5.0 fb^{-1}")

		pdf = afile.replace('.tex','.pdf')
		png = afile.replace('.tex','.png')
		c1.Print(pdf)
		c1.Print(png)

	for f in files:
		AnalyzeFile(f)

	for f in files:
		AnalyzeFile(f)	

	print ' '


setTDRStyle()


main()


print 'Time to completion:',(datetime.now()-startTime)




