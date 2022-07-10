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
    RunCommonEvent(
        0,
        90005646,
        args=(30010800, 30012840, 30012841, 30011840, 30012840, 30, 1, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RegisterGrace(grace_flag=73001, obj=30011950, unknown=5.0)
    Event_30012800()
    Event_30012810()
    Event_30012849()
    Event_30012811()
    RunCommonEvent(0, 90005211, args=(30010810, 30010, 20010, 30012800, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010811, 30010, 20010, 30012800, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010812, 30010, 20010, 30012800, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010813, 30010, 20010, 30012800, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005920, args=(30010520, 30011520, 30013520), arg_types="III")
    RunCommonEvent(0, 90005650, args=(30010540, 30011540, 30011541, 30013541, 27115), arg_types="IIIIi")
    RunCommonEvent(0, 90005651, args=(30010540, 30011540), arg_types="II")
    Event_30012505()
    Event_30012506()
    RunCommonEvent(
        0,
        90005670,
        args=(30012500, 30012510, 30012511, 30011500, 30012500, 30012502, 0),
        arg_types="IIIIIII",
    )
    Event_30012520()
    Event_30012580()
    Event_30010790(0, 30011520, 30010800)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(
        0,
        90005211,
        args=(30010200, 30004, 20004, 30012200, 0.0, 0.800000011920929, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30010201, 30002, 20002, 30012201, 1.0, 0.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010203, 30002, 20002, 30012203, 1.0, 2.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30010204, 30000, 20000, 30012204, 1.0, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30010205, 30000, 20000, 30012205, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010207, 30009, 20009, 30012207, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010209, 30009, 20009, 30012209, 1.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010321, 30000, 20000, 30012315, 5.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30010301, 30000, 20000, 30012312, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005200, args=(30010302, 30000, 20000, 30012312, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(30010304, 30000, 20000, 30012312, 0.6000000238418579, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(
        0,
        90005200,
        args=(30010305, 30000, 20000, 30012312, 0.4000000059604645, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005211, args=(30010303, 30000, 20000, 30012322, 5.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30010306, 30000, 20000, 30012322, 5.0, 0.30000001192092896, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30010312, 30000, 20000, 30012322, 5.0, 0.8999999761581421, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(0, 90005211, args=(30010308, 30000, 20000, 30012322, 5.0, 1.5, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010307, 30000, 20000, 30012322, 5.0, 2.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(30010309, 30000, 20000, 30012322, 5.0, 3.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(
        0,
        90005211,
        args=(30010310, 30000, 20000, 30012322, 5.0, 3.5999999046325684, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(30010311, 30000, 20000, 30012322, 5.0, 3.9000000953674316, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(30012330)
def Event_30012330(_, character: uint, character_1: uint):
    """Event 30012330"""
    IfCharacterType(AND_15, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_15, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_15)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30012301)
    IfConditionTrue(AND_5, input_condition=AND_1)
    IfCharacterAlive(AND_5, character)
    IfConditionTrue(MAIN, input_condition=AND_5)
    MakeEnemyAppear(character=character_1)
    Restart()


@RestartOnRest(30012910)
def Event_30012910(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 30012910"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfCharacterInsideRegion(OR_3, character=PLAYER, region=region)
    IfEntityWithinDistance(OR_3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(AND_1, input_condition=OR_3)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=character, attacker=0)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_2, character=character, unk_8_12=260, unk_12_16=1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    EnableCharacter(character)
    EnableAnimations(character)
    SkipLinesIfValueEqual(1, left=animation_id, right=-1)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.30000001192092896)
    Move(30010800, destination=30012901, destination_type=CoordEntityType.Region, copy_draw_parent=30010800)
    EnableAI(character)


@NeverRestart(30012500)
def Event_30012500():
    """Event 30012500"""
    GotoIfFlagEnabled(Label.L0, flag=30010500)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterType(OR_1, PLAYER, character_type=CharacterType.Unknown17)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30012500)
    IfConditionTrue(MAIN, input_condition=AND_1)
    ForceAnimation(30011500, 12, wait_for_completion=True, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    IfAllPlayersOutsideRegion(AND_1, region=30012500)
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    EnableFlag(30010500)
    ForceAnimation(30011500, 20, wait_for_completion=True, unknown2=1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(30010500)
    ForceAnimation(30011500, 21, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(30012505)
def Event_30012505():
    """Event 30012505"""
    IfFlagEnabled(AND_1, 30012510)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30012502)
    IfCharacterHasSpecialEffect(AND_1, PLAYER, 4195)
    IfConditionTrue(MAIN, input_condition=AND_1)
    MoveObjectToCharacter(30011501, character=PLAYER, model_point=93)
    WaitFrames(frames=1)
    SkipLinesIfFlagDisabled(1, 50)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301200,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301220,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301230,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301240,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301250,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301260,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    CreateHazard(
        obj_flag=30013501,
        obj=30011501,
        model_point=100,
        behavior_param_id=801301270,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.10000000149011612,
        repetition_time=0.0,
    )
    WaitFrames(frames=1)
    RemoveObjectFlag(obj_flag=30013501)
    Wait(0.5)
    Restart()


@NeverRestart(30012506)
def Event_30012506():
    """Event 30012506"""
    IfFlagEnabled(AND_1, 30012510)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=30012501)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4195)
    Wait(0.5)
    Restart()


@UnknownRestart(30012520)
def Event_30012520():
    """Event 30012520"""
    DisableFlag(30010500)
    End()


@NeverRestart(30012580)
def Event_30012580():
    """Event 30012580"""
    RegisterLadder(start_climbing_flag=30010580, stop_climbing_flag=30010581, obj=30011580)


@RestartOnRest(30010790)
def Event_30010790(_, obj: uint, flag: uint):
    """Event 30010790"""
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


@RestartOnRest(30012800)
def Event_30012800():
    """Event 30012800"""
    EndIfFlagEnabled(30010800)
    IfHealthValueLessThanOrEqual(MAIN, 30010800, value=0)
    Kill(30015800)
    Wait(4.0)
    PlaySoundEffect(30010800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 30010800)
    KillBossAndDisplayBanner(character=30010800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(30010800)
    EnableFlag(9201)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61201)


@RestartOnRest(30012810)
def Event_30012810():
    """Event 30012810"""
    GotoIfFlagDisabled(Label.L0, flag=30010800)
    DisableCharacter(30015800)
    DisableAnimations(30015800)
    Kill(30015800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(30010800)
    IfFlagEnabled(AND_2, 30012805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=30012800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(30010800)
    SetNetworkUpdateRate(30010800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(30010800, name=904260301)


@RestartOnRest(30012811)
def Event_30012811():
    """Event 30012811"""
    EndIfFlagEnabled(30010800)
    IfHealthLessThanOrEqual(AND_1, 30010800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(30012802)


@RestartOnRest(30012849)
def Event_30012849():
    """Event 30012849"""
    RunCommonEvent(
        0,
        9005800,
        args=(30010800, 30011800, 30012800, 30012805, 30015800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(30010800, 30011800, 30012800, 30012805, 30012806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(30010800, 30011800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(30010800, 930000, 30012805, 30012806, 0, 30012802, 0, 0), arg_types="IiIIIIii")
