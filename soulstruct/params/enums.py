"""Enums used in Dark Souls game parameters.

I have kept all of the original names of these for simplicity (typos and all). They are only referenced internally
anyway. Arranged alphabetically.
"""
from enum import IntEnum


# TODO: Use appropriate enum types.

class Int8Enum(IntEnum):
    @property
    def field_size(self):
        return 8


class Int16Enum(IntEnum):
    @property
    def field_size(self):
        return 16


class Int32Enum(IntEnum):
    @property
    def field_size(self):
        return 32


class ACCESSORY_CATEGORY(IntEnum):
    pass


class ACTION_PATTERN(IntEnum):
    pass


class ATK_PARAM_BOOL(IntEnum):
    pass


class ATK_PARAM_HIT_SOURCE(IntEnum):
    pass


class ATK_PARAM_HIT_TYPE(IntEnum):
    pass


class ATK_PARAM_MAP_HIT(IntEnum):
    pass


class ATK_PARAM_PARTSDMGTYPE(IntEnum):
    pass


class ATK_PATAM_THROWFLAG_TYPE(IntEnum):  # (sic)
    pass


class ATK_SIZE(IntEnum):
    pass


class ATK_TYPE(IntEnum):
    pass


class ATKPARAM_ATKATTR_TYPE(IntEnum):
    NoType = 0  # test only
    Blast = 1  # e.g. Iron Golem axe air blast
    Sharp = 3  # e.g. arrows and throwing knives
    Other = 4  # e.g. most bullets


class ATKPARAM_REP_DMGTYPE(IntEnum):
    pass


class ATKPARAM_SPATTR_TYPE(IntEnum):
    NoType = 0
    Physical = 1
    Fire = 2
    Magic = 3
    Poison = 4
    # 5 is not used.
    Lightning = 6
    # 7 is not used.
    Crystal = 8


class BEHAVIOR_ATK_SIZE(IntEnum):
    pass


class BEHAVIOR_ATK_TYPE(IntEnum):
    pass


class BEHAVIOR_CATEGORY(IntEnum):
    pass


class BEHAVIOR_REF_TYPE(IntEnum):
    Attack = 0
    Bullet = 1
    # TODO: Possibly a 2 somewhere? Throw?


class BULLET_ATTACH_EFFECT_TYPE(IntEnum):
    NoAttach = 0
    Attach = 1  # e.g. Grant special attack, Dragon Head Stone breath
    # No more observed.


class BULLET_EMITTE_POS_TYPE(IntEnum):
    pass


class BULLET_FOLLOW_TYPE(IntEnum):
    # TODO: Guess.
    DoNotFollow = 0
    Follow = 1


class BULLET_LAUNCH_CONDITION_TYPE(IntEnum):
    pass


class CHARACTER_INIT_SEX(IntEnum):
    Male = 0
    Female = 1


class CHRINIT_VOW_TYPE(IntEnum):
    NoCovenant = 0
    WayOfWhite = 1
    PrincessGuard = 2
    WarriorOfSunlight = 3
    Darkwraith = 4
    PathOfTheDragon = 5
    GravelordServant = 6
    ForestHunter = 7
    DarkmoonBlade = 8
    ChaosServant = 9


class ChrType(IntEnum):
    # TODO: Did I create this one?
    pass


class DURABILITY_DIVERGENCE_CATEGORY(IntEnum):
    pass


class ENEMY_BEHAVIOR_ID(IntEnum):
    pass


class EQUIP_BOOL(IntEnum):
    pass


class EQUIP_MODEL_CATEGORY(IntEnum):
    Hands = 1
    Torso = 2
    # 3 is missing.
    Bare = 4
    Head = 5
    Legs = 6
    pass


class EQUIP_MODEL_GENDER(IntEnum):
    NoGender = 0  # guess
    Male = 1
    Female = 2
    Detected = 3  # guess


class FACE_PARAM_HAIRCOLOR_TYPE(IntEnum):
    pass


class FACE_PARAM_HAIRSTYLE_TYPE(IntEnum):
    pass


class GOODS_CATEGORY(IntEnum):
    pass


class GOODS_OPEN_MENU(IntEnum):
    pass


class GOODS_TYPE(IntEnum):
    pass


class GOODS_USE_ANIM(IntEnum):
    pass


class GUARDMOTION_CATEGORY(IntEnum):
    pass


class HMP_FOOT_EFFECT_HEIGHT_TYPE(IntEnum):
    pass


