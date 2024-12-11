"""
Midna's Manse

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_9005810(
        0,
        flag=28000800,
        grace_flag=28000000,
        character=28000950,
        asset=28001950,
        enemy_block_distance=5.0,
    )
    RegisterGrace(grace_flag=28000001, asset=28001951)
    RegisterGrace(grace_flag=28000002, asset=28001952)
    RegisterGrace(grace_flag=28000003, asset=28001953)
    Event_28000800()
    Event_28002810()
    Event_28002811()
    Event_28002849()
    Event_28002814()
    Event_28002816()
    Event_28002820()
    Event_28002821()
    Event_28002822()
    Event_28002823()
    CommonFunc_90005200(
        0,
        character=28000310,
        animation_id=30000,
        animation_id_1=20000,
        region=28002310,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005260(0, character=28000200, region=28002203, radius=9.0, seconds=0.0, animation_id=0)
    CommonFunc_90005260(0, character=28000201, region=28002203, radius=9.0, seconds=0.0, animation_id=0)
    CommonFunc_90005260(0, character=28000202, region=28002203, radius=9.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000203, region=28002203, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=28000205, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005221(0, character=28000204, animation_id=30001, animation_id_1=20001, seconds=0.0, left=0)
    CommonFunc_90005221(0, character=28000207, animation_id=30000, animation_id_1=20000, seconds=0.0, left=0)
    Event_28002280(1, character=28000281, region=28002289, seconds=1.2000000476837158, animation_id=0, seconds_1=1.0)
    Event_28002280(2, character=28000282, region=28002289, seconds=0.699999988079071, animation_id=0, seconds_1=3.0)
    Event_28002280(3, character=28000283, region=28002289, seconds=0.5, animation_id=0, seconds_1=10.0)
    Event_28002280(4, character=28000284, region=28002289, seconds=1.0, animation_id=0, seconds_1=10.0)
    Event_28002280(5, character=28000285, region=28002289, seconds=1.7000000476837158, animation_id=0, seconds_1=7.0)
    Event_28002280(6, character=28000286, region=28002289, seconds=1.2999999523162842, animation_id=0, seconds_1=1.5)
    Event_28002280(7, character=28000287, region=28002289, seconds=1.0, animation_id=0, seconds_1=0.0)
    Event_28002280(9, character=28000380, region=28002289, seconds=0.5, animation_id=0, seconds_1=4.0)
    CommonFunc_90005250(0, character=28000210, region=28002210, seconds=1.399999976158142, animation_id=0)
    CommonFunc_90005250(0, character=28000211, region=28002210, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000212, region=28002210, seconds=0.699999988079071, animation_id=0)
    CommonFunc_90005250(0, character=28000216, region=28002216, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000217, region=28002216, seconds=0.699999988079071, animation_id=0)
    CommonFunc_90005250(0, character=28000215, region=28002215, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000214, region=28002214, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=28000229, region=28002229, radius=5.0, seconds=0.0, animation_id=3010)
    Event_28002229()
    CommonFunc_90005250(0, character=28000227, region=28002227, seconds=0.0, animation_id=3001)
    CommonFunc_90005200(
        0,
        character=28000311,
        animation_id=30000,
        animation_id_1=20000,
        region=28002311,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=28000220, region=28002220, seconds=0.0, animation_id=3003)
    CommonFunc_90005211(
        0,
        character=28000221,
        animation_id=30000,
        animation_id_1=20000,
        region=28002221,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=28000222,
        animation_id=30000,
        animation_id_1=20000,
        region=28002222,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=28000223,
        animation_id=30000,
        animation_id_1=20000,
        region=28002222,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=28000224, region=28002222, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000350, region=28002350, seconds=1.0, animation_id=0)
    CommonFunc_90005250(0, character=28000351, region=28002351, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000354, region=28002354, seconds=0.0, animation_id=0)
    Event_28002355(0, character=28000355, radius=6.0, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000390, region=28002390, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000358, region=28002358, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000360, region=28002360, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000361, region=28002361, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=28000362, region=28002360, seconds=0.0, animation_id=0)
    Event_28002580()
    CommonFunc_90005520(0, flag=28000589, asset=28001588, start_climbing_flag=28000588, stop_climbing_flag=28000859)
    Event_28002498()
    CommonFunc_90005525(0, flag=28000610, asset=28001610)
    CommonFunc_90005525(1, flag=28000611, asset=28001611)
    CommonFunc_90005540(
        0,
        flag=28008500,
        asset=28001500,
        asset_1=28001501,
        obj_act_id=28003500,
        obj_act_id_1=464009,
        animation_id=12,
        animation_id_1=20,
    )
    CommonFunc_90005540(
        1,
        flag=28008502,
        asset=28001502,
        asset_1=28001503,
        obj_act_id=28003502,
        obj_act_id_1=464009,
        animation_id=12,
        animation_id_1=20,
    )
    CommonFunc_90005515(0, flag=28008541, anchor_entity=28001541)
    Event_28000700(0, flag=28000800, character=28000801, character_1=28000800, distance=115.0)
    Event_28000701(
        0,
        flag=28000800,
        flag_1=28002700,
        seconds=2.0,
        flag_2=28002706,
        flag_3=28002707,
        seconds_1=2.5,
        flag_4=28002705,
        flag_5=28002701,
        region=28002801,
        flag_6=28002709,
        flag_7=28002708,
    )
    Event_28000702(0, flag=28000800, flag_1=28009210, region=28002700, flag_2=28002702)
    Event_28000702(1, flag=28000800, flag_1=28009211, region=28002701, flag_2=28002703)
    Event_28000702(2, flag=28000800, flag_1=28009212, region=28002702, flag_2=28002704)
    CommonFunc_90005706(0, character=28000700, animation_id=30020, left=0)
    CommonFunc_90005706(0, character=28000701, animation_id=30021, left=0)


@ContinueOnRest(28002580)
def Event_28002580():
    """Event 28002580"""
    RegisterLadder(start_climbing_flag=28000580, stop_climbing_flag=28000581, asset=28001580)
    RegisterLadder(start_climbing_flag=28000582, stop_climbing_flag=28000583, asset=28001582)
    RegisterLadder(start_climbing_flag=28000584, stop_climbing_flag=28000585, asset=28001584)
    RegisterLadder(start_climbing_flag=28000586, stop_climbing_flag=28000587, asset=28001586)


@ContinueOnRest(28002229)
def Event_28002229():
    """Event 28002229"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=28002228))
    
    MAIN.Await(AND_1)
    
    EnableThisNetworkSlotFlag()

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(28000229, patrol_information_id=28002399)


