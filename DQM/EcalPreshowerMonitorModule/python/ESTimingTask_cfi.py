import FWCore.ParameterSet.Config as cms

from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
ecalPreshowerTimingTask = DQMEDAnalyzer('ESTimingTask',
	RecHitLabel = cms.untracked.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
	DigiLabel = cms.untracked.InputTag("ecalPreshowerDigis"),
	prefixME = cms.untracked.string("EcalPreshower") 
)

