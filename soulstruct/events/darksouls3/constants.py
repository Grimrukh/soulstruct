import soulstruct.types as gt

class COMMON:
    file_name = 'common'

class COMMON_FUNC:
    file_name = 'common_func'


HIGH_WALL_OF_LOTHRIC = gt.Map(30, 0)
LOTHRIC_CASTLE = CONSUMED_KINGS_GARDEN = gt.Map(30, 1)
UNDEAD_SETTLEMENT = gt.Map(31, 0)
ARCHDRAGON_PEAK = gt.Map(32, 0)
ROAD_OF_SACRIFICES = FARRON_KEEP = gt.Map(33, 0)
GRAND_ARCHIVES = gt.Map(34, 1)
CATHEDRAL_OF_THE_DEEP = gt.Map(35, 0)
IRITHYLL = IRITHYLL_OF_THE_BOREAL_VALLEY = ANOR_LONDO = gt.Map(37, 0)
CATACOMBS_OF_CARTHUS = SMOULDERING_LAKE = DEMON_RUINS = gt.Map(38, 0)
IRITHYLL_DUNGEON = PROFANED_CAPITAL = gt.Map(39, 0)
CEMETERY_OF_ASH = FIRELINK_SHRINE = UNTENDED_GRAVES = gt.Map(40, 0)
KILN_OF_THE_FIRST_FLAME = gt.Map(41, 0)
PAINTED_WORLD_OF_ARIANDEL = gt.Map(45, 0)
ARENA_GRAND_ROOF = gt.Map(46, 0)
ARENA_KILN_OF_FLAME = gt.Map(47, 0)
DREG_HEAP = gt.Map(50, 0)
RINGED_CITY = gt.Map(51, 0)
ARENA_DRAGON_RUINS = gt.Map(53, 0)
ARENA_ROUND_PLAZA = gt.Map(54, 0)

ALL_MAPS = [COMMON, COMMON_FUNC, HIGH_WALL_OF_LOTHRIC, LOTHRIC_CASTLE, UNDEAD_SETTLEMENT, ARCHDRAGON_PEAK, FARRON_KEEP,
            GRAND_ARCHIVES, CATHEDRAL_OF_THE_DEEP, IRITHYLL, CATACOMBS_OF_CARTHUS, IRITHYLL_DUNGEON, FIRELINK_SHRINE,
            KILN_OF_THE_FIRST_FLAME, PAINTED_WORLD_OF_ARIANDEL, DREG_HEAP, RINGED_CITY, ARENA_GRAND_ROOF,
            ARENA_KILN_OF_FLAME, ARENA_DRAGON_RUINS, ARENA_ROUND_PLAZA]

MAP_NAMES = {
    (30, 0): "HIGH_WALL_OF_LOTHRIC",
    (30, 1): "LOTHRIC_CASTLE",
    (31, 0): "UNDEAD_SETTLEMENT",
    (32, 0): "ARCHDRAGON_PEAK",
    (33, 0): "FARRON_KEEP",
    (34, 1): "GRAND_ARCHIVES",
    (35, 0): "CATHEDRAL_OF_THE_DEEP",
    (37, 0): "IRITHYLL",
    (38, 0): "CATACOMBS_OF_CARTHUS",
    (39, 0): "IRITHYLL_DUNGEON",
    (40, 0): "FIRELINK_SHRINE",
    (41, 0): "KILN_OF_THE_FIRST_FLAME",
    (45, 0): "PAINTED_WORLD_OF_ARIANDEL",
    (50, 0): "DREG_HEAP",
    (51, 0): "RINGED_CITY",
    (46, 0): "ARENA_GRAND_ROOF",
    (47, 0): "ARENA_KILN_OF_FLAME",
    (53, 0): "ARENA_DRAGON_RUINS",
    (54, 0): "ARENA_ROUND_PLAZA",
}

VERBOSE_MAP_NAMES = {
    (30, 0): "High Wall of Lothric",
    (30, 1): "Lothric Castle",
    (31, 0): "Undead Settlement",
    (32, 0): "Archdragon Peak",
    (33, 0): "Road of Sacrifices/Farron Keep",
    (34, 1): "Grand Archives",
    (35, 0): "Cathedral of the Deep",
    (37, 0): "Irithyll of the Boreal Valley/Anor Londo",
    (38, 0): "Catacombs of Carthus",
    (39, 0): "Irithyll Dungeon/Profaned Capital",
    (40, 0): "Firelink Shrine",
    (41, 0): "Kiln of the First Flame",
    (45, 0): "Painted World of Ariandel",
    (50, 0): "Dreg Heap",
    (51, 0): "Ringed City",
    (46, 0): "Arena (Grand Roof)",
    (47, 0): "Arena (Kiln of Flame)",
    (53, 0): "Arena (Dragon Ruins)",
    (54, 0): "Arena (Round Plaza)",
}


class FLAG(gt.Flag):
    pass


class CHR(gt.Character):
    PrinceLorianWithoutLothric = 3410832
    PrinceLorianWithLothric = 3410830
    PrinceLothric = 3410831


class TEXT(gt.Text):
    PrinceLorianName = 905250
    PrinceLothicName = 905251


class SOUND(gt.SFXSound):
    BossDeath = 777777777


EVENT_NAMES = {
    13415830: "StartTwinPrincesBossFight",
    13415841: "MoveLothricToLorian",
    13410832: "TwinPrincesDeath",

    # Common functions. These event IDs are generally contiguous, so I assume they don't use flags.

    # Numerous variants of AI triggers. All of them trigger AI, and all of them trigger if the character in question is
    # attacked. The variants allow you to trigger them based on a radius from the player and/or when the player enters a
    # region, with an optional animation, with or without the addition of a gravity trigger (e.g. for falling slimes) or
    # a forced animation. There's also one that triggers if an arbitrary character's AI is in the Battle state, and one
    # that triggers on attack only (e.g. a sleeping enemy).
    20005110: "TriggerAIWithRegion",
    20005111: "TriggerAIAndAnimationWithRegion",
    20005112: "TriggerAIAndGravityWithRegion",
    20005113: "TriggerAIAndGravityWithRegionAfterDelay",
    20005114: "TriggerAIWithRegionAfterDelay",
    20005119: "TriggerAIWithRegions",
    20005120: "TriggerAIWithinDistance",
    20005121: "TriggerAIWithinDistanceAfterDelay",
    20005122: "TriggerAIAndAnimationWithinDistance",
    20005130: "TriggerAIWithinDistanceAndRegion",
    20005131: "TriggerAIAndAnimationWithinDistanceOrRegion",
    20005132: "TriggerAIWithinDistanceOrRegion",
    20005133: "TriggerAIAndAnimationWithinDistanceOrRegion",
    20005134: "TriggerAIWithinDistanceOrRegionWithAnimationInRegionOnly",
    20005140: "TriggerAIWithinRegionOrIfCharacterIsFighting",
    20005150: "TriggerAIOnAttackOnly",

    20005192: "RemoveSpEffect99006WithinRegion",
    20005190: "RemoveSpEffect99006WithinDistance",
    20005191: "RemoveSpEffect99006OnAttackOnly",

    20005200: "InterruptAnimationWithinRegion",


    20005350: "AwardItemLotOnCharacterDeath",
    20005530: "BurnObject",
    20005611: "EnableFlagWhenObjectActivated",
}
