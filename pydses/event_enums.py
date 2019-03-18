"""
@author: grimrhapsody
"""

from enum import IntEnum


""" EVENT ENUM DEFINITIONS """


class AIStatusType(IntEnum):
    normal = 0
    recognition = 1
    alert = 2
    battle = 3


class BitOperation(IntEnum):
    add = 0
    delete = 1
    invert = 2


# ENUM_BOOL omitted for lack of necessity and conflict with python keywords


class NumberButtons(IntEnum):
    one_button = 1
    two_button = 2
    no_button = 6


class ButtonType(IntEnum):
    yes_no = 0
    ok_cancel = 1


class Category(IntEnum):
    object = 0
    region = 1
    character = 2


class CharacterType(IntEnum):
    """
    This name chosen over the translation of the original ("survival"), since it is found in event_define.lua
    as CHR_TYPE_LivePlayer (and that's a translation by From Software themselves)
    """
    human = 0
    white_phantom = 1
    black_phantom = 2
    hollow = 8
    intruder = 10


class CharacterUpdateRate(IntEnum):
    never = -1
    always = 0
    every_two_frames = 2
    every_five_frames = 5


class ClassType(IntEnum):
    warrior = 0
    knight = 1
    wanderer = 2
    thief = 3
    bandit = 4
    hunter = 5
    sorcerer = 6
    pyromancer = 7
    cleric = 8
    deprived = 9
    temp_warrior = 20
    temp_knight = 21
    temp_sorcerer = 22
    temp_pyromancer = 23
    chi_warrior = 24
    chi_knight = 25
    chi_sorcerer = 26
    chi_pyromancer = 27


class ComparisonType(IntEnum):
    equal = 0
    not_equal = 1
    greater_than = 2
    less_than = 3
    greater_than_or_equal = 4
    less_than_or_equal = 5


# ENUM_CONDITION_STATE omitted because it's the same as ENUM_BOOL


class Contained(IntEnum):
    outside = 0
    inside = 1


class Covenant(IntEnum):
    none = 0
    way_of_white = 1
    princess_guard = 2
    warrior_of_sunlight = 3
    darkwraith = 4
    path_of_the_dragon = 5
    gravelord_servant = 6
    forest_hunter = 7
    darkmoon_blade = 8
    chaos_servant = 9


class CutsceneType(IntEnum):
    skippable = 0
    unskippable = 2
    skippable_with_fade_out = 8
    unskippable_with_fade_out = 10


class DamageTargetType(IntEnum):
    character = 1
    map = 2
    character_and_map = 3


# ENUM_DEATH_STATUS omitted since it's "bool IsDead"


# ENUM_ENABLE_STATE omitted since it's "bool IsEnabled"


class EventEndType(IntEnum):
    end = 0
    restart = 1


class FlagType(IntEnum):
    event_flag = 0
    event = 1
    event_with_slot = 2


class InterpolationState(IntEnum):
    interpolated = 0
    not_interpolated = 1


class ItemType(IntEnum):
    weapon = 0
    armor = 1
    ring = 2
    good = 3


class LogicalOperationType(IntEnum):
    all_on = 0
    all_off = 1
    not_all_off = 2
    not_all_on = 3


class MultiplayerState(IntEnum):
    host = 0
    client = 1
    multiplayer = 2
    singleplayer = 3


class NavimeshType(IntEnum):
    solid = 1
    exit = 2
    obstacle = 4
    wall = 8
    wall_touching_floor = 32
    landing_point = 64
    event = 128
    cliff = 256
    wide = 512
    ladder = 1024
    hole = 2048
    door = 4096
    closed_door = 8192


# ENUM_ON_OFF omitted for obvious reasons


class OnOffChange(IntEnum):
    off = 0
    on = 1
    change = 2


# ENUM_OWN_STATE omitted; "bool IsOwner"


class ReactionAttribute(IntEnum):
    human_or_hollow = 48
    all = 255


class SummonSignType(IntEnum):
    blue_eye_sign = 0
    black_eye_sign = 1
    red_eye_sign = 2
    detection_sign = 3
    white_help_sign = 4
    black_help_sign = 5


