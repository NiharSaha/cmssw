import FWCore.ParameterSet.Config as cms

    
from DQMServices.Core.DQMEDAnalyzer import DQMEDAnalyzer
ecalPreshowerOccupancyTask = DQMEDAnalyzer('ESOccupancyTask',
	RecHitLabel = cms.untracked.InputTag("ecalPreshowerRecHit","EcalRecHitsES"),
	DigiLabel = cms.untracked.InputTag("ecalPreshowerDigis"),
	prefixME = cms.untracked.string("EcalPreshower") 
)