@RestartOnRest(28002280)
def Event_28002280(_, character: uint, region: Region | int, seconds: float, animation_id: int, seconds_1: float):
    """Event 28002280"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AddSpecialEffect(character, 8082)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    Wait(seconds_1)
    RemoveSpecialEffect(character, 8082)


@RestartOnRest(28002355)
def Event_28002355(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 28002355"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    OR_3.Add(FlagEnabled(28008500))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(28002498)
def Event_28002498():
    """Event 28002498"""
    GotoIfFlagEnabled(Label.L0, flag=28000589)
    AddNavmeshFaceFlag(navmesh_id=28002498, navmesh_type=NavmeshFlag.Disable)
    
    MAIN.Await(FlagEnabled(28000589))

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveNavmeshFaceFlag(navmesh_id=28002498, navmesh_type=NavmeshFlag.Disable)
    End()


@RestartOnRest(28000800)
def Event_28000800():
    """Event 28000800"""
    if FlagEnabled(28000800):
        return
    
    MAIN.Await(HealthValue(28000800) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(28000800, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(28000800))
    
    KillBossAndDisplayBanner(character=28000800, banner_type=BannerType.LegendFelled)
    EnableFlag(28000800)
    EnableFlag(9156)
    if PlayerInOwnWorld():
        EnableFlag(61156)


@RestartOnRest(28002810)
def Event_28002810():
    """Event 28002810"""
    GotoIfFlagDisabled(Label.L0, flag=28000800)
    DisableCharacter(28005800)
    DisableAnimations(28005800)
    Kill(28005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(28005800)
    DisableGravity(28000800)
    DisableAnimations(28000800)
    DisableCharacter(28000800)
    SetAIParamID(28000801, ai_param_id=500000003)
    DisableAI(28000801)
    EnableInvincibility(28000801)
    ForceAnimation(28000801, 30000)
    GotoIfFlagEnabled(Label.L1, flag=28000801)
    OR_1.Add(FlagEnabled(28000814))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(28002805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=28002800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(28002700)
    EnableAI(28000801)
    ForceAnimation(28000801, 20000, wait_for_completion=True)
    DisableInvincibility(28000801)
    ForceAnimation(28000801, 20)
    EnableFlag(28002708)
    EnableNetworkFlag(28000801)


@RestartOnRest(28002811)
def Event_28002811():
    """Event 28002811"""
    if FlagEnabled(28000800):
        return
    AddSpecialEffect(28000100, 9531)
    
    MAIN.Await(HealthValue(28000801) < 1)
    
    EnableCharacter(28000800)
    DisableAnimations(28000801)
    Wait(5.0)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=28000000,
            cutscene_flags=0,
            move_to_region=28002810,
            map_id=28000000,
            player_id=10000,
            unk_20_24=28000000,
            unk_24_25=False,
        )
    else:
        PlayCutscene(28000000, cutscene_flags=0, player_id=10000)
    WaitRealFrames(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=8.260000228881836, y_angle=7.789999961853027)
    EnableFlag(28002801)
    EnableFlag(28002802)
    DisableCharacter(28000801)
    Move(28000800, destination=28002812, destination_type=CoordEntityType.Region, copy_draw_parent=28000801)
    EnableGravity(28000800)
    EnableAnimations(28000800)
    WaitRealFrames(frames=1)
    ForceAnimation(28000800, 20000)
    EnableAI(28000800)
    SetNetworkUpdateRate(28000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(28000800, name=905051000)
    AddSpecialEffect(28000100, 9532)


@RestartOnRest(28002814)
def Event_28002814():
    """Event 28002814"""
    if FlagEnabled(28000800):
        return
    if FlagEnabled(28000801):
        return
    DisableFlag(28000814)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=28002814))
    
    MAIN.Await(OR_1)
    
    EnableFlag(28000814)


@RestartOnRest(28002815)
def Event_28002815(_, flag: Flag | int, asset: uint, vfx_id: int):
    """Event 28002815"""
    DisableNetworkSync()
    DisableAsset(asset)
    DeleteAssetVFX(asset)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(flag))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(flag))
    OR_3.Add(FlagEnabled(28000814))
    OR_3.Add(FlagEnabled(28000801))
    AND_3.Add(OR_3)
    AND_3.Add(FlagDisabled(flag))
    OR_4.Add(Invasion())
    OR_4.Add(InvasionPending())
    AND_4.Add(OR_4)
    AND_4.Add(FlagEnabled(flag))
    AND_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_4.Add(not AND_7)
    OR_5.Add(Invasion())
    OR_5.Add(InvasionPending())
    AND_5.Add(OR_5)
    AND_5.Add(FlagEnabled(flag))
    AND_5.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_5.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    OR_8.Add(AND_1)
    OR_8.Add(AND_2)
    OR_8.Add(AND_3)
    OR_8.Add(AND_4)
    OR_8.Add(AND_5)
    
    MAIN.Await(OR_8)
    
    EnableAsset(asset)
    DeleteAssetVFX(asset)
    CreateAssetVFX(asset, dummy_id=101, vfx_id=vfx_id)
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader2))
    OR_11.Add(CharacterIsType(PLAYER, character_type=CharacterType.Invader3))
    AND_11.Add(OR_11)
    AND_11.Add(FlagDisabled(flag))
    OR_12.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_12.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    AND_12.Add(OR_12)
    AND_12.Add(FlagDisabled(flag))
    OR_13.Add(FlagEnabled(28000814))
    OR_13.Add(FlagEnabled(28000801))
    AND_13.Add(OR_13)
    AND_13.Add(FlagDisabled(flag))
    OR_14.Add(Invasion())
    OR_14.Add(InvasionPending())
    AND_14.Add(OR_14)
    AND_14.Add(FlagEnabled(flag))
    OR_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_14.Add(not OR_7)
    OR_15.Add(Invasion())
    OR_15.Add(InvasionPending())
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag))
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_15.Add(EntityBeyondDistance(entity=PLAYER, other_entity=asset, radius=1.0))
    AND_9.Add(not AND_11)
    AND_9.Add(not AND_12)
    AND_9.Add(not AND_13)
    AND_9.Add(not AND_14)
    AND_9.Add(not AND_15)
    
    MAIN.Await(AND_9)
    
    Restart()


@RestartOnRest(28002816)
def Event_28002816():
    """Event 28002816"""
    if FlagEnabled(28000800):
        return
    
    MAIN.Await(FlagEnabled(28002709))
    
    SetAIParamID(28000801, ai_param_id=50500000)
    EnableAI(28000801)


@RestartOnRest(28002820)
def Event_28002820():
    """Event 28002820"""
    if FlagEnabled(28000800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(28000800, 20010269))
    
    EnableFlag(28002820)


@RestartOnRest(28002821)
def Event_28002821():
    """Event 28002821"""
    DisableNetworkSync()
    if FlagEnabled(28000800):
        return
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=28002821))
    AND_1.Add(FlagEnabled(28002820))
    
    MAIN.Await(AND_1)
    
    SetWeather(weather=Weather.WindyPuffyClouds, duration=-1.0, immediate_change=True)
    DeleteAssetVFX(28001821)
    CreateAssetVFX(28001821, dummy_id=200, vfx_id=828710)
    
    MAIN.Await(FlagEnabled(28000800))
    
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    DeleteAssetVFX(28001821)


@RestartOnRest(28002822)
def Event_28002822():
    """Event 28002822"""
    if FlagEnabled(28000800):
        return
    AND_1.Add(FlagEnabled(28002700))
    OR_1.Add(FlagEnabled(28002701))
    OR_2.Add(AttackedWithDamageType(attacked_entity=28000801))
    OR_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SkipLinesIfLastConditionResultFalse(1, input_condition=OR_2)
    EnableFlag(28002705)
    EnableFlag(28002801)


@RestartOnRest(28002823)
def Event_28002823():
    """Event 28002823"""
    if FlagEnabled(28000800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(28000800, 20010298))
    
    EnableFlag(28002823)


@RestartOnRest(28002830)
def Event_28002830(
    _,
    flag: Flag | int,
    bgm_boss_conv_param_id: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    right: Flag | int,
    flag_3: Flag | int,
    left: int,
    left_1: int,
):
    """Event 28002830"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableFlag(flag_1)
    AND_1.Add(FlagEnabled(flag_1))
    if PlayerNotInOwnWorld():
        AND_1.Add(FlagEnabled(flag_2))
    if UnsignedNotEqual(left=0, right=right):
        AND_1.Add(FlagEnabled(right))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    if FlagDisabled(flag_3):
        OR_10.Add(HealthValue(28000801) <= 0)
    OR_10.Add(FlagEnabled(flag_3))
    OR_10.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_10)
    
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)
    OR_2.Add(FlagEnabled(flag_3))
    OR_2.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_2)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    WaitFrames(frames=1)
    SkipLinesIfValueEqual(0, left=left, right=0)  # NOTE: useless skip
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.HeatUp)
    OR_15.Add(FlagEnabled(28002823))
    OR_15.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_15)
    
    GotoIfFlagEnabled(Label.L1, flag=flag)
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.Unknown)
    OR_3.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_3)

    # --- Label 1 --- #
    DefineLabel(1)
    if ValueNotEqual(left=left_1, right=1):
        SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.LongFadeOut)
        End()
    SetBossMusic(bgm_boss_conv_param_id=bgm_boss_conv_param_id, state=BossMusicState.NormalFadeOut)


