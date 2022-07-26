"""
Southeast Liurnia (NE) (SE)

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
from .entities.m60_39_42_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1039420000, asset=Assets.AEG099_060_9000)
    Event_1039422202(0, character=Characters.RayaLucariaSoldier0)
    Event_1039422202(1, character=Characters.RayaLucariaSoldier1)
    Event_1039422202(2, character=Characters.RayaLucariaSoldier2)
    Event_1039422210(0, character=Characters.WanderingNoble0, region=1039422210, flag=1039422210)
    Event_1039422210(1, character=Characters.WanderingNoble1, region=1039422210, flag=1039422211)
    Event_1039422210(2, character=Characters.WanderingNoble2, region=1039422210, flag=1039422212)
    Event_1039422210(3, character=Characters.WanderingNoble3, region=1039422210, flag=1039422213)
    Event_1039422210(4, character=Characters.WanderingNoble4, region=1039422210, flag=1039422214)
    Event_1039422210(5, character=Characters.WanderingNoble5, region=1039422210, flag=1039422215)
    Event_1039422210(6, character=Characters.WanderingNoble6, region=1039422210, flag=1039422216)
    Event_1039422210(7, character=Characters.WanderingNoble7, region=1039422210, flag=1039422217)
    Event_1039422210(8, character=Characters.WanderingNoble8, region=1039422210, flag=1039422218)
    Event_1039422340(0, character=Characters.LiurniaTroll, region=1039422340, flag=1039422340)
    Event_1039422200(0, attacker__character=1039425200, region=1039422200)
    Event_1039422600(0, asset=1039421600, entity=1039421601, flag=82020)
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=60,
        block_id=35,
        cc_id=45,
        dd_id=0,
        player_start=1035452630,
        unk_8_12=0,
        flag=1035452610,
        left_flag=1039422611,
        cancel_flag__right_flag=1039422612,
        left=0,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    CommonFunc_90005630(0, far_view_id=61394200, asset=1039421500, model_point=115)
    CommonFunc_90005683(0, flag=62203, asset=Assets.AEG099_055_1000, vfx_id=209, flag_1=78294, flag_2=78294)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61020)
    CommonFunc_90005706(0, character=Characters.WanderingNoble9, animation_id=930025, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble9)


@RestartOnRest(1039422200)
def Event_1039422200(_, attacker__character: uint, region: uint):
    """Event 1039422200"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5657)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1039422200):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5657)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=35000))
    OR_2.Add(AttackedWithDamageType(attacked_entity=35000, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=35000, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=35000, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1039422200)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5657)


@RestartOnRest(1039422202)
def Event_1039422202(_, character: uint):
    """Event 1039422202"""
    Kill(character)
    End()


@RestartOnRest(1039422210)
def Event_1039422210(_, character: uint, region: uint, flag: uint):
    """Event 1039422210"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
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
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    ForceAnimation(character, 30004)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004)
    End()


@RestartOnRest(1039422340)
def Event_1039422340(_, character: uint, region: uint, flag: uint):
    """Event 1039422340"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
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
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    ForceAnimation(character, 30004)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20004)
    End()


@RestartOnRest(1039422600)
def Event_1039422600(_, asset: uint, entity: uint, flag: uint):
    """Event 1039422600"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    CreateAssetVFX(asset, vfx_id=200, model_point=803220)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 1)
    DeleteAssetVFX(asset)


@RestartOnRest(1039422610)
def Event_1039422610(
    _,
    anchor_entity: uint,
    area_id: uchar,
    block_id: uchar,
    cc_id: char,
    dd_id: char,
    player_start: uint,
    left_flag: uint,
    cancel_flag__right_flag: uint,
):
    """Event 1039422610"""
    if Multiplayer():
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9140, entity=anchor_entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialogAndSetFlags(
        message=4300,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=anchor_entity,
        display_distance=3.0,
        left_flag=left_flag,
        right_flag=cancel_flag__right_flag,
        cancel_flag=cancel_flag__right_flag,
    )
    GotoIfFlagEnabled(Label.L1, flag=left_flag)
    Wait(1.0)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    WarpToMap(game_map=(area_id, block_id, cc_id, dd_id), player_start=player_start)
