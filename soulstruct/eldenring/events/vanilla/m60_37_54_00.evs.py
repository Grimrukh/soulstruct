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
    RunCommonEvent(0, 90005250, args=(1037540341, 1037542341, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1037540341, 1037542342, 0.0, 0), arg_types="IIfi")
    Event_1037542500()
    RunCommonEvent(0, 90005300, args=(1037540341, 1037540341, 0, 3.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005271, args=(1037540253, 0.0, -1), arg_types="Ifi")
    Event_1037542260()
    RunCommonEvent(0, 90005250, args=(1037540250, 1037542250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1037540251, 1037542250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(1037540252, 1037542250, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1037540350, 30010, 20010, 1037542350, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005261, args=(1037540235, 1037542235, 5.0, 0.0, 3004), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037540351, 1037542351, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1037540352, 1037542351, 0.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1037540210, 1037542210, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1037540211, 1037542210, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(1037540212, 1037542210, 0.20000000298023224, 0), arg_types="IIfi")
    RunCommonEvent(3, 90005250, args=(1037540213, 1037542210, 0.10000000149011612, 0), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005200,
        args=(1037540214, 30001, 20001, 1037542215, 1.399999976158142, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(1, 90005200, args=(1037540215, 30001, 20001, 1037542215, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1037542220(0, 1037540260, 1037542360, 1037542260, 0.0)
    Event_1037542220(1, 1037540261, 1037542360, 1037542261, 1.0)
    Event_1037542220(2, 1037540262, 1037542360, 1037542262, 2.0)
    Event_1037542220(3, 1037540263, 1037542360, 1037542263, 0.20000000298023224)
    Event_1037542220(4, 1037540264, 1037542360, 1037542264, 0.10000000149011612)
    Event_1037542220(5, 1037540265, 1037542360, 1037542265, 1.100000023841858)
    Event_1037542220(6, 1037540266, 1037542360, 1037542266, 0.30000001192092896)
    Event_1037542220(7, 1037540267, 1037542360, 1037542267, 0.10000000149011612)
    Event_1037542220(8, 1037540268, 1037542360, 1037542268, 2.0999999046325684)
    Event_1037542220(9, 1037540269, 1037542360, 1037542269, 2.299999952316284)
    Event_1037542220(10, 1037540270, 1037542360, 1037542270, 2.5999999046325684)
    Event_1037542220(11, 1037540271, 1037542360, 1037542271, 2.4000000953674316)
    Event_1037542220(12, 1037540272, 1037542360, 1037542272, 2.700000047683716)
    Event_1037542220(13, 1037540273, 1037542360, 1037542273, 2.5)
    Event_1037542220(14, 1037540274, 1037542360, 1037542274, 2.0999999046325684)
    Event_1037542220(15, 1037540275, 1037542360, 1037542275, 2.200000047683716)
    RunCommonEvent(0, 90005251, args=(1037540370, 6.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(1037540301, 1037542304, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037540302, 1037542304, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037540306, 1037542306, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1037540303, 1037542306, 15.0, 0.0, -1), arg_types="IIffi")
    Event_1037542250(0, character=1037540339)
    Event_1037542250(1, character=1037540340)
    Event_1037542250(2, character=1037540303)
    RunCommonEvent(0, 90005200, args=(1037540304, 30000, 20000, 1037542304, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_1037542250(3, character=1037540306)
    Event_1037542300()
    RunCommonEvent(1, 90005250, args=(1037540440, 1037542810, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(1037540810, 30000, 20000, 1037542810, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005870, args=(1037540810, 904640600, 18), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1037540810, 0, 1037540810, 0, 30380, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005872, args=(1037540810, 18, 0), arg_types="III")
    Event_1037542255()
    Event_1037542270(0, attacker__character=1037545810, region=1037542810)
    Event_1037542580()
    RunCommonEvent(
        0,
        90005620,
        args=(1037540570, 1037541570, 1037541571, 1037541572, 1037542571, 1037542572, 1037542573),
        arg_types="IIIIIIi",
    )
    Event_1037542569(0, flag=1037540570, obj=1037541573)
    RunCommonEvent(0, 90005631, args=(1037541205, 61033), arg_types="Ii")
    Event_1037543700(0, character=1037540700)
    Event_1037543704(0, character=1037540701)
    Event_1037543701()
    Event_1037543702(
        0,
        character=1037540700,
        flag=1037542701,
        flag_1=1037549201,
        character_1=1037540701,
        flag_2=1037549216
    )
    Event_1037543703()
    Event_1037543705()
    Event_1037543706()
    RunCommonEvent(0, 90005704, args=(1037540700, 3681, 3680, 1037549201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1037540700, 3681, 3682, 1037549201, 3681, 3680, 3684, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1037540700, 3683, 3680, 3684), arg_types="IIII")
    RunCommonEvent(0, 90005704, args=(1037540701, 3681, 3680, 1037549216, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1037540701, 3681, 3682, 1037549216, 3681, 3680, 3684, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1037540701, 3683, 3680, 3684), arg_types="IIII")
    RunCommonEvent(
        0,
        90005725,
        args=(4770, 4771, 4773, 1037549255, 1037540705, 1037540706, 1037546700),
        arg_types="IIIIIII",
    )
    RunCommonEvent(0, 90005703, args=(1037540705, 4771, 4772, 1037549256, 4771, 4770, 4774, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1037540705, 4771, 4770, 1037549256, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(1037540705, 4773, 4770, 4774), arg_types="IIII")
    RunCommonEvent(0, 90005703, args=(1037540706, 4771, 4772, 1037549257, 4771, 4770, 4774, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(1037540706, 4771, 4770, 1037549257, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005728, args=(1037540706, 1037542716, 1037542717), arg_types="III")
    RunCommonEvent(0, 90005727, args=(4771, 1037540705, 1037540706, 4770, 4773), arg_types="IIIII")
    RunCommonEvent(0, 90005729, args=(1037549250, 1037540705, 36.0, 1037542712), arg_types="IIfI")
    Event_1037542350()
    Event_1037542351(0, flag=1037547060, flag_1=1037540220)
    Event_1037542351(1, flag=1037547080, flag_1=1037540221)
    Event_1037542351(2, flag=1037547090, flag_1=1037540222)
    Event_1037542351(3, flag=1037547070, flag_1=1037540223)
    Event_1037542505()
    Event_1037542450(0, obj=1037541400)
    Event_1037542450(1, obj=1037541401)
    Event_1037542450(2, obj=1037541402)
    Event_1037542450(3, obj=1037541403)
    Event_1037542450(4, obj=1037541404)
    Event_1037542450(5, obj=1037541405)
    Event_1037542450(6, obj=1037541406)
    Event_1037542450(7, obj=1037541407)
    Event_1037542450(8, 1037541408)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1037540700)
    DisableBackread(1037540701)
    DisableBackread(1037540705)
    DisableBackread(1037540706)
    RunCommonEvent(0, 90005261, args=(1037540360, 1037542450, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1037540361, 1037542452, 5.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(1, 90005261, args=(1037540362, 1037542452, 5.0, 0.0, -1), arg_types="IIffi")
    Event_1037542400(0, character=1037540360)
    Event_1037542400(2, character=1037540361)
    Event_1037542400(3, character=1037540362)
    Event_1037542210(0, character__targeting_character=1037540360, region=1037542460)
    Event_1037542210(1, character__targeting_character=1037540361, region=1037542461)
    Event_1037542210(2, 1037540362, 1037542461)


@RestartOnRest(1037542210)
def Event_1037542210(_, character__targeting_character: uint, region: uint):
    """Event 1037542210"""
    DisableNetworkSync()
    IfCharacterDead(AND_1, character__targeting_character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterTargeting(AND_1, targeting_character=character__targeting_character, targeted_character=20000)
    IfCharacterOutsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ClearTargetList(character__targeting_character)
    Wait(5.0)
    Restart()


@RestartOnRest(1037542220)
def Event_1037542220(_, character: uint, region: uint, destination: uint, seconds: float):
    """Event 1037542220"""
    DisableCharacter(character)
    DisableInvincibility(character)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(character)
    End()
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfPlayerInOwnWorld(OR_1)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableThisSlotFlag()
    Wait(seconds)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableInvincibility(character)
    Wait(3.0)
    DisableInvincibility(character)
    End()


@NeverRestart(1037542505)
def Event_1037542505():
    """Event 1037542505"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542410, 1037541300, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542411, 1037541301, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542412, 1037541302, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542413, 1037541303, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542414, 1037541304, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542415, 1037541305, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542416, 1037541306, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542417, 1037541307, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1037542418, 1037541308, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")


@NeverRestart(1037542580)
def Event_1037542580():
    """Event 1037542580"""
    RegisterLadder(start_climbing_flag=1037540580, stop_climbing_flag=1037540851, obj=1037541580)
    RegisterLadder(start_climbing_flag=1037540582, stop_climbing_flag=1037540853, obj=1037541582)
    RegisterLadder(start_climbing_flag=1037540584, stop_climbing_flag=1037540855, obj=1037541584)
    RegisterLadder(start_climbing_flag=1037540586, stop_climbing_flag=1037540857, obj=1037541586)
    RegisterLadder(start_climbing_flag=1037540588, stop_climbing_flag=1037540859, obj=1037541588)
    RegisterLadder(start_climbing_flag=1037540590, stop_climbing_flag=1037540861, obj=1037541590)
    RegisterLadder(start_climbing_flag=1037540592, stop_climbing_flag=1037540863, obj=1037541592)
    RegisterLadder(start_climbing_flag=1037540594, stop_climbing_flag=1037540865, obj=1037541594)
    RegisterLadder(start_climbing_flag=1037540596, stop_climbing_flag=1037540867, obj=1037541596)
    RegisterLadder(start_climbing_flag=1037540598, stop_climbing_flag=1037540869, obj=1037541598)
    RegisterLadder(start_climbing_flag=1037540600, stop_climbing_flag=1037540871, obj=1037541600)
    RegisterLadder(start_climbing_flag=1037540602, stop_climbing_flag=1037540873, obj=1037541602)
    RegisterLadder(start_climbing_flag=1037540604, stop_climbing_flag=1037540875, obj=1037541604)


@RestartOnRest(1037542250)
def Event_1037542250(_, character: uint):
    """Event 1037542250"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(character, 8087)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542255)
def Event_1037542255():
    """Event 1037542255"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(1037540810, 8087)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542260)
def Event_1037542260():
    """Event 1037542260"""
    SetTeamType(1037540250, TeamType.Enemy)
    SetTeamType(1037540251, TeamType.Enemy)
    SetTeamType(1037540252, TeamType.Enemy)
    SetTeamType(1037540253, TeamType.Enemy2)
    End()


@RestartOnRest(1037542270)
def Event_1037542270(_, attacker__character: uint, region: uint):
    """Event 1037542270"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5661)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1050562200)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5661)
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
    CancelSpecialEffect(attacker__character, 5661)


@RestartOnRest(1037542300)
def Event_1037542300():
    """Event 1037542300"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(MAIN, 1037540304, ai_status=AIStatusType.Battle)
    Wait(1.2999999523162842)
    ForceAnimation(1037540304, 3014, unknown2=1.0)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542350)
def Event_1037542350():
    """Event 1037542350"""
    DisableNetworkSync()
    DeleteVFX(1037542220, erase_root_only=False)
    DeleteVFX(1037542221, erase_root_only=False)
    DeleteVFX(1037542222, erase_root_only=False)
    DeleteVFX(1037542223, erase_root_only=False)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1037542225)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SkipLinesIfPlayerNotInOwnWorld(8)
    SkipLinesIfFlagEnabled(1, 1037540220)
    CreateVFX(1037542220)
    SkipLinesIfFlagEnabled(1, 1037540221)
    CreateVFX(1037542221)
    SkipLinesIfFlagEnabled(1, 1037540222)
    CreateVFX(1037542222)
    SkipLinesIfFlagEnabled(1, 1037540223)
    CreateVFX(1037542223)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1037542225)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(1037542220, erase_root_only=False)
    DeleteVFX(1037542221, erase_root_only=False)
    DeleteVFX(1037542222, erase_root_only=False)
    DeleteVFX(1037542223, erase_root_only=False)
    Restart()


@RestartOnRest(1037542351)
def Event_1037542351(_, flag: uint, flag_1: uint):
    """Event 1037542351"""
    IfFlagEnabled(MAIN, flag)
    EnableFlag(flag_1)
    End()


@RestartOnRest(1037542400)
def Event_1037542400(_, character: uint):
    """Event 1037542400"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, 30010, loop=True, skip_transition=True, unknown2=1.0)
    IfHasAIStatus(MAIN, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 20010, skip_transition=True, unknown2=1.0)
    DisableThisSlotFlag()
    End()


@RestartOnRest(1037542450)
def Event_1037542450(_, obj: uint):
    """Event 1037542450"""
    DisableObject(obj)
    End()


@RestartOnRest(1037542500)
def Event_1037542500():
    """Event 1037542500"""
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1037542342)
    CancelSpecialEffect(1037540341, 16283)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1037542342)
    AddSpecialEffect(1037540341, 16283)
    Restart()


@NeverRestart(1037542569)
def Event_1037542569(_, flag: uint, obj: uint):
    """Event 1037542569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=101, model_point=806043)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DeleteObjectVFX(obj)
    PlaySoundEffect(obj, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableObject(obj)


@RestartOnRest(1037542801)
def Event_1037542801():
    """Event 1037542801"""
    EndIfFlagEnabled(1037540810)
    IfHealthValueLessThanOrEqual(MAIN, 1037540810, value=0)
    Wait(4.0)
    PlaySoundEffect(1037540810, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1037540810)
    KillBossAndDisplayBanner(character=1037540810, banner_type=BannerType.DutyFulfilled)
    EnableFlag(1037540810)


@RestartOnRest(1037542810)
def Event_1037542810():
    """Event 1037542810"""
    DisableAI(1037540810)
    DisableCharacter(1037540810)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1037542810)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableCharacter(1037540810)
    EnableAI(1037540810)
    EnableFlag(1037542810)
    End()


@RestartOnRest(1037543700)
def Event_1037543700(_, character: uint):
    """Event 1037543700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3688)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3688)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagEnabled(OR_4, 3688)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1037543701)
def Event_1037543701():
    """Event 1037543701"""
    WaitFrames(frames=1)
    EndIfFlagEnabled(1037549210)
    EndIfFlagEnabled(3683)
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1045522710)
    IfFlagEnabled(AND_1, 3680)
    IfFlagEnabled(AND_1, 3688)
    IfCharacterNotMounted(AND_1, character=PLAYER)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1037549210)
    IfCharacterMounted(AND_2, character=PLAYER)
    SkipLinesIfConditionFalse(1, AND_2)
    Move(40000, destination=1045522712, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(9021)
    GotoIfPlayerInOwnWorld(Label.L1)
    IfCharacterHollow(OR_3, PLAYER)
    IfCharacterWhitePhantom(OR_3, PLAYER)
    IfCharacterType(OR_3, PLAYER, character_type=CharacterType.Unknown17)
    IfPlayerNotInOwnWorld(AND_3)
    IfConditionTrue(AND_3, input_condition=OR_3)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown15)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown16)
    IfCharacterType(OR_4, PLAYER, character_type=CharacterType.Unknown18)
    IfPlayerNotInOwnWorld(AND_4)
    IfConditionTrue(AND_4, input_condition=OR_4)
    GotoIfConditionTrue(Label.L3, input_condition=AND_4)
    Goto(Label.L4)

    # --- Label 1 --- #
    DefineLabel(1)
    UnknownCutscene_11(
        cutscene_id=60370000,
        cutscene_flags=0,
        move_to_region=1045522712,
        map_base_id=60375400,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    WaitFramesAfterCutscene(frames=1)
    EnableFlag(3698)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    UnknownCutscene_11(
        cutscene_id=60370000,
        cutscene_flags=0,
        move_to_region=1037542720,
        map_base_id=60375400,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    PlayCutscene(60370000, cutscene_flags=0, player_id=10000)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    End()


@RestartOnRest(1037543702)
def Event_1037543702(_, character: uint, flag: uint, flag_1: uint, character_1: uint, flag_2: uint):
    """Event 1037543702"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(3683)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    IfFlagDisabled(AND_1, 3688)
    IfFlagDisabled(AND_1, 3693)
    EndIfConditionTrue(input_condition=AND_1)
    GotoIfFlagDisabled(Label.L1, flag=3681)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(MAIN, 3681)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    IfFlagEnabled(AND_2, 3688)
    IfEntityWithinDistance(AND_2, entity=PLAYER, other_entity=character, radius=5.0)
    IfFlagEnabled(AND_3, 3693)
    IfEntityWithinDistance(AND_3, entity=PLAYER, other_entity=character_1, radius=5.0)
    IfConditionTrue(OR_4, input_condition=AND_2)
    IfConditionTrue(OR_4, input_condition=AND_3)
    IfCharacterHasSpecialEffect(AND_4, PLAYER, 9700)
    IfConditionTrue(AND_4, input_condition=OR_4)
    IfConditionTrue(MAIN, input_condition=AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(3680, 3684))
    EnableNetworkFlag(3680)
    SaveRequest()
    EnableNetworkFlag(flag)
    DisableNetworkFlag(flag_1)
    SkipLinesIfFlagDisabled(1, 3693)
    DisableNetworkFlag(flag_2)
    DisableNetworkFlag(31002701)
    DisableNetworkFlag(31002707)
    DisableNetworkFlag(31002700)
    DisableNetworkFlag(31009205)
    SetTeamType(character, TeamType.FriendlyNPC)
    SetTeamType(character_1, TeamType.FriendlyNPC)
    ClearTargetList(character)
    ClearTargetList(character_1)
    ReplanAI(character)
    ReplanAI(character_1)
    End()


@RestartOnRest(1037543703)
def Event_1037543703():
    """Event 1037543703"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(31009206)
    EndIfFlagEnabled(1037549211)
    IfFlagDisabled(AND_1, 3685)
    IfFlagDisabled(AND_1, 3686)
    IfFlagDisabled(AND_1, 3687)
    IfFlagDisabled(AND_1, 3688)
    IfFlagDisabled(AND_1, 3693)
    EndIfConditionTrue(input_condition=AND_1)
    EnableFlag(1037549211)
    WaitFrames(frames=1)
    EnableFlag(3698)
    End()


@RestartOnRest(1037543704)
def Event_1037543704(_, character: uint):
    """Event 1037543704"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagDisabled(1, 3680)
    DisableFlag(31009205)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3693)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_3, 3693)
    IfConditionTrue(MAIN, input_condition=OR_3)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3680)
    GotoIfFlagEnabled(Label.L2, flag=3681)
    GotoIfFlagEnabled(Label.L3, flag=3682)
    GotoIfFlagEnabled(Label.L4, flag=3683)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100, unknown2=1.0)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
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
    IfFlagEnabled(OR_4, 3693)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1037543705)
def Event_1037543705():
    """Event 1037543705"""
    WaitFrames(frames=1)
    SkipLinesIfFlagDisabled(7, 1037542705)
    CreateVFX(1045522711)
    CreateVFX(1037542710)
    CreateVFX(1037542711)
    CreateVFX(1037542712)
    CreateVFX(1037542713)
    EnableFlag(1037549212)
    End()
    DeleteVFX(1045522711, erase_root_only=False)
    DeleteVFX(1037542710, erase_root_only=False)
    DeleteVFX(1037542711, erase_root_only=False)
    DeleteVFX(1037542712, erase_root_only=False)
    DeleteVFX(1037542713, erase_root_only=False)
    DisableFlag(1037549212)
    EndIfFlagEnabled(3683)
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    IfFlagEnabled(OR_3, 3688)
    IfConditionTrue(MAIN, input_condition=OR_3)
    CreateVFX(1045522711)
    CreateVFX(1037542710)
    CreateVFX(1037542711)
    CreateVFX(1037542712)
    CreateVFX(1037542713)
    EnableFlag(1037549212)
    IfFlagEnabled(OR_4, 3688)
    IfConditionFalse(MAIN, input_condition=OR_4)
    Restart()


@RestartOnRest(1037543706)
def Event_1037543706():
    """Event 1037543706"""
    EndIfFlagEnabled(3683)
    EndIfFlagRangeAnyEnabled(flag_range=(3689, 3697))
    IfFlagEnabled(AND_1, 3688)
    IfFlagEnabled(AND_1, 3683)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1037542705)
    End()
