"""
Shadow Keep

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
    CommonFunc_9005810(
        0,
        flag=21000850,
        grace_flag=21000001,
        character=21000951,
        asset=21001951,
        enemy_block_distance=0.0,
    )
    RegisterGrace(grace_flag=21000002, asset=21001952, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21000006, asset=21001956, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21000007, asset=21001957, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21000008, asset=21001958, enemy_block_distance=0.0)
    RegisterGrace(grace_flag=21000009, asset=21001959, enemy_block_distance=0.0)
    Event_21002850()
    Event_21002860()
    Event_21002861()
    Event_21002899()
    CommonFunc_90005795(
        0,
        flag=7623,
        flag_1=0,
        flag_2=2048459292,
        left_flag=21002141,
        cancel_flag__right_flag=21002142,
        message=2080603,
        action_button_id=209053,
        asset=21001735,
        vfx_id=30010,
    )
    if CeremonyActive(ceremony=20):
        CommonFunc_90005799(
            0,
            flag=7623,
            character=21000735,
            banner_type=5,
            region=21002141,
            flag_1=21002729,
            character_1=21000736,
        )
    Event_21002144()
    CommonFunc_90005795(
        0,
        flag=7624,
        flag_1=0,
        flag_2=2048459292,
        left_flag=21012151,
        cancel_flag__right_flag=21012152,
        message=2080604,
        action_button_id=209054,
        asset=21001745,
        vfx_id=30000,
    )
    if CeremonyActive(ceremony=30):
        CommonFunc_90005798(0, flag=7624, character=21000745, banner_type=7, region=21002151, flag_1=21002739)
    Event_21002154()
    Event_21002470(0, character=21000472)
    Event_21002470(1, character=21000473)
    Event_21002320()
    Event_21002450()
    CommonFunc_90005301(0, flag=21000470, character=21000470, item_lot__unk1=21001991, seconds=0.0, unk1=2)
    CommonFunc_90005301(0, flag=21000471, character=21000471, item_lot__unk1=21001993, seconds=0.0, unk1=2)
    CommonFunc_90005301(0, flag=21000453, character=21000453, item_lot__unk1=21001995, seconds=0.0, unk1=2)
    Event_21002206()
    CommonFunc_90005501(
        0,
        flag=21000510,
        flag_1=21000511,
        left=0,
        asset=21001510,
        asset_1=21001511,
        asset_2=21001512,
        flag_2=21000512,
    )
    CommonFunc_90005501(
        0,
        flag=21000515,
        flag_1=21000516,
        left=0,
        asset=21001515,
        asset_1=21001516,
        asset_2=21001517,
        flag_2=21000517,
    )
    CommonFunc_90005501(
        0,
        flag=21000520,
        flag_1=21000521,
        left=0,
        asset=21001520,
        asset_1=21001521,
        asset_2=21001522,
        flag_2=21000522,
    )
    CommonFunc_90005501(
        0,
        flag=21000525,
        flag_1=21000526,
        left=1,
        asset=21001525,
        asset_1=21001526,
        asset_2=21001527,
        flag_2=21000527,
    )
    CommonFunc_90005501(
        0,
        flag=21000530,
        flag_1=21000531,
        left=0,
        asset=21001530,
        asset_1=21001531,
        asset_2=21001532,
        flag_2=21000532,
    )
    CommonFunc_90005501(
        0,
        flag=21000535,
        flag_1=21000536,
        left=0,
        asset=21001535,
        asset_1=21001536,
        asset_2=21001537,
        flag_2=21000537,
    )
    RunCommonEvent(21002515, slot=0, args=(21001521,))
    RunCommonEvent(21002515, slot=1, args=(21001531,))
    Event_21002510()
    Event_21002520()
    CommonFunc_90005511(0, flag=21000560, asset=21001560, obj_act_id=21003560, obj_act_id_1=-1, left=0)
    CommonFunc_90005512(0, flag=21000560, region=21002560, region_1=21002561)
    CommonFunc_90005510(
        0,
        flag=21008562,
        asset=21001562,
        obj_act_id=21003562,
        obj_act_id_1=1427027,
        text=20208036,
        left=0,
    )
    CommonFunc_90005525(0, flag=21000570, asset=21001570)
    CommonFunc_90005525(0, flag=21000572, asset=21001572)
    Event_21002580()
    CommonFunc_90005615(0, region=21002690, left=21009230)
    Event_21002600(0, flag=580120, asset=21001600, item_lot=80120)
    CommonFunc_90005780(
        0,
        flag=21000850,
        summon_flag=21002160,
        dismissal_flag=21002161,
        character=21000700,
        sign_type=20,
        region=21002160,
        right=2048459220,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=21000850, flag_1=21002160, flag_2=21002161, character=21000700)
    Event_21002890(
        0,
        flag=21002160,
        flag_1=21002855,
        character=21000700,
        region=21002850,
        region_1=21002859,
        animation=0,
    )
    CommonFunc_90005780(
        0,
        flag=21000850,
        summon_flag=21002164,
        dismissal_flag=21002165,
        character=21000720,
        sign_type=20,
        region=21002164,
        right=2046429373,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=21000850, flag_1=21002164, flag_2=21002165, character=21000720)
    Event_21002890(
        1,
        flag=21002164,
        flag_1=21002855,
        character=21000720,
        region=21002850,
        region_1=21002859,
        animation=0,
    )
    Event_21000700(
        0,
        character=21000710,
        flag=4340,
        flag_1=4341,
        flag_2=4342,
        flag_3=4343,
        flag_4=4345,
        flag_5=4346,
        flag_6=4860,
        flag_7=4358,
        flag_8=21002707,
        flag_9=21002706,
        flag_10=21009211,
        animation_id=90103,
        distance=45.0,
        animation_id_1=90100,
        flag_11=21009230,
    )
    CommonFunc_90005750(
        0,
        asset=21001711,
        action_button_id=4350,
        item_lot=106910,
        first_flag=400692,
        last_flag=400692,
        flag=21009213,
        vfx_id=0,
    )
    Event_21000701(0, flag=21009208, region=21002710, flag_1=21002705)
    Event_21000702(
        0,
        flag=21002710,
        flag_1=21002711,
        left=21002712,
        character=21000710,
        dummy_id=711,
        asset=21001710,
        dummy_id_1=711,
        radius=0.20000000298023224,
        animation=90212,
        animation_id=-1,
        special_effect=-1,
        radius_1=1.100000023841858,
        seconds=2.4000000953674316,
        flag_2=21009220,
        flag_3=21002715,
        flag_4=21009222,
        seconds_1=0.05000000074505806,
        flag_5=21009210,
        animation_1=90213,
        flag_6=21009211,
    )
    Event_21000703(
        0,
        flag=21002713,
        flag_1=21002714,
        left=21002712,
        character=21000710,
        animation__animation_id=90202,
        left_1=1,
        left_2=-1,
        special_effect=9600,
        seconds=0.0,
        flag_2=21009210,
        animation__animation_id_1=90201,
        flag_3=21009211,
    )
    Event_21000704(0, flag=21002715, flag_1=21009221, seconds=0.05000000074505806)
    Event_21000705(
        0,
        character=21000710,
        flag=21009214,
        flag_1=21009212,
        animation_id=90205,
        flag_2=21009210,
        animation_id_1=90203,
        flag_3=21009211,
        flag_4=21009212,
        seconds=3.200000047683716,
        flag_5=21009213,
        item_lot=106900,
        flag_6=21009230,
    )
    Event_21000706(0, flag=21009210, flag_1=21002706, flag_2=21009212, flag_3=21002707)
    Event_21000711(0, flag=7623, flag_1=4363, first_flag=4360, last_flag=4364, flag_2=4892, flag_3=2048459220)
    Event_21000712(0, character=21000735, flag=21002744, flag_1=7623)
    Event_21000714(0, flag=21002728, character=21000730, flag_1=21002726, flag_2=7623)
    Event_21000714(1, flag=21002745, character=21000735, flag_1=21002746, flag_2=7623)
    CommonFunc_90005769(
        0,
        character=21000735,
        flag=21002743,
        character_1=21000730,
        flag_1=21002722,
        flag_2=21002729,
        flag_3=7623,
        flag_4=7624,
    )
    CommonFunc_90005776(0, flag=400614, flag_1=7623, item_lot=116100)
    Event_21000735(0, character=21000735, character_1=21000730, ceremony=20)
    Event_21000712(1, character=21000745, flag=21002735, flag_1=7624)
    Event_21000714(2, flag=21002758, character=21000740, flag_1=21002757, flag_2=7624)
    Event_21000714(3, flag=21002737, character=21000745, flag_1=21002736, flag_2=7624)
    CommonFunc_90005769(
        0,
        character=21000745,
        flag=21002732,
        character_1=21000740,
        flag_1=21002752,
        flag_2=21002739,
        flag_3=7623,
        flag_4=7624,
    )
    CommonFunc_90005776(0, flag=400594, flag_1=7624, item_lot=105920)
    Event_21000735(1, character=21000745, character_1=21000740, ceremony=30)
    Event_21000725(0, flag=2048459220, flag_1=21010800, flag_2=21019205, flag_3=4898)
    CommonFunc_90005706(0, character=21000750, animation_id=30010, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_21000050()
    Event_21002500()
    CommonFunc_90005221(0, character=21000200, animation_id=30003, animation_id_1=20003, seconds=0.0, left=0)
    CommonFunc_90005211(
        0,
        character=21000201,
        animation_id=30001,
        animation_id_1=20001,
        region=21002201,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000202,
        animation_id=30001,
        animation_id_1=20001,
        region=21002201,
        radius=1.0,
        seconds=0.30000001192092896,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21000203, animation_id=30001, animation_id_1=20001, seconds=0.0, left=1)
    CommonFunc_90005261(0, character=21000204, region=21002204, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000205, region=21002205, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=21000207, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21000208,
        animation_id=30003,
        animation_id_1=20003,
        region=21002208,
        radius=1.0,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000209, region=21002240, radius=1.0, seconds=0.30000001192092896, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21000210,
        animation_id=30002,
        animation_id_1=20002,
        region=21002210,
        radius=1.0,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000211, region=21002210, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21000212,
        animation_id=30001,
        animation_id_1=20001,
        region=21002212,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000213, region=21002212, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000214, region=21002246, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000240, region=21002240, radius=1.0, seconds=1.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000241, region=21002241, radius=1.0, seconds=0.0, animation_id=3000)
    CommonFunc_90005261(0, character=21000242, region=21002242, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000244, region=21002244, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000246, region=21002246, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000282, region=21002283, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000283, region=21002283, radius=1.0, seconds=0.5, animation_id=-1)
    CommonFunc_90005261(0, character=21000284, region=21002284, radius=1.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005211(
        0,
        character=21000285,
        animation_id=30000,
        animation_id_1=20000,
        region=21002285,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000287, region=21002287, radius=1.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005261(
        0,
        character=21000288,
        region=21002287,
        radius=1.0,
        seconds=0.4000000059604645,
        animation_id=3001,
    )
    CommonFunc_90005211(
        0,
        character=21000290,
        animation_id=30000,
        animation_id_1=20000,
        region=21002290,
        radius=0.5,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_21002292(0, character=21000292, destination=21002292)
    Event_21002292(0, character=21000293, destination=21002293)
    Event_21002292(0, character=21000294, destination=21002294)
    CommonFunc_90005221(0, character=21000260, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000261, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000262, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000263, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000264, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000265, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000266, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=21000267, animation_id=30006, animation_id_1=20006, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=21000450, region=21002450, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000451, region=21002451, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000452, region=21002452, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=21000453, region=21002320, radius=1.0, seconds=1.0, animation_id=0)
    CommonFunc_90005261(0, character=21000454, region=21002454, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=21000300,
        animation_id=30002,
        animation_id_1=20002,
        region=21002300,
        radius=1.0,
        seconds=0.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000301,
        animation_id=30001,
        animation_id_1=20001,
        region=21002300,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000303,
        animation_id=30001,
        animation_id_1=20001,
        region=21002302,
        radius=1.0,
        seconds=0.699999988079071,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000304,
        animation_id=30002,
        animation_id_1=20002,
        region=21002302,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000305,
        animation_id=30001,
        animation_id_1=20001,
        region=21002305,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000306,
        animation_id=30001,
        animation_id_1=20001,
        region=21002306,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000307,
        animation_id=30001,
        animation_id_1=20001,
        region=21002305,
        radius=1.0,
        seconds=1.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000315,
        animation_id=30000,
        animation_id_1=20000,
        region=21002320,
        radius=1.0,
        seconds=2.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000316,
        animation_id=30001,
        animation_id_1=20001,
        region=21002320,
        radius=1.0,
        seconds=4.5,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000317,
        animation_id=30002,
        animation_id_1=20002,
        region=21002320,
        radius=1.0,
        seconds=3.0999999046325684,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000318,
        animation_id=30000,
        animation_id_1=20000,
        region=21002320,
        radius=1.0,
        seconds=2.200000047683716,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000340,
        animation_id=30001,
        animation_id_1=20001,
        region=21002306,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000350, region=21002350, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000351, region=21002351, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000352, region=21002351, radius=1.0, seconds=0.0, animation_id=3022)
    CommonFunc_90005211(
        0,
        character=21000355,
        animation_id=30000,
        animation_id_1=20000,
        region=21002355,
        radius=3.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000356,
        animation_id=30000,
        animation_id_1=20000,
        region=21002356,
        radius=3.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=21000368, region=21002368, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000369, region=21002368, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=21000370, region=21002368, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005211(
        0,
        character=21000380,
        animation_id=30001,
        animation_id_1=20001,
        region=21002380,
        radius=3.0,
        seconds=0.699999988079071,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005221(0, character=21000381, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    CommonFunc_90005261(0, character=21000382, region=21002382, radius=1.0, seconds=0.0, animation_id=3014)
    CommonFunc_90005211(
        0,
        character=21000470,
        animation_id=30002,
        animation_id_1=20002,
        region=21002470,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000471,
        animation_id=30002,
        animation_id_1=20002,
        region=21002471,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000472,
        animation_id=30002,
        animation_id_1=20002,
        region=21002472,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=21000473,
        animation_id=30002,
        animation_id_1=20002,
        region=21002473,
        radius=1.0,
        seconds=0.10000000149011612,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(21000050)
def Event_21000050():
    """Event 21000050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(21000525)


