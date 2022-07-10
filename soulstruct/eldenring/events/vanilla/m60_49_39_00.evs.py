"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049390000, obj=1049391950, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76414, 1049391980, 77400, 7, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    RunCommonEvent(0, 9005810, args=(1049390800, 1049390001, 1049390951, 1049391951, 5.0), arg_types="IIIIf")
    RegisterGrace(grace_flag=1049390002, obj=1049391952, unknown=5.0)
    RunCommonEvent(
        0,
        90005100,
        args=(76418, 76416, 1049391982, 77400, 6, 78400, 78401, 78402, 78403, 78404, 78405, 78406, 78407, 78408, 78409),
        arg_types="IIIIIIIIIIIIIII",
    )
    Event_1049392210()
    Event_1049392211(0, 1049391200, 19.0)
    Event_1049392211(1, 1049391201, 12.0)
    Event_1049392211(2, 1049391202, 5.0)
    Event_1049392211(3, 1049391203, 18.0)
    Event_1049392211(4, 1049391204, 11.0)
    Event_1049392211(5, 1049391205, 4.0)
    Event_1049392211(7, 1049391207, 17.0)
    Event_1049392211(8, 1049391208, 10.0)
    Event_1049392211(10, 1049391210, 3.0)
    Event_1049392211(12, 1049391212, 16.0)
    Event_1049392211(13, 1049391213, 9.0)
    Event_1049392211(14, 1049391214, 2.0)
    Event_1049392211(15, 1049391215, 1.0)
    Event_1049392211(16, 1049391216, 14.0)
    Event_1049392211(17, 1049391217, 7.0)
    Event_1049392580(0, start_climbing_flag=49390580, stop_climbing_flag=49390851, obj=1049391580)
    Event_1049392580(1, start_climbing_flag=49390582, stop_climbing_flag=49390853, obj=1049391582)
    Event_1049392300(0, obj=1049391650, flag=1049390200)
    Event_1049392301(1, obj=1049391651, flag=1049390201)
    Event_1049392302(1, obj=1049391601, flag=1049390201)
    Event_1049392303(0, obj=1049391600, flag=1049390200)
    Event_1049392849()
    Event_1049390800()
    Event_1049392810()
    RunCommonEvent(0, 9005811, args=(1049390800, 1049391801, 3, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        90005880,
        args=(1049390850, 1049390855, 1049392850, 1049390850, 1049390850, 60, 49, 39, 0, 1049392855),
        arg_types="IIIIiBBbbI",
    )
    RunCommonEvent(
        0,
        90005881,
        args=(1049390850, 1049390855, 1049392851, 1049392852, 20300, 1049391855, 60, 49, 39, 0, 1049392855),
        arg_types="IIIIiIBBbbI",
    )
    RunCommonEvent(
        0,
        90005882,
        args=(
            1049390850,
            1049390855,
            1049392850,
            1049390850,
            1049392856,
            1049395860,
            1049391850,
            1049390860,
            1049392860,
            903704520,
            -1,
            20004,
        ),
        arg_types="IIIIIIIIIiii",
    )
    RunCommonEvent(0, 90005883, args=(1049390850, 1049390855, 1049391855), arg_types="III")
    RunCommonEvent(0, 90005885, args=(1049390850, 0, 1049392856, 1049392857, 0, 1), arg_types="IiIIii")
    RunCommonEvent(0, 90005251, args=(1049390200, 17.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049390204, 8.0, 0.0, -1), arg_types="Iffi")
    RunCommonEvent(0, 90005251, args=(1049390208, 17.0, 0.0, -1), arg_types="Iffi")
    Event_1049392200(0, character=1049390200, special_effect_id=14809)
    Event_1049392200(1, character=1049390201, special_effect_id=14807)
    Event_1049392200(2, character=1049390202, special_effect_id=14809)
    Event_1049392200(3, character=1049390309, special_effect_id=10113)
    Event_1049392200(4, character=1049390204, special_effect_id=14807)
    Event_1049392200(5, character=1049390205, special_effect_id=14809)
    Event_1049392200(7, character=1049390207, special_effect_id=14808)
    Event_1049392200(9, character=1049390208, special_effect_id=14809)
    RunCommonEvent(0, 90005201, args=(1049390296, 30000, 20000, 20.0, 0.0, 0, 0, 0, 0), arg_types="IiiffIIII")
    Event_1049392350(
        0,
        character=1049390299,
        special_effect=12603,
        region=1049392299,
        region_1=1049392298,
        region_2=1049392297
    )
    RunCommonEvent(0, 90005300, args=(1049390299, 1049390299, 40418, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005300, args=(1049390298, 1049390298, 40416, 0.0, 0), arg_types="IIifi")
    Event_1049392201(0, 1049390308, 10113, 3.0, 5.0)
    Event_1049392201(2, 1049390310, 10113, 6.0, 2.0)
    Event_1049392201(3, 1049390203, 10113, 9.0, 3.0)
    RunCommonEvent(0, 90005250, args=(1049390405, 1049392405, 0.0, -1), arg_types="IIfi")


@RestartOnRest(1049392200)
def Event_1049392200(_, character: uint, special_effect_id: int):
    """Event 1049392200"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1049392201)
def Event_1049392201(_, character: uint, special_effect_id: int, seconds: float, seconds_1: float):
    """Event 1049392201"""
    DisableNetworkSync()
    AddSpecialEffect(character, special_effect_id)
    Wait(seconds_1)
    CancelSpecialEffect(character, special_effect_id)
    Wait(seconds)
    Restart()


@RestartOnRest(1049392210)
def Event_1049392210():
    """Event 1049392210"""
    CreateProjectileOwner(entity=1049390297)


@RestartOnRest(1049392211)
def Event_1049392211(_, source_entity: uint, seconds: float):
    """Event 1049392211"""
    EnableNetworkSync()
    Wait(8.0)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    Wait(seconds)
    IfNewGameCycleEqual(AND_1, completion_count=0)
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_2, completion_count=1)
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_3, completion_count=2)
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_4, completion_count=3)
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_5, completion_count=4)
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_6, completion_count=5)
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleEqual(AND_7, completion_count=6)
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    IfNewGameCycleGreaterThanOrEqual(AND_8, completion_count=7)
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=1049390297,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(1049392300)
def Event_1049392300(_, obj: uint, flag: uint):
    """Event 1049392300"""
    EnableNetworkSync()
    CreateObjectVFX(obj, vfx_id=200, model_point=1502)
    IfFlagEnabled(MAIN, flag)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@NeverRestart(1049392301)
def Event_1049392301(_, obj: uint, flag: uint):
    """Event 1049392301"""
    EnableNetworkSync()
    CreateObjectVFX(obj, vfx_id=200, model_point=1501)
    IfFlagEnabled(MAIN, flag)
    PlaySoundEffect(obj, 1500, sound_type=SoundType.s_SFX)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@NeverRestart(1049392302)
def Event_1049392302(_, obj: uint, flag: uint):
    """Event 1049392302"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9520, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    DisplayDialog(text=30000, anchor_entity=obj)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=100, model_point=806031)
    End()


@NeverRestart(1049392303)
def Event_1049392303(_, obj: uint, flag: uint):
    """Event 1049392303"""
    EnableNetworkSync()
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9520, entity=obj)
    IfConditionTrue(MAIN, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, obj, wait_for_completion=True)
    ForceAnimation(PLAYER, 60010, unknown2=1.0)
    Wait(1.2999999523162842)
    EnableFlag(flag)
    EnableFlag(1050390200)
    DisplayDialog(text=30000, anchor_entity=obj)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj, vfx_id=100, model_point=806031)


