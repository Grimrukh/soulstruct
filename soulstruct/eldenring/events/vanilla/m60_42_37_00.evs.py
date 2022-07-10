"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1042370000, obj=1042371950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(71001, 76111, 1042371980, 77100, 2, 78100, 78101, 78102, 78103, 78104, 78105, 78106, 78107, 78108, 78109),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 900005610, args=(1042371680, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(0, 900005610, args=(1042371681, 100, 800, 0), arg_types="IiiI")
    RunCommonEvent(
        0,
        90005880,
        args=(1042370800, 1042370805, 1042372800, 1042370800, 30120, 60, 42, 37, 0, 1042372805),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1042370800, 1042370805, 1042372801, 1042372802, 20300, 1042371805, 60, 42, 37, 0, 1042372805),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1042370800,
            1042370805,
            1042372800,
            1042370800,
            1042372806,
            1042375810,
            1042371800,
            1042370810,
            1042372810,
            902500520,
            -1,
            20000,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1042370800, 1042370805, 1042371805), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1042370800, 0, 1042372806, 1042372807, 0, 1), arg_types="IiIIii")
    Event_1042372610()
    Event_1042372651(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370
    )
    Event_1042373700(0, flag=78102, other_entity=1042370950, flag_1=1042379204)
    Event_1042373701(0, other_entity=1042370950, flag=1042379204)
    Event_1042373702(0, other_entity=1042370950, flag=1042379205)
    Event_1042373703(0, 1042370950, 1042379205)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005251, args=(1042370200, 5.0, 0.0, -1), arg_types="Iffi")


@RestartOnRest(1042372610)
def Event_1042372610():
    """Event 1042372610"""
    DisableObject(1042371610)


@RestartOnRest(1042372620)
def Event_1042372620(_, obj: uint, entity: uint, flag: uint):
    """Event 1042372620"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1042372651)
def Event_1042372651(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1042372651"""
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfPlayerHasGood(AND_1, 130)
    IfInsideMap(AND_1, game_map=WEST_LIMGRAVE_SE_NW)
    IfPlayerDoesNotHaveGood(AND_1, 9109)
    IfTryingToCreateSession(OR_1)
    IfTryingToJoinSession(OR_1)
    IfConditionFalse(AND_1, input_condition=OR_1)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 100690)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, PLAYER, 9640)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    EndIfFlagEnabled(flag_2)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1042373700)
def Event_1042373700(_, flag: uint, other_entity: uint, flag_1: uint):
    """Event 1042373700"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(AND_1, flag)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagDisabled(AND_1, flag_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372701)
    IfFlagDisabled(OR_1, flag)
    IfEntityBeyondDistance(OR_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(OR_1, flag_1)
    IfConditionTrue(MAIN, input_condition=OR_1)
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1042373701)
def Event_1042373701(_, other_entity: uint, flag: uint):
    """Event 1042373701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(4680)
    IfFlagEnabled(MAIN, 4680)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042373702)
def Event_1042373702(_, other_entity: uint, flag: uint):
    """Event 1042373702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379203)
    IfFlagEnabled(MAIN, 1042379203)
    IfEntityWithinDistance(AND_2, entity=20000, other_entity=other_entity, radius=5.0)
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1042373703)
def Event_1042373703(_, other_entity: uint, flag: uint):
    """Event 1042373703"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(1042379207)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=other_entity, radius=5.0)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1042372702)
    IfEntityBeyondDistance(MAIN, entity=20000, other_entity=other_entity, radius=5.0)
    DisableFlag(1042372702)
    Restart()
