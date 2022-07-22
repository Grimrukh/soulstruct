"""
Southeast Caelid (NW) (SW)

linked:
0
82
148

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\m60.emevd
148: N:\\GR\\data\\Param\\event\\common_macro.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_52_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=310,
        grace_flag=1052380000,
        character=Characters.TalkDummy,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    Event_1052382699()
    CommonFunc_90005646(
        0,
        flag=76422,
        left_flag=1052382690,
        cancel_flag__right_flag=1052382691,
        asset=Assets.AEG099_065_9000,
        player_start=1050362690,
        area_id=60,
        block_id=50,
        cc_id=36,
        dd_id=0,
    )
    Event_1252380700(0, character=Characters.Blaidd1)
    CommonFunc_90005704(0, attacked_entity=Characters.Blaidd1, flag=3601, flag_1=3600, flag_2=1052389301, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Blaidd1,
        flag=3601,
        flag_1=3602,
        flag_2=1052389301,
        flag_3=3603,
        first_flag=3600,
        last_flag=3603,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Blaidd1, flag=3603, first_flag=3600, last_flag=3604)
    Event_1252380705(0, character=Characters.LivingPot1)
    CommonFunc_90005704(0, attacked_entity=Characters.LivingPot1, flag=3661, flag_1=3660, flag_2=1043399301, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.LivingPot1,
        flag=3661,
        flag_1=3662,
        flag_2=1043399301,
        flag_3=3661,
        first_flag=3660,
        last_flag=3663,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.LivingPot1, flag=3663, first_flag=3660, last_flag=3664)
    Event_1252380710()
    Event_1252380720()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1052380700)
    DisableBackread(1052380710)
    DisableBackread(1052380715)
    DisableBackread(1052380720)
    DisableBackread(Characters.Blaidd1)
    DisableBackread(1052380730)
    DisableBackread(1052380735)


@ContinueOnRest(200)
def Event_200():
    """Event 200"""
    Event_1252382800()
    Event_1252382810()
    Event_1252382820()
    Event_1252382850()
    Event_1252382680(0, asset=Assets.AEG007_299_1003)
    Event_1252382680(1, asset=Assets.AEG007_299_1013)
    Event_1252382680(2, asset=Assets.AEG007_299_9000)
    Event_1252382680(3, asset=Assets.AEG007_299_9001)
    Event_1252382680(4, asset=Assets.AEG007_299_9002)
    Event_1252382680(5, asset=Assets.AEG007_299_9003)
    Event_1252382680(6, asset=Assets.AEG007_299_9004)
    Event_1252382680(7, asset=Assets.AEG007_299_9005)
    Event_1252382680(8, asset=Assets.AEG007_299_9007)
    Event_1252382680(9, asset=Assets.AEG007_299_9006)
    Event_1252382860()
    Event_1252382696()
    Event_1252382695()
    Event_1252382200(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9000,
        action_button_id=9540,
    )
    Event_1252382280(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9000,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9000,
    )
    Event_1252382440(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9000,
        animation_id=63040,
    )
    Event_1252382520(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        0,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9002,
        action_button_id=9542,
    )
    Event_1252382280(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9002,
        animation_id=20040,
        text=80820,
    )
    Event_1252382360(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9002,
    )
    Event_1252382440(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9002,
        animation_id=63040,
    )
    Event_1252382520(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=Assets.AEG099_090_9082,
    )
    Event_1252382600(
        2,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822,
    )
    Event_1252382200(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9006,
        action_button_id=9546,
    )
    Event_1252382280(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9006,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9006,
    )
    Event_1252382440(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9006,
        animation_id=63040,
    )
    Event_1252382520(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        6,
        character=Characters.Human1,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9008,
        action_button_id=9540,
    )
    Event_1252382280(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9008,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9008,
    )
    Event_1252382440(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9008,
        animation_id=63040,
    )
    Event_1252382520(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        8,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9009,
        action_button_id=9541,
    )
    Event_1252382280(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9009,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9009,
    )
    Event_1252382440(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9009,
        animation_id=63040,
    )
    Event_1252382520(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        9,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9012,
        action_button_id=9544,
    )
    Event_1252382280(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9012,
        animation_id=63021,
        text=80840,
    )
    Event_1252382360(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9012,
    )
    Event_1252382440(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9012,
        animation_id=63040,
    )
    Event_1252382520(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=Assets.AEG099_090_9084,
    )
    Event_1252382600(
        12,
        character=Characters.Okina,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842,
    )
    Event_1252382200(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9013,
        action_button_id=9545,
    )
    Event_1252382280(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9013,
        animation_id=63021,
        text=80850,
    )
    Event_1252382360(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9013,
    )
    Event_1252382440(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9013,
        animation_id=63040,
    )
    Event_1252382520(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=Assets.AEG099_090_9085,
    )
    Event_1252382600(
        13,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852,
    )
    Event_1252382200(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9014,
        action_button_id=9546,
    )
    Event_1252382280(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9014,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9014,
    )
    Event_1252382440(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9014,
        animation_id=63040,
    )
    Event_1252382520(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        14,
        character=Characters.Human1,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9016,
        action_button_id=9540,
    )
    Event_1252382280(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9016,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9016,
    )
    Event_1252382440(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9016,
        animation_id=63040,
    )
    Event_1252382520(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        16,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9017,
        action_button_id=9541,
    )
    Event_1252382280(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9017,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9017,
    )
    Event_1252382440(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9017,
        animation_id=63040,
    )
    Event_1252382520(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        17,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9018,
        action_button_id=9542,
    )
    Event_1252382280(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9018,
        animation_id=20040,
        text=80820,
    )
    Event_1252382360(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9018,
    )
    Event_1252382440(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9018,
        animation_id=63040,
    )
    Event_1252382520(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=Assets.AEG099_090_9082,
    )
    Event_1252382600(
        18,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822,
    )
    Event_1252382200(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9019,
        action_button_id=9543,
    )
    Event_1252382280(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9019,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9019,
    )
    Event_1252382440(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9019,
        animation_id=63040,
    )
    Event_1252382520(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        19,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9021,
        action_button_id=9545,
    )
    Event_1252382280(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9021,
        animation_id=63021,
        text=80850,
    )
    Event_1252382360(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9021,
    )
    Event_1252382440(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9021,
        animation_id=63040,
    )
    Event_1252382520(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=Assets.AEG099_090_9085,
    )
    Event_1252382600(
        21,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852,
    )
    Event_1252382200(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9023,
        action_button_id=9547,
    )
    Event_1252382280(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9023,
        animation_id=63021,
        text=80870,
    )
    Event_1252382360(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9023,
    )
    Event_1252382440(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9023,
        animation_id=63040,
    )
    Event_1252382520(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=Assets.AEG099_090_9087,
    )
    Event_1252382600(
        23,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872,
    )
    Event_1252382200(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9024,
        action_button_id=9540,
    )
    Event_1252382280(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9024,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9024,
    )
    Event_1252382440(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9024,
        animation_id=63040,
    )
    Event_1252382520(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        24,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9025,
        action_button_id=9541,
    )
    Event_1252382280(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9025,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9025,
    )
    Event_1252382440(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9025,
        animation_id=63040,
    )
    Event_1252382520(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        25,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9029,
        action_button_id=9545,
    )
    Event_1252382280(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9029,
        animation_id=63021,
        text=80850,
    )
    Event_1252382360(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9029,
    )
    Event_1252382440(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9029,
        animation_id=63040,
    )
    Event_1252382520(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=Assets.AEG099_090_9085,
    )
    Event_1252382600(
        29,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852,
    )
    Event_1252382200(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9035,
        action_button_id=9543,
    )
    Event_1252382280(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9035,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9035,
    )
    Event_1252382440(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9035,
        animation_id=63040,
    )
    Event_1252382520(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        35,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9036,
        action_button_id=9544,
    )
    Event_1252382280(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9036,
        animation_id=63021,
        text=80840,
    )
    Event_1252382360(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9036,
    )
    Event_1252382440(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9036,
        animation_id=63040,
    )
    Event_1252382520(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=Assets.AEG099_090_9084,
    )
    Event_1252382600(
        36,
        character=Characters.Okina,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842,
    )
    Event_1252382200(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9038,
        action_button_id=9546,
    )
    Event_1252382280(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9038,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9038,
    )
    Event_1252382440(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9038,
        animation_id=63040,
    )
    Event_1252382520(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        38,
        character=Characters.Human1,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9040,
        action_button_id=9540,
    )
    Event_1252382280(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9040,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9040,
    )
    Event_1252382440(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9040,
        animation_id=63040,
    )
    Event_1252382520(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        40,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9041,
        action_button_id=9541,
    )
    Event_1252382280(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9041,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9041,
    )
    Event_1252382440(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9041,
        animation_id=63040,
    )
    Event_1252382520(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        41,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9043,
        action_button_id=9543,
    )
    Event_1252382280(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9043,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9043,
    )
    Event_1252382440(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9043,
        animation_id=63040,
    )
    Event_1252382520(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        43,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9044,
        action_button_id=9544,
    )
    Event_1252382280(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9044,
        animation_id=63021,
        text=80840,
    )
    Event_1252382360(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9044,
    )
    Event_1252382440(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9044,
        animation_id=63040,
    )
    Event_1252382520(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=Assets.AEG099_090_9084,
    )
    Event_1252382600(
        44,
        character=Characters.Okina,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842,
    )
    Event_1252382200(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9045,
        action_button_id=9545,
    )
    Event_1252382280(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9045,
        animation_id=63021,
        text=80850,
    )
    Event_1252382360(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9045,
    )
    Event_1252382440(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9045,
        animation_id=63040,
    )
    Event_1252382520(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=Assets.AEG099_090_9085,
    )
    Event_1252382600(
        45,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852,
    )
    Event_1252382200(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9047,
        action_button_id=9547,
    )
    Event_1252382280(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9047,
        animation_id=63021,
        text=80870,
    )
    Event_1252382360(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9047,
    )
    Event_1252382440(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9047,
        animation_id=63040,
    )
    Event_1252382520(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=Assets.AEG099_090_9087,
    )
    Event_1252382600(
        47,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872,
    )
    Event_1252382200(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9048,
        action_button_id=9540,
    )
    Event_1252382280(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9048,
        animation_id=63021,
        text=80800,
    )
    Event_1252382360(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        asset=Assets.AEG099_090_9048,
    )
    Event_1252382440(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=Assets.AEG099_090_9048,
        animation_id=63040,
    )
    Event_1252382520(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=Assets.AEG099_090_9080,
    )
    Event_1252382600(
        48,
        character=Characters.CastellanJerren,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802,
    )
    Event_1252382200(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9051,
        action_button_id=9543,
    )
    Event_1252382280(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9051,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9051,
    )
    Event_1252382440(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9051,
        animation_id=63040,
    )
    Event_1252382520(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        51,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9052,
        action_button_id=9544,
    )
    Event_1252382280(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9052,
        animation_id=63021,
        text=80840,
    )
    Event_1252382360(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9052,
    )
    Event_1252382440(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9052,
        animation_id=63040,
    )
    Event_1252382520(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=Assets.AEG099_090_9084,
    )
    Event_1252382600(
        52,
        character=Characters.Okina,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842,
    )
    Event_1252382200(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9053,
        action_button_id=9545,
    )
    Event_1252382280(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9053,
        animation_id=63021,
        text=80850,
    )
    Event_1252382360(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        asset=Assets.AEG099_090_9053,
    )
    Event_1252382440(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=Assets.AEG099_090_9053,
        animation_id=63040,
    )
    Event_1252382520(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=Assets.AEG099_090_9085,
    )
    Event_1252382600(
        53,
        character=Characters.FingerMaidenTherolina,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852,
    )
    Event_1252382200(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9054,
        action_button_id=9546,
    )
    Event_1252382280(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9054,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9054,
    )
    Event_1252382440(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9054,
        animation_id=63040,
    )
    Event_1252382520(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        54,
        character=Characters.Human1,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9055,
        action_button_id=9547,
    )
    Event_1252382280(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9055,
        animation_id=63021,
        text=80870,
    )
    Event_1252382360(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9055,
    )
    Event_1252382440(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9055,
        animation_id=63040,
    )
    Event_1252382520(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=Assets.AEG099_090_9087,
    )
    Event_1252382600(
        55,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872,
    )
    Event_1252382200(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9057,
        action_button_id=9541,
    )
    Event_1252382280(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9057,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9057,
    )
    Event_1252382440(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9057,
        animation_id=63040,
    )
    Event_1252382520(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        57,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9059,
        action_button_id=9543,
    )
    Event_1252382280(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9059,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9059,
    )
    Event_1252382440(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9059,
        animation_id=63040,
    )
    Event_1252382520(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        59,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9062,
        action_button_id=9546,
    )
    Event_1252382280(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9062,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9062,
    )
    Event_1252382440(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9062,
        animation_id=63040,
    )
    Event_1252382520(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        62,
        character=Characters.Human1,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9066,
        action_button_id=9542,
    )
    Event_1252382280(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9066,
        animation_id=20040,
        text=80820,
    )
    Event_1252382360(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        asset=Assets.AEG099_090_9066,
    )
    Event_1252382440(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=Assets.AEG099_090_9066,
        animation_id=63040,
    )
    Event_1252382520(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=Assets.AEG099_090_9082,
    )
    Event_1252382600(
        66,
        character=Characters.LivingPot0,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822,
    )
    Event_1252382200(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9068,
        action_button_id=9544,
    )
    Event_1252382280(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9068,
        animation_id=63021,
        text=80840,
    )
    Event_1252382360(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        asset=Assets.AEG099_090_9068,
    )
    Event_1252382440(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=Assets.AEG099_090_9068,
        animation_id=63040,
    )
    Event_1252382520(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=Assets.AEG099_090_9084,
    )
    Event_1252382600(
        68,
        character=Characters.Okina,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842,
    )
    Event_1252382200(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9073,
        action_button_id=9541,
    )
    Event_1252382280(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9073,
        animation_id=20054,
        text=80810,
    )
    Event_1252382360(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        asset=Assets.AEG099_090_9073,
    )
    Event_1252382440(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=Assets.AEG099_090_9073,
        animation_id=63040,
    )
    Event_1252382520(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=Assets.AEG099_090_9081,
    )
    Event_1252382600(
        73,
        character=Characters.Blaidd0,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812,
    )
    Event_1252382200(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9075,
        action_button_id=9543,
    )
    Event_1252382280(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9075,
        animation_id=63021,
        text=80830,
    )
    Event_1252382360(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        asset=Assets.AEG099_090_9075,
    )
    Event_1252382440(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=Assets.AEG099_090_9075,
        animation_id=63040,
    )
    Event_1252382520(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=Assets.AEG099_090_9083,
    )
    Event_1252382600(
        75,
        character=Characters.GreatHornedTragoth,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832,
    )
    Event_1252382200(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9078,
        action_button_id=9546,
    )
    Event_1252382280(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9078,
        animation_id=63021,
        text=80860,
    )
    Event_1252382360(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        asset=Assets.AEG099_090_9078,
    )
    Event_1252382440(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=Assets.AEG099_090_9078,
        animation_id=63040,
    )
    Event_1252382520(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=Assets.AEG099_090_9086,
    )
    Event_1252382600(
        78,
        character=Characters.Human1,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862,
    )
    Event_1252382200(
        79,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9079,
        action_button_id=9547,
    )
    Event_1252382280(
        79,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9079,
        animation_id=63021,
        text=80870,
    )
    Event_1252382360(
        79,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        asset=Assets.AEG099_090_9079,
    )
    Event_1252382440(
        79,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=Assets.AEG099_090_9079,
        animation_id=63040,
    )
    Event_1252382520(
        79,
        character=Characters.Patches,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=Assets.AEG099_090_9087,
    )
    Event_1252382600(79, 1052380340, 1052389250, 1252382179, 1252382187, 1252382197, 0, 0, 80872)


@RestartOnRest(1252382200)
def Event_1252382200(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    destination: uint,
    action_button_id: int,
):
    """Event 1252382200"""
    if FlagEnabled(1252380800):
        return
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        GotoIfFlagDisabled(Label.L3, flag=left)
    AND_1.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=destination))
    AND_2.Add(FlagDisabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(1252380800))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    if FlagEnabled(1252380800):
        return

    # --- Label 1 --- #
    DefineLabel(1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    WaitFrames(frames=1)
    SkipLinesIfSingleplayer(1)
    if PlayerInOwnWorld():
        Move(
            character,
            destination=destination,
            destination_type=CoordEntityType.Asset,
            model_point=100,
            copy_draw_parent=PLAYER,
        )
    Wait(1.0)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(FlagDisabled(flag_1))
    AND_3.Add(FlagDisabled(flag_2))
    
    MAIN.Await(AND_3)
    
    WaitFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    
    MAIN.Await(FlagEnabled(left))
    
    Restart()


@RestartOnRest(1252382280)
def Event_1252382280(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    asset: uint,
    animation_id: int,
    text: int,
):
    """Event 1252382280"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetCharacterFadeOnEnable(character=character, state=True)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    if FlagEnabled(1252380800):
        return
    EnableCharacter(character)
    AddSpecialEffect(character, 18677)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    AND_1.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(1252380800):
        DisableCharacter(character)
        DisableAnimations(character)
        DisableCharacterCollision(character)
        DisableGravity(character)
        DisableAI(character)
        End()
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    CreateAssetVFX(asset, vfx_id=100, model_point=30320)
    RemoveSpecialEffect(character, 4380)
    RemoveSpecialEffect(character, 18677)
    EnableCharacter(character)
    EnableInvincibility(character)
    if ValueNotEqual(left=animation_id, right=0):
        ForceAnimation(character, animation_id, wait_for_completion=True)
    EnableAnimations(character)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableImmortality(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.WhitePhantom)
    SetCharacterEventTarget(character, region=1052380800)
    DisplayFlashingMessage(text)
    DeleteAssetVFX(asset)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(1252382360)
