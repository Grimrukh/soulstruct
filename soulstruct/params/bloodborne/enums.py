"""Enums used in Bloodborne game parameters.

I have kept all of the original names of these for simplicity (typos and all). They are only referenced internally
anyway. Ordered alphabetically.
"""
from soulstruct.params.field_types import *


class ACCESSORY_CATEGORY(UnsignedChar):
    """Always zero. Internal description says 'decoration' or 'armor' category."""

    Default = 0


class ACTION_BUTTON_REGION_TYPE(UnsignedChar):
    """Type of region in which action button prompt appears."""

    SphereWedge = 0  # defined by `radius` and `angle`
    Box = 1  # defined by `depth`, `width`, and `height`


class ACTION_BUTTON_ANGLE_CHECK_TYPE(UnsignedChar):
    """TODO"""


class ACTION_BUTTON_TEXT_BOX_TYPE(UnsignedChar):
    """TODO"""


class ACTION_BUTTON_EXEC_CIRCLE(UnsignedChar):
    """TODO"""


class ACTION_PATTERN(UnsignedChar):
    """Only used in the junk param table AI_STANDARD_INFO_BANK."""


class AI_SOUND_RATE_TYPE(UnsignedChar):
    """TODO"""


class AI_SOUND_FAKE_TARGET_TYPE(UnsignedChar):
    """TODO"""


class ATK_PARAM_HIT_SOURCE(UnsignedChar):
    """Almost always zero. Internal description says 'model point ID used to initiate the attack'."""

    Default = 0
    BodyOrParryOrRiposte = 1


class ATK_PARAM_HIT_TYPE(UnsignedChar):
    """Almost always zero. Applied to each collision of an attack."""

    Default = 0
    # 1 is unused.
    WhipAttack = 2


class ATK_PARAM_MAP_HIT(UnsignedChar):
    """Type of contact attack has with the map. Names are just based on the attacks that tend to use them."""

    Normal = 0  # deflected by map
    Projectile = 1  # arrows, bolts, knives, pyromancy
    Hazard = 2  # fire, boulders, pendulums, lava


class ATK_PARAM_PARTSDMGTYPE(UnsignedChar):
    """Always zero."""

    Default = 0


class ATK_PATAM_THROWFLAG_TYPE(UnsignedChar):  # (sic)
    NoThrow = 0
    ThrowTrigger = 1
    ThrowDamage = 2


class ATK_SIZE(UnsignedChar):
    """Always zero. Used to specify 'material size' of Bullets 'for SFX/SE'."""

    Default = 0


class ATK_TYPE(UnsignedChar):
    """Material attack type for Bullets, to determine sound effects, I believe."""

    Slash = 0
    Strike = 1
    Thrust = 2


class ATKPARAM_ATKATTR_TYPE(UnsignedChar):
    """High correlation with BEHAVIOR_ATK_TYPE below, which seems to specify physical damage type more reliably."""

    NoDamage = 0  # some Attacks are guarding actions
    Slash = 1
    Strike = 2
    Thrust = 3
    Neutral = 4  # most common


# TODO: Make sure the 'damage level' field in Attacks points to this type as well.
class ATKPARAM_REP_DMGTYPE(SignedChar):
    """Damage types. This enum is used by Special Effects to override one damage type with another (e.g. Iron Flesh
    reduces the weaker half 1 and the stronger half to 5)."""

    Null = 0  # means no replacement in Special Effect params
    Small = 1
    Medium = 2
    Large = 3
    Blowoff = 4
    Push = 5
    Strike = 6
    SmallBlow = 7
    Minimal = 8
    Launch = 9
    BlowBackward = 10
    BreathBurn = 11


class ATKPARAM_SFX_SE_ATK_DIR(SignedChar):
    """TODO"""


class ATKPARAM_SFX_SE_ATK_POW(SignedChar):
    """TODO"""


class ATKPARAM_SPATTR_TYPE(UnsignedChar):
    """Determines weaknesses and visual effect upon damage."""

    NoType = 0
    Physical = 1  # used for parries, ripostes, guarding, falls, Force miracles
    Fire = 2
    Magic = 3
    Poison = 4
    # 5 is not used.
    Lightning = 6
    StoneCurse = 7  # e.g. Basilisk breath
    CrystalCurse = 8  # e.g. Seath's crystal attacks
    Default = 255  # most basic physical attacks