class SiteType(IntEnum):
    part1 = 1
    part2 = 2
    part3 = 3
    part4 = 4
    part5 = 5
    part6 = 6
    weakpoint = 7
    part7 = 8
    part8 = 9


class SoundType(IntEnum):
    a_ambient = 0
    c_character_motion = 1
    f_menu_se = 2
    o_object = 3
    p_cutscene = 4
    s_sfx = 5
    m_music = 6
    v_voice = 7
    x_floor_material_dependant = 8
    b_armor_material_dependant = 9
    g_ghost = 10


class StatueType(IntEnum):
    stone = 0
    crystal = 1


team_type_dict = {
    ('none', 'no_team'): 0,
    ('live', 'human'): 1,
    ('white_phantom', 'white', 'white_ghost'): 2,
    ('black_phantom', 'black', 'black_ghost'): 3,
    ('hollow', 'gray_ghost', 'glay_ghost'): 4,
    ('vagrant', 'wander_ghost', 'wandering_ghost'): 5,
    ('enemy',): 6,
    ('boss', 'strong_enemy'): 7,
    ('ally', 'friend'): 8,
    ('hostile_ally', 'hostile_friend', 'angry_ally', 'angry_friend'): 9,
    ('decoy',): 10,
    ('decoy_like',): 11,
    ('fighting_ally', 'battle_ally', 'fighting_friend', 'fighting_ally'): 12,
    ('intruder', 'invader'): 13,
    ('neutral',): 14,
    ('charm',): 15,
}


class TeamType(IntEnum):
    """
    Names taken from ai_define.lua:
    TEAM_TYPE_None = 0
    TEAM_TYPE_Live = 1
    TEAM_TYPE_WhiteGhost = 2
    TEAM_TYPE_BlackGhost = 3
    TEAM_TYPE_GlayGhost = 4
    TEAM_TYPE_WanderGhost = 5
    TEAM_TYPE_Enemy = 6
    TEAM_TYPE_Boss = 7
    TEAM_TYPE_Friend = 8
    TEAM_TYPE_AngryFriend = 9
    TEAM_TYPE_Decoy = 10
    TEAM_TYPE_DecoyLike = 11
    TEAM_TYPE_BattleFriend = 12
    TEAM_TYPE_Intruder = 13
    TEAM_TYPE_Neutral = 14
    TEAM_TYPE_Charm = 15
    """
    none = 0
    live = 1
    white_phantom = 2
    black_phantom = 3
    hollow = 4
    vagrant = 5
    enemy = 6
    boss = 7
    ally = 8
    hostile_ally = 9
    decoy = 10
    decoy_like = 11
    fighting_ally = 12
    intruder = 13
    neutral = 14
    charm = 15


class TendencyType(IntEnum):
    white = 0
    black = 1


class TextBannerType(IntEnum):
    """
    Some values taken from event_define.lua:
    TEXT_TYPE_KillDemon = 1
    TEXT_TYPE_Dead = 2
    TEXT_TYPE_Revival = 3
    TEXT_TYPE_SoulGet = 4
    TEXT_TYPE_TargetClear = 5
    TEXT_TYPE_GhostDead = 6
    TEXT_TYPE_BlackClear = 7
    TEXT_TYPE_MapName = 8
    TEXT_TYPE_MagicResurrection = 9
    TEXT_TYPE_RingNormalResurrection = 10
    TEXT_TYPE_RingCurseResurrection = 11
    TEXT_TYPE_Congratulations = 12
    TEXT_TYPE_Bonfire = 13
    """
    boss_defeated = 1
    you_died = 2
    resurrection = 3
    souls_retrieved = 4
    target_defeated = 5
    ghost_death = 6
    black_ghost_death = 7
    map_name = 8
    magic_revival = 9
    ring_revival = 10
    rare_ring_revival = 11
    congratulations = 12
    bonfire_lit = 13
    arena_victory = 15
    arena_loss = 16
    arena_draw = 17


class UpdateAuthority(IntEnum):
    normal = 0
    forced = 4095