def Event_1252382360(_, character: uint, left: uint, flag: uint, flag_1: uint, flag_2: uint, asset: uint):
    """Event 1252382360"""
    GotoIfFlagEnabled(Label.L2, flag=1252380800)
    if PlayerNotInOwnWorld():
        return
    if UnsignedNotEqual(left=left, right=0):
        AND_5.Add(FlagDisabled(left))
        GotoIfConditionTrue(Label.L3, input_condition=AND_5)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagEnabled(flag_2))
    AND_3.Add(CharacterBackreadEnabled(character))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_4.Add(FlagEnabled(flag))
    AND_4.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    CreateAssetVFX(asset, vfx_id=100, model_point=30080)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(1252380800))
    
    MAIN.Await(OR_1)
    
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset)
    OR_2.Add(FlagDisabled(flag_2))
    OR_2.Add(FlagEnabled(1252380800))
    
    MAIN.Await(OR_2)
    
    AND_6.Add(FlagEnabled(flag))
    GotoIfConditionTrue(Label.L2, input_condition=AND_6)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DeleteAssetVFX(asset)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    
    MAIN.Await(FlagEnabled(left))
    
    Restart()


@RestartOnRest(1252382440)
def Event_1252382440(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    destination: uint,
    animation_id: int,
):
    """Event 1252382440"""
    if FlagEnabled(1252380800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L1, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=destination, radius=15.0))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAI(character)
    AddSpecialEffect(character, 4380)
    WaitFrames(frames=1)
    if PlayerInOwnWorld():
        SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    WaitFrames(frames=1)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    WaitFrames(frames=1)
    RemoveSpecialEffect(character, 18677)
    DisableInvincibility(character)
    DisableAnimations(character)
    DisableCharacterCollision(character)
    DisableGravity(character)
    WaitFrames(frames=1)
    if ValueNotEqual(left=animation_id, right=0):
        ForceAnimation(character, animation_id, loop=True)
    AND_2.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=left, right=0):
        AND_2.Add(FlagEnabled(left))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=destination, radius=15.0))
    
    MAIN.Await(AND_2)
    
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagDisabled(flag_2))
    
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(1252382520)
def Event_1252382520(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    animation_id: int,
    animation_id_1: int,
    text: int,
    destination: uint,
):
    """Event 1252382520"""
    if FlagEnabled(1252380800):
        return
    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(HealthRatio(character) <= 0.009999999776482582)
    
    MAIN.Await(AND_1)
    
    EnableInvincibility(character)
    DisableAnimations(character)
    SetTeamType(character, TeamType.NoTeam)
    Wait(0.10000000149011612)
    DisableCharacterCollision(character)
    DisableGravity(character)
    ClearTargetList(character)
    SkipLinesIfValueEqual(5, left=animation_id, right=0)
    SkipLinesIfValueEqual(1, left=animation_id, right=90009)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    SkipLinesIfValueNotEqual(2, left=animation_id, right=90009)
    ForceAnimation(character, animation_id)
    WaitFrames(frames=200)
    if ValueNotEqual(left=animation_id_1, right=0):
        ForceAnimation(character, animation_id_1, loop=True)
    if ValueEqual(left=animation_id, right=90009):
        AddSpecialEffect(character, 18677)
        Wait(3.0)
    DisplayFlashingMessage(text)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 20, loop=True)
    AddSpecialEffect(character, 4380)
    Wait(30.0)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Asset,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    ClearTargetList(character)
    WaitFrames(frames=1)
    ReplanAI(character)
    RemoveSpecialEffect(character, 18677)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    if PlayerNotInOwnWorld():
        return
    GotoIfUnsignedEqual(Label.L0, left=character, right=1052380340)
    EnableFlag(flag)
    GotoIfFlagEnabled(Label.L0, flag=1252380800)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(1252382600)