class BEHAVIOR_ATK_SIZE(UnsignedChar):
    """Always zero. Used to specify 'material size' of Attacks 'for SFX/SE'."""

    Default = 0


class BEHAVIOR_ATK_TYPE(UnsignedChar):
    """Determines sound/visual effects of behaviors. Same as ATK_TYPE. Seems unused, though."""

    Slash = 0
    Strike = 1
    Thrust = 2


class BEHAVIOR_CATEGORY(UnsignedChar):
    """Determines which special effects buffs/debuffs will affect the behavior."""

    NoCategory = 0
    HumanRightHand = 1  # includes two-handed
    HumanLeftHand = 2
    Magic = 3  # includes miracles and pyromancy
    # 4 is missing.
    Basic = 5  # includes rolls, ladder bonks, thrown goods, close-range shield behaviors (?) ...
    NonPlayerRightHand = 6
    NonPlayerLeftHand = 7
    # 8 is missing.
    Riposte = 9


class BEHAVIOR_REF_TYPE(UnsignedChar):
    """Also used by Goods, where 'Default' (0) does NOT mean Attack."""

    Default = 0  # Attack for behaviors, None for goods
    Bullet = 1
    SpecialEffect = 2


class BULLET_LAUNCH_CONDITION_TYPE(UnsignedChar):
    """Determines if child bullet should be generated when it lands and/or dies. Names are based solely on usage right
    now. I suspect that 1 and 2 generate bullets on expiry, and -1 (255) and -2 (254) generate bullets on hit."""

    NoChild = 0
    LightningLastBullet = 1  # used by lightning 'great great grandchild' bullets
    LightningParentBullet = 2  # used by all other lightning bullets
    PrismStoneChild = 254  # -2; used by the second of three Prism Stone bullets
    ChainBullet = 255  # -1; used for non-lightning chain bullets


class CHARACTER_INIT_SEX(UnsignedChar):
    Female = 0
    Male = 1


class CHARMAKEMENU_CMD_TYPE(SignedInt):
    """TODO"""


class CHARMAKEMENU_VIEW_CONDITION(SignedInt):
    """TODO"""


class CHARMAKEMENU_PREVIEW_MODE(SignedChar):
    """TODO"""


class ChrType(SignedInt):
    """This is a real enum used in the junk param table ENEMY_STANDARD_INFO_BANK."""


class DURABILITY_DIVERGENCE_CATEGORY(UnsignedChar):
    """Interal description says 'do you branch by durability? Magic weapon support: motion branch by durability'.
    Probably related to weapons that consume durability for attacks - possibly determines what alternate animation
    they use if the weapon doesn't have enough durability for the special attack."""

    NoDivergence = 0
    DragonslayerSpearGolemAxe = 1  # 20 durability? 30 durability?
    TridentGrantDrakeSword = 3  # 80 durability? 200 durability?
    MoonlightGreatsword = 4
    CrystalRingShield = 7


class ENEMY_BEHAVIOR_ID(SignedInt):
    """From junk param table ENEMY_STANDARD_INFO_BANK."""


class EQUIP_MODEL_CATEGORY(UnsignedChar):
    Hands = 1
    Torso = 2
    # 3 is missing.
    Bare = 4
    Head = 5
    Legs = 6
    Weapon = 7


class EQUIP_MODEL_GENDER(UnsignedChar):
    NoGender = 0  # identical model
    Male = 1
    Female = 2
    Player = 3  # auto-detected (guess)


class FACE_PARAM(SignedChar):
    """TODO: Probably just a FaceParam entry ID?"""


class GEM_SEGMENT_MASK(UnsignedChar):
    """TODO"""


class GEM_SLOT_TYPE_MASK(UnsignedInt):
    """TODO"""


class GEM_SLOT_TYPE_NO(UnsignedChar):
    """TODO"""


class GEMEFFECT_GEN_PT(UnsignedInt):
    """TODO"""


class GOODS_CATEGORY(UnsignedChar):
    """Always zero."""

    Default = 0


class GOODS_OPEN_MENU(UnsignedChar):
    """Menu or dialog activated when good is used."""

    NoMenu = 0
    YesOrNoDialog = 1
    # 2 is unused.
    # 3 is unused.
    BlackSeparationCrystalMenu = 4
    # 5 is unused.
    OrangeSoapstoneMenu = 6
    BookOfTheGuiltyMenu = 7
    ServantRosterMenu = 8


