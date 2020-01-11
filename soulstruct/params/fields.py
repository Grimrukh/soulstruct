from functools import partial

from .enums import *

__all__ = ['PARAM_NICKNAMES', 'GAME_PARAM_INFO']

# Overrides for certain basic enums.
ATK_PARAM_HIT_SOURCE = int
SP_EFFECT_SPCATEGORY = int

ATK_PARAM_BOOL = bool
EQUIP_BOOL = bool
MAGIC_BOOL = bool
NPC_BOOL = bool
NPC_THINK_REPLY_BEHAVIOR_TYPE = bool
ON_OFF = bool
RAGDOLL_PARAM_BOOL = bool
SP_EFFECT_BOOL = bool
THROW_ENABLE_STATE = bool


class AI:
    Logic = '<AI:Logic>'
    Battle = '<AI:Battle>'


Animation = '<Animation>'
Flag = '<Flag>'
Model = '<Model>'
Texture = '<Texture>'
VisualEffect = '<VisualEffect>'


class Params:
    AI = '<Params:AI>'
    Armor = '<Params:Armor>'
    ArmorUpgrades = '<Params:ArmorUpgrades>'
    Attacks = '<Params:Attacks>'  # links to both Human and Non Human Attacks are provided
    Behaviors = '<Params:Behaviors>'  # links to both Human and Non Human Behaviors are provided
    Bosses = '<Params:Bosses>'
    Bullets = '<Params:Bullets>'
    Cameras = '<Params:Cameras>'
    Conversations = '<Params:Conversations>'
    Faces = '<Params:Faces>'
    Goods = '<Params:Goods>'
    ItemLots = '<Params:ItemLots>'
    Knockback = '<Params:Knockback>'
    LevelSyncCorrect = '<Params:LevelSyncCorrect>'
    Movement = '<Params:Movement>'
    Rings = '<Params:Rings>'
    SpecialEffects = '<Params:SpecialEffects>'
    Spells = '<Params:Spells>'
    Terrains = '<Params:Terrains>'
    SpecialEffectVisuals = '<Params:SpecialEffectVisuals>'
    UpgradeMaterials = '<Params:UpgradeMaterials>'
    Weapons = '<Params:Weapons>'
    WeaponUpgrades = '<Params:WeaponUpgrades>'


class Sound:
    SFX = '<Sound:SFX>'
    Voice = '<Sound:Voice>'


class Text:
    Conversations = '<Text:Conversations>'
    EventText = '<Text:EventText>'
    NPCNames = '<Text:NPCNames>'


def _behavior_ref_id(behavior_param_entry):
    if behavior_param_entry['refType'] == BEHAVIOR_REF_TYPE.Default:
        return ('Attack', True, Params.Attacks,
                "Attack ID triggered by behavior.")
    elif behavior_param_entry['refType'] == BEHAVIOR_REF_TYPE.Bullet:
        return ('Bullet', True, Params.Bullets,
                "Bullet ID triggered by behavior.")
    elif behavior_param_entry['refType'] == BEHAVIOR_REF_TYPE.SpecialEffect:
        return ('SpecialEffect', True, Params.SpecialEffects,
                "Special Effect ID triggered by behavior. (Never used; may not work.)")
    else:
        return ('UnknownReferenceID', True, int,
                "Could not determine reference ID type (usually Attack or Bullet).")


def _good_ref_id(goods_param_entry):
    if goods_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.Default:
        return ('NoReference', True, int,
                "This value should be -1 when 'Default' reference type is selected.")
    elif goods_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.Bullet:
        return ('Bullet', True, Params.Bullets,
                "Bullet triggered by using good (which may simply be targeted at self).")
    elif goods_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.SpecialEffect:
        return ('SpecialEffect', True, Params.SpecialEffects,
                "Special effect triggered (on self) by using good.")
    else:
        return ('UnknownReferenceID', True, int,
                "Could not determine reference ID type (usually Bullet or SpecialEffect).")


def _spells_ref_id(spells_param_entry):
    if spells_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.Default:
        return ('NoReference', True, int,
                "This value should be -1 when 'Default' reference type is selected.")
    elif spells_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.Bullet:
        return ('Bullet', True, Params.Bullets,
                "Bullet triggered by casting spell (which may simply be targeted at self).")
    elif spells_param_entry['refCategory'] == BEHAVIOR_REF_TYPE.SpecialEffect:
        return ('SpecialEffect', True, Params.SpecialEffects,
                "Special effect triggered (on self) by casting spell.")
    else:
        return ('UnknownReferenceID', True, int,
                "Could not determine reference ID type (usually Bullet or SpecialEffect).")


