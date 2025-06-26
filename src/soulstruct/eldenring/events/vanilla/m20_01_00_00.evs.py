"""
Enir-Ilim

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_20010197()
    Event_20010199()
    DisableAsset(20011542)
    DisableAsset(20011544)
    DisableAsset(20011546)
    DisableAsset(20011548)
    CommonFunc_90005780(
        0,
        flag=20010800,
        summon_flag=20012160,
        dismissal_flag=20012161,
        character=20010701,
        sign_type=20,
        region=20012160,
        right=20019220,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=20010800, flag_1=20012160, flag_2=20012161, character=20010701)
    CommonFunc_90005784(
        0,
        flag=20012160,
        flag_1=20012805,
        character=20010701,
        region=20012800,
        region_1=20012809,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=20010800,
        summon_flag=20012164,
        dismissal_flag=20012165,
        character=20010710,
        sign_type=20,
        region=20012164,
        right=22009232,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=20010800, flag_1=20012164, flag_2=20012165, character=20010710)
    CommonFunc_90005784(
        0,
        flag=20012164,
        flag_1=20012805,
        character=20010710,
        region=20012800,
        region_1=20012809,
        animation=0,
    )
    if CeremonyInactive(ceremony=20):
        Event_20012150(
            0,
            flag=20012149,
            flag_1=20012168,
            flag_2=20012169,
            character=20010730,
            asset=20011730,
            flag_3=20012780,
            action_button_id=209530,
            message=2080840,
            text=4080843,
            left_flag=20012170,
            cancel_flag__right_flag=20012171,
        )
        Event_20012150(
            1,
            flag=20012149,
            flag_1=20012172,
            flag_2=20012173,
            character=20010731,
            asset=20011731,
            flag_3=20012781,
            action_button_id=209531,
            message=2080850,
            text=4080853,
            left_flag=20012174,
            cancel_flag__right_flag=20012175,
        )
        Event_20012150(
            2,
            flag=20012149,
            flag_1=20012176,
            flag_2=20012177,
            character=20010732,
            asset=20011732,
            flag_3=20012782,
            action_button_id=209532,
            message=2080860,
            text=4080863,
            left_flag=20012178,
            cancel_flag__right_flag=20012179,
        )
        Event_20012155(0, flag=20012149, flag_1=20012168, flag_2=20012780, other_entity=20011730, character=20010730)
        Event_20012155(1, flag=20012149, flag_1=20012172, flag_2=20012781, other_entity=20011731, character=20010731)
        Event_20012155(2, flag=20012149, flag_1=20012176, flag_2=20012782, other_entity=20011732, character=20010732)
    CommonFunc_9005810(
        0,
        flag=20010800,
        grace_flag=20010000,
        character=20010950,
        asset=20011950,
        enemy_block_distance=5.0,
    )
    RegisterGrace(grace_flag=20010002, asset=20011952, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=20010003, asset=20011953, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=20010004, asset=20011954, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=20010005, asset=20011955, enemy_block_distance=8.0)
    RegisterGrace(grace_flag=20010006, asset=20011956, enemy_block_distance=8.0)
    Event_20012800()
    Event_20012810()
    Event_20012811()
    Event_20012840()
    Event_20012847()
    Event_20012849()
    Event_20012820()
    Event_20012830(0, character=20010810, special_effect=20011580, special_effect_1=20011581)
    Event_20012830(1, character=20010811, special_effect=20011582, special_effect_1=20011583)
    Event_20012830(2, character=20010812, special_effect=20011584, special_effect_1=20011585)
    Event_20012830(3, character=20010813, special_effect=20011586, special_effect_1=20011587)
    Event_20012835()
    Event_20012145(
        0,
        flag=7625,
        flag_1=20012140,
        flag_2=20019257,
        left_flag=20012141,
        cancel_flag__right_flag=20012142,
        message=2080605,
        action_button_id=209055,
        asset=20011140,
        vfx_id=30010,
    )
    if CeremonyActive(ceremony=20):
        Event_20012146(0, flag=7625, character=20010725, banner_type=5, region=20012777)
        Event_20012195()
    CommonFunc_90005501(
        0,
        flag=20010510,
        flag_1=20010511,
        left=0,
        asset=20011510,
        asset_1=20011511,
        asset_2=20011512,
        flag_2=20010512,
    )
    CommonFunc_90005501(
        0,
        flag=20010515,
        flag_1=20010516,
        left=0,
        asset=20011515,
        asset_1=20011516,
        asset_2=20011517,
        flag_2=20010517,
    )
    CommonFunc_90005501(
        0,
        flag=20010520,
        flag_1=20010521,
        left=0,
        asset=20011520,
        asset_1=20011521,
        asset_2=20011522,
        flag_2=20010522,
    )
    CommonFunc_90005501(
        0,
        flag=20010525,
        flag_1=20010526,
        left=0,
        asset=20011525,
        asset_1=20011526,
        asset_2=20011527,
        flag_2=20010527,
    )
    CommonFunc_90005501(
        0,
        flag=20010530,
        flag_1=20010531,
        left=0,
        asset=20011530,
        asset_1=20011531,
        asset_2=20011532,
        flag_2=20010532,
    )
    CommonFunc_90005501(
        0,
        flag=20010535,
        flag_1=20010536,
        left=0,
        asset=20011535,
        asset_1=20011536,
        asset_2=20011537,
        flag_2=20010537,
    )
    Event_20012510()
    Event_20012580()
    Event_20012500()
    Event_20012200(
        0,
        character=20010451,
        special_effect=20011884,
        special_effect_1=20011894,
        weather=17,
        special_effect_2=20004220,
        character_1=20010453,
        special_effect_3=20011885,
        character_2=20010455,
        special_effect_4=20011886,
    )
    Event_20012200(
        1,
        character=20010453,
        special_effect=20011885,
        special_effect_1=20011895,
        weather=2,
        special_effect_2=20004221,
        character_1=20010451,
        special_effect_3=20011884,
        character_2=20010455,
        special_effect_4=20011886,
    )
    Event_20012200(
        2,
        character=20010455,
        special_effect=20011886,
        special_effect_1=20011896,
        weather=7,
        special_effect_2=20004222,
        character_1=20010451,
        special_effect_3=20011884,
        character_2=20010453,
        special_effect_4=20011885,
    )
    Event_20010610()
    CommonFunc_90005615(0, region=20019253, left=0)
    Event_20010700(
        0,
        character=20010720,
        flag=20012792,
        flag_1=20012149,
        flag_2=20012783,
        distance=165.0,
        flag_3=20019523,
        flag_4=20012791,
        text=4080920,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        seconds=2.0,
        right=0,
    )
    Event_20010700(
        1,
        character=20010724,
        flag=20012793,
        flag_1=20012149,
        flag_2=20012784,
        distance=165.0,
        flag_3=20019524,
        flag_4=20012791,
        text=4080930,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        seconds=2.0,
        right=0,
    )
    Event_20010700(
        2,
        character=20010722,
        flag=20012794,
        flag_1=20012149,
        flag_2=20012785,
        distance=165.0,
        flag_3=20019525,
        flag_4=20012791,
        text=4080890,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        seconds=2.0,
        right=0,
    )
    Event_20010700(
        3,
        character=20010723,
        flag=20012795,
        flag_1=20012149,
        flag_2=20012786,
        distance=165.0,
        flag_3=20019526,
        flag_4=20012791,
        text=4080900,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        seconds=2.0,
        right=0,
    )
    Event_20010700(
        4,
        character=20010721,
        flag=20012796,
        flag_1=20012149,
        flag_2=20012787,
        distance=165.0,
        flag_3=20019527,
        flag_4=20012791,
        text=4080910,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        seconds=2.0,
        right=1,
    )
    Event_20010705(
        0,
        character=20010730,
        flag=20012797,
        flag_1=20012149,
        flag_2=20012788,
        distance=165.0,
        flag_3=20019528,
        flag_4=20012791,
        text=4080840,
        text_1=4080841,
        flag_5=7630,
        seconds=0.0,
        seconds_1=2.0,
        right=1,
    )
    Event_20010705(
        1,
        character=20010731,
        flag=20012798,
        flag_1=20012149,
        flag_2=20012789,
        distance=165.0,
        flag_3=20019529,
        flag_4=20012791,
        text=4080850,
        text_1=4080851,
        flag_5=7630,
        seconds=0.0,
        seconds_1=2.0,
        right=1,
    )
    Event_20010705(
        2,
        character=20010732,
        flag=20012799,
        flag_1=20012149,
        flag_2=20012790,
        distance=165.0,
        flag_3=20019530,
        flag_4=20012791,
        text=4080860,
        text_1=4080861,
        flag_5=7630,
        seconds=0.0,
        seconds_1=2.0,
        right=0,
    )
    Event_20010736(
        0,
        character=20012791,
        first_flag=20012783,
        last_flag=20012787,
        first_flag_1=20012788,
        last_flag_1=20012790,
        flag=20012712,
        flag_1=20012713,
        flag_2=20012714,
        flag_3=20012715,
        flag_4=20012716,
        flag_5=20012711,
        distance=165.0,
        character_1=20010720,
        flag_6=7625,
        flag_7=20019294,
        flag_8=7630,
        seconds=4.5,
    )
    Event_20010708(
        0,
        flag=20012149,
        flag_1=20012787,
        flag_2=20019527,
        flag_3=20012738,
        seconds=5.0,
        flag_4=20012791,
        flag_5=7630,
    )
    Event_20010708(
        1,
        flag=20012149,
        flag_1=20012788,
        flag_2=20019528,
        flag_3=20019243,
        seconds=5.0,
        flag_4=20012791,
        flag_5=7630,
    )
    Event_20010708(
        2,
        flag=20012149,
        flag_1=20012789,
        flag_2=20019529,
        flag_3=20012726,
        seconds=5.0,
        flag_4=20012791,
        flag_5=7630,
    )
    Event_20010711(
        0,
        flag=20012149,
        character=20010720,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20019284,
        flag_2=20019290,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019295,
        flag_4=20019533,
        flag_5=20019523,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        1,
        flag=20012149,
        character=20010720,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20019284,
        flag_2=20019291,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019295,
        flag_4=20019533,
        flag_5=20019523,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        2,
        flag=20012149,
        character=20010720,
        character_1=20010730,
        radius=3.0,
        flag_1=20019285,
        flag_2=20019292,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019295,
        flag_4=20019533,
        flag_5=20019523,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019528,
        left=20019528,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        3,
        flag=20012149,
        character=20010720,
        character_1=20010731,
        radius=3.0,
        flag_1=20019286,
        flag_2=20019293,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019295,
        flag_4=20019533,
        flag_5=20019523,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019529,
        left=20019529,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        4,
        flag=20012149,
        character=20010722,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012745,
        flag_2=20019400,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019402,
        flag_4=20019533,
        flag_5=20019525,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        5,
        flag=20012149,
        character=20010722,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012745,
        flag_2=20019401,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019402,
        flag_4=20019533,
        flag_5=20019525,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        6,
        flag=20012149,
        character=20010723,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012753,
        flag_2=20012756,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20012758,
        flag_4=20019533,
        flag_5=20019526,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        7,
        flag=20012149,
        character=20010723,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012753,
        flag_2=20012757,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20012758,
        flag_4=20019533,
        flag_5=20019526,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        8,
        flag=20012149,
        character=20010721,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012736,
        flag_2=20019352,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019355,
        flag_4=20019533,
        flag_5=20019527,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        9,
        flag=20012149,
        character=20010721,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012736,
        flag_2=20019353,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019355,
        flag_4=20019533,
        flag_5=20019527,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        10,
        flag=20012149,
        character=20010721,
        character_1=20010730,
        radius=3.0,
        flag_1=20012737,
        flag_2=20019354,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019355,
        flag_4=20019533,
        flag_5=20019527,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019528,
        left=20019528,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        11,
        flag=20012149,
        character=20010730,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20019240,
        flag_2=20019245,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019249,
        flag_4=20019533,
        flag_5=20019528,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        12,
        flag=20012149,
        character=20010730,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20019240,
        flag_2=20019246,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019249,
        flag_4=20019533,
        flag_5=20019528,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        13,
        flag=20012149,
        character=20010730,
        character_1=20010720,
        radius=3.0,
        flag_1=20019241,
        flag_2=20019247,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019249,
        flag_4=20019533,
        flag_5=20019528,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019523,
        left=20019523,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        14,
        flag=20012149,
        character=20010730,
        character_1=20010721,
        radius=3.0,
        flag_1=20019242,
        flag_2=20019248,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019249,
        flag_4=20019533,
        flag_5=20019528,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019527,
        left=20019527,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        15,
        flag=20012149,
        character=20010731,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012724,
        flag_2=20012728,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019341,
        flag_4=20019533,
        flag_5=20019529,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        16,
        flag=20012149,
        character=20010731,
        character_1=ALL_PLAYERS,
        radius=3.0,
        flag_1=20012724,
        flag_2=20012729,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019341,
        flag_4=20019533,
        flag_5=20019529,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=0,
        left=0,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010711(
        17,
        flag=20012149,
        character=20010731,
        character_1=20010723,
        radius=3.0,
        flag_1=20012725,
        flag_2=20019340,
        seconds=5.0,
        seconds_1=30.0,
        flag_3=20019341,
        flag_4=20019533,
        flag_5=20019529,
        seconds_2=5.0,
        flag_6=20019532,
        flag_7=20019526,
        left=20019526,
        flag_8=7630,
        flag_9=4929,
    )
    Event_20010729(
        0,
        attacker__character=20010720,
        flag=20012149,
        flag_1=20019287,
        flag_2=20019288,
        flag_3=20019289,
        flag_4=20019531,
        seconds=5.0,
        flag_5=7630,
        flag_6=20019507,
        flag_7=20019533,
        flag_8=20019514,
        flag_9=20019515,
        flag_10=20019516,
        flag_11=20019517,
        flag_12=20019518,
        flag_13=20019282,
        flag_14=20019283,
        seconds_1=10.0,
    )
    Event_20010729(
        1,
        attacker__character=20010721,
        flag=20012149,
        flag_1=20012739,
        flag_2=20019350,
        flag_3=20019351,
        flag_4=20019531,
        seconds=5.0,
        flag_5=7630,
        flag_6=20019507,
        flag_7=20019533,
        flag_8=20019514,
        flag_9=20019515,
        flag_10=20019516,
        flag_11=20019517,
        flag_12=20019518,
        flag_13=20012734,
        flag_14=20012735,
        seconds_1=10.0,
    )
    Event_20010731(
        0,
        attacker__character=20010722,
        flag=20012149,
        flag_1=20012748,
        flag_2=20012749,
        flag_3=20019531,
        seconds=5.0,
        flag_4=7630,
        flag_5=20019507,
        flag_6=20019533,
        flag_7=20019514,
        flag_8=20019515,
        flag_9=20019516,
        flag_10=20019517,
        flag_11=20019518,
        flag_12=20012744,
        seconds_1=10.0,
    )
    Event_20010731(
        1,
        attacker__character=20010723,
        flag=20012149,
        flag_1=20012754,
        flag_2=20012755,
        flag_3=20019531,
        seconds=5.0,
        flag_4=7630,
        flag_5=20019507,
        flag_6=20019533,
        flag_7=20019514,
        flag_8=20019515,
        flag_9=20019516,
        flag_10=20019517,
        flag_11=20019518,
        flag_12=20012752,
        seconds_1=10.0,
    )
    Event_20010733(
        0,
        character=20010724,
        flag=20012149,
        flag_1=20012761,
        flag_2=20019531,
        seconds=5.0,
        flag_3=7630,
        left=1,
        flag_4=20019533,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        flag_10=20012760,
        seconds_1=10.0,
    )
    Event_20010733(
        1,
        character=20010730,
        flag=20012149,
        flag_1=20019244,
        flag_2=20019531,
        seconds=5.0,
        flag_3=7630,
        left=0,
        flag_4=20019533,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        flag_10=20019239,
        seconds_1=0.0,
    )
    Event_20010733(
        2,
        character=20010731,
        flag=20012149,
        flag_1=20012727,
        flag_2=20019531,
        seconds=5.0,
        flag_3=7630,
        left=0,
        flag_4=20019533,
        flag_5=20019514,
        flag_6=20019515,
        flag_7=20019516,
        flag_8=20019517,
        flag_9=20019518,
        flag_10=20012723,
        seconds_1=0.0,
    )
    Event_20010738(
        0,
        first_flag=20019235,
        last_flag=20019249,
        first_flag_1=20019280,
        last_flag_1=20019295,
        first_flag_2=20019340,
        last_flag_2=20019341,
        first_flag_3=20019350,
        last_flag_3=20019355,
        first_flag_4=20019400,
        last_flag_4=20019403,
        first_flag_5=20019500,
        last_flag_5=20019549,
        first_flag_6=20012711,
        last_flag_6=20012718,
        first_flag_7=20012720,
        last_flag_7=20012799,
    )
    Event_20010739(0, flag=7630)
    Event_20010770(
        0,
        flag=20019294,
        flag_1=20019500,
        flag_2=20019501,
        flag_3=20019502,
        flag_4=20019503,
        flag_5=20019504,
        seconds=30.0,
        seconds_1=120.0,
        seconds_2=120.0,
        seconds_3=120.0,
        flag_6=20012149,
        flag_7=20019531,
        first_flag=20012783,
        last_flag=20012787,
        flag_8=20012791,
        flag_9=7630,
        flag_10=20019514,
        flag_11=20019513,
        flag_12=20019535,
        flag_13=20019515,
        flag_14=20019536,
        flag_15=20019516,
        flag_16=20019517,
    )
    Event_20010771(
        0,
        flag=20019500,
        flag_1=20019501,
        flag_2=20019502,
        flag_3=20019503,
        flag_4=20019504,
        flag_5=20012792,
        flag_6=20012793,
        flag_7=20012794,
        flag_8=20012795,
        flag_9=20012796,
        flag_10=20012785,
        flag_11=20012787,
        flag_12=20012786,
        flag_13=20012149,
        flag_14=7630,
    )
    Event_20010772(
        0,
        flag=20019505,
        flag_1=20019506,
        flag_2=20012797,
        flag_3=20012798,
        flag_4=20012799,
        flag_5=20012788,
        flag_6=20012789,
        flag_7=20012790,
        flag_8=20012149,
        flag_9=7630,
    )
    Event_20010773(
        0,
        flag=20019523,
        flag_1=20019524,
        flag_2=20019525,
        flag_3=20019526,
        flag_4=20019527,
        seconds=20.0,
        seconds_1=110.0,
        seconds_2=110.0,
        seconds_3=110.0,
        first_flag=20012783,
        last_flag=20012787,
        flag_5=20019531,
        flag_6=20019532,
        flag_7=7630,
        flag_8=20019513,
        flag_9=20019536,
        flag_10=20019535,
        flag_11=20019515,
        flag_12=20019514,
        flag_13=20019540,
        flag_14=20019541,
        flag_15=20019542,
    )
    Event_20010774(0, flag=20019507)
    Event_20010775(
        0,
        character=20010720,
        flag=20012783,
        character_1=20010724,
        flag_1=20012784,
        character_2=20010722,
        flag_2=20012785,
        character_3=20010723,
        flag_3=20012786,
        character_4=20010721,
        flag_4=20012787,
        flag_5=4929,
        flag_6=20012149,
        flag_7=20012791,
        flag_8=7630,
    )
    Event_20010776(0, flag=7630, character=20010720)
    Event_20010777(0, first_flag=20012788, last_flag=20012790, flag=20019403, flag_1=20012791, flag_2=7630)
    Event_20010778(
        0,
        character=20010720,
        character_1=20010724,
        character_2=20010722,
        character_3=20010723,
        character_4=20010721,
        flag=20012783,
        flag_1=20012784,
        flag_2=20012785,
        flag_3=20012786,
        flag_4=20012787,
        first_flag=20019508,
        flag_5=20019509,
        flag_6=20019510,
        flag_7=20019511,
        last_flag=20019512,
        flag_8=20019513,
        value=0.5,
        flag_9=7630,
        flag_10=20012791,
        flag_11=20019535,
    )
    Event_20010780(
        0,
        flag=20019505,
        flag_1=20019501,
        seconds=20.0,
        first_flag=20012788,
        last_flag=20012790,
        flag_2=7630,
        value=1,
        flag_3=20019536,
        flag_4=20019543,
        flag_5=20019533,
    )
    Event_20010781(
        0,
        flag=20019506,
        flag_1=20019502,
        seconds=20.0,
        first_flag=20012788,
        last_flag=20012790,
        flag_2=7630,
        value=2,
        first_flag_1=20012783,
        last_flag_1=20012787,
        flag_3=20019505,
        flag_4=20019536,
        flag_5=20012791,
        flag_6=20019544,
        flag_7=20019533,
    )
    Event_20010782(
        0,
        flag=20019523,
        flag_1=20019524,
        flag_2=20019525,
        flag_3=20019526,
        flag_4=20019527,
        flag_5=20019528,
        flag_6=20019529,
        flag_7=20019530,
        seconds=5.0,
        flag_8=20019536,
        flag_9=20019537,
        flag_10=7630,
    )
    Event_20010783(
        0,
        flag=20019501,
        seconds=10.0,
        first_flag=20012788,
        last_flag=20012790,
        flag_1=7630,
        value=1,
        flag_2=20019532,
        flag_3=20019540,
        flag_4=20019541,
        flag_5=20019542,
        flag_6=20012788,
        flag_7=20012789,
        flag_8=20012790,
        flag_9=20019528,
        flag_10=20019529,
        flag_11=20019530,
    )
    Event_20010784(
        0,
        flag=20019529,
        flag_1=20019502,
        seconds=10.0,
        first_flag=20012788,
        last_flag=20012790,
        flag_2=7630,
        value=2,
        first_flag_1=20012783,
        last_flag_1=20012787,
        flag_3=20019505,
        flag_4=20019532,
        flag_5=20019540,
        flag_6=20019541,
        flag_7=20019542,
        flag_8=20012791,
    )
    Event_20010371(
        0,
        region=20012780,
        region_1=20012781,
        region_2=20012782,
        region_3=20012783,
        region_4=20012784,
        flag=20012765,
        flag_1=20012766,
        flag_2=20012767,
        flag_3=20012768,
        flag_4=20012769,
        flag_5=7630,
    )
    Event_20010785(0, character=20010720, text=4080922, flag=20012148, seconds=6.0)
    Event_20010785(1, character=20010724, text=4080932, flag=20012148, seconds=6.0)
    Event_20010785(2, character=20010722, text=4080892, flag=20012148, seconds=6.0)
    Event_20010785(3, character=20010723, text=4080902, flag=20012148, seconds=6.0)
    Event_20010785(4, character=20010721, text=4080912, flag=20012148, seconds=6.0)
    Event_20010785(5, character=20010730, text=4080842, flag=20012148, seconds=6.0)
    Event_20010785(6, character=20010731, text=4080852, flag=20012148, seconds=6.0)
    Event_20010785(7, character=20010732, text=4080862, flag=20012148, seconds=6.0)
    Event_20010793(0, flag=7630, flag_1=20019507)
    Event_20010740(0, character=20010700, flag=4400, flag_1=4407, animation_id=90100, flag_2=4899)
    Event_20010741(0, flag=20012168, flag_1=20019224, flag_2=7625)
    Event_20010742(0, flag=20012160, flag_1=20019226, flag_2=20010800)
    Event_20010743(0, character=20010700, flag=4400, flag_1=20012160, flag_2=4408, flag_3=20010800)
    Event_20010744(0, flag=20019228, flag_1=20019227, flag_2=20010800)
    Event_20010745(0, flag=20012172, flag_1=20019306, flag_2=7625)
    Event_20010746(0, flag=20012164, flag_1=20019311, flag_2=20010800)
    CommonFunc_90005748(0, entity=20011760, action_button_id=206020, text=1030028, display_distance=30.0, flag=4918)
    Event_20010760(0, character=20010770, flag=4928, flag_1=4902, animation_id=90100, distance=110.0)
    Event_20010761(
        0,
        character=20011770,
        character_1=20010770,
        flag=4928,
        flag_1=20012710,
        flag_2=4902,
        flag_3=20019257,
        flag_4=4893,
        flag_5=4894,
        flag_6=20012780,
        flag_7=20012781,
        flag_8=20012782,
    )
    Event_20010762(0, flag=4928, flag_1=20012140)
    CommonFunc_90005770(0, flag=4902)
    Event_20010763(0, character=20010790, flag=20010800, character_1=20010800)
    Event_20010750(0, character=20010740, flag=4440, flag_1=4448, animation_id=90102)
    CommonFunc_90005750(
        0,
        asset=20011740,
        action_button_id=4350,
        item_lot=105940,
        first_flag=400598,
        last_flag=400598,
        flag=4448,
        vfx_id=6102,
    )
    Event_20010750(1, character=20010741, flag=4420, flag_1=4427, animation_id=90102)
    CommonFunc_90005750(
        0,
        asset=20011741,
        action_button_id=4350,
        item_lot=106010,
        first_flag=400602,
        last_flag=400602,
        flag=4427,
        vfx_id=6102,
    )
    Event_20010750(2, character=20010742, flag=4360, flag_1=4370, animation_id=90103)
    CommonFunc_90005750(
        0,
        asset=20011742,
        action_button_id=4350,
        item_lot=116100,
        first_flag=400614,
        last_flag=400614,
        flag=4370,
        vfx_id=0,
    )
    Event_20010750(4, character=20010751, flag=4460, flag_1=4469, animation_id=90104)
    CommonFunc_90005750(
        0,
        asset=20011751,
        action_button_id=4350,
        item_lot=106320,
        first_flag=400634,
        last_flag=400634,
        flag=4469,
        vfx_id=6102,
    )
    Event_20010750(5, character=20010743, flag=4380, flag_1=4387, animation_id=90103)
    CommonFunc_90005750(
        0,
        asset=20011743,
        action_button_id=4350,
        item_lot=116400,
        first_flag=400644,
        last_flag=400645,
        flag=4387,
        vfx_id=6102,
    )
    Event_20010750(6, character=20010744, flag=4560, flag_1=4566, animation_id=90101)
    CommonFunc_90005750(
        0,
        asset=20011744,
        action_button_id=4350,
        item_lot=107310,
        first_flag=400732,
        last_flag=400732,
        flag=4566,
        vfx_id=0,
    )
    Event_20010750(7, character=20010750, flag=4400, flag_1=4408, animation_id=90102)
    CommonFunc_90005750(
        0,
        asset=20011750,
        action_button_id=4350,
        item_lot=106220,
        first_flag=400624,
        last_flag=400624,
        flag=4408,
        vfx_id=6102,
    )
    CommonFunc_90005715(0, character=20010800, character_1=0, flag=20010800, flag_1=20012805, distance=150.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_20010519()
    Event_20012144()
    CommonFunc_90005301(0, flag=20010455, character=20010455, item_lot__unk1=20011991, seconds=0.0, unk1=2)
    CommonFunc_90005261(0, character=20010215, region=20012215, radius=2.0, seconds=0.0, animation_id=3002)
    CommonFunc_90005261(0, character=20010216, region=20012215, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010217, region=20012215, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010218, region=20012215, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010219, region=20012215, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010300, region=20012300, radius=2.0, seconds=0.0, animation_id=3005)
    CommonFunc_90005211(
        0,
        character=20010301,
        animation_id=30005,
        animation_id_1=20005,
        region=20012303,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20010302,
        animation_id=30005,
        animation_id_1=20005,
        region=20012303,
        radius=0.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20010303,
        animation_id=30005,
        animation_id_1=20005,
        region=20012303,
        radius=0.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20010309,
        animation_id=30002,
        animation_id_1=20002,
        region=20012308,
        radius=0.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=20010304, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=20010305, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=20010306,
        animation_id=30002,
        animation_id_1=20002,
        region=20012306,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=20010307,
        animation_id=30002,
        animation_id_1=20002,
        region=20012306,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=20010330,
        region=20012330,
        radius=0.0,
        seconds=1.2999999523162842,
        animation_id=3009,
    )
    CommonFunc_90005211(
        0,
        character=20010331,
        animation_id=30000,
        animation_id_1=20000,
        region=20012331,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=20010332, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005261(
        0,
        character=20010333,
        region=20012333,
        radius=0.0,
        seconds=0.30000001192092896,
        animation_id=3009,
    )
    CommonFunc_90005211(
        0,
        character=20010334,
        animation_id=30001,
        animation_id_1=20001,
        region=20012334,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20010351, region=20012351, radius=0.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005251(0, character=20010352, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=20010355, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=20010364,
        animation_id=30000,
        animation_id_1=20000,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20010356, region=20012356, radius=3.0, seconds=2.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010357, region=20012356, radius=3.0, seconds=1.5, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=20010365,
        region=20012356,
        radius=3.0,
        seconds=0.10000000149011612,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=20010366,
        region=20012356,
        radius=3.0,
        seconds=0.10000000149011612,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=20010367, region=20012356, radius=3.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=20010368,
        region=20012356,
        radius=3.0,
        seconds=0.20000000298023224,
        animation_id=-1,
    )
    CommonFunc_90005261(0, character=20010369, region=20012356, radius=3.0, seconds=0.4000000059604645, animation_id=-1)
    CommonFunc_90005261(0, character=20010360, region=20012360, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010361, region=20012360, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010371, region=20012371, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010375, region=20012375, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=20010377,
        animation_id=30000,
        animation_id_1=20000,
        region=20012377,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=20010402, region=20012402, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010450, region=20012450, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010451, region=20012451, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010452, region=20012452, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010453, region=20012453, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010455, region=20012455, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=20010470, region=20012470, radius=1.0, seconds=0.0, animation_id=-1)


@ContinueOnRest(20010197)
def Event_20010197():
    """Event 20010197"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(20010197):
        return
    AND_1.Add(FlagEnabled(20010196))
    AND_1.Add(FlagEnabled(330))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 63010)
    CreateTemporaryVFX(vfx_id=820685, anchor_entity=PLAYER, dummy_id=900, anchor_type=CoordEntityType.Character)
    EnableFlag(20010197)
    RemoveGoodFromPlayer(item=2008021, quantity=1)
    End()