class GOODS_TYPE(UnsignedChar):
    Basic = 0  # Consumables, orbs, soapstones, etc. (first inventory tab)
    KeyItem = 1
    Titanite = 2
    # 3 is unused.
    # UnusedHumanity = 4  # unused good ID 350, "Humanity"
    Spell = 5


class GOODS_USE_ANIM(UnsignedChar):
    """This only determines the basic animation; the exact sounds and visual effects are determined by the 'effect
    variation ID'."""

    NoAnimation = 0  # generally means cannot be used
    ApplyToWeapon = 1  # Resins
    Throw = 2  # Throwing Knife, Dung Pie, Alluring Skull
    Lob = 3  # Firebomb, Lloyd's Talisman
    HoldToEyes = 4  # Binoculars
    Sprinkle = 5  # Repair Powder
    KneelAndBow = 6  # Darksign, Homeward Bone,
    TossOnGround = 7  # Carvings
    WriteOnGround = 8  # Orange Guidance Soapstone, Book of the Guilty
    CrushInHand = 9  # Soul consumables
    Drink = 10
    DragonHeadStone = 11
    DragonTorsoStone = 12
    BlackSeparationCrystal = 13
    SilverPendant = 14
    PurpleCowardsCrystal = 15
    DrinkEmpty = 254  # -2


class GUARDMOTION_CATEGORY(UnsignedChar):
    """Type of guard animation."""

    MediumShield = 0  # also arrows and bolts, so probably means 'default'
    Greatshield = 1
    SmallShieldOrWeapon = 2
    GiantSkeletonGuard = 3  # I thought this might be 'two-handed weapon guard', but normal Skeletons do that as well.
    NonPlayerGuard = 4


class ITEMLOT_ITEMCATEGORY(SignedInt):
    """Inexplicably wide/reversed bit field for simply specifying the item type."""

    NoItem = -1
    Weapon = 0
    Armor = 2 ** 28  # 268435456
    Ring = 2 ** 29  # 536870912
    Good = 2 ** 30  # 1073741824


class ITEMLOT_LVDEP_ITEMCATEGORY(SignedInt):
    """TODO: Probably the same as ITEMLOT_ITEMCATEGORY."""


class MAGIC_CATEGORY(UnsignedChar):
    """Also called 'EzState Behavior Type'."""

    Sorcery = 0
    Miracle = 1
    Pyromancy = 2


class MAGIC_MOTION_TYPE(UnsignedChar):
    """Determines the base animation used when casting a spell."""

    SorceryFastProjectile = 0  # Soul Arrow (not Heavy), Soul Spear, Dark Bead
    SorceryWeapon = 1  # Magic Weapon, Hidden Weapon
    SorceryOtherBuff = 2  # Fall Control, Repair Weapon
    MiracleOtherBuff = 3  # Tranquil Walk of Peace, Heal, Homeward
    MiracleRegen = 4  # Soothing Sunlight, Bountiful Sunlight
    PyromancyProjectile = 5
    PyromancyAffectingBody = 6  # Iron Flesh, Flash Sweat, Power Within
    # 7 is unused.
    PyromancyCloseRane = 8  # Combustion, Black Flame
    PyromancyMist = 9  # Poison Mist, Acid Mist
    PyromancyStorm = 10  # Firestorm, Chaos Firestorm
    PyromancyRapport = 11
    ForceWrath = 12  # Force, Wrath of the Gods
    Chameleon = 13
    # 14 is unused.
    Blade = 15  # Sunlight Blade, Darkmoon Blade
    GravelordDance = 16
    MagicShield = 17
    EmitForce = 18
    LightningSpear = 19  # Lightning Spear, Great Lightning Spear, Sunlight Spear
    CastLight = 20
    HeavySoulArrow = 22
    FireSurge = 23
    FireWhip = 24


class MENU_PROPERTY_CMP_TYPE(SignedChar):
    """TODO"""


class MENU_PROPERTY_FORMAT_TYPE(UnsignedChar):
    """TODO"""


class MENU_PROPERTY_ID(SignedInt):
    """TODO"""


class MENU_VALUE_TABLE_CMP_TYPE(SignedChar):
    """TODO"""


class NPC_BURN_TYPE(UnsignedChar):
    """Type of sound effect played during combustion, I believe. Only the Undead Dragon and Mass of Souls use value 1,
    hence the name."""

    Normal = 0
    MassiveUndead = 1


class NPC_DRAW_TYPE(UnsignedChar):
    Normal = 0
    WhitePhantom = 1
    RedPhantom = 2
    Hollow = 4


