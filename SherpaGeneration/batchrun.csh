#!/bin/csh
setenv SCRAM_ARCH slc5_amd64_gcc462
cd /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_6_0_1/src
cmsenv
cd -
cp /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_6_0_1/src/sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.py .
sed -i 's/123/NUMEVENT/g' sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.py
sed -i 's/456/RANDTAG/g'  sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.py
cp /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_6_0_1/src/sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER.tgz .

cmsRun sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.py
mv sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.root SherpaGEN_7TeV_Wleptonic_0j4incl_2mlnu7000_RANDTAG_NUMEVENT.root
xrdcp SherpaGEN_7TeV_Wleptonic_0j4incl_2mlnu7000_RANDTAG_NUMEVENT.root root://eoscms//eos/cms/store/group/phys_smp/WPlusJets/Sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000/SherpaGEN_7TeV_Wleptonic_0j4incl_2mlnu7000_RANDTAG_NUMEVENT.root