@RestartOnRest(21002144)
def Event_21002144():
    """Event 21002144"""
    if CeremonyInactive(ceremony=20):
        return
    DisableHealthBar(21000736)
    DisableFlag(1099002100)
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.Start)
    OR_3.Add(CharacterProportionDead(character=21000735))
    
    MAIN.Await(OR_3)
    
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.NormalFadeOut)


@RestartOnRest(21002154)
def Event_21002154():
    """Event 21002154"""
    if CeremonyInactive(ceremony=30):
        return
    DisableFlag(1099002100)
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.Start)
    OR_3.Add(CharacterProportionDead(character=21000745))
    
    MAIN.Await(OR_3)
    
    SetBossMusic(bgm_boss_conv_param_id=943000, state=BossMusicState.NormalFadeOut)


@RestartOnRest(21002206)
def Event_21002206():
    """Event 21002206"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(21000206)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(CharacterHasSpecialEffect(21000206, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90160))
    AND_5.Add(CharacterHasSpecialEffect(21000206, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90162))
    AND_6.Add(CharacterHasSpecialEffect(21000206, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90161))
    AND_7.Add(CharacterHasSpecialEffect(21000206, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90162))
    AND_8.Add(CharacterHasSpecialEffect(21000206, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(21000206, 90160))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=21002206))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=21002207))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=21000206))
    OR_2.Add(CharacterHasStateInfo(character=21000206, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=21000206, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=21000206, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=21000206, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=21000206, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=21002206))
    SkipLinesIfConditionFalse(1, AND_10)
    ForceAnimation(21000206, 3010)
    EnableAI(21000206)


@RestartOnRest(21002292)
def Event_21002292(_, character: Character | int, destination: uint):
    """Event 21002292"""
    if ThisEventSlotFlagEnabled():
        return
    if FlagDisabled(21008540):
        return
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(21002320)
def Event_21002320():
    """Event 21002320"""
    AND_1.Add(CharacterDead(21000453))
    AND_1.Add(FlagEnabled(21002320))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(21005320)
    DisableAnimations(21005320)
    DisableSpawner(entity=21003320)
    DisableSpawner(entity=21003321)
    DisableSpawner(entity=21003322)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagDisabled(21002320):
        DisableCharacter(21005320)
        DisableAnimations(21005320)
    DisableSpawner(entity=21003320)
    DisableSpawner(entity=21003321)
    DisableSpawner(entity=21003322)
    AND_2.Add(FlagEnabled(124))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21002320))
    
    MAIN.Await(AND_2)
    
    Wait(5.0)
    EnableSpawner(entity=21003320)
    EnableSpawner(entity=21003321)
    EnableSpawner(entity=21003322)
    EnableCharacter(21005320)
    EnableAnimations(21005320)
    OR_1.Add(CharacterDead(21000453))
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=21002320))
    OR_1.Add(HasAIStatus(21000453, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.NotEqual))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(21002450)
def Event_21002450():
    """Event 21002450"""
    AND_2.Add(FlagEnabled(124))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21002320))
    
    MAIN.Await(AND_2)
    
    Wait(2.0)
    AND_1.Add(CharacterProportionUnknownState_4_16(character=21000453, unk1=0, unk2=1120403456))
    if AND_1:
        return
    ForceAnimation(21000453, 20000)
    Wait(5.0)
    AND_1.Add(CharacterProportionUnknownState_4_16(character=21000453, unk1=0, unk2=1120403456))
    if AND_1:
        return
    ForceAnimation(21000453, 3028)


@RestartOnRest(21002470)
def Event_21002470(_, character: uint):
    """Event 21002470"""
    OR_1.Add(ThisEventSlotFlagEnabled())
    OR_1.Add(FlagEnabled(124))
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableImmortality(character)
    OR_2.Add(FlagEnabled(124))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    
    MAIN.Await(OR_2)
    
    if FlagDisabled(124):
        ForceAnimation(character, 20003, wait_for_completion=True)
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@RestartOnRest(21002500)
def Event_21002500():
    """Event 21002500"""
    DisableAnimations(21000509)
    DisableGravity(21000509)
    SetLockOnPoint(character=21000509, lock_on_dummy_id=220, state=False)
    SetTeamType(21000509, TeamType.NoTeam)
    DisableAI(21000509)
    GotoIfFlagDisabled(Label.L0, flag=124)
    DisableAssetActivation(21001500, obj_act_id=-1)
    ForceAnimation(21001500, 12)
    DisableAssetInvulnerability(21001502)
    DisableAsset(21006500)
    DisableMapCollision(collision=21007500)
    MoveAssetToCharacter(21001509, character=21000509)
    EndOfAnimation(asset=21001509, animation_id=10)
    EnableCharacter(21005500)
    Wait(1.0)
    EnableCharacter(21005470)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(21005500)
    DisableCharacter(21005470)
    EnableAssetInvulnerability(21001502)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AssetActivated(obj_act_id=21003500))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(124)
    EnableNetworkFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=21000020,
            cutscene_flags=0,
            move_to_region=21002500,
            map_id=21000000,
            player_id=10000,
            unk_20_24=21000000,
            unk_24_25=False,
        )
    else:
        PlayCutscene(21000020, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    DisableAssetInvulnerability(21001502)
    DisableAsset(21006500)
    DisableMapCollision(collision=21007500)
    MoveAssetToCharacter(21001509, character=21000509)
    EndOfAnimation(asset=21001509, animation_id=10)
    EnableCharacter(21005500)
    Wait(1.0)
    EnableCharacter(21005470)


@RestartOnRest(21002505)
def Event_21002505():
    """Event 21002505"""
    DisableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9710, entity=21001576))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    EnableFlag(9021)
    SetRespawnPoint(respawn_point=2049472020)
    SaveRequest()
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=21000000,
        cutscene_flags=0,
        move_to_region=2049472020,
        map_id=61494700,
        player_id=10000,
        unk_20_24=21000000,
        unk_24_25=False,
    )
    WaitRealFrames(frames=1)
    PlayCutscene(21000010, cutscene_flags=CutsceneFlags.Unknown16, player_id=10000)
    WaitFrames(frames=1)
    Wait(1.0)


@ContinueOnRest(21002510)
def Event_21002510():
    """Event 21002510"""
    CommonFunc_90005500(
        0,
        flag=21000510,
        flag_1=21000511,
        left=0,
        asset=21001510,
        asset_1=21001511,
        obj_act_id=21003511,
        asset_2=21001512,
        obj_act_id_1=21003512,
        region=21002511,
        region_1=21002512,
        flag_2=21000512,
        flag_3=21000513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21000515,
        flag_1=21000516,
        left=0,
        asset=21001515,
        asset_1=21001516,
        obj_act_id=21003516,
        asset_2=21001517,
        obj_act_id_1=21003517,
        region=21002516,
        region_1=21002517,
        flag_2=21000517,
        flag_3=21000518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21000520,
        flag_1=21000521,
        left=0,
        asset=21001520,
        asset_1=21001521,
        obj_act_id=21003521,
        asset_2=21001522,
        obj_act_id_1=21003522,
        region=21002521,
        region_1=21002522,
        flag_2=21000522,
        flag_3=21000523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21000525,
        flag_1=21000526,
        left=1,
        asset=21001525,
        asset_1=21001526,
        obj_act_id=21003526,
        asset_2=21001527,
        obj_act_id_1=21003527,
        region=21002526,
        region_1=21002527,
        flag_2=21000527,
        flag_3=21000528,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21000530,
        flag_1=21000531,
        left=0,
        asset=21001530,
        asset_1=21001531,
        obj_act_id=21003531,
        asset_2=21001532,
        obj_act_id_1=21003532,
        region=21002531,
        region_1=21002532,
        flag_2=21000532,
        flag_3=21000533,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=21000535,
        flag_1=21000536,
        left=0,
        asset=21001535,
        asset_1=21001536,
        obj_act_id=21003536,
        asset_2=21001537,
        obj_act_id_1=21003537,
        region=21002536,
        region_1=21002537,
        flag_2=21000537,
        flag_3=21000538,
        left_1=0,
    )


@RestartOnRest(21002515)
def Event_21002515(_, asset: uint):
    """Event 21002515"""
    DisableNetworkSync()
    if FlagEnabled(124):
        EnableAssetActivation(asset, obj_act_id=-1)
        End()
    WaitFrames(frames=2)
    DisableAssetActivation(asset, obj_act_id=-1)
    OR_2.Add(ActionButtonParamActivated(action_button_id=8301, entity=asset))
    OR_3.Add(OR_2)
    OR_3.Add(FlagEnabled(124))
    
    MAIN.Await(OR_3)
    
    if FlagDisabled(124):
        DisplayDialog(text=4000, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(21002520)
def Event_21002520():
    """Event 21002520"""
    DisableNetworkSync()
    if FlagEnabled(21000850):
        EnableAssetActivation(21001540, obj_act_id=-1)
        Goto(Label.L0)
    WaitFrames(frames=1)
    DisableAssetActivation(21001540, obj_act_id=-1)
    AND_1.Add(FlagEnabled(21000850))
    
    MAIN.Await(AND_1)
    
    EnableAssetActivation(21001540, obj_act_id=-1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=7101, entity=21001540))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(21008540))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(21008540):
        return
    DisplayDialog(text=4010, anchor_entity=21001540, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(21002580)
def Event_21002580():
    """Event 21002580"""
    RegisterLadder(start_climbing_flag=21000580, stop_climbing_flag=21000581, asset=21001580)
    RegisterLadder(start_climbing_flag=21000582, stop_climbing_flag=21000583, asset=21001582)
    RegisterLadder(start_climbing_flag=21000584, stop_climbing_flag=21000585, asset=21001584)
    RegisterLadder(start_climbing_flag=21000586, stop_climbing_flag=21000587, asset=21001586)


@RestartOnRest(21002600)
def Event_21002600(_, flag: Flag | int, asset: uint, item_lot: int):
    """Event 21002600"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    DeleteAssetVFX(asset, erase_root=False)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=806845)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=asset))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot, host_only=True)


