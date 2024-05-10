"""
Northwest Mountaintops (SW) (NW)

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
from .enums.m60_48_57_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005600(
        0,
        grace_flag=1048570000,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
        character=1048570480,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricArcher0,
        animation_id=30000,
        animation_id_1=20000,
        region=1048572277,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricArcher1,
        animation_id=30000,
        animation_id_1=20000,
        region=1048572277,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.AlbinauricArcher2,
        animation_id=30000,
        animation_id_1=20000,
        region=1048572285,
        radius=10.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005300(0, flag=1048570200, character=1048570200, item_lot=40526, seconds=0.0, item_is_dropped=0)
    CommonFunc_90005300(
        0,
        flag=1048570250,
        character=Characters.BlackKnifeAssassin0,
        item_lot=1048570900,
        seconds=0.0,
        item_is_dropped=0,
    )
    CommonFunc_90005300(
        0,
        flag=1048570251,
        character=Characters.BlackKnifeAssassin1,
        item_lot=1048570910,
        seconds=0.0,
        item_is_dropped=0,
    )
    CommonFunc_90005300(
        0,
        flag=1048570252,
        character=Characters.BlackKnifeAssassin2,
        item_lot=1048570920,
        seconds=0.0,
        item_is_dropped=0,
    )
    CommonFunc_90005300(
        0,
        flag=1048570253,
        character=Characters.BlackKnifeAssassin3,
        item_lot=1048570930,
        seconds=0.0,
        item_is_dropped=0,
    )
    Event_1048572820(
        0,
        character=Characters.DeathRiteBird,
        animation_id=30000,
        animation_id_1=20000,
        region=1048572800,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_FieldBattleHealthBar(0, boss=Characters.DeathRiteBird, name=904980607, npc_threat_level=24)
    CommonFunc_90005860(
        0,
        flag=1048570800,
        left=0,
        character=Characters.DeathRiteBird,
        left_1=0,
        item_lot=1048570700,
        seconds=0.0,
    )
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=15,
        block_id=0,
        cc_id=0,
        dd_id=0,
        player_start=15002600,
        unk_8_12=0,
        flag=1048572501,
        left_flag=1048572502,
        cancel_flag__right_flag=1048572503,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1048572300(
        0,
        anchor_entity=Assets.AEG099_171_2000,
        asset=1048576300,
        asset_1=1048576301,
        character=1048575300,
        character_1=1048575301,
        destination=1048572300,
    )
    Event_1048572310()
    Event_1048572320(0, entity=Assets.AEG099_171_2000)
    Event_1048572350()
    Event_1048572355()
    Event_1048572390()
    Event_1048572340(0, character=1048575310)
    Event_1048572370(0, asset=Assets.AEG110_029_2000, asset_1=Assets.AEG110_039_2000, flag=1048570370)
    Event_1048572370(1, asset=Assets.AEG110_029_2001, asset_1=Assets.AEG110_039_2001, flag=1048570371)
    Event_1048572370(2, asset=Assets.AEG110_029_2002, asset_1=Assets.AEG110_039_2002, flag=1048570372)
    Event_1048572370(3, asset=Assets.AEG110_029_2003, asset_1=Assets.AEG110_039_2003, flag=1048570373)
    CommonFunc_90005261(
        0,
        character=Characters.BlackKnifeAssassin0,
        region=1048572250,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    Event_1048572256()
    Event_1048572260()
    Event_1048572270()
    Event_1048572275(0, character=Characters.BlackKnifeAssassin5)
    Event_1048572580()
    Event_1048572400()


@RestartOnRest(1048572256)
def Event_1048572256():
    """Event 1048572256"""
    ForceAnimation(Characters.BlackKnifeAssassin6, 30001, loop=True)


@RestartOnRest(1048572260)
def Event_1048572260():
    """Event 1048572260"""
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(20000, 416))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(20000, 14508)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572270)
def Event_1048572270():
    """Event 1048572270"""
    AND_1.Add(CharacterHasSpecialEffect(Characters.BlackKnifeAssassin5, 14507))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.BlackKnifeAssassin4, 14507)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572275)
def Event_1048572275(_, character: uint):
    """Event 1048572275"""
    EnableInvincibility(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()


@RestartOnRest(1048572300)
def Event_1048572300(
    _,
    anchor_entity: uint,
    asset: uint,
    asset_1: uint,
    character: uint,
    character_1: uint,
    destination: uint,
):
    """Event 1048572300"""
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L5, flag=1048572308)
    GotoIfFlagEnabled(Label.L6, flag=1048572309)
    DeactivateGparamOverride(change_duration=0.0)
    DisableAsset(asset)
    EnableAsset(asset_1)
    EnableCharacter(character)
    DisableInvincibility(character)
    DisableCharacter(character_1)
    EnableInvincibility(character_1)
    RemoveSpecialEffect(PLAYER, 190)
    EnableTreasure(asset=Assets.AEG099_990_9001)
    EnableFlag(1048572308)
    DisableFlag(1048572309)
    EnableFlag(1048572305)
    EnableFlag(1048572308)
    DisableFlag(1048572309)
    Wait(1.0)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    if FlagEnabled(1048572309):
        return
    DeactivateGparamOverride(change_duration=0.0)
    DisableAsset(asset)
    EnableAsset(asset_1)
    EnableCharacter(character)
    DisableInvincibility(character)
    DisableCharacter(character_1)
    EnableInvincibility(character_1)
    RemoveSpecialEffect(PLAYER, 190)
    EnableTreasure(asset=Assets.AEG099_990_9001)
    Goto(Label.L7)

    # --- Label 6 --- #
    DefineLabel(6)
    ActivateGparamOverride(gparam_sub_id=0, change_duration=0.0)
    EnableAsset(asset)
    DisableAsset(asset_1)
    DisableCharacter(character)
    EnableInvincibility(character)
    EnableCharacter(character_1)
    DisableInvincibility(character_1)
    AddSpecialEffect(PLAYER, 190)
    DisableTreasure(asset=Assets.AEG099_990_9001)
    DeleteAssetVFX(Assets.AEG099_060_9000)
    AddSpecialEffect(PLAYER, 514)

    # --- Label 7 --- #
    DefineLabel(7)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1048572309):
        return
    if FlagEnabled(1048570350):
        return
    AwaitFlagEnabled(flag=1048570310)
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9527, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    AwaitDialogResponse(
        message=30021,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=1048572306,
        right_flag=1048572307,
        cancel_flag=0,
    )
    GotoIfFlagEnabled(Label.L2, flag=1048572306)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_3.Add(Multiplayer())
    OR_3.Add(MultiplayerPending())
    if OR_3:
        return RESTART
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60450)
    Wait(1.0)
    MoveCharacterAndCopyDrawParentWithFadeout(
        character=PLAYER,
        destination_type=CoordEntityType.Region,
        destination=destination,
        dummy_id=-1,
        copy_draw_parent=PLAYER,
        use_bonfire_effect=False,
        reset_camera=True,
    )
    Wait(1.0)
    ForceAnimation(PLAYER, 60451, skip_transition=True)
    EnableFlag(1048572305)
    ActivateGparamOverride(gparam_sub_id=0, change_duration=1.5)
    ShootProjectile(
        owner_entity=Characters.Dummy0,
        source_entity=1048572310,
        dummy_id=100,
        behavior_id=100930,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    EnableAsset(asset)
    DisableAsset(asset_1)
    DisableCharacter(character)
    DisableCharacter(1248550350)
    DisableCharacter(1248550351)
    DisableCharacter(1248550360)
    DisableCharacter(1248550361)
    EnableInvincibility(character)
    EnableInvincibility(1248550350)
    EnableInvincibility(1248550351)
    EnableInvincibility(1248550360)
    EnableInvincibility(1248550361)
    EnableCharacter(character_1)
    DisableInvincibility(character_1)
    AddSpecialEffect(PLAYER, 190)
    DisableTreasure(asset=Assets.AEG099_990_9001)
    DeleteAssetVFX(Assets.AEG099_060_9000)
    AddSpecialEffect(PLAYER, 514)
    DisableFlag(1048572308)
    EnableFlag(1048572309)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(1048572306)
    DisableFlag(1048572307)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572310)
def Event_1048572310():
    """Event 1048572310"""
    DisableNetworkSync()
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9210, entity=Assets.AEG099_023_2000))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=60100, anchor_entity=Assets.AEG099_023_2000)
    Wait(1.0)
    EnableNetworkFlag(1048570310)
    Restart()


@RestartOnRest(1048572320)
def Event_1048572320(_, entity: uint):
    """Event 1048572320"""
    ForceAnimation(entity, 0, loop=True)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1048570350):
        return
    ForceAnimation(entity, 10, loop=True)
    AwaitFlagEnabled(flag=1048570310)
    if FlagEnabled(1048572309):
        return
    AND_1.Add(Singleplayer())
    AND_2.Add(MultiplayerPending())
    AND_1.Add(not AND_2)
    AND_1.Add(FlagEnabled(1048570310))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    ForceAnimation(entity, 1, loop=True)
    AND_11.Add(Singleplayer())
    AND_12.Add(MultiplayerPending())
    AND_11.Add(not AND_12)
    OR_1.Add(not AND_11)
    OR_1.Add(FlagEnabled(1048572309))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(1048572340)
def Event_1048572340(_, character: uint):
    """Event 1048572340"""
    DisableAnimations(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    End()


@RestartOnRest(1048572350)
def Event_1048572350():
    """Event 1048572350"""
    GotoIfFlagEnabled(Label.L0, flag=1048570350)
    DeleteAssetVFX(Assets.AEG099_251_9000, erase_root=False)
    CreateAssetVFX(Assets.AEG099_251_9000, vfx_id=200, dummy_id=1505)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1048570370))
    AND_1.Add(FlagEnabled(1048570371))
    AND_1.Add(FlagEnabled(1048570372))
    AND_1.Add(FlagEnabled(1048570373))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1048570350)
    Wait(2.299999952316284)
    DisplayDialog(text=30020, anchor_entity=0, display_distance=5.0)
    DisableAsset(Assets.AEG099_251_9000)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    PlaySoundEffect(Assets.AEG099_251_9000, 1500, sound_type=SoundType.s_SFX)
    AddSpecialEffect(20000, 8870)
    Wait(4.5)
    WarpToMap(game_map=NORTHWEST_MOUNTAINTOPS_SW_NW, player_start=1048572301)
    End()
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG099_251_9000)
    DeleteAssetVFX(Assets.AEG099_251_9000)
    PlaySoundEffect(Assets.AEG099_251_9000, 1500, sound_type=SoundType.s_SFX)
    End()


@RestartOnRest(1048572355)
def Event_1048572355():
    """Event 1048572355"""
    GotoIfFlagEnabled(Label.L0, flag=1048570350)
    DeleteAssetVFX(1048571380, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2001, erase_root=False)
    DeleteAssetVFX(1048571382, erase_root=False)
    DeleteAssetVFX(1048571383, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2004, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2005, erase_root=False)
    CreateAssetVFX(1048571380, vfx_id=200, dummy_id=1503)
    CreateAssetVFX(Assets.AEG110_264_2001, vfx_id=200, dummy_id=1503)
    CreateAssetVFX(1048571382, vfx_id=200, dummy_id=1503)
    CreateAssetVFX(1048571383, vfx_id=200, dummy_id=1503)
    CreateAssetVFX(Assets.AEG110_264_2004, vfx_id=200, dummy_id=1503)
    CreateAssetVFX(Assets.AEG110_264_2005, vfx_id=200, dummy_id=1503)
    AND_1.Add(FlagEnabled(1048572309))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(1048571380)
    DisableAsset(Assets.AEG110_264_2001)
    DisableAsset(1048571382)
    DisableAsset(1048571383)
    DisableAsset(Assets.AEG110_264_2004)
    DisableAsset(Assets.AEG110_264_2005)
    DeleteAssetVFX(1048571380, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2001, erase_root=False)
    DeleteAssetVFX(1048571382, erase_root=False)
    DeleteAssetVFX(1048571383, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2004, erase_root=False)
    DeleteAssetVFX(Assets.AEG110_264_2005, erase_root=False)
    End()


@RestartOnRest(1048572370)
def Event_1048572370(_, asset: uint, asset_1: uint, flag: uint):
    """Event 1048572370"""
    DeleteAssetVFX(asset)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AwaitFlagEnabled(flag=1048572309)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9528, entity=asset))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 60550)
    EnableFlag(flag)
    Wait(1.2000000476837158)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(asset_1)
    CreateAssetVFX(asset_1, vfx_id=200, dummy_id=806061)
    AwaitFlagEnabled(flag=1048572309)
    CreateAssetVFX(asset, vfx_id=200, dummy_id=806060)
    End()
    GotoIfFlagEnabled(Label.L0, flag=1048572309)


@RestartOnRest(1048572390)
def Event_1048572390():
    """Event 1048572390"""
    DisableNetworkSync()
    if FlagEnabled(1048570350):
        return
    OR_1.Add(ActionButtonParamActivated(action_button_id=9529, entity=Assets.AEG099_251_9000))
    OR_1.Add(FlagEnabled(1048570350))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(1048570350):
        return
    DisplayDialog(text=30023, anchor_entity=Assets.AEG099_251_9000)
    Wait(1.0)
    Restart()


@RestartOnRest(1048572400)
def Event_1048572400():
    """Event 1048572400"""
    DisableAsset(1048576305)


@RestartOnRest(1048572580)
def Event_1048572580():
    """Event 1048572580"""
    RegisterLadder(start_climbing_flag=1048570580, stop_climbing_flag=1048570581, asset=Assets.AEG110_193_2000)
    RegisterLadder(start_climbing_flag=1048570582, stop_climbing_flag=1048570583, asset=Assets.AEG110_193_2001)
    RegisterLadder(start_climbing_flag=1048570584, stop_climbing_flag=1048570585, asset=Assets.AEG110_228_2000)
    RegisterLadder(start_climbing_flag=1048570586, stop_climbing_flag=1048570587, asset=1048571586)
    RegisterLadder(start_climbing_flag=1048570588, stop_climbing_flag=1048570589, asset=Assets.AEG110_286_2000)
    RegisterLadder(start_climbing_flag=1048570590, stop_climbing_flag=1048570591, asset=Assets.AEG110_288_2000)
    RegisterLadder(start_climbing_flag=1048570592, stop_climbing_flag=1048570593, asset=Assets.AEG110_193_2002)
    RegisterLadder(start_climbing_flag=1048570594, stop_climbing_flag=1048570595, asset=Assets.AEG110_238_2000)
    RegisterLadder(start_climbing_flag=1048570596, stop_climbing_flag=1048570597, asset=1048571596)


@RestartOnRest(1048572820)
def Event_1048572820(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: uint,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 1048572820"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    EnableAI(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()
