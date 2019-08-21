from functools import partial

from .enums import *

__all__ = ['GAME_PARAM_NICKNAMES', 'GAME_PARAM_INFO']


# Overrides for certain basic enums.
ATK_PARAM_HIT_SOURCE = int
SP_EFFECT_SPCATEGORY = int

ATK_PARAM_BOOL = bool
DURABILITY_DIVERGENCE_CATEGORY = bool
EQUIP_BOOL = bool
MAGIC_BOOL = bool
NPC_BOOL = bool
NPC_THINK_REPLY_BEHAVIOR_TYPE = bool
ON_OFF = bool
RAGDOLL_PARAM_BOOL = bool
SP_EFFECT_BOOL = bool

class AI:
    Logic = '<AI:Logic>'
    Battle = '<AI:Battle>'


Animation = '<Animation>'
Flag = '<Flag>'
Model = '<Model>'
Texture = '<Texture>'


class Params:
    AI = '<Params:AI>'
    Armor = '<Params:Armor>'
    Attacks = '<Params:Attacks>'
    Behaviors = '<Params:Behaviors>'
    Bosses = '<Params:Bosses>'
    Bullets = '<Params:Bullets>'
    Cameras = '<Params:Cameras>'
    Conversations = '<Params:Conversations>'
    Faces = '<Params:Faces>'
    Goods = '<Params:Goods>'
    ItemLots = '<Params:ItemLots>'
    Knockback = '<Params:Knockback>'
    Rings = '<Params:Rings>'
    SpecialEffects = '<Params:SpecialEffects>'
    Spells = '<Params:Spells>'
    Terrains = '<Params:Terrains>'
    SpecialEffectVisuals = '<Params:SpecialEffectVisuals>'
    Weapons = '<Params:Weapons>'


class Sound:
    SFX = '<Sound:SFX>'


class Text:
    Conversations = '<Text:Conversations>'
    EventText = '<Text:EventText>'
    NPCNames = '<Text:NPCNames>'


def behavior_ref_id(behavior_param_entry):
    if behavior_param_entry['refType'] == BEHAVIOR_REF_TYPE.Attack:
        return ('AttackID', True, Params.Attacks,
                "Attack ID triggered by behavior.")
    elif behavior_param_entry['refType'] == BEHAVIOR_REF_TYPE.Bullet:
        return ('BulletID', True, Params.Bullets,
                "Bullet ID triggered by behavior.")
    else:
        return ('UnknownReferenceID', True, int,
                "Could not determine reference ID type (usually Attack or Bullet).")