@ContinueOnRest(20010199)
def Event_20010199():
    """Event 20010199"""
    GotoIfPlayerInOwnWorld(Label.L0)
    DisableAsset(20011199)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(20011199)
    DeleteAssetVFX(20011199)
    if FlagEnabled(128):
        return
    AND_1.Add(FlagEnabled(20010800))
    
    MAIN.Await(AND_1)
    
    EnableAsset(20011199)
    DeleteAssetVFX(20011199)
    CreateAssetVFX(20011199, dummy_id=100, vfx_id=820680)
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(Multiplayer())
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButtonParamActivated(action_button_id=209600, entity=20011199))
    
    MAIN.Await(AND_1)
    
    EnableFlag(20010199)
    EnableFlag(20012199)
    FaceEntityAndForceAnimation(PLAYER, 20011199, wait_for_completion=True)
    ForceAnimation(PLAYER, 61030)
    WaitRealFrames(frames=100)
    CreateAssetVFX(20011199, dummy_id=100, vfx_id=820681)
    Character_Unknown_2004_85(
        character=1065353216,
        unk1=1086324736,
        unk2=1,
        unk3=0,
        unk4=1063675494,
        unk5=1063675494,
        unk6=1063675494,
    )
    Wait(6.0)
    DeleteAssetVFX(20011199, erase_root=False)
    Wait(0.6000000238418579)
    PlayCutscene(
        20010020,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16 | CutsceneFlags.Unknown32,
        player_id=10000,
    )
    CreateTemporaryVFX(vfx_id=820682, anchor_entity=20011199, dummy_id=100, anchor_type=CoordEntityType.Asset)
    WaitRealFrames(frames=60)
    ForceAnimation(PLAYER, 61032)
    WaitRealFrames(frames=60)
    AwardItemLot(20011981, host_only=True)
    EnableFlag(128)
    End()


