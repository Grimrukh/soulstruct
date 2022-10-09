"""
West Limgrave (NE) (NW)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_42_39_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_1042392200(0, character=Characters.Wolf0, region=1042392200, owner_entity=Characters.Dummy, flag=1042392200)
    Event_1042392200(1, character=Characters.Wolf1, region=1042392200, owner_entity=Characters.Dummy, flag=1042392200)
    Event_1042392200(2, character=Characters.Wolf2, region=1042392200, owner_entity=Characters.Dummy, flag=1042392200)
    Event_1042392200(3, character=Characters.Wolf3, region=1042392200, owner_entity=Characters.Dummy, flag=1042392200)
    Event_1042392200(4, character=Characters.Wolf4, region=1042392200, owner_entity=Characters.Dummy, flag=1042392200)
    Event_1042392200(5, character=Characters.Wolf5, region=1042392240, owner_entity=Characters.Dummy, flag=1042392240)
    Event_1042392200(6, character=Characters.Wolf6, region=1042392240, owner_entity=Characters.Dummy, flag=1042392240)
    Event_1042392200(7, character=Characters.Wolf7, region=1042392240, owner_entity=Characters.Dummy, flag=1042392240)
    Event_1042392200(8, character=Characters.Wolf8, region=1042392249, owner_entity=Characters.Dummy, flag=1042392249)
    Event_1042392200(9, character=Characters.Wolf9, region=1042392249, owner_entity=Characters.Dummy, flag=1042392249)
    Event_1042392200(10, character=Characters.Wolf10, region=1042392249, owner_entity=Characters.Dummy, flag=1042392249)
    Event_1042392200(11, character=Characters.Wolf11, region=1042392249, owner_entity=Characters.Dummy, flag=1042392249)
    CommonFunc_90005300(0, flag=1042390310, character=Characters.Scarab, item_lot=40146, seconds=0.0, left=0)
    Event_1042392600(0, attacked_entity=1042391600, region=1042392600)
    Event_1042392600(1, attacked_entity=1042391601, region=1042392601)
    Event_1042392600(2, attacked_entity=1042391602, region=1042392602)
    Event_1042392600(3, attacked_entity=1042391603, region=1042392603)
    Event_1042392600(4, attacked_entity=1042391604, region=1042392604)
    Event_1042392600(5, attacked_entity=1042391605, region=1042392605)
    Event_1042392600(6, attacked_entity=1042391606, region=1042392606)
    CommonFunc_90005790(
        0,
        right=0,
        flag=1042390180,
        summon_flag=1042392181,
        dismissal_flag=1042392182,
        character=Characters.RecusantHenricus,
        sign_type=22,
        region=1042392180,
        region_1=1042392181,
        seconds=0.0,
        right_1=1042399250,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(0, flag=1042390180, flag_1=1042392181, flag_2=1042392182, character=Characters.RecusantHenricus)
    CommonFunc_90005792(
        0,
        flag=1042390180,
        flag_1=1042392181,
        flag_2=1042392182,
        character=Characters.RecusantHenricus,
        item_lot=1042390700,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1042390180,
        flag_1=1042392181,
        flag_2=1042392182,
        character=Characters.RecusantHenricus,
        other_entity=1042392180,
        region=0,
        left=0,
    )
    CommonFunc_90005795(
        0,
        flag=7602,
        flag_1=0,
        flag_2=1042399300,
        left_flag=1042392141,
        cancel_flag__right_flag=1042392142,
        message=80602,
        action_button_id=9000,
        asset=Assets.AEG099_090_9000,
        model_point=30010,
    )
    if CeremonyActive(ceremony=20):
        CommonFunc_90005796(0, flag=7602, character=Characters.OldKnightIstvan, banner_type=5, region=1042392141)
        Event_1042392145()
    Event_1042393700()
    Event_1042393710()
    CommonFunc_90005774(0, flag=7602, item_lot=1042390500, flag_1=1042397500)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.OldKnightIstvan)
    DisableBackread(1042390180)


@RestartOnRest(1042392145)
def Event_1042392145():
    """Event 1042392145"""
    if CeremonyInactive(ceremony=20):
        return
    EnableBackread(Characters.OldKnightIstvan)
    SetTeamType(Characters.OldKnightIstvan, TeamType.Human)
    DeleteAssetVFX(Assets.AEG099_120_9000)
    CreateAssetVFX(Assets.AEG099_120_9000, vfx_id=200, model_point=806700)


@RestartOnRest(1042392200)
def Event_1042392200(_, character: uint, region: uint, owner_entity: uint, flag: uint):
    """Event 1042392200"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
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
    
    EnableFlag(flag)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_7.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_11.Add(OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    EnableCharacter(character)
    ForceAnimation(character, 20011)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        model_point=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    RemoveSpecialEffect(character, 8090)


@RestartOnRest(1042392300)
def Event_1042392300():
    """Event 1042392300"""
    if FlagEnabled(1042399710):
        return
    if FlagEnabled(1042399700):
        return
    if Multiplayer():
        return
    DisableCharacter(Characters.OldKnightIstvan)
    CreateAssetVFX(Assets.AEG099_090_9000, vfx_id=100, model_point=30010)
    AND_1.Add(FlagDisabled(1042399700))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9000, entity=Assets.AEG099_090_9000))
    AND_1.Add(Singleplayer())
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(Assets.AEG099_090_9000)
    Wait(1.0)
    AddSpecialEffect(PLAYER, 15)

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(1042392301)
def Event_1042392301():
    """Event 1042392301"""
    if FlagEnabled(1042399710):
        return
    if FlagDisabled(1042399700):
        return
    EnableCharacter(Characters.OldKnightIstvan)
    ActivateGparamOverride(gparam_sub_id=0, change_duration=0.0)
    SetTeamType(Characters.OldKnightIstvan, TeamType.Enemy)
    DisableFlag(1042399700)
    AND_1.Add(CharacterDead(Characters.OldKnightIstvan))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042399710)
    DeactivateGparamOverride(change_duration=10.0)
    DisplayBanner(BannerType.GreatEnemyFelled)
    SetPseudoMultiplayerReturnPosition(region=1042392721)
    IssueEndOfPseudoMultiplayerNotification(success=True)


@RestartOnRest(1042392302)
def Event_1042392302():
    """Event 1042392302"""
    GotoIfFlagEnabled(Label.L1, flag=1042399710)
    GotoIfFlagDisabled(Label.L0, flag=1042399700)
    EnableAsset(Assets.AEG099_120_9000)
    CreateAssetVFX(Assets.AEG099_120_9000, vfx_id=200, model_point=806700)
    DeleteAssetVFX(Assets.AEG099_090_9000)
    AND_1.Add(CharacterDead(Characters.OldKnightIstvan))
    
    MAIN.Await(AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteAssetVFX(Assets.AEG099_090_9000)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(Assets.AEG099_120_9000)


@RestartOnRest(1042392600)
def Event_1042392600(_, attacked_entity: uint, region: uint):
    """Event 1042392600"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 810000099, sound_type=SoundType.Unknown14)
    ForceAnimation(attacked_entity, 1)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(2.0)
    TriggerAISound(ai_sound_param_id=7000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()


@RestartOnRest(1042393700)
def Event_1042393700():
    """Event 1042393700"""
    WaitFrames(frames=1)
    EnableFlag(1042399250)
    if FlagDisabled(16009208):
        return
    DisableFlag(1042399250)
    End()


@RestartOnRest(1042393710)
def Event_1042393710():
    """Event 1042393710"""
    WaitFrames(frames=1)
    if FlagDisabled(400073):
        return
    EnableFlag(1042399300)
    End()
