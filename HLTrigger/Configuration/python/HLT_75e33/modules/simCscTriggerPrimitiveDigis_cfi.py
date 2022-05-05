import FWCore.ParameterSet.Config as cms

simCscTriggerPrimitiveDigis = cms.EDProducer("CSCTriggerPrimitivesProducer",
    CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi"),
    CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi"),
    GEMPadDigiClusterProducer = cms.InputTag("simMuonGEMPadDigiClusters"),
    GEMPadDigiProducer = cms.InputTag("simMuonGEMPadDigis"),
    MaxBX = cms.int32(11),
    MinBX = cms.int32(5),
    alctParam07 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    alctSLHC = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctSLHCME21 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(1),
        alctGhostCancellationSideQuality = cms.bool(True),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(True),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(3),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(0),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    alctSLHCME3141 = cms.PSet(
        alctAccelMode = cms.uint32(0),
        alctDriftDelay = cms.uint32(2),
        alctEarlyTbins = cms.int32(4),
        alctFifoPretrig = cms.uint32(10),
        alctFifoTbins = cms.uint32(16),
        alctGhostCancellationBxDepth = cms.int32(4),
        alctGhostCancellationSideQuality = cms.bool(False),
        alctHitPersist = cms.uint32(6),
        alctL1aWindowWidth = cms.uint32(7),
        alctNarrowMaskForR1 = cms.bool(False),
        alctNplanesHitAccelPattern = cms.uint32(4),
        alctNplanesHitAccelPretrig = cms.uint32(3),
        alctNplanesHitPattern = cms.uint32(4),
        alctNplanesHitPretrig = cms.uint32(3),
        alctPretrigDeadtime = cms.uint32(4),
        alctTrigMode = cms.uint32(2),
        alctUseCorrectedBx = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    checkBadChambers = cms.bool(False),
    clctParam07 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(10),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctStartBxShift = cms.int32(0),
        useComparatorCodes = cms.bool(False),
        useRun3Patterns = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctSLHC = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(3),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        clctUseCorrectedBx = cms.bool(False),
        useComparatorCodes = cms.bool(False),
        useDeadTimeZoning = cms.bool(True),
        useDynamicStateMachineZone = cms.bool(True),
        useRun3Patterns = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctSLHCME21 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(3),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        clctUseCorrectedBx = cms.bool(False),
        useComparatorCodes = cms.bool(False),
        useDeadTimeZoning = cms.bool(True),
        useDynamicStateMachineZone = cms.bool(False),
        useRun3Patterns = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    clctSLHCME3141 = cms.PSet(
        clctDriftDelay = cms.uint32(2),
        clctFifoPretrig = cms.uint32(7),
        clctFifoTbins = cms.uint32(12),
        clctHitPersist = cms.uint32(4),
        clctMinSeparation = cms.uint32(5),
        clctNplanesHitPattern = cms.uint32(4),
        clctNplanesHitPretrig = cms.uint32(3),
        clctPidThreshPretrig = cms.uint32(2),
        clctPretriggerTriggerZone = cms.uint32(224),
        clctStartBxShift = cms.int32(0),
        clctStateMachineZone = cms.uint32(4),
        clctUseCorrectedBx = cms.bool(False),
        useComparatorCodes = cms.bool(False),
        useDeadTimeZoning = cms.bool(True),
        useDynamicStateMachineZone = cms.bool(False),
        useRun3Patterns = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    commonParam = cms.PSet(
        alctClctOffset = cms.uint32(1),
        disableME1a = cms.bool(False),
        disableME42 = cms.bool(False),
        enableAlctSLHC = cms.bool(True),
        gangedME1a = cms.bool(False),
        isSLHC = cms.bool(True),
        runME11ILT = cms.bool(True),
        runME11Up = cms.bool(True),
        runME21ILT = cms.bool(True),
        runME21Up = cms.bool(True),
        runME31Up = cms.bool(True),
        runME41Up = cms.bool(True),
        useClusters = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    copadParamGE11 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(2),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    copadParamGE21 = cms.PSet(
        maxDeltaBX = cms.uint32(0),
        maxDeltaPad = cms.uint32(2),
        maxDeltaRoll = cms.uint32(1),
        verbosity = cms.uint32(0)
    ),
    debugParameters = cms.bool(True),
    me11tmbSLHCGEM = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        buildLCTfromALCTandGEM_ME1a = cms.bool(False),
        buildLCTfromALCTandGEM_ME1b = cms.bool(True),
        buildLCTfromCLCTandGEM_ME1a = cms.bool(False),
        buildLCTfromCLCTandGEM_ME1b = cms.bool(True),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        debugLUTs = cms.bool(False),
        debugMatching = cms.bool(False),
        doLCTGhostBustingWithGEMs = cms.bool(False),
        dropLowQualityALCTsNoGEMs_ME1a = cms.bool(False),
        dropLowQualityALCTsNoGEMs_ME1b = cms.bool(False),
        dropLowQualityCLCTsNoGEMs_ME1a = cms.bool(False),
        dropLowQualityCLCTsNoGEMs_ME1b = cms.bool(True),
        matchEarliestAlctOnly = cms.bool(False),
        matchEarliestClctOnly = cms.bool(False),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(3),
        maxDeltaBXCoPad = cms.int32(1),
        maxDeltaBXPad = cms.int32(1),
        maxDeltaPadL1Even = cms.int32(12),
        maxDeltaPadL1Odd = cms.int32(24),
        maxDeltaPadL2Even = cms.int32(12),
        maxDeltaPadL2Odd = cms.int32(24),
        maxLCTs = cms.uint32(2),
        mpcBlockMe1a = cms.uint32(0),
        promoteALCTGEMpattern = cms.bool(True),
        promoteALCTGEMquality = cms.bool(True),
        promoteCLCTGEMquality_ME1a = cms.bool(True),
        promoteCLCTGEMquality_ME1b = cms.bool(True),
        tmbCrossBxAlgorithm = cms.uint32(2),
        tmbDropUsedAlcts = cms.bool(False),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(False),
        useHighMultiplicityBits = cms.bool(False),
        useOldLCTDataFormat = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    me21tmbSLHCGEM = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        buildLCTfromALCTandGEM = cms.bool(True),
        buildLCTfromCLCTandGEM = cms.bool(True),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        debugLUTs = cms.bool(False),
        debugMatching = cms.bool(False),
        doLCTGhostBustingWithGEMs = cms.bool(False),
        dropLowQualityALCTsNoGEMs = cms.bool(True),
        dropLowQualityCLCTsNoGEMs = cms.bool(True),
        matchEarliestAlctOnly = cms.bool(False),
        matchEarliestClctOnly = cms.bool(False),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(3),
        maxDeltaBXCoPad = cms.int32(1),
        maxDeltaBXPad = cms.int32(1),
        maxDeltaPadL1Even = cms.int32(12),
        maxDeltaPadL1Odd = cms.int32(24),
        maxDeltaPadL2Even = cms.int32(12),
        maxDeltaPadL2Odd = cms.int32(24),
        maxLCTs = cms.uint32(2),
        mpcBlockMe1a = cms.uint32(0),
        promoteALCTGEMpattern = cms.bool(True),
        promoteALCTGEMquality = cms.bool(True),
        promoteCLCTGEMquality = cms.bool(True),
        tmbCrossBxAlgorithm = cms.uint32(2),
        tmbDropUsedAlcts = cms.bool(False),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(False),
        useHighMultiplicityBits = cms.bool(False),
        useOldLCTDataFormat = cms.bool(True),
        verbosity = cms.int32(0)
    ),
    meX1tmbSLHC = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        debugLUTs = cms.bool(False),
        debugMatching = cms.bool(False),
        matchEarliestAlctOnly = cms.bool(False),
        matchEarliestClctOnly = cms.bool(False),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(3),
        maxLCTs = cms.uint32(2),
        mpcBlockMe1a = cms.uint32(0),
        tmbCrossBxAlgorithm = cms.uint32(2),
        tmbDropUsedAlcts = cms.bool(False),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(False),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    mpcRun2 = cms.PSet(
        dropInvalidStubs = cms.bool(False),
        dropLowQualityStubs = cms.bool(False),
        sortStubs = cms.bool(False)
    ),
    savePreTriggers = cms.bool(False),
    tmbParam = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(7),
        mpcBlockMe1a = cms.uint32(0),
        tmbDropUsedAlcts = cms.bool(True),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(True),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    tmbSLHC = cms.PSet(
        alctTrigEnable = cms.uint32(0),
        clctToAlct = cms.bool(False),
        clctTrigEnable = cms.uint32(0),
        debugLUTs = cms.bool(False),
        debugMatching = cms.bool(False),
        ignoreAlctCrossClct = cms.bool(False),
        matchEarliestAlctOnly = cms.bool(False),
        matchEarliestClctOnly = cms.bool(False),
        matchTrigEnable = cms.uint32(1),
        matchTrigWindowSize = cms.uint32(3),
        maxLCTs = cms.uint32(2),
        mpcBlockMe1a = cms.uint32(0),
        tmbCrossBxAlgorithm = cms.uint32(1),
        tmbDropUsedAlcts = cms.bool(False),
        tmbDropUsedClcts = cms.bool(False),
        tmbEarlyTbins = cms.int32(4),
        tmbL1aWindowSize = cms.uint32(7),
        tmbReadoutEarliest2 = cms.bool(False),
        useHighMultiplicityBits = cms.bool(False),
        verbosity = cms.int32(0)
    ),
    writeOutAllALCTs = cms.bool(False),
    writeOutAllCLCTs = cms.bool(False)
)