def obj_act_success_condition(condition_field_name, obj_act_param_entry):
    if obj_act_param_entry[condition_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasGood:
        return ('RequiredGood', True, Params.Goods,
                "First condition: object action will succeed if user has this good in their inventory (does not "
                "include Bottomless Box).")
    elif obj_act_param_entry[condition_field_name] == OBJACT_SP_QUALIFIED_TYPE.HasSpecialEffect:
        return ('RequiredSpecialEffect', True, Params.SpecialEffects,
                "First condition: object action will succeed if user has this special effect.")
    else:
        return ('UnknownCondition', True, int,
                "Could not determine success condition ID type (usually HasGood or HasSpecialEffect).")


def item_lot_item_id(item_lot_slot: int, item_lot_param_entry):
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


def shop_item_id(shops_param_entry):
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


GAME_PARAM_NICKNAMES = {
    # Nicknames are per BND entry basename, not per internal param table name.
    'NpcThinkParam': 'AI',
    'EquipParamProtector': 'Armor',
    'ReinforceParamProtector': 'ArmorUpgrades',
    'GameAreaParam': 'Bosses',
    'Bullet': 'Bullets',  # note not 'BulletParam'
    # 'CalcCorrectGraph': 'CalcCorrectionGraph',
    'LockCamParam': 'Cameras',
    # 'default_EnemyBehaviorBank': 'DefaultEnemyBehavior',
    # 'default_AIStandardInfoBank': 'DefaultAIStandardInfoBank',
    'CharaInitParam': 'Humans',
    'AtkParam_Pc': 'HumanAttacks',
    'BehaviorParam_PC': 'HumanBehaviors',
    'TalkParam': 'Dialogue',
    'FaceGenParam': 'Faces',
    'EquipParamGoods': 'Goods',
    'ItemLotParam': 'ItemLots',
    'KnockbackParam': 'Knockback',
    'MenuColorTableParam': 'MenuColors',
    'MoveParam': 'Movement',
    'NpcParam': 'NonHumans',
    'AtkParam_Npc': 'NonHumanAttacks',
    'BehaviorParam': 'NonHumanBehaviors',
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
    'SpEffectVfxParam': 'VisualEffects',
    'EquipParamWeapon': 'Weapons',
    'ReinforceParamWeapon': 'WeaponUpgrades',

    # TODO: DrawParams?
}


GAME_PARAM_INFO = {
    # PARAM_TABLE_NAME: (ParamEntryNickname, VisibleDefault, ParamTableType, Docstring)

    'NPC_THINK_PARAM_ST': {
        'logicId': (
            'LogicID', True, AI.Logic,
            "ID of logic (non-battle) Lua script."),
        'battleGoalID': (
            'BattleID', True, AI.Battle,
            "Battle goal ID used to look up battle Lua script."),
        'nearDist': (
            'NearDistance', True, None,
            "Distance considered to be close range by this NPC (for scripts)."),
        'midDist': (
            'MidDistance', True, None,
            "Distance considered to be medium range by this NPC (for scripts)."),
        'farDist': (
            'FarDistance', True, None,
            "Distance considered to be long range by this NPC (for scripts)."),
        'outDist': (
            'OutOfRangeDistance', True, None,
            "Distance beyond which the NPC will not attempt to fight."),
        'BackHomeLife_OnHitEneWal': (
            'RetreatTimeOnHitEnemyWal', False, None,
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
            'SightDistance', True, None,
            "Distance of NPC eyesight (in meters)."),
        'ear_dist': (
            'HearingDistance', True, None,
            "Distance of NPC hearing (in meters)."),
        'ear_soundcut_dist': (
            'HearingCutDistance', False, None,
            "Internal description: 'Distance to reduce the size of the sound source. Sounds less "
            "than this distance will not be heard.' Set to 1 for Bloatheads and Bloathead Sorcerers "
            "and 0 for everyone else."),
        'nose_dist': (
            'SmellDistance', True, None,
            "Distance of NPC smell (auto-detect)."),
        'maxBackhomeDist': (
            'MaxRetreatDistance', True, None,
            "Absolute furthest the NPC can travel from their nest before retreating, in or out of "
            "battle. (Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.) Usually set to "
            "about 50% more than BattleRetreatDistance."),
        'backhomeDist': (
            'BattleRetreatDistance', True, None,
            "Furthest distance the NPC can travel from their nest before retreating in battle. (Argument "
            "of internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'backhomeBattleDist': (
            'RetreatBattleStartDistance', True, None,
            "Target distance at which battle mode is triggered while the enemy is retreating. "
            "(Argument of internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'nonBattleActLife': (
            'NonBattleActLife', False, None,
            "Lifespan of Acts outside of battle. Set to 10 for Bloatheads and Bloathead Sorcerers, "
            "0 for Priscilla's Tail and the Bed of Chaos bug, and 5 for everyone else. (Argument of "
            "internal GOAL function 'COMMON_SetBattleActLogic()'.)"),
        'BackHome_LookTargetTime': (
            'SearchTimeBeforeRetreat', True, None,
            "Time that NPC will search for a lost target before retreating (I think). Set to "
            "20 for everyone except the Bounding Demons of Izalith, who have a value of 0."),
        'BackHome_LookTargetDist': (
            'SearchDistanceBeforeRetreat', True, None,
            "Distance that NPC will search for a lost target before retreating (I think). Set "
            "to 20 for everyone except the Bounding Demons of Izaltih, who have a value of 0."),
        'SightTargetForgetTime': (
            'SightForgetTime', True, None,
            "Time to forget about sighted targets. Usually set to 600."),
        'SoundTargetForgetTime': (
            'HearingForgetTime', True, None,
            "Time to forget about heard targets. Usually set to 300."),
        'BattleStartDist': (
            'BattleStartDistance', True, None,
            "Target distance at which battle mode is triggered."),
        'callHelp_MyPeerId': (
            'HelpGroupID', True, None,
            "Determines which calls for help this NPC will respond to (must match caller's "
            "HelpCallGroupID). Only 0 (no ID) and 1 are used."),
        'callHelp_CallPeerId': (
            'HelpCallGroupID', True, None,
            "HelpGroupID value of NPCs who should respond to calls for help by this NPC. Only 0 "
            "(no ID) and 1 are used."),
        'targetSys_DmgEffectRate': (
            'TargetSysDamageRate', False, None,
            "Internal description: 'Get damage rate (%) for target system evaluation "
            "information.' Set to 0 for summons, phantoms, and the Parasitic Wall Hugger, and "
            "100 for everyone else."),
        'TeamAttackEffectivity': (
            'TeamAttackEffectivity', True, None,
            "Value from 0 to 100 that determines the number of simultaneous attacks made by this "
            "NPC's team. Higher values mean that less members of this team can participate in "
            "attacks at the same time. (I presume that the total score of attacking team members "
            "cannot exceed 100.) Usually set to 25 or 100."),
        # TODO: Apparently X is height and Y is width here. The internal descriptions or names may be incorrect.
        'eye_angX': (
            'SightRangeHeight', True, None,
            "Angular width of sight field in degrees."),
        'eye_angY': (
            'SightRangeWidth', True, None,
            "Angular height of sight field in degrees."),
        'ear_angX': (
            'HearingRangeHeight', True, None,
            "Angular width of hearing field in degrees."),
        'ear_angY': (
            'HearingRangeWidth', True, None,
            "Angular height of hearing field in degrees."),
        'callHelp_CallValidMinDistTarget': (
            'HelpCallTargetMinDistance', False, None,
            "Minimum distance from AI target for help call to be made. Always zero."),
        'callHelp_CallValidRange': (
            'HelpCallFriendMaxDistance', True, None,
            "Maximum distance of friend to receive help call from this NPC. Set to 50 for both "
            "Male and Female Ghosts, and 0 for everyone else."),
        'callHelp_ForgetTimeByArrival': (
            'HelpCallForgetTime', True, None,
            "Time until call for help is forgotten by responder."),
        'callHelp_MinWaitTime': (
            'HelpCallMinWaitTime', True, None,
            "Internal description: 'Minimum time for response goal at first waiting goal'. Units "
            "are in tenths of a second. Only used for Male Ghosts (20)."),
        'callHelp_MaxWaitTime': (
            'HelpCallMaxWaitTime', True, None,
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
            'IgnoreNavimesh', True, bool,  # NOTE: Not a boolean field, but used like one.
            "If 1, this NPC will ignore navimesh when moving. True for Ghosts and enemies that don't "
            "move at all."),
        'skipArrivalVisibleCheck': (
            'SkipArrivalVisibleCheck', False, bool,
            "Internal description: 'If enabled, arrival determination is performed even if the "
            "line of sight is not passed.' True only for Hawkeye Gough."),
        'thinkAttr_doAdmirer': (
            'AdmirerAttribute', True, None,
            "Internal description: 'Thought attribute: when enabled, it plays the role of a wrap.' "
            "I don't know exactly what that means, but this is likely important for something. "
            "Enabled for Soulmass and Pursuers, non-giant Rats, Infested Ghouls, Mushrooms, most "
            "Hollows (not archers), Male Ghosts, normals Skeletons and Skeleton Beasts, Pisaca, "
            "Gardeners, Bloatheads (not Sorcerers), Humanity Phantoms, and the Four Kings."),
        'enableNaviFlg_Edge:1': (
            'CanFallOffEdges', True, None,
            "If True, this NPC will pursue targets off navimesh edges (survivable falls)."),
        'enableNaviFlg_LargeSpace:1': (
            'CanNavigateWideSpaces', True, None,
            "If True, this NPC can enter navimesh regions flagged as 'large spaces'."),
        'enableNaviFlg_Ladder:1': (
            'CanNavigateLadders', True, None,
            "If True, this NPC will use ladders."),
        'enableNaviFlg_Hole:1': (
            'CanNavigateHoles', True, None,
            "If True, this NPC can fall into navimesh holes."),
        'enableNaviFlg_Door:1': (
            'CanNavigateDoors', True, None,
            "If True, this NPC can go through doors (but not necessarily open closed doors)."),
        'enableNaviFlg_InSideWall:1': (
            'CanNavigateInsideWalls', True, None,
            "If True, this NPC can go through walls (i.e. ignores navimesh walls)."),
        'enableNaviFlg_reserve0:2': (
            'UnusedNavimeshCheckX2', False, None,
            "Two unused bytes reserved for other navimesh checks. No effect."),
        'enableNaviFlg_reserve1[3]': (
            'UnusedNavimeshCheckX3', False, None,
            "Three unused bytes reserved for other navimesh checks. No effect."),
        'pad0[12]': (
            'Pad0', False, None,
            "Null padding."),
    },
    'EQUIP_PARAM_PROTECTOR_ST': {
        'sortId': (
            'SortIndex', True, None,
            "Index for automatic inventory sorting."),
        'NetworkGhostReplacement': (
            'Ghost.', True, Params.Armor,
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
            "Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
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
            'UpgradeMaterialID', True, '<Param:UpgradeMaterials>',
            "Upgrade material set for reinforcement."),
        'partsDamageRate': (
            'SiteDamageMultiplier', True, None,
            "Multiplier for damage taken to this part of the body. Used to specify weakness, not strength, so is "
            "never less than 1. Usually 1.5 for weak head pieces, 1.3 for strong head pieces, 1.1 for gauntlets "
            "and leggings, and 1 for torso armor."),
        'corectSARecover': (
            'PoiseRecoveryTimeModifier', True, None,
            "Value added to poise recovery time (so negative values are better). -0.1 for heavy armor and 0 "
            "otherwise."),
        'originEquipPro': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 0 of this armor (i.e. what you receive when a blacksmith removes upgrades). "
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro1': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 1 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro2': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 2 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro3': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 3 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro4': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 4 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro5': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 5 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro6': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 6 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro7': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 7 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro8': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 8 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro9': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 9 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro10': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 10 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro11': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 11 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro12': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 12 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro13': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 13 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro14': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 14 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'originEquipPro15': (
            'UpgradeOrigin0', True, None,
            "Origin armor for level 15 of this armor (i.e. what you receive when a blacksmith removes upgrades)."
            "If -1, the armor cannot be reverted. Otherwise, it will appear in each blacksmith's reversion menu."),
        'faceScaleM_ScaleX': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleM_ScaleZ': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleM_MaxX': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleM_MaxZ': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleF_ScaleX': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleF_ScaleZ': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleF_MaxX': (
            '', True, None,
            "DOC-TODO"),
        'faceScaleF_MaxZ': (
            '', True, None,
            "DOC-TODO"),
        'qwcId': (
            'QWC', True, '<Params:QWC>',  # TODO: Am I including QWC?
            "DOC-TODO"),
        'equipModelId': (
            'EquipmentModel', True, '<Model>',
            "DOC-TODO"),
        'iconIdM': (
            'MaleIcon', True, '<Icon>',
            "DOC-TODO"),
        'iconIdF': (
            'FemaleIcon', True, '<Icon>',
            "DOC-TODO"),
        'knockBack': (
            'KnockbackMultiplier', True, None,
            "DOC-TODO"),
        'knockbackBounceRate': (
            'KnockbackDeflectRate', True, None,
            "DOC-TODO"),
        'durability': (
            'InitialDurability', True, None,
            "Durability of armor when it is obtained. Always equal to max durability in vanilla game."),
        'durabilityMax': (
            'MaxDurability', True, None,
            "Maximum durability of armor."),
        'saDurability': (
            'Poise', True, None,
            "Amount of poise added when wearing armor."),
        'defFlickPower': (
            'RepelDefense', True, None,
            "DOC-TODO"),
        'defensePhysics': (
            'PhysicalDefense', True, None,
            "DOC-TODO"),
        'defenseMagic': (
            'MagicDefense', True, None,
            "DOC-TODO"),
        'defenseFire': (
            'FireDefense', True, None,
            "DOC-TODO"),
        'defenseThunder': (
            'LightningDefense', True, None,
            "DOC-TODO"),
        'defenseSlash': (
            'SlashDefense', True, None,
            "DOC-TODO"),
        'defenseBlow': (
            'StrikeDefense', True, None,
            "DOC-TODO"),
        'defenseThrust': (
            'ThrustDefense', True, None,
            "DOC-TODO"),
        'resistPoison': (
            'PoisonResistance', True, None,
            "DOC-TODO"),
        'resistDisease': (
            'ToxicResistance', True, None,
            "DOC-TODO"),
        'resistBlood': (
            'BleedResistance', True, None,
            "DOC-TODO"),
        'resistCurse': (
            'CurseResistance', True, None,
            "DOC-TODO"),
        'reinforceTypeId': (
            'ReinforcementID', True, '<Params:ArmorUpgrades>',
            "DOC-TODO"),
        'trophySGradeId': (
            'AchievementContributionID', True, None,
            "Index of armor as it contributes to certain multi-item achievements."),
        'shopLv': (
            'ShopLevel', False, None,
            "Level of armor that can be sold in 'the shop'. Always -1 or 0. Probably unused."),
        'knockbackParamId': (
            'KnockbackID', True, '<Params:Knockback>',
            "DOC-TODO"),
        'flickDamageCutRate': (
            'RepelDamageMultiplier', True, None,
            "I think this affects damage taken during a missed parry."),
        'equipModelCategory': (
            'EquipmentModelCategory', True, EQUIP_MODEL_CATEGORY,
            "DOC-TODO"),
        'equipModelGender': (
            'EquipmentModelGender', True, EQUIP_MODEL_GENDER,
            "DOC-TODO"),
        'protectorCategory': (
            'ArmorType', True, PROTECTOR_CATEGORY,
            "DOC-TODO"),
        'defenseMaterial': (
            'DefenseMaterialVisualEffect', True, None,
            "DOC-TODO"),
        'defenseMaterialSfx': (
            'DefenseMaterialSound', True, None,
            "DOC-TODO"),
        'partsDmgType': (
            'PartsDamageType', False, None,  # TODO: Type is possibly ATK_PARAM_PARTSDMGTYPE
            "Always zero."),
        'defenseMaterial_Weak': (
            'WeakDefenseMaterialVisualEffect', True, None,
            "Visual effects for when damage is taken to weak spot (used for head armor)."),
        'defenseMaterialSfx_Weak': (
            'WeakDefenseMaterialSound', True, None,
            "Sound to play when damage is taken to weak spot (used for head armor)."),
        'isDeposit:1': (
            'CanBeStored', True, bool,
            "If True, this armor can be stored in the Bottomless Box. Always False for armor."),
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
            "DOC-TODO"),
        'invisibleFlag00:1': (
            'HideFlag0', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag01:1': (
            'HideFlag1', False, None,
            "Hide part of the character model: (hair fringe)"),
        'invisibleFlag02:1': (
            'HideFlag2', False, None,
            "Hide part of the character model: (sideburns)"),
        'invisibleFlag03:1': (
            'HideFlag3', False, None,
            "Hide part of the character model: (top of head)"),
        'invisibleFlag04:1': (
            'HideFlag4', False, None,
            "Hide part of the character model: (top of head)"),
        'invisibleFlag05:1': (
            'HideFlag5', False, None,
            "Hide part of the character model: (back hair)"),
        'invisibleFlag06:1': (
            'HideFlag6', False, None,
            "Hide part of the character model: (back hair tip)"),
        'invisibleFlag07:1': (
            'HideFlag7', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag08:1': (
            'HideFlag8', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag09:1': (
            'HideFlag9', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag10:1': (
            'HideFlag10', False, None,
            "Hide part of the character model: (collar)"),
        'invisibleFlag11:1': (
            'HideFlag11', False, None,
            "Hide part of the character model: (around collar)"),
        'invisibleFlag12:1': (
            'HideFlag12', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag13:1': (
            'HideFlag13', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag14:1': (
            'HideFlag14', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag15:1': (
            'HideFlag15', False, None,
            "Hide part of the character model: (hood hem)"),
        'invisibleFlag16:1': (
            'HideFlag16', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag17:1': (
            'HideFlag17', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag18:1': (
            'HideFlag18', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag19:1': (
            'HideFlag19', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag20:1': (
            'HideFlag20', False, None,
            "Hide part of the character model: (sleeve A)"),
        'invisibleFlag21:1': (
            'HideFlag21', False, None,
            "Hide part of the character model: (sleeve B)"),
        'invisibleFlag22:1': (
            'HideFlag22', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag23:1': (
            'HideFlag23', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag24:1': (
            'HideFlag24', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag25:1': (
            'HideFlag25', False, None,
            "Hide part of the character model: (arm)"),
        'invisibleFlag26:1': (
            'HideFlag26', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag27:1': (
            'HideFlag27', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag28:1': (
            'HideFlag28', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag29:1': (
            'HideFlag29', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag30:1': (
            'HideFlag30', False, None,
            "Hide part of the character model: (belt)"),
        'invisibleFlag31:1': (
            'HideFlag31', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag32:1': (
            'HideFlag32', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag33:1': (
            'HideFlag33', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag34:1': (
            'HideFlag34', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag35:1': (
            'HideFlag35', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag36:1': (
            'HideFlag36', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag37:1': (
            'HideFlag37', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag38:1': (
            'HideFlag38', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag39:1': (
            'HideFlag39', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag40:1': (
            'HideFlag40', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag41:1': (
            'HideFlag41', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag42:1': (
            'HideFlag42', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag43:1': (
            'HideFlag43', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag44:1': (
            'HideFlag44', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag45:1': (
            'HideFlag45', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag46:1': (
            'HideFlag46', False, None,
            "Hide part of the character model: (unknown)"),
        'invisibleFlag47:1': (
            'HideFlag47', False, None,
            "Hide part of the character model: (unknown)"),
        'disableMultiDropShare:1': (
            'DisableMultiplayerShare', False, None,
            "If True, this armor cannot be given to other players by dropping it. Always False in vanilla."),
        'simpleModelForDlc:1': (
            'SimpleDLCModelExists', False, None,
            "Unknown; always set to False."),
        'pad_0[1]': (
            'Pad0', False, None,
            "Null padding."),
        'oldSortId': (
            'OldSortIndex', False, None,
            "Sorting index for an obsolete build of the game. No effect."),
        'pad_1[6]': (
            'Pad1', False, None,
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
        'residentSpEffectId1': (  # TODO: Do these override the base Armor effects? Can't remember.
            'WearerSpecialEffect1', True, Params.SpecialEffects,
            "Special effect granted to wearer (first of three)."),
        'residentSpEffectId2': (
            'WearerSpecialEffect2', True, Params.SpecialEffects,
            "Special effect granted to wearer (second of three)."),
        'residentSpEffectId3': (
            'WearerSpecialEffect3', True, Params.SpecialEffects,
            "Special effect granted to wearer (third of three)."),
        'materialSetId': (
            'UpgradeMaterialID', True, '<Param:UpgradeMaterials>',
            "Upgrade material set for reinforcement."),  # TODO: I assume this overrides ID for base Armor.
    },
    'GAME_AREA_PARAM_ST': {
        'bonusSoul_single': (
            'SingleplayerSoulReward', True, None,
            "Souls awarded (after delay) when boss is defeated with no summons."),
        'bonusSoul_multi': (
            'MultiplayerSoulReward', True, None,
            "Souls awarded to each player (after delay) when boss is defeated with summons."),
        'humanityPointCountFlagIdTop': (
            'FirstHumanityFlag', True, None,
            "First flag for recording number of humanity drops awarded in boss's area."),
        'humanityDropPoint1': (
            'HumanityDropPoint1', True, None,
            "Number of 'points' needed from killing enemies in the boss area for first Humanity."),
        'humanityDropPoint2': (
            'HumanityDropPoint2', True, None,
            "Number of 'points' needed from killing enemies in the boss area for second Humanity."),
        'humanityDropPoint3': (
            'HumanityDropPoint3', True, None,
            "Number of 'points' needed from killing enemies in the boss area for third Humanity."),
        'humanityDropPoint4': (
            'HumanityDropPoint4', True, None,
            "Number of 'points' needed from killing enemies in the boss area for fourth Humanity."),
        'humanityDropPoint5': (
            'HumanityDropPoint5', True, None,
            "Number of 'points' needed from killing enemies in the boss area for fifth Humanity."),
        'humanityDropPoint6': (
            'HumanityDropPoint6', True, None,
            "Number of 'points' needed from killing enemies in the boss area for sixth Humanity."),
        'humanityDropPoint7': (
            'HumanityDropPoint7', True, None,
            "Number of 'points' needed from killing enemies in the boss area for seventh Humanity."),
        'humanityDropPoint8': (
            'HumanityDropPoint8', True, None,
            "Number of 'points' needed from killing enemies in the boss area for eighth Humanity."),
        'humanityDropPoint9': (
            'HumanityDropPoint9', True, None,
            "Number of 'points' needed from killing enemies in the boss area for ninth Humanity."),
        'humanityDropPoint10': (
            'HumanityDropPoint10', True, None,
            "Number of 'points' needed from killing enemies in the boss area for final Humanity."),
    },
    'BULLET_PARAM_ST': {
        'atkId_Bullet': (
            'BulletAttack', True, '<Params:Attacks>',  # TODO: Ambiguous attack parameter.
            "Attack parameters for bullet impact. Only certain fields in the attack parameter are used. "
            "Could be directed to either HumanAttacks table or NonHumanAttacks table, depending on "
            "the bullet's owner. Set to 0 if bullet has no attack data (no damage)."),
        'sfxId_Bullet': (
            'ProjectileFX', True, '<Params:VisualEffects>',
            "Visual effect ID for bullet projectile."),
        'sfxId_Hit': (
            'ImpactFX', True, '<Params:VisualEffects>',
            "Visual effect ID for bullet impact."),
        'sfxId_Flick': (
            'FlickFX', True, '<Params:VisualEffects>',
            "Visual effect ID for when bullet is blocked (I think). Used predominantly for arrows and "
            "throwing knives."),
        'life': (
            'LifeTime', True, None,
            "Maximum time before bullet will disappear on its own. -1 means it will last indefinitely."),
        'dist': (
            'AttenuationDistance', True, None,
            "Distance at which attenuation of the projectile begins."),
        'shootInterval': (
            'LaunchInterval', True, None,
            "Time between emitted bullets. Does nothing for bullets that only shoot once and is "
            "generally left at zero for those bullets."),
        'gravityInRange': (
            'GravityBeforeAttenuation', True, None,
            "Downward acceleration of bullet. Rarely used."),
        'gravityOutRange': (
            'GravityAfterAttenuation', True, None,
            "Downward acceleration of bullet after it passes the attenuation distance."),
        'hormingStopRange': (
            'ClosestHomingDistance', True, None,
            "Bullet will stop homing if it is within this distance of its homing target. Use this to "
            "prevent homing bullets from being too oppressive."),
        'initVellocity': (
            'InitialSpeed', True, None,
            "Initial speed of bullet."),
        'accelInRange': (
            'AccelerationBeforeAttenuation', True, None,
            "Forward acceleration acting on bullet before it reaches the attenuation distance. Negative "
            "values will slow the bullet down."),
        'accelOutRange': (
            'AccelerationAfterAttenuation', True, None,
            "Forward acceleration acting on bullet after it passes the attenuation distance. Negative "
            "values will slow the bullet down."),
        'maxVellocity': (
            'MaxSpeed', True, None,
            "Maximum speed of bullet, regardless of acceleration."),
        'minVellocity': (
            'MinSpeed', True, None,
            "Minimum speed of bullet, regardless of acceleration."),
        'accelTime': (
            'AccelerationTime', True, None,
            "Time that acceleration is active after bullet creation."),
        'homingBeginDist': (
            'HomingStartDistance', True, None,
            "Distance from owner at which the bullet starts homing in on targets."),
        'hitRadius': (
            'InitialHitRadius', True, None,
            "Initial hit radius of bullet projectile."),
        'hitRadiusMax': (
            'FinalHitRadius', True, None,
            "Final hit radius of bullet projectile. Set to -1 if radius does not change, which is always "
            "coupled with a value of 0 for RadiusIncreaseDuration."),
        'spreadTime': (
            'RadiusIncreaseTime', True, None,
            "Time taken by bullet to transition from initial to final hit radius. Value of 0 are always "
            "coupled with values of -1 for RadiusIncreaseDuration. I'm not sure if this can actually "
            "decrease the hit radius if the final value is less than the initial value."),
        'expDelay': (
            'ExpDelay', False, None,
            "Delay between impact and 'explosion' (not sure if that refers to the visual effect and/or "
            "hitbox). Never used (always zero)."),
        'hormingOffsetRange': (
            'HomingOffsetRange', True, None,
            "Internal description: 'When shooting, aim to shift each component of XYZ by this "
            "amount.' Nonzero only for Hydra blasts and Vagrant attacks."),
        'dmgHitRecordLifeTime': (
            'HitboxLifeTime', True, None,
            "Duration of bullet impact hitbox. A value of zero means it is disabled immediately "
            "after first impact."),
        'externalForce': (
            'ExternalForce', True, None,
            "Unknown. Used only for Gargoyle fire breath and Undead Dragon poison breath."),
        'spEffectIDForShooter': (
            'OwnerSpecialEffect', True, Params.SpecialEffects,
            "Special effect applied to owner when bullet is created. (Unclear if it is applied "
            "repeatedly by repeating bullets.)"),
        'autoSearchNPCThinkID': (
            'BulletAI', True, '<Params:AI>',
            "AI parameter ID for triggered floating bullets. Only used by Homing [Crystal] "
            "Soulmass (10000) and Pursuers (10001) in the vanilla game."),
        'HitBulletID': (
            'BulletOnHit', True, '<Params:Bullets>',
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
            'BulletCount', True, None,
            "Number of bullets emitted at once."),
        'homingAngle': (
            'HomingAnglePerSecond', True, None,
            "Turning angle of homing bullet per second. Higher values are better for homing."),
        'shootAngle': (
            'AzimuthAngleStart', True, None,
            "Angle of first bullet in degrees around the vertical axis, relative to the forward direction."),
        'shootAngleInterval': (
            'AzimuthAngleInterval', True, None,
            "Angle from one bullet to the next around the vertical axis, beginning at the azimuth "
            "angle start."),
        'shootAngleXInterval': (
            'ElevationAngleInterval', True, None,
            "Angle between bullets in elevation."),
        'damageDamp': (
            'PhysicalDamageDamp', True, None,
            "Percentage reduction in physical damage per second."),
        'spelDamageDamp': (
            'MagicDamageDamp', True, None,
            "Percentage reduction in magic damage per second."),
        'fireDamageDamp': (
            'FireDamageDamp', True, None,
            "Percentage reduction in fire damage per second."),
        'thunderDamageDamp': (
            'LightningDamageDamp', True, None,
            "Percentage reduction in lightning damage per second."),
        'staminaDamp': (
            'StaminaDamp', False, None,
            "Percentage reduction in stamina damage per second."),
        'knockbackDamp': (
            'KnockbackDamp', False, None,
            "Percentage reduction in knockback power per second."),
        'shootAngleXZ': (
            'FirstBulletElevationAngle', True, None,
            "Angle of elevation of first bullet. Positive values will angle the bullets up (e.g. "
            "Quelaag's fireballs) and negative values will angle the bullets down (e.g. most breath "
            "attacks)."),
        'lockShootLimitAng': (
            'LockShootLimitAngle', True, None,
            "Unknown, but likely important. Set to 30 for most basic projectile magic."),
        'isPenetrate': (
            'PiercesTargets', True, None,
            "Bullet will go through objects, players, and NPCs."),
        'prevVelocityDirRate': (
            'PreviousDirectionRatio', False, None,
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
            'MaterialAttackType', True, None,
            "DOC-TODO"),
        'Material_AttackMaterial': (
            'MaterialAttackMaterial', True, None,
            "DOC-TODO"),
        'Material_Size': (
            'MaterialSize', True, None,
            "DOC-TODO"),
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
            "Bullet hitbox is continuous (I think). Only used for corrosion cloud in vanilla."),
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
            'AttachEffectType', False, '<ParamEnum:BULLET_ATTACH_EFFECT_TYPE>',
            "Mostly 0, but sometimes 1 (Dragon Head breath, Grant AoE, Force miracles)."),
        'isHitForceMagic:1': (
            'CanBeDeflectedByMagic', True, None,
            "If True, this bullet will impact appropriate Force-type magic (e.g. arrows, bolts, knives)."),
        'isIgnoreSfxIfHitWater:1': (
            'IgnoreFXOnWaterHit', True, None,
            "If True, hit FX are not produced if the bullet impacts water."),
        'isIgnoreMoveStateIfHitWater:1': (
            'IgnoreStateTransitionOnWaterHit', True, None,
            "Unclear effect, but True for knives/arrows/bolts and False otherwise."),
        'isHitDarkForceMagic:1': (
            'CanBeDeflectedBySilverPendant', True, None,
            "If True, this bullet will impact the Silver Pendant shield effect. True only for dark sorceries."),
        'pad[3]': (
            'Pad3', False, None,
            "Null padding."),

    },
    'LOCK_CAM_PARAM_ST': {},
    'ATK_PARAM_ST': {},
    'BEHAVIOR_PARAM_ST': {
        'variationId': ('VariationID', True, int,  # TODO: connect to model/TAE somehow.
                        ""),
        'behaviorJudgeId': ('BehaviorJudgeID', True, int,
                            "This is the ID specified by TAE events that trigger behaviors."),
        'ezStateBehaviorType_old': ('EzstateBehaviorType', False, None,
                                    "Unused remnant from Demon's Souls."),
        'refType': ('ReferenceType', True, BEHAVIOR_REF_TYPE,
                    "Is the reference ID below an Attack or Bullet ID?"),
        'pad0[2]': ('Pad1', False, '<Pad:2>', "Null padding."),
        'refId': behavior_ref_id,  # TODO: wrap this whole dictionary in a class that calls this (with entry) if needed.
        'sfxVariationId': ('FXVariationID', True, int,
                           "Visual effect ID."),
        'stamina': ('StaminaCost', True, int,
                    "Stamina cost of behavior."),
        'mp': ('DurabilityCost', True, int,
               "Weapon/shield durability cost of behavior."),
        'category': ('Category', True, BEHAVIOR_CATEGORY,
                     "Determines compatibility with special effects that affect certain types of attacks."),
        'heroPoint': ('HumanityCost', True, int,
                      "Humanity cost of behavior."),  # TODO: ever used? does it even work?
        'pad1[2]': ('Pad2', False, '<Pad:2>', "Null padding."),
    },
    'CHARACTER_INIT_PARAM': {
        'baseRec_mp': ('BaseRecMP', False, int, "Unknown."),
        'baseRec_sp': ('BaseRecSP', False, int, "Unknown."),
        'red_Falldam': ('RedFallDamage', False, int, "Unknown."),
        'soul': ('SoulCount', True, int, "Starting soul count of character."),
        'equip_Wep_Right': ('RightHandWeapon1', True, Params.Weapons,
                            "First (default) weapon/shield equipped in right hand."),
        'equip_Subwep_Right': ('RightHandWeapon2', True, Params.Weapons,
                               "Second weapon/shield equipped in right hand."),
        'equip_Wep_Left': ('LeftHandWeapon1', True, Params.Weapons,
                           "First (default) weapon/shield equipped in left hand."),
        'equip_Subwep_Left': ('LeftHandWeapon2', True, Params.Weapons,
                              "Second weapon/shield equipped in left hand."),
        'equip_Helm': ('HeadArmor', True, Params.Armor, "Armor equipped to head."),
        'equip_Armer': ('BodyArmor', True, Params.Armor, "Armor equipped to body."),
        'equip_Gaunt': ('HandsArmor', True, Params.Armor, "Armor equipped to hands."),
        'equip_Leg': ('LegsArmor', True, Params.Armor, "Armor equipped to legs."),
        'equip_Arrow': ('ArrowSlot1', True, Params.Weapons, "Arrows equipped in slot 1."),  # TODO: Show arrows only?
        'equip_Bolt': ('BoltSlot1', True, Params.Weapons, "Bolts equipped in slot 1."),
        'equip_SubArrow': ('ArrowSlot2', True, Params.Weapons, "Arrows equipped in slot 2."),
        'equip_SubBolt': ('BoltSlot2', True, Params.Weapons, "Bolts equipped in slot 2."),
        'equip_Accessory01': ('RingSlot1', True, Params.Rings,
                              "First ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory02': ('RingSlot2', True, Params.Rings,
                              "Second ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory03': ('RingSlot3', True, Params.Rings,
                              "Third ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory04': ('RingSlot4', True, Params.Rings,
                              "Fourth ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Accessory05': ('RingSlot5', True, Params.Rings,
                              "Fifth ring equipped. Note that up to five rings can be equipped to human NPCs."),
        'equip_Skill_01': ('SkillSlot1', False, int, ""),  # TODO: unused?
        'equip_Skill_02': ('SkillSlot2', False, int, ""),
        'equip_Skill_03': ('SkillSlot3', False, int, ""),
        'equip_Spell_01': ('SpellSlot1', True, int, "First spell equipped."),  # TODO: points to Goods or Spells?
        'equip_Spell_02': ('SpellSlot2', True, int, "Second spell equipped."),
        'equip_Spell_03': ('SpellSlot3', True, int, "Third spell equipped."),
        'equip_Spell_04': ('SpellSlot4', True, int, "Fourth spell equipped."),
        'equip_Spell_05': ('SpellSlot5', True, int, "Fifth spell equipped."),
        'equip_Spell_06': ('SpellSlot6', True, int, "Sixth spell equipped."),
        'equip_Spell_07': ('SpellSlot7', True, int, "Seventh spell equipped."),
        'item_01': ('GoodSlot1', True, int, "Good (item) equipped in slot 1."),
        'item_02': ('GoodSlot2', True, int, "Good (item) equipped in slot 2."),
        'item_03': ('GoodSlot3', True, int, "Good (item) equipped in slot 3."),
        'item_04': ('GoodSlot4', True, int, "Good (item) equipped in slot 4."),
        'item_05': ('GoodSlot5', True, int, "Good (item) equipped in slot 5."),
        'item_06': ('GoodSlot6', True, int, "Good (item) equipped in slot 6."),
        'item_07': ('GoodSlot7', True, int, "Good (item) equipped in slot 7."),
        'item_08': ('GoodSlot8', True, int, "Good (item) equipped in slot 8."),
        'item_09': ('GoodSlot9', True, int, "Good (item) equipped in slot 9."),
        'item_10': ('GoodSlot10', True, int, "Good (item) equipped in slot 10."),
        'npcPlayerFaceGenId': ('FaceID', True, Params.Faces,
                               "Face parameter ID (NPCs only)."),
        'npcPlayerThinkId': ('Default AI', True, Params.AI,
                             "Default AI (NPCs only)."),
        'baseHp': ('BaseMaxHP', True, int, "Base amount of maximum HP (excluding effects of vitality)."),
        'baseMp': ('BaseMaxMP', False, int, "Base amount of maximum MP (unused in Dark Souls)."),
        'baseSp': ('BaseMaxStamina', True, int, "Base maximum stamina (excluding effects of endurance)."),
        'arrowNum': ('ArrowSlot1Count', True, int, "Count of arrows equipped in slot 1."),
        'boltNum': ('BoltSlot1Count', True, int, "Count of arrows equipped in slot 2."),
        'subArrowNum': ('ArrowSlot2Count', True, int, "Count of bolts equipped in slot 1."),
        'subBoltNum': ('BoltSlot2Count', True, int, "Count of bolts equipped in slot 2."),
        'QWC_sb': ('QWC_SB', False, int, "Unknown. Likely to be unused world tendency effect."),
        'QWC_mw': ('QWC_MW', False, int, "Unknown. Likely to be unused world tendency effect."),
        'QWC_cd': ('QWC_CD', False, int, "Unknown. Likely to be unused world tendency effect."),
        'soulLv': ('SoulLevel', True, int,
                   "Soul level, independent of actual stats. Determines amount of souls rewarded by human NPCs."),
        'baseVit': ('Vitality', True, int, "Base vitality level. Determines maximum health."),
        'baseWil': ('Attunement', True, int, "Base attunement level. Determines spell slots and casting speed."),
        'baseEnd': ('Endurance', True, int, "Base endurance level. Determines maximum stamina and equip load."),
        'baseStr': ('Strength', True, int, "Base strength level. Affects strength-based weapons and damage."),
        'baseDex': ('Dexterity', True, int, "Base dexterity level. Affects skill-based weapons and damage."),
        'baseMag': ('Intelligence', True, int, "Base intelligence level. Affects magic usability and effectiveness."),
        'baseFai': ('Faith', True, int, "Base faith level. Affects miracle usability and effectiveness."),
        'baseLuc': ('Luck', True, int, "Base luck level. Improves chances of rare item drops."),
        'baseHeroPoint': ('Humanity', True, int, "Base 'soft' humanity."),
        'baseDurability': ('Resistance', True, int, "Base resistance level. Improves resistances to status ailments."),
        'itemNum_01': ('GoodSlot1Count', True, int, "Count of good equipped in slot 1."),
        'itemNum_02': ('GoodSlot2Count', True, int, "Count of good equipped in slot 2."),
        'itemNum_03': ('GoodSlot3Count', True, int, "Count of good equipped in slot 3."),
        'itemNum_04': ('GoodSlot4Count', True, int, "Count of good equipped in slot 4."),
        'itemNum_05': ('GoodSlot5Count', True, int, "Count of good equipped in slot 5."),
        'itemNum_06': ('GoodSlot6Count', True, int, "Count of good equipped in slot 6."),
        'itemNum_07': ('GoodSlot7Count', True, int, "Count of good equipped in slot 7."),
        'itemNum_08': ('GoodSlot8Count', True, int, "Count of good equipped in slot 8."),
        'itemNum_09': ('GoodSlot9Count', True, int, "Count of good equipped in slot 9."),
        'itemNum_10': ('GoodSlot10Count', True, int, "Count of good equipped in slot 10."),
        'bodyScaleHead': ('HeadScale', True, int, "Multiplier applied to head size."),
        'bodyScaleBreast': ('ChestScale', True, int, "Multiplier applied to chest size."),
        'bodyScaleAbdomen': ('AbdomenScale', True, int, "Multiplier applied to abdomen size."),
        'bodyScaleArm': ('ArmScale', True, int, "Multiplier applied to arm size."),
        'bodyScaleLeg': ('LegScale', True, int, "Multiplier applied to leg size."),
        'gestureId0': ('Gesture1', True, int, "First equipped gesture."),
        'gestureId1': ('Gesture2', True, int, "Second equipped gesture."),
        'gestureId2': ('Gesture3', True, int, "Third equipped gesture."),
        'gestureId3': ('Gesture4', True, int, "Fourth equipped gesture."),
        'gestureId4': ('Gesture5', True, int, "Fifth equipped gesture."),
        'gestureId5': ('Gesture6', True, int, "Sixth equipped gesture."),
        'gestureId6': ('Gesture7', True, int, "Seventh equipped gesture."),
        'npcPlayerType': ('NPCType', True, NPC_TYPE, "Type of human NPC."),
        'npcPlayerDrawType': ('DrawType', True, NPC_DRAW_TYPE, "Draw type of human NPC."),
        'npcPlayerSex': ('Sex', True, CHARACTER_INIT_SEX, "Character sex."),
        'vowType:4': ('Covenant', True, CHRINIT_VOW_TYPE, "Character covenant."),
        'pad:4': ('Pad0', False, '<Pad:4>', "Null padding."),
        'pad0[10]': ('Pad1', False, '<Pad:10>', "Null padding."),
    },
    'TALK_PARAM_ST': {
        'msgId': (
            'SubtitleText', True, Text.Conversations,
            "Text ID for dialogue subtitle."),
        'voiceId': (
            'VoiceSound', True, '<Sound:Voice>',
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
    'FACE_PARAM_ST': {},
    'EQUIP_PARAM_GOODS_ST': {},
    'HIT_MTRL_PARAM_ST': {
        'aiVolumeRate': (
            'SoundRadiusMultiplier', True, float,
            "Multiplier for foot sound effect radius on this terrain."),
        'spEffectIdOnHit0': (
            'SpecialEffect1', True, None,
            "Special effect applied to character walking on terrain (first of two)."),
        'spEffectIdOnHit1': (
            'SpecialEffect2', True, None,
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
        'lotItemCategory01': (
            'Item1Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 1)."),
        'lotItemId01': partial(item_lot_item_id, 1),
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
            'Item1LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint01': (
            'Item1CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset01:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory02': (
            'Item2Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 2)."),
        'lotItemId02': partial(item_lot_item_id, 2),
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
            'Item2LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint02': (
            'Item2CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset02:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory03': (
            'Item3Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 3)."),
        'lotItemId03': partial(item_lot_item_id, 3),
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
            'Item3LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint03': (
            'Item3CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset03:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory04': (
            'Item4Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 4)."),
        'lotItemId04': partial(item_lot_item_id, 4),
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
            'Item4LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint04': (
            'Item4CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset04:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory05': (
            'Item5Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 5)."),
        'lotItemId05': partial(item_lot_item_id, 5),
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
            'Item5LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint05': (
            'Item5CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset05:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory06': (
            'Item6Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 6)."),
        'lotItemId06': partial(item_lot_item_id, 6),
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
            'Item6LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint06': (
            'Item6CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset06:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory07': (
            'Item7Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 7)."),
        'lotItemId07': partial(item_lot_item_id, 7),
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
            'Item7LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint07': (
            'Item7CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset07:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

        'lotItemCategory08': (
            'Item8Category', True, ITEMLOT_ITEMCATEGORY,
            "Type of item (slot 8)."),
        'lotItemId08': partial(item_lot_item_id, 8),
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
            'Item8LuckEnabled', True, None,
            "If True, increased player luck will *reduce* the chance points of this slot. Usually used on the empty "
            "item slot so that rarer items have a relatively better chance of dropping."),
        'cumulateLotPoint08': (
            'Item8CumulativePoints', True, None,
            "Points that will be cumulatively added to this slot's chance points every time the item lot is rolled. "
            "This "),
        'cumulateReset08:1': (
            'ResetCumulativePointsOnDrop', True, bool,
            "If True, all cumulative points in this slot will be reset when the slot is actually dropped."),

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
            'TurnVelocity', True, None,  # TODO: types from here on.
            "DOC-TODO"),
        'hitHeight': (
            'HitHeight', True, None,
            "DOC-TODO"),
        'hitRadius': (
            'HitRadius', True, None,
            "DOC-TODO"),
        'weight': (
            'Weight', True, None,
            "DOC-TODO"),
        'hitYOffset': (
            'HitYOffset', False, None,
            "DOC-TODO"),
        'hp': (
            'MaximumHP', True, None,
            "DOC-TODO"),
        'mp': (
            'MaximumMP', True, None,
            "DOC-TODO"),
        'getSoul': (
            'SoulReward', True, None,
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
            'HumanityLotID', True, int,  # TODO: flags?
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
            'SlashGuardCutRate', False, float,
            "Always zero."),
        'blowGuardCutRate': (
            'BlowGuardCutRate', False, float,
            "Always zero."),
        'thrustGuardCutRate': (
            'ThrustGuardCutRate', False, float,
            "Always zero."),
        'superArmorDurability': (
            'MaxPoise', True, int,
            "DOC-TODO"),
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
            'DefaultLightingParamID', False, '<Lighting:Lod>',
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
            'GuardLevel', False, int,  # TODO: possibly GUARDMOTION_CATEGORY
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
            'Pad1', False, None,
            "DOC-TODO"),
        'vowType:3': (
            'VowType', False, int,
            "Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone else."),
        'disableInitializeDead:1': (
            'DisableInitializeDead', False, bool,
            "True for bosses and non-respawning enemies that are disabled in event scripts, "
            "but its effects are unknown."),
        'pad3:4': (
            '__Pad3', False, None,
            "DOC-TODO"),
        'pad2[6]': (
            '__Pad2', False, None,
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
            'DisableMultiplayerShare', False, None,
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
            '', True, None, ""),
        'isAttackBacklash:1': (
            '', True, None, ""),
        'isDisableBreakForFirstAppear:1': (
            '', True, None, ""),
        'isLadder:1': (
            '', True, None, ""),
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
        'spQualifiedId': partial(obj_act_success_condition, 'spQualifiedId'),
        'spQualifiedId2': partial(obj_act_success_condition, 'spQualifiedId2'),
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
        'spQualifiedType': (
            'SuccessCondition1Type', True, OBJACT_SP_QUALIFIED_TYPE,
            "Type of first success condition."),
        'spQualifiedType2': (
            'SuccessCondition2Type', True, OBJACT_SP_QUALIFIED_TYPE,
            "Type of second success condition."),
        'validObjAngle': (
            'MaxObjectAngle', True, None,
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
        'equipId': shop_item_id,
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
            "potentially glitchy behavior (e.g. desynchronized grab animations and missed hitboxes)."),
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
            'ReplaceNoDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of NoDamage level."),
        'dmgLv_S': (
            'ReplaceSmallDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Small damage level."),
        'dmgLv_M': (
            'ReplaceMediumDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Medium damage level."),
        'dmgLv_L': (
            'ReplaceLargeDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Large damage level."),
        'dmgLv_BlowM': (
            'ReplaceBlowoffDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Blowoff damage level."),
        'dmgLv_Push': (
            'ReplacePushDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Push damage level."),
        'dmgLv_Strike': (
            'ReplaceStrikeDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Strike damage level."),
        'dmgLv_BlowS': (
            'ReplaceSmallBlowDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Blow damage level."),
        'dmgLv_Min': (
            'ReplaceMinimalDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Minimal damage level."),
        'dmgLv_Uppercut': (
            'ReplaceLaunchDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of Launch damage level."),
        'dmgLv_BlowLL': (
            'ReplaceBlowBackwardDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of BlowBackward damage level."),
        'dmgLv_Breath': (
            'ReplaceBreathBurnDamageLevel', True, ATKPARAM_REP_DMGTYPE,
            "Damage level that will occur instead of BreathBurn damage level."),
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
            'CanAffectHumans', True, bool,
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
            'UseMagicCorrection', True, bool,
            "If True, correction will be applied to magic (or intelligence?). Not sure what this does."),
        'bAdjustFaithAblity:1': (
            'UseFaithCorrection', True, bool,
            "If True, correction will be applied to faith (or miracles?). Not sure what this does."),
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
    'MAGIC_PARAM_ST': {},
    'THROW_INFO_BANK': {},
    'EQUIP_MTRL_SET_PARAM_ST': {},
    'EQUIP_PARAM_WEAPON_ST': {},
    'REINFORCE_PARAM_WEAPON_ST': {},
    'MOVE_PARAM_ST': {},
}