@RestartOnRest(21002850)
def Event_21002850():
    """Event 21002850"""
    if FlagEnabled(21000850):
        return
    
    MAIN.Await(HealthValue(21000850) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(21000850, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(21000850))
    
    KillBossAndDisplayBanner(character=21000850, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(21000850)
    EnableFlag(9144)
    if PlayerInOwnWorld():
        EnableFlag(61144)


@RestartOnRest(21002860)
def Event_21002860():
    """Event 21002860"""
    GotoIfFlagDisabled(Label.L0, flag=21000850)
    DisableCharacter(21005850)
    DisableAnimations(21005850)
    Kill(21005850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(21005850)
    GotoIfFlagEnabled(Label.L1, flag=21000851)
    AddSpecialEffect(21000100, 9531)
    ForceAnimation(21000850, 30000)
    DisableAnimations(21000850)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=21002851))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=21000850, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(21000851)
    ForceAnimation(21000850, 20000)
    EnableAnimations(21000850)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(21002855))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=21002850))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(21005850)
    SetNetworkUpdateRate(21005800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(21000100, 9532)
    Wait(0.5)
    EnableBossHealthBar(21000850, name=905010000)


@RestartOnRest(21002861)
def Event_21002861():
    """Event 21002861"""
    if FlagEnabled(21000850):
        return
    AND_1.Add(CharacterHasSpecialEffect(21000850, 10010050))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    EnableNetworkFlag(21002852)


@RestartOnRest(21002890)
def Event_21002890(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    character: Character | int,
    region: uint,
    region_1: Region | int,
    animation: int,
):
    """Event 21002890"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterInsideRegion(character=character, region=21002890))
    GotoIfConditionTrue(Label.L10, input_condition=AND_2)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region_1))
    
    if ValueNotEqual(left=animation, right=0):
        FaceEntityAndForceAnimation(character, region, animation=animation, wait_for_completion=True)
    else:
        FaceEntityAndForceAnimation(character, region, animation=60060, wait_for_completion=True)
    OR_4.Add(TimeElapsed(seconds=3.0))
    OR_5.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_5)
    
    if LastResult(OR_4):
        return RESTART
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)

    # --- Label 10 --- #
    DefineLabel(10)
    End()


@RestartOnRest(21002899)
def Event_21002899():
    """Event 21002899"""
    CommonFunc_9005800(
        0,
        flag=21000850,
        entity=21001850,
        region=21002850,
        flag_1=21002855,
        character=21005850,
        action_button_id=10000,
        left=21000851,
        region_1=21002851,
    )
    CommonFunc_9005801(
        0,
        flag=21000850,
        entity=21001850,
        region=21002850,
        flag_1=21002855,
        flag_2=21002856,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=21000850, asset=21001850, vfx_id=5, right=21000851)
    CommonFunc_9005822(
        0,
        flag=21000850,
        bgm_boss_conv_param_id=920600,
        flag_1=21002855,
        flag_2=21002856,
        right=0,
        flag_3=21002852,
        left=0,
        left_1=0,
    )
    CommonFunc_9005812(0, flag=21000850, asset=21001851, vfx_id=5, right=21000851, vfx_id_1=0)
    CommonFunc_9005812(0, flag=21000850, asset=21001852, vfx_id=5, right=21000851, vfx_id_1=0)


@RestartOnRest(21000700)
def Event_21000700(
    _,
    character: uint,
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
    animation_id: int,
    distance: float,
    animation_id_1: int,
    flag_11: Flag | int,
):
    """Event 21000700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableFlag(flag_11)
    OR_1.Add(FlagEnabled(flag_5))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    OR_2.Add(FlagEnabled(flag_5))
    AND_2.Add(FlagEnabled(flag_4))
    AND_2.Add(FlagEnabled(flag_6))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    if FlagEnabled(flag_6):
        EnableFlag(flag_7)
        WaitFrames(frames=1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L2, flag=flag_1)
    GotoIfFlagEnabled(Label.L3, flag=flag_2)
    GotoIfFlagEnabled(Label.L4, flag=flag_3)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_5.Add(FlagEnabled(flag_8))
    AND_5.Add(FlagEnabled(flag_9))
    if AND_5:
        return
    EnableCharacter(character)
    EnableBackread(character)
    EnableFlag(flag_11)
    SetTeamType(character, TeamType.FriendlyNPC)
    EnableInvincibility(character)
    AND_6.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_6)
    
    ResetCharacterPosition(character=character)
    AND_10.Add(FlagEnabled(flag_8))
    AND_10.Add(FlagEnabled(flag_10))
    SkipLinesIfConditionFalse(2, AND_10)
    ForceAnimation(character, animation_id)
    Goto(Label.L20)
    SetCharacterTalkRange(character=character, distance=distance)
    ForceAnimation(character, animation_id_1)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_15.Add(FlagEnabled(flag_5))
    
    MAIN.Await(not OR_15)
    
    Restart()


