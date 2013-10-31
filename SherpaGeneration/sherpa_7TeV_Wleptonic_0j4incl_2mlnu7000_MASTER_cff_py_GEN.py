# Auto generated configuration file
# using: 
# Revision: 1.400 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/SherpaWork/sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff.py -s GEN -n 100 --no_exec --conditions auto:mc --eventcontent RAWSIM
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.RandomNumberGeneratorService.generator.initialSeed=456

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(123)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.400 $'),
    annotation = cms.untracked.string('Configuration/SherpaWork/sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff.py nevts:100'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('sherpa_7TeV_Wleptonic_0j4incl_2mlnu7000_MASTER_cff_py_GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("SherpaGeneratorFilter",
    SherpaProcess = cms.string('7TeV_Wleptonic_0j4incl_2mlnu7000'),
    SherpaParameters = cms.PSet(
        parameterSets = cms.vstring('Run'),
        Run = cms.vstring('(run){', 
            ' EVENTS = 1000;', 
            ' EVENT_MODE = HepMC;', 
            ' # avoid comix re-init after runcard modification', 
            ' WRITE_MAPPING_FILE 3;', 
            '}(run)', 
            '(beam){', 
            ' BEAM_1 = 2212; BEAM_ENERGY_1 = 3500.;', 
            ' BEAM_2 = 2212; BEAM_ENERGY_2 = 3500.;', 
            '}(beam)', 
            '(processes){', 
            ' Process 93 93 -> 90 91 93{4};', 
            ' Order_EW 2;', 
            ' Enhance_Factor 2 {3};', 
            ' Enhance_Factor 35 {4};', 
            ' Enhance_Factor 40 {5};', 
            ' Enhance_Factor 50 {6};', 
            ' CKKW sqr(20./E_CMS);', 
            ' Integration_Error 0.02 {5,6};', 
            ' End process;', 
            '}(processes)', 
            '(selector){', 
            ' Mass  90 91 2. E_CMS;', 
            '}(selector)', 
            '(integration){', 
            ' FINISH_OPTIMIZATION = Off', 
            '}(integration)', 
            '(isr){', 
            ' PDF_LIBRARY     = LHAPDFSherpa', 
            ' PDF_SET         = CT10.LHgrid', 
            ' PDF_SET_VERSION = 0', 
            ' PDF_GRID_PATH   = PDFsets', 
            '}(isr)', 
            '(me){', 
            ' ME_SIGNAL_GENERATOR = Internal Comix', 
            ' EVENT_GENERATION_MODE = Unweighted;', 
            '}(me)', 
            '(mi){', 
            ' MI_HANDLER = Amisic  # None or Amisic', 
            '}(mi)')
    ),
    filterEfficiency = cms.untracked.double(1.0),
    FetchSherpack = cms.bool(False),
    SherpackChecksum = cms.string('c010a65685b81568788df7160dd47f21'),
    SherpaResultDir = cms.string('Result'),
    SherpaPath = cms.string('./'),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.int32(0),
    SherpaPathPiece = cms.string('./'),
    SherpackLocation = cms.string('./'),
    SherpaDefaultWeight = cms.double(1.0)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

