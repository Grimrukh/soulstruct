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
    RegisterGrace(grace_flag=71211, obj=12011951, unknown=5.0)
    RegisterGrace(grace_flag=71212, obj=12011952, unknown=5.0)
    RegisterGrace(grace_flag=71213, obj=12011953, unknown=5.0)
    RegisterGrace(grace_flag=71214, obj=12011954, unknown=5.0)
    RegisterGrace(grace_flag=71215, obj=12011955, unknown=5.0)
    RegisterGrace(grace_flag=71216, obj=12011956, unknown=5.0)
    RegisterGrace(grace_flag=71217, obj=12011957, unknown=5.0)
    RegisterGrace(grace_flag=71218, obj=12011958, unknown=5.0)
    RegisterGrace(grace_flag=71219, obj=12011959, unknown=5.0)
    RunCommonEvent(0, 9005810, args=(12010800, 71210, 12010950, 12011950, 5.0), arg_types="IIIIf")
    RunCommonEvent(
        0,
        90005620,
        args=(12010570, 12011570, 12011571, 0, 12012570, 12012571, 12012572),
        arg_types="IIIIIIi",
    )
    Event_12012569(0, flag=12010570, obj=12011573)
    Event_12012569(1, flag=12010570, obj=12011575)
    RunCommonEvent(0, 90005251, args=(12010201, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010202, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010204, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010207, 10.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010214, 40.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(12010203, 30001, 20001, 14.0, 0.5, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005201, args=(12010205, 30001, 20001, 10.0, 2.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005250, args=(12010210, 12012200, 0.5, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(12010211, 30009, 20022, 12012211, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010212, 30009, 20022, 12012211, 10.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005251, args=(12010216, 3.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005201, args=(12010222, 30001, 20001, 8.0, 0.0, 1, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005300, args=(12010240, 12010240, 12010105, 3.5, 0), arg_types="IIifi")
    Event_12012220(0, character=12010231)
    Event_12012220(1, character=12010232)
    Event_12012220(2, character=12010233)
    Event_12012220(3, character=12010234)
    Event_12012220(4, character=12010235)
    Event_12012220(5, character=12010236)
    Event_12012220(6, character=12010237)
    Event_12012220(7, character=12010240)
    Event_12012231(0, 12010231, 0.0)
    Event_12012231(1, 12010232, 3.0)
    Event_12012231(2, 12010233, 6.0)
    Event_12012231(3, 12010234, 9.0)
    Event_12012231(4, 12010235, 12.0)
    Event_12012231(5, 12010236, 12.0)
    Event_12012231(6, 12010237, 16.0)
    RunCommonEvent(0, 90005261, args=(12010245, 12012245, 30.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(12010246, 12012246, 1.0, -1), arg_types="IIfi")
    Event_12012239()
    Event_12012249()
    Event_12012240()
    Event_12012256()
    Event_12012257()
    Event_12012288(0, character=12010298, character_1=12010248, region=12022298)
    Event_12012288(1, character=12010299, character_1=12010249, region=12022299)
    RunCommonEvent(0, 90005261, args=(12010251, 12012251, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005250, args=(12010260, 12012260, 0.5, 3006), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12010263, 12012260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12010264, 12012260, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(12010276, 25.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005261, args=(12015280, 12012280, 10.0, 0.0, -1), arg_types="IIffi")
    RunCommonEvent(0, 90005200, args=(12010288, 30000, 20000, 12012288, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010289, 30000, 20000, 12012289, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010290, 30000, 20000, 12012290, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010291, 30000, 20000, 12012290, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010292, 30000, 20000, 12012290, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_12012301()
    RunCommonEvent(0, 90005251, args=(12010305, 5.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005200, args=(12010320, 30001, 20001, 12012320, 6.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010330, 30000, 20000, 12012330, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(12010331, 30000, 20000, 12012330, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(12010332, 30000, 20000, 12012330, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(12010333, 30000, 20000, 12012330, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(12010334, 30000, 20000, 12012330, 1.2000000476837158, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(12010335, 30000, 20000, 12012330, 1.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005860, args=(12010850, 0, 12010850, 1, 30600, 0.0), arg_types="IIIIif")
    RunCommonEvent(0, 90005870, args=(12010850, 904650601, 25), arg_types="IiI")
    RunCommonEvent(0, 90005201, args=(12010850, 30000, 20000, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005251, args=(12010850, 20.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010373, 12.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(12010375, 18.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005250, args=(12010377, 12012377, 0.0, 3000), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12010378, 12012377, 2.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(12010379, 12012377, 2.0, 3001), arg_types="IIfi")
    RunCommonEvent(0, 90005211, args=(12010400, 30005, 20005, 12012400, 30.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005300, args=(12010400, 12010400, 0, 3.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12010401, 12010401, 12015995, 3.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12010403, 12010403, 40600, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12010404, 12010404, 40602, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(12010420, 12010420, 12015997, 3.5, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005201, args=(12010420, 30002, 20002, 15.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_12012421()
    RunCommonEvent(0, 90005300, args=(12010421, 12010421, 0, 1.5, 0), arg_types="IIifi")
    RunCommonEvent(
        0,
        90005200,
        args=(12010415, 30005, 20005, 12012410, 1.2999999523162842, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(12010416, 30005, 20005, 12012410, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(12010417, 30005, 20005, 12012410, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(12010418, 30005, 20005, 12012410, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(12010419, 30005, 20005, 12012410, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    Event_12012800()
    Event_12012810()
    Event_12012849()
    Event_12012820()
    Event_12012830()
    Event_12012811()
    Event_12012812()
    RunCommonEvent(
        0,
        90005501,
        args=(12010510, 12010511, 2, 12011510, 12011511, 12011512, 12010512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(12010515, 12010516, 3, 12011515, 12011516, 12011517, 12010517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(12010520, 12010521, 6, 12011520, 12011521, 12011522, 12010522),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005501,
        args=(12010525, 12010526, 9, 12011525, 12011526, 12011527, 12010527),
        arg_types="IIIIIII",
    )
    Event_12010509()
    Event_12012506()
    Event_12012507()
    Event_12012530()
    Event_12012590()
    Event_12012591()
    Event_12012593()
    Event_12012594()
    Event_12012595()
    Event_12012580(0, 12010590, 105, 12012580, 20.0, 100.0)
    Event_12012581(1, 12010591, 105, 12012581, 100.0, 400.0)
    Event_12012582(2, 12010593, 105, 12012583, 100.0, 400.0)
    Event_12012583(3, 12010594, 105, 12012584, 100.0, 400.0)
    Event_12012584(4, 12010595, 105, 12012585, 35.0, 150.0)
    Event_12010700()
    Event_12010701()
    Event_12010702()
    Event_12010705()
    Event_12010706()
    Event_12010707()
    Event_12010708()
    RunCommonEvent(0, 90005750, args=(12011710, 4350, 103940, 400394, 400394, 1034509430, 0), arg_types="IiiIIIi")
    RunCommonEvent(0, 90005726, args=(4805, 4806, 4808, 1035469205, 12010705, 12016700), arg_types="IIIIII")
    RunCommonEvent(0, 90005703, args=(12010705, 4806, 4807, 12019006, 4806, 4805, 4809, 0), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005704, args=(12010705, 4806, 4805, 12019006, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005702, args=(12010705, 4808, 4805, 4809), arg_types="IIII")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_12010519()
    Event_12012050()
    DisableBackread(12010715)
    DisableBackread(12010720)


@RestartOnRest(12010700)
def Event_12010700():
    """Event 12010700"""
    EndIfPlayerNotInOwnWorld()
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010711, radius=3.0)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010712, radius=3.0)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(12012710)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010711, radius=3.0)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010712, radius=3.0)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(12012710)
    Restart()


@RestartOnRest(12010701)
def Event_12010701():
    """Event 12010701"""
    EndIfPlayerNotInOwnWorld()
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010712, radius=3.0)
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(12012711)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010712, radius=3.0)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(12012711)
    Restart()


@RestartOnRest(12010702)
def Event_12010702():
    """Event 12010702"""
    EndIfPlayerNotInOwnWorld()
    IfEntityWithinDistance(OR_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(12012712)
    IfEntityBeyondDistance(AND_1, entity=PLAYER, other_entity=12010713, radius=3.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableFlag(12012712)
    Restart()


@RestartOnRest(12010705)
def Event_12010705():
    """Event 12010705"""
    DisableBackread(12010715)
    GotoIfFlagEnabled(Label.L0, flag=12012715)
    SkipLinesIfFlagDisabled(2, 12019280)
    Kill(12010715)
    End()
    IfFlagEnabled(AND_1, 12019257)
    IfPlayerInOwnWorld(AND_1)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=12010715, radius=53.0)
    IfConditionTrue(MAIN, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(12012715)
    EnableBackread(12010715)
    EnableCharacter(12010715)
    WaitFrames(frames=1)
    ForceAnimation(12010715, 20039, unknown2=1.0)
    End()


@RestartOnRest(12010706)
def Event_12010706():
    """Event 12010706"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12019280)
    IfCharacterDead(OR_1, 12010715)
    IfHealthValueLessThanOrEqual(OR_1, 12010715, value=0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(12019280)
    EnableFlag(12012716)
    End()


@RestartOnRest(12010707)
def Event_12010707():
    """Event 12010707"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12019280)
    EndIfFlagEnabled(12019271)
    DisableFlag(12019270)
    IfFlagEnabled(AND_1, 12012715)
    IfEntityWithinDistance(AND_1, entity=20000, other_entity=12010715, radius=25.0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetCharacterTalkRange(character=12010714, distance=100.0)
    EnableFlag(12019270)
    IfTimeElapsed(OR_1, seconds=30.0)
    IfFlagEnabled(OR_1, 12019280)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfFlagEnabled(1, 12019280)
    SetCharacterTalkRange(character=12010714, distance=17.0)
    End()


@RestartOnRest(12010708)
def Event_12010708():
    """Event 12010708"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(12019280)
    EndIfFlagEnabled(12019273)
    DisableFlag(12019272)
    IfFlagEnabled(MAIN, 12019280)
    Move(
        12010714,
        destination=20000,
        destination_type=CoordEntityType.Character,
        model_point=11,
        copy_draw_parent=20000,
    )
    SetCharacterTalkRange(character=12010714, distance=100.0)
    EnableFlag(12019272)
    IfTimeElapsed(MAIN, seconds=30.0)
    SetCharacterTalkRange(character=12010714, distance=17.0)
    End()


@RestartOnRest(12012050)
def Event_12012050():
    """Event 12012050"""
    EndIfThisEventSlotFlagEnabled()
    AddSpecialEffect(12010340, 90010)
    AddSpecialEffect(12010850, 90010)
    AddSpecialEffect(12010420, 90010)
    AddSpecialEffect(12010245, 5490)
    IfInsideMap(MAIN, game_map=AINSEL_RIVER)
    DisableObject(12015650)


@NeverRestart(12012569)
def Event_12012569(_, flag: uint, obj: uint):
    """Event 12012569"""
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


@RestartOnRest(12012580)
def Event_12012580(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012580"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.699999988079071)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=106,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012581)
def Event_12012581(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012581"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.6000000238418579)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012582)
def Event_12012582(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012582"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=106,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012583)
def Event_12012583(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012583"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012584)
def Event_12012584(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012584"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(MAIN, flag)
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2999999523162842)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012590)
def Event_12012590():
    """Event 12012590"""
    GotoIfFlagDisabled(Label.L0, flag=12010590)
    EndOfAnimation(obj=12011590, animation_id=2)
    EndOfAnimation(obj=12011596, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=12011590, animation_id=1)
    EndOfAnimation(obj=12011596, animation_id=0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12010590)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012590)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12010590)
    ForceAnimation(12011596, 1, wait_for_completion=True, unknown2=1.0)
    Wait(1.0)
    ForceAnimation(12011590, 0, unknown2=1.0)
    End()


@RestartOnRest(12012591)
def Event_12012591():
    """Event 12012591"""
    GotoIfFlagDisabled(Label.L0, flag=12010591)
    EndOfAnimation(obj=12011591, animation_id=2)
    EndOfAnimation(obj=12011592, animation_id=2)
    EndOfAnimation(obj=12011597, animation_id=2)
    EnableMapCollision(collision=12014594)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=12011591, animation_id=1)
    EndOfAnimation(obj=12011592, animation_id=1)
    EndOfAnimation(obj=12011597, animation_id=0)
    DisableMapCollision(collision=12014594)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12010591)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012591)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12010591)
    SetCameraVibration(
        vibration_id=107,
        anchor_entity=12012581,
        decay_start_distance=50.0,
        decay_end_distance=100.0,
        anchor_type=CoordEntityType.Region,
    )
    ForceAnimation(12011597, 1, wait_for_completion=True, unknown2=1.0)
    Wait(1.0)
    ForceAnimation(12011591, 0, unknown2=1.0)
    ForceAnimation(12011592, 0, unknown2=1.0)
    EnableMapCollision(collision=12014594)
    End()


@RestartOnRest(12012593)
def Event_12012593():
    """Event 12012593"""
    GotoIfFlagDisabled(Label.L0, flag=12010593)
    EndOfAnimation(obj=12011593, animation_id=2)
    EndOfAnimation(obj=12011598, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=12011593, animation_id=1)
    EndOfAnimation(obj=12011598, animation_id=0)
    DisableObject(12011699)
    DisableTreasure(obj=12011699)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12010593)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012593)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12010593)
    ForceAnimation(12011598, 1, wait_for_completion=True, unknown2=1.0)
    Wait(1.0)
    ForceAnimation(12011593, 0, wait_for_completion=True, unknown2=1.0)
    EnableObject(12011699)
    EnableTreasure(obj=12011699)
    End()


@RestartOnRest(12012594)
def Event_12012594():
    """Event 12012594"""
    GotoIfFlagDisabled(Label.L0, flag=12010594)
    EndOfAnimation(obj=12011594, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=12011594, animation_id=1)
    DisableMapCollision(collision=12014591)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12010594)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012594)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12010594)
    ForceAnimation(12011594, 0, unknown2=1.0)
    EnableMapCollision(collision=12014591)
    End()


@RestartOnRest(12012595)
def Event_12012595():
    """Event 12012595"""
    GotoIfFlagDisabled(Label.L0, flag=12010595)
    EndOfAnimation(obj=12011595, animation_id=2)
    EndOfAnimation(obj=12011599, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=12011595, animation_id=1)
    EndOfAnimation(obj=12011599, animation_id=0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12010595)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012595)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12010595)
    ForceAnimation(12011599, 1, unknown2=1.0)
    Wait(1.0)
    ForceAnimation(12011595, 0, unknown2=1.0)
    End()


@RestartOnRest(12012421)
def Event_12012421():
    """Event 12012421"""
    GotoIfUnknown_1004_05(Label.L0, character=12010421, unk_8_12=True)
    DisableCharacter(12010421)
    DisableMapCollision(collision=12014421)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012421)
    IfFlagEnabled(AND_1, 12010591)
    IfFlagEnabled(AND_1, 12010593)
    IfFlagEnabled(AND_1, 12010594)
    IfCharacterHasSpecialEffect(AND_4, 12010421, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12010421, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12010421, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, 12010421, 90160)
    IfCharacterHasSpecialEffect(AND_5, 12010421, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12010421, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12010421, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12010421, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, 12010421, 90162)
    IfCharacterHasSpecialEffect(AND_6, 12010421, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12010421, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12010421, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12010421, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, 12010421, 90161)
    IfCharacterHasSpecialEffect(AND_7, 12010421, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12010421, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12010421, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12010421, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, 12010421, 90162)
    IfCharacterHasSpecialEffect(AND_8, 12010421, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12010421, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12010421, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, 12010421, 90160)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12010421, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12010421, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010421, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010421, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010421, unk_8_12=260, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010421, unk_8_12=436, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=12010421, unk_4_8=1)
    EnableCharacter(12010421)
    End()


@RestartOnRest(12012220)
def Event_12012220(_, character: uint):
    """Event 12012220"""
    EndIfThisEventSlotFlagEnabled()
    EnableThisSlotFlag()
    IfCharacterHasSpecialEffect(AND_4, character, 481)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90110)
    IfCharacterDoesNotHaveSpecialEffect(AND_4, character, 90160)
    IfCharacterHasSpecialEffect(AND_5, character, 482)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90120)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_5, character, 90162)
    IfCharacterHasSpecialEffect(AND_6, character, 483)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90140)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90160)
    IfCharacterDoesNotHaveSpecialEffect(AND_6, character, 90161)
    IfCharacterHasSpecialEffect(AND_7, character, 484)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90130)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90161)
    IfCharacterDoesNotHaveSpecialEffect(AND_7, character, 90162)
    IfCharacterHasSpecialEffect(AND_8, character, 487)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90100)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90150)
    IfCharacterDoesNotHaveSpecialEffect(AND_8, character, 90160)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(OR_2, input_condition=AND_4)
    IfConditionTrue(OR_2, input_condition=AND_5)
    IfConditionTrue(OR_2, input_condition=AND_6)
    IfConditionTrue(OR_2, input_condition=AND_7)
    IfConditionTrue(OR_2, input_condition=AND_8)
    IfConditionTrue(MAIN, input_condition=OR_2)
    EnableFlag(12012230)


@RestartOnRest(12012231)
def Event_12012231(_, character: uint, seconds: float):
    """Event 12012231"""
    GotoIfUnknown_1004_05(Label.L0, character=character, unk_8_12=True)
    DisableGravity(character)
    AddSpecialEffect(character, 2900)
    ForceAnimation(character, 30001, loop=True, unknown2=1.0)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfFlagEnabled(OR_2, 12012230)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Unknown_2004_83(character=character, unk_4_8=1)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5080)
    IfCharacterDoesNotHaveSpecialEffect(AND_2, character, 5450)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    EnableGravity(character)
    ForceAnimation(character, 20001, loop=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    End()


@RestartOnRest(12012249)
def Event_12012249():
    """Event 12012249"""
    IfFlagEnabled(OR_10, 12012247)
    IfFlagEnabled(OR_10, 12012249)
    GotoIfConditionFalse(Label.L0, input_condition=OR_10)
    ForceAnimation(12010247, 20003, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12010247)
    IfAttackedWithDamageType(OR_2, attacked_entity=12010247, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12010247, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010247, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010247, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010247, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010247, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagDisabled(AND_2, 12012247)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableNetworkFlag(12012249)
    EnableAI(12010247)


@RestartOnRest(12012239)
def Event_12012239():
    """Event 12012239"""
    IfCharacterInsideRegion(MAIN, character=12010245, region=12012239)
    AddSpecialEffect(12010245, 16318)
    Wait(1.0)
    IfCharacterOutsideRegion(MAIN, character=12010245, region=12012239)
    AddSpecialEffect(12010245, 16319)
    Wait(1.0)
    Restart()


@RestartOnRest(12012240)
def Event_12012240():
    """Event 12012240"""
    EndIfFlagEnabled(12012249)
    EndIfFlagEnabled(12012247)
    IfCharacterInsideRegion(AND_15, character=PLAYER, region=12012247)
    IfFlagDisabled(AND_15, 12012249)
    IfConditionTrue(MAIN, input_condition=AND_15)
    Wait(1.0)
    GotoIfFlagEnabled(Label.L0, flag=12012240)
    MakeEnemyAppear(character=12013240)
    EnableNetworkFlag(12012240)
    Wait(3.0)
    DisableSpawner(entity=12013240)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=12012241)
    MakeEnemyAppear(character=12013241)
    EnableNetworkFlag(12012241)
    Wait(8.0)
    DisableSpawner(entity=12013241)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=12012242)
    MakeEnemyAppear(character=12013242)
    EnableNetworkFlag(12012242)
    Wait(5.0)
    DisableSpawner(entity=12013242)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L3, flag=12012243)
    MakeEnemyAppear(character=12013243)
    EnableNetworkFlag(12012243)
    Wait(5.0)
    DisableSpawner(entity=12013243)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L4, flag=12012244)
    MakeEnemyAppear(character=12013244)
    EnableNetworkFlag(12012244)
    Wait(8.0)
    DisableSpawner(entity=12013244)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L5, flag=12012245)
    MakeEnemyAppear(character=12013245)
    EnableNetworkFlag(12012245)
    Wait(8.0)
    DisableSpawner(entity=12013245)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L6, flag=12012246)
    MakeEnemyAppear(character=12013246)
    EnableNetworkFlag(12012246)
    Wait(3.0)
    DisableSpawner(entity=12013246)
    Goto(Label.L10)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=12012247)
    MakeEnemyAppear(character=12013247)
    EnableAI(12010247)
    ForceAnimation(12010247, 20003, unknown2=1.0)
    EnableNetworkFlag(12012247)
    DisableSpawner(entity=12013247)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@RestartOnRest(12012256)
def Event_12012256():
    """Event 12012256"""
    IfFlagEnabled(AND_15, 12012256)
    IfFlagDisabled(AND_15, 12012257)
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    EndOfAnimation(obj=12011256, animation_id=0)
    ForceAnimation(12010256, 20003, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfFlagEnabled(AND_14, 12012256)
    IfFlagEnabled(AND_14, 12012257)
    GotoIfConditionFalse(Label.L1, input_condition=AND_14)
    EndOfAnimation(obj=12011256, animation_id=2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=12011256, animation_id=2)
    DisableAI(12010256)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012256)
    IfCharacterAlive(AND_1, 12010256)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12012256)
    ForceAnimation(12011256, 3, unknown2=1.0)
    ForceAnimation(12010256, 20003, unknown2=1.0)
    EnableAI(12010256)


@RestartOnRest(12012257)
def Event_12012257():
    """Event 12012257"""
    IfFlagEnabled(OR_15, 12012257)
    EndIfConditionTrue(input_condition=OR_15)
    IfFlagEnabled(AND_1, 12012256)
    IfCharacterDead(OR_1, 12010256)
    IfCharacterOutsideRegion(OR_1, character=PLAYER, region=12012257)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(12012257)
    ForceAnimation(12011256, 1, unknown2=1.0)


@RestartOnRest(12012288)
def Event_12012288(_, character: uint, character_1: uint, region: uint):
    """Event 12012288"""
    IfCharacterAlive(AND_15, character_1)
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    IfThisEventSlotFlagEnabled(AND_1)
    IfPlayerNotInOwnWorld(AND_1)
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    IfCharacterHasSpecialEffect(MAIN, character, 16307)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    SetNest(character_1, region=region)
    DisableAnimations(character)
    WaitFrames(frames=5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 63010, skip_transition=True, unknown2=1.0)
    AddSpecialEffect(character_1, 16316)
    Wait(4.5)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    EnableAI(character_1)


@RestartOnRest(12012301)
def Event_12012301():
    """Event 12012301"""
    GotoIfFlagDisabled(Label.L0, flag=12012301)
    CancelSpecialEffect(12015301, 8081)
    CancelSpecialEffect(12015301, 8082)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(12015301, 8081)
    AddSpecialEffect(12015301, 8082)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=12012301, min_target_count=0)
    CancelSpecialEffect(12015301, 8081)
    CancelSpecialEffect(12015301, 8082)
    EnableNetworkFlag(12012301)


@NeverRestart(12012506)
def Event_12012506():
    """Event 12012506"""
    IfPlayerInOwnWorld(AND_1)
    IfFlagDisabled(AND_1, 12040800)
    IfActionButtonParamActivated(AND_1, action_button_id=9711, entity=12011506)
    IfConditionTrue(MAIN, input_condition=AND_1)
    BanishInvaders(unknown=0)
    EnableFlag(9021)
    SkipLinesIfPlayerNotInOwnWorld(3)
    UnknownCutscene_11(
        cutscene_id=12010000,
        cutscene_flags=0,
        move_to_region=12042506,
        map_base_id=12040000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    SkipLines(2)
    UnknownCutscene_11(
        cutscene_id=12010000,
        cutscene_flags=0,
        move_to_region=12042508,
        map_base_id=12040000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    End()


@NeverRestart(12012507)
def Event_12012507():
    """Event 12012507"""
    EndIfPlayerNotInOwnWorld()
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, 12040800)
    IfActionButtonParamActivated(AND_1, action_button_id=9711, entity=12011506)
    IfConditionTrue(MAIN, input_condition=AND_1)
    BanishPhantoms(unknown=0)
    Wait(1.0)
    EnableFlag(9021)
    UnknownCutscene_11(
        cutscene_id=12010000,
        cutscene_flags=0,
        move_to_region=12042506,
        map_base_id=12040000,
        player_id=10000,
        unknown2=0,
        unknown3=0,
    )
    PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    End()


@NeverRestart(12010509)
def Event_12010509():
    """Event 12010509"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            12010510,
            12010511,
            2,
            12011510,
            12011511,
            12013511,
            12011512,
            12013512,
            12012511,
            12012512,
            12010512,
            12010513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            12010515,
            12010516,
            3,
            12011515,
            12011516,
            12013516,
            12011517,
            12013517,
            12012516,
            12012517,
            12010517,
            12010518,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            12010520,
            12010521,
            6,
            12011520,
            12011521,
            12013521,
            12011522,
            12013522,
            12012521,
            12012522,
            12010522,
            12010523,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005500,
        args=(
            12010525,
            12010526,
            9,
            12011525,
            12011526,
            12013526,
            12011527,
            12013527,
            12012526,
            12012527,
            12010527,
            12010528,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(12010519)
def Event_12010519():
    """Event 12010519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(12010510)
    EnableFlag(12010515)
    EnableFlag(12010520)
    EnableFlag(12010525)


@RestartOnRest(12012530)
def Event_12012530():
    """Event 12012530"""
    RegisterLadder(start_climbing_flag=12010530, stop_climbing_flag=12010531, obj=12011530)
    RegisterLadder(start_climbing_flag=12010532, stop_climbing_flag=12010533, obj=12011532)


@RestartOnRest(12012800)
def Event_12012800():
    """Event 12012800"""
    EndIfFlagEnabled(12010800)
    IfHealthValueLessThanOrEqual(MAIN, 12010800, value=0)
    Kill(12010801)
    Kill(12010802)
    Wait(4.0)
    PlaySoundEffect(12010800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 12010800)
    KillBossAndDisplayBanner(character=12010800, banner_type=BannerType.Unknown)
    EnableFlag(12010800)
    EnableFlag(9109)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61109)


@RestartOnRest(12012810)
def Event_12012810():
    """Event 12012810"""
    GotoIfFlagDisabled(Label.L0, flag=12010800)
    DisableCharacter(12010800)
    DisableAnimations(12010800)
    Kill(12010800)
    DisableCharacter(12010801)
    DisableAnimations(12010801)
    Kill(12010801)
    DisableCharacter(12010802)
    DisableAnimations(12010802)
    Kill(12010802)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(12010801)
    DisableAI(12010802)
    DisableHealthBar(12010801)
    DisableHealthBar(12010802)
    ReferDamageToEntity(12010801, target_entity=12010800)
    ReferDamageToEntity(12010802, target_entity=12010800)
    EnableImmortality(12010801)
    EnableImmortality(12010802)
    DisableGravity(12010800)
    DisableAnimations(12010800)
    DisableCharacter(12010802)
    ForceAnimation(12010801, 30002, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=12010801)
    DisableCharacter(12010800)
    DisableCharacter(12010801)
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012801)
    IfCharacterBackreadEnabled(AND_1, 12010801)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=12010801, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=12010801, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010801, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010801, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010801, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=12010801, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    Wait(0.10000000149011612)
    EnableCharacter(12010800)
    EnableCharacter(12010801)
    ForceAnimation(12010801, 20002, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_10, 12012805)
    IfCharacterInsideRegion(AND_10, character=PLAYER, region=12012800)
    IfConditionTrue(MAIN, input_condition=AND_10)
    ForceAnimation(12010801, 20002, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    EnableNetworkFlag(12010840)
    Wait(2.0)
    EnableNetworkFlag(12012803)
    Wait(0.10000000149011612)
    EnableNetworkFlag(12010801)
    EnableAI(12010801)
    SetNetworkUpdateRate(12010801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(12010800, name=904650000)


@RestartOnRest(12012820)
def Event_12012820():
    """Event 12012820"""
    EndIfFlagEnabled(12010800)
    IfEntityWithinDistance(AND_1, entity=12010802, other_entity=PLAYER, radius=50.0)
    IfCharacterHasSpecialEffect(AND_1, 12010802, 13208)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=4651)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12012830)
def Event_12012830():
    """Event 12012830"""
    EndIfFlagEnabled(12010800)
    DisableNetworkSync()
    IfEntityWithinDistance(AND_1, entity=12010802, other_entity=PLAYER, radius=50.0)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, 12010802, 13208)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=4650)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12012811)
def Event_12012811():
    """Event 12012811"""
    EndIfFlagEnabled(12010800)
    IfCharacterHasSpecialEffect(AND_1, 12010801, 13209)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(12012811)
    EnableFlag(12012802)
    EnableCharacter(12010802)
    DisableAnimations(12010802)
    EnableAI(12010802)
    SetNetworkUpdateRate(12010802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(12010802, destination=12010801, destination_type=CoordEntityType.Character, model_point=100, short_move=True)
    WaitFrames(frames=90)
    DisableCharacter(12010801)
    EnableAnimations(12010802)


@RestartOnRest(12012812)
def Event_12012812():
    """Event 12012812"""
    EndIfFlagEnabled(12010800)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=12012812)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkUpdateRate(12010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(12010801, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(12012849)
def Event_12012849():
    """Event 12012849"""
    RunCommonEvent(0, 9005811, args=(12010800, 12011801, 4, 12010840), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(12010800, 920300, 12012805, 12012806, 12012803, 12012802, 0, 0),
        arg_types="IiIIIIii",
    )
    RunCommonEvent(
        0,
        9005800,
        args=(12010800, 12011800, 12012800, 12012805, 12015800, 10000, 12010801, 12012801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(12010800, 12011800, 12012800, 12012805, 12012806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(12010800, 12011800, 5, 12010801), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(12010800, 920300, 12012805, 12012806, 12012803, 12012802, 0, 0),
        arg_types="IiIIIIii",
    )