def Event_1252382600(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    left_1: uint,
    animation_id: int,
    text: int,
):
    """Event 1252382600"""
    if FlagEnabled(1252380800):
        return
    GotoIfUnsignedEqual(Label.L2, left=character, right=1052380340)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=0)
    AND_1.Add(PlayerInOwnWorld())
    if UnsignedNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(left))
    AND_1.Add(HealthRatio(character) > 0.009999999776482582)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_1.Add(FlagEnabled(1252380800))
    OR_1.Add(FlagEnabled(left_1))
    OR_1.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=200.0))
    AND_1.Add(OR_1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(HealthRatio(character) <= 0.009999999776482582)
    AND_3.Add(FlagEnabled(flag))
    OR_3.Add(AND_1)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(HealthRatio(character) > 0.009999999776482582)
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(CharacterBackreadEnabled(character))
    OR_2.Add(FlagEnabled(1252380800))
    OR_2.Add(EntityBeyondDistance(entity=character, other_entity=PLAYER, radius=200.0))
    AND_2.Add(OR_2)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(CharacterBackreadEnabled(character))
    AND_4.Add(HealthRatio(character) <= 0.009999999776482582)
    AND_4.Add(FlagEnabled(flag))
    OR_4.Add(AND_2)
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    Goto(Label.L1)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_5.Add(PlayerInOwnWorld())
    AND_5.Add(HealthRatio(character) > 0.009999999776482582)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(FlagEnabled(flag_2))
    AND_5.Add(CharacterBackreadEnabled(character))
    AND_6.Add(PlayerInOwnWorld())
    AND_6.Add(CharacterBackreadEnabled(character))
    AND_6.Add(HealthRatio(character) <= 0.009999999776482582)
    AND_6.Add(FlagEnabled(flag))
    OR_6.Add(AND_5)
    OR_6.Add(AND_6)
    
    MAIN.Await(OR_6)
    
    Wait(20.0)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_9.Add(HealthRatio(character) <= 0.009999999776482582)
    if AND_9:
        return
    SetTeamType(character, TeamType.NoTeam)
    DisableAnimations(character)
    EnableInvincibility(character)
    SkipLines(2)
    if ValueNotEqual(left=animation_id, right=0):
        ForceAnimation(character, animation_id, wait_for_completion=True)
    AddSpecialEffect(character, 18677)
    ReplanAI(character)
    ClearTargetList(character)
    Wait(3.0)
    DisableAI(character)
    DisableInvincibility(character)
    ResetAnimation(character, disable_interpolation=True)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.AtLeastEveryTwoFrames)
    AND_10.Add(HealthRatio(character) <= 0.009999999776482582)
    if AND_10:
        return
    if FlagDisabled(1252380800):
        DisplayFlashingMessage(text)
    GotoIfUnsignedEqual(Label.L3, left=character, right=1052380340)
    EnableFlag(flag)
    GotoIfFlagEnabled(Label.L3, flag=1252380800)
    AddSpecialEffect(character, 4380)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(1252382680)
