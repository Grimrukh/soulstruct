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
    RegisterGrace(grace_flag=76305, obj=1041521951, unknown=5.0)
    Event_1041522320(0, character=1041520800, name=904510600, unk_4_8=28)
    RunCommonEvent(0, 90005860, args=(1041520800, 0, 1041520800, 1, 30300, 0.0), arg_types="IIIIif")
    Event_1041522270(0, owner_entity=1041520270, region=1041522270, source_entity=1041522271)
    Event_1041522270(1, owner_entity=1041520270, region=1041522270, source_entity=1041522271)
    Event_1041522270(2, owner_entity=1041520280, region=1041522280, source_entity=1041522281)
    Event_1041522270(3, owner_entity=1041520280, region=1041522280, source_entity=1041522281)
    RunCommonEvent(
        0,
        90005633,
        args=(580320, 580020, 1041520300, 30015, 20015, 1041521300, 1041521310),
        arg_types="IIIiiII",
    )
    RunCommonEvent(0, 90005631, args=(1041521400, 61030), arg_types="Ii")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1041522300(0, 1041520800)


@RestartOnRest(1041522270)
def Event_1041522270(_, owner_entity: uint, region: uint, source_entity: uint):
    """Event 1041522270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=owner_entity)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, 50)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 51)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 52)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 53)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 54)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 55)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 56)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(1, 57)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=900,
        behavior_id=802103070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@RestartOnRest(1041522300)
def Event_1041522300(_, character: uint):
    """Event 1041522300"""
    GotoIfFlagEnabled(Label.L0, flag=1041520800)
    GotoIfFlagEnabled(Label.L0, flag=1037510800)
    GotoIfFlagEnabled(Label.L1, flag=1041522810)
    DisableCharacter(character)
    DisableAnimations(character)
    IfCharacterHuman(AND_1, PLAYER)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=1041522800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(1041520820)
    EnableFlag(1041522810)
    Unknown_2004_73(entity=character, unk_4_8=1)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20019, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@NeverRestart(1041522320)
def Event_1041522320(_, character: uint, name: int, unk_4_8: uint):
    """Event 1041522320"""
    DisableNetworkSync()
    DisableHealthBar(character)
    IfHasAIStatus(AND_1, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_1, unk_4_8=unk_4_8, unk_8_9=True)
    IfFlagDisabled(AND_1, 9000)
    IfConditionTrue(MAIN, input_condition=AND_1)
    GotoIfFlagDisabled(Label.L0, flag=9290)
    GotoIfFlagDisabled(Label.L1, flag=9291)
    Wait(5.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(9290)
    SkipLinesIfFlagDisabled(1, 1037510810)
    AddSpecialEffect(character, 4401)
    Wait(1.0)
    EnableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_2, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_2, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_2, input_condition=AND_2)
    IfCharacterDead(OR_2, character)
    IfFlagEnabled(OR_2, 9000)
    IfConditionTrue(MAIN, input_condition=OR_2)
    IfCharacterDead(OR_3, character)
    SkipLinesIfConditionFalse(2, OR_3)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9290)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(9291)
    SkipLinesIfFlagDisabled(1, 1037510810)
    AddSpecialEffect(character, 4401)
    Wait(1.0)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Unknown8192)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Unknown102)
    IfHasAIStatus(AND_12, character, ai_status=AIStatusType.Battle)
    IfUnknownCondition_33(AND_12, unk_4_8=unk_4_8, unk_8_9=True)
    IfConditionFalse(OR_12, input_condition=AND_12)
    IfCharacterDead(OR_12, character)
    IfFlagEnabled(OR_12, 9000)
    IfConditionTrue(MAIN, input_condition=OR_12)
    IfCharacterDead(OR_13, character)
    SkipLinesIfConditionFalse(2, OR_13)
    Wait(3.0)
    SkipLines(2)
    SkipLinesIfFlagEnabled(1, 9000)
    Wait(1.0)
    DisableBossHealthBar(character, name=name, bar_slot=1)
    SkipLinesIfPlayerNotInOwnWorld(2)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Normal)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Unknown102)
    DisableFlag(9291)
    Restart()