@RestartOnRest(20012144)
def Event_20012144():
    """Event 20012144"""
    DisableNetworkSync()
    GotoIfCeremonyActive(Label.L10, ceremony=20)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    if FlagEnabled(7625):
        EnableNetworkFlag(20012149)
        Goto(Label.L1)
    DisableNetworkFlag(20012149)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(7630)
    DisableFlag(7631)
    DisableFlag(7632)
    DisableFlag(7640)
    DisableFlag(7641)
    DisableFlag(7642)
    DisableFlag(7643)
    DisableFlag(7644)
    DisableFlag(7645)
    DisableFlag(7646)
    DisableFlag(7647)
    DisableFlag(7648)
    DisableFlag(7649)
    DisableFlag(20012168)
    DisableFlag(20012172)
    DisableFlag(20012176)
    EnableAsset(20011148)
    DeleteAssetVFX(20011148)
    CreateAssetVFX(20011148, dummy_id=101, vfx_id=806761)
    DisableAsset(20011775)
    DeleteAssetVFX(20011776)
    DisableAsset(20011776)
    OR_1.Add(FlagEnabled(20012149))
    
    MAIN.Await(OR_1)
    
    DeleteAssetVFX(20011148)
    DisableAsset(20011148)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagDisabled(Label.L11, flag=7630)
    if FlagEnabled(7640):
        EnableNetworkFlag(4890)
    if FlagEnabled(7641):
        EnableNetworkFlag(4891)
    if FlagEnabled(7642):
        EnableNetworkFlag(4892)
    if FlagEnabled(7643):
        EnableNetworkFlag(4895)
    if FlagEnabled(7644):
        EnableNetworkFlag(4908)
    if FlagEnabled(7645):
        EnableNetworkFlag(20012168)
    if FlagEnabled(7646):
        EnableNetworkFlag(20012172)
    if FlagEnabled(7647):
        EnableNetworkFlag(20012176)
    if FlagEnabled(7648):
        EnableNetworkFlag(12059262)
    if FlagEnabled(7649):
        EnableNetworkFlag(2048459275)
    if FlagEnabled(7631):
        EnableNetworkFlag(20012190)
    if FlagEnabled(7632):
        EnableNetworkFlag(20012191)

    # --- Label 11 --- #
    DefineLabel(11)
    EnableFlag(20012148)
    DeleteAssetVFX(20011775)
    DeleteAssetVFX(20011776)
    CreateAssetVFX(20011775, dummy_id=101, vfx_id=806761)
    CreateAssetVFX(20011776, dummy_id=101, vfx_id=806761)
    SetBossMusic(bgm_boss_conv_param_id=944000, state=BossMusicState.Start)
    End()


@RestartOnRest(20012145)
def Event_20012145(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
    message: EventText | int,
    action_button_id: int,
    asset: uint,
    vfx_id: int,
):
    """Event 20012145"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DeleteAssetVFX(asset)
    if FlagEnabled(flag):
        return
    if FlagEnabled(20012149):
        return
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(InvasionPending())
    OR_1.Add(Invasion())
    AND_1.Add(not OR_1)
    
    MAIN.Await(AND_1)
    
    CreateAssetVFX(asset, dummy_id=100, vfx_id=vfx_id)
    OR_2.Add(Invasion())
    OR_2.Add(InvasionPending())
    OR_3.Add(OR_2)
    OR_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_3.Add(FlagDisabled(flag_2))
    
    MAIN.Await(OR_3)
    
    if LastResult(OR_2):
        return RESTART
    if FlagDisabled(flag_2):
        return RESTART
    AwaitDialogResponse(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=2.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagDisabled(left_flag):
        return RESTART
    EnableFlag(flag_1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    EnableFlag(7630)
    if FlagEnabled(4890):
        EnableFlag(7640)
    if FlagEnabled(4891):
        EnableFlag(7641)
    if FlagEnabled(4892):
        EnableFlag(7642)
    if FlagEnabled(4895):
        EnableFlag(7643)
    if FlagEnabled(4908):
        EnableFlag(7644)
    if FlagEnabled(20012168):
        EnableFlag(7645)
    if FlagEnabled(20012172):
        EnableFlag(7646)
    if FlagEnabled(20012176):
        EnableFlag(7647)
    if FlagEnabled(12059262):
        EnableFlag(7648)
    if FlagEnabled(2048459275):
        EnableFlag(7649)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitRealFrames(frames=30)
    AddSpecialEffect(PLAYER, 15)
    SkipLinesIfCoopClientCountComparison(5, comparison_type=ComparisonType.Equal, value=0)
    SkipLinesIfCoopClientCountComparison(1, comparison_type=ComparisonType.Equal, value=1)
    SkipLinesIfCoopClientCountComparison(2, comparison_type=ComparisonType.Equal, value=2)
    EnableFlag(7631)
    SkipLines(1)
    EnableFlag(7632)
    Wait(10.0)
    Restart()


@RestartOnRest(20012146)
def Event_20012146(_, flag: Flag | int, character: Character | int, banner_type: uchar, region: Region | int):
    """Event 20012146"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        return
    AND_1.Add(FlagEnabled(4929))
    
    MAIN.Await(AND_1)
    
    Kill(character)
    Wait(3.0)
    if FlagEnabled(7630):
        EnableFlag(flag)
        AwardItemLot(10420, host_only=True)
    DisplayBanner(banner_type)
    SetBossMusic(bgm_boss_conv_param_id=944000, state=BossMusicState.NormalFadeOut)
    Wait(10.0)
    if UnsignedNotEqual(left=region, right=0):
        SetPseudoMultiplayerReturnPosition(region=region)
    AddSpecialEffect(ALL_PLAYERS, 20004820)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(20012195)
def Event_20012195():
    """Event 20012195"""
    SetTeamType(20010195, TeamType.Enemy)
    
    MAIN.Await(FlagEnabled(20012102))
    
    SetTeamType(ALL_SPIRIT_SUMMONS, TeamType.Enemy)


@RestartOnRest(20012150)
def Event_20012150(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    character: uint,
    asset: uint,
    flag_3: Flag | int,
    action_button_id: int,
    message: EventText | int,
    text: EventText | int,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 20012150"""
    DisableNetworkSync()
    if PlayerInOwnWorld():
        GotoIfFlagDisabled(Label.L10, flag=flag_3)
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    if FlagEnabled(flag_1):
        DisableCharacter(character)
        End()
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    DisableAnimations(character)
    EnableImmortality(character)
    DisableAI(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    RemoveSpecialEffect(character, 18677)
    AddSpecialEffect(character, 20004380)
    if PlayerInOwnWorld():
        DeleteAssetVFX(asset)
        CreateAssetVFX(asset, dummy_id=100, vfx_id=30001)
    GotoIfPlayerNotInOwnWorld(Label.L18)
    AND_1.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(flag_3))
    AND_3.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=asset))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(Invasion())
    OR_1.Add(InvasionPending())
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    OR_11.Add(Invasion())
    OR_11.Add(InvasionPending())
    GotoIfConditionTrue(Label.L10, input_condition=OR_11)
    Goto(Label.L20)

    # --- Label 18 --- #
    DefineLabel(18)
    AND_1.Add(PlayerNotInOwnWorld())
    AND_3.Add(FlagEnabled(left_flag))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    OR_11.Add(Invasion())
    OR_11.Add(InvasionPending())
    GotoIfConditionTrue(Label.L10, input_condition=OR_11)
    Goto(Label.L19)

    # --- Label 20 --- #
    DefineLabel(20)
    AwaitDialogResponse(
        message=message,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=asset,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    if FlagDisabled(left_flag):
        RemoveSpecialEffect(character, 20004380)
        AddSpecialEffect(character, 18677)
        DeleteAssetVFX(asset)
        Wait(0.5)
        Restart()
    EnableNetworkFlag(left_flag)

    # --- Label 19 --- #
    DefineLabel(19)
    Wait(1.5)
    DisplayNetworkMessage(text=text, unk_4_5=False)
    EnableFlag(flag_1)
    RemoveSpecialEffect(character, 20004380)
    AddSpecialEffect(character, 18677)
    DeleteAssetVFX(asset)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DeleteAssetVFX(asset)
    AND_12.Add(FlagEnabled(flag_3))
    OR_12.Add(Invasion())
    OR_12.Add(InvasionPending())
    AND_12.Add(not OR_12)
    
    MAIN.Await(AND_12)
    
    Restart()


@RestartOnRest(20012155)
def Event_20012155(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, other_entity: uint, character: uint):
    """Event 20012155"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=1.5))
    OR_10.Add(Invasion())
    OR_10.Add(InvasionPending())
    AND_1.Add(not OR_10)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAI(character)
    WaitFrames(frames=1)
    DisableAnimations(character)
    WaitFrames(frames=1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=1.5))
    OR_2.Add(AND_2)
    OR_2.Add(Invasion())
    OR_2.Add(InvasionPending())
    OR_2.Add(FlagDisabled(flag_2))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(20012200)