class NPC_HITSTOP_TYPE(UnsignedChar):
    """Guesses only."""

    Normal = 0
    Tough = 1
    Boss = 2


class NPC_ITEMDROP_TYPE(UnsignedShort):
    """Determines appearance of dropped item from NPC."""

    GlowingCorpse = 0
    ItemEffect = 1


class NPC_MOVE_TYPE(UnsignedChar):
    NoMovement = 0  # e.g. tails
    Giant = 1  # e.g. Hydra, Living Tree
    Insects = 2  # e.g. Rockworms, Chaos Bugs
    Normal = 3
    FourLegged = 4  # e.g. Rats, Basilisks, Dogs, Tree Lizards
    FlyingDrake = 5
    Flying = 6
    # 7 unused.
    # 8 unused.
    BoundingDemon = 9


class NPC_SFX_SIZE(UnsignedChar):
    Normal = 0
    Large = 1
    VeryLarge = 2
    # No other values observed.


class NPC_TEAM_TYPE(UnsignedChar):  # "TEMA" typo fixed from older games
    """Unsure how this differs from the standard TeamType event enum."""

    Enemy = 0
    Boss = 1  # can hurt Enemy team
    Ally = 2
    UnusedUndeadDragon = 6
    Summon = 7
    UnusedSkeletonTest = 9


class NPC_THINK_ACTTYPE_ON_FAILEDPATH(UnsignedChar):
    """TODO"""


class NPC_THINK_CHANGE_STATE_ACTION(UnsignedChar):
    """TODO"""


class NPC_THINK_GOAL_ACTION(UnsignedChar):
    # TODO
    # 0
    # 1
    # 2
    # 3
    LogicScript = 4


class NPC_THINK_REPLY_BEHAVIOR_TYPE(UnsignedChar):
    """Used to indicate whether NPCs respond to calls for help."""

    Ignore = 0
    Answer = 1


class NPC_TYPE(UnsignedChar):
    """Internal description: 'if the enemies/boss enemies are distinguished OK'. Just guessing at names."""

    Normal = 0
    Boss = 1
    NonPlayerAlly = 2


class OBJACT_SP_QUALIFIED_TYPE(UnsignedChar):
    NoCondition = 0
    HasGood = 1
    HasSpecialEffect = 2


class OBJACT_CHR_SORB_TYPE(UnsignedChar):
    """Method of snapping character to object when object is activated. Only occurrence of 1 is for opening chests."""

    Normal = 0
    OpenChest = 1


class OBJACT_EVENT_KICK_TIMING(UnsignedChar):
    """Guessing at these, based on the fact that actions that trigger cutscenes seem to use a value of 0."""

    EndOfAction = 0
    StartOfAction = 1


class OBJECT_NAVIMESH_FLAG(UnsignedChar):
    """TODO"""


class ON_OFF(UnsignedChar):
    Off = 0
    On = 1


class PHYS_ATK_MENU_DISP_TYPE(UnsignedChar):
    """TODO"""


class PROTECTOR_CATEGORY(UnsignedChar):
    Helm = 0
    Body = 1
    Hands = 2
    Legs = 3
    Hair = 4


class RAGDOLL_PARAM_BOOL(UnsignedChar):
    """Boolean used in RAGDOLL_PARAM_ST, which I have hidden."""

    Off = 0
    On = 1


class REPLACE_CATEGORY(UnsignedChar):
    """I believe that goods/spells that have non-zero values here will replace the effects of previous goods/spells
    used that have the same value. Names are based on vanilla usage, but presumably these are open slots."""

    NoReplacement = 0
    # 1 is unused.
    HealingMiracle = 2
    DarkmoonSorcery = 3
    GravelordMiracle = 4
    DragonStones = 5


class RETURN_POINT_TYPE_YES_NO(UnsignedChar):
    """TODO"""


class SHOP_LINEUP_SHOPTYPE(UnsignedChar):
    Normal = 0
    # 1 is unused.
    AttunementMenu = 2


class SHOP_LINEUP_EQUIPTYPE(UnsignedChar):
    Weapon = 0
    Armor = 1
    Ring = 2
    Good = 3
    Spell = 4


class SKELETON_PARAM_KNEE_AXIS_DIR(UnsignedChar):
    """TODO"""


class SP_EFE_PC_WEAPON_STATE(UnsignedChar):
    """TODO"""