def Event_1252382680(_, asset: uint):
    """Event 1252382680"""
    GotoIfFlagEnabled(Label.L0, flag=9411)
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(9411))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAsset(asset)
    
    MAIN.Await(FlagEnabled(1252380800))

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)


@RestartOnRest(1252382695)
def Event_1252382695():
    """Event 1252382695"""
    DisableNetworkSync()
    DisableBackread(Characters.CastellanJerren)
    DisableBackread(Characters.Blaidd0)
    DisableBackread(Characters.LivingPot0)
    DisableBackread(Characters.GreatHornedTragoth)
    DisableBackread(Characters.Okina)
    DisableBackread(Characters.FingerMaidenTherolina)
    DisableBackread(Characters.Human1)
    DisableBackread(Characters.Patches)
    if FlagEnabled(1252380800):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1052382695))
    
    EnableBackread(Characters.CastellanJerren)
    EnableBackread(Characters.Blaidd0)
    EnableBackread(Characters.LivingPot0)
    EnableBackread(Characters.GreatHornedTragoth)
    EnableBackread(Characters.Okina)
    EnableBackread(Characters.FingerMaidenTherolina)
    EnableBackread(Characters.Human1)
    EnableBackread(Characters.Patches)
    SetBackreadStateAlternate(Characters.CastellanJerren, True)
    SetBackreadStateAlternate(Characters.Blaidd0, True)
    SetBackreadStateAlternate(Characters.LivingPot0, True)
    SetBackreadStateAlternate(Characters.GreatHornedTragoth, True)
    SetBackreadStateAlternate(Characters.Okina, True)
    SetBackreadStateAlternate(Characters.FingerMaidenTherolina, True)
    SetBackreadStateAlternate(Characters.Human1, True)
    SetBackreadStateAlternate(Characters.Patches, True)
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=1052382695))
    OR_1.Add(FlagEnabled(1252380800))
    
    MAIN.Await(OR_1)
    
    SetBackreadStateAlternate(Characters.CastellanJerren, False)
    SetBackreadStateAlternate(Characters.Blaidd0, False)
    SetBackreadStateAlternate(Characters.LivingPot0, False)
    SetBackreadStateAlternate(Characters.GreatHornedTragoth, False)
    SetBackreadStateAlternate(Characters.Okina, False)
    SetBackreadStateAlternate(Characters.FingerMaidenTherolina, False)
    SetBackreadStateAlternate(Characters.Human1, False)
    SetBackreadStateAlternate(Characters.Patches, False)
    if FlagEnabled(1252380800):
        Wait(30.0)
    DisableBackread(Characters.CastellanJerren)
    DisableBackread(Characters.Blaidd0)
    DisableBackread(Characters.LivingPot0)
    DisableBackread(Characters.GreatHornedTragoth)
    DisableBackread(Characters.Okina)
    DisableBackread(Characters.FingerMaidenTherolina)
    DisableBackread(Characters.Human1)
    DisableBackread(Characters.Patches)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382696)
