import FWCore.ParameterSet.Config as cms

ticlTrackstersHAD = cms.EDProducer("TrackstersProducer",
    detector = cms.string('HGCAL'),
    filtered_mask = cms.InputTag("filteredLayerClustersHAD","HAD"),
    itername = cms.string('HAD'),
    layer_clusters = cms.InputTag("hgcalLayerClusters"),
    layer_clusters_hfnose_tiles = cms.InputTag("ticlLayerTileHFNose"),
    layer_clusters_tiles = cms.InputTag("ticlLayerTileProducer"),
    mightGet = cms.optional.untracked.vstring,
    original_mask = cms.InputTag("ticlTrackstersTrk"),
    patternRecognitionBy = cms.string('CA'),
    pluginPatternRecognitionByCA = cms.PSet(
        algo_verbosity = cms.int32(0),
        eid_input_name = cms.string('input'),
        eid_min_cluster_energy = cms.double(1),
        eid_n_clusters = cms.int32(10),
        eid_n_layers = cms.int32(50),
        eid_output_name_energy = cms.string('output/regressed_energy'),
        eid_output_name_id = cms.string('output/id_probabilities'),
        energy_em_over_total_threshold = cms.double(-1),
        etaLimitIncreaseWindow = cms.double(2.1),
        filter_on_categories = cms.vint32(0),
        max_delta_time = cms.double(-1),
        max_longitudinal_sigmaPCA = cms.double(9999),
        max_missing_layers_in_trackster = cms.int32(9999),
        max_out_in_hops = cms.int32(10),
        min_cos_pointing = cms.double(0.819),
        min_cos_theta = cms.double(0.866),
        min_layers_per_trackster = cms.int32(12),
        oneTracksterPerTrackSeed = cms.bool(False),
        out_in_dfs = cms.bool(True),
        pid_threshold = cms.double(0),
        promoteEmptyRegionToTrackster = cms.bool(False),
        root_doublet_max_distance_from_seed_squared = cms.double(9999),
        shower_start_max_layer = cms.int32(9999),
        siblings_maxRSquared = cms.vdouble(0.0006, 0.0006, 0.0006),
        skip_layers = cms.int32(1),
        type = cms.string('CA')
    ),
    pluginPatternRecognitionByCLUE3D = cms.PSet(
        algo_verbosity = cms.int32(0),
        criticalDensity = cms.double(4),
        criticalEtaPhiDistance = cms.double(0.035),
        densityEtaPhiDistanceSqr = cms.double(0.0008),
        densityOnSameLayer = cms.bool(False),
        densitySiblingLayers = cms.int32(3),
        eid_input_name = cms.string('input'),
        eid_min_cluster_energy = cms.double(1),
        eid_n_clusters = cms.int32(10),
        eid_n_layers = cms.int32(50),
        eid_output_name_energy = cms.string('output/regressed_energy'),
        eid_output_name_id = cms.string('output/id_probabilities'),
        minNumLayerCluster = cms.int32(5),
        outlierMultiplier = cms.double(2),
        type = cms.string('CLUE3D')
    ),
    pluginPatternRecognitionByFastJet = cms.PSet(
        algo_verbosity = cms.int32(0),
        antikt_radius = cms.double(0.09),
        eid_input_name = cms.string('input'),
        eid_min_cluster_energy = cms.double(1),
        eid_n_clusters = cms.int32(10),
        eid_n_layers = cms.int32(50),
        eid_output_name_energy = cms.string('output/regressed_energy'),
        eid_output_name_id = cms.string('output/id_probabilities'),
        minNumLayerCluster = cms.int32(5),
        type = cms.string('FastJet')
    ),
    seeding_regions = cms.InputTag("ticlSeedingGlobal"),
    time_layerclusters = cms.InputTag("hgcalLayerClusters","timeLayerCluster")
)

