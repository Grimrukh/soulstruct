"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 9005810, args=(310, 1052380000, 1052380950, 1052381950, 5.0), arg_types="IIIIf")
    Event_1052382699()
    RunCommonEvent(
        0,
        90005646,
        args=(76422, 1052382690, 1052382691, 1052381690, 1050362690, 60, 50, 36, 0),
        arg_types="IIIIIBBbb",
    )
    Event_1252380700(0, character=1052380726)
    RunCommonEvent(0, 90005704, args=(1052380726, 3601, 3600, 1052389301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1052380726, 3601, 3602, 1052389301, 3603, 3600, 3603, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1052380726, 3603, 3600, 3604), arg_types="IIII")
    Event_1252380705(0, character=1052380706)
    RunCommonEvent(0, 90005704, args=(1052380706, 3661, 3660, 1043399301, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1052380706, 3661, 3662, 1043399301, 3661, 3660, 3663, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1052380706, 3663, 3660, 3664), arg_types="IIII")
    Event_1252380710()
    Event_1252380720()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1052380700)
    DisableBackread(1052380710)
    DisableBackread(1052380715)
    DisableBackread(1052380720)
    DisableBackread(1052380726)
    DisableBackread(1052380730)
    DisableBackread(1052380735)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1252382800()
    Event_1252382810()
    Event_1252382820()
    Event_1252382850()
    Event_1252382680(0, obj=1052381600)
    Event_1252382680(1, obj=1052381601)
    Event_1252382680(2, obj=1052381602)
    Event_1252382680(3, obj=1052381603)
    Event_1252382680(4, obj=1052381604)
    Event_1252382680(5, obj=1052381605)
    Event_1252382680(6, obj=1052381606)
    Event_1252382680(7, obj=1052381607)
    Event_1252382680(8, obj=1052381608)
    Event_1252382680(9, obj=1052381609)
    Event_1252382860()
    Event_1252382696()
    Event_1252382695()
    Event_1252382200(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381500,
        action_button_id=9540
    )
    Event_1252382280(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381500,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381500
    )
    Event_1252382440(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381500,
        animation_id=63040
    )
    Event_1252382520(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        0,
        character=1052380200,
        left=1252382890,
        flag=1252382100,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381502,
        action_button_id=9542
    )
    Event_1252382280(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381502,
        animation_id=20040,
        text=80820
    )
    Event_1252382360(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381502
    )
    Event_1252382440(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381502,
        animation_id=63040
    )
    Event_1252382520(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=1052381582
    )
    Event_1252382600(
        2,
        character=1052380240,
        left=1051369259,
        flag=1252382102,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822
    )
    Event_1252382200(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381506,
        action_button_id=9546
    )
    Event_1252382280(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381506,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381506
    )
    Event_1252382440(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381506,
        animation_id=63040
    )
    Event_1252382520(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        6,
        character=1052380320,
        left=0,
        flag=1252382106,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381508,
        action_button_id=9540
    )
    Event_1252382280(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381508,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381508
    )
    Event_1252382440(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381508,
        animation_id=63040
    )
    Event_1252382520(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        8,
        character=1052380200,
        left=1252382890,
        flag=1252382108,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381509,
        action_button_id=9541
    )
    Event_1252382280(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381509,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381509
    )
    Event_1252382440(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381509,
        animation_id=63040
    )
    Event_1252382520(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        9,
        character=1052380220,
        left=1051369359,
        flag=1252382109,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381512,
        action_button_id=9544
    )
    Event_1252382280(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381512,
        animation_id=63021,
        text=80840
    )
    Event_1252382360(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381512
    )
    Event_1252382440(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381512,
        animation_id=63040
    )
    Event_1252382520(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=1052381584
    )
    Event_1252382600(
        12,
        character=1052380280,
        left=0,
        flag=1252382112,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842
    )
    Event_1252382200(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381513,
        action_button_id=9545
    )
    Event_1252382280(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381513,
        animation_id=63021,
        text=80850
    )
    Event_1252382360(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381513
    )
    Event_1252382440(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381513,
        animation_id=63040
    )
    Event_1252382520(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=1052381585
    )
    Event_1252382600(
        13,
        character=1052380300,
        left=0,
        flag=1252382113,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852
    )
    Event_1252382200(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381514,
        action_button_id=9546
    )
    Event_1252382280(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381514,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381514
    )
    Event_1252382440(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381514,
        animation_id=63040
    )
    Event_1252382520(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        14,
        character=1052380320,
        left=0,
        flag=1252382114,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381516,
        action_button_id=9540
    )
    Event_1252382280(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381516,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381516
    )
    Event_1252382440(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381516,
        animation_id=63040
    )
    Event_1252382520(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        16,
        character=1052380200,
        left=1252382890,
        flag=1252382116,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381517,
        action_button_id=9541
    )
    Event_1252382280(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381517,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381517
    )
    Event_1252382440(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381517,
        animation_id=63040
    )
    Event_1252382520(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        17,
        character=1052380220,
        left=1051369359,
        flag=1252382117,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381518,
        action_button_id=9542
    )
    Event_1252382280(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381518,
        animation_id=20040,
        text=80820
    )
    Event_1252382360(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381518
    )
    Event_1252382440(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381518,
        animation_id=63040
    )
    Event_1252382520(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=1052381582
    )
    Event_1252382600(
        18,
        character=1052380240,
        left=1051369259,
        flag=1252382118,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822
    )
    Event_1252382200(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381519,
        action_button_id=9543
    )
    Event_1252382280(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381519,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381519
    )
    Event_1252382440(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381519,
        animation_id=63040
    )
    Event_1252382520(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        19,
        character=1052380260,
        left=1052389200,
        flag=1252382119,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381521,
        action_button_id=9545
    )
    Event_1252382280(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381521,
        animation_id=63021,
        text=80850
    )
    Event_1252382360(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381521
    )
    Event_1252382440(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381521,
        animation_id=63040
    )
    Event_1252382520(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=1052381585
    )
    Event_1252382600(
        21,
        character=1052380300,
        left=0,
        flag=1252382121,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852
    )
    Event_1252382200(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381523,
        action_button_id=9547
    )
    Event_1252382280(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381523,
        animation_id=63021,
        text=80870
    )
    Event_1252382360(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381523
    )
    Event_1252382440(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381523,
        animation_id=63040
    )
    Event_1252382520(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=1052381587
    )
    Event_1252382600(
        23,
        character=1052380340,
        left=1052389250,
        flag=1252382123,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872
    )
    Event_1252382200(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381524,
        action_button_id=9540
    )
    Event_1252382280(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381524,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381524
    )
    Event_1252382440(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381524,
        animation_id=63040
    )
    Event_1252382520(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        24,
        character=1052380200,
        left=1252382890,
        flag=1252382124,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381525,
        action_button_id=9541
    )
    Event_1252382280(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381525,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381525
    )
    Event_1252382440(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381525,
        animation_id=63040
    )
    Event_1252382520(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        25,
        character=1052380220,
        left=1051369359,
        flag=1252382125,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381529,
        action_button_id=9545
    )
    Event_1252382280(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381529,
        animation_id=63021,
        text=80850
    )
    Event_1252382360(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381529
    )
    Event_1252382440(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381529,
        animation_id=63040
    )
    Event_1252382520(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=1052381585
    )
    Event_1252382600(
        29,
        character=1052380300,
        left=0,
        flag=1252382129,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852
    )
    Event_1252382200(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381535,
        action_button_id=9543
    )
    Event_1252382280(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381535,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381535
    )
    Event_1252382440(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381535,
        animation_id=63040
    )
    Event_1252382520(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        35,
        character=1052380260,
        left=1052389200,
        flag=1252382135,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381536,
        action_button_id=9544
    )
    Event_1252382280(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381536,
        animation_id=63021,
        text=80840
    )
    Event_1252382360(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381536
    )
    Event_1252382440(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381536,
        animation_id=63040
    )
    Event_1252382520(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=1052381584
    )
    Event_1252382600(
        36,
        character=1052380280,
        left=0,
        flag=1252382136,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842
    )
    Event_1252382200(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381538,
        action_button_id=9546
    )
    Event_1252382280(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381538,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381538
    )
    Event_1252382440(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381538,
        animation_id=63040
    )
    Event_1252382520(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        38,
        character=1052380320,
        left=0,
        flag=1252382138,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381540,
        action_button_id=9540
    )
    Event_1252382280(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381540,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381540
    )
    Event_1252382440(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381540,
        animation_id=63040
    )
    Event_1252382520(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        40,
        character=1052380200,
        left=1252382890,
        flag=1252382140,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381541,
        action_button_id=9541
    )
    Event_1252382280(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381541,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381541
    )
    Event_1252382440(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381541,
        animation_id=63040
    )
    Event_1252382520(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        41,
        character=1052380220,
        left=1051369359,
        flag=1252382141,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381543,
        action_button_id=9543
    )
    Event_1252382280(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381543,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381543
    )
    Event_1252382440(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381543,
        animation_id=63040
    )
    Event_1252382520(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        43,
        character=1052380260,
        left=1052389200,
        flag=1252382143,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381544,
        action_button_id=9544
    )
    Event_1252382280(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381544,
        animation_id=63021,
        text=80840
    )
    Event_1252382360(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381544
    )
    Event_1252382440(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381544,
        animation_id=63040
    )
    Event_1252382520(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=1052381584
    )
    Event_1252382600(
        44,
        character=1052380280,
        left=0,
        flag=1252382144,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842
    )
    Event_1252382200(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381545,
        action_button_id=9545
    )
    Event_1252382280(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381545,
        animation_id=63021,
        text=80850
    )
    Event_1252382360(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381545
    )
    Event_1252382440(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381545,
        animation_id=63040
    )
    Event_1252382520(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=1052381585
    )
    Event_1252382600(
        45,
        character=1052380300,
        left=0,
        flag=1252382145,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852
    )
    Event_1252382200(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381547,
        action_button_id=9547
    )
    Event_1252382280(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381547,
        animation_id=63021,
        text=80870
    )
    Event_1252382360(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381547
    )
    Event_1252382440(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381547,
        animation_id=63040
    )
    Event_1252382520(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=1052381587
    )
    Event_1252382600(
        47,
        character=1052380340,
        left=1052389250,
        flag=1252382147,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872
    )
    Event_1252382200(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381548,
        action_button_id=9540
    )
    Event_1252382280(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381548,
        animation_id=63021,
        text=80800
    )
    Event_1252382360(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        obj=1052381548
    )
    Event_1252382440(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        destination=1052381548,
        animation_id=63040
    )
    Event_1252382520(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        animation_id=90009,
        animation_id_1=90007,
        text=80801,
        destination=1052381580
    )
    Event_1252382600(
        48,
        character=1052380200,
        left=1252382890,
        flag=1252382148,
        flag_1=1252382180,
        flag_2=1252382190,
        left_1=0,
        animation_id=0,
        text=80802
    )
    Event_1252382200(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381551,
        action_button_id=9543
    )
    Event_1252382280(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381551,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381551
    )
    Event_1252382440(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381551,
        animation_id=63040
    )
    Event_1252382520(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        51,
        character=1052380260,
        left=1052389200,
        flag=1252382151,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381552,
        action_button_id=9544
    )
    Event_1252382280(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381552,
        animation_id=63021,
        text=80840
    )
    Event_1252382360(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381552
    )
    Event_1252382440(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381552,
        animation_id=63040
    )
    Event_1252382520(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=1052381584
    )
    Event_1252382600(
        52,
        character=1052380280,
        left=0,
        flag=1252382152,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842
    )
    Event_1252382200(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381553,
        action_button_id=9545
    )
    Event_1252382280(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381553,
        animation_id=63021,
        text=80850
    )
    Event_1252382360(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        obj=1052381553
    )
    Event_1252382440(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        destination=1052381553,
        animation_id=63040
    )
    Event_1252382520(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        animation_id=90009,
        animation_id_1=90007,
        text=80851,
        destination=1052381585
    )
    Event_1252382600(
        53,
        character=1052380300,
        left=0,
        flag=1252382153,
        flag_1=1252382185,
        flag_2=1252382195,
        left_1=0,
        animation_id=0,
        text=80852
    )
    Event_1252382200(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381554,
        action_button_id=9546
    )
    Event_1252382280(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381554,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381554
    )
    Event_1252382440(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381554,
        animation_id=63040
    )
    Event_1252382520(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        54,
        character=1052380320,
        left=0,
        flag=1252382154,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381555,
        action_button_id=9547
    )
    Event_1252382280(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381555,
        animation_id=63021,
        text=80870
    )
    Event_1252382360(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381555
    )
    Event_1252382440(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381555,
        animation_id=63040
    )
    Event_1252382520(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=1052381587
    )
    Event_1252382600(
        55,
        character=1052380340,
        left=1052389250,
        flag=1252382155,
        flag_1=1252382187,
        flag_2=1252382197,
        left_1=0,
        animation_id=0,
        text=80872
    )
    Event_1252382200(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381557,
        action_button_id=9541
    )
    Event_1252382280(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381557,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381557
    )
    Event_1252382440(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381557,
        animation_id=63040
    )
    Event_1252382520(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        57,
        character=1052380220,
        left=1051369359,
        flag=1252382157,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381559,
        action_button_id=9543
    )
    Event_1252382280(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381559,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381559
    )
    Event_1252382440(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381559,
        animation_id=63040
    )
    Event_1252382520(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        59,
        character=1052380260,
        left=1052389200,
        flag=1252382159,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381562,
        action_button_id=9546
    )
    Event_1252382280(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381562,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381562
    )
    Event_1252382440(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381562,
        animation_id=63040
    )
    Event_1252382520(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        62,
        character=1052380320,
        left=0,
        flag=1252382162,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381566,
        action_button_id=9542
    )
    Event_1252382280(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381566,
        animation_id=20040,
        text=80820
    )
    Event_1252382360(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        obj=1052381566
    )
    Event_1252382440(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        destination=1052381566,
        animation_id=63040
    )
    Event_1252382520(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        animation_id=20049,
        animation_id_1=0,
        text=80821,
        destination=1052381582
    )
    Event_1252382600(
        66,
        character=1052380240,
        left=1051369259,
        flag=1252382166,
        flag_1=1252382182,
        flag_2=1252382192,
        left_1=0,
        animation_id=0,
        text=80822
    )
    Event_1252382200(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381568,
        action_button_id=9544
    )
    Event_1252382280(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381568,
        animation_id=63021,
        text=80840
    )
    Event_1252382360(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        obj=1052381568
    )
    Event_1252382440(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        destination=1052381568,
        animation_id=63040
    )
    Event_1252382520(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        animation_id=90009,
        animation_id_1=90007,
        text=80841,
        destination=1052381584
    )
    Event_1252382600(
        68,
        character=1052380280,
        left=0,
        flag=1252382168,
        flag_1=1252382184,
        flag_2=1252382194,
        left_1=0,
        animation_id=0,
        text=80842
    )
    Event_1252382200(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381573,
        action_button_id=9541
    )
    Event_1252382280(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381573,
        animation_id=20054,
        text=80810
    )
    Event_1252382360(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        obj=1052381573
    )
    Event_1252382440(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        destination=1052381573,
        animation_id=63040
    )
    Event_1252382520(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        animation_id=20049,
        animation_id_1=0,
        text=80811,
        destination=1052381581
    )
    Event_1252382600(
        73,
        character=1052380220,
        left=1051369359,
        flag=1252382173,
        flag_1=1252382181,
        flag_2=1252382191,
        left_1=0,
        animation_id=0,
        text=80812
    )
    Event_1252382200(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381575,
        action_button_id=9543
    )
    Event_1252382280(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381575,
        animation_id=63021,
        text=80830
    )
    Event_1252382360(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        obj=1052381575
    )
    Event_1252382440(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        destination=1052381575,
        animation_id=63040
    )
    Event_1252382520(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        animation_id=90009,
        animation_id_1=90007,
        text=80831,
        destination=1052381583
    )
    Event_1252382600(
        75,
        character=1052380260,
        left=1052389200,
        flag=1252382175,
        flag_1=1252382183,
        flag_2=1252382193,
        left_1=0,
        animation_id=0,
        text=80832
    )
    Event_1252382200(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381578,
        action_button_id=9546
    )
    Event_1252382280(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381578,
        animation_id=63021,
        text=80860
    )
    Event_1252382360(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        obj=1052381578
    )
    Event_1252382440(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        destination=1052381578,
        animation_id=63040
    )
    Event_1252382520(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        animation_id=90009,
        animation_id_1=90007,
        text=80861,
        destination=1052381586
    )
    Event_1252382600(
        78,
        character=1052380320,
        left=0,
        flag=1252382178,
        flag_1=1252382186,
        flag_2=1252382196,
        left_1=0,
        animation_id=0,
        text=80862
    )
    Event_1252382200(
        79,
        character=1052380340,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381579,
        action_button_id=9547
    )
    Event_1252382280(
        79,
        character=1052380340,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381579,
        animation_id=63021,
        text=80870
    )
    Event_1252382360(
        79,
        character=1052380340,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        obj=1052381579
    )
    Event_1252382440(
        79,
        character=1052380340,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        destination=1052381579,
        animation_id=63040
    )
    Event_1252382520(
        79,
        character=1052380340,
        left=1052389250,
        flag=1252382179,
        flag_1=1252382187,
        flag_2=1252382197,
        animation_id=90009,
        animation_id_1=90007,
        text=80871,
        destination=1052381587
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
    EndIfFlagEnabled(1252380800)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    GotoIfFlagDisabled(Label.L3, flag=left)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_2, action_button_id=action_button_id, entity=destination)
    IfFlagDisabled(AND_2, flag)
    IfFlagDisabled(AND_2, flag_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfFlagEnabled(OR_1, flag_1)
    IfFlagEnabled(OR_1, 1252380800)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    EndIfFlagEnabled(1252380800)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    WaitFrames(frames=1)
    SkipLinesIfLeavingSession(1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Object,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    Wait(1.0)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(AND_3, flag_1)
    IfFlagDisabled(AND_3, flag_2)
    IfConditionTrue(MAIN, input_condition=AND_3)
    WaitFrames(frames=1)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    IfFlagEnabled(MAIN, left)
    Restart()


@RestartOnRest(1252382280)
def Event_1252382280(
    _,
    character: uint,
    left: uint,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    obj: uint,
    animation_id: int,
    text: int,
):
    """Event 1252382280"""
    DisableCharacter(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    Unknown_2004_73(entity=character, unk_4_8=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    EndIfFlagEnabled(1252380800)
    EnableCharacter(character)
    AddSpecialEffect(character, 18677)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetTeamType(character, TeamType.NoTeam)
    EnableImmortality(character)
    IfFlagEnabled(AND_1, flag)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfCharacterBackreadEnabled(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfFlagDisabled(6, 1252380800)
    DisableCharacter(character)
    DisableAnimations(character)
    EnableCharacterCollision(character)
    DisableGravity(character)
    DisableAI(character)
    End()
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    CreateObjectVFX(obj, vfx_id=100, model_point=30320)
    CancelSpecialEffect(character, 4380)
    CancelSpecialEffect(character, 18677)
    EnableCharacter(character)
    EnableInvincibility(character)
    SkipLinesIfValueEqual(1, left=animation_id, right=0)
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    EnableAnimations(character)
    DisableCharacterCollision(character)
    EnableGravity(character)
    DisableInvincibility(character)
    EnableImmortality(character)
    EnableAI(character)
    ReplanAI(character)
    ClearTargetList(character)
    EnableHealthBar(character)
    SetTeamType(character, TeamType.WhitePhantom)
    SetCharacterEventTarget(character, region=1052380800)
    DisplayBattlefieldMessage(text)
    DeleteObjectVFX(obj)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    End()


@RestartOnRest(1252382360)
def Event_1252382360(_, character: uint, left: uint, flag: uint, flag_1: uint, flag_2: uint, obj: uint):
    """Event 1252382360"""
    GotoIfFlagEnabled(Label.L2, flag=1252380800)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfUnsignedEqual(2, left=left, right=0)
    IfFlagDisabled(AND_5, left)
    GotoIfConditionTrue(Label.L3, input_condition=AND_5)
    IfFlagDisabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_1)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    IfFlagEnabled(AND_2, flag)
    IfFlagEnabled(AND_2, flag_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    IfFlagEnabled(AND_3, flag_2)
    IfCharacterBackreadEnabled(AND_3, character)
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    IfFlagEnabled(AND_4, flag)
    IfFlagEnabled(AND_4, flag_1)
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    CreateObjectVFX(obj, vfx_id=100, model_point=30080)
    IfFlagEnabled(OR_1, flag_1)
    IfFlagEnabled(OR_1, 1252380800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(obj)
    IfFlagDisabled(OR_2, flag_2)
    IfFlagEnabled(OR_2, 1252380800)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfFlagEnabled(AND_6, flag)
    GotoIfConditionTrue(Label.L2, input_condition=AND_6)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DeleteObjectVFX(obj)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    IfFlagEnabled(MAIN, left)
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
    EndIfFlagEnabled(1252380800)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L1, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=destination, radius=15.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAI(character)
    AddSpecialEffect(character, 4380)
    WaitFrames(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    WaitFrames(frames=1)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Object,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    WaitFrames(frames=1)
    CancelSpecialEffect(character, 18677)
    DisableInvincibility(character)
    DisableAnimations(character)
    EnableCharacterCollision(character)
    DisableGravity(character)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(1, left=animation_id, right=0)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    IfPlayerInOwnWorld(AND_2)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_2, left)
    IfEntityBeyondDistance(AND_2, entity=PLAYER, other_entity=destination, radius=15.0)
    IfConditionTrue(MAIN, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagDisabled(MAIN, flag_2)
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
    EndIfFlagEnabled(1252380800)
    IfPlayerInOwnWorld(AND_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, flag_2)
    IfCharacterBackreadEnabled(AND_1, character)
    IfHealthLessThanOrEqual(AND_1, character, value=0.009999999776482582)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableInvincibility(character)
    DisableAnimations(character)
    SetTeamType(character, TeamType.NoTeam)
    Wait(0.10000000149011612)
    EnableCharacterCollision(character)
    DisableGravity(character)
    ClearTargetList(character)
    SkipLinesIfValueEqual(5, left=animation_id, right=0)
    SkipLinesIfValueEqual(1, left=animation_id, right=90009)
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfValueNotEqual(2, left=animation_id, right=90009)
    ForceAnimation(character, animation_id, unknown2=1.0)
    WaitFrames(frames=200)
    SkipLinesIfValueEqual(1, left=animation_id_1, right=0)
    ForceAnimation(character, animation_id_1, loop=True, unknown2=1.0)
    SkipLinesIfValueNotEqual(2, left=animation_id, right=90009)
    AddSpecialEffect(character, 18677)
    Wait(3.0)
    DisplayBattlefieldMessage(text)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 20, loop=True, unknown2=1.0)
    AddSpecialEffect(character, 4380)
    Wait(30.0)
    AddSpecialEffect(character, 110)
    AddSpecialEffect(character, 111)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Object,
        model_point=100,
        copy_draw_parent=PLAYER,
    )
    ClearTargetList(character)
    WaitFrames(frames=1)
    ReplanAI(character)
    CancelSpecialEffect(character, 18677)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    EndIfPlayerNotInOwnWorld()
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
    EndIfFlagEnabled(1252380800)
    GotoIfUnsignedEqual(Label.L2, left=character, right=1052380340)
    GotoIfUnsignedEqual(Label.L0, left=left_1, right=0)
    IfPlayerInOwnWorld(AND_1)
    SkipLinesIfUnsignedEqual(1, left=left, right=0)
    IfFlagEnabled(AND_1, left)
    IfHealthGreaterThan(AND_1, character, value=0.009999999776482582)
    IfFlagEnabled(AND_1, flag)
    IfCharacterBackreadEnabled(AND_1, character)
    IfFlagEnabled(OR_1, 1252380800)
    IfFlagEnabled(OR_1, left_1)
    IfEntityBeyondDistance(OR_1, entity=character, other_entity=PLAYER, radius=200.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfPlayerInOwnWorld(AND_3)
    IfCharacterBackreadEnabled(AND_3, character)
    IfHealthLessThanOrEqual(AND_3, character, value=0.009999999776482582)
    IfFlagEnabled(AND_3, flag)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_3)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_2)
    IfHealthGreaterThan(AND_2, character, value=0.009999999776482582)
    IfFlagEnabled(AND_2, flag)
    IfCharacterBackreadEnabled(AND_2, character)
    IfFlagEnabled(OR_2, 1252380800)
    IfEntityBeyondDistance(OR_2, entity=character, other_entity=PLAYER, radius=200.0)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfPlayerInOwnWorld(AND_4)
    IfCharacterBackreadEnabled(AND_4, character)
    IfHealthLessThanOrEqual(AND_4, character, value=0.009999999776482582)
    IfFlagEnabled(AND_4, flag)
    IfConditionTrue(OR_4, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=AND_4)
    IfConditionTrue(MAIN, input_condition=OR_4)
    Goto(Label.L1)

    # --- Label 2 --- #
    DefineLabel(2)
    IfPlayerInOwnWorld(AND_5)
    IfHealthGreaterThan(AND_5, character, value=0.009999999776482582)
    IfFlagEnabled(AND_5, flag)
    IfFlagEnabled(AND_5, flag_2)
    IfCharacterBackreadEnabled(AND_5, character)
    IfPlayerInOwnWorld(AND_6)
    IfCharacterBackreadEnabled(AND_6, character)
    IfHealthLessThanOrEqual(AND_6, character, value=0.009999999776482582)
    IfFlagEnabled(AND_6, flag)
    IfConditionTrue(OR_6, input_condition=AND_5)
    IfConditionTrue(OR_6, input_condition=AND_6)
    IfConditionTrue(MAIN, input_condition=OR_6)
    Wait(20.0)

    # --- Label 1 --- #
    DefineLabel(1)
    IfHealthLessThanOrEqual(AND_9, character, value=0.009999999776482582)
    EndIfConditionTrue(input_condition=AND_9)
    SetTeamType(character, TeamType.NoTeam)
    DisableAnimations(character)
    EnableInvincibility(character)
    SkipLines(2)
    SkipLinesIfValueEqual(1, left=animation_id, right=0)
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    AddSpecialEffect(character, 18677)
    ReplanAI(character)
    ClearTargetList(character)
    Wait(3.0)
    DisableAI(character)
    DisableInvincibility(character)
    ResetAnimation(character, disable_interpolation=True)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    IfHealthLessThanOrEqual(AND_10, character, value=0.009999999776482582)
    EndIfConditionTrue(input_condition=AND_10)
    SkipLinesIfFlagEnabled(1, 1252380800)
    DisplayBattlefieldMessage(text)
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
def Event_1252382680(_, obj: uint):
    """Event 1252382680"""
    GotoIfFlagEnabled(Label.L0, flag=9411)
    GotoIfFlagEnabled(Label.L1, flag=1252380800)
    DisableObject(obj)
    IfFlagEnabled(MAIN, 9411)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(obj)
    IfFlagEnabled(MAIN, 1252380800)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)


@RestartOnRest(1252382695)
def Event_1252382695():
    """Event 1252382695"""
    DisableNetworkSync()
    DisableBackread(1052380200)
    DisableBackread(1052380220)
    DisableBackread(1052380240)
    DisableBackread(1052380260)
    DisableBackread(1052380280)
    DisableBackread(1052380300)
    DisableBackread(1052380320)
    DisableBackread(1052380340)
    EndIfFlagEnabled(1252380800)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1052382695)
    EnableBackread(1052380200)
    EnableBackread(1052380220)
    EnableBackread(1052380240)
    EnableBackread(1052380260)
    EnableBackread(1052380280)
    EnableBackread(1052380300)
    EnableBackread(1052380320)
    EnableBackread(1052380340)
    SetBackreadStateAlternate(1052380200, True)
    SetBackreadStateAlternate(1052380220, True)
    SetBackreadStateAlternate(1052380240, True)
    SetBackreadStateAlternate(1052380260, True)
    SetBackreadStateAlternate(1052380280, True)
    SetBackreadStateAlternate(1052380300, True)
    SetBackreadStateAlternate(1052380320, True)
    SetBackreadStateAlternate(1052380340, True)
    IfCharacterOutsideRegion(OR_1, character=PLAYER, region=1052382695)
    IfFlagEnabled(OR_1, 1252380800)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetBackreadStateAlternate(1052380200, False)
    SetBackreadStateAlternate(1052380220, False)
    SetBackreadStateAlternate(1052380240, False)
    SetBackreadStateAlternate(1052380260, False)
    SetBackreadStateAlternate(1052380280, False)
    SetBackreadStateAlternate(1052380300, False)
    SetBackreadStateAlternate(1052380320, False)
    SetBackreadStateAlternate(1052380340, False)
    SkipLinesIfFlagDisabled(1, 1252380800)
    Wait(30.0)
    DisableBackread(1052380200)
    DisableBackread(1052380220)
    DisableBackread(1052380240)
    DisableBackread(1052380260)
    DisableBackread(1052380280)
    DisableBackread(1052380300)
    DisableBackread(1052380320)
    DisableBackread(1052380340)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382696)
def Event_1252382696():
    """Event 1252382696"""
    EndIfFlagEnabled(1252382699)
    IfFlagEnabled(MAIN, 1252382183)
    EnableFlag(1252382699)


@RestartOnRest(1052382699)
def Event_1052382699():
    """Event 1052382699"""
    IfCharacterBackreadEnabled(MAIN, 1052380699)
    DisableCharacter(1052380699)
    DisableAnimations(1052380699)


@RestartOnRest(1252382800)
def Event_1252382800():
    """Event 1252382800"""
    EndIfFlagEnabled(1252380800)
    IfHealthValueLessThanOrEqual(AND_1, 1052380800, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(1052380800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 1052380800)
    IfCharacterAlive(AND_2, PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_2)
    CancelSpecialEffect(PLAYER, 13925)
    SkipLinesIfPlayerNotInOwnWorld(2)
    AddSpecialEffect(PLAYER, 4280)
    AddSpecialEffect(PLAYER, 4282)
    SetNetworkUpdateRate(1052380899, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(1052380800, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    KillBossAndDisplayBanner(character=1052380800, banner_type=BannerType.HollowArenaLoss)
    SkipLinesIfPlayerNotInOwnWorld(1)
    TriggerMultiplayerEvent(event_id=0)
    UnknownTimer_05(unknown1=0)
    EnableFlag(1252380800)
    EnableFlag(9130)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61130)
    EnableFlag(9412)
    Unknown_2003_68(unknown1=5, unknown2=300.0, unknown3=0)


@RestartOnRest(1252382810)
def Event_1252382810():
    """Event 1252382810"""
    GotoIfFlagDisabled(Label.L0, flag=1252380800)
    DisableCharacter(1052380800)
    DisableAnimations(1052380800)
    Kill(1052380800)
    DisableCharacter(1052380899)
    DisableAnimations(1052380899)
    Kill(1052380899)
    SetBackreadStateAlternate(1052380899, False)
    SetTeamType(1052380899, TeamType.NoTeam)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAnimations(1052380899)
    DisableGravity(1052380899)
    SetLockOnPoint(character=1052380899, lock_on_model_point=220, state=False)
    SetTeamType(1052380899, TeamType.NoTeam)
    DisableAI(1052380899)
    Unknown_2004_70(unk_0_4=1052380899, unk_4_8=1)
    DisableAI(1052380800)
    Unknown_2004_70(unk_0_4=1052380800, unk_4_8=1)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1052380800, radius=220.0)
    IfCharacterAlive(AND_1, 1052380800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1252380801)
    SetBackreadStateAlternate(1052380899, True)
    SetBackreadStateAlternate(1052380800, True)
    SetNetworkUpdateRate(1052380899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(1052380800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(1052380800)
    AddSpecialEffect(PLAYER, 13925)
    AddSpecialEffect(1052380800, 13918)
    IfCharacterAlive(AND_5, 1052380800)
    IfCharacterBackreadEnabled(AND_5, 1052380800)
    IfHasAIStatus(AND_5, 1052380800, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=AND_5)
    EnableBossHealthBar(1052380800, name=904730000)
    EnableNetworkFlag(1252382815)


@RestartOnRest(1252382820)
def Event_1252382820():
    """Event 1252382820"""
    EndIfFlagEnabled(1252380800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterHasSpecialEffect(AND_1, 1052380800, 13906)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableAI(1052380800)
    DisableCharacter(1052380800)
    DisableAnimations(1052380800)
    AddSpecialEffect(1052380800, 13918)
    GotoIfFlagEnabled(Label.L0, flag=1252382890)
    Unknown_2003_68(unknown1=5, unknown2=-1.0, unknown3=0)
    EnableNetworkFlag(1252382895)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(5.0)
    GotoIfTryingToCreateSession(Label.L2)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=1052380800, radius=200.0)
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    SetNetworkUpdateAuthority(1052380800, authority_level=UpdateAuthority.Unknown8192)
    IfCharacterOutsideRegion(AND_3, character=PLAYER, region=1052382298)
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    Move(
        1052380899,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=PLAYER,
    )
    RotateToFaceEntity(1052380899, 1052382299, wait_for_completion=True)
    RotateToFaceEntity(1052380899, 1052382299, wait_for_completion=True)
    Wait(1.0)
    Move(
        1052380800,
        destination=1052380899,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=1052380899,
    )
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(1.0)
    Move(
        1052380800,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=229,
        copy_draw_parent=PLAYER,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(1052380800)
    EnableAnimations(1052380800)
    EnableAI(1052380800)
    ForceAnimation(1052380800, 3037, unknown2=1.0)
    SkipLinesIfFlagEnabled(1, 1252382890)
    EnableNetworkFlag(1252382890)
    Wait(1.0)
    Restart()


@RestartOnRest(1252382850)
def Event_1252382850():
    """Event 1252382850"""
    RunCommonEvent(
        0,
        9005822,
        args=(1252380800, 473000, 1052382805, 1052382806, 1252382815, 1252382895, 0, 1),
        arg_types="IiIIIIii",
    )


@RestartOnRest(1252382860)
def Event_1252382860():
    """Event 1252382860"""
    EndIfFlagEnabled(1252380800)
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagEnabled(Label.L0, flag=9411)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    UnknownTimer_04(
        hours=3,
        minutes=30,
        seconds=0,
        unknown1=0,
        unknown2=0,
        unknown3=0,
        unknown4=0,
        unknown5=0,
        unknown6=0,
    )


@RestartOnRest(1252380700)
def Event_1252380700(_, character: uint):
    """Event 1252380700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3600)
    DisableFlag(1052389302)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L13, flag=3613)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3613)
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
    ForceAnimation(character, 930010, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3613)
    Restart()


@RestartOnRest(1252380705)
def Event_1252380705(_, character: uint):
    """Event 1252380705"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    SkipLinesIfFlagDisabled(1, 3660)
    DisableFlag(1043399303)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3668)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3668)
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
    ForceAnimation(character, 930012, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3668)
    Restart()


@RestartOnRest(1252380710)
def Event_1252380710():
    """Event 1252380710"""
    WaitFrames(frames=1)
    EnableFlag(1052389200)
    EndIfFlagDisabled(7606)
    DisableFlag(1052389200)
    End()


@RestartOnRest(1252380720)
def Event_1252380720():
    """Event 1252380720"""
    WaitFrames(frames=1)
    DisableFlag(1052389250)
    EndIfFlagDisabled(31009206)
    EndIfFlagEnabled(3681)
    EndIfFlagEnabled(3683)
    EnableFlag(1052389250)
    End()