class SP_EFE_WEP_CHANGE_PARAM(UnsignedChar):
    All = 0
    CurrentRightHand = 1  # effect will end if weapon is changed
    CurrentLeftHand = 2  # effect will end if weapon is changed
    Self = 3  # affects character directly (i.e. status damage) rather than being applied to hits
    FootDamage = 4  # from kicking or landing, e.g. Orange Charred Ring effect


class SP_EFFECT_BOOL(UnsignedChar):
    """Boolean used in Special Effects table."""

    Off = 0
    On = 1


class SP_EFFECT_CHANGE_TEAM_TYPE(SignedChar):
    """TODO"""


class SP_EFFECT_CONVERT_ATTRIBUTE(UnsignedChar):
    """TODO"""


class SP_EFFECT_MOVE_TYPE(UnsignedChar):
    """Named after observed usage."""

    Normal = 0
    Chameleon = 3
    DeepWater = 4
    IronFlesh = 5


class SP_EFFECT_SAVE_CATEGORY(SignedChar):
    """Determines how often and/or in what order special effects are saved on every update. Names are from observed
    usage only."""

    NoSave = -1
    Poison = 0
    Bleed = 1
    Toxic = 2
    Egg = 3
    DragonHeadStone = 4
    DragonTorsoStone = 5


class SP_EFFECT_SPCATEGORY(UnsignedShort):
    """Category of special effect, which determines which other special effects it will replace (and maybe more). Many
    values used."""

    SorceryOrPyromancy = 3
    Miracle = 4


class SP_EFFECT_THROW_CONDITION_TYPE(UnsignedChar):
    """Field in SpEffect entries that changes all throws in some way (e.g. disables them / increases riposte damage)."""

    Default = 0
    ThrowDisabled = 1
    ParryCollapsed = 2  # used only by SpEffect 30 at an unknown time; unknown effect on throws
    InCoffinOrNearQuelana = 3  # unknown effect on throws
    Falling = 4  # unknown effect on throws
    HornetRing = 5  # damage boost
    HumanityDrain = 6  # lose soft humanity


class SP_EFFECT_TYPE(UnsignedChar):
    """TODO"""


class SP_EFFECT_USELIMIT_CATEGORY(UnsignedChar):
    """Category of special effect triggered by goods or spells in which only one effect can be active at once.
    Additional attempts to use goods or cast spells in the same category will be prohibited, rather than overriding
    the earlier one."""

    NoLimit = 0
    BuffWeapon = 1
    BuffBody = 2
    DragonStone = 3
    BuffShield = 13


class SP_EFFECT_VFX_EFFECT_TYPE(UnsignedChar):
    """TODO"""


class SP_EFFECT_VFX_PLAYCATEGORY(UnsignedChar):
    """TODO"""


class SP_EFFECT_VFX_SOUL_PARAM_TYPE(UnsignedChar):
    """TODO"""


