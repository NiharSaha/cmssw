import FWCore.ParameterSet.Config as cms
    
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
ecalPreshowerFEDIntegrityTask = DQMEDAnalyzer('ESFEDIntegrityTask',
                                               prefixME = cms.untracked.string('EcalPreshower'),
                                               ESDCCCollections = cms.untracked.InputTag("ecalPreshowerDigis"),
                                               ESKChipCollections = cms.untracked.InputTag("ecalPreshowerDigis"),
                                               FEDRawDataCollection = cms.untracked.InputTag("rawDataCollector"),
                                               OutputFile = cms.untracked.string(""),
                                               FEDDirName =cms.untracked.string("FEDIntegrity")
                                               )