@NeverRestart(1049392350)
def Event_1049392350(_, character: uint, special_effect: int, region: uint, region_1: uint, region_2: uint):
    """Event 1049392350"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterHasSpecialEffect(AND_2, character, special_effect)
    IfCharacterAlive(AND_2, character)
    IfConditionTrue(MAIN, input_condition=AND_2)
    DisableFlag(1049392201)
    DisableFlag(1049392202)
    WaitFrames(frames=1)
    EnableRandomFlagInRange(flag_range=(1049392201, 1049392202))
    WaitFrames(frames=1)
    GotoIfCharacterInsideRegion(Label.L1, character=character, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=character, region=region_1)
    GotoIfCharacterInsideRegion(Label.L3, character=character, region=region_2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfFlagEnabled(1, 1049392201)
    SkipLines(3)
    Move(character, destination=region, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)
    Wait(1.0)
    Restart()


@NeverRestart(1049392580)
def Event_1049392580(_, start_climbing_flag: uint, stop_climbing_flag: uint, obj: uint):
    """Event 1049392580"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)


@RestartOnRest(1049390800)
def Event_1049390800():
    """Event 1049390800"""
    EndIfFlagEnabled(1049390800)
    IfHealthValueLessThanOrEqual(AND_1, 1049390800, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 1049390801, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(1049390800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1049390800)
    KillBossAndDisplayBanner(character=1049390800, banner_type=BannerType.DutyFulfilled)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AwardItemLot(1049390800, host_only=True)
    EnableFlag(1049390800)


@RestartOnRest(1049392810)
def Event_1049392810():
    """Event 1049392810"""
    GotoIfFlagDisabled(Label.L0, flag=1049390800)
    DisableCharacter(1049390800)
    DisableAnimations(1049390800)
    Kill(1049390800)
    DisableCharacter(1049390801)
    DisableAnimations(1049390801)
    Kill(1049390801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(1049390800)
    DisableAI(1049390801)
    IfFlagEnabled(AND_2, 1049392805)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1049392800)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagEnabled(AND_2, 1049392805)
    IfConditionTrue(MAIN, input_condition=AND_2)
    EnableAI(1049390800)
    EnableAI(1049390801)
    SetNetworkUpdateRate(1049390800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(1049390801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(1049390800, name=903300560)
    EnableBossHealthBar(1049390801, name=903300561, bar_slot=1)


@RestartOnRest(1049392849)
def Event_1049392849():
    """Event 1049392849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1049390800, 1049391800, 1049392800, 1049392805, 1049395800, 10000, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1049390800, 1049391800, 1049392800, 1049392805, 1049392806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1049390800, 1049391800, 4, 0), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1049390800, 920900, 1049392805, 1049392806, 0, 1049392802, 0, 0),
        arg_types="IiIIIIii",
    )