class SpecialStateInfo(UnsignedChar):
    """Enum documented by me for the SpecialStateIndex field, which specifies many varying hard-coded effects in the
    game engine, like ongoing animations, particle effects, and special triggers. The visual effect parameters are
    specified by the same index in the Special Effect Visuals param table."""

    # TODO: Unclear what carries over to Bloodborne. Probably extensive changes.

    NoState = 0
    LavaBurning = 1  # Lava damage on self, probably burning feet (not visible with resin though).
    PoisonAura = 2  # Poison cloud on self.
    SlimeCovered = 3  # "Jelly covered".
    DurabilityDamage = 4  # Corrosive attack.
    ToxicAura = 5  # Toxic on self.
    BleedAura = 6  # Bleeding on self.
    Transparent = 8  # Makes player transparent (Fog Ring/Hidden Figure) and possibly causes cancellation when hit.
    PurpleMossClump = 10  # Purple Moss Clump application effect.
    BloomingPurpleMossClump = 11  # Blooming Purple Moss Clump application effect.
    BloodRedMossClump = 12  # Blood-Red Moss Clump application effect.
    DivineBlessing = 13  # Divine Blessing full health recovery.
    BinocularsZoom = 15  # Apply Binoculars camera zoom. Not recommended.
    ForceRespawn = 16  # Return to last spawn point (Darksign/Homeward Bone).
    # 17 CRASHES THE GAME. Unfinished "resurrection stone" stuff.
    RepairPowder = 26  # Repair Powder, no visible effect for resin.
    MagicWeapon = 28  # Magic Weapon.
    FallingControl = 47  # Falling Control glowing blue feet. TODO: damage reduction as well?
    TearstoneRingAura = 48  # Tearstone Ring aura; yellow rays come out of you. Kind of annoying, actually.
    ElizabethMushroom = 50  # Elizabeth's Mushroom regen effect.
    SilentMovement = 54  # Sound cancellation. Does not affect enemy hearing itself.
    StrongMagicWeapon = 60  # Strong Magic Weapon.
    CrystalMagicWeapon = 61  # Crystal Magic Weapon.
    FireWeapon = 62  # Flaming right-hand weapon (Charcoal Pine Resin).
    DarkmoonBlade = 64  # Likely just a visual effect.
    CovetousGoldSerpentRing = 66  # Must increase item discovery, e.g. by shifting points to other item lot slots.
    MagicPowerUp = 71  # Magic/Miracle power up. Not sure what this does exactly.
    GreenBlossom = 75  # Green aura VFX (Green Blossom).
    CovetousSilverSerpentRing = 76  # Not sure what it does, since the soul increase is done with params.
    TranquilWalkOfPeace = 102  # Stone Knight "gravity", probably enables Tranquil Walk glyph around player.
    EggParasiteInvisible = 111  # no sign of it yet (incubation).
    EggParasiteScratching = 112  # player scratches head every ten seconds (interval set in params).
    EggParasiteStandby = 113  # seems to pass instantly.
    EggParasiteHead = 114  # egg appears, eats half souls. Goes to 192.
    FlipDodge = 115  # Enables flip dodges (Dark Wood Grain Ring).
    CurseDamage = 116  # Petrification/crystal curse damage.
    Petrification = 117  # Turn into a stone statue and die.
    PurgingStone = 118  # Purging stone.
    HumanityRecovery = 119  # "Humanity recovery", has no immediate effect. Also used for Darkwraith effect.
    AnimationPoiseChange = 120  # Animation superarmor changes.
    ThornedHead = 123  # Armor deals damage on contact.
    ThornedBody = 124  # Armor deals damage on contact.
    ThornedArms = 125  # Armor deals damage on contact.
    ThornedLegs = 126  # Armor deals damage on contact.
    MimicSleep = 127  # Lloyd's Talisman used on Mimic.
    UndeadRapport = 132  # Undead enemies (hard-coded list) become your ally temporarily.
    Crystallization = 136  # Turn into a crystal statue and die.
    LavaDamage = 142  # Damaging effect of walking in lava.
    SkeletonImmortality = 143  # Immortal skeleton.
    SkeletonDisassembled = 144  # Skeleton disassembled?
    CastLight = 147  # Ball of light from Cast Light.
    LightningWeapon = 151  # Lightning right-hand weapon (Gold Pine Resin).
    PoisonedWeapon = 152  # Adds poisoned weapon VFX and actually makes "atkOccurrenceSpEffectId" apply on each hit.
    SunlightBlade = 153  # Sunlight Blade VFX.
    WolfRing = 155  # Change in superarmor (Wolf Ring). White aura effect.
    TransientCurse = 157  # Transient Curse effect (white aura).
    MagicShield = 158  # Magic Shield.
    RingOfSacrifice = 159  # Ring of Sacrifice, probably disables loss of souls.
    RareRingOfSacrifice = 160  # Ring of Rare Sacrifice, probably disables loss of souls and negates curse.
    # 161-165 are extra Homeward Bone effects, apparently unused (and they have no immediate effect).
    PledgeStoneDestroyed = 166  # "Pledge stone destroyed", no immediate effect.
    BowRangeBoost = 168  # from Hawk Ring. Seems necessary for boost to apply.
    KarmicJustice = 170  # (Karmic Justice)
    AlluringSkullA = 176  # Alluring Skull "A".
    AlluringSkullB = 177  # Alluring Skull "B".
    HiddenWeapon = 184  # Hidden Weapon.
    OrangeCharredRing = 186  # "lava walk", probably involved with canceling damage from effect 4030.
    EggParasiteFinal = 192  # kick replaced by larva attack.
    LingeringDragoncrestRing = 193  # (Lingering Dragoncrest Ring)
    ExtraAttunement = 194  # 50% attunement slot boost from Dusk Crown Ring. Does not include half HP effect.
    AffectThrustCounterDamageOnly = 197  # Attack boosts only affect counter damage with thrusting-type attacks.
    EggVermifuge = 198  # Egg Vermifuge treatment.
    RingOfTheEvilEye = 199  # Triggers hard-coded special effect 2241 whenever an enemy is killed.
    HalfSpellCasts = 203  # Manus Catalyst, Tin Crystallization Catalyst
    StrongMagicShield = 204  # Strong Magic Shield.


