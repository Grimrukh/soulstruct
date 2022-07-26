"""
South Caelid (NW) (SE)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_49_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterLadder(start_climbing_flag=49381500, stop_climbing_flag=49381501, asset=1049381500)
    RegisterLadder(start_climbing_flag=49381502, stop_climbing_flag=49381503, asset=1049381502)
    RegisterLadder(start_climbing_flag=49381504, stop_climbing_flag=49381505, asset=1049381504)
    CommonFunc_9005810(
        0,
        flag=1049380800,
        grace_flag=1049380000,
        character=Characters.TalkDummy1,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    RegisterGrace(grace_flag=1049380001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76413,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=5,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    CommonFunc_90005511(
        0,
        flag=1049380560,
        asset=Assets.AEG110_421_2000,
        obj_act_id=1049383560,
        obj_act_id_1=99020,
        left=0,
    )
    CommonFunc_90005512(0, flag=1049380560, region=1049382560, region_1=1049382561)
    CommonFunc_90005780(
        0,
        flag=1049380800,
        summon_flag=1049382160,
        dismissal_flag=1049382161,
        character=Characters.Human1,
        sign_type=20,
        region=1049382701,
        right=0,
        unknown=1,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=1049380800, flag_1=1049382160, flag_2=1049382161, character=Characters.Human1)
    CommonFunc_90005783(
        0,
        flag=1049380800,
        flag_1=1049382160,
        flag_2=1049382161,
        character=Characters.Human1,
        other_entity=1049382700,
        region=1049382400,
        left=0,
    )
    CommonFunc_90005300(0, flag=1049380290, character=Characters.Scarab, item_lot=40404, seconds=0.0, left=0)
    Event_1049382210()
    Event_1049382211(0, source_entity=Assets.AEG099_046_9035, seconds=6.0)
    Event_1049382211(1, source_entity=Assets.AEG099_046_9036, seconds=12.0)
    Event_1049382211(2, source_entity=Assets.AEG099_046_9037, seconds=3.0)
    Event_1049382211(3, source_entity=Assets.AEG099_046_9038, seconds=2.0)
    Event_1049382211(4, source_entity=Assets.AEG099_046_9039, seconds=10.0)
    Event_1049382211(5, source_entity=Assets.AEG099_046_9040, seconds=14.0)
    Event_1049382211(6, source_entity=Assets.AEG099_046_9041, seconds=8.0)
    Event_1049382211(7, source_entity=Assets.AEG099_046_9042, seconds=5.0)
    Event_1049382211(8, source_entity=Assets.AEG099_046_9043, seconds=4.0)
    CommonFunc_90005250(0, character=Characters.DeathRiteBird, region=1049382399, seconds=0.0, animation_id=-1)
    Event_1049382200(0, character=Characters.RayaLucariaScholar0, special_effect_id=14807)
    Event_1049382200(1, character=Characters.RayaLucariaScholar1, special_effect_id=14807)
    Event_1049382200(2, character=Characters.RayaLucariaScholar2, special_effect_id=14807)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar0, region=1049382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar1, region=1049382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.RayaLucariaScholar2, region=1049382200, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.CleanrotKnight2,
        animation_id=30002,
        animation_id_1=20002,
        region=1049382311,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.CleanrotKnight0, region=1049382311, seconds=82.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CleanrotKnight1, region=1049382311, seconds=22.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CleanrotKnight3, region=1049382311, seconds=115.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.CleanrotKnight4, region=1049382311, seconds=50.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commander, radius=35.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005870(0, character=Characters.Commander, name=903050600, npc_threat_level=11)
    CommonFunc_90005860(
        0,
        flag=1049380800,
        left=0,
        character=Characters.Commander,
        left_1=1,
        item_lot=30405,
        seconds=0.0,
    )
    CommonFunc_90005872(0, character=Characters.Commander, npc_threat_level=11, right=0)
    Event_1049382820(
        0,
        character=Characters.Commander,
        character_1=1049385800,
        special_effect=11130,
        animation_id=20015,
    )
    Event_1049382824(
        0,
        character=Characters.Commander,
        character_1=1049385801,
        special_effect=11131,
        animation_id=20015,
    )
    Event_1049382821(0, character=1049380800, character_1=1049385800, character_2=1049385801, animation_id=20016)


@RestartOnRest(1049382200)
def Event_1049382200(_, character: uint, special_effect_id: int):
    """Event 1049382200"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(1049382210)
def Event_1049382210():
    """Event 1049382210"""
    CreateProjectileOwner(entity=Characters.Human0)


@RestartOnRest(1049382211)
def Event_1049382211(_, source_entity: uint, seconds: float):
    """Event 1049382211"""
    EnableNetworkSync()
    Wait(8.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=source_entity, radius=70.0))
    
    Wait(seconds)
    AND_1.Add(NewGameCycleEqual(completion_count=0))
    SkipLinesIfConditionFalse(2, AND_1)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700000,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_2.Add(NewGameCycleEqual(completion_count=1))
    SkipLinesIfConditionFalse(2, AND_2)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_3.Add(NewGameCycleEqual(completion_count=2))
    SkipLinesIfConditionFalse(2, AND_3)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700020,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_4.Add(NewGameCycleEqual(completion_count=3))
    SkipLinesIfConditionFalse(2, AND_4)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700030,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_5.Add(NewGameCycleEqual(completion_count=4))
    SkipLinesIfConditionFalse(2, AND_5)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700040,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_6.Add(NewGameCycleEqual(completion_count=5))
    SkipLinesIfConditionFalse(2, AND_6)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700050,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_7.Add(NewGameCycleEqual(completion_count=6))
    SkipLinesIfConditionFalse(2, AND_7)
    ShootProjectile(
        owner_entity=Characters.Human0,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=802700060,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L0)
    AND_8.Add(NewGameCycleGreaterThanOrEqual(completion_count=7))
    SkipLinesIfConditionFalse(2, AND_8)
    ShootProjectile(
        owner_entity=Characters.Human0,
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


@ContinueOnRest(1049382399)
def Event_1049382399(_, character: uint, destination: uint, special_effect: int):
    """Event 1049382399"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_2.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    ForceAnimation(character, 20025, loop=True)
    ReplanAI(character)


@RestartOnRest(1049382820)
def Event_1049382820(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1049382820"""
    GotoIfFlagDisabled(Label.L0, flag=1049380800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1049382300)
    DisableAI(character_1)
    DisableCharacter(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=-1, command_slot=0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    if FlagDisabled(1049382300):
        EnableFlag(1049382300)
        ForceAnimation(character_1, animation_id, wait_for_completion=True)


@RestartOnRest(1049382821)
def Event_1049382821(_, character: uint, character_1: uint, character_2: uint, animation_id: int):
    """Event 1049382821"""
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterDead(character))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character_1, animation_id, skip_transition=True)
    ForceAnimation(character_2, animation_id, skip_transition=True)
    Wait(3.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    Kill(character_2)
    End()


@RestartOnRest(1049382824)
def Event_1049382824(_, character: uint, character_1: uint, special_effect: int, animation_id: int):
    """Event 1049382824"""
    GotoIfFlagDisabled(Label.L0, flag=1049380800)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1049382301)
    DisableAI(character_1)
    DisableCharacter(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=-1, command_slot=0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    if FlagDisabled(1049382301):
        EnableFlag(1049382301)
        ForceAnimation(character_1, animation_id, wait_for_completion=True)