def Event_20012200(
    _,
    character: Character | int,
    special_effect: int,
    special_effect_1: int,
    weather: char,
    special_effect_2: int,
    character_1: Character | int,
    special_effect_3: int,
    character_2: Character | int,
    special_effect_4: int,
):
    """Event 20012200"""
    AND_10.Add(HealthRatio(character) > 0.0)
    GotoIfConditionTrue(Label.L0, input_condition=AND_10)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect):
        SetWeather(weather=weather, duration=-1.0, immediate_change=False)
        AddSpecialEffect(PLAYER, special_effect_2)
    OR_1.Add(CharacterHasSpecialEffect(character_1, special_effect_3))
    OR_1.Add(CharacterHasSpecialEffect(character_2, special_effect_4))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_6.Add(AND_1)
    OR_2.Add(HealthRatio(character) <= 0.0)
    OR_6.Add(OR_2)
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_3.Add(not OR_3)
    AND_3.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_6.Add(AND_3)
    AND_4.Add(CharacterHasSpecialEffect(character, 20011883))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, special_effect))
    OR_6.Add(AND_4)
    OR_5.Add(WeatherState(weather=weather, unk_4_8=0.0, unk_8_12=0.0))
    AND_5.Add(not OR_5)
    AND_5.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_6.Add(AND_5)
    AND_6.Add(OR_6)
    AND_7.Add(WeatherState(weather=Weather.FlatClouds, unk_4_8=0.0, unk_8_12=0.0))
    AND_6.Add(not AND_7)
    
    MAIN.Await(AND_6)
    
    OR_11.Add(CharacterHasSpecialEffect(character_1, special_effect_3))
    OR_11.Add(CharacterHasSpecialEffect(character_2, special_effect_4))
    AND_11.Add(OR_11)
    AND_11.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_11.Add(WeatherState(weather=weather, unk_4_8=0.0, unk_8_12=0.0))
    SkipLinesIfConditionFalse(4, AND_11)
    AddSpecialEffect(character, special_effect_1)
    RemoveSpecialEffect(PLAYER, special_effect_2)
    Wait(15.0)
    Restart()
    OR_12.Add(HealthRatio(character) <= 0.0)
    SkipLinesIfConditionFalse(5, OR_12)
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect):
        SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    AddSpecialEffect(character, special_effect_1)
    RemoveSpecialEffect(PLAYER, special_effect_2)
    End()
    OR_13.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_13.Add(not OR_13)
    AND_13.Add(CharacterHasSpecialEffect(character, special_effect))
    SkipLinesIfConditionFalse(6, AND_13)
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect):
        SetWeather(weather=Weather.Default, duration=-1.0, immediate_change=False)
    AddSpecialEffect(character, special_effect_1)
    RemoveSpecialEffect(PLAYER, special_effect_2)
    Wait(15.0)
    Restart()
    OR_14.Add(WeatherState(weather=weather, unk_4_8=0.0, unk_8_12=0.0))
    AND_14.Add(not OR_14)
    AND_14.Add(CharacterHasSpecialEffect(character, special_effect))
    SkipLinesIfConditionFalse(2, AND_14)
    SetWeather(weather=weather, duration=-1.0, immediate_change=False)
    AddSpecialEffect(PLAYER, special_effect_2)
    Restart()


@RestartOnRest(20012210)
def Event_20012210(_, entity: uint, region: Region | int):
    """Event 20012210"""
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    ForceAnimation(entity, 3000, wait_for_completion=True)
    Wait(4.0)
    Restart()


@ContinueOnRest(20012500)
def Event_20012500():
    """Event 20012500"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(20010500):
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=20012500))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=20002500))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(330))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(FlagEnabled(9000))
    OR_2.Add(AND_2)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=20012500))
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=20002500))
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(PLAYER, 4281)
    AddSpecialEffect(PLAYER, 4283)
    EnableFlag(20010500)


@ContinueOnRest(20012510)
def Event_20012510():
    """Event 20012510"""
    CommonFunc_90005500(
        0,
        flag=20010510,
        flag_1=20010511,
        left=0,
        asset=20011510,
        asset_1=20011511,
        obj_act_id=20013511,
        asset_2=20011512,
        obj_act_id_1=20013512,
        region=20012511,
        region_1=20012512,
        flag_2=20010512,
        flag_3=20010513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20010515,
        flag_1=20010516,
        left=0,
        asset=20011515,
        asset_1=20011516,
        obj_act_id=20013516,
        asset_2=20011517,
        obj_act_id_1=20013517,
        region=20012516,
        region_1=20012517,
        flag_2=20010517,
        flag_3=20010518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20010520,
        flag_1=20010521,
        left=0,
        asset=20011520,
        asset_1=20011521,
        obj_act_id=20013521,
        asset_2=20011522,
        obj_act_id_1=20013522,
        region=20012521,
        region_1=20012522,
        flag_2=20010522,
        flag_3=20010523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20010525,
        flag_1=20010526,
        left=0,
        asset=20011525,
        asset_1=20011526,
        obj_act_id=20013526,
        asset_2=20011527,
        obj_act_id_1=20013527,
        region=20012526,
        region_1=20012527,
        flag_2=20010527,
        flag_3=20010528,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20010530,
        flag_1=20010531,
        left=0,
        asset=20011530,
        asset_1=20011531,
        obj_act_id=20013531,
        asset_2=20011532,
        obj_act_id_1=20013532,
        region=20012531,
        region_1=20012532,
        flag_2=20010532,
        flag_3=20010533,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=20010535,
        flag_1=20010536,
        left=0,
        asset=20011535,
        asset_1=20011536,
        obj_act_id=20013536,
        asset_2=20011537,
        obj_act_id_1=20013537,
        region=20012536,
        region_1=20012537,
        flag_2=20010537,
        flag_3=20010538,
        left_1=0,
    )


@ContinueOnRest(20010519)
def Event_20010519():
    """Event 20010519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(20010510)
    DisableFlag(20010515)
    DisableFlag(20010520)
    EnableFlag(20010525)
    EnableFlag(20010530)
    DisableFlag(20010535)


@ContinueOnRest(20012580)
def Event_20012580():
    """Event 20012580"""
    RegisterLadder(start_climbing_flag=20010580, stop_climbing_flag=20010581, asset=20011580)
    RegisterLadder(start_climbing_flag=20010582, stop_climbing_flag=20010583, asset=20011582)


@ContinueOnRest(20010610)
def Event_20010610():
    """Event 20010610"""
    if ThisEventSlotFlagEnabled():
        return
    Move(20010375, destination=20012611, destination_type=CoordEntityType.Region, short_move=True)
    DisableGravity(20010375)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=20012610))
    
    MAIN.Await(AND_1)
    
    EnableGravity(20010375)
    if MapHasUpdatePermission(unk_state=False, game_map=(0, 0, 0, 0)):
        EnableNetworkFlag(20010515)


@RestartOnRest(20012800)
def Event_20012800():
    """Event 20012800"""
    if FlagEnabled(20010800):
        return
    
    MAIN.Await(HealthValue(20010800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(20018000, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(20010800))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9646))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(20010800))
    
    MAIN.Await(OR_2)
    
    KillBossAndDisplayBanner(character=20010800, banner_type=BannerType.GodSlain)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableNetworkFlag(20010800)
    EnableFlag(9143)
    if PlayerInOwnWorld():
        EnableFlag(61143)


