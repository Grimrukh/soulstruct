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
    RunCommonEvent(0, 90005600, args=(1038540000, 1038541950, 5.0, 1038540480), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005100,
        args=(71602, 76351, 1038541980, 77350, 2, 78350, 78351, 78352, 78353, 78354, 78355, 78356, 78357, 78358, 78359),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 90005870, args=(1038540800, 904680601, 19), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1038540800, 1038540800, 1038540800, 0, 0, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005250, args=(1038540229, 1038542229, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1038540227, 1038542229, 1.0, -1), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(1038540228, 1038542229, 6.0, -1), arg_types="IIfi")
    Event_1038542260(0, character=1038540229)
    Event_1038542260(1, character=1038540227)
    Event_1038542260(2, character=1038540228)
    RunCommonEvent(0, 90005261, args=(1038540200, 1038542220, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1038540201, 1038542220, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(
        0,
        90005790,
        args=(0, 1038540410, 1038542410, 1038542411, 1038540700, 22, 1038542701, 1038542700, 0.0, 0, 0, 0),
        arg_types="IIIIIiIIfIBi",
    )
    RunCommonEvent(0, 90005791, args=(1038540410, 1038542410, 1038542411, 1038540700), arg_types="IIII")
    RunCommonEvent(
        0,
        90005792,
        args=(1038540410, 1038542410, 1038542411, 1038540700, 1038540700, 0.0),
        arg_types="IIIIif",
    )
    RunCommonEvent(
        0,
        90005793,
        args=(1038540410, 1038542410, 1038542411, 1038540700, 1038542701, 1038542702, 0),
        arg_types="IIIIIIi",
    )
    RunCommonEvent(0, 90005261, args=(1038540370, 1038542370, 5.0, 3.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1038540371, 1038542370, 5.0, 3.0999999046325684, -1), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(1038540372, 1038542370, 5.0, 3.200000047683716, -1), arg_types="IIffi")
    Event_1038542270(0, character=1038540370)
    Event_1038542270(1, character=1038540371)
    Event_1038542270(2, character=1038540372)
    RunCommonEvent(0, 90005261, args=(1038540380, 1038542380, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1038540381, 1038542381, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(1038540382, 1038542382, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(3, 90005261, args=(1038540383, 1038542383, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(4, 90005261, args=(1038540384, 1038542384, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(5, 90005261, args=(1038540385, 1038542385, 5.0, 0.0, 3020), arg_types="IIffi")
    RunCommonEvent(
        4,
        90005211,
        args=(1038540250, 30005, 20005, 1038542370, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005201, args=(1038540211, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540212, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540213, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540268, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540269, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540270, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540271, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540272, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540273, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540274, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540275, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540276, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540277, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540278, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540279, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540280, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540281, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540282, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540283, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540284, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540285, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540286, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540287, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540288, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540289, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540290, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540291, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540292, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540294, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540295, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540296, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540297, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(1038540298, 30007, 20007, 3.5, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(1038540205, 30010, 20010, 1038542205, 10.0, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1038540206, 30010, 20010, 1038542205, 10.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    Event_1038542250(0, attacker__character=1038545200, region=1038542200)
    RunCommonEvent(0, 90005261, args=(1038540340, 1039532350, 10.0, 1.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1038540341, 1039532350, 10.0, 0.0, -1), arg_types="IIffi")
    Event_1038542340()
    RunCommonEvent(0, 90005251, args=(1038540330, 8.0, 0.0, -1), arg_types="Iffi")
    Event_1038542580()
    RunCommonEvent(0, 90005300, args=(1038540400, 1038540400, 1038540100, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005200, args=(1038540390, 30020, 20020, 1038542390, 2.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1038542400()
    Event_1038542500()
    Event_1038542450(0, obj=1038541400)
    Event_1038542450(1, obj=1038541401)
    Event_1038542450(2, obj=1038541402)
    Event_1038542450(3, 1038541403)


@NeverRestart(1038542580)
def Event_1038542580():
    """Event 1038542580"""
    RegisterLadder(start_climbing_flag=1038540580, stop_climbing_flag=1038540581, obj=1038541580)
    RegisterLadder(start_climbing_flag=1038540582, stop_climbing_flag=1038540583, obj=1038541582)
    RegisterLadder(start_climbing_flag=1038540584, stop_climbing_flag=1038540585, obj=1038541584)
    RegisterLadder(start_climbing_flag=1038540586, stop_climbing_flag=1038540587, obj=1038541586)
    RegisterLadder(start_climbing_flag=1038540588, stop_climbing_flag=1038540589, obj=1038541588)
    RegisterLadder(start_climbing_flag=1038540590, stop_climbing_flag=1038540591, obj=1038541590)


@RestartOnRest(1038542250)
def Event_1038542250(_, attacker__character: uint, region: uint):
    """Event 1038542250"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5660)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1050562200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5660)
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
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=attacker__character, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1050562200)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5660)


@RestartOnRest(1038542260)
def Event_1038542260(_, character: uint):
    """Event 1038542260"""
    AddSpecialEffect(character, 8087)
    End()


@RestartOnRest(1038542270)
def Event_1038542270(_, character: uint):
    """Event 1038542270"""
    AddSpecialEffect(character, 8092)
    End()


@RestartOnRest(1038542340)
def Event_1038542340():
    """Event 1038542340"""
    IfCharacterInsideRegion(MAIN, character=1038540340, region=1038542340)
    ChangePatrolBehavior(1038540340, patrol_information_id=1038543340)
    End()


@RestartOnRest(1038542400)
def Event_1038542400():
    """Event 1038542400"""
    IfCharacterDead(OR_1, 1038540400)
    IfCharacterDead(OR_1, 1038540390)
    EndIfConditionTrue(input_condition=OR_1)
    SetTeamType(1038540400, TeamType.ArchEnemyTeam)
    SetTeamType(1038540390, TeamType.ArchEnemyTeam)
    End()


@RestartOnRest(1038542450)
def Event_1038542450(_, obj: uint):
    """Event 1038542450"""
    DisableObject(obj)
    End()


@NeverRestart(1038542500)
def Event_1038542500():
    """Event 1038542500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1038542200, 1038541200, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1038542201, 1038541201, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1038542202, 1038541202, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1038542203, 1038541203, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