@RestartOnRest(21000701)
def Event_21000701(_, flag: Flag | int, region: Region | int, flag_1: Flag | int):
    """Event 21000701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    EnableFlag(flag_1)
    End()


@RestartOnRest(21000702)
def Event_21000702(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    dummy_id: int,
    asset: uint,
    dummy_id_1: short,
    radius: float,
    animation: int,
    animation_id: int,
    special_effect: int,
    radius_1: float,
    seconds: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds_1: float,
    flag_5: Flag | int,
    animation_1: int,
    flag_6: Flag | int,
):
    """Event 21000702"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_4)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=dummy_id, right=0)
    GotoIfUnsignedEqual(Label.L0, left=asset, right=0)
    MoveAssetToCharacter(asset, character=character, dummy_id=dummy_id_1)
    WaitRealFrames(frames=1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLinesIfConditionFalse(3, AND_1)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius_1))
    AND_15.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius_1))
    SkipLinesIfConditionFalse(3, AND_15)
    EnableFlag(flag_1)
    EnableFlag(flag_4)
    Goto(Label.L15)
    FaceEntityAndForceAnimation(PLAYER, asset, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, asset, animation=90006)
    Goto(Label.L8)

    # --- Label 0 --- #
    DefineLabel(0)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L9, input_condition=AND_1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=90006)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableFlag(flag_2)
    WaitRealFrames(frames=1)
    DisableFlag(flag_2)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(TimeElapsed(seconds=seconds))
    OR_1.Add(AND_2)
    OR_1.Add(OR_2)
    SkipLinesIfValueEqual(3, left=dummy_id, right=0)
    SkipLinesIfUnsignedEqual(2, left=asset, right=0)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=asset, radius=radius))
    SkipLines(1)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L19, input_condition=OR_2)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(flag_1)
    SkipLinesIfValueEqual(5, left=dummy_id, right=0)
    ResetAnimation(PLAYER)
    SkipLinesIfFlagEnabled(3, flag_4)
    FaceEntityAndForceAnimation(PLAYER, character, wait_for_completion=True)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    Goto(Label.L15)
    EnableFlag(flag_3)
    Wait(seconds_1)

    # --- Label 15 --- #
    DefineLabel(15)
    if UnsignedNotEqual(left=left, right=0):
        EnableFlag(left)
    if ValueNotEqual(left=dummy_id, right=0):
        Move(
            PLAYER,
            destination=character,
            destination_type=CoordEntityType.Character,
            dummy_id=dummy_id,
            short_move=True,
        )
    SkipLinesIfValueEqual(2, left=special_effect, right=-1)
    FaceEntityAndForceAnimation(PLAYER, character, animation=animation)
    SkipLines(1)
    if FlagEnabled(flag_5):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation, wait_for_completion=True)
    if FlagEnabled(flag_6):
        FaceEntityAndForceAnimation(PLAYER, character, animation=animation_1, wait_for_completion=True)
    Goto(Label.L8)

    # --- Label 8 --- #
    DefineLabel(8)
    WaitRealFrames(frames=1)
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_3.Add(FlagDisabled(flag))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_3)
    GotoIfValueComparison(Label.L18, comparison_type=ComparisonType.Equal, left=animation_id, right=-1)
    GotoIfValueComparison(Label.L10, comparison_type=ComparisonType.Equal, left=special_effect, right=-1)
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9900))
    OR_4.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfLastConditionResultTrue(Label.L20, input_condition=AND_4)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableFlag(flag_1)
    ForceAnimation(PLAYER, animation_id, wait_for_completion=True)
    Restart()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableFlag(flag_1)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag)
    ForceAnimation(PLAYER, 0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(21000703)
def Event_21000703(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    left: Flag | int,
    character: uint,
    animation__animation_id: int,
    left_1: uint,
    left_2: int,
    special_effect: int,
    seconds: float,
    flag_2: Flag | int,
    animation__animation_id_1: int,
    flag_3: Flag | int,
):
    """Event 21000703"""
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    if UnsignedNotEqual(left=left, right=0):
        DisableFlag(left)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=1)
    SkipLinesIfValueEqual(5, left=special_effect, right=-1)
    SkipLinesIfFlagDisabled(1, flag_2)
    ForceAnimation(character, animation__animation_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    ForceAnimation(character, animation__animation_id_1)
    SkipLines(1)
    if FlagEnabled(flag_2):
        ForceAnimation(character, animation__animation_id)
    if FlagEnabled(flag_3):
        ForceAnimation(character, animation__animation_id_1)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(5, left=special_effect, right=-1)
    SkipLinesIfFlagDisabled(1, flag_2)
    FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    SkipLinesIfFlagDisabled(1, flag_3)
    FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id_1)
    SkipLines(1)
    if FlagEnabled(flag_2):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id)
    if FlagEnabled(flag_3):
        FaceEntityAndForceAnimation(character, PLAYER, animation=animation__animation_id_1)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_1.Add(FlagDisabled(flag))
    if ValueNotEqual(left=special_effect, right=-1):
        AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    GotoIfValueComparison(Label.L19, comparison_type=ComparisonType.Equal, left=left_2, right=-1)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(flag_1)
    Wait(seconds)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(21000704)