def Event_1252382696():
    """Event 1252382696"""
    if FlagEnabled(1252382699):
        return
    
    MAIN.Await(FlagEnabled(1252382183))
    
    EnableFlag(1252382699)


@RestartOnRest(1052382699)
def Event_1052382699():
    """Event 1052382699"""
    MAIN.Await(CharacterBackreadEnabled(Characters.CleanrotKnight))
    
    DisableCharacter(Characters.CleanrotKnight)
    DisableAnimations(Characters.CleanrotKnight)


@RestartOnRest(1252382800)
def Event_1252382800():
    """Event 1252382800"""
    if FlagEnabled(1252380800):
        return
    AND_1.Add(HealthValue(Characters.StarscourgeRadahn) <= 0)
    
    MAIN.Await(AND_1)
    
    Wait(4.0)
    PlaySoundEffect(Characters.StarscourgeRadahn, 888880000, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(Characters.StarscourgeRadahn))
    AND_2.Add(CharacterAlive(PLAYER))
    
    MAIN.Await(AND_2)
    
    RemoveSpecialEffect(PLAYER, 13925)
    if PlayerInOwnWorld():
        AddSpecialEffect(PLAYER, 4280)
        AddSpecialEffect(PLAYER, 4282)
    SetNetworkUpdateRate(Characters.Human0, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.StarscourgeRadahn, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    KillBossAndDisplayBanner(character=Characters.StarscourgeRadahn, banner_type=BannerType.DemigodFelled)
    if PlayerInOwnWorld():
        TriggerMultiplayerEvent(event_id=0)
    UnfreezeTime()
    EnableFlag(1252380800)
    EnableFlag(9130)
    if PlayerInOwnWorld():
        EnableFlag(61130)
    EnableFlag(9412)
    SetWeather(weather=Weather.Cloudless, duration=300.0, immediate_change=False)


@RestartOnRest(1252382810)
def Event_1252382810():
    """Event 1252382810"""
    GotoIfFlagDisabled(Label.L0, flag=1252380800)
    DisableCharacter(Characters.StarscourgeRadahn)
    DisableAnimations(Characters.StarscourgeRadahn)
    Kill(Characters.StarscourgeRadahn)
    DisableCharacter(Characters.Human0)
    DisableAnimations(Characters.Human0)
    Kill(Characters.Human0)
    SetBackreadStateAlternate(Characters.Human0, False)
    SetTeamType(Characters.Human0, TeamType.NoTeam)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAnimations(Characters.Human0)
    DisableGravity(Characters.Human0)
    SetLockOnPoint(character=Characters.Human0, lock_on_model_point=220, state=False)
    SetTeamType(Characters.Human0, TeamType.NoTeam)
    DisableAI(Characters.Human0)
    SetDistanceBasedNetworkAuthorityUpdate(character=Characters.Human0, state=True)
    DisableAI(Characters.StarscourgeRadahn)
    SetDistanceBasedNetworkAuthorityUpdate(character=Characters.StarscourgeRadahn, state=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.StarscourgeRadahn, radius=220.0))
    AND_1.Add(CharacterAlive(Characters.StarscourgeRadahn))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1252380801)
    SetBackreadStateAlternate(Characters.Human0, True)
    SetBackreadStateAlternate(Characters.StarscourgeRadahn, True)
    SetNetworkUpdateRate(Characters.Human0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.StarscourgeRadahn, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(Characters.StarscourgeRadahn)
    AddSpecialEffect(PLAYER, 13925)
    AddSpecialEffect(Characters.StarscourgeRadahn, 13918)
    AND_5.Add(CharacterAlive(Characters.StarscourgeRadahn))
    AND_5.Add(CharacterBackreadEnabled(Characters.StarscourgeRadahn))
    AND_5.Add(HasAIStatus(Characters.StarscourgeRadahn, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_5)
    
    EnableBossHealthBar(Characters.StarscourgeRadahn, name=904730000)
    EnableNetworkFlag(1252382815)


@RestartOnRest(1252382820)
def Event_1252382820():
    """Event 1252382820"""
    if FlagEnabled(1252380800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(Characters.StarscourgeRadahn, 13906))
    
    MAIN.Await(AND_1)
    
    DisableAI(Characters.StarscourgeRadahn)
    DisableCharacter(Characters.StarscourgeRadahn)
    DisableAnimations(Characters.StarscourgeRadahn)
    AddSpecialEffect(Characters.StarscourgeRadahn, 13918)
    GotoIfFlagEnabled(Label.L0, flag=1252382890)
    SetWeather(weather=Weather.Cloudless, duration=-1.0, immediate_change=False)
    EnableNetworkFlag(1252382895)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(5.0)
    GotoIfMultiplayer(Label.L2)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.StarscourgeRadahn, radius=200.0))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    SetNetworkUpdateAuthority(Characters.StarscourgeRadahn, authority_level=UpdateAuthority.Forced)
    AND_3.Add(CharacterOutsideRegion(character=PLAYER, region=1052382298))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    Move(
        Characters.Human0,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=PLAYER,
    )
    RotateToFaceEntity(Characters.Human0, 1052382299, wait_for_completion=True)
    RotateToFaceEntity(Characters.Human0, 1052382299, wait_for_completion=True)
    Wait(1.0)
    Move(
        Characters.StarscourgeRadahn,
        destination=Characters.Human0,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=Characters.Human0,
    )
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Move(
        Characters.StarscourgeRadahn,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=229,
        copy_draw_parent=PLAYER,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(Characters.StarscourgeRadahn)
    EnableAnimations(Characters.StarscourgeRadahn)
    EnableAI(Characters.StarscourgeRadahn)
    ForceAnimation(Characters.StarscourgeRadahn, 3037)
    if FlagDisabled(1252382890):
        EnableNetworkFlag(1252382890)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382850)
