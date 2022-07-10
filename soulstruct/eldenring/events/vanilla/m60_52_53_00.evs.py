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
    RegisterGrace(grace_flag=1052530000, obj=1052531950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76510, 76508, 1052531980, 77500, 7, 78500, 78501, 78502, 78503, 78504, 78505, 78506, 78507, 78508, 78509),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1052532500()
    Event_1052532510()
    RunCommonEvent(0, 90005771, args=(1052530950, 1052532710), arg_types="II")
    Event_1052533700()
    Event_1052533701()


@RestartOnRest(1052532500)
def Event_1052532500():
    """Event 1052532500"""
    GotoIfFlagDisabled(Label.L0, flag=1252520800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(1052530100, 9531)
    GotoIfFlagEnabled(Label.L1, flag=1252520801)
    IfFlagEnabled(MAIN, 1252520801)
    GotoIfConditionTrue(Label.L2, input_condition=MAIN)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_1, attacked_entity=1052520801, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_1, entity=1052520801, other_entity=PLAYER, radius=120.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1052532800)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1052532801)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagEnabled(AND_2, 1252522805)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(1052530100, 9532)
    End()


@RestartOnRest(1052532510)
def Event_1052532510():
    """Event 1052532510"""
    EndIfFlagEnabled(1254560800)
    SetCharacterTalkRange(character=1052530100, distance=300.0)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    RunCommonEvent(0, 90005781, args=(1252520800, 1252532160, 1252532161, 1052530700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1252520800, 1252532160, 1252532161, 1052530700, 1052532700, 1052532162, 2),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005781, args=(1252520800, 1252532164, 1252532165, 1052530701), arg_types="IIII")
    RunCommonEvent(
        0,
        90005783,
        args=(1252520800, 1252532164, 1252532165, 1052530701, 1052532701, 1052532162, 2),
        arg_types="IIIIIIi",
    )
    Event_1052532400(
        0,
        1252520800,
        1252532160,
        1252532161,
        1052530700,
        1052532700,
        1035539209,
        0,
        1252532400,
        1252532401,
    )
    Event_1052532400(
        1,
        1252520800,
        1252532164,
        1252532165,
        1052530701,
        1052532701,
        1035539209,
        0,
        1252532401,
        1252532400,
    )


@NeverRestart(1052532400)
def Event_1052532400(
    _,
    flag: uint,
    summon_flag: uint,
    dismissal_flag: uint,
    character: uint,
    region: uint,
    right: uint,
    unknown: uchar,
    flag_1: uint,
    flag_2: uint,
):
    """Event 1052532400"""
    SkipLinesIfPlayerNotInOwnWorld(1)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    EndIfFlagEnabled(flag)
    SkipLinesIfUnsignedEqual(1, left=0, right=right)
    IfFlagEnabled(AND_1, right)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterBackreadEnabled(AND_1, character)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=character, radius=10.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EndIfFlagEnabled(flag_2)
    EnableFlag(flag_1)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    EnableNetworkFlag(1252520804)

    # --- Label 1 --- #
    DefineLabel(1)
    PlaceSummonSign(
        sign_type=SummonSignType.Unknown20,
        character=character,
        region=region,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
        unknown=unknown,
    )


@RestartOnRest(1052533700)
def Event_1052533700():
    """Event 1052533700"""
    EndIfFlagEnabled(1052520800)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, 1052520800)
    IfFlagEnabled(OR_1, 1252532160)
    IfFlagEnabled(OR_1, 1252532164)
    IfConditionTrue(AND_1, input_condition=OR_1)
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(13009259)
    End()


@RestartOnRest(1052533701)
def Event_1052533701():
    """Event 1052533701"""
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(AND_1, flag_range=(3661, 3663))
    AwaitConditionTrue(AND_1)
    DisableNetworkFlag(1035539209)
    End()
