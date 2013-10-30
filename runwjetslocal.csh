

# JUST RUN THESE COMMANDS. Make sure to cmsenv before you run anything!

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9  

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_JetScaleUp --jetscale 1.04

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_JetScaleDown --jetscale 0.96

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_MuScaleUp --muscale 1.002

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_MuScaleDown --muscale 0.998

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_JetSmear --jetres 1.0

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_MuSmear --mures 0.006


python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_Oct9_MetPhiMod --phicorr  




