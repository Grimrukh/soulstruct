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
    RunCommonEvent(1, 90005600, args=(76352, 1036541951, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(
        0,
        90005100,
        args=(71602, 76352, 1036541981, 77350, 3, 78350, 78351, 78352, 78353, 78354, 78355, 78356, 78357, 78358, 78359),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(2, 90005600, args=(76353, 1036541952, 5.0, 0), arg_types="IIfI")
    RunCommonEvent(0, 90005261, args=(1036540800, 1036542805, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005870, args=(1036540800, 904680603, 19), arg_types="IiI")
    RunCommonEvent(0, 90005860, args=(1036540800, 0, 1036540800, 0, 30375, 0.0), arg_types="IIIIif")
    Event_1036542350(0, region=1036542450, special_effect_id=16488, special_effect_id_1=16489)
    RunCommonEvent(0, 90005300, args=(1036540498, 1036540498, 40334, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005261, args=(1036540210, 1036542210, 5.0, 0.30000001192092896, 0), arg_types="IIffi")
    RunCommonEvent(2, 90005261, args=(1036540212, 1036542210, 5.0, 0.20000000298023224, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1036540208, 1036542220, 5.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(1036540425, 1036542425, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1036540426, 1036542425, 2.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(1036540414, 1036542414, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(
        0,
        90005211,
        args=(1036540410, 30010, 20010, 1036542410, 10.0, 7.099999904632568, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        1,
        90005211,
        args=(1036540411, 30010, 20010, 1036542410, 10.0, 7.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        2,
        90005211,
        args=(1036540204, 30010, 20010, 1036542410, 10.0, 7.199999809265137, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        3,
        90005211,
        args=(1036540205, 30010, 20010, 1036542410, 10.0, 7.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        4,
        90005211,
        args=(1036540450, 30000, 20000, 1036542410, 5.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005250, args=(1036540305, 1036542305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(1036540306, 1036542305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(2, 90005250, args=(1036540307, 1036542305, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005391, args=(1036540350, 1036542350, 1036540350, 1036540355, 1), arg_types="IIIIi")
    Event_1036542250(
        0,
        flag=1036540350,
        flag_1=1036542350,
        anchor_entity=1036540350,
        character=1036540355,
        left=1,
        item_lot_param_id=1036540100
    )
    Event_1036542580()
    Event_1036542240(0, obj=1036541200, entity=1036541201, flag=82032)
    Event_1036542301()
    Event_1036542300(0, 1036541300, 0.800000011920929)
    Event_1036542300(1, 1036541301, 0.0)
    Event_1036542300(2, 1036541302, 4.400000095367432)
    Event_1036542300(3, 1036541303, 1.100000023841858)
    Event_1036542300(4, 1036541304, 6.0)
    Event_1036542300(5, 1036541305, 7.0)
    Event_1036542300(6, 1036541306, 1.0)
    Event_1036542300(7, 1036541307, 1.5)
    Event_1036542300(8, 1036541308, 3.5999999046325684)
    Event_1036542300(9, 1036541309, 5.0)
    Event_1036542300(10, 1036541310, 3.5)
    Event_1036542300(11, 1036541311, 6.0)
    Event_1036542300(12, 1036541312, 4.0)
    Event_1036542300(13, 1036541313, 4.099999904632568)
    Event_1036542300(14, 1036541314, 7.400000095367432)
    Event_1036542300(15, 1036541315, 4.400000095367432)
    Event_1036542300(16, 1036541316, 6.5)
    Event_1036542300(17, 1036541317, 7.599999904632568)
    Event_1036542300(18, 1036541318, 6.599999904632568)
    Event_1036542300(19, 1036541319, 7.0)
    Event_1036542300(20, 1036541320, 7.099999904632568)
    Event_1036542300(21, 1036541321, 7.5)
    Event_1036542300(22, 1036541322, 0.30000001192092896)
    Event_1036542300(23, 1036541323, 4.199999809265137)
    Event_1036542300(24, 1036541324, 0.0)
    Event_1036542300(25, 1036541325, 1.0)
    Event_1036542500()
    Event_1036542450(0, obj=1036541400)
    Event_1036542450(1, obj=1036541401)
    Event_1036542450(2, obj=1036541402)
    Event_1036542450(3, obj=1036541403)
    Event_1036542450(4, obj=1036541404)
    Event_1036542450(5, obj=1036541405)
    Event_1036542450(6, obj=1036541406)
    Event_1036542450(7, obj=1036541407)
    Event_1036542450(8, obj=1036541408)
    RunCommonEvent(0, 90005706, args=(1036540701, 930021, 0), arg_types="IiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1036540701)


@NeverRestart(1036542580)
def Event_1036542580():
    """Event 1036542580"""
    RegisterLadder(start_climbing_flag=1036540580, stop_climbing_flag=1036540851, obj=1036541580)


@RestartOnRest(1036542200)
def Event_1036542200(_, character: uint):
    """Event 1036542200"""
    Kill(character)
    End()


@RestartOnRest(1036542240)
def Event_1036542240(_, obj: uint, entity: uint, flag: uint):
    """Event 1036542240"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(MAIN, flag)
    ForceAnimation(entity, 1, unknown2=1.0)
    DeleteObjectVFX(obj)


@RestartOnRest(1036542250)
def Event_1036542250(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 1036542250"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(5.0)
    DisableCharacter(character)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfValueEqual(1, left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(1036542400)
def Event_1036542400(_, character: uint, region: uint, seconds: float):
    """Event 1036542400"""
    DisableAI(character)
    DisableGravity(character)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    Wait(seconds)
    ForceAnimation(character, 3032, wait_for_completion=True, unknown2=1.0)
    EnableAI(character)
    Wait(2.799999952316284)
    EnableGravity(character)
    End()


@RestartOnRest(1036542450)
def Event_1036542450(_, obj: uint):
    """Event 1036542450"""
    DisableObject(obj)
    End()


@NeverRestart(1036542500)
def Event_1036542500():
    """Event 1036542500"""
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542350, 1036541350, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542351, 1036541351, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542352, 1036541352, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542353, 1036541353, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542354, 1036541354, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542355, 1036541355, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542356, 1036541356, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542357, 1036541357, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 57)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003270, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 56)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003260, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 55)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003250, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 54)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003240, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 53)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003230, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 52)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003220, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 51)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003210, 1.0, 0.0, 1.0), arg_types="IIiiifff")
    SkipLinesIfFlagDisabled(1, 50)
    RunCommonEvent(0, 90005694, args=(1036542358, 1036541358, 200, 0, 802003200, 1.0, 0.0, 1.0), arg_types="IIiiifff")


@RestartOnRest(1036542300)
def Event_1036542300(_, source_entity: uint, seconds: float):
    """Event 1036542300"""
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    Wait(seconds)
    DisableThisSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803240,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803250,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803260,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=1036540400,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802803270,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(8.0)
    RestartIfConditionTrue(input_condition=MAIN)


@RestartOnRest(1036542301)
def Event_1036542301():
    """Event 1036542301"""
    CreateProjectileOwner(entity=1036540400)


@RestartOnRest(1036542350)
def Event_1036542350(_, region: uint, special_effect_id: int, special_effect_id_1: int):
    """Event 1036542350"""
    EndIfFlagEnabled(1036540800)
    DisableNetworkSync()
    IfCharacterInsideRegion(AND_1, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(20000, special_effect_id)
    Wait(0.10000000149011612)
    IfCharacterOutsideRegion(AND_2, character=20000, region=region)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(0.10000000149011612)
    AddSpecialEffect(20000, special_effect_id_1)
    Restart()


@RestartOnRest(1036542800)
def Event_1036542800():
    """Event 1036542800"""
    EndIfFlagEnabled(1036540800)
    DisableAI(1036540800)
    DisableCharacter(1036540800)
    GotoIfFlagEnabled(Label.L0, flag=1036540805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1036542800)
    IfActionButtonParamActivated(AND_1, action_button_id=9000, entity=1036541800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableObject(1036541800)
    EnableCharacter(1036540800)
    ForceAnimation(1036540800, 20016, wait_for_completion=True, unknown2=1.0)
    EnableAI(1036540800)
    SetNetworkUpdateRate(1036540800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1036542800)
    DisableAI(1036540800)
    ForceAnimation(1036540800, 3030, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Wait(3.4000000953674316)
    Move(1036540800, destination=1036542801, destination_type=CoordEntityType.Region, model_point=0, short_move=True)
    DisableCharacter(1036540800)
    EnableNetworkFlag(1036540805)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1036542802)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=1036542800)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Move(1036540800, destination=1036542801, destination_type=CoordEntityType.Region, model_point=0, short_move=True)
    Wait(3.0)
    EnableCharacter(1036540800)
    ForceAnimation(1036540800, 20016, wait_for_completion=True, unknown2=1.0)
    EnableAI(1036540800)
    SetNetworkUpdateRate(1036540800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    IfCharacterOutsideRegion(MAIN, character=PLAYER, region=1036542800)
    DisableAI(1036540800)
    ForceAnimation(1036540800, 3030, loop=True, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    Wait(3.4000000953674316)
    Move(1036540800, destination=1036542801, destination_type=CoordEntityType.Region, model_point=0, short_move=True)
    DisableCharacter(1036540800)
    Restart()


@RestartOnRest(1036542801)
def Event_1036542801():
    """Event 1036542801"""
    EndIfFlagEnabled(1036540800)
    IfHealthValueLessThanOrEqual(MAIN, 1036540800, value=0)
    Wait(4.0)
    PlaySoundEffect(1036540800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1036540800)
    KillBossAndDisplayBanner(character=1036540800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(1036540800)


@RestartOnRest(1036542810)
def Event_1036542810():
    """Event 1036542810"""
    GotoIfFlagDisabled(Label.L0, flag=1036540800)
    DisableCharacter(1036540800)
    DisableAnimations(1036540800)
    Kill(1036540800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1036540800)
    DisableCharacter(1036540800)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=1036542800)
    EnableCharacter(1036540800)
    ForceAnimation(1036540800, 20016, wait_for_completion=True, unknown2=1.0)
    EnableAI(1036540800)
    SetNetworkUpdateRate(1036540800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableNetworkFlag(1036540801)


@RestartOnRest(1036542849)
def Event_1036542849():
    """Event 1036542849"""
    RunCommonEvent(0, 9005822, args=(1036540800, 90003101, 0, 0, 0, 0, 0, 0), arg_types="IiIIIIii")