@RestartOnRest(28002849)
def Event_28002849():
    """Event 28002849"""
    CommonFunc_9005800(
        0,
        flag=28000800,
        entity=28001800,
        region=28002800,
        flag_1=28002805,
        character=28005800,
        action_button_id=10000,
        left=28000801,
        region_1=28002801,
    )
    CommonFunc_9005801(
        0,
        flag=28000800,
        entity=28001800,
        region=28002800,
        flag_1=28002805,
        flag_2=28002806,
        action_button_id=10000,
    )
    Event_28002815(0, flag=28000800, asset=28001800, vfx_id=3)
    Event_28002830(
        0,
        flag=28000800,
        bgm_boss_conv_param_id=505000,
        flag_1=28002805,
        flag_2=28002806,
        right=28002801,
        flag_3=28002802,
        left=1,
        left_1=0,
    )


@RestartOnRest(28000700)
def Event_28000700(_, flag: Flag | int, character: Character | int, character_1: Character | int, distance: float):
    """Event 28000700"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    SetCharacterTalkRange(character=character, distance=distance)
    if UnsignedNotEqual(left=0, right=character_1):
        SetCharacterTalkRange(character=character_1, distance=distance)
    End()


@RestartOnRest(28000701)
def Event_28000701(
    _,
    flag: Flag | int,
    flag_1: Flag | int,
    seconds: float,
    flag_2: Flag | int,
    flag_3: Flag | int,
    seconds_1: float,
    flag_4: Flag | int,
    flag_5: Flag | int,
    region: Region | int,
    flag_6: Flag | int,
    flag_7: Flag | int,
):
    """Event 28000701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Wait(seconds)
    EnableFlag(flag_2)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(flag_3))
    
    OR_1.Add(TimeElapsed(seconds=seconds_1))
    AND_1.Add(FlagEnabled(flag_7))
    AND_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag_4))
    
    MAIN.Await(OR_1)
    
    EnableNetworkFlag(flag_6)
    if FlagEnabled(flag_4):
        return
    EnableFlag(flag_5)
    End()


@RestartOnRest(28000702)
def Event_28000702(_, flag: Flag | int, flag_1: Flag | int, region: Region | int, flag_2: Flag | int):
    """Event 28000702"""
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(CharacterInsideRegion(character=ALL_PLAYERS, region=region))
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    if FlagEnabled(flag_2):
        return
    EnableFlag(flag_2)
    End()