@RestartOnRest(20012810)
def Event_20012810():
    """Event 20012810"""
    GotoIfFlagDisabled(Label.L0, flag=20010800)
    DisableCharacter(20015800)
    DisableAnimations(20015800)
    Kill(20015800)
    DisableCharacter(20010830)
    DisableAnimations(20010830)
    Kill(20010830)
    SetBackreadStateAlternate(20010830, False)
    SetTeamType(20010830, TeamType.NoTeam)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(20015800)
    DisableGravity(20010800)
    DisableAnimations(20010800)
    DisableHealthBar(20010800)
    EnableImmortality(20010801)
    DisableCharacter(20015810)
    DisableAnimations(20015810)
    DisableAnimations(20010830)
    DisableGravity(20010830)
    SetLockOnPoint(character=20010830, lock_on_dummy_id=220, state=False)
    SetTeamType(20010830, TeamType.NoTeam)
    DisableAI(20010830)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=20010801)
    ForceAnimation(20010801, 30010)
    AND_1.Add(FlagEnabled(20012805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=20012800))
    
    MAIN.Await(AND_1)
    
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=20010000,
            cutscene_flags=0,
            move_to_region=20012811,
            map_id=20010000,
            player_id=10000,
            unk_20_24=20010000,
            unk_24_25=False,
        )
    else:
        PlayCutscene(20010000, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    EnableNetworkFlag(20010801)
    DeactivateGparamOverride(change_duration=0.0)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-2.7899999618530273, y_angle=116.75)
    Move(20010801, destination=20012812, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(20010801, 20010)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(20010801, destination=20012814, destination_type=CoordEntityType.Region, short_move=True)
    AND_2.Add(FlagEnabled(20012805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=20012800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    ReferDamageToEntity(20010801, target_entity=20010800)
    EnableAI(20010801)
    SetNetworkUpdateRate(20010801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(20010801, name=905220000)


@RestartOnRest(20012811)
def Event_20012811():
    """Event 20012811"""
    if FlagEnabled(20010800):
        return
    AND_1.Add(HealthRatio(20010801) <= 0.6499999761581421)
    
    MAIN.Await(AND_1)
    
    EnableFlag(20012841)
    WaitRealFrames(frames=1)
    DisableAnimations(20010801)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=20010010,
            cutscene_flags=0,
            move_to_region=20012815,
            map_id=20010000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
    else:
        PlayCutscene(20010010, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=6.0, y_angle=116.56999969482422)
    EnableFlag(20012802)
    DisableCharacter(20010801)
    EnableCharacter(20010800)
    EnableAI(20010800)
    EnableAnimations(20010800)
    EnableGravity(20010800)
    Move(20010800, destination=20012816, destination_type=CoordEntityType.Region, short_move=True)
    EnableBossHealthBar(20010800, name=905220001)
    ForceAnimation(20010800, 20011)


@RestartOnRest(20012820)
def Event_20012820():
    """Event 20012820"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 19680))
    
    EnableFlag(20012820)


@ContinueOnRest(20012830)
def Event_20012830(_, character: uint, special_effect: int, special_effect_1: int):
    """Event 20012830"""
    if FlagEnabled(20010800):
        return
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    AND_1.Add(CharacterHasSpecialEffect(20010800, special_effect))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    WaitFrames(frames=1)
    if CharacterHasSpecialEffect(character=20010800, special_effect=20011588):
        Move(
            character,
            destination=20010800,
            destination_type=CoordEntityType.Character,
            dummy_id=228,
            copy_draw_parent=20010800,
        )
        ForceAnimation(character, 20002)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20010800, special_effect=20011589):
        Move(
            character,
            destination=20010800,
            destination_type=CoordEntityType.Character,
            dummy_id=228,
            copy_draw_parent=20010800,
        )
        ForceAnimation(character, 20003)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20010800, special_effect=20011590):
        Move(
            character,
            destination=20010800,
            destination_type=CoordEntityType.Character,
            dummy_id=228,
            copy_draw_parent=20010800,
        )
        ForceAnimation(character, 20004)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20010800, special_effect=20011591):
        Move(
            character,
            destination=20010800,
            destination_type=CoordEntityType.Character,
            dummy_id=228,
            copy_draw_parent=20010800,
        )
        ForceAnimation(character, 20005)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=20010800, special_effect=20011592):
        Move(
            character,
            destination=20010800,
            destination_type=CoordEntityType.Character,
            dummy_id=228,
            copy_draw_parent=20010800,
        )
        ForceAnimation(character, 20006)
        Goto(Label.L1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(9, character=20010800, special_effect=20011593)
    SkipLinesIfUnsignedNotEqual(1, left=20010810, right=character)
    ForceAnimation(character, 20007)
    SkipLinesIfUnsignedNotEqual(1, left=20010811, right=character)
    ForceAnimation(character, 20008)
    SkipLinesIfUnsignedNotEqual(1, left=20010812, right=character)
    ForceAnimation(character, 20009)
    SkipLinesIfUnsignedNotEqual(1, left=20010813, right=character)
    ForceAnimation(character, 20013)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    EnableAnimations(character)
    AND_5.Add(CharacterHasSpecialEffect(character, special_effect_1))
    
    MAIN.Await(AND_5)
    
    Restart()


@RestartOnRest(20012835)
def Event_20012835():
    """Event 20012835"""
    if FlagEnabled(20010800):
        return
    AND_1.Add(CharacterHasSpecialEffect(20010800, 20011572))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    DisableAI(20010800)
    DisableCharacter(20010800)
    DisableAnimations(20010800)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(20010800, authority_level=UpdateAuthority.Forced)
    if CharacterInsideRegion(character=PLAYER, region=20012833):
        Move(20010830, destination=20012823, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
        FaceEntityAndForceAnimation(20010830, 20012822, wait_for_completion=True)
        FaceEntityAndForceAnimation(20010830, 20012822, wait_for_completion=True)
        Goto(Label.L1)
    if CharacterInsideRegion(character=PLAYER, region=20012830):
        Move(
            20010830,
            destination=PLAYER,
            destination_type=CoordEntityType.Character,
            dummy_id=235,
            copy_draw_parent=PLAYER,
        )
        FaceEntityAndForceAnimation(20010830, 20012820, wait_for_completion=True)
        FaceEntityAndForceAnimation(20010830, 20012820, wait_for_completion=True)
        Goto(Label.L1)
    if CharacterInsideRegion(character=PLAYER, region=20012831):
        Move(
            20010830,
            destination=PLAYER,
            destination_type=CoordEntityType.Character,
            dummy_id=235,
            copy_draw_parent=PLAYER,
        )
        FaceEntityAndForceAnimation(20010830, 20012821, wait_for_completion=True)
        FaceEntityAndForceAnimation(20010830, 20012821, wait_for_completion=True)
        Goto(Label.L1)
    if CharacterInsideRegion(character=PLAYER, region=20012832):
        Move(
            20010830,
            destination=PLAYER,
            destination_type=CoordEntityType.Character,
            dummy_id=235,
            copy_draw_parent=PLAYER,
        )
        FaceEntityAndForceAnimation(20010830, 20012822, wait_for_completion=True)
        FaceEntityAndForceAnimation(20010830, 20012822, wait_for_completion=True)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(20010800)
    EnableAnimations(20010800)
    EnableAI(20010800)
    ForceAnimation(20010800, 3024)
    Wait(0.4000000059604645)
    Move(
        20010800,
        destination=20010830,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=20010830,
    )
    Move(
        20010810,
        destination=20010830,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=20010830,
    )
    Move(
        20010811,
        destination=20010830,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=20010830,
    )
    Move(
        20010812,
        destination=20010830,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=20010830,
    )
    Move(
        20010813,
        destination=20010830,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=20010830,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(20012840)
def Event_20012840():
    """Event 20012840"""
    DisableNetworkSync()
    if FlagEnabled(20010800):
        return
    AND_2.Add(FlagEnabled(20012841))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=20012840))
    
    MAIN.Await(AND_2)
    
    SetWeather(weather=Weather.FlatClouds, duration=-1.0, immediate_change=True)
    OR_3.Add(CharacterOutsideRegion(character=PLAYER, region=20012840))
    OR_3.Add(FlagEnabled(20010800))
    
    MAIN.Await(OR_3)
    
    SetWeather(weather=Weather.Default, duration=0.10000000149011612, immediate_change=False)
    Restart()


@RestartOnRest(20012847)
def Event_20012847():
    """Event 20012847"""
    DisableNetworkSync()
    if FlagEnabled(20010801):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=20012847))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(20010801):
        return
    ActivateGparamOverride(gparam_sub_id=4, change_duration=3.0)
    OR_2.Add(CharacterOutsideRegion(character=PLAYER, region=20012847))
    OR_2.Add(FlagEnabled(20010801))
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(20010801):
        return
    DeactivateGparamOverride(change_duration=3.0)
    Restart()


@RestartOnRest(20012849)
def Event_20012849():
    """Event 20012849"""
    CommonFunc_9005800(
        0,
        flag=20010800,
        entity=20011800,
        region=20012800,
        flag_1=20012805,
        character=20015800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=20010800,
        entity=20011800,
        region=20012800,
        flag_1=20012805,
        flag_2=20012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=20010800, asset=20011800, vfx_id=1590, right=0)
    CommonFunc_9005811(0, flag=20010800, asset=20011801, vfx_id=0, right=0)
    CommonFunc_9005822(
        0,
        flag=20010800,
        bgm_boss_conv_param_id=522000,
        flag_1=20012805,
        flag_2=20012806,
        right=0,
        flag_3=20012802,
        left=0,
        left_1=0,
    )


@RestartOnRest(20012850)
def Event_20012850():
    """Event 20012850"""
    if FlagEnabled(20010850):
        return
    AND_1.Add(HealthValue(20010850) <= 0)
    AND_1.Add(HealthValue(20010851) <= 0)
    AND_1.Add(HealthValue(20010852) <= 0)
    AND_1.Add(HealthValue(20010853) <= 0)
    AND_1.Add(HealthValue(20010854) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    PlaySoundEffect(20010850, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(20010850))
    AND_2.Add(CharacterDead(20010851))
    AND_2.Add(CharacterDead(20010852))
    AND_2.Add(CharacterDead(20010853))
    AND_2.Add(CharacterDead(20010854))
    
    MAIN.Await(AND_2)
    
    KillBossAndDisplayBanner(character=20010850, banner_type=BannerType.GreatEnemyFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    EnableNetworkFlag(20010850)


@RestartOnRest(20012860)
def Event_20012860():
    """Event 20012860"""
    GotoIfFlagDisabled(Label.L0, flag=20010850)
    DisableCharacter(20015850)
    DisableAnimations(20015850)
    Kill(20015850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(20015850)
    GotoIfFlagEnabled(Label.L1, flag=20010851)
    AND_1.Add(FlagEnabled(20012855))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=20012851))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(20010851)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(20012855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=20012850))
    
    MAIN.Await(AND_2)

    # --- Label 10 --- #
    DefineLabel(10)
    EnableAI(20015850)
    SetNetworkUpdateRate(20015850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(20010850, name=141800)
    EnableBossHealthBar(20010851, name=142500, bar_slot=1)
    EnableBossHealthBar(20010852, name=141700, bar_slot=2)


@RestartOnRest(20012899)
def Event_20012899():
    """Event 20012899"""
    CommonFunc_9005800(
        0,
        flag=20010850,
        entity=20011850,
        region=20012850,
        flag_1=20012855,
        character=20015850,
        action_button_id=10000,
        left=20010851,
        region_1=20012851,
    )
    CommonFunc_9005801(
        0,
        flag=20010850,
        entity=20011850,
        region=20012850,
        flag_1=20012855,
        flag_2=20012856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=20010850, asset=20011850, vfx_id=3, right=20010851)
    CommonFunc_9005822(
        0,
        flag=20010850,
        bgm_boss_conv_param_id=931000,
        flag_1=20012855,
        flag_2=20012856,
        right=0,
        flag_3=20012852,
        left=0,
        left_1=0,
    )


@RestartOnRest(20010700)
def Event_20010700(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    text: EventText | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    seconds: float,
    right: int,
):
    """Event 20010700"""
    DisableNetworkSync()
    DisableCharacter(character)
    DisableBackread(character)
    if FlagEnabled(flag_1):
        return
    AwaitFlagEnabled(flag=flag_4)
    if FlagDisabled(flag_2):
        return
    EnableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(20012766))
    OR_2.Add(FlagEnabled(20012767))
    OR_2.Add(FlagEnabled(20012768))
    OR_2.Add(FlagEnabled(20012769))
    OR_3.Add(FlagEnabled(20012765))
    SkipLinesIfConditionFalse(2, OR_1)
    Move(character, destination=20012792, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    SkipLinesIfConditionFalse(2, OR_2)
    Move(character, destination=20012790, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    SkipLinesIfConditionFalse(2, OR_3)
    Move(character, destination=20012791, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableAnimations(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetTeamType(character, TeamType.Human)
    EnableAI(character)
    SkipLinesIfFlagEnabled(2, 20012190)
    SkipLinesIfFlagEnabled(3, 20012191)
    SkipLines(3)
    AddSpecialEffect(character, 7870)
    SkipLines(1)
    AddSpecialEffect(character, 7871)
    ForceAnimation(character, 63010)
    SetCharacterTalkRange(character=character, distance=distance)
    DisplayNetworkMessage(text=text, unk_4_5=False)
    if FlagEnabled(flag_8):
        EnableFlag(flag_9)
        DisableFlag(flag_8)
        Goto(Label.L2)
    if FlagEnabled(flag_7):
        EnableFlag(flag_8)
        DisableFlag(flag_7)
        Goto(Label.L2)
    if FlagEnabled(flag_6):
        EnableFlag(flag_7)
        DisableFlag(flag_6)
        Goto(Label.L2)
    if FlagEnabled(flag_5):
        EnableFlag(flag_6)
        DisableFlag(flag_5)
        Goto(Label.L2)
    EnableFlag(flag_5)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    if ValueNotEqual(left=0, right=right):
        Wait(seconds)
    EnableFlag(flag_3)
    if FlagEnabled(20019523):
        SetBossMusic(bgm_boss_conv_param_id=944000, state=BossMusicState.HeatUp)
    End()


@RestartOnRest(20010705)
def Event_20010705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    distance: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    text: EventText | int,
    text_1: EventText | int,
    flag_5: Flag | int,
    seconds: float,
    seconds_1: float,
    right: int,
):
    """Event 20010705"""
    DisableNetworkSync()
    DisableAI(character)
    DisableCharacter(character)
    if FlagEnabled(flag_1):
        DisableCharacter(character)
        DisableBackread(character)
        End()
    SetTeamType(character, TeamType.NoTeam)
    AwaitFlagEnabled(flag=flag_4)
    if FlagDisabled(flag_2):
        DisableCharacter(character)
        DisableBackread(character)
        End()
    EnableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(20012765))
    OR_1.Add(FlagEnabled(20012766))
    OR_1.Add(FlagEnabled(20012767))
    OR_2.Add(FlagEnabled(20012769))
    OR_3.Add(FlagEnabled(20012768))
    SkipLinesIfConditionFalse(2, OR_1)
    Move(character, destination=20012793, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    SkipLinesIfConditionFalse(2, OR_2)
    Move(character, destination=20012794, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    SkipLinesIfConditionFalse(2, OR_3)
    Move(character, destination=20012795, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(seconds)
    EnableCharacter(character)
    EnableAnimations(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetTeamType(character, TeamType.Enemy)
    EnableAI(character)
    ForceAnimation(character, 63010)
    SetCharacterTalkRange(character=character, distance=distance)
    RemoveSpecialEffect(character, 18677)
    RemoveSpecialEffect(character, 20004380)
    if FlagEnabled(flag_5):
        DisplayNetworkMessage(text=text, unk_4_5=False)
    else:
        DisplayNetworkMessage(text=text_1, unk_4_5=False)
    if ValueNotEqual(left=0, right=right):
        Wait(seconds_1)
    EnableFlag(flag_3)
    End()


@RestartOnRest(20010708)
def Event_20010708(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds: float,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 20010708"""
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_5):
        return
    AwaitFlagEnabled(flag=flag_4)
    if FlagDisabled(flag_1):
        return
    
    MAIN.Await(FlagEnabled(flag_2))
    
    EnableFlag(flag_3)
    Wait(seconds)
    DisableFlag(flag_3)
    End()


@RestartOnRest(20010711)
def Event_20010711(
    _,
    flag: Flag | int,
    character: uint,
    character_1: uint,
    radius: float,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    seconds_1: float,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    seconds_2: float,
    flag_6: Flag | int,
    flag_7: Flag | int,
    left: int,
    flag_8: Flag | int,
    flag_9: Flag | int,
):
    """Event 20010711"""
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_8):
        return
    AwaitFlagEnabled(flag=flag_5)
    if ValueNotEqual(left=left, right=0):
        AwaitFlagEnabled(flag=flag_7)
    if FlagEnabled(flag_2):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    AwaitFlagDisabled(flag=flag_6)
    OR_15.Add(EntityWithinDistance(entity=character_1, other_entity=character, radius=radius))
    OR_15.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_15)
    
    if FlagEnabled(flag_6):
        return RESTART
    OR_14.Add(HealthValue(character) == 0)
    OR_14.Add(HealthValue(character_1) == 0)
    if OR_14:
        return
    if FlagEnabled(flag_9):
        return
    GotoIfFlagEnabled(Label.L2, flag=flag_3)
    WaitFrames(frames=1)
    EnableFlag(flag_1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(TimeElapsed(seconds=seconds_2))
    AND_2.Add(FlagEnabled(flag_3))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(flag_1)
    OR_2.Add(TimeElapsed(seconds=seconds))
    AND_3.Add(FlagEnabled(flag_3))
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L2, input_condition=AND_3)
    if FlagEnabled(flag_6):
        return RESTART
    if FlagEnabled(flag_9):
        return
    OR_3.Add(HealthValue(character) == 0)
    OR_3.Add(HealthValue(character_1) == 0)
    if OR_3:
        return
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    DisableFlag(flag_1)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    DisableFlag(flag_1)
    AwaitFlagDisabled(flag=flag_4)
    Wait(seconds_1)
    DisableFlag(flag_3)
    Restart()


@RestartOnRest(20010729)
def Event_20010729(
    _,
    attacker__character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds: float,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
    flag_14: Flag | int,
    seconds_1: float,
):
    """Event 20010729"""
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_5):
        return
    AND_1.Add(HealthValue(attacker__character) == 0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=ALL_PLAYERS, attacker=attacker__character))
    AND_2.Add(HealthValue(ALL_PLAYERS) == 0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_2)
    if FlagEnabled(flag_6):
        return RESTART
    EnableFlag(flag_1)
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_2.Add(HealthValue(attacker__character) == 0)
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag_1)
    Restart()
    AND_3.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_PLAYERS))
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(flag_2)
    SkipLines(1)
    EnableFlag(flag_3)
    WaitFrames(frames=1)
    OR_3.Add(FlagEnabled(flag_13))
    OR_3.Add(FlagEnabled(flag_14))
    GotoIfConditionTrue(Label.L0, input_condition=OR_3)
    Wait(seconds)
    DisableFlag(flag_2)
    DisableFlag(flag_3)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagDisabled(flag=flag_7)
    Wait(seconds_1)
    if FlagEnabled(flag_12):
        DisableFlag(flag_12)
        EnableFlag(flag_11)
        Goto(Label.L1)
    if FlagEnabled(flag_11):
        DisableFlag(flag_11)
        EnableFlag(flag_10)
        Goto(Label.L1)
    if FlagEnabled(flag_10):
        DisableFlag(flag_10)
        EnableFlag(flag_9)
        Goto(Label.L1)
    if FlagEnabled(flag_9):
        DisableFlag(flag_9)
        EnableFlag(flag_8)
        Goto(Label.L1)
    if FlagEnabled(flag_8):
        DisableFlag(flag_8)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_4)
    End()