class THROW_DMY_CHR_DIR_TYPE(UnsignedChar):
    """Named after observed usage. Not sure if this simply describes if the model point contains information about
    character direction, or actually makes that so. Non-zero values are rarely used."""

    Normal = 0
    ArmoredTusk = 1
    IronGolemGapingDragon = 255


class THROW_ENABLE_STATE(UnsignedChar):
    Off = 0
    On = 1


class THROW_PAD_TYPE(UnsignedChar):
    NoPad = 0  # Used only for test throw.
    Default = 1  # Used for all others.
    Unknown = 3  # Used for Centipede Demon grab, Male Ghost grab, and Dark Hand grab.


class THROW_TYPE(UnsignedChar):
    """Named after observed usage. The Hornet Ring variants have slightly different animations when used against PCs."""

    Backstab = 0
    # 1-7 unused.
    Riposte = 8
    CoffinStab = 9
    Plunging = 10
    HornetBackstab = 11
    HornetRiposte = 12
    Drain = 13
    HornetCoffinStab = 14
    HornetPlunging = 15
    HornetDrain = 16


class WEAPON_CATEGORY(UnsignedChar):
    """Each category includes weapons of all sizes."""

    Dagger = 0
    StraightSword = 1  # includes whips
    ThrustingSword = 2
    CurvedSword = 3  # includes katanas
    Axe = 4
    Hammer = 5
    Spear = 6
    Halberd = 7
    SpellTool = 8  # includes Catalysts and Talismans
    Fists = 9
    Bow = 10
    Crossbow = 11
    Shield = 12
    Arrow = 13
    Bolt = 14


class WEP_MATERIAL_ATK(UnsignedChar):
    """Determines both sound and visual effects of attack."""

    Metal = 0
    WoodOrLeather = 2
    Riposte_Ladder_SpellTool = 3  # not sure why these are combined
    Magic = 5
    OtherBullet = 6  # Non-Magic bullet.
    Special = 6  # cop-out name; used for dark sorceries, Firebombs, Moonlight Greatsword, and falling/rolling damage
    Default = 255  # most attacks; uses weapon attack material, presumably.


class WEP_MATERIAL_DEF(UnsignedChar):
    """Sound effect when material is struck."""

    NoEffect = 0
    Hairstyle = 29  # not sure when this would actually be used
    MetalWeapon = 50
    WoodWeapon = 52  # includes catalysts
    Hands = 53  # talismans, Pyromancy Flame, Skull Lantern, bare fists
    MetalShield = 54
    WoodenShield = 55
    MetalArmor = 56  # e.g. Catarina, Dark, Black Iron, Favor
    ChainArmor = 57  # e.g. Paladin, Channeler, Chain, Cleric
    FabricArmor = 58  # e.g. Brigand, Shadow, Crystalline, Sealer
    NoArmor = 59  # no armor; also Dragon Stone skin
    HeadshotFabric = 60
    HeadshotMetal = 63
    StoneShield = 79


class WEP_MATERIAL_DEF_SFX(UnsignedChar):
    """Visual effect when material is struck."""

    NoEffect = 0
    Hairstyle = 29  # not sure when this would actually be used
    MetalWeapon = 50
    WoodOrLeatherWeapon = 52
    MetalArmor = 56
    HandsOrFabricArmor = 59
    HeadshotFabric = 60
    HeadshotMetal = 63


class WEP_CORRECT_TYPE(UnsignedChar):
    """I believe this determines the graph used for applying scaling."""

    PhysicalMelee = 0
    MagicMelee = 1  # Magic/Enchanted/Divine/Occult weapon upgrades
    PhysicalAndSorcerySpells = 11  # Logan's Catalyst (boosts dark sorceries more)
    MiracleSpells = 12  # most talismans
    DarkmoonTalisman = 13  # not sure why this has its own category rather than Velka's Talisman
    SorcerySpells = 14  # most catalysts
    OolacileIvoryCatalyst = 15
    IvorySunlightTalismans = 16