def _obj_act_success_condition(condition_field_name, obj_act_param_entry):
    n = '2' if condition_field_name.endswith('2') else '1'
    if obj_act_param_entry[condition_field_name] == OBJACT_SP_QUALIFIED_TYPE.NoCondition:
        return (f'NoCondition{n}', True, int,
                f"No condition type selected.")
    elif obj_act_param_entry[condition_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasGood:
        return (f'RequiredGood{n}', True, Params.Goods,
                f"Condition: object action will succeed if user has this good in their inventory (does not "
                "include Bottomless Box).")
    elif obj_act_param_entry[condition_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasSpecialEffect:
        return (f'RequiredSpecialEffect{n}', True, Params.SpecialEffects,
                "Condition: object action will succeed if user has this special effect.")
    else:
        return (f'UnknownCondition{n}', True, int,
                "Could not determine success condition ID type (usually HasGood or HasSpecialEffect).")


def _item_lot_item_id(item_lot_slot: int, item_lot_param_entry):
    item_type = item_lot_param_entry[f'lotItemCategory0{item_lot_slot}']
    if item_type == ITEMLOT_ITEMCATEGORY.Weapon:
        return (f'ItemSlot{item_lot_slot}', True, Params.Weapons,
                f"Item slot {item_lot_slot} (Weapon).")
    elif item_type == ITEMLOT_ITEMCATEGORY.Armor:
        return (f'ItemSlot{item_lot_slot}', True, Params.Armor,
                f"Item slot {item_lot_slot} (Armor).")
    elif item_type == ITEMLOT_ITEMCATEGORY.Ring:
        return (f'ItemSlot{item_lot_slot}', True, Params.Rings,
                f"Item slot {item_lot_slot} (Ring).")
    elif item_type == ITEMLOT_ITEMCATEGORY.Good:
        return (f'ItemSlot{item_lot_slot}', True, Params.Goods,
                f"Item slot {item_lot_slot} (Good).")
    else:
        return (f'ItemSlot{item_lot_slot}', True, int,
                f"Item slot {item_lot_slot} (unknown item type {item_type}).")


def _shop_item_id(shops_param_entry):
    item_type = shops_param_entry[f'equipType']
    if item_type == SHOP_LINEUP_EQUIPTYPE.Weapon:
        return (f'Weapon', True, Params.Weapons,
                f"Weapon to be listed in shop menu.")
    if item_type == SHOP_LINEUP_EQUIPTYPE.Armor:
        return (f'Armor', True, Params.Armor,
                f"Armor to be listed in shop menu.")
    if item_type == SHOP_LINEUP_EQUIPTYPE.Ring:
        return (f'Ring', True, Params.Rings,
                f"Ring to be listed in shop menu.")
    if item_type == SHOP_LINEUP_EQUIPTYPE.Good:
        return (f'Good', True, Params.Goods,
                f"Good to be listed in shop menu.")
    if item_type == SHOP_LINEUP_EQUIPTYPE.Spell:
        return (f'Spell', True, Params.Spells,
                f"Spell to be listed in attunement menu.")
    else:
        return (f'ItemID', True, int,
                f"Item to be listed in shop/attunement menu (unknown item type {item_type}).")


PARAM_NICKNAMES = {
    # Nicknames are per BND entry basename, not per internal param table name. Unused tables are commented out.
    'NpcThinkParam': 'AI',
    'EquipParamProtector': 'Armor',
    'ReinforceParamProtector': 'ArmorUpgrades',
    'GameAreaParam': 'Bosses',
    'Bullet': 'Bullets',  # note not 'BulletParam'
    # 'CalcCorrectGraph': 'CalcCorrectionGraph',
    'LockCamParam': 'Cameras',
    # 'default_EnemyBehaviorBank': 'DefaultEnemyBehavior',
    # 'default_AIStandardInfoBank': 'DefaultAIStandardInfoBank',
    'CharaInitParam': 'Players',
    'AtkParam_Pc': 'PlayerAttacks',
    'BehaviorParam_PC': 'PlayerBehaviors',
    'TalkParam': 'Dialogue',
    'FaceGenParam': 'Faces',
    'EquipParamGoods': 'Goods',
    'ItemLotParam': 'ItemLots',
    'KnockbackParam': 'Knockback',
    'MenuColorTableParam': 'MenuColors',
    'MoveParam': 'Movement',
    'NpcParam': 'NonPlayers',
    'AtkParam_Npc': 'NonPlayerAttacks',
    'BehaviorParam': 'NonPlayerBehaviors',
    'EquipParamAccessory': 'Rings',
    'ObjectParam': 'Objects',
    'ObjActParam': 'ObjectActivations',
    # 'QwcChange': 'QwcChange',
    # 'QwcJudge': 'QwcJudge',
    # 'RagdollParam': 'Ragdolls',
    'ShopLineupParam': 'Shops',
    # 'SkeletonParam': 'Skeletons',
    'SpEffectParam': 'SpecialEffects',
    'Magic': 'Spells',
    'HitMtrlParam': 'Terrains',
    'ThrowParam': 'Throws',
    'EquipMtrlSetParam': 'UpgradeMaterials',
    'SpEffectVfxParam': 'SpecialEffectVisuals',
    'EquipParamWeapon': 'Weapons',
    'ReinforceParamWeapon': 'WeaponUpgrades',

    'DofBank': 'DepthOfField',
    'EnvLightTexBank': 'EnvLightTex',
    'FogBank': 'Fog',
    'LensFlareBank': 'LensFlares',
    'LensFlareExBank': 'LensFlareSources',
    'LightBank': 'AmbientLight',
    'LightScatteringBank': 'ScatteredLight',
    'LodBank': 'Lod',  # default_DrawParam only
    'PointLightBank': 'PlayerLights',
    'ShadowBank': 'Shadows',
    'ToneCorrectBank': 'ToneCorrection',
    'ToneMapBank': 'ToneMapping',
    's_LightBank': 'DebugAmbientLight',
}

GAME_PARAM_INFO = {
    # PARAM_TABLE_NAME: (ParamEntryNickname, VisibleDefault, ParamTableType, Docstring)

    'NPC_THINK_PARAM_ST': {
        'logicId': (
            'Logic ID', True, AI.Logic,
            "ID of logic (non-battle) Lua script."),
        'battleGoalID': (
            'BattleID', True, AI.Battle,
            "Battle goal ID used to look up battle Lua script."),
        'nearDist': (
            'NearDistance', True, float,
            "Distance considered to be close range by this NPC (for scripts)."),
        'midDist': (
            'MidDistance', True, float,
            "Distance considered to be medium range by this NPC (for scripts)."),
        'farDist': (
            'FarDistance', True, float,
            "Distance considered to be long range by this NPC (for scripts)."),
        'outDist': (
            'OutOfRangeDistance', True, float,
            "Distance beyond which the NPC will not attempt to fight."),
        'BackHomeLife_OnHitEneWal': (
            'RetreatTimeAfterHittingEnemyWall', False, float,
            "Retreat goal time when touching an 'enemy wall' that blocks the NPC's path. "
            "(Not clear what an 'enemy wall' means. Almost always set to 5 (rarely 6)."),
        'goalID_ToCaution': (
            'CautionGoalID', True, AI.Logic,
            "Lua script to use when NPC's AI enters the 'Caution' state (I think). Requires a "
            "CautionGoalAction value of 4. Used only by Hawkeye Gough (411000); zero otherwise."),
        'idAttackCannotMove': (
            'StuckAnimationID', True, Animation,
            "Animation to use if the NPC gets stuck on a destructible object. Usually 3000 (basic "
            "attack)."),
        'goalID_ToFind': (
            'SearchGoalID', True, AI.Logic,
            "Lua script to use when NPC's AI enters the 'Search' state (I think). Requires a "
            "SearchGoalAction value of 4. Not used by any vanilla NPC (all zero)."),
        'callHelp_ActionAnimId': (
            'HelpCallResponseAnimation', True, Animation,
            "Animation to play when responding to a call for help. Usually set to -1 for NPCs "
            "who can reply to calls for help, which I assume means no animation is played. Set "
            "to 0 for NPCs who ignore calls for help."),
        'callHelp_CallActionId': (
            'HelpCallSendAnimation', True, Animation,
            "Animation to play when calling for help. Only used by Female Ghost (7300) and Male "
            "Ghost and summons (-1). I assume -1 means no animation is played. Set to 0 for all "
            "other NPCs."),
        'eye_dist': (
            'SightDistance', True, int,
            "Distance of NPC eyesight (in meters)."),
        'ear_dist': (
            'HearingDistance', True, int,
            "Distance of NPC hearing (in meters)."),
        'ear_soundcut_dist': (
            'HearingCutDistance', False, int,
            "Internal description: 'Distance to reduce the size of the sound source. Sounds less "
            "than this distance will not be heard.' Set to 1 for Bloatheads and Bloathead Sorcerers "
            "and 0 for everyone else."),
        'nose_dist': (
            'SmellDistance', True, int,
            "Distance of NPC smell (auto-detect)."),
        'maxBackhomeDist': (
            'MaxRetreatDistance', True, int,
            "Absolute furthest the NPC can travel from their nest before retreating, in or out of "
            "battle. (Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.) Usually set to "
            "about 50% more than BattleRetreatDistance."),
        'backhomeDist': (
            'BattleRetreatDistance', True, int,
            "Furthest distance the NPC can travel from their nest before retreating in battle. (Argument "
            "of internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'backhomeBattleDist': (
            'RetreatBattleStartDistance', True, int,
            "Target distance at which battle mode is triggered while the enemy is retreating. "
            "(Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'nonBattleActLife': (
            'NonBattleActLife', False, int,
            "Lifespan of Acts outside of battle. Set to 10 for Bloatheads and Bloathead Sorcerers, "
            "0 for Priscilla's Tail and the Bed of Chaos bug, and 5 for everyone else. (Argument of "
            "internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'BackHome_LookTargetTime': (
            'SearchTimeBeforeRetreat', True, int,
            "Time that NPC will search for a lost target before retreating (I think). Set to "
            "20 for everyone except the Bounding Demons of Izalith, who have a value of 0."),
        'BackHome_LookTargetDist': (
            'SearchDistanceBeforeRetreat', True, int,
            "Distance that NPC will search for a lost target before retreating (I think). Set "
            "to 20 for everyone except the Bounding Demons of Izaltih, who have a value of 0."),
        'SightTargetForgetTime': (
            'SightForgetTime', True, int,
            "Time to forget about sighted targets. Usually set to 600."),
        'SoundTargetForgetTime': (
            'HearingForgetTime', True, int,
            "Time to forget about heard targets. Usually set to 300."),
        'BattleStartDist': (
            'BattleStartDistance', True, int,
            "Target distance at which battle mode is triggered."),
        'callHelp_MyPeerId': (
            'HelpGroupID', True, int,
            "Determines which calls for help this NPC will respond to (must match caller's "
            "HelpCallGroupID). Only 0 (no ID) and 1 are used."),
        'callHelp_CallPeerId': (
            'HelpCallGroupID', True, int,
            "HelpGroupID value of NPCs who should respond to calls for help by this NPC. Only 0 "
            "(no ID) and 1 are used."),
        'targetSys_DmgEffectRate': (
            'TargetSysDamageRate', False, int,
            "Internal description: 'Get damage rate (%) for target system evaluation "
            "information.' Set to 0 for summons, phantoms, and the Parasitic Wall Hugger, and "
            "100 for everyone else."),
        'TeamAttackEffectivity': (
            'TeamAttackEffectivity', True, int,
            "Value from 0 to 100 that determines the number of simultaneous attacks made by this "
            "NPC's team. Higher values mean that less members of this team can participate in "
            "attacks at the same time. (I presume that the total score of attacking team members "
            "cannot exceed 100.) Usually set to 25 or 100."),
        # TODO: Apparently X is height and Y is width here. The internal descriptions or names may be incorrect.
        'eye_angX': (
            'SightRangeHeight', True, int,
            "Angular width of sight field in degrees."),
        'eye_angY': (
            'SightRangeWidth', True, int,
            "Angular height of sight field in degrees."),
        'ear_angX': (
            'HearingRangeHeight', True, int,
            "Angular width of hearing field in degrees."),
        'ear_angY': (
            'HearingRangeWidth', True, int,
            "Angular height of hearing field in degrees."),
        'callHelp_CallValidMinDistTarget': (
            'HelpCallTargetMinDistance', False, int,
            "Minimum distance from AI target for help call to be made. Always zero."),
        'callHelp_CallValidRange': (
            'HelpCallFriendMaxDistance', True, int,
            "Maximum distance of friend to receive help call from this NPC. Set to 50 for both "
            "Male and Female Ghosts, and 0 for everyone else."),
        'callHelp_ForgetTimeByArrival': (
            'HelpCallForgetTime', True, int,
            "Time until call for help is forgotten by responder."),
        'callHelp_MinWaitTime': (
            'HelpCallMinWaitTime', True, int,
            "Internal description: 'Minimum time for response goal at first waiting goal'. Units "
            "are in tenths of a second. Only used for Male Ghosts (20)."),
        'callHelp_MaxWaitTime': (
            'HelpCallMaxWaitTime', True, int,
            "Internal description: 'Maximum time for response goal at first waiting goal'. Units "
            "are in tenths of a second. Only used for Female Ghosts (40)."),
        'goalAction_ToCaution': (
            'CautionGoalAction', True, NPC_THINK_GOAL_ACTION,
            "Type of action taken when AI enters the 'Caution' state."),
        'goalAction_ToFind': (
            'SearchGoalAction', True, NPC_THINK_GOAL_ACTION,
            "Type of action taken when AI enters the 'Search' state."),
        'callHelp_ReplyBehaviorType': (
            'HelpCallReplyType', True, NPC_THINK_REPLY_BEHAVIOR_TYPE,
            "Set to 0 for NPCs who do not reply to calls for help and 1 for NPCs who do."),
        'disablePathMove': (
            'IgnoreNavmesh', True, bool,  # NOTE: Not a boolean field, but used like one.
            "If 1, this NPC will ignore navmesh when moving. True for Ghosts and enemies that don't "
            "move at all."),
        'skipArrivalVisibleCheck': (
            'SkipArrivalVisibleCheck', False, bool,
            "Internal description: 'If enabled, arrival determination is performed even if the "
            "line of sight is not passed.' True only for Hawkeye Gough."),
        'thinkAttr_doAdmirer': (
            'AdmirerAttribute', True, bool,
            "Internal description: 'Thought attribute: when enabled, it plays the role of a wrap.' "
            "I don't know exactly what that means, but this is likely important for something. "
            "Enabled for Soulmass and Pursuers, non-giant Rats, Infested Ghouls, Mushrooms, most "
            "Hollows (not archers), Male Ghosts, normal Skeletons and Skeleton Beasts, Pisaca, "
            "Gardeners, Bloatheads (not Sorcerers), Humanity Phantoms, and the Four Kings."),
        'enableNaviFlg_Edge:1': (
            'CanFallOffEdges', True, bool,
            "If True, this NPC will pursue targets off navmesh edges (survivable falls)."),
        'enableNaviFlg_LargeSpace:1': (
            'CanNavigateWideSpaces', True, bool,
            "If True, this NPC can enter navmesh regions flagged as 'large spaces'."),
        'enableNaviFlg_Ladder:1': (
            'CanNavigateLadders', True, bool,
            "If True, this NPC will use ladders."),
        'enableNaviFlg_Hole:1': (
            'CanNavigateHoles', True, bool,
            "If True, this NPC can fall into navmesh holes."),
        'enableNaviFlg_Door:1': (
            'CanNavigateDoors', True, bool,
            "If True, this NPC can go through doors (but not necessarily open closed doors)."),
        'enableNaviFlg_InSideWall:1': (
            'CanNavigateInsideWalls', True, bool,
            "If True, this NPC can go through walls (i.e. ignores navmesh walls)."),
        'enableNaviFlg_reserve0:2': (
            'UnusedNavmeshCheckX2', False, bool,
            "Two unused bytes reserved for other navmesh checks. No effect."),
        'enableNaviFlg_reserve1[3]': (
            'UnusedNavmeshCheckX3', False, bool,
            "Three unused bytes reserved for other navmesh checks. No effect."),
        'pad0[12]': (
            'Pad0', False, '<Pad:12>',
            "Null padding."),
    },
    'EQUIP_PARAM_PROTECTOR_ST': {
        'sortId': (
            'SortIndex', True, int,
            "Index for automatic inventory sorting."),
        'wanderingEquipId': (
            'GhostArmorReplacement', True, Params.Armor,
            "Replacement equipment for network ghosts."),
        'vagrantItemLotId': (
            'VagrantItemLot', True, Params.ItemLots,
            "DOC-TODO"),
        'vagrantBonusEneDropItemLotId': (
            'VagrantBonusEnemyDropItemLot', True, Params.ItemLots,
            "DOC-TODO"),
        'vagrantItemEneDropItemLotId': (
            'VagrantItemEnemyDropItemLot', True, Params.ItemLots,
            "DOC-TODO"),
        'fixPrice': (
            'RepairCost', True, int,
            "Amount of souls required to repair armor fully. Actual repair cost is this multiplied by current "
            "durability over max durability."),
        'basicPrice': (
            'BasicCost', False, int,
            "Unsure when this is used. Possibly sets the default if the cost is not specified in Shop parameters. "
            "Always set to 200."),
        'sellValue': (
            'FramptSellValue', True, int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold."),
        'weight': (
            'Weight', True, float,
            "Weight of armor."),
        'residentSpEffectId': (
            'WearerSpecialEffect1', True, Params.SpecialEffects,
            "Special effect granted to wearer (first of three)."),
        'residentSpEffectId2': (
            'WearerSpecialEffect2', True, Params.SpecialEffects,
            "Special effect granted to wearer (second of three)."),
        'residentSpEffectId3': (
            'WearerSpecialEffect3', True, Params.SpecialEffects,
            "Special effect granted to wearer (third of three)."),
        'materialSetId': (
            'UpgradeMaterialID', True, Params.UpgradeMaterials,
            "Upgrade material set for reinforcement."),
        'partsDamageRate': (
            'SiteDamageMultiplier', True, float,
            "Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, so is "
            "never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, 1.1 for gauntlets "
            "and leggings, and 1 for torso armor."),
        'corectSARecover': (
            'PoiseRecoveryTimeModifier', True, float,
            "Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
            "otherwise."),
        'originEquipPro': (
            'UpgradeOrigin0', True, Params.Armor,
            "Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro1': (
            'UpgradeOrigin1', True, Params.Armor,
            "Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro2': (
            'UpgradeOrigin2', True, Params.Armor,
            "Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro3': (
            'UpgradeOrigin3', True, Params.Armor,
            "Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro4': (
            'UpgradeOrigin4', True, Params.Armor,
            "Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro5': (
            'UpgradeOrigin5', True, Params.Armor,
            "Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro6': (
            'UpgradeOrigin6', True, Params.Armor,
            "Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro7': (
            'UpgradeOrigin7', True, Params.Armor,
            "Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro8': (
            'UpgradeOrigin8', True, Params.Armor,
            "Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro9': (
            'UpgradeOrigin9', True, Params.Armor,
            "Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro10': (
            'UpgradeOrigin10', True, Params.Armor,
            "Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro11': (
            'UpgradeOrigin11', True, Params.Armor,
            "Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro12': (
            'UpgradeOrigin12', True, Params.Armor,
            "Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro13': (
            'UpgradeOrigin13', True, Params.Armor,
            "Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro14': (
            'UpgradeOrigin14', True, Params.Armor,
            "Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro15': (
            'UpgradeOrigin15', True, Params.Armor,
            "Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'faceScaleM_ScaleX': (
            'MaleFaceScaleX', True, float,
            "Scale factor applied to X dimension of male faces when worn."),
        'faceScaleM_ScaleZ': (
            'MaleFaceScaleZ', True, float,
            "Scale factor applied to Z dimension of male faces when worn."),
        'faceScaleM_MaxX': (
            'MaleFaceMaxScaleX', True, float,
            "Maximum scale permitted for X dimension of male faces when worn."),
        'faceScaleM_MaxZ': (
            'MaleFaceMaxScaleZ', True, float,
            "Maximum scale permitted for Z dimension of male faces when worn."),
        'faceScaleF_ScaleX': (
            'FemaleFaceScaleX', True, float,
            "Scale factor applied to X dimension of female faces when worn."),
        'faceScaleF_ScaleZ': (
            'FemaleFaceScaleZ', True, float,
            "Scale factor applied to Z dimension of female faces when worn."),
        'faceScaleF_MaxX': (
            'FemaleFaceMaxScaleX', True, float,
            "Maximum scale permitted for X dimension of female faces when worn."),
        'faceScaleF_MaxZ': (
            'FemaleFaceMaxScaleZ', True, float,
            "Maximum scale permitted for Z dimension of female faces when worn."),
        'qwcId': (
            'QWCID', False, int,
            "Unused world tendency remnant."),
        'equipModelId': (
            'EquipmentModel', True, Model,
            "Model ID of armor."),
        'iconIdM': (
            'MaleIcon', True, Texture,
            "Icon of male variant of armor in inventory."),
        'iconIdF': (
            'FemaleIcon', True, Texture,
            "Icon of female variant of armor in inventory."),
        'knockBack': (
            'KnockbackPercentageReduction', False, int,
            "Never used. Probably the percentage of knockback reduced (from 0 to 100) when wearing armor."),
        'knockbackBounceRate': (
            'KnockbackBouncePercentage', False, int,
            "Never used. Possibly affects knockback of incoming attacks."),
        'durability': (
            'InitialDurability', True, int,
            "Durability of armor when it is obtained. Always equal to max durability in vanilla game."),
        'durabilityMax': (
            'MaxDurability', True, int,
            "Maximum durability of armor."),
        'saDurability': (
            'Poise', True, int,
            "Amount of poise added when wearing armor."),
        'defFlickPower': (
            'RepelDefense', True, int,
            "Determines when incoming attacks will bounce off."),
        'defensePhysics': (
            'PhysicalDefense', True, int,
            "Added defense against physical attack damage."),
        'defenseMagic': (
            'MagicDefense', True, int,
            "Added defense against magic attack damage."),
        'defenseFire': (
            'FireDefense', True, int,
            "Added defense against fire attack damage."),
        'defenseThunder': (
            'LightningDefense', True, int,
            "Added defense against lightning attack damage."),
        'defenseSlash': (
            'SlashDefense', True, int,
            "Added defense against physical slash attack damage."),
        'defenseBlow': (
            'StrikeDefense', True, int,
            "Added defense against physical strike attack damage."),
        'defenseThrust': (
            'ThrustDefense', True, int,
            "Added defense against physical thrust attack damage."),
        'resistPoison': (
            'PoisonResistance', True, int,
            "Poison resistance added by armor."),
        'resistDisease': (
            'ToxicResistance', True, int,
            "Toxic resistance added by armor."),
        'resistBlood': (
            'BleedResistance', True, int,
            "Bleed resistance added by armor."),
        'resistCurse': (
            'CurseResistance', True, int,
            "Curse resistance added by armor."),
        'reinforceTypeId': (
            'UpgradeMaterials', True, Params.UpgradeMaterials,
            "Upgrade materials required for reinforcement at each level."),
        'trophySGradeId': (
            'AchievementContributionID', False, int,
            "Index of armor as it contributes to certain multi-item achievements."),
        'shopLv': (
            'ShopLevel', False, int,
            "Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused."),
        'knockbackParamId': (
            'KnockbackID', False, Params.Knockback,
            "Knockback entry. Always 1."),
        'flickDamageCutRate': (
            'RepelDamagePercentageReduction', True, int,
            "Determines some aspect of attack deflection. Always set to 0 (for light armor) or 255 (for heavy armor)."),
        'equipModelCategory': (
            'EquipmentModelCategory', True, EQUIP_MODEL_CATEGORY,
            "Body part covered by armor model."),
        'equipModelGender': (
            'EquipmentModelGender', True, EQUIP_MODEL_GENDER,
            "Gender variant of armor."),
        'protectorCategory': (
            'ArmorType', True, PROTECTOR_CATEGORY,
            "Type of armor (equip slot)."),
        'defenseMaterial': (
            'SoundEffectOnHit', True, WEP_MATERIAL_DEF,
            "Type of sound effect generated when this armor is hit."),
        'defenseMaterialSfx': (
            'VisualEffectOnHit', True, WEP_MATERIAL_DEF_SFX,
            "Type of visual effect generated when this armor is hit."),
        'partsDmgType': (
            'PartsDamageType', False, ATK_PARAM_PARTSDMGTYPE,
            "Always zero."),
        'defenseMaterial_Weak': (
            'SoundEffectOnWeakSpotHit', True, WEP_MATERIAL_DEF,
            "Sound effect for when damage is taken to weak spot (used for head armor)."),
        'defenseMaterialSfx_Weak': (
            'VisualEffectOnWeakSpotHit', True, WEP_MATERIAL_DEF_SFX,
            "Visual effect for when damage is taken to weak spot (used for head armor)."),
        'isDeposit:1': (
            'CanBeStored', True, bool,
            "If True, this armor can be stored in the Bottomless Box."),
        'headEquip:1': (
            'EquippedToHead', True, bool,
            "This armor is equipped to the head."),
        'bodyEquip:1': (
            'EquippedToBody', True, bool,
            "This armor is equipped to the body."),
        'armEquip:1': (
            'EquippedToHands', True, bool,
            "This armor is equipped to the hands."),
        'legEquip:1': (
            'EquippedToLegs', True, bool,
            "This armor is equipped to the legs."),
        'useFaceScale:1': (
            'UseFaceScale', False, bool,
            "If True, the face-scaling parameters of this armor will be applied."),
        'invisibleFlag00:1': (
            'HideFlag0', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag01:1': (
            'HideFlag1', False, bool,
            "Hide part of the character model: (hair fringe)"),
        'invisibleFlag02:1': (
            'HideFlag2', False, bool,
            "Hide part of the character model: (sideburns)"),
        'invisibleFlag03:1': (
            'HideFlag3', False, bool,
            "Hide part of the character model: (top of head)"),
        'invisibleFlag04:1': (
            'HideFlag4', False, bool,
            "Hide part of the character model: (top of head)"),
        'invisibleFlag05:1': (
            'HideFlag5', False, bool,
            "Hide part of the character model: (back hair)"),
        'invisibleFlag06:1': (
            'HideFlag6', False, bool,
            "Hide part of the character model: (back hair tip)"),
        'invisibleFlag07:1': (
            'HideFlag7', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag08:1': (
            'HideFlag8', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag09:1': (
            'HideFlag9', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag10:1': (
            'HideFlag10', False, bool,
            "Hide part of the character model: (collar)"),
        'invisibleFlag11:1': (
            'HideFlag11', False, bool,
            "Hide part of the character model: (around collar)"),
        'invisibleFlag12:1': (
            'HideFlag12', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag13:1': (
            'HideFlag13', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag14:1': (
            'HideFlag14', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag15:1': (
            'HideFlag15', False, bool,
            "Hide part of the character model: (hood hem)"),
        'invisibleFlag16:1': (
            'HideFlag16', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag17:1': (
            'HideFlag17', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag18:1': (
            'HideFlag18', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag19:1': (
            'HideFlag19', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag20:1': (
            'HideFlag20', False, bool,
            "Hide part of the character model: (sleeve A)"),
        'invisibleFlag21:1': (
            'HideFlag21', False, bool,
            "Hide part of the character model: (sleeve B)"),
        'invisibleFlag22:1': (
            'HideFlag22', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag23:1': (
            'HideFlag23', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag24:1': (
            'HideFlag24', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag25:1': (
            'HideFlag25', False, bool,
            "Hide part of the character model: (arm)"),
        'invisibleFlag26:1': (
            'HideFlag26', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag27:1': (
            'HideFlag27', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag28:1': (
            'HideFlag28', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag29:1': (
            'HideFlag29', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag30:1': (
            'HideFlag30', False, bool,
            "Hide part of the character model: (belt)"),
        'invisibleFlag31:1': (
            'HideFlag31', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag32:1': (
            'HideFlag32', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag33:1': (
            'HideFlag33', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag34:1': (
            'HideFlag34', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag35:1': (
            'HideFlag35', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag36:1': (
            'HideFlag36', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag37:1': (
            'HideFlag37', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag38:1': (
            'HideFlag38', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag39:1': (
            'HideFlag39', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag40:1': (
            'HideFlag40', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag41:1': (
            'HideFlag41', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag42:1': (
            'HideFlag42', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag43:1': (
            'HideFlag43', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag44:1': (
            'HideFlag44', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag45:1': (
            'HideFlag45', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag46:1': (
            'HideFlag46', False, bool,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag47:1': (
            'HideFlag47', False, bool,
            "Hide part of the character model: (unknown)"),
        'disableMultiDropShare:1': (
            'DisableMultiplayerShare', False, bool,
            "If True, this armor cannot be given to other players by dropping it. Always False in vanilla."),
        'simpleModelForDlc:1': (
            'SimpleDLCModelExists', False, bool,
            "Unknown; always set to False."),
        'pad_0[1]': (
            'Pad0', False, '<Pad:1>',
            "Null padding."),
        'oldSortId': (
            'OldSortIndex', False, int,
            "Sorting index for an obsolete build of the game. No effect."),
        'pad_1[6]': (
            'Pad1', False, '<Pad:6>',
            "Null padding."),
    },
    'REINFORCE_PARAM_PROTECTOR_ST': {
        'physicsDefRate': (
            'PhysicalDefenseMultiplier', True, float,
            "Multiplier for physical defense at this upgrade level."),
        'magicDefRate': (
            'MagicDefenseMultiplier', True, float,
            "Multiplier for magic defense at this upgrade level."),
        'fireDefRate': (
            'FireDefenseMultiplier', True, float,
            "Multiplier for fire defense at this upgrade level."),
        'thunderDefRate': (
            'LightningDefenseMultiplier', True, float,
            "Multiplier for lightning defense at this upgrade level."),
        'slashDefRate': (
            'SlashDefenseMultiplier', True, float,
            "Multiplier for slash defense at this upgrade level."),
        'blowDefRate': (
            'StrikeDefenseMultiplier', True, float,
            "Multiplier for strike defense at this upgrade level."),
        'thrustDefRate': (
            'ThrustDefenseMultiplier', True, float,
            "Multiplier for thrust defense at this upgrade level."),
        'resistPoisonRate': (
            'PoisonResistanceMultiplier', True, float,
            "Multiplier for poison resistance at this upgrade level."),
        'resistDiseaseRate': (
            'ToxicResistanceMultiplier', True, float,
            "Multiplier for toxic resistance at this upgrade level."),
        'resistBloodRate': (
            'BleedResistanceMultiplier', True, float,
            "Multiplier for bleed resistance at this upgrade level."),
        'resistCurseRate': (
            'CurseResistanceMultiplier', True, float,
            "Multiplier for curse resistance at this upgrade level."),
        'residentSpEffectId1': (
            'WearerSpecialEffect1', True, Params.SpecialEffects,
            "Special effect granted to wearer (first of three)."),
        'residentSpEffectId2': (
            'WearerSpecialEffect2', True, Params.SpecialEffects,
            "Special effect granted to wearer (second of three)."),
        'residentSpEffectId3': (
            'WearerSpecialEffect3', True, Params.SpecialEffects,
            "Special effect granted to wearer (third of three)."),
        'materialSetId': (
            'UpgradeMaterialID', True, Params.UpgradeMaterials,
            "Upgrade material set for reinforcement."),
    },
    'GAME_AREA_PARAM_ST': {
        'bonusSoul_single': (
            'SingleplayerSoulReward', True, int,
            "Souls awarded (after delay) when boss is defeated with no summons."),
        'bonusSoul_multi': (
            'MultiplayerSoulReward', True, int,
            "Souls awarded to each player (after delay) when boss is defeated with summons."),
        'humanityPointCountFlagIdTop': (
            'FirstHumanityFlag', True, Flag,
            "First flag for recording number of humanity drops awarded in boss's area."),
        'humanityDropPoint1': (
            'HumanityDropPoint1', True, int,
            "Number of 'points' needed from killing enemies in the boss area for first Humanity."),
        'humanityDropPoint2': (
            'HumanityDropPoint2', True, int,
            "Number of 'points' needed from killing enemies in the boss area for second Humanity."),
        'humanityDropPoint3': (
            'HumanityDropPoint3', True, int,
            "Number of 'points' needed from killing enemies in the boss area for third Humanity."),
        'humanityDropPoint4': (
            'HumanityDropPoint4', True, int,
            "Number of 'points' needed from killing enemies in the boss area for fourth Humanity."),
        'humanityDropPoint5': (
            'HumanityDropPoint5', True, int,
            "Number of 'points' needed from killing enemies in the boss area for fifth Humanity."),
        'humanityDropPoint6': (
            'HumanityDropPoint6', True, int,
            "Number of 'points' needed from killing enemies in the boss area for sixth Humanity."),
        'humanityDropPoint7': (
            'HumanityDropPoint7', True, int,
            "Number of 'points' needed from killing enemies in the boss area for seventh Humanity."),
        'humanityDropPoint8': (
            'HumanityDropPoint8', True, int,
            "Number of 'points' needed from killing enemies in the boss area for eighth Humanity."),
        'humanityDropPoint9': (
            'HumanityDropPoint9', True, int,
            "Number of 'points' needed from killing enemies in the boss area for ninth Humanity."),
        'humanityDropPoint10': (
            'HumanityDropPoint10', True, int,
            "Number of 'points' needed from killing enemies in the boss area for final Humanity."),
    },
    'BULLET_PARAM_ST': {
        'atkId_Bullet': (
            'BulletAttack', True, Params.Attacks,
            "Attack parameters for bullet impact. Only certain fields in the attack parameter are used. "
            "Could be directed to either PlayerAttacks table or NonPlayerAttacks table, depending on "
            "the bullet's owner. Set to 0 if bullet has no attack data (no damage)."),
        'sfxId_Bullet': (
            'ProjectileFX', True, int,
            "Visual effect ID for bullet projectile."),
        'sfxId_Hit': (
            'ImpactFX', True, int,
            "Visual effect ID for bullet impact."),
        'sfxId_Flick': (
            'FlickFX', True, int,
            "Visual effect ID for when bullet is blocked (I think). Used predominantly for arrows and "
            "throwing knives."),
        'life': (
            'LifeTime', True, float,
            "Maximum time before bullet will disappear on its own. -1 means it will last indefinitely."),
        'dist': (
            'AttenuationDistance', True, float,
            "Distance at which attenuation of the projectile begins."),
        'shootInterval': (
            'LaunchInterval', True, float,
            "Time between emitted bullets. Does nothing for bullets that only shoot once and is "
            "generally left at zero for those bullets."),
        'gravityInRange': (
            'GravityBeforeAttenuation', True, float,
            "Downward acceleration of bullet. Rarely used."),
        'gravityOutRange': (
            'GravityAfterAttenuation', True, float,
            "Downward acceleration of bullet after it passes the attenuation distance."),
        'hormingStopRange': (
            'ClosestHomingDistance', True, float,
            "Bullet will stop homing if it is within this distance of its homing target. Use this to "
            "prevent homing bullets from being too oppressive."),
        'initVellocity': (
            'InitialSpeed', True, float,
            "Initial speed of bullet."),
        'accelInRange': (
            'AccelerationBeforeAttenuation', True, float,
            "Forward acceleration acting on bullet before it reaches the attenuation distance. Negative "
            "values will slow the bullet down."),
        'accelOutRange': (
            'AccelerationAfterAttenuation', True, float,
            "Forward acceleration acting on bullet after it passes the attenuation distance. Negative "
            "values will slow the bullet down."),
        'maxVellocity': (
            'MaxSpeed', True, float,
            "Maximum speed of bullet, regardless of acceleration."),
        'minVellocity': (
            'MinSpeed', True, float,
            "Minimum speed of bullet, regardless of acceleration."),
        'accelTime': (
            'AccelerationTime', True, float,
            "Time that acceleration is active after bullet creation."),
        'homingBeginDist': (
            'HomingStartDistance', True, float,
            "Distance from owner at which the bullet starts homing in on targets."),
        'hitRadius': (
            'InitialHitRadius', True, float,
            "Initial hit radius of bullet projectile."),
        'hitRadiusMax': (
            'FinalHitRadius', True, float,
            "Final hit radius of bullet projectile. Set to -1 if radius does not change, which is always "
            "coupled with a value of 0 for RadiusIncreaseDuration."),
        'spreadTime': (
            'RadiusIncreaseTime', True, float,
            "Time taken by bullet to transition from initial to final hit radius. Value of 0 are always "
            "coupled with values of -1 for RadiusIncreaseDuration. I'm not sure if this can actually "
            "decrease the hit radius if the final value is less than the initial value."),
        'expDelay': (
            'ExpDelay', False, float,
            "Delay between impact and 'explosion' (not sure if that refers to the visual effect and/or "
            "Collision). Never used (always zero)."),
        'hormingOffsetRange': (
            'HomingOffsetRange', True, float,
            "Internal description: 'When shooting, aim to shift each component of XYZ by this "
            "amount.' Nonzero only for Hydra blasts and Vagrant attacks."),
        'dmgHitRecordLifeTime': (
            'CollisionLifeTime', True, float,
            "Duration of bullet impact Collision. A value of zero means it is disabled immediately "
            "after first impact."),
        'externalForce': (
            'ExternalForce', True, float,
            "Unknown. Used only for Gargoyle fire breath and Undead Dragon poison breath."),
        'spEffectIDForShooter': (
            'OwnerSpecialEffect', True, Params.SpecialEffects,
            "Special effect applied to owner when bullet is created. (Unclear if it is applied "
            "repeatedly by repeating bullets.)"),
        'autoSearchNPCThinkID': (
            'BulletAI', True, Params.AI,
            "AI parameter ID for triggered floating bullets. Only used by Homing [Crystal] "
            "Soulmass (10000) and Pursuers (10001) in the vanilla game."),
        'HitBulletID': (
            'BulletOnHit', True, Params.Bullets,
            "Bullet emitted on impact of this bullet. Used often for 'throw'/'landing' or 'parent'/'child' "
            "combinations, like a thrown Firebomb (bullet 110) triggering a fiery explosion (bullet 111). "
            "These can be chained together indefinitely (see White Dragon Breath, bullet 11500)."),
        'spEffectId0': (
            'HitSpecialEffect0', True, Params.SpecialEffects,
            "Special effect applied to target hit by bullet. (Slot 0)"),
        'spEffectId1': (
            'HitSpecialEffect1', True, Params.SpecialEffects,
            "Special effect applied to target hit by bullet. (Slot 1)"),
        'spEffectId2': (
            'HitSpecialEffect2', True, Params.SpecialEffects,
            "Special effect applied to target hit by bullet. (Slot 2)"),
        'spEffectId3': (
            'HitSpecialEffect3', True, Params.SpecialEffects,
            "Special effect applied to target hit by bullet. (Slot 3)"),
        'spEffectId4': (
            'HitSpecialEffect4', True, Params.SpecialEffects,
            "Special effect applied to target hit by bullet. (Slot 4)"),
        'numShoot': (
            'BulletCount', True, int,
            "Number of bullets emitted at once."),
        'homingAngle': (
            'HomingAnglePerSecond', True, int,
            "Turning angle of homing bullet per second. Higher values are better for homing."),
        'shootAngle': (
            'AzimuthAngleStart', True, int,
            "Angle of first bullet in degrees around the vertical axis, relative to the forward direction."),
        'shootAngleInterval': (
            'AzimuthAngleInterval', True, int,
            "Angle from one bullet to the next around the vertical axis, beginning at the azimuth "
            "angle start."),
        'shootAngleXInterval': (
            'ElevationAngleInterval', True, int,
            "Angle between bullets in elevation."),
        'damageDamp': (
            'PhysicalDamageDamp', True, int,
            "Percentage reduction in physical damage per second."),
        'spelDamageDamp': (
            'MagicDamageDamp', True, int,
            "Percentage reduction in magic damage per second."),
        'fireDamageDamp': (
            'FireDamageDamp', True, int,
            "Percentage reduction in fire damage per second."),
        'thunderDamageDamp': (
            'LightningDamageDamp', True, int,
            "Percentage reduction in lightning damage per second."),
        'staminaDamp': (
            'StaminaDamp', False, int,
            "Percentage reduction in stamina damage per second."),
        'knockbackDamp': (
            'KnockbackDamp', False, int,
            "Percentage reduction in knockback power per second."),
        'shootAngleXZ': (
            'FirstBulletElevationAngle', True, int,
            "Angle of elevation of first bullet. Positive values will angle the bullets up (e.g. "
            "Quelaag's fireballs) and negative values will angle the bullets down (e.g. most breath "
            "attacks)."),
        'lockShootLimitAng': (
            'LockShootLimitAngle', True, int,
            "Unknown, but likely important. Set to 30 for most basic projectile magic."),
        'isPenetrate': (
            'PiercesTargets', True, bool,
            "Bullet will go through objects, players, and NPCs."),
        'prevVelocityDirRate': (
            'PreviousDirectionRatio', False, int,
            "Internal description: 'Ratio of adding the previous moving direction to the current direction when a "
            "sliding bullet hits the wall.' Like ExternalForce, this is used only for Gargoyle and Undead Dragon "
            "breath (100) and is zero for everything else."),
        'atkAttribute': (
            'AttackAttribute', True, ATKPARAM_ATKATTR_TYPE,
            "Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts)."),
        'spAttribute': (
            'ElementAttribute', True, ATKPARAM_SPATTR_TYPE,
            "Element attached to bullet hit."),
        'Material_AttackType': (
            'MaterialAttackType', True, ATK_TYPE,
            "Determines visual effects of bullet hit."),
        'Material_AttackMaterial': (
            'EffectsOnHit', True, WEP_MATERIAL_ATK,
            "Sound and visual effects on hit."),
        'Material_Size': (
            'MaterialSize', False, ATK_SIZE,
            "'Size' of attack. Never used.'"),
        'launchConditionType': (
            'LaunchConditionType', True, BULLET_LAUNCH_CONDITION_TYPE,
            "Condition for determing if a new bullet will be generated when this bullet lands or expires."),
        'FollowType:3': (
            'FollowType', True, BULLET_FOLLOW_TYPE,
            "Follow type."),
        'EmittePosType:3': (
            'OriginType', True, BULLET_EMITTE_POS_TYPE,
            "Origin type of bullet. Usually comes from model points ('damipoly')."),
        'isAttackSFX:1': (
            'RemainAttachedToTarget', True, bool,
            "Set whether bullets (e.g. arrows) stay stuck upon impact."),
        'isEndlessHit:1': (
            'IsEndlessHit', True, bool,
            "Bullet Collision is continuous (I think). Only used for corrosion cloud in vanilla."),
        'isPenetrateMap:1': (
            'IsMapPiercing', True, bool,
            "Bullet will pierce the map (e.g. Stray Demon blast)."),
        'isHitBothTeam:1': (
            'HitsBothTeams', True, bool,
            "Bullet can hit any character."),
        'isUseSharedHitList:1': (
            'SharedHitCheck', True, bool,
            "Repeating bullets share the amount of times they have hit a target (usually so the "
            "target is only hit once by any of those repeating bullets)."),
        'isUseMultiDmyPolyIfPlace:1': (
            'UsesMultipleModelPoints', True, bool,
            "Set to True if the same model point ('damipoly') is used multiple times when spawning the bullet."),
        'attachEffectType:2': (
            'AttachEffectType', False, BULLET_ATTACH_EFFECT_TYPE,
            "Mostly 0, but sometimes 1 (Dragon Head breath, Grant AoE, Force miracles)."),
        'isHitForceMagic:1': (
            'CanBeDeflectedByMagic', True, bool,
            "If True, this bullet will impact appropriate Force-type magic (e.g. arrows, bolts, knives)."),
        'isIgnoreSfxIfHitWater:1': (
            'IgnoreFXOnWaterHit', True, bool,
            "If True, hit FX are not produced if the bullet impacts water."),
        'isIgnoreMoveStateIfHitWater:1': (
            'IgnoreStateTransitionOnWaterHit', True, bool,
            "Unclear effect, but True for knives/arrows/bolts and False otherwise."),
        'isHitDarkForceMagic:1': (
            'CanBeDeflectedBySilverPendant', True, bool,
            "If True, this bullet will impact the Silver Pendant shield effect. True only for dark sorceries."),
        'pad[3]': (
            'Pad3', False, '<Pad:3>',
            "Null padding."),
    },
    'LOCK_CAM_PARAM_ST': {
        'camDistTarget': (
            'CameraDistanceFromTarget', True, float,
            "Distance maintained from target by camera in meters. (Default value is 4.)"),
        'rotRangeMinX': (
            'MinRotationElevation', True, float,
            "Minimum angle of elevation (X-axis rotation) permitted for camera."),
        'lockRotXShiftRatio': (
            'LockElevationShiftRatio', True, float,
            "'Lock X-rotation shift ratio (0.0 to 1.0).' Unclear effect. Default value is 0.6."),
        'chrOrgOffset_Y': (
            'CharacterVerticalOffset', True, float,
            "Vertical offset of camera target from character's base. Default value is 1.42."),
        'chrLockRangeMaxRadius': (
            'MaxDistanceFromCharacter', True, float,
            "Maximum distance ('radius') of camera from character in meters. Default value is 15; only other value "
            "used is 7."),
        'camFovY': (
            'VerticalFieldOfView', True, float,
            "Vertical field of view of camera in degrees. Default value is 43. Never goes above 48 (Lost Izalith)."),
        'pad[8]': (
            'Pad1', False, '<Pad:8>',
            "Null padding."),
    },
    'ATK_PARAM_ST': {
        'hit0_Radius': (
            'Collision0Radius', True, float,
            "Radius of sphere/capsule Collision (slot 0)."),
        'hit1_Radius': (
            'Collision1Radius', True, float,
            "Radius of sphere/capsule Collision (slot 1)."),
        'hit2_Radius': (
            'Collision2Radius', True, float,
            "Radius of sphere/capsule Collision (slot 2)."),
        'hit3_Radius': (
            'Collision3Radius', True, float,
            "Radius of sphere/capsule Collision (slot 3)."),
        'knockbackDist': (
            'KnockbackDistance', True, float,
            "Knockback distance of attack."),
        'hitStopTime': (
            'HitStopTime', True, float,
            "Unclear. This isn't Collision duration, which is determined by the duration of the triggering TAE event. It "
            "may be the duration of the 'hit' flag on the target. Always set to 0, 0.08. or 0.11."),
        'spEffectId0': (
            'SpecialEffectOnHit0', True, Params.SpecialEffects,
            "Special effect applied to target on hit (slot 0)."),
        'spEffectId1': (
            'SpecialEffectOnHit1', True, Params.SpecialEffects,
            "Special effect applied to target on hit (slot 1)."),
        'spEffectId2': (
            'SpecialEffectOnHit2', True, Params.SpecialEffects,
            "Special effect applied to target on hit (slot 2)."),
        'spEffectId3': (
            'SpecialEffectOnHit3', True, Params.SpecialEffects,
            "Special effect applied to target on hit (slot 3)."),
        'spEffectId4': (
            'SpecialEffectOnHit4', True, Params.SpecialEffects,
            "Special effect applied to target on hit (slot 4)."),
        'hit0_DmyPoly1': (
            'Collision0StartModelPoint', True, int,
            "Model point at origin of Collision (slot 0). If Collision0EndModelPoint is not -1, the Collision will be a capsule "
            "with hemispherical caps positioned at these origins (with a joining cylinder)."),
        'hit1_DmyPoly1': (
            'Collision1StartModelPoint', True, int,
            "Model point at origin of Collision (slot 1). If Collision1EndModelPoint is not -1, the Collision will be a capsule "
            "with hemispherical caps positioned at these origins (with a joining cylinder)."),
        'hit2_DmyPoly1': (
            'Collision2StartModelPoint', True, int,
            "Model point at origin of Collision (slot 2). If Collision2EndModelPoint is not -1, the Collision will be a capsule "
            "with hemispherical caps positioned at these origins (with a joining cylinder)."),
        'hit3_DmyPoly1': (
            'Collision3StartModelPoint', True, int,
            "Model point at origin of Collision (slot 3). If Collision3EndModelPoint is not -1, the Collision will be a capsule "
            "with hemispherical caps positioned at these origins (with a joining cylinder)."),
        'hit0_DmyPoly2': (
            'Collision0EndModelPoint', True, int,
            "Model point at end of capsule Collision (slot 0). If this is -1, the Collision will be a sphere placed at "
            "Collision0StartModelPoint."),
        'hit1_DmyPoly2': (
            'Collision1EndModelPoint', True, int,
            "Model point at end of capsule Collision (slot 1). If this is -1, the Collision will be a sphere placed at "
            "Collision1StartModelPoint."),
        'hit2_DmyPoly2': (
            'Collision2EndModelPoint', True, int,
            "Model point at end of capsule Collision (slot 2). If this is -1, the Collision will be a sphere placed at "
            "Collision2StartModelPoint."),
        'hit3_DmyPoly2': (
            'Collision3EndModelPoint', True, int,
            "Model point at end of capsule Collision (slot 3). If this is -1, the Collision will be a sphere placed at "
            "Collision3StartModelPoint."),
        'blowingCorrection': (
            'BlowOffCorrection', False, int,
            "Unknown. Never used."),
        'atkPhysCorrection': (
            'PhysicalAttackPowerPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character attack power to "
            "calculate physical attack damage."),
        'atkMagCorrection': (
            'MagicAttackPowerPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character attack power to "
            "calculate magic attack damage."),
        'atkFireCorrection': (
            'FireAttackPowerPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character attack power to "
            "calculate fire attack damage."),
        'atkThunCorrection': (
            'LightningAttackPowerPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character attack power to "
            "calculate lightning attack damage."),
        'atkStamCorrection': (
            'PhysicalAttackPowerPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character attack power to "
            "calculate physical attack damage."),
        'guardAtkRateCorrection': (
            'GuardAttackPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character guard attack power. "
            "Throw attacks have a value of 9900, which must essentially ignore blocking completely."),
        'guardBreakCorrection': (
            'GuardBreakPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to character guard breaking power. "
            "Not sure what that is, exactly, but this is set to 0 for parries and 100 for all other attacks."),
        'atkThrowEscapeCorrection': (
            'AttackDuringThrowPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to weapon attacks during throws. "
            "Generally set to 100, except for throw attacks themselves."),
        'atkSuperArmorCorrection': (
            'PoiseAttackPercentage', True, int,  # TODO: Player Attacks only.
            "Multiplier (as percentage from 0 upwards) applied to damage to target poise. "
            "Generally set to 100, except for throw attacks themselves."),
        'atkPhys': (
            'PhysicalAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute physical attack power of attack."),
        'atkMag': (
            'MagicAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute magic attack power of attack."),
        'atkFire': (
            'FireAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute fire attack power of attack."),
        'atkThun': (
            'LightningAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute lightning attack power of attack."),
        'atkStam': (
            'StaminaAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute stamina attack power of attack."),
        'guardAtkRate': (
            'GuardAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute guard attack power of attack."),
        'guardBreakRate': (
            'GuardBreakPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute guard breaking power of attack."),
        'atkSuperArmor': (
            'PoiseAttackPower', True, int,  # TODO: Non Player Attacks only.
            "Absolute poise attack power of attack."),
        'atkThrowEscape': (
            'AttackPowerDuringThrows', False, int,  # TODO: Non Player Attacks only.
            "Absolute attack power of attack. Never used."),
        'atkObj': (
            'ObjectDamage', True, int,
            "Amount of damage dealt to objects by this attack."),
        'guardStaminaCutRate': (
            'GuardStaminaPercentage', False, int,
            "Correction applied to the stamina required to block this attack (I presume). Never used."),
        'guardRate': (
            'GuardPercentage', True, int,
            "Percentage correction made to the guarding ability of the attack, as set in weapon parameters or NPC "
            "parameters. Only used to halve the guarding ability of parries (-50)."),
        'throwTypeId': (
            'ThrowID', True, int,  # TODO: Link to Throws using the ThrowID field rather than by entry ID.
            "Throw to trigger when attack hits. For some reason, throws are triggered using this ID, which is a field "
            "within each Throw table entry rather than the ID of the Throw table entry itself."),
        'hit0_hitType': (  # TODO: Player Attacks only.
            'Collision0HitType', False, ATK_PARAM_HIT_TYPE,
            "Type of hit applied by Collision (slot 0). Always zero, except for some whip attacks."),
        'hit1_hitType': (
            'Collision1HitType', False, ATK_PARAM_HIT_TYPE,
            "Type of hit applied by Collision (slot 1). Always zero, except for some whip attacks."),
        'hit2_hitType': (
            'Collision2HitType', False, ATK_PARAM_HIT_TYPE,
            "Type of hit applied by Collision (slot 2). Always zero, except for some whip attacks."),
        'hit3_hitType': (
            'Collision3HitType', False, ATK_PARAM_HIT_TYPE,
            "Type of hit applied by Collision (slot 3). Always zero, except for some whip attacks."),
        'hti0_Priority': (
            'Collision0Priority', False, int,
            "Priority of Collision (slot 0). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used."),
        'hti1_Priority': (
            'Collision1Priority', False, int,
            "Priority of Collision (slot 1). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used."),
        'hti2_Priority': (
            'Collision2Priority', False, int,
            "Priority of Collision (slot 2). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used."),
        'hti3_Priority': (
            'Collision3Priority', False, int,
            "Priority of Collision (slot 3). If two hits occur simultaneously, only the highest priority hit occurs. "
            "Never used."),
        'dmgLevel': (
            'ImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level of attack, which determines how the target reacts to it (e.g. knocked backward, launched "
            "into the air, etc.). Certain special effects on the target (e.g. Iron Flesh) may re-map this impact level "
            "to a different one."),
        'mapHitType': (
            'MapHitType', True, ATK_PARAM_MAP_HIT,
            "Determines how this attack interacts with the map."),
        'guardCutCancelRate': (
            'IgnoreGuardPercentage', False, int,
            "Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
            "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in favor "
            "of the simple 'IgnoreGuard' boolean field."),
        'atkAttribute': (
            'AttackAttribute', True, ATKPARAM_ATKATTR_TYPE,
            "Type of physical damage done by attack."),
        'spAttribute': (
            'ElementAttribute', True, ATKPARAM_SPATTR_TYPE,
            "Type of elemental damage done by attack. (Attacks can apply any combination of damage types, but this "
            "value will determine what visual effects the attack generates, etc.)"),
        'atkType': (
            'VisualSoundEffectsOnAttack', True, ATK_TYPE,
            "Determines the sounds and visual effects generated by the attack itself (before hit)."),
        'atkMaterial': (
            'VisualSoundEffectsOnHit', True, WEP_MATERIAL_ATK,
            "Determines the sounds and visual effects generated when the attack hits. A value of 255 uses the weapon "
            "default."),
        'atkSize': (
            'AttackSize', False, BEHAVIOR_ATK_SIZE,
            "Internal description says this determines the size of sounds and visual effects, but it is never used."),
        'defMaterial': (
            'SoundEffectsWhileBlocking', False, WEP_MATERIAL_DEF,
            "Determines the sound effects used when guarding. Usually 255 for Player Attacks and 0 (if not a block) "
            "or 50 (if blocking) for Non-Player Attacks."),
        'defSfxMaterial': (
            'VisualEffectsWhileBlocking', False, WEP_MATERIAL_DEF_SFX,
            "Determines the visual effects used when guarding. Usually 255 for Player Attacks and 0 (if not a block) "
            "or 50 (if blocking) for Non-Player Attacks."),
        'hitSourceType': (
            'ModelPointSource', True, ATK_PARAM_HIT_SOURCE,
            "Internal description says 'specify where you get the model point for attack'. Set to 1 for parries, "
            "ripostes, and basic body attacks (falling, rolling, etc.), and zero otherwise. Use that pattern."),
        'throwFlag': (
            'ThrowFlag', True, ATK_PATAM_THROWFLAG_TYPE,
            "Determines how this attack relates to throws: not at all, a throw trigger, or a throw damage parameter."),
        'disableGuard:1': (
            'IgnoreGuard', True, bool,
            "If True, this attack cannot be blocked (e.g. throws)."),
        'disableStaminaAttack:1': (
            'NoStaminaDamage', True, bool,
            "If True, this attack will deal no stamina damage, regardless of its stamina attack power."),
        'disableHitSpEffect:1': (
            'NoSpecialEffects', True, bool,
            "If True, this attack will trigger no special effects on the target. Internal description mentions this is "
            "an 'SCE bug countermeasure' (referring to the original Dark Souls demo)."),
        'IgnoreNotifyMissSwingForAI:1': (
            'NoMissNotificationForAI', True, bool,
            "If True, the character's AI will not be informed when this attack misses. Enabled for basic body attacks "
            "(falling, rolling, ladder punches, etc.) that are generally not considered to be serious attacks."),
        'repeatHitSfx:1': (
            'RepeatHitSoundEffects', False, bool,
            "If True, sound effects will supposedly be repeated as long as the attack continuously hits a wall. Never "
            "enabled, which is probably a good thing."),
        'isArrowAtk:1': (
            'IsPhysicalProjectile', True, bool,
            "Flags if this is the attack damage parameter of a physical projectile (arrow, bolt, or throwing knife)."),
        'isGhostAtk:1': (
            'IsAttackByGhost', True, bool,  # TODO: Non Player Attacks only.
            "Flags if this is an attack of a ghost, which presumably disables wall collision, etc."),
        'isDisableNoDamage:1': (
            'IgnoreInvincibilityFrames', True, bool,
            "If True, this attack will ignore invincibility frames from rolling or backstepping (but not other sources "
            "of invincibility such as TAE or events)."),
        'pad[1]': (
            'Pad1', False, '<Pad:1>',
            "Null padding."),
    },
    'BEHAVIOR_PARAM_ST': {
        'variationId': (
            'VariationID', True, int,  # TODO: connect to model/TAE somehow.
            ""),
        'behaviorJudgeId': (
            'BehaviorJudgeID', True, int,
            "This is the ID specified by TAE events that trigger behaviors."),
        'ezStateBehaviorType_old': (
            'EzstateBehaviorType', False, int,
            "Unused remnant from Demon's Souls."),
        'refType': (
            'ReferenceType', True, BEHAVIOR_REF_TYPE,
            "Is the reference ID below an Attack or Bullet ID?"),
        'pad0[2]': (
            'Pad1', False, '<Pad:2>', "Null padding."),
        'refId': _behavior_ref_id,
        'sfxVariationId': (
            'FXVariationID', True, int,
            "Visual effect ID."),
        'stamina': (
            'StaminaCost', True, int,
            "Stamina cost of behavior."),
        'mp': (
            'DurabilityCost', True, int,
            "Weapon/shield durability cost of behavior."),
        'category': (
            'Category', True, BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' for "
            "thrown goods and 'No Category' otherwise."),
        'heroPoint': (
            'HumanityCost', False, int,
            "Humanity cost of behavior. Never used."),
        'pad1[2]': (
            'Pad2', False, '<Pad:2>', "Null padding."),
    },
    'CHARACTER_INIT_PARAM': {
        'baseRec_mp': (
            'BaseRecMP', False, int, "Unknown."),
        'baseRec_sp': (
            'BaseRecSP', False, int, "Unknown."),
        'red_Falldam': (
            'RedFallDamage', False, int, "Unknown."),
        'soul': (
            'SoulCount', True, int, "Starting soul count of character."),
        'equip_Wep_Right': (
            'RightHandWeapon1', True, Params.Weapons,
            "First (default) weapon/shield equipped in right hand."),
        'equip_Subwep_Right': (
            'RightHandWeapon2', True, Params.Weapons,
            "Second weapon/shield equipped in right hand."),
        'equip_Wep_Left': (
            'LeftHandWeapon1', True, Params.Weapons,
            "First (default) weapon/shield equipped in left hand."),
        'equip_Subwep_Left': (
            'LeftHandWeapon2', True, Params.Weapons,
            "Second weapon/shield equipped in left hand."),
        'equip_Helm': (
            'HeadArmor', True, Params.Armor, "Armor equipped to head."),
        'equip_Armer': (
            'BodyArmor', True, Params.Armor, "Armor equipped to body."),
        'equip_Gaunt': (
            'HandsArmor', True, Params.Armor, "Armor equipped to hands."),
        'equip_Leg': (
            'LegsArmor', True, Params.Armor, "Armor equipped to legs."),
        'equip_Arrow': (
            'ArrowSlot1', True, Params.Weapons, "Arrows equipped in slot 1."),  # TODO: Show arrows only?
        'equip_Bolt': (
            'BoltSlot1', True, Params.Weapons, "Bolts equipped in slot 1."),
        'equip_SubArrow': (
            'ArrowSlot2', True, Params.Weapons, "Arrows equipped in slot 2."),
        'equip_SubBolt': (
            'BoltSlot2', True, Params.Weapons, "Bolts equipped in slot 2."),
        'equip_Accessory01': (
            'RingSlot1', True, Params.Rings,
            "First ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory02': (
            'RingSlot2', True, Params.Rings,
            "Second ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory03': (
            'RingSlot3', True, Params.Rings,
            "Third ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory04': (
            'RingSlot4', True, Params.Rings,
            "Fourth ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory05': (
            'RingSlot5', True, Params.Rings,
            "Fifth ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Skill_01': (
            'SkillSlot1', False, int, ""),  # TODO: unused?
        'equip_Skill_02': (
            'SkillSlot2', False, int, ""),
        'equip_Skill_03': (
            'SkillSlot3', False, int, ""),
        'equip_Spell_01': (
            'SpellSlot1', True, int, "First spell equipped."),  # TODO: points to Goods or Spells?
        'equip_Spell_02': (
            'SpellSlot2', True, int, "Second spell equipped."),
        'equip_Spell_03': (
            'SpellSlot3', True, int, "Third spell equipped."),
        'equip_Spell_04': (
            'SpellSlot4', True, int, "Fourth spell equipped."),
        'equip_Spell_05': (
            'SpellSlot5', True, int, "Fifth spell equipped."),
        'equip_Spell_06': (
            'SpellSlot6', True, int, "Sixth spell equipped."),
        'equip_Spell_07': (
            'SpellSlot7', True, int, "Seventh spell equipped."),
        'item_01': (
            'GoodSlot1', True, int, "Good (item) equipped in slot 1."),
        'item_02': (
            'GoodSlot2', True, int, "Good (item) equipped in slot 2."),
        'item_03': (
            'GoodSlot3', True, int, "Good (item) equipped in slot 3."),
        'item_04': (
            'GoodSlot4', True, int, "Good (item) equipped in slot 4."),
        'item_05': (
            'GoodSlot5', True, int, "Good (item) equipped in slot 5."),
        'item_06': (
            'GoodSlot6', True, int, "Good (item) equipped in slot 6."),
        'item_07': (
            'GoodSlot7', True, int, "Good (item) equipped in slot 7."),
        'item_08': (
            'GoodSlot8', True, int, "Good (item) equipped in slot 8."),
        'item_09': (
            'GoodSlot9', True, int, "Good (item) equipped in slot 9."),
        'item_10': (
            'GoodSlot10', True, int, "Good (item) equipped in slot 10."),
        'npcPlayerFaceGenId': (
            'FaceID', True, Params.Faces,
            "Face parameter ID (NPCs only)."),
        'npcPlayerThinkId': (
            'Default AI', True, Params.AI,
            "Default AI (NPCs only)."),
        'baseHp': (
            'BaseMaxHP', True, int, "Base amount of maximum HP (excluding effects of vitality)."),
        'baseMp': (
            'BaseMaxMP', False, int, "Base amount of maximum MP (unused in Dark Souls)."),
        'baseSp': (
            'BaseMaxStamina', True, int, "Base maximum stamina (excluding effects of endurance)."),
        'arrowNum': (
            'ArrowSlot1Count', True, int, "Count of arrows equipped in slot 1."),
        'boltNum': (
            'BoltSlot1Count', True, int, "Count of arrows equipped in slot 2."),
        'subArrowNum': (
            'ArrowSlot2Count', True, int, "Count of bolts equipped in slot 1."),
        'subBoltNum': (
            'BoltSlot2Count', True, int, "Count of bolts equipped in slot 2."),
        'QWC_sb': (
            'QWC_SB', False, int, "Unknown. Likely to be unused world tendency effect."),
        'QWC_mw': (
            'QWC_MW', False, int, "Unknown. Likely to be unused world tendency effect."),
        'QWC_cd': (
            'QWC_CD', False, int, "Unknown. Likely to be unused world tendency effect."),
        'soulLv': (
            'SoulLevel', True, int,
            "Soul level, independent of actual stats. Determines amount of souls rewarded by human NPCs."),
        'baseVit': (
            'Vitality', True, int, "Base vitality level. Determines maximum health."),
        'baseWil': (
            'Attunement', True, int, "Base attunement level. Determines spell slots and casting speed."),
        'baseEnd': (
            'Endurance', True, int, "Base endurance level. Determines maximum stamina and equip load."),
        'baseStr': (
            'Strength', True, int, "Base strength level. Affects strength-based weapons and damage."),
        'baseDex': (
            'Dexterity', True, int, "Base dexterity level. Affects skill-based weapons and damage."),
        'baseMag': (
            'Intelligence', True, int, "Base intelligence level. Affects magic usability and effectiveness."),
        'baseFai': (
            'Faith', True, int, "Base faith level. Affects miracle usability and effectiveness."),
        'baseLuc': (
            'Luck', True, int, "Base luck level. Improves chances of rare item drops."),
        'baseHeroPoint': (
            'Humanity', True, int, "Base 'soft' humanity."),
        'baseDurability': (
            'Resistance', True, int, "Base resistance level. Improves resistances to status ailments."),
        'itemNum_01': (
            'GoodSlot1Count', True, int, "Count of good equipped in slot 1."),
        'itemNum_02': (
            'GoodSlot2Count', True, int, "Count of good equipped in slot 2."),
        'itemNum_03': (
            'GoodSlot3Count', True, int, "Count of good equipped in slot 3."),
        'itemNum_04': (
            'GoodSlot4Count', True, int, "Count of good equipped in slot 4."),
        'itemNum_05': (
            'GoodSlot5Count', True, int, "Count of good equipped in slot 5."),
        'itemNum_06': (
            'GoodSlot6Count', True, int, "Count of good equipped in slot 6."),
        'itemNum_07': (
            'GoodSlot7Count', True, int, "Count of good equipped in slot 7."),
        'itemNum_08': (
            'GoodSlot8Count', True, int, "Count of good equipped in slot 8."),
        'itemNum_09': (
            'GoodSlot9Count', True, int, "Count of good equipped in slot 9."),
        'itemNum_10': (
            'GoodSlot10Count', True, int, "Count of good equipped in slot 10."),
        'bodyScaleHead': (
            'HeadScale', True, int, "Multiplier applied to head size."),
        'bodyScaleBreast': (
            'ChestScale', True, int, "Multiplier applied to chest size."),
        'bodyScaleAbdomen': (
            'AbdomenScale', True, int, "Multiplier applied to abdomen size."),
        'bodyScaleArm': (
            'ArmScale', True, int, "Multiplier applied to arm size."),
        'bodyScaleLeg': (
            'LegScale', True, int, "Multiplier applied to leg size."),
        'gestureId0': (
            'Gesture1', True, int, "First equipped gesture."),
        'gestureId1': (
            'Gesture2', True, int, "Second equipped gesture."),
        'gestureId2': (
            'Gesture3', True, int, "Third equipped gesture."),
        'gestureId3': (
            'Gesture4', True, int, "Fourth equipped gesture."),
        'gestureId4': (
            'Gesture5', True, int, "Fifth equipped gesture."),
        'gestureId5': (
            'Gesture6', True, int, "Sixth equipped gesture."),
        'gestureId6': (
            'Gesture7', True, int, "Seventh equipped gesture."),
        'npcPlayerType': (
            'NPCType', True, NPC_TYPE, "Type of human NPC."),
        'npcPlayerDrawType': (
            'DrawType', True, NPC_DRAW_TYPE, "Draw type of human NPC."),
        'npcPlayerSex': (
            'Sex', True, CHARACTER_INIT_SEX, "Character sex."),
        'vowType:4': (
            'Covenant', True, CHRINIT_VOW_TYPE, "Character covenant."),
        'pad:4': (
            'Pad0', False, '<Pad:4>', "Null padding."),
        'pad0[10]': (
            'Pad1', False, '<Pad:10>', "Null padding."),
    },
    'TALK_PARAM_ST': {
        'msgId': (
            'SubtitleText', True, Text.Conversations,
            "Text ID for dialogue subtitle."),
        'voiceId': (
            'VoiceSound', True, Sound.Voice,
            "Sound ID (voice) for dialogue."),
        'motionId': (
            'TalkingAnimation', True, Animation,
            "Animation used for talking (-1 for default, or no animation). Usually 7000 (e.g. Fair Lady) or 7001 (e.g. "
            "Andre) when used."),
        'returnPos': (
            'ReturnConversation', False, Params.Conversations,
            "Conversation ID to use instead if the player has 'returned' to this conversation. Used exactly once for "
            "one line by the Crestfallen Warrior, so presumably works, but probably not useful."),
        'reactionId': (
            'ReactionConverastion', False, Params.Conversations,
            "Conversation ID to use as 'reaction'. Always -1."),
        'eventId': (
            'EventFlag', False, Flag,
            "Flag that is enabled when conversation plays (I assume). Used exactly once, for the same Crestfallen "
            "Warrior line that uses the ReturnConversation field."),
        'isMotionLoop': (
            'IsMotionLoop', True, bool,
            "If True, specified TalkingAnimation will loop while dialogue is being spoken. Always True for any entry "
            "that has a non-zero TalkingAnimation."),
        'pad0[7]': (
            'Pad', False, '<Pad:7>',
            "Null padding."),
    },
    'FACE_PARAM_ST': {
        'faceGeoData00': (
            'GeometryData00', True, int,
            "Geometry data point 0."),
        'faceGeoData01': (
            'GeometryData01', True, int,
            "Geometry data point 1."),
        'faceGeoData02': (
            'GeometryData02', True, int,
            "Geometry data point 2."),
        'faceGeoData03': (
            'GeometryData03', True, int,
            "Geometry data point 3."),
        'faceGeoData04': (
            'GeometryData04', True, int,
            "Geometry data point 4."),
        'faceGeoData05': (
            'GeometryData05', True, int,
            "Geometry data point 5."),
        'faceGeoData06': (
            'GeometryData06', True, int,
            "Geometry data point 6."),
        'faceGeoData07': (
            'GeometryData07', True, int,
            "Geometry data point 7."),
        'faceGeoData08': (
            'GeometryData08', True, int,
            "Geometry data point 8."),
        'faceGeoData09': (
            'GeometryData09', True, int,
            "Geometry data point 9."),
        'faceGeoData10': (
            'GeometryData10', True, int,
            "Geometry data point 10."),
        'faceGeoData11': (
            'GeometryData11', True, int,
            "Geometry data point 11."),
        'faceGeoData12': (
            'GeometryData12', True, int,
            "Geometry data point 12."),
        'faceGeoData13': (
            'GeometryData13', True, int,
            "Geometry data point 13."),
        'faceGeoData14': (
            'GeometryData14', True, int,
            "Geometry data point 14."),
        'faceGeoData15': (
            'GeometryData15', True, int,
            "Geometry data point 15."),
        'faceGeoData16': (
            'GeometryData16', True, int,
            "Geometry data point 16."),
        'faceGeoData17': (
            'GeometryData17', True, int,
            "Geometry data point 17."),
        'faceGeoData18': (
            'GeometryData18', True, int,
            "Geometry data point 18."),
        'faceGeoData19': (
            'GeometryData19', True, int,
            "Geometry data point 19."),
        'faceGeoData20': (
            'GeometryData20', True, int,
            "Geometry data point 20."),
        'faceGeoData21': (
            'GeometryData21', True, int,
            "Geometry data point 21."),
        'faceGeoData22': (
            'GeometryData22', True, int,
            "Geometry data point 22."),
        'faceGeoData23': (
            'GeometryData23', True, int,
            "Geometry data point 23."),
        'faceGeoData24': (
            'GeometryData24', True, int,
            "Geometry data point 24."),
        'faceGeoData25': (
            'GeometryData25', True, int,
            "Geometry data point 25."),
        'faceGeoData26': (
            'GeometryData26', True, int,
            "Geometry data point 26."),
        'faceGeoData27': (
            'GeometryData27', True, int,
            "Geometry data point 27."),
        'faceGeoData28': (
            'GeometryData28', True, int,
            "Geometry data point 28."),
        'faceGeoData29': (
            'GeometryData29', True, int,
            "Geometry data point 29."),
        'faceGeoData30': (
            'GeometryData30', True, int,
            "Geometry data point 30."),
        'faceGeoData31': (
            'GeometryData31', True, int,
            "Geometry data point 31."),
        'faceGeoData32': (
            'GeometryData32', True, int,
            "Geometry data point 32."),
        'faceGeoData33': (
            'GeometryData33', True, int,
            "Geometry data point 33."),
        'faceGeoData34': (
            'GeometryData34', True, int,
            "Geometry data point 34."),
        'faceGeoData35': (
            'GeometryData35', True, int,
            "Geometry data point 35."),
        'faceGeoData36': (
            'GeometryData36', True, int,
            "Geometry data point 36."),
        'faceGeoData37': (
            'GeometryData37', True, int,
            "Geometry data point 37."),
        'faceGeoData38': (
            'GeometryData38', True, int,
            "Geometry data point 38."),
        'faceGeoData39': (
            'GeometryData39', True, int,
            "Geometry data point 39."),
        'faceGeoData40': (
            'GeometryData40', True, int,
            "Geometry data point 40."),
        'faceGeoData41': (
            'GeometryData41', True, int,
            "Geometry data point 41."),
        'faceGeoData42': (
            'GeometryData42', True, int,
            "Geometry data point 42."),
        'faceGeoData43': (
            'GeometryData43', True, int,
            "Geometry data point 43."),
        'faceGeoData44': (
            'GeometryData44', True, int,
            "Geometry data point 44."),
        'faceGeoData45': (
            'GeometryData45', True, int,
            "Geometry data point 45."),
        'faceGeoData46': (
            'GeometryData46', True, int,
            "Geometry data point 46."),
        'faceGeoData47': (
            'GeometryData47', True, int,
            "Geometry data point 47."),
        'faceGeoData48': (
            'GeometryData48', True, int,
            "Geometry data point 48."),
        'faceGeoData49': (
            'GeometryData49', True, int,
            "Geometry data point 49."),
        'faceTexData00': (
            'TextureData00', True, int,
            "Texture data point 0."),
        'faceTexData01': (
            'TextureData01', True, int,
            "Texture data point 1."),
        'faceTexData02': (
            'TextureData02', True, int,
            "Texture data point 2."),
        'faceTexData03': (
            'TextureData03', True, int,
            "Texture data point 3."),
        'faceTexData04': (
            'TextureData04', True, int,
            "Texture data point 4."),
        'faceTexData05': (
            'TextureData05', True, int,
            "Texture data point 5."),
        'faceTexData06': (
            'TextureData06', True, int,
            "Texture data point 6."),
        'faceTexData07': (
            'TextureData07', True, int,
            "Texture data point 7."),
        'faceTexData08': (
            'TextureData08', True, int,
            "Texture data point 8."),
        'faceTexData09': (
            'TextureData09', True, int,
            "Texture data point 9."),
        'faceTexData10': (
            'TextureData10', True, int,
            "Texture data point 10."),
        'faceTexData11': (
            'TextureData11', True, int,
            "Texture data point 11."),
        'faceTexData12': (
            'TextureData12', True, int,
            "Texture data point 12."),
        'faceTexData13': (
            'TextureData13', True, int,
            "Texture data point 13."),
        'faceTexData14': (
            'TextureData14', True, int,
            "Texture data point 14."),
        'faceTexData15': (
            'TextureData15', True, int,
            "Texture data point 15."),
        'faceTexData16': (
            'TextureData16', True, int,
            "Texture data point 16."),
        'faceTexData17': (
            'TextureData17', True, int,
            "Texture data point 17."),
        'faceTexData18': (
            'TextureData18', True, int,
            "Texture data point 18."),
        'faceTexData19': (
            'TextureData19', True, int,
            "Texture data point 19."),
        'faceTexData20': (
            'TextureData20', True, int,
            "Texture data point 20."),
        'faceTexData21': (
            'TextureData21', True, int,
            "Texture data point 21."),
        'faceTexData22': (
            'TextureData22', True, int,
            "Texture data point 22."),
        'faceTexData23': (
            'TextureData23', True, int,
            "Texture data point 23."),
        'faceTexData24': (
            'TextureData24', True, int,
            "Texture data point 24."),
        'faceTexData25': (
            'TextureData25', True, int,
            "Texture data point 25."),
        'faceTexData26': (
            'TextureData26', True, int,
            "Texture data point 26."),
        'faceTexData27': (
            'TextureData27', True, int,
            "Texture data point 27."),
        'faceTexData28': (
            'TextureData28', True, int,
            "Texture data point 28."),
        'faceTexData29': (
            'TextureData29', True, int,
            "Texture data point 29."),
        'faceTexData30': (
            'TextureData30', True, int,
            "Texture data point 30."),
        'faceTexData31': (
            'TextureData31', True, int,
            "Texture data point 31."),
        'faceTexData32': (
            'TextureData32', True, int,
            "Texture data point 32."),
        'faceTexData33': (
            'TextureData33', True, int,
            "Texture data point 33."),
        'faceTexData34': (
            'TextureData34', True, int,
            "Texture data point 34."),
        'faceTexData35': (
            'TextureData35', True, int,
            "Texture data point 35."),
        'faceTexData36': (
            'TextureData36', True, int,
            "Texture data point 36."),
        'faceTexData37': (
            'TextureData37', True, int,
            "Texture data point 37."),
        'faceTexData38': (
            'TextureData38', True, int,
            "Texture data point 38."),
        'faceTexData39': (
            'TextureData39', True, int,
            "Texture data point 39."),
        'faceTexData40': (
            'TextureData40', True, int,
            "Texture data point 40."),
        'faceTexData41': (
            'TextureData41', True, int,
            "Texture data point 41."),
        'faceTexData42': (
            'TextureData42', True, int,
            "Texture data point 42."),
        'faceTexData43': (
            'TextureData43', True, int,
            "Texture data point 43."),
        'faceTexData44': (
            'TextureData44', True, int,
            "Texture data point 44."),
        'faceTexData45': (
            'TextureData45', True, int,
            "Texture data point 45."),
        'faceTexData46': (
            'TextureData46', True, int,
            "Texture data point 46."),
        'faceTexData47': (
            'TextureData47', True, int,
            "Texture data point 47."),
        'faceTexData48': (
            'TextureData48', True, int,
            "Texture data point 48."),
        'faceTexData49': (
            'TextureData49', True, int,
            "Texture data point 49."),
        'hairStyle': (
            'HairStyle', True, FACE_PARAM_HAIRSTYLE_TYPE,
            "Hairstyle of face."),
        'hairColor_Base ': (
            'BaseHairColor', True, FACE_PARAM_HAIRCOLOR_TYPE,
            "Base hair color of face."),
        'hairColor_R ': (
            'HairColorRed', True, int,
            "Red channel of hair color (0 to 255)."),
        'hairColor_G ': (
            'HairColorGreen', True, int,
            "Greenchannel of hair color (0 to 255)."),
        'hairColor_B ': (
            'HairColorBlue', True, int,
            "Blue channel of hair color (0 to 255)."),
        'eyeColor_R': (
            'EyeColorRed', True, int,
            "Red channel of eye color (0 to 255)."),
        'eyeColor_G': (
            'EyeColorGreen', True, int,
            "Green channel of eye color (0 to 255)."),
        'eyeColor_B': (
            'EyeColorBlue', True, int,
            "Blue channel of eye color (0 to 255)."),
        'pad[20]': (
            'Pad1', False, '<Pad:20>',
            "Null padding."),
    },
    'EQUIP_PARAM_GOODS_ST': {
        'refId': _good_ref_id,
        'sfxVariationId': (
            'AnimationVariationID', True, int,
            "Animation variation ID to combine with the base usage animation."),
        'weight': (
            'Weight', False, float,
            "Weight of good. Never used in vanilla Dark Souls."),
        'basicPrice': (
            'BasicCost', False, int,
            "Unsure. Does not appear to be used."),
        'sellValue': (
            'FramptSellValue', True, int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold."),
        'behaviorId': (
            'Behavior', False, Params.Behaviors,
            "Behavior triggered by good use. Never used."),
        'replaceItemId': (
            'GoodToReplace', True, Params.Goods,
            "Good to replace when this item is obtained. Used only for full/empty Estus Flask exchange."),
        'sortId': (
            'SortIndex', True, int,
            "Index for automatic inventory sorting."),
        'qwcId': (
            'QWCID', False, int,
            "Unused world tendency remnant."),
        'yesNoDialogMessageId': (
            'ConfirmationMessage', True, Text.EventText,
            "Message displayed in yes/no dialog box to confirm use of good."),
        'magicId': (
            'Spell', True, Params.Spells,
            "Spell unlocked in attunement menu by possession of this good. (Usually matches the good ID.)"),
        'iconId': (
            'GoodIcon', True, Texture,
            "Good icon texture ID."),
        'modelId': (
            'ModelID', False, Model,
            "Model of good. Never used."),
        'shopLv': (
            'ShopLevel', False, int,
            "Level of good that can be sold in 'the shop'. Always -1 or 0. Probably unused."),
        'compTrophySedId': (
            'CollectionAchievementID', False, int,
            "Collection achievement (e.g. all spells) to which obtaining this good contributes."),
        'trophySeqId': (
            'AchievementID', False, int,
            "Achievement unlocked when this good is first obtained (e.g. Estus Flask)."),
        'maxNum': (
            'MaxHoldQuantity', True, int,
            "Maximum number of good that can be held at once."),
        'consumeHeroPoint': (
            'HumanityCost', False, int,
            "Humanity cost of using good. Always zero."),
        'overDexterity': (
            'OverDexterity', False, int,
            "'Skill over start value'. Unknown effect; set to 0 for spells and 50 otherwise."),
        'goodsType': (
            'GoodType', True, GOODS_TYPE,
            "Determines if this is a basic good, upgrade material, key item, or spell."),
        'refCategory': (
            'ReferenceType', True, BEHAVIOR_REF_TYPE,
            "Indicates if this good triggers a Bullet or Special Effect. (Attacks are possible, but unused.)"),
        'spEffectCategory': (
            'SpecialEffectCategory', True, BEHAVIOR_CATEGORY,
            "Determines compatibility with special effects that affect certain types of attacks. Set to 'Basic' for "
            "thrown goods and 'No Category' otherwise."),
        'goodsCategory': (
            'GoodCategory', False, GOODS_CATEGORY,
            "Never used. Only one value (0) used."),
        'goodsUseAnim': (
            'UseAnimation', True, GOODS_USE_ANIM,
            "Points to basic animation used when good is used. Visual/sound effects are set by the variation ID."),
        'opmeMenuType': (
            'MenuActivated', True, GOODS_OPEN_MENU,
            "Menu activated (if any) when good is used. Generally only 'No Menu' or 'Yes or No Menu' will be useful."),
        'useLimitCategory': (
            'LimitCategory', True, SP_EFFECT_USELIMIT_CATEGORY,
            "Only one good-triggered special effect with this category can be active at once. Additional attempts to "
            "use goods in this category will be prevented. (Unclear how Dragon Stones work, though.)"),
        'replaceCategory': (
            'ReplaceCategory', False, REPLACE_CATEGORY,
            "The special effect triggered by this good will replace any special effects in the same category as this "
            "one. Used only by Dragon Stones."),
        'vowType0:1': (
            'UseableByNoCovenant', True, bool,
            "Determines if this good can be used by characters with no covenant."),
        'vowType1:1': (
            'UseableByWayOfWhite', True, bool,
            "Determines if this good can be used by characters in the Way of White."),
        'vowType2:1': (
            'UseableByPrincessGuard', True, bool,
            "Determines if this good can be used by characters in the Princess's Guard."),
        'vowType3:1': (
            'UseableByWarriorsOfSunlight', True, bool,
            "Determines if this good can be used by characters in the Warriors of Sunlight."),
        'vowType4:1': (
            'UseableByDarkwraith', True, bool,
            "Determines if this good can be used by characters in the Darkwraith covenant."),
        'vowType5:1': (
            'UseableByPathOfTheDragon', True, bool,
            "Determines if this good can be used by characters in the Path of the Dragon."),
        'vowType6:1': (
            'UseableByGravelordServant', True, bool,
            "Determines if this good can be used by characters in the Gravelord Servants."),
        'vowType7:1': (
            'UseableByForestHunter', True, bool,
            "Determines if this good can be used by characters in the Forest Hunters."),
        'vowType8:1': (
            'UseableByDarkmoonBlade', True, bool,
            "Determines if this good can be used by characters in the Blades of the Darkmoon."),
        'vowType9:1': (
            'UseableByChaosServant', True, bool,
            "Determines if this good can be used by characters in the Chaos Servant covenant."),
        'vowType10:1': (
            'UseableByCovenant10', False, bool,
            "Determines if this good can be used by characters in unused covenant 10."),
        'vowType11:1': (
            'UseableByCovenant11', False, bool,
            "Determines if this good can be used by characters in unused covenant 11."),
        'vowType12:1': (
            'UseableByCovenant12', False, bool,
            "Determines if this good can be used by characters in unused covenant 12."),
        'vowType13:1': (
            'UseableByCovenant13', False, bool,
            "Determines if this good can be used by characters in unused covenant 13."),
        'vowType14:1': (
            'UseableByCovenant14', False, bool,
            "Determines if this good can be used by characters in unused covenant 14."),
        'vowType15:1': (
            'UseableByCovenant15', False, bool,
            "Determines if this good can be used by characters in unused covenant 15."),
        'enable_live:1': (
            'UseableByHumans', True, bool,
            "Determines if this good can be used by characters who have revived to Human status."),
        'enable_gray:1': (
            'UseableByHollows', True, bool,
            "Determines if this good can be used by characters who are Hollow."),
        'enable_white:1': (
            'UseableByWhitePhantoms', True, bool,
            "Determines if this good can be used by White Phantoms (summons)."),
        'enable_black:1': (
            'UseableByBlackPhantoms', True, bool,
            "Determines if this good can be used by Black Phantoms (invaders)."),
        'enable_multi:1': (
            'UseableInMultiplayer', True, bool,
            "Determines if this good can be used while multiple players are together."),
        'enable_pvp:1': (  # DSR ONLY
            'UseableInPVP', True, bool,
            "<DSR> Determines if this good can be used in 'PVP' multiplayer. Not sure exactly what that refers to."),
        'disable_offline:1': (
            'DisabledOffline', True, bool,
            "Determines if this good can be used while the game is disconnected from the network."),
        'isEquip:1': (
            'CanBeEquipped', True, bool,
            "Determines if this good can be equipped in a quick item slot."),
        'isConsume:1': (
            'ConsumedOnUse', True, bool,
            "Determines if this good is consumed (count decreases) when used."),
        'isAutoEquip:1': (
            'AutomaticallyEquipped', True, bool,
            "Determines if this good will be equipped in an available quick slot when obtained."),
        'isEstablishment:1': (
            'IsStationary', True, bool,
            "Unknown; need to look at usage."),
        'isOnlyOne:1': (
            'IsUnique', True, bool,
            "Determines if only one of this good exists in the game."),
        'isDrop:1': (
            'CanBeDropped', True, bool,
            "Determines if this item can be dropped."),
        'isDeposit:1': (
            'CanBeStored', True, bool,
            "Determines if good can be stored in Bottomless Box."),
        'isDisableHand:1': (
            'IsDisableHand?', True, bool,
            "Not sure. Could disable model hand when good is used?"),
        'IsTravelItem:1': (
            'IsTravelItem?', True, bool,
            "Not sure. Could flag items that warp the player."),
        'isSuppleItem:1': (
            'Is Empty Estus Flask?', True, bool,
            "Not sure. Only enabled for empty Estus Flask."),
        'isFullSuppleItem:1': (
            'Is Non-Empty Estus Flask?', True, bool,
            "Not sure. Only enabled for non-empty Estus Flask."),
        'isEnhance:1': (
            'IsUpgradeMaterial', True, bool,
            "Determines if this is an upgrade material."),
        'isFixItem:1': (
            'IsFixItem?', True, bool,
            "Probably True for Repair Powder, etc."),
        'disableMultiDropShare:1': (
            'DisableMultiplayerShare', True, bool,
            "If True, this good cannot be given to other players by dropping it."),
        'disableUseAtColiseum:1': (
            'DisabledInArena', False, bool,
            "If True, this good cannot be used in the PvP Arena in Oolacile."),
        'disableUseAtOutOfColiseum:1': (
            'DisabledOutsideArena', False, bool,
            "If True, this good cannot be used outside the PvP Arena in Oolacile."),
        'pad[9]': (
            'Pad1', False, '<Pad:9>',
            "Null padding."),
        'vagrantItemLotId': (
            'VagrantItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantBonusEneDropItemLotId': (
            'VagrantBonusEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantItemEneDropItemLotId': (
            'VagrantItemEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
    },
    'HIT_MTRL_PARAM_ST': {
        'aiVolumeRate': (
            'SoundRadiusMultiplier', True, float,
            "Multiplier for foot sound effect radius on this terrain."),
        'spEffectIdOnHit0': (
            'SpecialEffect1', True, Params.SpecialEffects,
            "Special effect applied to character walking on terrain (first of two)."),
        'spEffectIdOnHit1': (
            'SpecialEffect2', True, Params.SpecialEffects,
            "Special effect applied to character walking on terrain (second of two)."),
        'footEffectHeightType:2': (
            'FootEffectHeightType', True, HMP_FOOT_EFFECT_HEIGHT_TYPE,
            "Determines the height at which foot impact effects are generated."),
        'footEffectDirType:2': (
            'FootEffectDirectionType', True, HMP_FOOT_EFFECT_DIR_TYPE,
            "Determines the direction of foot impact effects."),
        'floorHeightType:2': (
            'TerrainHeightType', True, HMP_FLOOR_HEIGHT_TYPE,
            "Determines distance from floor collision at which effects are applied."),
        'pad0[3]': (
            'Pad1', False, '<Pad:3>',
            "Null padding."),
    },
    'ITEMLOT_PARAM_ST': {
        'getItemFlagId': (
            'ItemFlag', True, Flag,
            "Flag enabled when any item from this item lot is picked up."),
        'cumulateNumFlagId': (
            'FirstCumulativeFlag', True, Flag,
            "First of eight consecutive flags used to store the cumulative points for this item lot."),
        'cumulateNumMax': (
            'MaxCumulativeAdditions', True, int,
            "Maximum number of times that cumulative points will be added to the total. I suspect that the cumulative "
            "slot may be awarded automatically after this; if not, I don't know how the Symbol of Avarice always drops "
            "after all seven Mimics are killed."),
        'lotItem_Rarity': (
            'ItemLotRarity', True, int,
            "Overall rarity of item lot, from 0 to 3. Used fairly consistently, but seems to have no effect. Set to 2 "
            "for all character drops except Crystal Lizards, who have 3."),

        'lotItemCategory01': (
            'Item1Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 1)."),
        'lotItemId01': partial(_item_lot_item_id, 1),
        'lotItemNum01': (
            'Item1Count', True, int,
            "Count of item (slot 1)."),
        'lotItemBasePoint01': (
            'Item1ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId01': (
            'Item1Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck01:1': (
            'Item1LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint01': (
            'Item1CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset01:1': (
            'Item1ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory02': (
            'Item2Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 2)."),
        'lotItemId02': partial(_item_lot_item_id, 2),
        'lotItemNum02': (
            'Item2Count', True, int,
            "Count of item (slot 2)."),
        'lotItemBasePoint02': (
            'Item2ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId02': (
            'Item2Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck02:1': (
            'Item2LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint02': (
            'Item2CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset02:1': (
            'Item2ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory03': (
            'Item3Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 3)."),
        'lotItemId03': partial(_item_lot_item_id, 3),
        'lotItemNum03': (
            'Item3Count', True, int,
            "Count of item (slot 3)."),
        'lotItemBasePoint03': (
            'Item3ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId03': (
            'Item3Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck03:1': (
            'Item3LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint03': (
            'Item3CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset03:1': (
            'Item3ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory04': (
            'Item4Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 4)."),
        'lotItemId04': partial(_item_lot_item_id, 4),
        'lotItemNum04': (
            'Item4Count', True, int,
            "Count of item (slot 4)."),
        'lotItemBasePoint04': (
            'Item4ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId04': (
            'Item4Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck04:1': (
            'Item4LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint04': (
            'Item4CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset04:1': (
            'Item4ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory05': (
            'Item5Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 5)."),
        'lotItemId05': partial(_item_lot_item_id, 5),
        'lotItemNum05': (
            'Item5Count', True, int,
            "Count of item (slot 5)."),
        'lotItemBasePoint05': (
            'Item5ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId05': (
            'Item5Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck05:1': (
            'Item5LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint05': (
            'Item5CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset05:1': (
            'Item5ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory06': (
            'Item6Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 6)."),
        'lotItemId06': partial(_item_lot_item_id, 6),
        'lotItemNum06': (
            'Item6Count', True, int,
            "Count of item (slot 6)."),
        'lotItemBasePoint06': (
            'Item6ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId06': (
            'Item6Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck06:1': (
            'Item6LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint06': (
            'Item6CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset06:1': (
            'Item6ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory07': (
            'Item7Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 7)."),
        'lotItemId07': partial(_item_lot_item_id, 7),
        'lotItemNum07': (
            'Item7Count', True, int,
            "Count of item (slot 7)."),
        'lotItemBasePoint07': (
            'Item7ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId07': (
            'Item7Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck07:1': (
            'Item7LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint07': (
            'Item7CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset07:1': (
            'Item7ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory08': (
            'Item8Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 8)."),
        'lotItemId08': partial(_item_lot_item_id, 8),
        'lotItemNum08': (
            'Item8Count', True, int,
            "Count of item (slot 8)."),
        'lotItemBasePoint08': (
            'Item8ChancePoints', True, int,
            "Relative chance (divided by total chance points across all eight slots) that this item will be dropped."),
        'getItemFlagId08': (
            'Item8Flag', False, Flag,
            "Flag that will be enabled when this exact item slot is dropped (and presumably picked up). Never used."),
        'enableLuck08:1': (
            'Item8LuckEnabled', True, bool,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint08': (
            'Item8CumulativePoints', True, int,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset08:1': (
            'Item8ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),
    },
    'MENU_PARAM_COLOR_TABLE_ST': {
        'r': ('RedChannel', True, int, "Red value of RGBA color (0-255)."),
        'g': ('GreenChannel', True, int, "Green value of RGBA color (0-255)."),
        'b': ('BlueChannel', True, int, "Blue value of RGBA color (0-255)."),
        'a': ('AlphaChannel', True, int, "Alpha value of RGBA color (0-255). Higher means less transparent."),
    },
    'NPC_PARAM_ST': {
        'behaviorVariationId': (
            'BehaviorVariationID', True, int,
            "DOC-TODO"),
        'aiThinkId': (
            'AiThinkID', True, Params.AI,
            "DOC-TODO"),
        'nameId': (
            'NameID', True, Text.NPCNames,
            "DOC-TODO"),
        'turnVellocity': (
            'TurnVelocity', True, float,
            "DOC-TODO"),
        'hitHeight': (
            'HitHeight', True, float,
            "DOC-TODO"),
        'hitRadius': (
            'HitRadius', True, float,
            "DOC-TODO"),
        'weight': (
            'Weight', True, int,
            "DOC-TODO"),
        'hitYOffset': (
            'HitYOffset', False, float,
            "DOC-TODO"),
        'hp': (
            'MaximumHP', True, int,
            "DOC-TODO"),
        'mp': (
            'MaximumMP', True, int,
            "DOC-TODO"),
        'getSoul': (
            'SoulReward', True, int,
            "DOC-TODO"),
        'itemLotId_1': (
            'ItemLotID1', True, Params.ItemLots,
            "DOC-TODO"),
        'itemLotId_2': (
            'ItemLotID2', True, Params.ItemLots,
            "DOC-TODO"),
        'itemLotId_3': (
            'ItemLotID3', True, Params.ItemLots,
            "DOC-TODO"),
        'itemLotId_4': (
            'ItemLotID4', True, Params.ItemLots,
            "DOC-TODO"),
        'itemLotId_5': (
            'ItemLotID5', True, Params.ItemLots,
            "DOC-TODO"),
        'itemLotId_6': (
            'ItemLotID6', True, Params.ItemLots,
            "DOC-TODO"),
        'humanityLotId': (
            'HumanityLotID', True, Flag,
            "DOC-TODO"),
        'spEffectID0': (
            'SpecialEffectID0', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID1': (
            'SpecialEffectID1', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID2': (
            'SpecialEffectID2', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID3': (
            'SpecialEffectID3', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID4': (
            'SpecialEffectID4', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID5': (
            'SpecialEffectID5', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID6': (
            'SpecialEffectID6', True, Params.SpecialEffects,
            "DOC-TODO"),
        'spEffectID7': (
            'SpecialEffectID7', True, Params.SpecialEffects,
            "DOC-TODO"),
        'GameClearSpEffectID': (
            'NewGamePlusSpecialEffect', True, Params.SpecialEffects,
            "DOC-TODO"),
        'physGuardCutRate': (
            'PhysicalGuardCutRate', True, float,
            "DOC-TODO"),
        'magGuardCutRate': (
            'MagicGuardCutRate', True, float,
            "DOC-TODO"),
        'fireGuardCutRate': (
            'FireGuardCutRate', True, float,
            "DOC-TODO"),
        'thunGuardCutRate': (
            'LightningGuardCutRate', True, float,
            "DOC-TODO"),
        'animIdOffset': (
            'AnimationIDOffset', True, int,
            "DOC-TODO"),
        'moveAnimId': (
            'MoveAnimationID', False, Animation,
            "DOC-TODO"),
        'spMoveAnimId1': (
            'SpecialMoveAnimationID1', False, Animation,
            "DOC-TODO"),
        'spMoveAnimId2': (
            'SpecialMoveAnimationID2', False, Animation,
            "DOC-TODO"),
        'networkWarpDist': (
            'NetworkWarpDistance', False, int,
            "DOC-TODO"),
        'dbgBehaviorR1': (
            'DebugBehaviorR1', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorL1': (
            'DebugBehaviorL1', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorR2': (
            'DebugBehaviorR2', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorL2': (
            'DebugBehaviorL2', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorRL': (
            'DebugBehaviorRL', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorRR': (
            'DebugBehaviorRR', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorRD': (
            'DebugBehaviorRD', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorRU': (
            'DebugBehaviorRU', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorLL': (
            'DebugBehaviorLL', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorLR': (
            'DebugBehaviorLR', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorLD': (
            'DebugBehaviorLD', False, Animation,
            "DOC-TODO"),
        'dbgBehaviorLU': (
            'DebugBehaviorLU', False, Animation,
            "DOC-TODO"),
        'animIdOffset2': (
            'AnimationIDOffset2', False, int,
            "DOC-TODO"),
        'partsDamageRate1': (
            'Part1DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate2': (
            'Part2DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate3': (
            'Part3DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate4': (
            'Part4DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate5': (
            'Part5DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate6': (
            'Part6DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate7': (
            'Part7DamageRate', True, float,
            "DOC-TODO"),
        'partsDamageRate8': (
            'Part8DamageRate', True, float,
            "DOC-TODO"),
        'weakPartsDamageRate': (
            'WeakPartsDamageRate', True, float,
            "DOC-TODO"),
        'superArmorRecoverCorrection': (
            'PoiseRecoveryCorrection', True, float,
            "DOC-TODO"),
        'superArmorBrakeKnockbackDist': (
            'StaggerKnockbackDistance', True, float,
            "DOC-TODO"),
        'stamina': (
            'MaxStamina', True, int,
            "DOC-TODO"),
        'staminaRecoverBaseVel': (
            'StaminaRecoveryBaseSpeed', True, int,
            "DOC-TODO"),
        'def_phys': (
            'PhysicalDefense', True, int,
            "Base defense applied to all physical attacks."),
        'def_slash': (
            'SlashDefense', True, int,
            "Base defense added against slashing physical attacks."),
        'def_blow': (
            'StrikeDefense', True, int,
            "Base defense added against striking physical attacks."),
        'def_thrust': (
            'ThrustDefense', True, int,
            "Base defense added against thrusting physical attacks."),
        'def_mag': (
            'MagicDefense', True, int,
            "DOC-TODO"),
        'def_fire': (
            'FireDefense', True, int,
            "DOC-TODO"),
        'def_thunder': (
            'LightningDefense', True, int,
            "DOC-TODO"),
        'defFlickPower': (
            'DefenseRepelPower', False, int,
            "Determines how badly an attacker is repelled when they fail to break this NPC's "
            "poise. The Armored Tusk and Chained Prisoner have very high values (50-60), but most "
            "NPCs have 0."),
        'resist_poison': (
            'PoisonResistance', True, int,
            "Base poison resistance."),
        'resist_desease': (
            'ToxicResistance', True, int,
            "Base toxic resistance."),
        'resist_blood': (
            'BleedResistance', True, int,
            "Base bleed resistance."),
        'resist_curse': (
            'CurseResistance', True, int,
            "Base curse resistance."),
        'ghostModelId': (
            'GhostModelID', False, Model,
            "Model to be used when this quest-related NPC appears as a ghost to other players. Defaults "
            "to -1 for almost all standard enemies, which means they do not appear as a ghost to others."),
        'normalChangeResouceId': (
            'NormalChangeResourceID', False, int,
            "Unknown. Always -1."),
        'guardAngle': (
            'GuardAngle', False, int,
            "Zero for every NPC except the Phalanx Hollow (20)."),
        'slashGuardCutRate': (
            'SlashDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'blowGuardCutRate': (
            'StrikeDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'thrustGuardCutRate': (
            'ThrustDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'superArmorDurability': (
            'MaxPoise', True, int,
            "Maximum poise of character. Poise is reduced when attacked, but quickly refills. If reduced to zero, the "
            "character will be staggered."),
        'normalChangeTexChrId': (
            'NormalChangeTextureChrID', False, int,
            "Unknown. Used for only some NPCs, where it is generally set to a number close to "
            "the NPC's character model ID."),
        'dropType': (
            'ItemDropAppearance', True, NPC_ITEMDROP_TYPE,
            "Determines appearance of dropped items. 0 means the item appears to glow faintly from inside the "
            "NPC's body (e.g. Rat, Mushroom Child/Parent, Ent) and 1 means the item is a clear white orb "
            "just like regular treasure on corpses (most NPCs)."),
        'knockbackRate': (
            'KnockbackRate', True, int,
            "DOC-TODO"),
        'knockbackParamId': (
            'KnockbackID', True, Params.Knockback,
            "Knockback parameters were abandoned after Demons' Souls."),
        'fallDamageDump': (
            'FallDamageReduction', True, int,
            "Percentage of fall damage to ignore."),
        'staminaGuardDef': (
            'StaminaGuardDefense', True, int,
            "Always set to zero in the game, but presumably, increasing it will reduce the amount of "
            "stamina lost when this NPC blocks an attack."),
        'pcAttrB': (
            'PCAttrB', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'pcAttrW': (
            'PCAttrW', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'pcAttrL': (
            'PCAttrL', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'pcAttrR': (
            'PCAttrR', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'areaAttrB': (
            'AreaAttrB', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'areaAttrW': (
            'AreaAttrW', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'areaAttrL': (
            'AreaAttrL', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'areaAttrR': (
            'AreaAttrR', False, int,
            "Like a remnant of World Tendency. Always set to zero."),
        'mpRecoverBaseVel': (
            'MPRecoveryBaseSpeed', False, int,
            "Unknown effect, likely none. Set to zero for NPC parts (tails and Hydra heads) and 10 "
            "for everyone else."),
        'flickDamageCutRate': (
            'RepelDamageCutRate', False, int,
            "Unknown effect, but it is set to zero for most enemies, 50 for very heavy enemies "
            "like Great Stone Knights and Titanite Demons, and 100 for Mimics."),
        'defaultLodParamId': (
            'DefaultLightingParamID', False, '<Lighting:Lod>',  # TODO
            "Default lighting."),
        'drawType': (
            'DrawType', True, NPC_DRAW_TYPE,
            "DOC-TODO"),
        'npcType': (
            'NPCType', True, NPC_TYPE,
            "DOC-TODO"),
        'teamType': (
            'TeamType', True, NPC_TEMA_TYPE,
            "0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom"),
        'moveType': (
            'MoveType', True, NPC_MOVE_TYPE,
            "DOC-TODO"),
        'lockDist': (
            'LockOnDistance', True, int,
            "DOC-TODO"),
        'material': (
            'Material', False, int,
            "DOC-TODO"),
        'materialSfx': (
            'MaterialSFX', False, int,
            "DOC-TODO"),
        'material_Weak': (
            'MaterialWeak', False, int,
            "DOC-TODO"),
        'materialSfx_Weak': (
            'MaterialWeakSFX', False, int,
            "DOC-TODO"),
        'partsDamageType': (
            'PartsDamageType', False, int,
            "Unknown. Seems to be set to 1 for most enemies with multiple parts (Sentinels, Quelaag, "
            "Seath, Gaping Dragon), but not all of them (Bell Gargoyles), and 0 otherwise."),
        'maxUndurationAng': (
            'MaxUndurationAngle', False, int,
            "Unknown effect, but it is generally set to 30 for all four-legged enemies, and 0 for all "
            "others."),
        'guardLevel': (
            'GuardLevel', False, GUARDMOTION_CATEGORY,  # TODO: possibly GUARDMOTION_CATEGORY
            "Set to 4 for enemies who can guard (including Manus), except Giant "
            "Skeletons, who have a value of 3. All other NPCs have zero."),
        'burnSfxType': (
            'BurnSFXType', False, NPC_BURN_TYPE,
            "Set to 1 for Slimes and Undead Dragons, and 0 for everyone else."),
        'poisonGuardResist': (
            'PoisonGuardResistance', True, int,
            "Added poison resistance while guarding."),
        'diseaseGuardResist': (
            'ToxicGuardResistance', True, int,
            "Added toxic resistance while guarding."),
        'bloodGuardResist': (
            'BleedGuardResistance', True, int,
            "Added bleed resistance while guarding."),
        'curseGuardResist': (
            'CurseGuardResistance', True, int,
            "Added curse resistance while guarding."),
        'parryAttack': (
            'ParryAttack', False, int,
            "Always zero."),
        'parryDefence': (
            'ParryDefense', False, int,
            "Always zero."),
        'sfxSize': (
            'SFXSize', False, NPC_SFX_SIZE,
            "Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise."),
        'pushOutCamRegionRadius': (
            'PushOutCameraRegionRadius', False, int,
            "Always zero."),
        'hitStopType': (
            'HitStopType', False, NPC_HITSTOP_TYPE,
            "Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely related to AI triggers."),
        'ladderEndChkOffsetTop': (
            'LadderEndCheckOffsetTop', False, int,
            "Not something you want to mess with."),
        'ladderEndChkOffsetLow': (
            'LadderEndCheckOffsetBottom', False, int,
            "Not something you want to mess with."),
        'useRagdollCamHit:1': (
            'UseRagdollCameraHit', False, bool,
            "DOC-TODO"),
        'disableClothRigidHit:1': (
            'DisableClothRigidHit', False, bool,
            "DOC-TODO"),
        'useRagdoll:1': (
            'UseRagdoll', False, bool,
            "DOC-TODO"),
        'isDemon:1': (
            'IsDemon', True, bool,
            "DOC-TODO"),
        'isGhost:1': (
            'IsGhost', True, bool,
            "DOC-TODO"),
        'isNoDamageMotion:1': (
            'IsNoDamageMotion', True, bool,
            "DOC-TODO"),
        'isUnduration:1': (
            'IsUnduration', False, bool,
            "DOC-TODO"),
        'isChangeWanderGhost:1': (
            'IsChangeWanderGhost', False, bool,
            "Always false."),
        'modelDispMask0:1': (
            'ModelDisplayMask0', False, bool,
            "DOC-TODO"),
        'modelDispMask1:1': (
            'ModelDisplayMask1', False, bool,
            "DOC-TODO"),
        'modelDispMask2:1': (
            'ModelDisplayMask2', False, bool,
            "DOC-TODO"),
        'modelDispMask3:1': (
            'ModelDisplayMask3', False, bool,
            "DOC-TODO"),
        'modelDispMask4:1': (
            'ModelDisplayMask4', False, bool,
            "DOC-TODO"),
        'modelDispMask5:1': (
            'ModelDisplayMask5', False, bool,
            "DOC-TODO"),
        'modelDispMask6:1': (
            'ModelDisplayMask6', False, bool,
            "DOC-TODO"),
        'modelDispMask7:1': (
            'ModelDisplayMask7', False, bool,
            "DOC-TODO"),
        'modelDispMask8:1': (
            'ModelDisplayMask8', False, bool,
            "DOC-TODO"),
        'modelDispMask9:1': (
            'ModelDisplayMask9', False, bool,
            "DOC-TODO"),
        'modelDispMask10:1': (
            'ModelDisplayMask10', False, bool,
            "DOC-TODO"),
        'modelDispMask11:1': (
            'ModelDisplayMask11', False, bool,
            "DOC-TODO"),
        'modelDispMask12:1': (
            'ModelDisplayMask12', False, bool,
            "DOC-TODO"),
        'modelDispMask13:1': (
            'ModelDisplayMask13', False, bool,
            "DOC-TODO"),
        'modelDispMask14:1': (
            'ModelDisplayMask14', False, bool,
            "DOC-TODO"),
        'modelDispMask15:1': (
            'ModelDisplayMask15', False, bool,
            "DOC-TODO"),
        'isEnableNeckTurn:1': (
            'IsEnableNeckTurn', False, bool,
            "DOC-TODO"),
        'disableRespawn:1': (
            'DisableRespawnOnRest', True, bool,
            "Prevents NPC from respawning when you rest at a bonfire, though they will still respawn "
            "when you die or the map is de-loaded unless they are disabled by an event script."),
        'isMoveAnimWait:1': (
            'IsMoveAnimationWait', False, bool,
            "DOC-TODO"),
        'isCrowd:1': (
            'IsCrowd', False, bool,
            "Always false."),
        'isWeakSaint:1': (
            'IsWeakToDivine', True, bool,
            "True for skeletons and friends, but not sure how it is actually used to disable their "
            "reanimation by Necromancers."),
        'isWeakA:1': (
            'IsWeakToOccult', True, bool,
            "True for all Gods and most NPCs in Anor Londo."),
        'isWeakB:1': (
            'IsAbyssal', True, bool,
            "True for Darkwraiths, Primordial Serpents, and the Four Kings, but not Manus."),
        'pad1:1': (
            'Pad1', False, '<Pad:1>',
            "DOC-TODO"),
        'vowType:3': (
            'VowType', False, int,
            "Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone else."),
        'disableInitializeDead:1': (
            'DisableInitializeDead', False, bool,
            "True for bosses and non-respawning enemies that are disabled in event scripts, "
            "but its effects are unknown."),
        'pad3:4': (
            'Pad2', False, '<Pad:4>',
            "DOC-TODO"),
        'pad2[6]': (
            'Pad3', False, '<Pad:6>',
            "DOC-TODO"),
    },
    'EQUIP_PARAM_ACCESSORY_ST': {
        'refId': (
            'SpecialEffect', True, Params.SpecialEffects,
            "Special effect applied when ring is equipped."),
        'sfxVariationId': (
            'SFXVariation', False, int,
            "SFX variation ID combined with the value specified in TAE animation data. Always -1; likely works with "
            "unused Behavior parameter below."),
        'weight': (
            'Weight', False, float,
            "Weight of ring. Always set to zero in vanilla Dark Souls, but likely works just like other equipment."),
        'behaviorId': (
            'Behavior', False, Params.Behaviors,
            "Behavior of ring 'skill'. Always zero in the vanilla game."),
        'basicPrice': (
            'BasicCost', False, int,
            "Unknown purpose, and unused."),
        'sellValue': (
            'FramptSellValue', True, int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold."),
        'sortId': (
            'SortIndex', True, int,
            "Index for automatic inventory sorting."),
        'qwcId': (
            'QWCID', False, int,
            "Unused world tendency remnant."),
        'equipModelId': (
            'EquipmentModel', False, Model,
            "Always zero. (Rings have no model, presumably.)"),
        'iconId': (
            'MenuIcon', True, Texture,
            "Icon ID of ring in menu."),
        'shopLv': (
            'ShopLevel', False, int,
            "Internal description: 'Level that can be solved in the shop.' Unknown and unused (rings have no level)."),
        'trophySGradeId': (
            'AchievementContributionID', False, int,
            "Index of ring as it contributes to certain multi-item achievements (none for rings)."),
        'trophySeqId': (
            'AchievementUnlockID', False, int,
            "Achievement unlocked when ring is acquired (Covenant of Artorias)."),
        'equipModelCategory': (
            'EquipmentModelCategory', False, EQUIP_MODEL_CATEGORY,
            "Always zero."),
        'equipModelGender': (
            'EquipmentModelGender', False, EQUIP_MODEL_GENDER,
            "Always zero."),
        'accessoryCategory': (
            'AccessoryCategory', False, ACCESSORY_CATEGORY,
            "Always zero."),
        'refCategory': (
            'ReferenceType', False, BEHAVIOR_REF_TYPE,
            "Always set to Special Effects. No idea what happens if you set it to Attacks for a ring..."),
        'spEffectCategory': (
            'SpecialEffectCategory', False, SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this equipment. Unused for rings."),
        'pad[1]': (
            'Pad1', False, '<Pad:1>',
            "Null padding."),
        'vagrantItemLotId': (
            'VagrantItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantBonusEneDropItemLotId': (
            'VagrantBonusEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantItemEneDropItemLotId': (
            'VagrantItemEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'isDeposit:1': (
            'CanBeStored', False, bool,
            "If True, this ring can be stored in the Bottomless Box. Always True for rings."),
        'isEquipOutBrake:1': (
            'BreaksWhenUnequipped', True, bool,
            "If True, this ring will break when it is unequipped (e.g. Ring of Favor and Protection)."),
        'disableMultiDropShare:1': (
            'DisableMultiplayerShare', False, bool,
            "If True, this ring cannot be given to other players by dropping it. Always False in vanilla."),
        'pad1[3]': (
            'Pad2', False, '<Pad:3>',
            "Null padding."),
    },
    'OBJECT_PARAM_ST': {
        'hp': (
            'ObjectHP', True, int,
            "Amount of damage object can take before it is destroyed. (Set to -1 for invulnerability.)"),
        'defense': (
            'MinAttackForDamage', True, int,
            "Minimum attack power required to damage object. Attacks with less power than this will deal no damage."),
        'extRefTexId': (
            'ExternalTextureID', False, int,
            "Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area number)'."),
        'materialId': (
            'MaterialID', True, Params.Terrains,
            "Treated the same as floor material. (Set to -1 to use default.)"),
        'animBreakIdMax': (
            'MaxDestructionAnimationID', False, Animation,
            "Upper limit of range of destruction animations, which seem to always start at 0."),
        'isCamHit:1': (
            'CollidesWithCamera', True, bool,
            "If True, the camera will collide with this object."),
        'isBreakByPlayerCollide:1': (
            'BrokenByPlayerCollision', True, bool,
            "If True, the player will break the object just by touching it."),
        'isAnimBreak:1': (
            'HasDestructionAnimation', True, bool,
            "If True, the object will use an animation when destroyed rather than using physics-based destruction."),
        'isPenetrationBulletHit:1': (
            'HitByPiercingBullets', True, bool,
            "If True, the object can be damaged by Bullets with target-piercing enabled."),
        'isChrHit:1': (
            'CharacterCollision', True, bool,
            "If False, characters will pass through the object (e.g. branches)."),
        'isAttackBacklash:1': (
            'DeflectsAttacks', True, bool,
            "If True, attacks will bounce off the object as though it were a wall."),
        'isDisableBreakForFirstAppear:1': (
            'CannotSpawnBroken', True, bool,
            "If True, the object cannot be destroyed when the player first spawns."),
        'isLadder:1': (
            'IsLadder', True, bool,
            "Object is a ladder."),
        'isAnimPauseOnRemoPlay:1': (
            'StopAnimationDuringCutscenes', True, bool,
            "If True, object animation will not play in cutscenes."),
        'isDamageNoHit:1': (
            'PreventAllDamage', True, bool,
            "If True, all damage to the object will be prevented. (Not sure if this is the same effet as settings its "
            "HP to -1.)"),
        'isMoveObj:1': (
            'IsMovingObject', True, bool,
            "If True, this object can move."),
        'pad_1:5': (
            'Pad1', False, '<Pad:5>', "Null padding."),
        'defaultLodParamId': (
            'DefaultLOD', True, int,  # TODO: LOD.
            "Default LOD (level of default) parameter."),
        'breakSfxId': (
            'DestructionSoundEffect', True, Sound.SFX,
            "Sound effect played upon destruction. (Set to -1 to use default value, which is apparently 80.)"),
    },
    'OBJ_ACT_PARAM_ST': {
        'actionEnableMsgId': (
            'SuccessMessage', True, Text.EventText,
            "Message displayed in dialog box upon successful action (e.g. 'Door opened')."),
        'actionFailedMsgId': (
            'FailureMessage', True, Text.EventText,
            "Message displayed in dialog box upon failed action (e.g. 'Door locked')."),
        'spQualifiedPassEventFlag': (
            'FlagForAutomaticSuccess', True, Flag,
            "Action will always be successful if this flag is enabled."),
        'validDist': (
            'MaxActionDistance', True, float,
            "Maximum distance from action model point at which the object action will be prompted."),
        'playerAnimId': (
            'PlayerActionAnimation', True, Animation,
            "Animation played by a player character when they successfully activate the object."),
        'chrAnimId': (
            'NonPlayerActionAnimation', True, Animation,
            "Animation played by a non-player character when they successfully activate the object."),
        'spQualifiedType': (
            'SuccessCondition1Type', True, OBJACT_SP_QUALIFIED_TYPE,
            "Type of first success condition."),
        'spQualifiedId': partial(_obj_act_success_condition, 'spQualifiedType'),
        'spQualifiedType2': (
            'SuccessCondition2Type', True, OBJACT_SP_QUALIFIED_TYPE,
            "Type of second success condition."),
        'spQualifiedId2': partial(_obj_act_success_condition, 'spQualifiedType2'),
        'objDummyId': (
            'ObjectActionModelPoint', True, int,
            "Model point that specifies where the action occurs on the object (for snapping the player and distance "
            "check)."),
        'objAnimId': (
            'ObjectActionAnimation', True, Animation,
            "Animation played by the object when it is successfully activated."),
        'validPlayerAngle': (
            'MaxPlayerAngle', True, int,
            "Maximum angle between the character's forward direction and the direction to the object "
            "action point for the action prompt to appear."),
        'validObjAngle': (
            'MaxObjectAngle', True, int,
            "Maximum angle between the object's forward direction and the direction to the player for "
            "the action prompt to appear."),
        'chrSorbType': (
            'CharacterSnapType', True, OBJACT_CHR_SORB_TYPE,
            "Type of method used to snap the character to the object before animations are played."),
        'eventKickTiming': (
            'EventTriggerDelay', True, int,
            "I believe this is the delay between successful object activation and the outgoing "
            "'success' trigger used by game events."),
        'pad1[2]': (
            'Pad1', False, '<Pad:2>',
            "Null padding."),

    },
    'SHOP_LINEUP_PARAM': {
        'equipId': _shop_item_id,
        'value': (
            'SoulCost', True, int,
            "Cost of item, in souls."),
        'mtrlId': (
            'RequiredGood', True, Params.Goods,
            "Good that must be possessed for item to be listed. Used to control appearance of spells in attunement "
            "menu."),
        'eventFlag': (
            'QuantityFlag', True, Flag,
            "Flag value that holds the count of this item that have been sold already."),
        'qwcId': (
            'QWCID', False, int,
            "Unused world tendency condition."),
        'sellQuantity': (
            'InitialQuantity', True, int,
            "Quantity of this item initially available to be sold. Set to -1 for infinite quantity."),
        'shopType': (
            'ShopMenuType', True, SHOP_LINEUP_SHOPTYPE,
            "Determines if this is a standard shop menu or the spell attunement menu."),
        'equipType': (
            'ItemType', True, SHOP_LINEUP_EQUIPTYPE,
            "Type of item listed in menu."),
        'pad_0[8]': (
            'Pad1', False, '<Pad:8>',
            "Null padding."),
    },
    'SP_EFFECT_PARAM_ST': {
        'iconId': (
            'StatusIcon', True, Texture,
            "Icon that appears in HUD under stamina bar while special effect is active. Set to -1 for no icon."),
        'conditionHp': (
            'MaxHPPercentageForEffect', True, float,
            "Special effect will only take effect if character's current HP is less than or equal to this percentage "
            "(from 0 to 100). Set to -1 for no HP condition."),
        'effectEndurance': (
            'EffectDuration', True, float,
            "Duration of special effect. Set to 0 for an effect that occurs for only one frame (e.g. to award souls) "
            "or to -1 for an effect that will last until specifically removed or its source is lost (e.g. rings)."),
        'motionInterval': (
            'UpdateInterval', True, float,
            "Time (in seconds) between applications of the special effect, while active. Set to higher values to have "
            "the effect apply less frequently. Set to 0 to have it occur every frame."),
        'maxHpRate': (
            'MaxHPMultiplier', True, float,
            "Multiplier applied to maximum HP."),
        'maxMpRate': (
            'MaxMPMultiplier', False, float,
            "Multiplier applied to maximum MP. (Unused in Dark Souls; does NOT refer to spell usages.)"),
        'maxStaminaRate': (
            'MaxStaminaMultiplier', True, float,
            "Multiplier applied to maximum stamina."),
        'slashDamageCutRate': (
            'IncomingSlashDamageMultiplier', True, float,
            "Multiplier applied to incoming slashing physical damage."),
        'blowDamageCutRate': (
            'IncomingStrikeDamageMultiplier', True, float,
            "Multiplier applied to incoming striking physical damage."),
        'thrustDamageCutRate': (
            'IncomingThrustDamageMultiplier', True, float,
            "Multiplier applied to incoming thrusting physical damage."),
        'neutralDamageCutRate': (
            'IncomingNeutralDamageMultiplier', True, float,
            "Multiplier applied to incoming neutral physical damage."),
        'magicDamageCutRate': (
            'IncomingMagicDamageMultiplier', True, float,
            "Multiplier applied to incoming magic damage."),
        'fireDamageCutRate': (
            'IncomingFireDamageMultiplier', True, float,
            "Multiplier applied to incoming fire damage."),
        'thunderDamageCutRate': (
            'IncomingLightningDamageMultiplier', True, float,
            "Multiplier applied to incoming lightning damage."),
        'physicsAttackRate': (
            'OutgoingPhysicalDamageMultiplier', True, float,
            "Multiplier applied to outgoing physical damage (of any type)."),
        'magicAttackRate': (
            'OutgoingMagicDamageMultiplier', True, float,
            "Multiplier applied to outgoing magic damage."),
        'fireAttackRate': (
            'OutgoingFireDamageMultiplier', True, float,
            "Multiplier applied to outgoing fire damage."),
        'thunderAttackRate': (
            'OutgoingLightningDamageMultiplier', True, float,
            "Multiplier applied to outgoing lightning damage."),
        'physicsAttackPowerRate': (
            'PhysicalAttackPowerMultiplier', True, float,
            "Multiplier applied to character's physical attack power (of any type)."),
        'magicAttackPowerRate': (
            'MagicAttackPowerMultiplier', True, float,
            "Multiplier applied to character's magic attack power."),
        'fireAttackPowerRate': (
            'FireAttackPowerMultiplier', True, float,
            "Multiplier applied to character's fire attack power."),
        'thunderAttackPowerRate': (
            'LightningAttackPowerMultiplier', True, float,
            "Multiplier applied to character's lightning attack power."),
        'physicsAttackPower': (
            'PhysicalAttackPowerAddition', True, int,
            "Value to add to or subtract fromcharacter's physical attack power (of any type)."),
        'magicAttackPower': (
            'MagicAttackPowerAddition', True, int,
            "Value to add to or subtract fromcharacter's magic attack power."),
        'fireAttackPower': (
            'FireAttackPowerAddition', True, int,
            "Value to add to or subtract fromcharacter's fire attack power."),
        'thunderAttackPower': (
            'LightningAttackPowerAddition', True, int,
            "Value to add to or subtract fromcharacter's lightning attack power."),
        'physicsDiffenceRate': (
            'PhysicalDefenseMultiplier', True, float,
            "Multiplier applied to character's physical defense (all types)."),
        'magicDiffenceRate': (
            'MagicDefenseMultiplier', True, float,
            "Multiplier applied to character's magic defense."),
        'fireDiffenceRate': (
            'FireDefenseMultiplier', True, float,
            "Multiplier applied to character's fire defense."),
        'thunderDiffenceRate': (
            'LightningDefenseMultiplier', True, float,
            "Multiplier applied to character's lightning defense."),
        'physicsDiffence': (
            'PhysicalDefenseAddition', True, float,
            "Value to add to or subtract from character's physical defense."),
        'magicDiffence': (
            'MagicDefenseAddition', True, float,
            "Value to add to or subtract from character's magic defense."),
        'fireDiffence': (
            'FireDefenseAddition', True, float,
            "Value to add to or subtract from character's fire defense."),
        'thunderDiffence': (
            'LightningDefenseAddition', True, float,
            "Value to add to or subtract from character's lightning defense."),
        'NoGuardDamageRate': (
            'NoGuardIncomingDamageMultiplier', False, float,
            "Multiplier to use instead of usual multiplier if character is not guarding. (Always set to 0 in vanilla "
            "game, which must deactivate it. Only an educated guess that it refers to incoming damage, not outgoing.)"),
        'vitalSpotChangeRate': (
            'CriticalHitIncomingDamageMultiplier', False, float,
            "Multiplier to use instead of usual multiplier if character is hit in a weak spot. (Always set to -1 in "
            "vanilla game, which deactivates it. Only an educated guess that it affects incoming damage.)"),
        'normalSpotChangeRate': (
            'NonCriticalHitIncomingDamageMultiplier', False, float,
            "Multiplier to use instead of usual multiplier if character is *not* hit in a weak spot. (Always set to -1 "
            "in vanilla game, which deactivates it. Only an educated guess that it affects incoming damage.)"),
        'maxHpChangeRate': (
            'MaxHPChangeRatio', False, float,
            "Appears to be an unused variant of MaxHPMultiplier. Always set to 0."),
        'behaviorId': (
            'BehaviorToTrigger', True, Params.Behaviors,
            "Behavior ID to trigger (which can in turn trigger an Attack or Bullet) whenever special effect is "
            "applied. Set to -1 to use no behavior."),
        'changeHpRate': (
            'HPReductionPercentage', True, int,
            "Percentage reduction of maximum HP (from 0 to 100). Negative values (to -100) will restore that "
            "percentage instead. Applied every time the special effect updates."),
        'changeHpPoint': (
            'HPPointsLost', True, int,
            "HP value to subtract (if positive) or add (if negative) to character's current HP on every update of the "
            "special effect."),
        'changeMpRate': (
            'MPReductionPercentage', False, int,
            "Percentage reduction of maximum MP (from 0 to 100). Negative values (to -100) will restore that "
            "percentage instead. Applied every time the special effect updates. (Unused in Dark Souls 1.)"),
        'changeMpPoint': (
            'MPPointsLost', False, int,
            "MP value to subtract (if positive) or add (if negative) to character's current MP on every update of the "
            "special effect. (Unused in Dark Souls 1.)"),
        'mpRecoverChangeSpeed': (
            'MPRecoverySpeedChange', False, int,
            "Points added to or subtracted from MP recovery formula. (Unused in Dark Souls 1.)"),
        'changeStaminaRate': (
            'StaminaReductionPercentage', True, int,
            "Percentage reduction of maximum stamina (from 0 to 100). Negative values (to -100) will restore that "
            "percentage instead. Applied every time the special effect updates."),
        'changeStaminaPoint': (
            'StaminaPointsLost', True, int,
            "Stamina value to subtract (if positive) or add (if negative) to character's current stamina on every "
            "update of the special effect."),
        'staminaRecoverChangeSpeed': (
            'StaminaRecoverySpeedChange', True, int,
            "Points added to or subtracted from stamina recovery formula. I believe this affects the amount of stamina "
            "restored every second. (For reference, a Green Blossom adds 40 points.)"),
        'magicEffectTimeChange': (
            'MagicEffectTimeChange', False, float,
            "Name suggests this changes the duration of magic effects, but it is never used (always zero)."),
        'insideDurability': (
            'CurrentDurabilityAddition', True, int,
            "Amount of durability to subtract (if positive) or add (if negative) to current durability on every update "
            "of the special effect. The equipment affected is determined by... "),  # TODO
        'maxDurability': (
            'MaxDurabilityAddition', True, int,
            "Amount of durability to subtract (if positive) or add (if negative) to the character's maximum "
            "durability while the special effect is active. The equipment affected is determined by... "),  # TODO
        'staminaAttackRate': (
            'OutgoingStaminaDamageMultiplier', True, float,
            "Multiplier applied to the amount of damage dealt to targets' stamina."),
        'poizonAttackPower': (
            'PoisonDamage', True, int,
            "Amount of poison damage (in units of resistance) added to the character on every update. Negative values "
            "will heal poison damage instead (e.g. Purple Moss Clump). Unclear how this distinguishes between "
            "reducing build-up and actually healing the status."),
        'registIllness': (
            'ToxicDamage', True, int,
            "Amount of toxic damage (in units of resistance) added to the character on every update. Negative values "
            "will heal toxic damage instead (e.g. Blooming Purple Moss Clump). Unclear how this distinguishes between "
            "reducing build-up and actually healing the status."),
        'registBlood': (
            'BleedDamage', True, int,
            "Amount of bleed damage (in units of resistance) added to the character on every update. Negative values "
            "will heal bleed damage instead (e.g. Blood-Red Moss Clump). Unclear how this distinguishes between "
            "reducing build-up and actually healing the status."),
        'registCurse': (
            'CurseDamage', True, int,
            "Amount of curse damage (in units of resistance) added to the character on every update. Negative values "
            "will heal curse damage instead (e.g. Purging Stone). Unclear how this distinguishes between "
            "reducing build-up and actually healing the status."),
        'fallDamageRate': (
            'FallDamageMultiplier', True, float,
            "Multiplier applied to amount of fall damage taken by character. Cannot prevent lethal falls."),
        'soulRate': (
            'SoulsFromKillsMultiplier', True, float,
            "Multiplier applied to the amount of souls received when enemies or bosses are killed."),
        'equipWeightChangeRate': (
            'MaxEquipLoadMultiplier', True, float,
            "Multiplier applied to the character's maximum equip load."),
        'allItemWeightChangeRate': (
            'MaxItemLoadMultiplier', False, float,
            "Multiplier applied to how much the character can carry, equipped or not. Seems to have no effect in Dark "
            "Souls 1."),
        'soul': (
            'SoulAmountChange', True, int,
            "Amount of souls received (if positive) or taken away (if negative) every time the special effect is "
            "updated."),
        'animIdOffset': (
            'AnimationIDOffset', True, int,
            "Override default animation ID offset of character, which can change their animation set temporarily."),
        'haveSoulRate': (
            'SoulRewardMultiplier', True, float,
            "Multiplier applied to the amount of souls given to the player when they kill this character (e.g. enemies "
            "in NG+)."),
        'targetPriority': (
            'TargetPriorityChange', True, float,
            "Value added to or subtract from this character's priority in the target queue. Higher priority means "
            "they are more likely to be targeted by enemies."),
        'sightSearchEnemyCut': (
            'EnemySightPercentageReduction', True, int,
            "Percentage reduction in enemy sight (from 0 to 100) when looking for this character. Not sure if negative "
            "values can be used to make this character *more* visible."),
        'hearingSearchEnemyCut': (
            'EnemyHearingPercentageReduction', True, int,
            "Percentage reduction in enemy hearing (from 0 to 100) when looking for this character. Not sure if "
            "negative values can be used to make this character *more* audible."),
        'grabityRate': (
            'AnimationSpeedMultiplier', True, float,
            "Multiplier applied to all of this character's animations. Values other than 1 can lead to cool but "
            "potentially glitchy behavior (e.g. desynchronized grab animations and missed Collisiones)."),
        'registPoizonChangeRate': (
            'PoisonResistanceMultiplier', True, float,
            "Multiplier applied to character's maximum poison resistance."),
        'registIllnessChangeRate': (
            'ToxicResistanceMultiplier', True, float,
            "Multiplier applied to character's maximum toxic resistance."),
        'registBloodChangeRate': (
            'BleedResistanceMultiplier', True, float,
            "Multiplier applied to character's maximum bleed resistance."),
        'registCurseChangeRate': (
            'CurseResistanceMultiplier', True, float,
            "Multiplier applied to character's maximum curse resistance."),
        'soulStealRate': (
            'SoulStealMultiplier', False, float,
            "Internal description says 'defense against HP when NPCs are robbed by soul steal'. Probably unused."),
        'lifeReductionRate': (
            'EffectDurationMultiplier', False, int,
            "Multiplier applied to the duration of the effect specified in EffectDurationMultiplierType. Used only by "
            "Hawkeye Gough to reduce poison and toxic duration in vanilla game."),
        'hpRecoverRate': (
            'HPRecoveryRate', True, float,
            "Multiplier applied to any increase in character's current HP."),
        'replaceSpEffectId': (
            'NextSpecialEffect', True, Params.SpecialEffects,
            "Special effect to apply to character automatically when this special effect ends (if not terminated "
            "manually by an event)."),
        'cycleOccurrenceSpEffectId': (
            'SpecialEffectPerUpdate', True, Params.SpecialEffects,
            "Special effect to apply to character every time this special effect updates (e.g. Symbol of Avarice HP "
            "reduction)."),
        'atkOccurrenceSpEffectId': (
            'SpecialEffectOnAttack', True, Params.SpecialEffects,
            "Special effect to apply to any target hit by an attack.\n\nWARNING: This will not trigger unless "
            "SpecialStateIndex is set to 152 (PoisonedWeapon), and must therefore always be accompanied by the poison "
            "weapon visual effect."),
        'guardDefFlickPowerRate': (
            'GuardDefenseFlickPowerRate', False, float,
            "Unknown; never used."),
        'guardStaminaCutRate': (
            'GuardStaminaMultiplier', True, float,
            "Multiplier applied to amount of stamina lost when an attack is blocked."),
        'rayCastPassedTime': (
            'RayCastPassingTime', False, int,
            "Internal description says 'Gaze passing: activation time (milliseconds).' Likely unused."),
        'changeSuperArmorPoint': (
            'PoiseAddition', True, int,
            "Amount added (if positive) or subtracted (if negative) from character's poise."),
        'bowDistRate': (
            'BowRangePercentageChange', True, int,
            "Percentage change (from 0 to 100) in bow range. Requires SpecialStateIndex BowBoostRange (168) to work."),
        'spCategory': (
            'SpecialEffectCategory', True, SP_EFFECT_SPCATEGORY,
            "Category of special effect. This effect will override (i.e. cancel out) all other active effects with "
            "the same category when it is added."),
        'categoryPriority': (
            'SpecialEffectPriority', True, int,
            "Priority ordering for special effect to be applied on each update (lower values are updated first)."),
        'saveCategory': (
            'SaveCategory', True, SP_EFFECT_SAVE_CATEGORY,
            "Determines automatic game saving behavior (used for status ailments only). Set to -1 for no saving."),
        'changeMagicSlot': (
            'AttunementSlotCountChange', False, int,
            "Supposed to modify attunement slots, but does nothing. You can use special state 'Extra Attunement' to "
            "get 50% extra attunment slots, if needed."),
        'changeMiracleSlot': (
            'AttunementMiracleSlotCountChange', False, int,
            "Miracle slots are not even separate from other magic slots, so this is likely an abandoned field."),
        'heroPointDamage': (
            'HumanityDamage', True, int,
            "Damage applied to soft humanity count. Negative values will add soft humanity."),
        'defFlickPower': (
            'RiposteDefenseAddition', True, int,
            "Value added to or subtracted from defense against riposte attacks."),
        'flickDamageCutRate': (
            'FlickDamageMultiplier', True, float,
            "Multiplier to use instead of usual multiplier on incoming (I assume) riposte attacks). Never used."),
        'bloodDamageRate': (
            'IncomingBleedDamagePercentage', True, int,
            "Percentage of incoming bleed damage received (usually 100)."),
        'dmgLv_None': (
            'ReplaceNoImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of NoImpact level."),
        'dmgLv_S': (
            'ReplaceSmallImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Small impact level."),
        'dmgLv_M': (
            'ReplaceMediumImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Medium impact level."),
        'dmgLv_L': (
            'ReplaceLargeImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Large impact level."),
        'dmgLv_BlowM': (
            'ReplaceBlowoffImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Blowoff impact level."),
        'dmgLv_Push': (
            'ReplacePushImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Push impact level."),
        'dmgLv_Strike': (
            'ReplaceStrikeImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Strike impact level."),
        'dmgLv_BlowS': (
            'ReplaceSmallBlowImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Blow impact level."),
        'dmgLv_Min': (
            'ReplaceMinimalImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Minimal impact level."),
        'dmgLv_Uppercut': (
            'ReplaceLaunchImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of Launch impact level."),
        'dmgLv_BlowLL': (
            'ReplaceBlowBackwardImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of BlowBackward impact level."),
        'dmgLv_Breath': (
            'ReplaceBreathBurnImpactLevel', True, ATKPARAM_REP_DMGTYPE,
            "Impact level that will occur instead of BreathBurn impact level."),
        'atkAttribute': (
            'AttackAttribute', True, ATKPARAM_ATKATTR_TYPE,
            "Attack type attached to hits while special effect is active."),
        'spAttribute': (
            'ElementAttribute', True, ATKPARAM_SPATTR_TYPE,
            "Element attached to hits while special effect is active."),
        'stateInfo': (
            'SpecialState', True, SpecialStateInfo,  # TODO: right click can edit numeric entry directly.
            "Hard-coded special state to use. Also determines visual effect from Special Effect Visuals table."),
        'wepParamChange': (
            'AffectedWeaponType', True, SP_EFE_WEP_CHANGE_PARAM,
            "Weapon category that is affected by special effect. "),
        'moveType': (
            'MovementType', True, SP_EFFECT_MOVE_TYPE,
            "Determines how movement is affected. (Does not correspond to Movement param entries.)"),
        'lifeReductionType': (
            'EffectDurationMultiplierType', False, int,
            "Type of effect whose duration is affected by EffectDurationMultiplier. Known values: 2 = poison, "
            "5 = toxic."),
        'throwCondition': (
            'ThrowCondition', False, SP_EFFECT_THROW_CONDITION_TYPE,
            "Determines how throws are affected while special effect is active. Values still unknown (rarely used)."),
        'addBehaviorJudgeId_condition': (
            'AddBehaviorJudgeIDCondition', False, int,
            "Unclear; used only to manage the Hydra as more heads are cut off. All other values are -1."),
        'addBehaviorJudgeId_add': (
            'AddBehaviorJudgeIDAdd', False, int,
            "Always zero. Unknown effect. Internal description suggests that this is a constant added to all behavior "
            "judge IDs (from TAE) issued by character."),
        'effectTargetSelf:1': (
            'CanAffectSelf', True, bool,
            "Effect will target self."),
        'effectTargetFriend:1': (
            'CanAffectAlly', True, bool,
            "Effect will target self."),
        'effectTargetEnemy:1': (
            'CanAffectEnemy', True, bool,
            "Effect will target enemies."),
        'effectTargetPlayer:1': (
            'CanAffectPlayer', True, bool,
            "Effect will target player characters."),
        'effectTargetAI:1': (
            'CanAffectAI', True, bool,
            "Effect will target non-player characters."),
        'effectTargetLive:1': (
            'CanAffectPlayers', True, bool,
            "Effect will target humans."),
        'effectTargetGhost:1': (
            'CanAffectPhantoms', True, bool,
            "Effect will target phantoms (white or black)."),
        'effectTargetWhiteGhost:1': (
            'CanAffectWhitePhantoms', True, bool,
            "Effect will target white phantoms."),
        'effectTargetBlackGhost:1': (
            'CanAffectWhitePhantoms', True, bool,
            "Effect will target white phantoms."),
        'effectTargetAttacker:1': (
            'CanAffectAttacker', True, bool,
            "Effect will target character when they attack (e.g. HP drain)."),
        'dispIconNonactive:1': (
            'DisplayIconWhenInactive', False, bool,
            "Display icon even when special effect is inactive (not sure what that means). Never enabled."),
        'useSpEffectEffect:1': (
            'UseVisualEffect', True, bool,
            "Use visual effect from Special Effect Visuals table (indexed by Special State field)."),
        'bAdjustMagicAblity:1': (
            'UseIntelligenceScaling', True, bool,
            "If True, special effect damage will be scaled by character intelligence (I believe)."),
        'bAdjustFaithAblity:1': (
            'UseFaithScaling', True, bool,
            "If True, special effect damage will be scaled by character faith (I believe)."),
        'bGameClearBonus:1': (
            'ForNewGamePlus', True, bool,
            "If True, this effect will be applied multiple times depending on the NG+ cycle (I think)."),
        'magParamChange:1': (
            'AffectsMagic', True, bool,
            "If True, multipliers will be applied to magic attacks."),
        'miracleParamChange:1': (
            'AffectsMiracles', True, bool,
            "If True, multipliers will be applied to miracle attacks."),
        'clearSoul:1': (
            'ClearSoul', False, bool,
            "Unused Demon's Souls remnant."),
        'requestSOS:1': (
            'RequestWhitePhantomSummon', False, bool,
            "Used only by White Sign Soapstone."),
        'requestBlackSOS:1': (
            'RequestBlackPhantomSummon', False, bool,
            "Used only by Red Sign Soapstone."),
        'requestForceJoinBlackSOS:1': (
            'RequestInvasion', False, bool,
            "Used only be (Cracked) Red Eye Orb."),
        'requestKickSession:1': (
            'RequestKick', False, bool,
            "Not used by any item. Likely kicks all clients out of your world."),
        'requestLeaveSession:1': (
            'RequestReturnToOwnWorld', False, bool,
            "Used only by Black Separation Crystal."),
        'requestNpcInveda:1': (
            'RequestNPCInvasion', False, bool,
            "Used only by Black Eye Orb (Lautrec quest and cut Shiva quest)."),
        'noDead:1': (
            'Immortal', True, bool,
            "If True, character cannot die. Never used in vanilla game."),
        'bCurrHPIndependeMaxHP:1': (
            'CurrentHPIgnoresMaxHPChange', True, bool,
            "If True, changes to maximum HP will not affect current HP (unless it must be reduced to new maximum)."),
        'corrosionIgnore:1': (
            'IgnoreCorrosion', False, bool,
            "If True, character will ignore corrosion damage to durability. Used only by Demon's Souls junk."),
        'sightSearchCutIgnore:1': (
            'IgnoreSightReduction', False, bool,
            "If True, character will ignore any changes to their sight range from other special effects. Used only by "
            "Demon's Souls junk."),
        'hearingSearchCutIgnore:1': (
            'IgnoreHearingReduction', False, bool,
            "If True, character will ignore any changes to their hearing range from other special effects. Used only "
            "by Demon's Souls junk."),
        'antiMagicIgnore:1': (
            'IgnoreMagicDisabling', False, bool,
            "If True, character will ignore any special effect that attempts to disable their magic. Used only by "
            "Demon's Souls junk."),
        'fakeTargetIgnore:1': (
            'IgnoreFakeTargets', False, bool,
            "Unknown; never used."),
        'fakeTargetIgnoreUndead:1': (
            'IgnoreUndeadFakeTargets', False, bool,
            "Unknown; never used."),
        'fakeTargetIgnoreAnimal:1': (
            'IgnoreBeastFakeTargets', False, bool,
            "Unknown; never used."),
        'grabityIgnore:1': (
            'IgnoreGravity', True, bool,
            "Ignore gravity. (Not sure if this actually works.)"),
        'disablePoison:1': (
            'PoisonImmunity', True, bool,
            "Immune to poison."),
        'disableDisease:1': (
            'ToxicImmunity', True, bool,
            "Immune to toxic."),
        'disableBlood:1': (
            'CurseImmunity', True, bool,
            "Immune to curse."),
        'disableCurse:1': (
            'PoisonImmunity', True, bool,
            "Immune to poison."),
        'enableCharm:1': (
            'EnableCharming', False, bool,
            "Not sure if this refers to the Alluring Skull. May not work at all."),
        'enableLifeTime:1': (
            'EnableLifeTime', False, bool,
            "Internal description: 'Is the life extended when setting a flag by TAE?'. Effect unknown. Used by Dragon "
            "Head and Torso Stones and some internal summon-related effects."),
        'hasTarget : 1': (
            'HasTarget', False, bool,
            "For unused 'evil eye' mechanics, probably a Demon's Souls remnant."),
        'isFireDamageCancel:1': (
            'FireImmunity', True, bool,
            "Immune to fire damage. Never enabled, and may not actually work. Needs testing."),
        'isExtendSpEffectLife:1': (
            'AffectedByLingeringDragoncrestRing', True, bool,
            "If True, this special effect will be affected by the Lingering Dragoncrest Ring special state (193) that "
            "extends effect durations."),
        'requestLeaveColiseumSession:1': (
            'RequestColiseumExit', False, bool,
            "Used only by Purple Coward's Crystal."),
        'pad_2:4': (
            'Pad1', False, '<Pad:4>',
            "Null padding."),
        'vowType0:1': (
            'AffectsCharactersWithNoCovenant', True, bool,
            "Determines if this special effect will affect characters with no covenant."),
        'vowType1:1': (
            'AffectsWayOfWhite', True, bool,
            "Determines if this special effect will affect characters in the Way of White covenant."),
        'vowType2:1': (
            'AffectsPrincessGuard', True, bool,
            "Determines if this special effect will affect characters in the Princess's Guard covenant."),
        'vowType3:1': (
            'AffectsWarriorOfSunlight', True, bool,
            "Determines if this special effect will affect characters in the Warriors of Sunlight covenant."),
        'vowType4:1': (
            'AffectsDarkwraith', True, bool,
            "Determines if this special effect will affect characters in the Darkwraith covenant."),
        'vowType5:1': (
            'AffectsPathOfTheDragon', True, bool,
            "Determines if this special effect will affect characters in the Path of the Dragon covenant."),
        'vowType6:1': (
            'AffectsGravelordServant', True, bool,
            "Determines if this special effect will affect characters in the Gravelord Servant covenant."),
        'vowType7:1': (
            'AffectsForestHunter', True, bool,
            "Determines if this special effect will affect characters in the Forest Hunters covenant."),
        'vowType8:1': (
            'AffectsDarkmoonBlade', True, bool,
            "Determines if this special effect will affect characters in the Blades of the Darkmoon covenant."),
        'vowType9:1': (
            'AffectsChaosServant', True, bool,
            "Determines if this special effect will affect characters in the Chaos Servants covenant."),
        'vowType10:1': (
            'AffectsCovenant10', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'vowType11:1': (
            'AffectsCovenant11', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'vowType12:1': (
            'AffectsCovenant12', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'vowType13:1': (
            'AffectsCovenant13', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'vowType14:1': (
            'AffectsCovenant14', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'vowType15:1': (
            'AffectsCovenant15', False, bool,
            "Determines if this special effect will affect characters in unused covenant."),
        'pad1[11]': (
            'Pad2', False, '<Pad:11>',
            "Null padding."),
    },
    'MAGIC_PARAM_ST': {
        'yesNoDialogMessageId': (
            'ConfirmationMessage', True, Text.EventText,
            "Message displayed in yes/no dialog box to confirm use of spell. Requires the Yes/No menu type."),
        'limitCancelSpEffectId': (
            'LimitCancelSpecialEffect', False, Params.SpecialEffects,
            "Unknown. Never used."),
        'sortId': (
            'SortIndex', True, int,
            "Index for automatic inventory sorting."),
        'refId': _spells_ref_id,
        'mp': (
            'MPCost', False, int,
            "MP cost of spell. Unused in Dark Souls 1 (always zero)."),
        'stamina': (
            'StaminaCost', False, int,
            "Stamina cost of spell. Always zero."),
        'iconId': (
            'SpellIcon', True, Texture,
            "Spell icon texture for inventory and equipped slot."),
        'behaviorId': (
            'Behavior', False, Params.Behaviors,
            "Behavior triggered by spell. Never used."),
        'mtrlItemId': (
            'RequiredGood', False, Params.Goods,
            "Good required for use. Never used (usability is handled in Shops parameters)."),
        'replaceMagicId': (
            'ReplaceSpell', False, Params.Spells,
            "Spell to replace 'when the state change matches'. Never used."),
        'maxQuantity': (
            'BaseCastCount', True, int,
            "Number of spell casts. Note that some spells consume multiple casts per use (e.g. Firestorm)."),
        'heroPoint': (
            'HumanityCost', False, int,
            "Soft humanity consumed when casting spell. Never used."),
        'overDexterity': (
            'OverDexterity', False, int,
            "Unknown effect. Always 99."),
        'sfxVariationId': (
            'VisualEffectVariation', True, int,
            "Visual effect variation. (I believe this alters the animation ID used for casting.)"),
        'slotLength': (
            'AttunementSlotsUsed', True, int,
            "Number of attunement slots required to attune spell."),
        'requirementIntellect': (
            'RequiredIntelligence', True, int,
            "Minimum intelligence required to cast spell."),
        'requirementFaith': (
            'RequiredFaith', True, int,
            "Minimum faith required to cast spell."),
        'analogDexiterityMin': (
            'MinDexterityForBonus', False, int,
            "Dexterity value where casting speed starts to be affected (I think). This is always 20, but apparently "
            "speed isn't actually affected until dexterity is 35."),
        'analogDexiterityMax': (
            'MaxDexterityForBonus', False, int,
            "Dexterity value where casting speed stops being further affected (I think). Always 45, which is "
            "consistent with the observed dexterity cap."),
        'ezStateBehaviorType': (
            'SpellCategory', True, MAGIC_CATEGORY,
            "Type of spell."),
        'refCategory': (
            'ReferenceType', True, BEHAVIOR_REF_TYPE,
            "Determines if this spell triggers a Bullet or Special Effect. ('Default' is never used, but probably "
            "triggers an Attack, which is unlikely to be useful to you.)"),
        'spEffectCategory': (
            'SpecialEffectCategory', True, SP_EFFECT_SPCATEGORY,
            "Determines what type of special effects affect the stats of this spell. (Vanilla game uses 3 for "
            "sorceries and pyromancies, and 4 for miracles.)"),
        'refType': (
            'AnimationType', True, MAGIC_MOTION_TYPE,
            "Basic animation type when casting spell. The Visual Effect Variation field further refines it."),
        'opmeMenuType': (
            'MenuActivated', True, GOODS_OPEN_MENU,
            "Menu activated (if any) when spell is cast. Only used by Homeward (Yes/No Dialog)."),
        'hasSpEffectType': (
            'HasSpecialEffectType', False, int,
            "Determines 'the state change that needs to replace the spell ID'. Never used."),
        'replaceCategory': (
            'ReplaceCategory', True, REPLACE_CATEGORY,
            "Determines which existing effects this spell will replace. Only used for a few spells."),
        'useLimitCategory': (
            'LimitCategory', True, SP_EFFECT_USELIMIT_CATEGORY,
            "Only one special effect with this category can be active at once. Additional attempts to cast spells (or "
            "use goods) in this category will be prevented."),
        'vowType0:1': (
            'UseableByNoCovenant', True, bool,
            "Determines if this spell can be cast by characters with no covenant."),
        'vowType1:1': (
            'UseableByWayOfWhite', True, bool,
            "Determines if this spell can be cast by characters in the Way of White."),
        'vowType2:1': (
            'UseableByPrincessGuard', True, bool,
            "Determines if this spell can be cast by characters in the Princess's Guard."),
        'vowType3:1': (
            'UseableByWarriorsOfSunlight', True, bool,
            "Determines if this spell can be cast by characters in the Warriors of Sunlight."),
        'vowType4:1': (
            'UseableByDarkwraith', True, bool,
            "Determines if this spell can be cast by characters in the Darkwraith covenant."),
        'vowType5:1': (
            'UseableByPathOfTheDragon', True, bool,
            "Determines if this spell can be cast by characters in the Path of the Dragon."),
        'vowType6:1': (
            'UseableByGravelordServant', True, bool,
            "Determines if this spell can be cast by characters in the Gravelord Servants."),
        'vowType7:1': (
            'UseableByForestHunter', True, bool,
            "Determines if this spell can be cast by characters in the Forest Hunters."),
        'vowType8:1': (
            'UseableByDarkmoonBlade', True, bool,
            "Determines if this spell can be cast by characters in the Blades of the Darkmoon."),
        'vowType9:1': (
            'UseableByChaosServant', True, bool,
            "Determines if this spell can be cast by characters in the Chaos Servant covenant."),
        'vowType10:1': (
            'UseableByCovenant10', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 10."),
        'vowType11:1': (
            'UseableByCovenant11', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 11."),
        'vowType12:1': (
            'UseableByCovenant12', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 12."),
        'vowType13:1': (
            'UseableByCovenant13', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 13."),
        'vowType14:1': (
            'UseableByCovenant14', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 14."),
        'vowType15:1': (
            'UseableByCovenant15', False, bool,
            "Determines if this spell can be cast by characters in unused covenant 15."),
        'enable_multi:1': (
            'UseableInMultiplayer', True, bool,
            "Determines if this spell can be cast while multiple players are together. Only disabled for Homeward in "
            "vanilla game."),
        'enable_multi_only:1': (
            'DisabledOutsideMultiplayer', False, bool,
            "Determines if this spell can ONLY be cast while multiple players are together. Always False."),
        'isEnchant:1': (
            'IsWeaponBuff', True, bool,
            "Indicates if this spell buffs your weapon."),
        'isShieldEnchant:1': (
            'IsShieldBuff', True, bool,
            "Indicates if this spell buffs your shield."),
        'enable_live:1': (
            'UseableByHumans', True, bool,
            "Determines if this spell can be cast by players who have revived to human."),
        'enable_gray:1': (
            'UseableByHollows', True, bool,
            "Determines if this spell can be cast by players who have NOT revived to human."),
        'enable_white:1': (
            'UseableByWhitePhantoms', True, bool,
            "Determines if this spell can be cast by White Phantoms (summons). Only disabled for Homeward and the "
            "unused Escape Death miracle in vanilla game."),
        'enable_black:1': (
            'UseableByBlackPhantoms', True, bool,
            "Determines if this spell can be cast by Black Phantoms (invaders). Only disabled for Homeward and the "
            "unused Escape Death miracle in vanilla game."),
        'disableOffline:1': (
            'DisabledOffline', False, bool,
            "If True, this spell cannot be cast without a network connection. Always False."),
        'castResonanceMagic:1': (
            'CreateResonanceRing', True, bool,
            "If True, using this spell will create a resonance ring to help players in other worlds."),
        'pad_1:6': (
            'Pad1', False, '<Pad:6>',
            "Null padding."),
        'pad[2]': (
            'Pad2', False, '<Pad:2>',
            "Null padding."),
    },
    'THROW_INFO_BANK': {
        'AtkChrId': (
            'AttackingCharacterModel', True, Model,
            "Model ID of attacking character."),
        'DefChrId': (
            'DefendingCharacterModel', True, Model,
            "Model ID of defending character."),
        'Dist': (
            'MaxDistance', True, float,
            "Maximum distance at which throw can be triggered."),
        'DiffAngMin': (
            'MinDifferenceInFacingAngle', True, float,
            "Minimum angular difference between attacker's facing direction and defender's facing direction."),
        'DiffAngMax': (
            'MaxDifferenceInFacingAngle', True, float,
            "Maximum angular difference between attacker's facing direction and defender's facing direction."),
        'upperYRange': (
            'MaxDistanceAbove', True, float,
            "Maximum distance that defender can be above attacker."),
        'lowerYRange': (
            'MaxDistanceBelow', True, float,
            "Maximum distance that defender can be below attacker."),
        'diffAngMyToDef': (
            'MaxAngleToDefender', True, float,
            "Maximum angular difference between attacker's direction and the direction of the defender."),
        'throwTypeId': (
            'ThrowID', True, int,
            "Throw ID that should be specified in Attacks to use this throw."),
        'atkAnimId': (
            'AttackerAnimation', True, Animation,
            "Animation played by attacker during throw."),
        'defAnimId': (
            'DefenderAnimation', True, Animation,
            "Animation played by defender during throw."),
        'escHp': (
            'MinHPPercentageForEscape', True, int,
            "Minimum HP percentage required to escape the throw early by mashing buttons. (Not sure if 0 prevents any "
            "escape, or if escapes are disabled by another parameter like "),
        'selfEscCycleTime': (
            'EscapeCycleTime', True, int,
            "Time of escape cycle, in milliseconds. Not sure exactly what it does. Set to 100 milliseconds for throws "
            "that can be escaped, and zero otherwise."),
        'sphereCastRadiusRateTop': (
            'SphereCastUpperRadiusRatio', True, int,
            "Determines size of upper hemisphere of spherecast. I believe this is a percentage relative to the model "
            "size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's model size."),
        'sphereCastRadiusRateLow': (
            'SphereCastLowerRadiusRatio', True, int,
            "Determines size of lower hemisphere of spherecast. I believe this is a percentage relative to the model "
            "size, so a value of 80 will send out a sphere with a radius that is 0.8 times the attacker's model size."),
        'PadType': (
            'ButtonMashType', True, THROW_PAD_TYPE,
            "Determines buttons that can be mashed to escape. Enumeration is unknown, but it is set to 3 for the "
            "Centipede Demon grab, Male Ghost grab, and Dark Hand grab, and 1 for every other throw."),
        'AtkEnableState': (
            'AttackEnabled', False, THROW_ENABLE_STATE,
            "Internal description says 'Set the throwable throwable state type' (?). Set to 1 for all player backstabs "
            "and ripostes, and 0 otherwise (including player plunging attacks and all enemy throws)."),
        'atkSorbDmyId': (
            'SnapToAttackerModelPoint', True, int,
            "Model point ID on attacker that defender will be snapped to. If this is zero, 'Snap To Defender Model "
            "Point' should be non-zero, and vice versa."),
        'defSorbDmyId': (
            'SnapToDefenderModelPoint', True, int,
            "Model point ID on defender that attacker will be snapped to. If this is zero, 'Snap To Attacker Model "
            "Point' should be non-zero, and vice versa."),
        'throwType': (
            'ThrowType', True, THROW_TYPE,
            "Type of throw. Not sure what uses this, but it could affect various things."),
        'selfEscCycleCnt': (
            'EscapeCycleCount', True, int,
            "Internal description says 'number of self-throwing cycles'. Always set to 1 when EscapeCycleTime is set "
            "to 100 (and MinHPPercentageForEscape is almost always 25). Not sure how it determines *when* you can "
            "escape the throw."),
        'dmyHasChrDirType': (
            'ModelPointCharacterDirectionType', False, THROW_DMY_CHR_DIR_TYPE,
            "'Direction of model point possessed character when thrown'. Set to 1 for the Armored Tusk backstab, 255 "
            "for the Iron Golem and Gaping Dragon grabs, and 0 otherwise."),
        'isTurnAtker:1': (
            'AttackerTurns', True, bool,
            "Attacker will turn when throw begins (presumably before model point snapping occurs)."),
        'isSkipWepCate:1': (
            'SkipAttackerWeaponCategoryCheck', True, bool,
            "If True, the weapon category check for the attacker will be skipped. Enabled only for Dark Hand drain."),
        'isSkipSphereCast:1': (
            'SkipSphereCast', True, bool,
            "If True, the sphere cast check will be skipped. Usually False, but True for the coffin stab, Armored "
            "Tusk backstab, and a few large enemy grabs. (Presumably, if False, the throw trigger relies on distance "
            "and character angles only and is generally easier to trigger.)"),
        'pad0:5': (
            'Pad1', False, '<Pad:5>',
            "Null padding."),
        'pad1[4]': (
            'Pad2', False, '<Pad:4>',
            "Null padding."),
    },
    'EQUIP_MTRL_SET_PARAM_ST': {
        'materialId01': (
            'UpgradeGood', True, Params.Goods,
            "Good required to upgrade weapon."),
        'materialId02': (
            'UpgradeGood2', False, Params.Goods,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it may "
            "still work as a requirement)."),
        'materialId03': (
            'UpgradeGood3', False, Params.Goods,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it may "
            "still work as a requirement)."),
        'materialId04': (
            'UpgradeGood4', False, Params.Goods,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it may "
            "still work as a requirement)."),
        'materialId05': (
            'UpgradeGood5', False, Params.Goods,
            "Second good required to upgrade weapon. Never used, and the upgrade menu can't display it (though it may "
            "still work as a requirement)."),
        'itemNum01': (
            'UpgradeQuantity', True, int,
            "Amount of Upgrade Good required for reinforcement."),
        'itemNum02': (
            'UpgradeQuantity2', False, int,
            "Amount of Upgrade Good 2 required for upgrade. Never used, and the upgrade menu can't display it (though "
            "it may still work as a requirement)."),
        'itemNum03': (
            'UpgradeQuantity3', False, int,
            "Amount of Upgrade Good 3 required for upgrade. Never used, and the upgrade menu can't display it (though "
            "it may still work as a requirement)."),
        'itemNum04': (
            'UpgradeQuantity4', False, int,
            "Amount of Upgrade Good 4 required for upgrade. Never used, and the upgrade menu can't display it (though "
            "it may still work as a requirement)."),
        'itemNum05': (
            'UpgradeQuantity5', False, int,
            "Amount of Upgrade Good 5 required for upgrade. Never used, and the upgrade menu can't display it (though "
            "it may still work as a requirement)."),
        'isDisableDispNum01:1': (
            'DisableQuantityIndicator', True, bool,
            "If True, the upgrade quantity will not be shown. Often used when only one of the upgrade good is needed."),
        'isDisableDispNum02:1': (
            'DisableQuantity Indicator2', False, bool,
            "If True, the upgrade quantity for Upgrade Good 2 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used)."),
        'isDisableDispNum03:1': (
            'DisableQuantity Indicator3', False, bool,
            "If True, the upgrade quantity for Upgrade Good 3 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used)."),
        'isDisableDispNum04:1': (
            'DisableQuantity Indicator4', False, bool,
            "If True, the upgrade quantity for Upgrade Good 4 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used)."),
        'isDisableDispNum05:1': (
            'DisableQuantity Indicator5', False, bool,
            "If True, the upgrade quantity for Upgrade Good 5 will not be shown. Often used when only one of the "
            "upgrade good is needed (though again, this slot is never used)."),
        'pad[6]': (
            'Pad1', False, '<Pad:6>',
            "Null padding."),
    },
    'EQUIP_PARAM_WEAPON_ST': {
        'behaviorVariationId': (
            'BehaviorVariationID', True, int,
            "Number attached to the front of behaviors triggered from TAE."),
        'sortId': (
            'SortIndex', True, int,
            "Index for automatic inventory sorting."),
        'wanderingEquipId': (
            'GhostWeaponReplacement', True, Params.Weapons,
            "Weapon replacement for ghosts."),
        'weight': (
            'Weight', True, float,
            "Weight of weapon."),
        'weaponWeightRate': (
            'WeightRatio', True, float,
            "Unknown effect. Value is about evenly split between 0 and 1 across weapons, with no obvious pattern."),
        'fixPrice': (
            'RepairCost', True, int,
            "Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
            "durability over max durability."),
        'basicPrice': (
            'BasicCost', False, int,
            "Unknown purpose, and unused."),
        'sellValue': (
            'FramptSellValue', True, int,
            "Amount of souls received when fed to Frampt. (Set to -1 to prevent it from being sold."),
        'correctStrength': (
            'StrengthScaling', True, int,
            "Amount of attack power gained from strength. (I believe this is the percentage of the player's strength "
            "to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)"),
        'correctAgility': (
            'DexterityScaling', True, int,
            "Amount of attack power gained from dexterity. (I believe this is the percentage of the player's "
            "dexterity to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)."),
        'correctMagic': (
            'IntelligenceScaling', True, int,
            "Amount of attack power gained from intelligence. (I believe this is the percentage of the player's "
            "intelligence to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)"),
        'correctFaith': (
            'FaithScaling', True, int,
            "Amount of attack power gained from faith. (I believe this is the percentage of the player's faith "
            "to add to the weapon's attack power, but it also depends on ScalingFormulaType below.)"),
        'physGuardCutRate': (
            'PhysicalGuardPercentage', True, int,
            "Percentage of physical damage prevented when guarding with this weapon."),
        'magGuardCutRate': (
            'MagicGuardPercentage', True, int,
            "Percentage of magic damage prevented when guarding with this weapon."),
        'fireGuardCutRate': (
            'FireGuardPercentage', True, int,
            "Percentage of fire damage prevented when guarding with this weapon."),
        'thunGuardCutRate': (
            'LightningGuardPercentage', True, int,
            "Percentage of lightning damage prevented when guarding with this weapon."),
        'spEffectBehaviorId0': (
            'SpecialEffectOnHit0', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 0)."),
        'spEffectBehaviorId1': (
            'SpecialEffectOnHit1', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 1)."),
        'spEffectBehaviorId2': (
            'SpecialEffectOnHit2', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 2)."),
        'residentSpEffectId': (
            'EquippedSpecialEffect0', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 0)."),
        'residentSpEffectId1': (
            'EquippedSpecialEffect1', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 1)."),
        'residentSpEffectId2': (
            'EquippedSpecialEffect2', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 2)."),
        'materialSetId': (
            'WeaponUpgradeID', True, Params.WeaponUpgrades,
            "Weapon Upgrade parameter for weapon reinforcement."),
        'originEquipWep': (
            'UpgradeOrigin0', True, Params.Weapons,
            "Origin armor for level 0 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep1': (
            'UpgradeOrigin1', True, Params.Weapons,
            "Origin armor for level 1 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep2': (
            'UpgradeOrigin2', True, Params.Weapons,
            "Origin armor for level 2 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep3': (
            'UpgradeOrigin3', True, Params.Weapons,
            "Origin armor for level 3 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep4': (
            'UpgradeOrigin4', True, Params.Weapons,
            "Origin armor for level 4 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep5': (
            'UpgradeOrigin5', True, Params.Weapons,
            "Origin armor for level 5 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep6': (
            'UpgradeOrigin6', True, Params.Weapons,
            "Origin armor for level 6 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep7': (
            'UpgradeOrigin7', True, Params.Weapons,
            "Origin armor for level 7 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep8': (
            'UpgradeOrigin8', True, Params.Weapons,
            "Origin armor for level 8 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep9': (
            'UpgradeOrigin9', True, Params.Weapons,
            "Origin armor for level 9 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep10': (
            'UpgradeOrigin10', True, Params.Weapons,
            "Origin armor for level 10 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep11': (
            'UpgradeOrigin11', True, Params.Weapons,
            "Origin armor for level 11 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep12': (
            'UpgradeOrigin12', True, Params.Weapons,
            "Origin armor for level 12 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep13': (
            'UpgradeOrigin13', True, Params.Weapons,
            "Origin armor for level 13 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep14': (
            'UpgradeOrigin14', True, Params.Weapons,
            "Origin armor for level 14 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipWep15': (
            'UpgradeOrigin15', True, Params.Weapons,
            "Origin armor for level 15 of this weapon (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the weapon cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'antiDemonDamageRate': (
            'DamageAgainstDemonsMultiplier', True, float,
            "Multiplier applied to damage dealt against demons with this weapon."),
        'antSaintDamageRate': (
            'WeakToDivineDamageMultiplier', True, float,
            "Multiplier applied to damage dealt against enemies weak to divine (e.g. skeletons) with this weapon."),
        'antWeakA_DamageRate': (
            'GodDamageMultiplier', True, float,
            "Multiplier applied to damage dealt against Gods and Goddesses with this weapon."),
        'antWeakB_DamageRate': (
            'AbyssDamageMultiplier', True, float,
            "Multiplier applied to damage dealt against enemies from the Abyss with this weapon."),
        'vagrantItemLotId': (
            'VagrantItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantBonusEneDropItemLotId': (
            'VagrantBonusEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'vagrantItemEneDropItemLotId': (
            'VagrantItemEnemyDropItemLot', False, Params.ItemLots,
            "DOC-TODO"),
        'equipModelId': (
            'WeaponModel', True, Model,
            "Weapon model ID."),
        'iconId': (
            'WeaponIcon', True, Texture,
            "Weapon icon texture ID."),
        'durability': (
            'InitialDurability', True, int,
            "Durability of weapon when it is obtained. Always equal to max durability in vanilla game."),
        'durabilityMax': (
            'MaxDurability', True, int,
            "Maximum durability of weapon."),
        'attackThrowEscape': (
            'ThrowEscapePower', False, int,
            "Power for escaping throws. Always 1, except for a few (and only a few) of the ghost replacement weapons."),
        'parryDamageLife': (
            'MaxParryWindowDuration', False, int,
            "Maximum parry window duration (cannot exceed TAE duration). Always set to 10."),
        'attackBasePhysics': (
            'BasePhysicalDamage', True, int,
            "Base physical damage of weapon attacks."),
        'attackBaseMagic': (
            'BaseMagicDamage', True, int,
            "Base magic damage of weapon attacks."),
        'attackBaseFire': (
            'BaseFireDamage', True, int,
            "Base fire damage of weapon attacks."),
        'attackBaseThunder': (
            'BaseLightningDamage', True, int,
            "Base lightning damage of weapon attacks."),
        'attackBaseStamina': (
            'BaseStaminaDamage', True, int,
            "Base stamina damage of weapon attacks."),
        'saWeaponDamage': (
            'BasePoiseDamage', True, int,
            "Base poise damage of weapon attacks."),
        'saDurability': (
            'AttackPoiseBonus', False, int,
            "Poise gained during attack animations with this weapon. Never used (probably done in TAE)."),
        'guardAngle': (
            'EffectiveGuardAngle', False, int,
            "Angle that can be guarded with this weapon. Never used."),
        'staminaGuardDef': (
            'GuardStaminaDefense', True, int,
            "Defense against (i.e. value subtracted from) stamina attack damage while guarding."),
        'reinforceTypeId': (
            'UpgradeMaterials', True, Params.UpgradeMaterials,
            "Upgrade materials required for reinforcement at each level."),
        'trophySGradeId': (
            'KnightHonorIndex', False, int,
            "Index of weapon as it contributes to the Knight's Honor achievement."),
        'trophySeqId': (
            'MaxUpgradeAchievementID', False, int,
            "Achievement unlocked when weapon is upgraded to maximum level (one per upgrade path)."),
        'throwAtkRate': (
            'ThrowDamageChangePercentage', True, int,
            "Percentage damage increase (if positive) or decrease (if negative) during backstabs and ripostes with "
            "this weapon."),
        'bowDistRate': (
            'BowRangeChangePercentage', True, int,
            "Percentage range increase (if positive) or decrease (if negative) with this bow."),
        'equipModelCategory': (
            'WeaponModelCategory', False, EQUIP_MODEL_CATEGORY,
            "Model category for equipment. Only one option for weapons."),
        'equipModelGender': (
            'WeaponModelGender', False, EQUIP_MODEL_GENDER,
            "Model gender variant. All weapons are genderless."),
        'weaponCategory': (
            'WeaponCategory', True, WEAPON_CATEGORY,
            "Basic category of weapon. Many 'weapon types' you may be familiar with are merged here (e.g. whips are "
            "straight swords)."),
        'wepmotionCategory': (
            'AttackAnimationCategory', True, WEPMOTION_CATEGORY,
            "Basic weapon attack animation type. More diverse than WeaponCategory. This number is multiplied by "
            "10000 and used as an animation offset for all attacks, I believe."),
        'guardmotionCategory': (
            'GuardAnimationCategory', True, GUARDMOTION_CATEGORY,
            "Basic weapon/shield block animation type."),
        'atkMaterial': (
            'VisualSoundEffectsOnHit', True, WEP_MATERIAL_ATK,
            "Determines the sounds and visual effects generated when this weapon hits."),
        'defMaterial': (
            'VisualEffectsOnBlock', True, WEP_MATERIAL_DEF,
            "Determines the visual effects generated when this weapon blocks an attack."),
        'defSfxMaterial': (
            'SoundEffectsOnBlock', True, WEP_MATERIAL_DEF_SFX,
            "Determines the sound effects generated when this weapon blocks an attack."),
        'correctType': (
            'ScalingFormulaType', True, WEP_CORRECT_TYPE,
            "Determines how scaling changes with attribute level."),
        'spAttribute': (
            'ElementAttribute', True, ATKPARAM_SPATTR_TYPE,
            "Element attached to hits with this weapon."),
        'spAtkcategory': (
            'SpecialAttackCategory', True, WEPMOTION_CATEGORY,
            "Category of special attack (R2) performed with this weapon, from 50 to 199 (or 0 for none). This number "
            "is multiplied by 10000 and used as an animation offset for R2 attacks, I believe."),
        'wepmotionOneHandId': (
            'OneHandedAnimationCategory', True, WEPMOTION_CATEGORY,
            "Category for one-handed attacks.This number is multiplied by 10000 and used as an animation offset for "
            "one-handed attacks, I believe. Not sure how it interacts with the base AttackAnimationCategory."),
        'wepmotionBothHandId': (
            'TwoHandedAnimationCategory', True, WEPMOTION_CATEGORY,
            "Category for two-handed attacks. This number is multiplied by 10000 and used as an animation offset for "
            "two-handed attacks, I believe. Not sure how it interacts with the base AttackAnimationCategory."),
        'properStrength': (
            'RequiredStrength', True, int,
            "Required strength to wield weapon properly. (Reduced by one third if held two-handed.)"),
        'properAgility': (
            'RequiredDexterity', True, int,
            "Required dexterity to wield weapon properly."),
        'properMagic': (
            'RequiredIntelligence', True, int,
            "Required intelligence to wield weapon properly."),
        'properFaith': (
            'RequiredFaith', True, int,
            "Required faith to wield weapon properly."),
        'overStrength': (
            'OverStrength', False, int,
            "Unknown. Always set to 99, except for arrows and bolts."),
        'attackBaseParry': (
            'AttackBaseParry', False, int,
            "Unknown. Never used."),
        'defenseBaseParry': (
            'DefenseBaseParry', False, int,
            "Unknown. Never used."),
        'guardBaseRepel': (
            'DeflectOnBlock', True, int,
            "Determines if an enemy will be deflected when you block them with this weapon (by comparing it to their "
            "DeflectOnAttack)."),
        'attackBaseRepel': (
            'DeflectOnAttack', True, int,
            "Determines if this weapon will be deflected when attacking a blocking enemy (by comparing it to their "
            "DeflectOnBlock)."),
        'guardCutCancelRate': (
            'IgnoreGuardPercentage', False, int,
            "Percentage (from -100 to 100) of target's current guard rate to ignore. A value of 100 will ignore "
            "guarding completely, and a value of -100 will double their guarding effectiveness. Never used, in favor "
            "of the simple 'IgnoreGuard' boolean field."),
        'guardLevel': (
            'GuardLevel', True, int,
            "Internal description: 'in which guard motion is the enemy attacked when guarded?' Exact effects are "
            "unclear, but this ranges from 0 to 4 in effectiveness of blocking in a predictable way (daggers are worse "
            "than swords, which are worse than greatswords, which are worse than all shields)."),
        'slashGuardCutRate': (
            'SlashDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'blowGuardCutRate': (
            'StrikeDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'thrustGuardCutRate': (
            'ThrustDamageReductionWhenGuarding', False, int,
            "Always zero."),
        'poisonGuardResist': (
            'PoisonDamageReductionWhenGuarding', True, int,
            "Percentage of incoming poison damage ignored when guarding."),
        'diseaseGuardResist': (
            'ToxicDamageReductionWhenGuarding', True, int,
            "Percentage of incoming toxic damage ignored when guarding."),
        'bloodGuardResist': (
            'BleedDamageReductionWhenGuarding', True, int,
            "Percentage of incoming bleed damage ignored when guarding."),
        'curseGuardResist': (
            'CurseDamageReductionWhenGuarding', True, int,
            "Percentage of incoming curse damage ignored when guarding."),
        'isDurabilityDivergence': (
            'DurabilityDivergenceCategory', True, DURABILITY_DIVERGENCE_CATEGORY,
            "Determines an alternate animation used if the player tries to use this weapon's special attack without "
            "having enough durability to use it. Exact enumeration is unknown, but existing usages are documented."),
        'rightHandEquipable:1': (
            'RightHandAllowed', True, bool,
            "If True, this weapon can be equipped in the right hand."),
        'leftHandEquipable:1': (
            'LeftHandAllowed', True, bool,
            "If True, this weapon can be equipped in the left hand."),
        'bothHandEquipable:1': (
            'BothHandsAllowed', True, bool,
            "If True, this weapon can be held in two-handed mode."),
        'arrowSlotEquipable:1': (
            'UsesEquippedArrows', True, bool,
            "If True, this weapon will use equipped arrow slot."),
        'boltSlotEquipable:1': (
            'UsesEquippedBolts', True, bool,
            "If True, this weapon will use equipped bolt slot."),
        'enableGuard:1': (
            'GuardEnabled', True, bool,
            "If True, the player can guard with this weapon by holding L1."),
        'enableParry:1': (
            'ParryEnabled', True, bool,
            "If True, the player can parry with htis weapon by pressing L2."),
        'enableMagic:1': (
            'CanCastMagic', True, bool,
            "If True, this weapon can be used to cast magic."),  # TODO: what magic?
        'enableSorcery:1': (
            'CanCastSorcery', True, bool,
            ""),
        'enableMiracle:1': (
            'CanCastMiracles', True, bool,
            ""),
        'enableVowMagic:1': (
            'CanCastCovenantMagic', True, bool,
            ""),
        'isNormalAttackType:1': (
            'DealsNeutralDamage', True, bool,
            ""),
        'isBlowAttackType:1': (
            'DealsStrikeDamage', True, bool,
            ""),
        'isSlashAttackType:1': (
            'DealsSlashDamage', True, bool,
            ""),
        'isThrustAttackType:1': (
            'DealsThrustDamage', True, bool,
            ""),
        'isEnhance:1': (
            'IsUpgraded', True, bool,
            ""),
        'isLuckCorrect:1': (
            'IsAffectedByLuck', True, bool,
            ""),
        'isCustom:1': (
            'IsCustom?', True, bool,
            ""),
        'disableBaseChangeReset:1': (
            'DisableBaseChangeReset', True, bool,
            ""),
        'disableRepair:1': (
            'DisableRepairs', True, bool,
            "If True, this weapon cannot be repaired."),
        'isDarkHand:1': (
            'IsDarkHand', False, bool,
            "Enabled only for the Dark Hand."),
        'simpleModelForDlc:1': (
            'SimpleDLCModelExists', False, bool,
            "Unknown; always set to False."),
        'lanternWep:1': (
            'IsLantern?', True, bool,
            ""),
        'isVersusGhostWep:1': (
            'CanHitGhosts', True, bool,
            "If True, this weapon can hit ghosts without a Transient Curse active."),
        'baseChangeCategory:6': (
            'BaseChangeCategory', False, int,
            "Never used. Likely Demon's Souls junk."),
        'isDragonSlayer:1': (
            'IsDragonSlayer', True, bool,
            ""),
        'isDeposit:1': (
            'CanBeStored', True, bool,
            "If True, this weapon can be stored in the Bottomless Box. Always True for rings."),
        'pad_1[8]': (
            'Pad1', False, '<Pad:8>',
            "Null padding."),
        'disableMultiDropShare:1': (
            'DisableMultiplayerShare', False, bool,
            "If True, this weapon cannot be given to other players by dropping it. Always False in vanilla."),
        'pad_0[1]': (
            'Pad2', False, '<Pad:1>',
            "Null padding."),
        'oldSortId': (
            'OldSortIndex', False, int,
            "Sorting index for an obsolete build of the game. No effect."),
        'levelSyncCorrectID': (
            'LevelSyncCorrection', False, int,
            "Level sync correction (DSR only). Probably not useful."),
        'pad_1[6]': (
            'Pad3', False, '<Pad:6>',
            "Null padding."),
    },
    'REINFORCE_PARAM_WEAPON_ST': {
        'physicsAtkRate': (
            'PhysicalDamageMultiplier', True, float,
            "Multiplier applied to outgoing physical damage (of any type)."),
        'magicAtkRate': (
            'MagicDamageMultiplier', True, float,
            "Multiplier applied to outgoing magic damage."),
        'fireAtkRate': (
            'FireDamageMultiplier', True, float,
            "Multiplier applied to outgoing fire damage."),
        'thunderAtkRate': (
            'LightningDamageMultiplier', True, float,
            "Multiplier applied to outgoing lightning damage."),
        'staminaAtkRate': (
            'StaminaDamageMultiplier', True, float,
            "Multiplier applied to the amount of damage dealt to targets' stamina."),
        'saWeaponAtkRate': (
            'PoiseDamageMultiplier', True, float,
            "Multiplier applied to the amount of damage dealt to targets' poise. Never used."),
        'saDurabilityRate': (
            'PoiseDefenseMultiplier', True, float,
            "Multiplier applied to wielder's poise while using (attacking/blocking with?) weapon. Never used."),
        'correctStrengthRate': (
            'StrengthScalingMultiplier', True, float,
            "Multiplier applied to strength scaling of this weapon."),
        'correctAgilityRate': (
            'DexterityScalingMultiplier', True, float,
            "Multiplier applied to dexterity scaling of this weapon."),
        'correctMagicRate': (
            'IntelligenceScalingMultiplier', True, float,
            "Multiplier applied to intelligence scaling of this weapon."),
        'correctFaithRate': (
            'FaithScalingMultiplier', True, float,
            "Multiplier applied to faith scaling of this weapon."),
        'physicsGuardCutRate': (
            'PhysicalGuardReductionMultiplier', True, float,
            "Multiplier applied to the percentage of physical damage blocked by this weapon/shield."),
        'magicGuardCutRate': (
            'MagicGuardReductionMultiplier', True, float,
            "Multiplier applied to the percentage of magic damage blocked by this weapon/shield."),
        'fireGuardCutRate': (
            'FireGuardReductionMultiplier', True, float,
            "Multiplier applied to the percentage of fire damage blocked by this weapon/shield."),
        'thunderGuardCutRate': (
            'LightningGuardReductionMultiplier', True, float,
            "Multiplier applied to the percentage of lightning damage blocked by this weapon/shield."),
        'poisonGuardResistRate': (
            'PoisonGuardResistanceMultiplier', True, float,
            "Multiplier applied to the percentage of poison damage blocked by this weapon/shield."),
        'diseaseGuardResistRate': (
            'ToxicGuardResistanceMultiplier', True, float,
            "Multiplier applied to the percentage of toxic damage blocked by this weapon/shield."),
        'bloodGuardResistRate': (
            'BleedGuardResistanceMultiplier', True, float,
            "Multiplier applied to the percentage of bleed damage blocked by this weapon/shield."),
        'curseGuardResistRate': (
            'CurseGuardResistanceMultiplier', True, float,
            "Multiplier applied to the percentage of curse damage blocked by this weapon/shield."),
        'staminaGuardDefRate': (
            'StaminaGuardReductionMultiplier', True, float,
            "Multiplier applied to the percentage of stamina damage blocked by this weapon/shield."),
        'spEffectId1': (
            'SpecialEffectOnHit0', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 0). Overrides slot 0 of base weapon parameters."),
        'spEffectId2': (
            'SpecialEffectOnHit1', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 1). Overrides slot 1 of base weapon parameters."),
        'spEffectId3': (
            'SpecialEffectOnHit2', True, Params.SpecialEffects,
            "Special effect applied to struck target (slot 2). Overrides slot 2 of base weapon parameters."),
        'residentSpEffectId1': (
            'EquippedSpecialEffect0', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 0). Overrides slot 0 of base weapon "
            "parameters."),
        'residentSpEffectId2': (
            'EquippedSpecialEffect1', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 1). Overrides slot 1 of base weapon "
            "parameters."),
        'residentSpEffectId3': (
            'EquippedSpecialEffect2', True, Params.SpecialEffects,
            "Special effect granted to character with weapon equipped (slot 2). Overrides slot 2 of base weapon "
            "parameters."),
        'materialSetId': (
            'UpgradeMaterialOffset', True, int,
            "Value to be added to Upgrade Materials field in base weapon parameters."),
        'pad[9]': (
            'Pad1', False, '<Pad:9>',
            "Null padding."),
        'reinforcementLevel': (  # DSR ONLY
            'ReinforcementLevel', True, int,
            "<DSR> Reinforcement level. Not sure where this is used; it could be used to calculate the final weapon ID "
            "(e.g. 100005 for Dagger+5)."),
    },
    'MOVE_PARAM_ST': {
        'stayId': (
            'StillAnimation', True, Animation,
            "Animation ID."),
        'walkF': (
            'WalkForwardAnimatiom', True, Animation,
            "Animation ID."),
        'walkB': (
            'WalkBackwardAnimation', True, Animation,
            "Animation ID."),
        'walkL': (
            'StrafeLeftAnimation', True, Animation,
            "Animation ID."),
        'walkR': (
            'StrafeRightAnimation', True, Animation,
            "Animation ID."),
        'dashF': (
            'RunForwardAnimation', True, Animation,
            "Animation ID."),
        'dashB': (
            'RunBackwardAnimation', True, Animation,
            "Animation ID."),
        'dashL': (
            'StrafeRunLeftAnimation', True, Animation,
            "Animation ID."),
        'dashR': (
            'StrafeRunRightAnimation', True, Animation,
            "Animation ID."),
        'superDash': (
            'SprintForwardAnimation', True, Animation,
            "Animation ID."),
        'escapeF': (
            'RollForwardAnimation', True, Animation,
            "Animation ID."),
        'escapeB': (
            'RollBackwardAnimation', True, Animation,
            "Animation ID."),
        'escapeL': (
            'RollLeftAnimation', True, Animation,
            "Animation ID."),
        'escapeR': (
            'RollRightAnimation', True, Animation,
            "Animation ID."),
        'turnL': (
            'TurnLeftAnimation', True, Animation,
            "Animation ID."),
        'trunR': (
            'TurnRightAnimation', True, Animation,
            "Animation ID."),
        'largeTurnL': (
            'LargeTurnLeftAnimation', True, Animation,
            "Animation ID."),
        'largeTurnR': (
            'LargeTurnRightAnimation', True, Animation,
            "Animation ID."),
        'stepMove': (
            'BackstepAnimation', True, Animation,
            "Animation ID."),
        'flyStay': (
            'HoverAnimation', True, Animation,
            "Animation ID."),
        'flyWalkF': (
            'FlyForwardAnimation', True, Animation,
            "Animation ID."),
        'flyWalkFL': (
            'FlyForwardLeftAnimation', True, Animation,
            "Animation ID."),
        'flyWalkFR': (
            'FlyForwardRightAnimation', True, Animation,
            "Animation ID."),
        'flyWalkFL2': (
            'FlyForwardLeft2Animation', True, Animation,
            "Animation ID."),
        'flyWalkFR2': (
            'FlyForwardRight2Animation', True, Animation,
            "Animation ID."),
        'flyDashF': (
            'FlyForwardFastAnimation', True, Animation,
            "Animation ID."),
        'flyDashFL': (
            'FlyForwardLeftFastAnimation', True, Animation,
            "Animation ID."),
        'flyDashFR': (
            'FlyForwardRightFastAnimation', True, Animation,
            "Animation ID."),
        'flyDashFL2': (
            'FlyForwardLeftFast2Animation', True, Animation,
            "Animation ID."),
        'flyDashFR2': (
            'FlyForwardRightFast2Animation', True, Animation,
            "Animation ID."),
        'dashEscapeF': (
            'RunningRollForwardAnimation', True, Animation,
            "Animation ID."),
        'dashEscapeB': (
            'RunningRollBackwardAnimation', True, Animation,
            "Animation ID. (Never used.)"),
        'dashEscapeL': (
            'RunningRollLeftAnimation', True, Animation,
            "Animation ID. (Never used.)"),
        'dashEscapeR': (
            'RunningRollRightAnimation', True, Animation,
            "Animation ID. (Never used.)"),
        'analogMoveParamId': (
            'AnalogMovement', True, int,
            "Movement settings for analog stick version of movement. (Unknown enum.)"),
        'pad[4]': (
            'Pad1', False, '<Pad:4>',
            "Null padding."),
    },
    'SP_EFFECT_VFX_PARAM_ST': {
        'effectType': (
            'EffectType', True, SP_EFFECT_VFX_EFFECT_TYPE,
            "Type of effect. Enum not yet mapped."),
        'midstSfxId': (
            'OngoingVisualEffect', True, '<VisualEffect>',
            "Ongoing visual effect for special effect. -1 is no effect."),
        'midstSeId': (
            'OngoingSoundEffect', True, '<Sound.SFX>',
            "Ongoing sound effect for special effect. -1 is no effect."),
        'midstDmyId': (
            'OngoingModelPoint', True, int,
            "Model point where ongoing effects are centered. -1 is model root."),
        'initSfxId': (
            'InitialVisualEffect', True, '<VisualEffect>',
            "One-off visual effect when special effect begins. -1 is no effect."),
        'initSeId': (
            'InitialSoundEffect', False, '<Sound.SFX>',
            "One-off sound effect when special effect begins. -1 is no effect. (Does not appear to work.)"),
        'initDmyId': (
            'InitialModelPoint', True, int,
            "Model point where initial effect is centered. -1 is model root."),
        'finishSfxId': (
            'FinishVisualEffect', True, '<VisualEffect>',
            "One-off visual effect when special effect ends. -1 is no effect."),
        'finishSeId': (
            'FinishSoundEffect', False, '<Sound.SFX>',
            "One-off sound effect when special effect ends. -1 is no effect. (Does not appear to work.)"),
        'finishDmyId': (
            'FinishModelPoint', True, int,
            "Model point where finish effect is centered. -1 is model root."),
        'camouflageBeginDist': (
            'HideStartDistance', True, float,
            "Closest distance at which effect is disabled."),
        'camouflageEndDist': (
            'HideStartDistance', True, float,
            "Furthest distance at which effect is disabled."),
        'transformProtectorId': (
            'TransformationArmorID', True, Params.Armor,
            "Transformation armor ID. Unknown effect. -1 is no armor."),
        'soulParamIdForWepEnchant': (
            'WeaponEnchantmentSoulParam', True, SP_EFFECT_VFX_SOUL_PARAM_TYPE,
            "Internal description: 'Soul Param ID for weapon enchantment.' Enum not yet mapped."),
        'playCategory': (
            'PlaybackCategory', True, SP_EFFECT_VFX_PLAYCATEGORY,
            "Only one effect in each category can be active at once (determined by PlaybackPriority)."),
        'playPriority': (
            'PlaybackPriority', True, int,
            "Only the lowest-numbered-priority effect in each PlaybackCategory will be active at once."),
        'existEffectForLarge:1': (
            'LargeEffectExists', True, bool,
            "Indicates if a large version of the effect exists."),
        'existEffectForSoul:1': (
            'SoulEffectExists', True, bool,
            "Indicates if a 'soul version' of the effect exists."),
        'effectInvisibleAtCamouflage:1': (
            'InvisibleWhenHidden', True, bool,
            "Indicates if the effect should be invisible when hidden (unclear exactly what this means)."),
        'useCamouflage:1': (
            'HidingActive', True, bool,
            "I believe this determines if the hiding range fields are actually used."),
        'invisibleAtFriendCamouflage:1': (
            'InvisibleWhenFriendHidden', True, bool,
            "Unclear."),
        'addMapAreaBlockOffset:1': (
            'AddMapAreaBlockOffset', True, bool,
            "If enabled, the three-digit area/block number for the current map will be added to all effect IDs "
            "(e.g. m13_02 -> adds 132)."),
        'halfCamouflage:1': (
            'HalfHiddenOnly', True, bool,
            "If enabled, effects are made semi-transparent rather than fully hidden."),
        'isFullBodyTransformProtectorId:1': (
            'ArmorTransformationIsFullBody', True, bool,
            "Indicates whether the armor transformation should be applied to the whole body."),
        'isInvisibleWeapon:1': (
            'HideWeapon', True, bool,
            "Weapon is invisible if enabled."),
        'isSilence:1': (
            'IsSilent', True, bool,
            "Movement noises are silenced if enabled."),
        'pad_1[6]': (
            'Pad1', False, '<Pad:6>',
            "Null padding."),
        'pad[16]': (
            'Pad2', False, '<Pad:16>',
            "Null padding."),
    },
    # TODO
    'FOG_BANK': {
        'fogBeginZ': (
            'FogStartDistance', True, int,
            'Distance (m) at which fog begins.'),
        'fogEndZ': (
            'FogEndDistance', True, int,
            'Distance (m) at which fog ends.'),
        'degRotZ': (
            'RotationZ', True, int,
            'Rotation of fog around the Z axis.'),
        'degRotW': (
            'RotationW', True, int,
            'Rotation of fog around the W axis.'),
        'colR': (
            'Red', True, int,
            'Red color channel (0-255).'),
        'colG': (
            'Green', True, int,
            'Green color channel (0-255).'),
        'colB': (
            'Blue', True, int,
            'Blue color channel (0-255).'),
        'colA': (
            'Alpha', True, int,
            'Alpha channel (0-255).'),
    },
    'LIGHT_BANK': {
        'degRotX_0': (
            'AmbientLight0RotationX', False, int,
            'Rotation (X-axis) of ambient (parallle) light source 0.'),
        'degRotY_0': (
            'AmbientLight0RotationY', False, int,
            'Rotation (Y-axis) of ambient (parallle) light source 0.'),
        'colR_0': (
            'AmbientLight0Red', False, int,
            'Red channel (0-255) of ambient (parallle) light source 0.'),
        'colG_0': (
            'AmbientLight0Green', False, int,
            'Green channel (0-255) of ambient (parallle) light source 0.'),
        'colB_0': (
            'AmbientLight0Blue', False, int,
            'Blue channel (0-255) of ambient (parallle) light source 0.'),
        'colA_0': (
            'AmbientLight0Alpha', False, int,
            'Alpha channel (0-255) of ambient (parallle) light source 0.'),
        'degRotX_1': (
            'AmbientLight1RotationX', False, int,
            'Rotation (X-axis) of ambient (parallle) light source 1.'),
        'degRotY_1': (
            'AmbientLight1RotationY', False, int,
            'Rotation (Y-axis) of ambient (parallle) light source 1.'),
        'colR_1': (
            'AmbientLight1Red', False, int,
            'Red channel (0-255) of ambient (parallle) light source 1.'),
        'colG_1': (
            'AmbientLight1Green', False, int,
            'Green channel (0-255) of ambient (parallle) light source 1.'),
        'colB_1': (
            'AmbientLight1Blue', False, int,
            'Blue channel (0-255) of ambient (parallle) light source 1.'),
        'colA_1': (
            'AmbientLight1Alpha', False, int,
            'Alpha channel (0-255) of ambient (parallle) light source 1.'),
        'degRotX_2': (
            'AmbientLight2RotationX', False, int,
            'Rotation (X-axis) of ambient (parallle) light source 2.'),
        'degRotY_2': (
            'AmbientLight2RotationY', False, int,
            'Rotation (Y-axis) of ambient (parallle) light source 2.'),
        'colR_2': (
            'AmbientLight2Red', False, int,
            'Red channel (0-255) of ambient (parallle) light source 2.'),
        'colG_2': (
            'AmbientLight2Green', False, int,
            'Green channel (0-255) of ambient (parallle) light source 2.'),
        'colB_2': (
            'AmbientLight2Blue', False, int,
            'Blue channel (0-255) of ambient (parallle) light source 2.'),
        'colA_2': (
            'AmbientLight2Alpha', False, int,
            'Alpha channel (0-255) of ambient (parallle) light source 2.'),
        'colR_u': (
            'TopDownLightRed', True, int,
            'Red channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colG_u': (
            'TopDownLightGreen', True, int,
            'Green channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colB_u': (
            'TopDownLightBlue', True, int,
            'Blue channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colA_u': (
            'TopDownLightAlpha', True, int,
            'Alpha channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colR_d': (
            'BottomUpLightRed', True, int,
            'Red channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colG_d': (
            'BottomUpLightGreen', True, int,
            'Green channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colB_d': (
            'BottomUpLightBlue', True, int,
            'Blue channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'colA_d': (
            'BottomUpLightAlpha', True, int,
            'Alpha channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for '
            'surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until the '
            'surface is oriented sideways (e.g. walls).'),
        'degRotX_s': (
            'SpecularAmbientLightRotationX', True, int,
            'Rotation (X-axis) of specular ambient (parallel) light source.'),
        'degRotY_s': (
            'SpecularAmbientLightRotationY', True, int,
            'Rotation (Y-axis) of specular ambient (parallel) light source.'),
        'colR_s': (
            'SpecularAmbientLightRed', True, int,
            'Red channel (0-255) of specular ambient light source.'),
        'colG_s': (
            'SpecularAmbientLightGreen', True, int,
            'Green channel (0-255) of specular ambient light source.'),
        'colB_s': (
            'SpecularAmbientLightBlue', True, int,
            'Blue channel (0-255) of specular ambient light source.'),
        'colA_s': (
            'SpecularAmbientLightAlpha', True, int,
            'Alpha channel (0-255) of specular ambient light source.'),
        'envDif_colR': (
            'DiffuseLightRed', True, int,
            'Red channel (0-255) of base diffuse ambient light of surfaces.'),
        'envDif_colG': (
            'DiffuseLightGreen', True, int,
            'Green channel (0-255) of base diffuse ambient light of surfaces.'),
        'envDif_colB': (
            'DiffuseLightBlue', True, int,
            'Blue channel (0-255) of base diffuse ambient light of surfaces.'),
        'envDif_colA': (
            'DiffuseLightAlpha', True, int,
            'Alpha channel (0-255) of base diffuse ambient light of surfaces.'),
        'envSpc_colR': (
            'SpecularLightRed', True, int,
            'Red channel (0-255) of specular ambient light of surfaces.'),
        'envSpc_colG': (
            'SpecularLightGreen', True, int,
            'Green channel (0-255) of specular ambient light of surfaces.'),
        'envSpc_colB': (
            'SpecularLightBlue', True, int,
            'Blue channel (0-255) of specular ambient light of surfaces.'),
        'envSpc_colA': (
            'SpecularLightAlpha', True, int,
            'Alpha channel (0-255) of specular ambient light of surfaces.'),
        'envDif': (
            'DiffuseLightTextureID', False, int,
            'Changing this has drastic effects on the diffuse ambient light.'),
        'envSpc_0': (
            'SpecularLightTextureID0', False, int,
            'Changing this has drastic effects on the specular ambient light.'),
        'envSpc_1': (
            'SpecularLightTextureID1', False, int,
            'Changing this has drastic effects on the specular ambient light.'),
        'envSpc_2': (
            'SpecularLightTextureID2', False, int,
            'Changing this has drastic effects on the specular ambient light.'),
        'envSpc_3': (
            'SpecularLightTextureID3', False, int,
            'Changing this has drastic effects on the specular ambient light.'),
        'pad[2]': (
            'Pad1', False, '<Pad:2>',
            'Null padding.'),
    },
    'LIGHT_SCATTERING_BANK': {
        'sunRotX': (
            'LightRotationX', True, int,
            'Rotation (X-axis) of scattering light source.'),
        'sunRotY': (
            'LightRotationY', True, int,
            'Rotation (Y-axis) of scattering light source.'),
        'distanceMul': (
            'DistanceMultiplier', True, int,
            'Magnification (0-100) of scattering light source distance.'),
        'sunR': (
            'LightRed', True, int,
            'Red channel (0-255) of scattering light source.'),
        'sunG': (
            'LightGreen', True, int,
            'Green channel (0-255) of scattering light source.'),
        'sunB': (
            'LightBlue', True, int,
            'Blue channel (0-255) of scattering light source.'),
        'sunA': (
            'LightAlpha', True, int,
            'Alpha channel (0-255) of scattering light source.'),
        'pad_0[2]': (
            'Pad0', False, '<Pad:2>',
            'Null padding.'),
        'lsHGg': (
            'ScatteringDirection', True, float,
            'Coefficient of scattering direction, between -1 (backward) and 1 (forward).'),
        'lsBetaRay': (
            'RayleighCoefficient', True, float,
            'Coefficient determining how much light is lost to scattering (e.g. simulating amount of atmosphere).'),
        'lsBetaMie': (
            'MieCoefficient', True, float,
            'Coefficient determining how much light is scattered by larger particles (e.g. simulating dust/smoke).'),
        'blendCoef': (
            'ScatteringCoefficient', True, int,
            'Coefficient determining the overall amount of scattering from 0 (no scattering) to 100 (max scattering).'),
        'reflectanceR': (
            'SurfaceReflectanceRed', True, int,
            'Red channel (0-255) of the effect of the scattered light as it hits surfaces.'),
        'reflectanceG': (
            'SurfaceReflectanceGreen', True, int,
            'Green channel (0-255) of the effect of the scattered light as it hits surfaces.'),
        'reflectanceB': (
            'SurfaceReflectanceBlue', True, int,
            'Blue channel (0-255) of the effect of the scattered light as it hits surfaces.'),
        'reflectanceA': (
            'SurfaceReflectanceAlpha', True, int,
            'Alpha channel (0-255) of the effect of the scattered light as it hits surfaces.'),
        'pad_1[2]': (
            'Pad1', False, '<Pad:2>',
            'Null padding.'),
    },
    'POINT_LIGHT_BANK': {
        'dwindleBegin': (
            'FadeStartDistance', True, float,
            "Distance at which player's point light begins to fade."),
        'dwindleEnd': (
            'FadeEndDistance', True, float,
            "Distance at which player's point light finishes fading and disappears entirely."),
        'colR': (
            'PlayerLightRed', True, int,
            'Red channel (0-255) of point light.'),
        'colG': (
            'PlayerLightGreen', True, int,
            'Green channel (0-255) of point light.'),
        'colB': (
            'PlayerLightBlue', True, int,
            'Blue channel (0-255) of point light.'),
        'colA': (
            'PlayerLightAlpha', True, int,
            'Alpha channel (0-255) of point light.'),
    },
    'LENS_FLARE_BANK': {
        'texId': (
            'LensFlareTextureID', True, int,
            "Texture ID of lens flare (texture name format is 'lensflare_XX'). -1 means disabled."),
        'isFlare': (
            'IsLensFlare', True, bool,
            "Flare if enabled, or 'ghost' if disabled."),
        'enableRoll': (
            'EnableRotation', True, bool,
            'Allows lens flare texture to rotate with camera.'),
        'enableScale': (
            'EnableScaling', True, bool,
            'Allows lens flare texture to change scale with camera.'),
        'locateDistRate': (
            'PositionRatio', True, float,
            'Relative position of lens flare between light source (0.0) and center of screen (1.0).'),
        'texScale': (
            'TextureScale', True, float,
            'Base scaling of lens flare texture.'),
        'colR': (
            'TextureRed', True, int,
            'Red channel (0-255) of lens flare texture.'),
        'colG': (
            'TextureGreen', True, int,
            'Green channel (0-255) of lens flare texture.'),
        'colB': (
            'TextureBlue', True, int,
            'Blue channel (0-255) of lens flare texture.'),
        'colA': (
            'TextureAlpha', True, int,
            'Alpha channel (0-255) of lens flare texture.'),
    },
    'LENS_FLARE_EX_BANK': {
        'lightDegRotX': (
            'LensFlareSourceRotationX', True, int,
            'Rotation (X-axis) of visible light source (e.g. sun) that causes lens flares.'),
        'lightDegRotY': (
            'LensFlareSourceRotationX', True, int,
            'Rotation (Y-axis) of visible light source (e.g. sun) that causes lens flares.'),
        'colR': (
            'LensFlareSourceRed', True, int,
            'Red channel (0-255) of visible light source (e.g. sun).'),
        'colG': (
            'LensFlareSourceGreen', True, int,
            'Green channel (0-255) of visible light source (e.g. sun).'),
        'colB': (
            'LensFlareSourceBlue', True, int,
            'Blue channel (0-255) of visible light source (e.g. sun).'),
        'colA': (
            'LensFlareSourceAlpha', True, int,
            'Alpha channel (0-255) of visible light source (e.g. sun).'),
        'lightDist': (
            'LensFlareSourceDistance', True, float,
            'Distance of visible light source (e.g. sun). Not sure about the units.'),
    },
    'DOF_BANK': {
        'farDofBegin': (
            'FarBlurStartDistance', True, float,
            'Distance (m) at which far depth of field blur begins.'),
        'farDofEnd': (
            'FarBlurEndDistance', True, float,
            'Distance (m) at which far depth of field blur ends (reaches maximum).'),
        'farDofMul': (
            'FarBlurMagnitude', True, int,
            'Amount of far depth of field blur applied between the start and end distances.'),
        'pad_0[3]': (
            'Pad0', False, '<Pad:3>',
            'Null padding.'),
        'nearDofBegin': (
            'NearBlurStartDistance', True, float,
            'Distance (m) at which near depth of field blur begins (further away than end distance).'),
        'nearDofEnd': (
            'NearBlurEndDistance', True, float,
            'Distance (m) at which near depth of field blur ends (reaches maximum) (closer than start distance).'),
        'nearDofMul': (
            'NearBlurMagnitude', True, int,
            'Amount of near depth of field blur applied between start and end distances.'),
        'pad_1[3]': (
            'Pad1', False, '<Pad:3>',
            'Null padding.'),
        'dispersionSq': (
            'BlurSquaredDispersion', True, float,
            'Squared dispersion of depth of field blur (greater value means more blur).'),
    },
    'TONE_MAP_BANK': {
        'bloomBegin': (
            'NearBloomThreshold', True, int,
            'Near light blooming begins when brightness exceeds this threshold.'),
        'bloomMul': (
            'NearBloomMultiplier', True, int,
            'Near light blooming multiplier.'),
        'bloomBeginFar': (
            'FarBloomThreshold', True, int,
            'Far light blooming begins when brightness exceeds this threshold.'),
        'bloomMulFar': (
            'FarBloomMultiplier', True, int,
            'Far light blooming multiplier.'),
        'bloomNearDist': (
            'NearBloomEndDistance', True, float,
            'Near bloom parameters apply up to this maximum distance.'),
        'bloomFarDist': (
            'FarBloomStartDistance', True, float,
            'Far bloom parameters apply beyond this minimum distance.'),
        'grayKeyValue': (
            'OverallBrightness', True, float,
            'Larger values make the screen brighter overall.'),
        'minAdaptedLum': (
            'MinimumAdaptationBrightness', True, float,
            'Minimum brightness for tone adaptation. Smaller values mean that darker places will be adapted.'),
        'maxAdapredLum': (
            'MaximumAdaptationBrightness', True, float,
            'Maximum brightness for tone adaptation. Larger values mean that brighter places will be adapted.'),
        'adaptSpeed': (
            'AdaptationSpeed', True, float,
            'Tone adaptation speed.'),
        'lightShaftBegin': (
            'LightShaftThreshold', True, int,
            'Light shafts will appear when brightness exceeds this threshold.'),
        'pad_0[3]': (
            'Pad0', True, '<Pad:3>',
            'Null padding.'),
        'lightShaftPower': (
            'LightShaftMagnitude', True, float,
            'Light shaft magnitude (0 means no light shafts).'),
        'lightShaftAttenRate': (
            'LightShaftAttenuationRate', True, float,
            'Smaller values will shorten the light shafts more.'),
    },
    'TONE_CORRECT_BANK': {
        'brightnessR': (
            'BrightnessRed', True, float,
            'Red channel (0-255) of tone correction brightness.'),
        'brightnessG': (
            'BrightnessGreen', True, float,
            'Green channel (0-255) of tone correction brightness.'),
        'brightnessB': (
            'BrightnessBlue', True, float,
            'Blue channel (0-255) of tone correction brightness.'),
        'contrastR': (
            'ContrastRed', True, float,
            'Red channel (0-255) of tone correction contrast.'),
        'contrastG': (
            'ContrastGreen', True, float,
            'Green channel (0-255) of tone correction contrast.'),
        'contrastB': (
            'ContrastBlue', True, float,
            'Blue channel (0-255) of tone correction contrast.'),
        'saturation': (
            'SaturationCorrection', True, float,
            'Color saturation correction value.'),
        'hue': (
            'HueCorrection', True, float,
            'Color hue correction value.'),
    },
    'SHADOW_BANK': {
        'lightDegRotX': (
            'ShadowSourceRotationX', True, int,
            'Rotation (X-axis) of shadow-casting light source.'),
        'lightDegRotY': (
            'ShadowSourceRotationY', True, int,
            'Rotation (Y-axis) of shadow-casting light source.'),
        'densityRatio': (
            'ShadowDensityPercentage', True, int,
            'Density of cast shadow (0-100), where 100 is the darkest.'),
        'colR': (
            'ShadowRed', True, int,
            'Red channel (0-255) of cast shadow.'),
        'colG': (
            'ShadowGreen', True, int,
            'Green channel (0-255) of cast shadow.'),
        'colB': (
            'ShadowBlue', True, int,
            'Blue channel (0-255) of cast shadow.'),
        'beginDist': (
            'ShadowStartDistance', True, float,
            "Minimum distance (m) at which shadoes are cast. A value of 0 means the camera's near-clip plane is used."),
        "endDist": (
            'ShadowEndDistance', True, float,
            'Maximum distance (m) at which shadows are cast.'),
        'calibulateFar': (
            'HeadOnDistanceReduction', True, float,
            'Shorten the shadow end distance by this distance when facing the light source direction.'),
        'fadeBeginDist': (
            'FadeStartDistance', True, float,
            'Shadow starts fading at this distance.'),
        'fadeDist': (
            'FadeDistance', True, float,
            'Distance (after start distance) until shadow is fully faded.'),
        'persedDepthOffset': (
            'DepthOffset', True, float,
            "Depth offset for shadows. With negative values, self-shadows are less likely to occur."),
        'ｇradFactor': (
            'ShadowMapStrength', True, float,
            'Negative values weaken the shadow map, positive values strengthen it.'),
        'shadowVolumeDepth': (
            'ShadowVolumeDepth', True, float,
            'Increase this value to cast shadows on tall objects such as buildings.'),
    },
    # 'LENS_FLAG_EX_BANK': 'LensFlareExBank',  # unused
    # 'ENV_LIGHT_TEX_BANK': 'EnvLightTexBank',  # unused
    # 'LOD_BANK': 'LodBank',  # unused
}