@RestartOnRest(20010731)
def Event_20010731(
    _,
    attacker__character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds: float,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    seconds_1: float,
):
    """Event 20010731"""
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_4):
        return
    AND_1.Add(HealthValue(attacker__character) == 0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=ALL_PLAYERS, attacker=attacker__character))
    AND_2.Add(HealthValue(ALL_PLAYERS) == 0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_2)
    if FlagEnabled(flag_5):
        return RESTART
    EnableFlag(flag_1)
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_2.Add(HealthValue(attacker__character) == 0)
    
    MAIN.Await(OR_2)
    
    DisableFlag(flag_1)
    Restart()
    EnableFlag(flag_2)
    WaitFrames(frames=1)
    OR_3.Add(FlagEnabled(flag_12))
    GotoIfConditionTrue(Label.L0, input_condition=OR_3)
    Wait(seconds)
    DisableFlag(flag_1)
    DisableFlag(flag_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagDisabled(flag=flag_6)
    Wait(seconds_1)
    if FlagEnabled(flag_11):
        DisableFlag(flag_11)
        EnableFlag(flag_10)
        Goto(Label.L1)
    if FlagEnabled(flag_10):
        DisableFlag(flag_10)
        EnableFlag(flag_9)
        Goto(Label.L1)
    if FlagEnabled(flag_9):
        DisableFlag(flag_9)
        EnableFlag(flag_8)
        Goto(Label.L1)
    if FlagEnabled(flag_8):
        DisableFlag(flag_8)
        EnableFlag(flag_7)
        Goto(Label.L1)
    if FlagEnabled(flag_7):
        DisableFlag(flag_7)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_3)
    End()


@RestartOnRest(20010733)
def Event_20010733(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    seconds: float,
    flag_3: Flag | int,
    left: int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    seconds_1: float,
):
    """Event 20010733"""
    if FlagEnabled(flag):
        return
    if FlagDisabled(flag_3):
        return
    AND_1.Add(HealthValue(character) == 0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    OR_1.Add(FlagEnabled(flag_10))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    Wait(seconds)
    DisableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagDisabled(flag=flag_4)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=0)
    Wait(seconds_1)
    if FlagEnabled(flag_9):
        DisableFlag(flag_9)
        EnableFlag(flag_8)
        Goto(Label.L1)
    if FlagEnabled(flag_8):
        DisableFlag(flag_8)
        EnableFlag(flag_7)
        Goto(Label.L1)
    if FlagEnabled(flag_7):
        DisableFlag(flag_7)
        EnableFlag(flag_6)
        Goto(Label.L1)
    if FlagEnabled(flag_6):
        DisableFlag(flag_6)
        EnableFlag(flag_5)
        Goto(Label.L1)
    if FlagEnabled(flag_5):
        DisableFlag(flag_5)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfValueEqual(3, left=left, right=0)  # NOTE: skip goes past end of event
    EnableFlag(flag_2)
    End()


@RestartOnRest(20010736)
def Event_20010736(
    _,
    character: uint,
    first_flag: Flag | int,
    last_flag: Flag | int,
    first_flag_1: Flag | int,
    last_flag_1: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    distance: float,
    character_1: Character | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    seconds: float,
):
    """Event 20010736"""
    if FlagEnabled(flag_6):
        return
    if FlagDisabled(flag_8):
        return
    AwaitFlagEnabled(flag=character)
    Wait(seconds)
    EnableBackread(character_1)
    SetCharacterTalkRange(character=character_1, distance=distance)
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 4)
    OR_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) >= 1)
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader))
    AND_1.Add(OR_1)
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 4)
    OR_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) == 0)
    OR_2.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader, target_count=0.0))
    OR_2.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader, target_count=0.0))
    OR_2.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader, target_count=0.0))
    OR_2.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader, target_count=0.0))
    AND_2.Add(OR_2)
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 3)
    OR_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) >= 1)
    OR_3.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_3.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_3.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_3.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader))
    AND_3.Add(OR_3)
    AND_4.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 3)
    OR_4.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) == 0)
    OR_4.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader, target_count=0.0))
    OR_4.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader, target_count=0.0))
    OR_4.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader, target_count=0.0))
    OR_4.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader, target_count=0.0))
    AND_4.Add(OR_4)
    AND_5.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 2)
    OR_5.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) >= 1)
    OR_5.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_5.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_5.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_5.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader))
    AND_5.Add(OR_5)
    AND_6.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 2)
    OR_6.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) == 0)
    OR_6.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader, target_count=0.0))
    OR_6.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader, target_count=0.0))
    OR_6.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader, target_count=0.0))
    OR_6.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader, target_count=0.0))
    AND_6.Add(OR_6)
    SkipLinesIfConditionFalse(2, AND_1)
    EnableFlag(flag_5)
    Goto(Label.L0)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag)
    Goto(Label.L0)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(flag_1)
    Goto(Label.L0)
    SkipLinesIfConditionFalse(2, AND_4)
    EnableFlag(flag_2)
    Goto(Label.L0)
    SkipLinesIfConditionFalse(2, AND_5)
    EnableFlag(flag_3)
    Goto(Label.L0)
    SkipLinesIfConditionFalse(2, AND_6)
    EnableFlag(flag_4)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagEnabled(flag=flag_7)
    SetBackreadStateAlternate(character, False)
    End()


