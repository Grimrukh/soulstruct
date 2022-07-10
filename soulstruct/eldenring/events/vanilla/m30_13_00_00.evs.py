"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=73013, obj=30131950, unknown=5.0)
    RunCommonEvent(0, 90005250, args=(30130250, 30132250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30130251, 30000, 20000, 30132251, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        2,
        90005200,
        args=(30130253, 30000, 20000, 30132251, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(3, 90005200, args=(30130254, 30000, 20000, 30132251, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        4,
        90005200,
        args=(30130255, 30000, 20000, 30132251, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30130256, 30000, 20000, 30132256, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        1,
        90005200,
        args=(30130257, 30000, 20000, 30132256, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005250, args=(30130270, 30132270, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(30130271, 30132270, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(
        1,
        90005200,
        args=(30130275, 30000, 20000, 30132405, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(2, 90005200, args=(30130276, 30000, 20000, 30132405, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30130297, 30132297, 3.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005221, args=(30130289, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(1, 90005221, args=(30130290, 30000, 20000, 0.0, 0), arg_types="IiifI")
    RunCommonEvent(0, 90005200, args=(30130400, 30000, 20000, 30132400, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(2, 90005200, args=(30130402, 30000, 20000, 30132400, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005201, args=(30130407, 30000, 20000, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(30130408, 30000, 20000, 30132408, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30130300, 30132300, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005200,
        args=(30130301, 30000, 20000, 30132301, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1,
        90005200,
        args=(30130302, 30000, 20000, 30132302, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005250, args=(30130307, 30132307, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30130308, 30132308, 0.0, 3004), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(30130309, 30132309, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005261, args=(30130315, 30132315, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(30130312, 30132312, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(30130316, 30010, 20010, 30132316, 5.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(30130317, 30003, 20003, 30132317, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(30130318, 30132318, 0.0, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(30130320, 4.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005650, args=(30130540, 30131540, 30131541, 30133541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30130540, 30131540), arg_types="II")
    RunCommonEvent(
        0,
        90005501,
        args=(30130510, 30131510, 0, 30131510, 30131511, 30131512, 30130511),
        arg_types="IIIIIII",
    )
    Event_30132510()
    RunCommonEvent(0, 90005525, args=(30130570, 30131570), arg_types="II")
    Event_30132580()
    Event_30132800()
    Event_30132810()
    Event_30132849()
    Event_30132811()
    RunCommonEvent(0, 90005200, args=(30130292, 30000, 20000, 30132800, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        1,
        90005200,
        args=(30130293, 30000, 20000, 30132800, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        2,
        90005200,
        args=(30130298, 30000, 20000, 30132800, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(3, 90005200, args=(30130299, 30000, 20000, 30132800, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005646,
        args=(30130800, 30132840, 30132841, 30131840, 30132840, 30, 13, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_30130790(0, obj=30131520, flag=30130800)
    Event_30132200(
        0,
        obj=30131200,
        obj_1=30131201,
        region=30132350,
        region_1=30132211,
        flag=30131200,
        obj_act_id=30133200
    )
    Event_30132205(0, flag=30131200, region=30132350)
    Event_30132200(
        1,
        obj=30131201,
        obj_1=30131200,
        region=30132351,
        region_1=30132210,
        flag=30131201,
        obj_act_id=30133201
    )
    Event_30132205(1, flag=30131201, region=30132351)
    Event_30132200(
        2,
        obj=30131202,
        obj_1=30131203,
        region=30132352,
        region_1=30132213,
        flag=30131202,
        obj_act_id=30133202
    )
    Event_30132205(2, flag=30131202, region=30132352)
    Event_30132200(
        3,
        obj=30131203,
        obj_1=30131202,
        region=30132353,
        region_1=30132212,
        flag=30131203,
        obj_act_id=30133203
    )
    Event_30132205(3, flag=30131203, region=30132353)
    Event_30132200(
        4,
        obj=30131204,
        obj_1=30131205,
        region=30132354,
        region_1=30132215,
        flag=30131204,
        obj_act_id=30133204
    )
    Event_30132205(4, flag=30131204, region=30132354)
    Event_30132200(
        5,
        obj=30131205,
        obj_1=30131204,
        region=30132355,
        region_1=30132214,
        flag=30131205,
        obj_act_id=30133205
    )
    Event_30132205(5, flag=30131205, region=30132355)
    Event_30132200(
        6,
        obj=30131206,
        obj_1=30131207,
        region=30132356,
        region_1=30132217,
        flag=30131206,
        obj_act_id=30133206
    )
    Event_30132205(6, flag=30131206, region=30132356)
    Event_30132200(
        7,
        obj=30131207,
        obj_1=30131206,
        region=30132357,
        region_1=30132216,
        flag=30131207,
        obj_act_id=30133207
    )
    Event_30132205(7, flag=30131207, region=30132357)
    Event_30132200(
        8,
        obj=30131208,
        obj_1=30131209,
        region=30132358,
        region_1=30132219,
        flag=30131208,
        obj_act_id=30133208
    )
    Event_30132205(8, flag=30131208, region=30132358)
    Event_30132200(
        9,
        obj=30131209,
        obj_1=30131208,
        region=30132359,
        region_1=30132218,
        flag=30131209,
        obj_act_id=30133209
    )
    Event_30132205(9, flag=30131209, region=30132359)
    Event_30132200(
        10,
        obj=30131220,
        obj_1=30131221,
        region=30132280,
        region_1=30132231,
        flag=30131220,
        obj_act_id=30133220
    )
    Event_30132205(10, flag=30131220, region=30132280)
    Event_30132200(
        11,
        obj=30131221,
        obj_1=30131220,
        region=30132281,
        region_1=30132230,
        flag=30131221,
        obj_act_id=30133221
    )
    Event_30132205(11, 30131221, 30132281)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30130519()


@NeverRestart(30132510)
def Event_30132510():
    """Event 30132510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            30130510,
            30131510,
            0,
            30131510,
            30131511,
            30133511,
            30131512,
            30133512,
            30132511,
            30132512,
            30130511,
            30132512,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(30132580)
def Event_30132580():
    """Event 30132580"""
    RegisterLadder(start_climbing_flag=30130580, stop_climbing_flag=30130581, obj=30131580)
    RegisterLadder(start_climbing_flag=30130582, stop_climbing_flag=30130583, obj=30131582)


@RestartOnRest(30132200)
def Event_30132200(_, obj: uint, obj_1: uint, region: uint, region_1: uint, flag: uint, obj_act_id: uint):
    """Event 30132200"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfObjectActivated(MAIN, obj_act_id=obj_act_id)
    EnableNetworkFlag(flag)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableNetworkSync()
    Wait(1.2999999523162842)
    Wait(0.8999999761581421)
    IfHealthValueEqual(AND_1, PLAYER, value=0)
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L20, character=PLAYER, special_effect=4170)
    GotoIfCharacterOutsideRegion(Label.L20, character=PLAYER, region=region)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=1, unknown4=-1.0)
    DisplayDialog(text=20700, anchor_entity=0, display_distance=5.0, button_type=ButtonType.Yes_or_No)
    Wait(0.699999988079071)
    AddSpecialEffect(PLAYER, 4090)
    PlaySoundEffect(PLAYER, 8700, sound_type=SoundType.c_CharacterMotion)
    Wait(2.700000047683716)
    IfHealthValueEqual(AND_2, PLAYER, value=0)
    GotoIfConditionTrue(Label.L18, input_condition=AND_2)
    DisableCharacter(PLAYER)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=region_1,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    Wait(1.0)
    AddSpecialEffect(PLAYER, 4091)
    EnableCharacter(PLAYER)
    ForceAnimation(PLAYER, 60131, unknown2=1.0)
    Unknown_2004_77(unknown1=0.0, unknown2=0.0, unknown3=0, unknown4=-1.0)
    Goto(Label.L19)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(3.4000000953674316)

    # --- Label 18 --- #
    DefineLabel(18)
    Wait(1.0)

    # --- Label 19 --- #
    DefineLabel(19)
    ForceAnimation(obj, 2, wait_for_completion=True, unknown2=1.0)
    DisableNetworkFlag(flag)
    EnableNetworkSync()
    EnableObjectActivation(obj, obj_act_id=-1)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableNetworkFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    EnableObjectActivation(obj_1, obj_act_id=-1)
    EnableNetworkSync()
    Restart()


@RestartOnRest(30132205)
def Event_30132205(_, flag: uint, region: uint):
    """Event 30132205"""
    GotoIfCharacterHasSpecialEffect(Label.L0, character=PLAYER, special_effect=4170)
    IfFlagEnabled(AND_1, flag)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4170)
    Wait(2.299999952316284)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, 4171)
    CancelSpecialEffect(PLAYER, 4170)
    Restart()


@NeverRestart(30130519)
def Event_30130519():
    """Event 30130519"""
    EndIfFlagEnabled(30130519)
    EnableFlag(30130510)


@RestartOnRest(30130790)
def Event_30130790(_, obj: uint, flag: uint):
    """Event 30130790"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfThisEventSlotFlagDisabled(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    EnableObjectActivation(obj, obj_act_id=-1)
    End()


@RestartOnRest(30132800)
def Event_30132800():
    """Event 30132800"""
    EndIfFlagEnabled(30130800)
    IfHealthValueLessThanOrEqual(MAIN, 30130800, value=0)
    Wait(4.0)
    PlaySoundEffect(30130800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30130800)
    KillBossAndDisplayBanner(character=30130800, banner_type=BannerType.DutyFulfilled)
    Kill(30130292, award_souls=True)
    Kill(30130293, award_souls=True)
    Kill(30130298, award_souls=True)
    Kill(30130299, award_souls=True)
    EnableFlag(30130800)
    EnableFlag(9213)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61213)


@RestartOnRest(30132802)
def Event_30132802():
    """Event 30132802"""
    EndIfFlagEnabled(30130810)
    IfHealthValueLessThanOrEqual(MAIN, 30130810, value=0)
    Wait(4.0)
    PlaySoundEffect(30130810, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30130810)
    KillBossAndDisplayBanner(character=30130810, banner_type=BannerType.Unknown)
    EnableFlag(30130810)


@RestartOnRest(30132810)
def Event_30132810():
    """Event 30132810"""
    GotoIfFlagDisabled(Label.L0, flag=30130800)
    DisableCharacter(30130800)
    DisableAnimations(30130800)
    Kill(30130800)
    DisableCharacter(30130292)
    DisableAnimations(30130292)
    Kill(30130292)
    DisableCharacter(30130293)
    DisableAnimations(30130293)
    Kill(30130293)
    DisableCharacter(30130298)
    DisableAnimations(30130298)
    Kill(30130298)
    DisableCharacter(30130299)
    DisableAnimations(30130299)
    Kill(30130299)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30130800)
    IfFlagEnabled(AND_2, 30132805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30132800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30130800)
    SetNetworkUpdateRate(30130800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30130800, name=903400301)


@RestartOnRest(30132811)
def Event_30132811():
    """Event 30132811"""
    EndIfFlagEnabled(30130800)
    IfHealthLessThanOrEqual(AND_1, 30130800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30132802)


@RestartOnRest(30132812)
def Event_30132812():
    """Event 30132812"""
    GotoIfFlagDisabled(Label.L0, flag=30130810)
    DisableCharacter(30130810)
    DisableAnimations(30130810)
    Kill(30130810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30130810)
    IfFlagEnabled(AND_2, 30132815)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30132810)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30130810)
    SetNetworkUpdateRate(30130800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30130810)


@RestartOnRest(30132849)
def Event_30132849():
    """Event 30132849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30130800, 30131800, 30132800, 30132805, 30135800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30130800, 30131800, 30132800, 30132805, 30132806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30130800, 30131800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30130800, 900000, 30132805, 30132806, 0, 30132802, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(30132850)
def Event_30132850():
    """Event 30132850"""
    RunCommonEvent(
        0,
        9005800,
        args=(30130810, 30131810, 30132810, 30132815, 30135810, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30130810, 30131810, 30132810, 30132815, 30132816, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30130810, 30131810, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30130810, 930000, 30132815, 30132816, 0, 11002852, 0, 0), arg_types="IiIIIIii")
