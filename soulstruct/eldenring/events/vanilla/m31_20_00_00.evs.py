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
    Event_31202800()
    Event_31202801()
    Event_31202802()
    Event_31202810()
    Event_31202811()
    Event_31092849()
    RunCommonEvent(0, 900005610, args=(31201200, 100, 800, 0), arg_types="IiiI")
    RegisterGrace(grace_flag=31200000, obj=31201950, unknown=5.0)
    RunCommonEvent(
        0,
        90005646,
        args=(31200800, 31202840, 31202841, 31201840, 31202840, 31, 20, 0, 0),
        arg_types="IIIIIBBbb",
    )
    Event_31202550(0, 31200455, 31201555, 5.0, 0.0)
    Event_31202550(2, 31200465, 31201565, 5.0, 0.0)
    Event_31202550(3, 31200470, 31201570, 5.0, 1.0)
    Event_31202550(5, 31200475, 31201575, 5.0, 2.0)
    Event_31202550(1, 31200480, 31201580, 5.0, 3.0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(0, 90005200, args=(31200240, 30000, 20000, 31202240, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(1, 90005200, args=(31200241, 30000, 20000, 31202240, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(2, 90005200, args=(31200242, 30000, 20000, 31202240, 1.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(3, 90005200, args=(31200243, 30000, 20000, 31202240, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(31200230, 31202230, 0.0, 0), arg_types="IIfi")
    RunCommonEvent(1, 90005250, args=(31200231, 31202230, 0.0, 0), arg_types="IIfi")


@RestartOnRest(31202520)
def Event_31202520(_, flag: uint, flag_1: uint, obj: uint):
    """Event 31202520"""
    DisableObjectActivation(obj, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableObjectActivation(obj, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfPlayerInOwnWorld(AND_1)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, flag)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    EnableObjectActivation(obj, obj_act_id=-1)


@RestartOnRest(31202550)
def Event_31202550(_, owner_entity: uint, source_entity: uint, seconds: float, seconds_1: float):
    """Event 31202550"""
    Wait(seconds)
    IfEntityWithinDistance(MAIN, entity=PLAYER, other_entity=source_entity, radius=70.0)
    Wait(seconds_1)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802730070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(31202800)
def Event_31202800():
    """Event 31202800"""
    EndIfFlagEnabled(31200800)
    IfCharacterDead(AND_1, 31200800)
    IfCharacterDead(AND_1, 31200801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    KillBossAndDisplayBanner(character=31200800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31200800)
    EnableFlag(9245)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61245)


@RestartOnRest(31202801)
def Event_31202801():
    """Event 31202801"""
    EndIfFlagEnabled(31200800)
    IfHealthValueLessThanOrEqual(MAIN, 31200800, value=0)
    Wait(4.0)
    PlaySoundEffect(31200800, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31202802)
def Event_31202802():
    """Event 31202802"""
    EndIfFlagEnabled(31200800)
    IfHealthValueLessThanOrEqual(MAIN, 31200801, value=0)
    Wait(4.0)
    PlaySoundEffect(31200801, 888880000, sound_type=SoundType.s_SFX)


@RestartOnRest(31202810)
def Event_31202810():
    """Event 31202810"""
    GotoIfFlagDisabled(Label.L0, flag=31200800)
    DisableCharacter(31200800)
    DisableCharacter(31200801)
    DisableAnimations(31200800)
    DisableAnimations(31200801)
    Kill(31200800)
    Kill(31200801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(31200800)
    DisableAI(31200801)
    ForceAnimation(31200800, 30001, unknown2=1.0)
    IfFlagEnabled(AND_2, 31202805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31202800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(31200800)
    SetNetworkUpdateRate(31200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(1.0)
    EnableBossHealthBar(31200800, name=903800311)
    ForceAnimation(31200800, 20001, unknown2=1.0)
    Wait(5.0)
    EnableAI(31200801)
    SetNetworkUpdateRate(31200801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    IfAttackedWithDamageType(OR_15, attacked_entity=31200801, attacker=0)
    IfTimeElapsed(OR_15, seconds=7.0)
    AwaitConditionTrue(OR_15)
    EnableBossHealthBar(31200801, name=903800312, bar_slot=1)


@RestartOnRest(31202811)
def Event_31202811():
    """Event 31202811"""
    EndIfFlagEnabled(31200800)
    IfCharacterDead(OR_15, 31200800)
    IfCharacterDead(OR_15, 31200801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31202842)


@RestartOnRest(31092849)
def Event_31092849():
    """Event 31092849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31200800, 31201800, 31202800, 31202805, 31205800, 10010, 0, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31200800, 31201800, 31202800, 31202805, 31202806, 10010), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31200800, 31201800, 3, 0), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(31200800, 931000, 31202805, 31202806, 0, 31202842, 0, 0), arg_types="IiIIIIii")