@RestartOnRest(20010371)
def Event_20010371(
    _,
    region: Region | int,
    region_1: Region | int,
    region_2: Region | int,
    region_3: Region | int,
    region_4: Region | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 20010371"""
    if FlagDisabled(flag_5):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region_1))
    AND_3.Add(FlagDisabled(flag_2))
    AND_3.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region_2))
    AND_4.Add(FlagDisabled(flag_3))
    AND_4.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region_3))
    AND_5.Add(FlagDisabled(flag_4))
    AND_5.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region_4))
    AND_6.Add(FlagEnabled(flag))
    AND_6.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region))
    AND_7.Add(FlagEnabled(flag_1))
    AND_7.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region_1))
    AND_8.Add(FlagEnabled(flag_2))
    AND_8.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region_2))
    AND_9.Add(FlagEnabled(flag_3))
    AND_9.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region_3))
    AND_10.Add(FlagEnabled(flag_4))
    AND_10.Add(CharacterOutsideRegion(character=ALL_PLAYERS, region=region_4))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    EnableNetworkFlag(flag)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    EnableNetworkFlag(flag_1)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    EnableNetworkFlag(flag_2)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_4)
    EnableNetworkFlag(flag_3)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_5)
    EnableNetworkFlag(flag_4)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_6)
    DisableNetworkFlag(flag)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_7)
    DisableNetworkFlag(flag_1)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_8)
    DisableNetworkFlag(flag_2)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_9)
    DisableNetworkFlag(flag_3)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_10)
    DisableNetworkFlag(flag_4)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(20010738)
def Event_20010738(
    _,
    first_flag: Flag | int,
    last_flag: Flag | int,
    first_flag_1: Flag | int,
    last_flag_1: Flag | int,
    first_flag_2: Flag | int,
    last_flag_2: Flag | int,
    first_flag_3: Flag | int,
    last_flag_3: Flag | int,
    first_flag_4: Flag | int,
    last_flag_4: Flag | int,
    first_flag_5: Flag | int,
    last_flag_5: Flag | int,
    first_flag_6: Flag | int,
    last_flag_6: Flag | int,
    first_flag_7: Flag | int,
    last_flag_7: Flag | int,
):
    """Event 20010738"""
    DisableFlagRange((first_flag, last_flag))
    DisableFlagRange((first_flag_1, last_flag_1))
    DisableFlagRange((first_flag_2, last_flag_2))
    DisableFlagRange((first_flag_3, last_flag_3))
    DisableFlagRange((first_flag_4, last_flag_4))
    DisableFlagRange((first_flag_5, last_flag_5))
    DisableFlagRange((first_flag_6, last_flag_6))
    DisableFlagRange((first_flag_7, last_flag_7))
    End()


@RestartOnRest(20010739)
def Event_20010739(_, flag: Flag | int):
    """Event 20010739"""
    DisableFlag(20012791)
    WaitFrames(frames=2)
    if FlagDisabled(flag):
        return
    AND_1.Add(FlagEnabled(7640))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableNetworkFlag(20012783)
    AND_2.Add(FlagEnabled(7644))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableNetworkFlag(20012784)
    AND_3.Add(FlagEnabled(7642))
    SkipLinesIfConditionFalse(1, AND_3)
    EnableNetworkFlag(20012785)
    AND_4.Add(FlagEnabled(7643))
    SkipLinesIfConditionFalse(1, AND_4)
    EnableNetworkFlag(20012786)
    AND_5.Add(FlagEnabled(7641))
    SkipLinesIfConditionFalse(1, AND_5)
    EnableNetworkFlag(20012787)
    AND_6.Add(FlagEnabled(7645))
    SkipLinesIfConditionFalse(1, AND_6)
    EnableNetworkFlag(20012788)
    AND_7.Add(FlagEnabled(7646))
    SkipLinesIfConditionFalse(1, AND_7)
    EnableNetworkFlag(20012789)
    AND_8.Add(FlagEnabled(7647))
    SkipLinesIfConditionFalse(1, AND_8)
    EnableNetworkFlag(20012790)
    if FlagRangeAnyEnabled((20012788, 20012790)):
        EnableFlag(20019403)
    EnableNetworkFlag(20012791)
    End()


@RestartOnRest(20010770)
def Event_20010770(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    flag_6: Flag | int,
    flag_7: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
    flag_14: Flag | int,
    flag_15: Flag | int,
    flag_16: Flag | int,
):
    """Event 20010770"""
    if FlagEnabled(flag_6):
        return
    if FlagDisabled(flag_9):
        return
    AwaitFlagEnabled(flag=flag_8)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagEnabled(flag_14))
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagEnabled(flag_11))
    AND_2.Add(OR_1)
    AND_3.Add(FlagEnabled(flag_2))
    AND_3.Add(FlagDisabled(flag_3))
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 3)
    AND_3.Add(FlagEnabled(flag_14))
    OR_2.Add(TimeElapsed(seconds=seconds_1))
    OR_2.Add(FlagEnabled(flag_12))
    OR_2.Add(FlagEnabled(flag_7))
    AND_3.Add(OR_2)
    AND_4.Add(FlagEnabled(flag_3))
    AND_4.Add(FlagDisabled(flag_4))
    AND_4.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 4)
    AND_4.Add(FlagEnabled(flag_14))
    OR_3.Add(TimeElapsed(seconds=seconds_2))
    OR_3.Add(FlagEnabled(flag_10))
    OR_3.Add(FlagEnabled(flag_13))
    AND_5.Add(FlagDisabled(flag_10))
    AND_5.Add(FlagDisabled(flag_13))
    AND_5.Add(FlagDisabled(flag_15))
    OR_3.Add(AND_5)
    AND_4.Add(OR_3)
    AND_6.Add(FlagEnabled(flag_4))
    AND_6.Add(FlagDisabled(flag_5))
    AND_6.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 5)
    AND_6.Add(FlagEnabled(flag_14))
    OR_4.Add(TimeElapsed(seconds=seconds_3))
    OR_4.Add(FlagEnabled(flag_10))
    OR_4.Add(FlagEnabled(flag_13))
    AND_7.Add(FlagDisabled(flag_10))
    AND_7.Add(FlagDisabled(flag_13))
    AND_7.Add(FlagDisabled(flag_15))
    AND_7.Add(FlagDisabled(flag_16))
    OR_4.Add(AND_7)
    AND_6.Add(OR_4)
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(AND_3)
    OR_5.Add(AND_4)
    OR_5.Add(AND_6)
    
    MAIN.Await(OR_5)
    
    DisableFlag(flag_11)
    DisableFlag(flag_7)
    DisableFlag(flag_14)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    EnableFlag(flag_1)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    EnableFlag(flag_2)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    EnableFlag(flag_3)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_4)
    EnableFlag(flag_4)
    Goto(Label.L0)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_6)
    EnableFlag(flag_5)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@RestartOnRest(20010771)
def Event_20010771(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
    flag_14: Flag | int,
):
    """Event 20010771"""
    if FlagEnabled(flag_13):
        return
    if FlagDisabled(flag_14):
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_4))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L4, flag=flag_4)
    GotoIfFlagEnabled(Label.L3, flag=flag_3)
    GotoIfFlagEnabled(Label.L2, flag=flag_2)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_11):
        EnableNetworkFlag(flag_9)
        Goto(Label.L5)
    if FlagEnabled(flag_10):
        EnableNetworkFlag(flag_7)
        Goto(Label.L5)
    if FlagEnabled(flag_12):
        EnableNetworkFlag(flag_8)
        Goto(Label.L5)
    EnableNetworkFlag(flag_6)
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L6, flag=flag_11)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    if FlagEnabled(flag_10):
        EnableNetworkFlag(flag_7)
        Goto(Label.L5)
    if FlagEnabled(flag_12):
        EnableNetworkFlag(flag_8)
        Goto(Label.L5)
    EnableNetworkFlag(flag_6)
    Goto(Label.L5)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_1.Add(FlagEnabled(flag_10))
    AND_1.Add(FlagEnabled(flag_12))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableNetworkFlag(flag_8)
    Goto(Label.L5)
    AND_2.Add(FlagDisabled(flag_10))
    AND_2.Add(FlagDisabled(flag_12))
    SkipLinesIfConditionFalse(2, AND_2)
    EnableNetworkFlag(flag_5)
    Goto(Label.L5)
    EnableNetworkFlag(flag_6)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagEnabled(flag_10))
    AND_3.Add(FlagEnabled(flag_11))
    AND_3.Add(FlagEnabled(flag_12))
    SkipLinesIfConditionFalse(2, AND_3)
    EnableNetworkFlag(flag_8)
    Goto(Label.L5)
    AND_4.Add(FlagDisabled(flag_10))
    AND_4.Add(FlagEnabled(flag_11))
    AND_4.Add(FlagEnabled(flag_12))
    AND_5.Add(FlagEnabled(flag_10))
    AND_5.Add(FlagDisabled(flag_11))
    AND_5.Add(FlagEnabled(flag_12))
    AND_6.Add(FlagEnabled(flag_10))
    AND_6.Add(FlagEnabled(flag_11))
    AND_6.Add(FlagDisabled(flag_12))
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    SkipLinesIfConditionFalse(2, OR_3)
    EnableNetworkFlag(flag_6)
    Goto(Label.L5)
    EnableNetworkFlag(flag_5)
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_7.Add(FlagEnabled(flag_10))
    AND_7.Add(FlagEnabled(flag_11))
    AND_7.Add(FlagEnabled(flag_12))
    SkipLinesIfConditionFalse(2, AND_7)
    EnableNetworkFlag(flag_6)
    Goto(Label.L5)
    EnableNetworkFlag(flag_5)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(flag_5)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    Restart()


@RestartOnRest(20010772)
def Event_20010772(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
):
    """Event 20010772"""
    if FlagEnabled(flag_8):
        return
    if FlagDisabled(flag_9):
        return
    WaitFrames(frames=1)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_5):
        EnableNetworkFlag(flag_2)
        Goto(Label.L2)
    if FlagEnabled(flag_7):
        EnableNetworkFlag(flag_4)
        Goto(Label.L2)
    if FlagEnabled(flag_6):
        EnableNetworkFlag(flag_3)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(flag_5))
    AND_1.Add(FlagEnabled(flag_6))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableNetworkFlag(flag_3)
    Goto(Label.L2)
    AND_2.Add(FlagDisabled(flag_5))
    AND_2.Add(FlagEnabled(flag_6))
    AND_2.Add(FlagEnabled(flag_7))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableNetworkFlag(flag_3)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(20010773)
def Event_20010773(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
    flag_12: Flag | int,
    flag_13: Flag | int,
    flag_14: Flag | int,
    flag_15: Flag | int,
):
    """Event 20010773"""
    if FlagDisabled(flag_7):
        return
    WaitFrames(frames=1)
    AwaitFlagEnabled(flag=flag)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_9))
    OR_1.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(FlagEnabled(flag_8))
    AND_1.Add(OR_1)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 3)
    AND_2.Add(FlagEnabled(flag_9))
    OR_2.Add(TimeElapsed(seconds=seconds_1))
    OR_2.Add(FlagEnabled(flag_10))
    OR_2.Add(FlagEnabled(flag_5))
    AND_2.Add(OR_2)
    AND_3.Add(FlagEnabled(flag_2))
    AND_3.Add(FlagDisabled(flag_3))
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 4)
    AND_3.Add(FlagEnabled(flag_9))
    OR_3.Add(TimeElapsed(seconds=seconds_2))
    OR_3.Add(FlagEnabled(flag_11))
    OR_3.Add(FlagEnabled(flag_12))
    AND_3.Add(OR_3)
    AND_4.Add(FlagEnabled(flag_3))
    AND_4.Add(FlagDisabled(flag_4))
    AND_4.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) == 5)
    AND_4.Add(FlagEnabled(flag_9))
    OR_4.Add(TimeElapsed(seconds=seconds_3))
    OR_4.Add(FlagEnabled(flag_11))
    OR_4.Add(FlagEnabled(flag_12))
    AND_4.Add(OR_4)
    OR_5.Add(AND_1)
    OR_5.Add(AND_2)
    OR_5.Add(AND_3)
    OR_5.Add(AND_4)
    
    MAIN.Await(OR_5)
    
    EnableFlag(flag_6)
    EnableFlag(flag_13)
    OR_10.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_10.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_10.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_10.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    OR_10.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_4))
    
    MAIN.Await(OR_10)
    
    DisableFlag(flag_13)
    AND_5.Add(FlagDisabled(flag_13))
    AND_5.Add(FlagDisabled(flag_14))
    AND_5.Add(FlagDisabled(flag_15))
    SkipLinesIfConditionFalse(1, AND_5)
    DisableFlag(flag_6)
    Restart()


@RestartOnRest(20010774)
def Event_20010774(_, flag: Flag | int):
    """Event 20010774"""
    if FlagEnabled(7625):
        return
    if FlagDisabled(7630):
        return
    WaitFrames(frames=1)
    AND_1.Add(FlagDisabled(20019533))
    OR_1.Add(FlagEnabled(20019284))
    OR_1.Add(FlagEnabled(20019285))
    OR_1.Add(FlagEnabled(20019286))
    OR_1.Add(FlagEnabled(20019287))
    OR_1.Add(FlagEnabled(20019288))
    OR_1.Add(FlagEnabled(20019289))
    OR_1.Add(FlagEnabled(20019240))
    OR_1.Add(FlagEnabled(20019241))
    OR_1.Add(FlagEnabled(20019242))
    OR_1.Add(FlagEnabled(20019243))
    OR_1.Add(FlagEnabled(20019244))
    OR_1.Add(FlagEnabled(20012724))
    OR_1.Add(FlagEnabled(20012725))
    OR_1.Add(FlagEnabled(20012726))
    OR_1.Add(FlagEnabled(20012727))
    OR_1.Add(FlagEnabled(20012736))
    OR_1.Add(FlagEnabled(20012737))
    OR_1.Add(FlagEnabled(20012738))
    OR_1.Add(FlagEnabled(20012739))
    OR_1.Add(FlagEnabled(20019350))
    OR_1.Add(FlagEnabled(20019351))
    OR_1.Add(FlagEnabled(20012745))
    OR_1.Add(FlagEnabled(20012748))
    OR_1.Add(FlagEnabled(20012749))
    OR_1.Add(FlagEnabled(20012753))
    OR_1.Add(FlagEnabled(20012754))
    OR_1.Add(FlagEnabled(20012755))
    OR_1.Add(FlagEnabled(20012761))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(20019287):
        EnableFlag(20019281)
        Goto(Label.L0)
    if FlagEnabled(20019288):
        EnableFlag(20019282)
        Goto(Label.L0)
    if FlagEnabled(20019289):
        EnableFlag(20019283)
        Goto(Label.L0)
    if FlagEnabled(20012761):
        EnableFlag(20012760)
        Goto(Label.L0)
    if FlagEnabled(20019244):
        EnableFlag(20019239)
        Goto(Label.L0)
    if FlagEnabled(20012739):
        EnableFlag(20012733)
        Goto(Label.L0)
    if FlagEnabled(20019350):
        EnableFlag(20012734)
        Goto(Label.L0)
    if FlagEnabled(20019351):
        EnableFlag(20012735)
        Goto(Label.L0)
    if FlagEnabled(20012754):
        EnableFlag(20012751)
        Goto(Label.L0)
    if FlagEnabled(20012755):
        EnableFlag(20012752)
        Goto(Label.L0)
    if FlagEnabled(20012727):
        EnableFlag(20012723)
        Goto(Label.L0)
    if FlagEnabled(20012748):
        EnableFlag(20012743)
        Goto(Label.L0)
    if FlagEnabled(20012749):
        EnableFlag(20012744)
        Goto(Label.L0)
    if FlagEnabled(20019243):
        EnableFlag(20019238)
        Goto(Label.L0)
    if FlagEnabled(20012738):
        EnableFlag(20012732)
        Goto(Label.L0)
    if FlagEnabled(20012726):
        EnableFlag(20012722)
        Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20019284)
    EnableFlag(20012717)
    Goto(Label.L0)
    if FlagEnabled(20019285):
        EnableFlag(20012718)
        Goto(Label.L0)
    if FlagEnabled(20019286):
        EnableFlag(20019280)
        Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20019240)
    EnableFlag(20019235)
    Goto(Label.L0)
    if FlagEnabled(20019241):
        EnableFlag(20019236)
        Goto(Label.L0)
    if FlagEnabled(20019242):
        EnableFlag(20019237)
        Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20012736)
    EnableFlag(20012730)
    Goto(Label.L0)
    if FlagEnabled(20012737):
        EnableFlag(20012731)
        Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20012753)
    EnableFlag(20012750)
    Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20012724)
    EnableFlag(20012720)
    Goto(Label.L0)
    if FlagEnabled(20012725):
        EnableFlag(20012721)
        Goto(Label.L0)
    SkipLinesIfFlagEnabled(3, flag)
    SkipLinesIfFlagDisabled(2, 20012745)
    EnableFlag(20012740)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(20010775)
def Event_20010775(
    _,
    character: Character | int,
    flag: Flag | int,
    character_1: Character | int,
    flag_1: Flag | int,
    character_2: Character | int,
    flag_2: Flag | int,
    character_3: Character | int,
    flag_3: Flag | int,
    character_4: Character | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 20010775"""
    if FlagEnabled(flag_6):
        return
    if FlagDisabled(flag_8):
        return
    AwaitFlagEnabled(flag=flag_7)
    OR_1.Add(HealthValue(character) == 0)
    OR_1.Add(FlagDisabled(flag))
    OR_2.Add(HealthValue(character_1) == 0)
    OR_2.Add(FlagDisabled(flag_1))
    OR_3.Add(HealthValue(character_2) == 0)
    OR_3.Add(FlagDisabled(flag_2))
    OR_4.Add(HealthValue(character_3) == 0)
    OR_4.Add(FlagDisabled(flag_3))
    OR_5.Add(HealthValue(character_4) == 0)
    OR_5.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_1.Add(OR_3)
    AND_1.Add(OR_4)
    AND_1.Add(OR_5)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag_5)
    End()


@RestartOnRest(20010776)
def Event_20010776(_, flag: Flag | int, character: Character | int):
    """Event 20010776"""
    if FlagDisabled(flag):
        return
    SetBackreadStateAlternate(character, True)
    End()


@RestartOnRest(20010777)
def Event_20010777(
    _,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
):
    """Event 20010777"""
    if FlagDisabled(flag_2):
        return
    AwaitFlagEnabled(flag=flag_1)
    OR_1.Add(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_2, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_3, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_4, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(CLIENT_PLAYER_5, character_type=CharacterType.Invader))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(flag)
    End()


@RestartOnRest(20010778)
def Event_20010778(
    _,
    character: Character | int,
    character_1: Character | int,
    character_2: Character | int,
    character_3: Character | int,
    character_4: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    first_flag: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    last_flag: Flag | int,
    flag_8: Flag | int,
    value: float,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
):
    """Event 20010778"""
    if FlagDisabled(flag_9):
        return
    AwaitFlagEnabled(flag=flag_10)
    if FlagEnabled(flag):
        AND_1.Add(HealthRatio(character) <= value)
        AND_1.Add(FlagDisabled(first_flag))
        OR_1.Add(AND_1)
    if FlagEnabled(flag_1):
        AND_2.Add(HealthRatio(character_1) <= value)
        AND_2.Add(FlagDisabled(flag_5))
        OR_1.Add(AND_2)
    if FlagEnabled(flag_2):
        AND_3.Add(HealthRatio(character_2) <= value)
        AND_3.Add(FlagDisabled(flag_6))
        OR_1.Add(AND_3)
    if FlagEnabled(flag_3):
        AND_4.Add(HealthRatio(character_3) <= value)
        AND_4.Add(FlagDisabled(flag_7))
        OR_1.Add(AND_4)
    if FlagEnabled(flag_4):
        AND_5.Add(HealthRatio(character_4) <= value)
        AND_5.Add(FlagDisabled(last_flag))
        OR_1.Add(AND_5)
    if FlagEnabled(flag):
        AND_6.Add(HealthRatio(character) > value)
        AND_6.Add(FlagEnabled(first_flag))
        OR_2.Add(AND_6)
    if FlagEnabled(flag_1):
        AND_7.Add(HealthRatio(character_1) > value)
        AND_7.Add(FlagEnabled(flag_5))
        OR_2.Add(AND_7)
    if FlagEnabled(flag_2):
        AND_8.Add(HealthRatio(character_2) > value)
        AND_8.Add(FlagEnabled(flag_6))
        OR_2.Add(AND_8)
    if FlagEnabled(flag_3):
        AND_9.Add(HealthRatio(character_3) > value)
        AND_9.Add(FlagEnabled(flag_7))
        OR_2.Add(AND_9)
    if FlagEnabled(flag_4):
        AND_10.Add(HealthRatio(character_4) > value)
        AND_10.Add(FlagEnabled(last_flag))
        OR_2.Add(AND_10)
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFlagDisabled(4, flag)
    SkipLinesIfFlagEnabled(3, first_flag)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_1)
    EnableFlag(first_flag)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(4, flag_1)
    SkipLinesIfFlagEnabled(3, flag_5)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_2)
    EnableFlag(flag_5)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(4, flag_2)
    SkipLinesIfFlagEnabled(3, flag_6)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    EnableFlag(flag_6)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(4, flag_3)
    SkipLinesIfFlagEnabled(3, flag_7)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_4)
    EnableFlag(flag_7)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(4, flag_4)
    SkipLinesIfFlagEnabled(3, last_flag)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_5)
    EnableFlag(last_flag)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(4, flag)
    SkipLinesIfFlagDisabled(3, first_flag)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_6)
    DisableFlag(first_flag)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(4, flag_1)
    SkipLinesIfFlagDisabled(3, flag_5)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_7)
    DisableFlag(flag_5)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(4, flag_2)
    SkipLinesIfFlagDisabled(3, flag_6)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_8)
    DisableFlag(flag_6)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(4, flag_3)
    SkipLinesIfFlagDisabled(3, flag_7)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_9)
    DisableFlag(flag_7)
    Goto(Label.L1)
    SkipLinesIfFlagDisabled(4, flag_4)
    SkipLinesIfFlagDisabled(3, last_flag)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_10)
    DisableFlag(last_flag)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag_8)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_6.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= 2)
    SkipLinesIfConditionFalse(2, AND_6)
    EnableFlag(flag_11)
    SkipLines(1)
    DisableFlag(flag_11)
    Restart()