def Event_1252382850():
    """Event 1252382850"""
    CommonFunc_9005822(0, 1252380800, 473000, 1052382805, 1052382806, 1252382815, 1252382895, 0, 1)


@RestartOnRest(1252382860)
def Event_1252382860():
    """Event 1252382860"""
    if FlagEnabled(1252380800):
        return
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=9411)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCurrentTime(
        time=(3, 30, 0),
        fade_transition=False,
        wait_for_completion=False,
        show_clock=False,
        clock_start_delay=0.0,
        clock_change_duration=0.0,
        clock_finish_delay=0.0,
    )


@RestartOnRest(1252380700)
def Event_1252380700(_, character: uint):
    """Event 1252380700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3600):
        DisableFlag(1052389302)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L13, flag=3613)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3613))
    
    Restart()

    # --- Label 13 --- #
    DefineLabel(13)
    GotoIfFlagEnabled(Label.L0, flag=3600)
    GotoIfFlagEnabled(Label.L1, flag=3601)
    GotoIfFlagEnabled(Label.L3, flag=3603)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 930010)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(character)
    DisableCharacter(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3613))
    
    Restart()


@RestartOnRest(1252380705)
def Event_1252380705(_, character: uint):
    """Event 1252380705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    if FlagEnabled(3660):
        DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3668)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3668))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3660)
    GotoIfFlagEnabled(Label.L2, flag=3661)
    GotoIfFlagEnabled(Label.L4, flag=3663)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930012)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3668))
    
    Restart()


@RestartOnRest(1252380710)
def Event_1252380710():
    """Event 1252380710"""
    WaitFrames(frames=1)
    EnableFlag(1052389200)
    if FlagDisabled(7606):
        return
    DisableFlag(1052389200)
    End()


@RestartOnRest(1252380720)
def Event_1252380720():
    """Event 1252380720"""
    WaitFrames(frames=1)
    DisableFlag(1052389250)
    if FlagDisabled(31009206):
        return
    if FlagEnabled(3681):
        return
    if FlagEnabled(3683):
        return
    EnableFlag(1052389250)
    End()
