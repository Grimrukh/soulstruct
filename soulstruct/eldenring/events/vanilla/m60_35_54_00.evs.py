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
    RunCommonEvent(0, 90005261, args=(1035540400, 1035542400, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1035540200, 1035542200, 8.0, 0.5, -1), arg_types="IIffi")
    Event_1035542200(0, character=1035540200)
    RunCommonEvent(0, 90005261, args=(1035540210, 1035542210, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1035540211, 1035542210, 5.0, 0.0, -1), arg_types="IIffi")
    Event_1035542201(0, attacker__character=1035545201, region=1035542201)
    Event_1035542236(0, character=1035540450)
    Event_1035542236(1, character=1035540451)
    Event_1035542236(2, character=1035540452)
    Event_1035542236(3, character=1035540453)
    Event_1035542236(4, character=1035540454)
    Event_1035542236(5, character=1035540455)
    Event_1035542236(6, character=1035540456)
    Event_1035542236(7, character=1035540457)
    Event_1035542236(8, character=1035540458)
    Event_1035542236(9, character=1035540459)
    RunCommonEvent(0, 90005550, args=(1035540500, 1035541500, 1035543500), arg_types="III")
    RunCommonEvent(0, 90005511, args=(1035540560, 1035541560, 1035543560, 99020, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(1035540560, 1035542560, 1035542561), arg_types="III")
    Event_1035542580()
    Event_1035542500()
    Event_1035542450(0, obj=1035541400)
    RunCommonEvent(0, 90005261, args=(1035540310, 1035542310, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005200,
        args=(1035540260, 30000, 20000, 1035542260, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(1, 90005200, args=(1035540261, 30000, 20000, 1035542260, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        2,
        90005200,
        args=(1035540262, 30000, 20000, 1035542260, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1035540265, 30000, 20000, 1035542265, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1,
        90005200,
        args=(1035540266, 30000, 20000, 1035542265, 1.399999976158142, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        2,
        90005200,
        args=(1035540267, 30000, 20000, 1035542265, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        3,
        90005200,
        args=(1035540268, 30000, 20000, 1035542265, 1.600000023841858, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(1035540275, 30000, 20000, 1035542275, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(1035540280, 30000, 20000, 1035542280, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1,
        90005200,
        args=(1035540281, 30000, 20000, 1035542280, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1035540285, 30000, 20000, 1035542285, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1,
        90005200,
        args=(1035540286, 30000, 20000, 1035542285, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(1035540290, 30003, 20003, 1035542290, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        1,
        90005200,
        args=(1035540291, 30003, 20003, 1035542290, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        2,
        90005200,
        args=(1035540292, 30003, 20003, 1035542292, 0.10000000149011612, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(1035540300, 30004, 20004, 1035542300, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(1035540275, 30000, 20000, 1035542275, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(1035540256, 1035542301, 0.5, 20004), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1035540257, 1035542301, 1.0, 20004), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(1035540258, 1035542301, 1.2000000476837158, 20004), arg_types="IIfi")
    RunCommonEvent(4, 90005250, args=(1035540270, 1035542301, 1.5, -1), arg_types="IIfi")
    RunCommonEvent(5, 90005250, args=(1035540271, 1035542301, 1.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 900005610, args=(1035541680, 100, 800, 0), arg_types="IiiI")
    Event_1035542230()
    RunCommonEvent(0, 90005706, args=(1035540700, 930023, 0), arg_types="IiI")
    RunCommonEvent(0, 90005730, args=(1035542700, 10.0, 1035549200, 6001, 1035549201, 1035542702), arg_types="IfIIII")
    RunCommonEvent(
        0,
        90005730,
        args=(1035542700, 20.0, 1035549200, 1035542702, 1035549201, 1035549202),
        arg_types="IfIIII",
    )
    RunCommonEvent(0, 90005732, args=(1035549200, 1035542350, 1035542350), arg_types="III")
    Event_1035543700(0, 1035540700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1035540700)


@RestartOnRest(1035542200)
def Event_1035542200(_, character: uint):
    """Event 1035542200"""
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 3001, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(1035542201)
def Event_1035542201(_, attacker__character: uint, region: uint):
    """Event 1035542201"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5659)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1035542201)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5659)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1035542201)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5659)


@RestartOnRest(1035542220)
def Event_1035542220():
    """Event 1035542220"""
    AddSpecialEffect(1035540400, 8089)
    IfHasAIStatus(MAIN, 1035540400, ai_status=AIStatusType.Battle)
    ForceAnimation(1035540400, 3002, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(1035542230)
def Event_1035542230():
    """Event 1035542230"""
    EndOfAnimation(obj=1035541500, animation_id=1)
    End()


@RestartOnRest(1035542236)
def Event_1035542236(_, character: uint):
    """Event 1035542236"""
    RotateToFaceEntity(character, 1035542200, animation=5002)
    WaitFrames(frames=7)
    Kill(character)
    End()


@RestartOnRest(1035542450)
def Event_1035542450(_, obj: uint):
    """Event 1035542450"""
    DisableObject(obj)
    End()


@NeverRestart(1035542500)
def Event_1035542500():
    """Event 1035542500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1035542250, 1035541200, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")


@NeverRestart(1035542580)
def Event_1035542580():
    """Event 1035542580"""
    RegisterLadder(start_climbing_flag=1035540580, stop_climbing_flag=1035540581, obj=1035541580)


@RestartOnRest(1035543700)
def Event_1035543700(_, character: uint):
    """Event 1035543700"""
    EndIfFlagEnabled(1035549201)
    SetCharacterTalkRange(character=character, distance=35.0)
    IfFlagEnabled(MAIN, 1035549201)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()