@RestartOnRest(20010779)
def Event_20010779(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 20010779"""
    if FlagDisabled(flag_7):
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag_5):
        EnableFlag(flag_6)
        DisableFlag(flag_5)
        Restart()
    if FlagEnabled(flag_4):
        EnableFlag(flag_5)
        DisableFlag(flag_4)
        Restart()
    if FlagEnabled(flag_3):
        EnableFlag(flag_4)
        DisableFlag(flag_3)
        Restart()
    if FlagEnabled(flag_2):
        EnableFlag(flag_3)
        DisableFlag(flag_2)
        Restart()
    EnableFlag(flag_2)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(flag_6):
        DisableFlag(flag_6)
        EnableFlag(flag_5)
        Restart()
    if FlagEnabled(flag_5):
        DisableFlag(flag_5)
        EnableFlag(flag_4)
        Restart()
    if FlagEnabled(flag_4):
        DisableFlag(flag_4)
        EnableFlag(flag_3)
        Restart()
    if FlagEnabled(flag_3):
        DisableFlag(flag_3)
        EnableFlag(flag_2)
        Restart()
    if FlagEnabled(flag_2):
        DisableFlag(flag_2)
        Restart()


@RestartOnRest(20010780)
def Event_20010780(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_2: Flag | int,
    value: int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
):
    """Event 20010780"""
    if FlagDisabled(flag_2):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_4)
    AwaitFlagEnabled(flag=flag_1)
    AND_1.Add(TimeElapsed(seconds=seconds))
    AND_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_4)

    # --- Label 0 --- #
    DefineLabel(0)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L1, flag=flag_3)
    GotoIfFlagEnabled(Label.L1, flag=flag_5)
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= value)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag)
    DisableFlag(flag_3)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(flag_3))
    AND_3.Add(FlagDisabled(flag_5))
    
    MAIN.Await(AND_3)
    
    Restart()


@RestartOnRest(20010781)
def Event_20010781(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_2: Flag | int,
    value: int,
    first_flag_1: Flag | int,
    last_flag_1: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 20010781"""
    if FlagDisabled(flag_2):
        return
    GotoIfFlagEnabled(Label.L2, flag=flag_6)
    AwaitFlagEnabled(flag=flag_5)
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) >= 3)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AwaitFlagEnabled(flag=flag_3)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitFlagEnabled(flag=flag_1)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(TimeElapsed(seconds=seconds))
    AND_2.Add(FlagEnabled(flag_4))
    AND_2.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag_6)

    # --- Label 2 --- #
    DefineLabel(2)
    WaitFrames(frames=1)
    GotoIfFlagDisabled(Label.L3, flag=flag_4)
    GotoIfFlagEnabled(Label.L3, flag=flag_7)
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= value)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(flag)
    DisableFlag(flag_4)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    AND_4.Add(FlagEnabled(flag_4))
    AND_4.Add(FlagDisabled(flag_7))
    
    MAIN.Await(AND_4)
    
    Restart()


@RestartOnRest(20010782)
def Event_20010782(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    seconds: float,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
):
    """Event 20010782"""
    if FlagDisabled(flag_10):
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_4))
    AND_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_5))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_6))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_7))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(seconds)
    AwaitFlagDisabled(flag=flag_9)
    EnableFlag(flag_8)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(seconds)
    EnableFlag(flag_8)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    Restart()


@RestartOnRest(20010783)
def Event_20010783(
    _,
    flag: Flag | int,
    seconds: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_1: Flag | int,
    value: int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
    flag_9: Flag | int,
    flag_10: Flag | int,
    flag_11: Flag | int,
):
    """Event 20010783"""
    if FlagDisabled(flag_1):
        return
    AwaitFlagEnabled(flag=flag)
    AND_1.Add(TimeElapsed(seconds=seconds))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= value)
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag_2)
    EnableFlag(flag_4)
    if FlagEnabled(flag_6):
        AwaitFlagEnabled(flag=flag_9)
        Goto(Label.L0)
    if FlagEnabled(flag_8):
        AwaitFlagEnabled(flag=flag_11)
        Goto(Label.L0)
    if FlagEnabled(flag_7):
        AwaitFlagEnabled(flag=flag_10)
        Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag_4)
    AND_3.Add(FlagDisabled(flag_3))
    AND_3.Add(FlagDisabled(flag_4))
    AND_3.Add(FlagDisabled(flag_5))
    SkipLinesIfConditionFalse(1, AND_3)
    DisableFlag(flag_2)
    End()


@RestartOnRest(20010784)
def Event_20010784(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_2: Flag | int,
    value: int,
    first_flag_1: Flag | int,
    last_flag_1: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 20010784"""
    if FlagDisabled(flag_2):
        return
    AwaitFlagEnabled(flag=flag_8)
    AND_1.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag_1, last_flag_1)) > 2)
    SkipLinesIfConditionFalse(2, AND_1)
    AwaitFlagEnabled(flag=flag_1)
    SkipLines(1)
    AwaitFlagEnabled(flag=flag_3)
    AND_2.Add(TimeElapsed(seconds=seconds))
    
    MAIN.Await(AND_2)
    
    AND_3.Add(EnabledFlagCount(FlagType.Absolute, flag_range=(first_flag, last_flag)) >= value)
    SkipLinesIfConditionFalse(2, AND_3)
    EnableFlag(flag_4)
    EnableFlag(flag_7)
    AwaitFlagEnabled(flag=flag)
    DisableFlag(flag_7)
    AND_4.Add(FlagDisabled(flag_5))
    AND_4.Add(FlagDisabled(flag_6))
    AND_4.Add(FlagDisabled(flag_7))
    SkipLinesIfConditionFalse(1, AND_4)
    DisableFlag(flag_4)
    End()


@RestartOnRest(20010785)
def Event_20010785(_, character: Character | int, text: EventText | int, flag: Flag | int, seconds: float):
    """Event 20010785"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(HealthValue(character) == 0)
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    DisplayNetworkMessage(text=text, unk_4_5=False)
    End()


@RestartOnRest(20010793)
def Event_20010793(_, flag: Flag | int, flag_1: Flag | int):
    """Event 20010793"""
    if FlagDisabled(flag):
        return
    AND_1.Add(HealthValue(ALL_PLAYERS) == 0)
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    EnableFlag(flag_1)
    End()


@RestartOnRest(20010740)
def Event_20010740(_, character: uint, flag: Flag | int, flag_1: Flag | int, animation_id: int, flag_2: Flag | int):
    """Event 20010740"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableInvincibility(character)
    AND_6.Add(FlagEnabled(flag_1))
    AND_6.Add(FlagDisabled(flag_2))
    GotoIfConditionTrue(Label.L0, input_condition=AND_6)
    
    MAIN.Await(AND_6)
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    ForceAnimation(character, animation_id)
    WaitRealFrames(frames=1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_10.Add(FlagDisabled(flag_1))
    OR_10.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(20010741)
def Event_20010741(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20010741"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L20, flag=flag_2)
    DisableFlag(flag_1)
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    EnableFlag(flag_1)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(20010742)
def Event_20010742(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20010742"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    AND_1.Add(HealthValue(PLAYER) <= 0)
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag_1)
    End()


@RestartOnRest(20010743)
def Event_20010743(
    _,
    character: Character | int,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 20010743"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagDisabled(flag):
        return
    if FlagEnabled(flag_2):
        return
    OR_10.Add(FlagEnabled(flag_1))
    OR_10.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_10)
    
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    Restart()


@RestartOnRest(20010744)
def Event_20010744(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20010744"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag_2):
        return
    if FlagDisabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    End()


@RestartOnRest(20010745)
def Event_20010745(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20010745"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L20, flag=flag_2)
    DisableFlag(flag_1)
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    EnableFlag(flag_1)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    End()


@RestartOnRest(20010746)
def Event_20010746(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 20010746"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if FlagEnabled(flag_2):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitFrames(frames=1)
    AND_1.Add(HealthValue(PLAYER) <= 0)
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfConditionFalse(2, AND_2)
    EnableFlag(flag_1)
    End()


@RestartOnRest(20010750)
def Event_20010750(_, character: uint, flag: Flag | int, flag_1: Flag | int, animation_id: int):
    """Event 20010750"""
    DisableNetworkSync()
    WaitFrames(frames=1)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    ForceAnimation(character, animation_id, loop=True)
    SetTeamType(character, TeamType.NoTeam)


@RestartOnRest(20010760)
def Event_20010760(_, character: uint, flag: Flag | int, flag_1: Flag | int, animation_id: int, distance: float):
    """Event 20010760"""
    DisableNetworkSync()
    WaitFrames(frames=1)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(FlagDisabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_2)
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ResetCharacterPosition(character=character)
    SetCharacterTalkRange(character=character, distance=distance)
    ForceAnimation(character, animation_id, loop=True)
    SetTeamType(character, TeamType.NoTeam)


@RestartOnRest(20010761)
def Event_20010761(
    _,
    character: Character | int,
    character_1: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    flag_5: Flag | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
    flag_8: Flag | int,
):
    """Event 20010761"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    AND_10.Add(FlagEnabled(flag_2))
    AND_10.Add(FlagDisabled(flag_3))
    SkipLinesIfConditionFalse(7, AND_10)
    EnableFlag(flag_3)
    if FlagEnabled(flag_4):
        EnableFlag(flag_6)
    else:
        EnableFlag(flag_8)
    if FlagEnabled(flag_5):
        EnableFlag(flag_7)
    GotoIfFlagEnabled(Label.L20, flag=flag)
    GotoIfFlagEnabled(Label.L19, flag=flag_2)
    EnableInvincibility(character_1)
    EnableImmortality(character)
    DisableCharacter(character)
    OR_2.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_2)
    
    AddSpecialEffect(character_1, 9910)
    DisableAnimations(character_1)
    CreateTemporaryVFX(vfx_id=604220, anchor_entity=character_1, dummy_id=200, anchor_type=CoordEntityType.Character)
    EnableFlag(4418)
    EnableFlag(4438)
    EnableFlag(4378)
    EnableFlag(4398)
    EnableFlag(4478)
    EnableFlag(4578)
    EnableFlag(4458)
    EnableFlag(flag_1)
    WaitRealFrames(frames=5)
    SkipLinesIfFlagDisabled(7, flag_2)
    EnableFlag(flag_3)
    SkipLinesIfFlagDisabled(2, flag_4)
    EnableFlag(flag_6)
    SkipLines(1)
    EnableFlag(flag_8)
    SkipLinesIfFlagDisabled(1, flag_5)
    EnableFlag(flag_7)
    Wait(5.0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 19 --- #
    DefineLabel(19)
    EnableFlag(flag_3)
    if FlagEnabled(flag_4):
        EnableFlag(flag_6)
    else:
        EnableFlag(flag_8)
    if FlagEnabled(flag_5):
        EnableFlag(flag_7)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(7, 7625)
    EnableFlag(flag_3)
    SkipLinesIfFlagDisabled(2, flag_4)
    EnableFlag(flag_6)
    SkipLines(1)
    EnableFlag(flag_8)
    SkipLinesIfFlagDisabled(1, flag_5)
    EnableFlag(flag_7)
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    Restart()


@RestartOnRest(20010762)
def Event_20010762(_, flag: Flag | int, flag_1: Flag | int):
    """Event 20010762"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableFlag(flag)


@RestartOnRest(20010763)
def Event_20010763(_, character: Character | int, flag: Flag | int, character_1: uint):
    """Event 20010763"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    EnableInvincibility(character)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(HealthValue(character_1) <= 0)
    
    EnableCharacter(character)
    WaitRealFrames(frames=1)
    Move(character, destination=character_1, destination_type=CoordEntityType.Character, dummy_id=6, short_move=True)
    Wait(20.0)
    DisableCharacter(character)
