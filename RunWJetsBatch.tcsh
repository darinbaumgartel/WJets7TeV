#!/bin/tcsh


# cd /afs/cern.ch/user/d/darinb/CMSSW_5_0_1/src
# # setenv SCRAM_ARCH slc5_amd64_gcc462
# # cd /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_6_0_1/src
# #cd /afs/cern.ch/user/d/darinb/CMSSW_5_3_4/src
# cmsenv
# cd /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_4_2_8/src/WJetsAnalysis
# python WJetsTreeAnalyzer.py


cd /afs/cern.ch/user/d/darinb/CMSSW_5_0_1/src
cmsenv
cd -
cp /afs/cern.ch/work/d/darinb/WAnalysis/CMSSW_4_2_8/src/WJetsAnalysis/WJetsTreeAnalyzer.py .

mkdir ResDir
mkdir OutDir

python WJetsTreeAnalyzer.py

rm OutDir/*root

cp OutDir/* AFSDir/