class HMP_FOOT_EFFECT_DIR_TYPE(IntEnum):
    pass


class HMP_FLOOR_HEIGHT_TYPE(IntEnum):
    pass


class ITEMLOT_CUMULATE_RESET(IntEnum):
    pass


class ITEMLOT_ENABLE_LUCK(IntEnum):
    pass


class ITEMLOT_ITEMCATEGORY(IntEnum):
    pass


class MAGIC_BOOL(IntEnum):
    pass


class MAGIC_CATEGORY(IntEnum):
    pass


class MAGIC_MOTION_TYPE(IntEnum):
    pass


class NPC_BOOL(IntEnum):
    pass


class NPC_BURN_TYPE(IntEnum):
    pass


class NPC_DRAW_TYPE(IntEnum):
    pass


class NPC_HITSTOP_TYPE(IntEnum):
    """Guesses only."""
    Normal = 0
    Tough = 1
    Boss = 2
    # No other values observed.


class NPC_ITEMDROP_TYPE(IntEnum):
    pass


class NPC_MOVE_TYPE(IntEnum):
    pass


class NPC_SFX_SIZE(IntEnum):
    Normal = 0
    Large = 1
    VeryLarge = 2
    # No other values observed.

class NPC_TEMA_TYPE(IntEnum):
    pass  # (sic)


class NPC_THINK_GOAL_ACTION(IntEnum):
    # 0
    # 1
    # 2
    # 3
    LogicScript = 4


class NPC_THINK_REPLY_BEHAVIOR_TYPE(IntEnum):
    """Used to indicate whether NPCs respond to calls for help."""
    Ignore = 0
    Answer = 1
    # No other values observed.


class NPC_TYPE(IntEnum):
    Enemy = 0
    Boss = 1
    Ally = 2
    # No other values observed.


class OBJACT_SP_QUALIFIED_TYPE(IntEnum):
    pass


class OBJACT_CHR_SORB_TYPE(IntEnum):
    pass


class OBJACT_EVENT_KICK_TIMING(IntEnum):
    pass


class ON_OFF(IntEnum):
    # TODO: Confirm my obvious guess.
    Off = 0
    On = 1


class PROTECTOR_CATEGORY(IntEnum):
    Helm = 0
    Body = 1
    Hands = 2
    Legs = 3


class RAGDOLL_PARAM_BOOL(IntEnum):
    pass


class REPLACE_CATEGORY(IntEnum):
    pass


class SHOP_LINEUP_SHOPTYPE(IntEnum):
    pass


class SHOP_LINEUP_EQUIPTYPE(IntEnum):
    pass


class SKELETON_PARAM_KNEE_AXIS_DIR(IntEnum):
    pass


class SP_EFE_WEP_CHANGE_PARAM(IntEnum):
    pass


class SP_EFFECT_BOOL(IntEnum):
    pass


class SP_EFFECT_MOVE_TYPE(IntEnum):
    pass


class SP_EFFECT_SAVE_CATEGORY(IntEnum):
    pass


class SP_EFFECT_SPCATEGORY(IntEnum):
    pass


class SP_EFFECT_THROW_CONDITION_TYPE(IntEnum):
    pass


class SP_EFFECT_TYPE(IntEnum):
    pass


class SP_EFFECT_USELIMIT_CATEGORY(IntEnum):
    pass


class SP_EFFECT_VFX_EFFECT_TYPE(IntEnum):
    pass


class SP_EFFECT_VFX_PLAYCATEGORY(IntEnum):
    pass


class SP_EFFECT_VFX_SOUL_PARAM_TYPE(IntEnum):
    pass


class THROW_DMY_CHR_DIR_TYPE(IntEnum):
    pass


class THROW_ENABLE_STATE(IntEnum):
    pass


class THROW_PAD_TYPE(IntEnum):
    pass


class THROW_TYPE(IntEnum):
    pass


class WEAPON_CATEGORY(IntEnum):
    pass


class WEP_MATERIAL_ATK(IntEnum):
    pass


class WEP_MATERIAL_DEF(IntEnum):
    pass


class WEP_MATERIAL_DEF_SFX(IntEnum):
    pass


class WEP_CORRECT_TYPE(IntEnum):
    pass


class WEPMOTION_CATEGORY(IntEnum):
    pass


class WEP_BASE_CHANGE_CATEGORY(IntEnum):
    pass