class WEPMOTION_CATEGORY(UnsignedChar):
    """Animation offset for player weapons. Used in TAE lookup (multiplied by 10000)."""

    Default = 0  # includes default one-handed animations; no attack animations

    # One-handed passive animations (if different from default)
    OneHandedHeavy = 2  # carried on shoulder
    OneHandedSpear = 3  # held out wide and low

    # Two-handed passive animations (always set)
    TwoHandedLight = 10  # holds weapon in front (swords, axes, etc.)
    TwoHandedHeavy = 12  # holds weapon over shoulder (greatswords)
    TwoHandedSpear = 13  # holds weapon as a spear (spears, halberds, scythes, etc.)
    TwoHandedBow = 14
    TwoHandedShield = 15
    TwoHandedCrossbow = 16

    # Class base attack animations
    DaggerClass = 20
    StraightSwordClass = 23
    GreatswordClass = 25  # includes Curved Greatswords
    UltraGreatswordClass = 26
    RapierClass = 27
    CurvedSwordClass = 28
    KatanaClass = 29
    AxeClass = 30
    GreataxeClass = 32
    HammerClass = 33
    GreatHammerClass = 35
    SpearClass = 36
    HalberdClass = 38
    SpellToolClass = 41
    FistsClass = 42
    WhipClass = 43
    BowClass = 44
    CrossbowClass = 46
    GreatshieldClass = 47
    ShieldClass = 48  # small and medium shields

    # Weapon-specific animation overrides
    GreatScythes = 50  # Great Scythe, Lifehunt Scythe
    CurvedGreatswords = 51  # Server, Murakumo
    Talisman = 52  # includes Pyromancy Flame
    SwordSmash = 53  # Broadsword, Barbed Straight Sword, Straight Sword Hilt
    BalderSideSword = 54
    SilverKnightStraightSword = 55
    QuelaagsFurysword = 56
    Darksword = 57
    DrakeSword = 58
    HammerSmash = 59  # Mace, Morning Star, Blacksmith Hammer, Hammer of Vamos
    Warpick = 60
    Pickaxe = 61
    Grant = 62
    Partizan = 63
    DemonsSpear = 64
    ChannelersTrident = 65
    SilverKnightSpear = 66
    Pike = 67
    DragonslayerSpear = 68
    GreatClub = 69
    SmoughsHammer = 70
    ParryingDagger = 71
    BanditKnife = 72
    PriscillasDagger = 73
    Claymore = 74
    Flamberge = 75
    StoneGreatsword = 77
    GreatswordOfArtorias = 78
    MoonlightGreatsword = 79
    BlackKnightSword = 80
    ShortBowSpecial = 81  # Short Bow, Composite Bow, Darkmoon Bow
    BlackBowOfPharis = 82
    GreatbowSpecial = 83  # Dragonslayer Greatbow, Gough's Greatbow
    Avelyn = 84
    SniperCrossbow = 85
    Claw = 86
    DragonBoneFist = 87
    Iaito = 89
    ChaosBlade = 90
    BetterParry = 91  # Target Shield, Buckler
    CrystalRingShield = 92
    MediumShieldBash = 93  # Spiked Shield, Crystal Shield, Pierce Shield
    HavelsGreatshield = 94
    Greatsword = 95  # actual weapon named Greatsword, not class
    DemonGreatMachete = 96
    GreatLordGreatsword = 97
    DragonGreatsword = 98
    Shotel = 99
    JaggedGhostBlade = 100
    PaintingGuardianSword = 101
    HandAxe = 102
    ButcherKnife = 103
    GolemAxe = 104
    DemonsGreataxe = 105
    DragonKingGreataxe = 106
    BlackKnightGreataxe = 107
    Halberd = 108
    Lucerne = 109
    GiantsHalberd = 110
    TitaniteCatchPole = 111
    BlackKnightHalberd = 112
    Estoc = 113
    VelkasRapier = 114
    RicardsRapier = 115
    GravelordSword = 116
    Ryuken = 117  # Seems to be an unused Fists variant.
    CrescentAxe = 118
    MailBreaker = 119
    GhostBlade = 120
    SkullLantern = 121
    DarkHand = 123
    LargeClub = 124
    GargoyleTailAxe = 125
    BonewheelShield = 126
    CatalystThrust = 127  # Tin Crystallization Catalyst, Demon's Catalyst
    BlackKnightGreatsword = 128
    HeavyCrossbow = 129
    DarkSilverTracer = 130
    AbyssGreatsword = 131
    GoldTracer = 132
    StoneGreataxe = 133
    FourProngedPlow = 134
    ObsidianGreatsword = 135
    ManusCatalyst = 136
