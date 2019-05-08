"""
@author: grimrhapsody
"""


from enum import IntEnum


""" EVENT_DEFINE.LUA """


# Verbatim
LOCAL_PLAYER = 10000


# Verbatim
NET_PLAYER = 10001


class message_category(IntEnum):
    """
    Extended original abbreviated name ("MSG_CATEGORY").
    Obvious enough to assume "message" is the proper extended word.
    """
    sample = 0
    talk = 1
    blood = 2  # Likely refers to BloodMsg's, which are orange soapstone messages rather than bloodstains IIRC
    item = 10
    weapon = 11
    protector = 12
    accessory = 13
    item_exp = 14
    weapon_exp = 15
    protector_exp = 16
    accessory_exp = 17
    event = 30
    dialog = 78


class info_menu_type(IntEnum):
    list = 0
    simple = 1


class object_damage_hit_type(IntEnum):
    """
    Note: IntEnum name obtained from comment left in Demon's Souls event_define.lua which reads:
    【OnObjectDamageHit ヒット対象識別用定数】

    Rough Google Translation:
    【OnObjectDamageHit hit object identification constant】

    The names of the enum members come from the comments on the variables in DeS event_define.lua
    """
    characters = 1
    maps = 2
    characters_and_maps = 3


class trigger_attribute(IntEnum):
    """
    Note: IntEnum name obtained from comment left in Demon's Souls event_define.lua which reads:
    【発動属性】 --発動をプレイヤの状態によって制限できる

    Translation:
    【Trigger Attribute】 - Limit activation depending on player's condition.
    """
    session = 1
    no_session = 2
    host = 4
    client = 8
    live = 16
    gray = 32  # Spelling changed from "GREY" so it matches other enums.
    white = 64
    black = 128
    all = 255


class talk_attribute(IntEnum):
    """
    Note: IntEnum name obtained from comment left in Demon's Souls event_define.lua which reads:
    【イベント会話の設定フラグ】 --会話の設定フラグ関連

    Rough Google Translation:
    【Event Flag Setting Flag】 - Conversation Setting Flag Relation
    """
    repeat = 1
    pad = 2
    draw = 4
    voice = 8
    all = 255


class player_death_type(IntEnum):
    """
    Renamed from original name "DEATH_STATE" to avoid confusion with EMELD's "Death State",
    which has the values "Alive" and "Dead"

    Values renamed to their ingame names for both easier understanding and shorter names.

    Original event_define.lua values:
    DEATH_STATE_Normal = 0
    DEATH_STATE_MagicResurrection = 1
    DEATH_STATE_RingNormalResurrection = 2
    DEATH_STATE_RingCurseResurrection = 3
    """
    normal = 0
    magic_revival = 1  # This is what the unused text banner texture says IIRC.
    ring_revival = 2
    rare_ring_revival = 3


class summon_param_type(IntEnum):
    none = 0
    white = -1
    black = -2
    force_join_black = -4  # Fixed typo in original ("FroceJoinBlack")
    detect_black = -4
    invade_nito = -7
    dragonewt = -10
    invade_bounty = -11
    coliseum = -12


""" This is probably completely useless, but feel free to uncomment if you find a use:
class soul_rate(IntEnum):
    small = 0.1
    medium = 0.5
    large = 0.5
"""


class invade_type(IntEnum):
    none = 0
    normal_white = 1
    normal_black = 2
    force_join_black = 3
    detect_black = 4
    white_rescue = 5
    black_rescue = 6
    nito = 7
    thieves_guild = 8
    otouto_umbasa = 9
    dragonewt = 10
    invade_bounty = 11
    coliseum_one_b = 12
    coliseum_two_a2 = 13
    coliseum_two_b1 = 14
    coliseum_two_b2 = 15
    coliseum_br_b = 16
    coliseum_br_c = 17
    coliseum_br_d = 18


