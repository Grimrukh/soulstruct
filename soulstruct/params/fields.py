from .enums import *

__all__ = ['GAME_PARAM_INFO']

class AI:
    Logic = '<AI:Logic>'
    Battle = '<AI:Battle>'
    
    
Animation = '<Animation>'
Model = '<Model>'

class Params:
    Armor = '<Params:Armor>'
    Bosses = '<Params:Bosses>'
    Bullets = '<Params:Bullets>'
    Cameras = '<Params:Cameras>'
    ItemLots = '<Params:ItemLots>'
    Knockback = '<Params:Knockback>'
    SpecialEffects = '<Params:SpecialEffects>'
    
    
class Text:
    Conversations = '<Text:Conversations>'


GAME_PARAM_INFO = {

    # Structure is:
    # { ParamTableName: ( ParamTableAttributeName, {
    #       ParamEntryName: ( ParamEntryNickname, VisibleDefault, ParamTableType, Docstring )
    # } ) }

    'NpcThinkParam': (
        'AI', {
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
        }),
    'EquipParamProtector': (
        'Armor', {
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
                'RepairCost', True, None,
                "Amount of souls required to repair weapon fully. Actual repair cost is this multiplied by current "
                "durability over max durability."),
            'basicPrice': (
                'BasicCost', False, None,
                "Unsure when this is used. Possibly sets the default if the cost is not specified in Shop parameters. "
                "Always set to 200."),
            'sellValue': (
                'FramptSellValue', True, None,
                "Amount of souls received when fed to Frampt."),
            'weight': (
                'Weight', True, None,
                "Weight of armor."),
            'residentSpEffectId': (
                'WearerSpecialEffect1', True, Params.SpecialEffects,
                "Special effect granted to wearer (first of three)."),
            'residentSpEffectId2': (
                '', True, Params.SpecialEffects,
                "Special effect granted to wearer (second of three)."),
            'residentSpEffectId3': (
                '', True, Params.SpecialEffects,
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
                'AchievementID', True, None,
                "DOC-TODO"),
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
                'EquipmentModelCategory', True, '<ParamEnum:EQUIP_MODEL_CATEGORY>',
                "DOC-TODO"),
            'equipModelGender': (
                '', True, '<ParamEnum:EQUIP_MODEL_GENDER>',
                "DOC-TODO"),
            'protectorCategory': (
                'ArmorType', True, '<ParamEnum:PROTECTOR_CATEGORY>',
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
        }),
    'ReinforceParamProtector': (
        'ArmorUpgrades', {
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
        }),
    'GameAreaParam': (
        'Bosses', {
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
        }),
    'Bullet': (
        'Bullets', {
            'atkId_Bullet': (
                'BulletAttack', True, '<Params:Attacks>',  # TODO: Ambiguous attack parameter.
                "Attack parameters for bullet impact. Only certain fields in the attack parameter are used. "
                "Could be directed to either CharacterAttacks table or CreatureAttacks table, depending on "
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
                'AttackAttribute', True, '<Enum:AttackAttribute>',
                "Attack type. Almost always 4 ('other'), but sometimes 3 (knives/arrows/bolts)."),
            'spAttribute': (
                'ElementAttribute', True, '<Enum:SpecialAttribute>',
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
                'LaunchConditionType', True, '<ParamEnum:BULLET_LAUNCH_CONDITION_TYPE>',
                "Condition for determing if a new bullet will be generated when this bullet lands or expires."),
            'FollowType:3': (
                'FollowType', True, '<ParamEnum:BULLET_FOLLOW_TYPE>',
                "Follow type."),
            'EmittePosType:3': (
                'OriginType', True, '<ParamEnum:BULLET_EMITTE_POS_TYPE>',
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

        }),
    'LockCamParam': (
        'Cameras', {}),
    'AtkParam_Pc': (
        'CharacterAttacks', {}),
    'BehaviorParam_PC': (
        'CharacterBehaviors', {}),
    'CharaInitParam': (
        'CharacterSheets', {}),
    'TalkParam': (
        'Dialogue', {
            'msgId': (
                'SubtitleText', True, Text.Conversations,
                "Text ID for dialogue subtitle."),
            'voiceId': (
                'VoiceSound', True, '<Sound:Voice>',
                "Sound ID (voice) for dialogue."),
            'motionId': (
            ),  # TODO
            'returnPos': (
            ),  # TODO
            'reactionId': (
            ),  # TODO
            'eventId': (
            ),  # TODO
            'isMotionLoop': (
                'IsMotionLoop', True, bool,
                "DOC-TODO"),
            'pad0[7]': (
                'Pad', False, None,
                "Null padding."),
        }),
    'FaceGenParam': (
        'Faces', {}),
    'EquipParamGoods': (
        'Goods', {}),
    'HitMtrlParam': (
        'Terrains', {}),
    'ItemLotParam': (
        'ItemLots', {}),
    'MenuColorTableParam': (
        'MenuColors', {}),
    'AtkParam_Npc': (
        'CreatureAttacks', {}),
    'BehaviorParam': (
        'CreatureBehaviors', {}),
    'NpcParam': (
        'NPCs', {
            'behaviorVariationId': (
                'BehaviorVariationID', True, None,
                "DOC-TODO"),
            'aiThinkId': (
                'AiThinkID', True, '<Param:AI>',
                "DOC-TODO"),
            'nameId': (
                'NameID', True, '<Text:NPCNames>',
                "DOC-TODO"),
            'turnVellocity': (
                'TurnVelocity', True, None,
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
        }),
    # 'RagdollParam': ('Ragdolls', {}),
    'EquipParamAccessory': (
        'Rings', {}),
    'ObjectParam': (
        'Objects', {}),
    'ObjActParam': (
        'ObjectActivations', {}),
    'ShopLineupParam': (
        'Shops', {}),
    # 'SkeletonParam': ('Skeletons', {}),
    'SpEffectParam': (
        'SpecialEffects', {}),
    'Magic': (
        'Spells', {}),
    'ThrowParam': (
        'Throws', {}),
    'EquipMtrlSetParam': (
        'UpgradeMaterials', {}),
    'EquipParamWeapon': (
        'Weapons', {}),
    'ReinforceParamWeapon': (
        'WeaponUpgrades', {}),
}