def Event_21000704(_, flag: Flag | int, flag_1: Flag | int, seconds: float):
    """Event 21000704"""
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)
    Wait(seconds)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@RestartOnRest(21000705)
def Event_21000705(
    _,
    character: uint,
    flag: Flag | int,
    flag_1: Flag | int,
    animation_id: int,
    flag_2: Flag | int,
    animation_id_1: int,
    flag_3: Flag | int,
    flag_4: Flag | int,
    seconds: float,
    flag_5: Flag | int,
    item_lot: int,
    flag_6: Flag | int,
):
    """Event 21000705"""
    if PlayerNotInOwnWorld():
        return
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    
    MAIN.Await(FlagEnabled(flag))
    
    if FlagEnabled(flag_2):
        ForceAnimation(character, animation_id)
    if FlagEnabled(flag_3):
        ForceAnimation(character, animation_id_1)
    EnableFlag(flag_4)
    Wait(seconds)
    if FlagEnabled(flag_2):
        DisableCharacter(character)
        DisableBackread(character)
        AwardItemLot(item_lot, host_only=False)
        DisableFlag(flag_6)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(flag_3):
        EnableFlag(flag_5)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(flag):
        return RESTART
    if FlagEnabled(flag_1):
        return


@RestartOnRest(21000706)
def Event_21000706(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 21000706"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_3))
    if AND_1:
        return
    if FlagEnabled(flag):
        EnableNetworkFlag(flag_1)
    if FlagEnabled(flag_2):
        EnableNetworkFlag(flag_3)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    if OR_1:
        return RESTART


@RestartOnRest(21000711)
def Event_21000711(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    first_flag: Flag | int,
    last_flag: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 21000711"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag_1)
    DisableNetworkFlag(flag_2)
    DisableNetworkFlag(flag_3)
    SaveRequest()
    EnableFlag(4378)


@RestartOnRest(21000712)
def Event_21000712(_, character: Character | int, flag: Flag | int, flag_1: Flag | int):
    """Event 21000712"""
    WaitFrames(frames=1)
    OR_10.Add(FlagEnabled(flag_1))
    if OR_10:
        return
    AND_4.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_4.Add(CharacterAlive(character))
    
    MAIN.Await(AND_4)
    
    EnableFlag(flag)


@RestartOnRest(21000714)
def Event_21000714(_, flag: Flag | int, character: Character | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 21000714"""
    WaitFrames(frames=1)
    OR_10.Add(FlagEnabled(flag_2))
    if OR_10:
        return
    OR_1.Add(HealthValue(PLAYER) <= 0)
    OR_1.Add(HealthValue(character) <= 0)
    
    MAIN.Await(OR_1)
    
    AND_2.Add(HealthValue(PLAYER) <= 0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    AND_3.Add(HealthValue(character) <= 0)
    SkipLinesIfConditionFalse(1, AND_3)
    EnableFlag(flag_1)


@RestartOnRest(21000725)
def Event_21000725(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 21000725"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    End()


@RestartOnRest(21000735)
def Event_21000735(_, character: Character | int, character_1: Character | int, ceremony: int):
    """Event 21000735"""
    WaitFrames(frames=1)
    if CeremonyInactive(ceremony=ceremony):
        return
    OR_1.Add(HealthValue(character) <= 0)
    OR_1.Add(CharacterDead(character))
    
    MAIN.Await(OR_1)
    
    DisableAI(character_1)
