import FWCore.ParameterSet.Config as cms
    
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
ecalPreshowerTrendTask = DQMEDAnalyzer('ESTrendTask',
                                        RecHitLabel = cms.untracked.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
                                        ESDCCCollections = cms.untracked.InputTag("ecalPreshowerDigis"),
                                        prefixME = cms.untracked.string("EcalPreshower") 
                                        )

