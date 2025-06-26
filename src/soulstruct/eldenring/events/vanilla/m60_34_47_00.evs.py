"""
West Liurnia (NE) (NW)

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
from .enums.m60_34_47_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034470000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76214,
        flag_1=76211,
        asset=Assets.AEG099_090_9001,
        source_flag=77220,
        value=1,
        flag_2=78220,
        flag_3=78221,
        flag_4=78222,
        flag_5=78223,
        flag_6=78224,
        flag_7=78225,
        flag_8=78226,
        flag_9=78227,
        flag_10=78228,
        flag_11=78229,
    )
    CommonFunc_90005605(
        0,
        asset=Assets.AEG099_510_9000,
        area_id=10,
        block_id=1,
        cc_id=0,
        dd_id=0,
        player_start=10012690,
        unk_8_12=0,
        flag=1034472610,
        left_flag=1034472611,
        cancel_flag__right_flag=1034472612,
        left=1034470610,
        text=0,
        seconds=0.0,
        seconds_1=0.0,
    )
    Event_1034472611(
        0,
        flag=1034470611,
        destination=Assets.AEG099_295_9000,
        left_flag=1034472613,
        cancel_flag__right_flag=1034472614,
    )
    Event_1034472612(0, flag=1034470611, asset=Assets.AEG027_216_9000)
    Event_1034472260(
        0,
        flag=1034470250,
        destination=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1034472260(
        1,
        flag=1034470251,
        destination=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        seconds_5=0.0,
        seconds_6=0.0,
    )
    Event_1034472261(
        0,
        flag=1034470250,
        asset=Assets.AEG099_160_9000,
        character=Characters.Balloon0,
        character_1=1034475260,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1034471300,
        flag_1=1034472250,
    )
    Event_1034472261(
        1,
        flag=1034470251,
        asset=Assets.AEG099_160_9001,
        character=Characters.Balloon1,
        character_1=1034475263,
        seconds=0.0,
        seconds_1=0.0,
        seconds_2=0.0,
        seconds_3=0.0,
        seconds_4=0.0,
        item_lot=1034471310,
        flag_1=1034472251,
    )
    Event_1034472262(
        0,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette0,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034472250,
    )
    Event_1034472262(
        1,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette1,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034472250,
    )
    Event_1034472262(
        3,
        character=Characters.Balloon0,
        seconds=0.0,
        attacked_entity=Characters.Balloon0,
        seconds_1=0.0,
        character_1=Characters.Marionette2,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034472250,
    )
    Event_1034472262(
        4,
        character=Characters.Balloon1,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character_1=Characters.Marionette3,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034472251,
    )
    Event_1034472262(
        5,
        character=Characters.Balloon1,
        seconds=0.0,
        attacked_entity=Characters.Balloon1,
        seconds_1=0.0,
        character_1=Characters.Marionette4,
        animation_id=30010,
        animation_id_1=20010,
        radius=20.0,
        seconds_2=0.0,
        seconds_3=0.0,
        flag=1034472251,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=1034470340,
        animation_id=30005,
        animation_id_1=20005,
        region=1034472340,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower0,
        region=1034472200,
        radius=5.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower1,
        region=1034472200,
        radius=5.0,
        seconds=2.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower2,
        region=1034472200,
        radius=5.0,
        seconds=1.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower3,
        region=1034472200,
        radius=5.0,
        seconds=0.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower4,
        region=1034472200,
        radius=5.0,
        seconds=1.5,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower5,
        region=1034472200,
        radius=5.0,
        seconds=0.0,
        animation_id=1705,
    )
    CommonFunc_90005261(
        0,
        character=Characters.RevenantFollower6,
        region=1034472200,
        radius=5.0,
        seconds=2.0,
        animation_id=1705,
    )


@RestartOnRest(1034472260)
def Event_1034472260(
    _,
    flag: Flag | int,
    destination: uint,
    character: Character | int,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    seconds_5: float,
    seconds_6: float,
):
    """Event 1034472260"""
    if FlagEnabled(flag):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    if AND_1:
        return
    ForceAnimation(destination, 0)
    Move(character, destination=destination, destination_type=CoordEntityType.Asset, dummy_id=220, short_move=True)
    Wait(5.400000095367432)
    Restart()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)
    Wait(seconds_5)
    Wait(seconds_6)


@RestartOnRest(1034472261)
def Event_1034472261(
    _,
    flag: Flag | int,
    asset: uint,
    character: uint,
    character_1: uint,
    seconds: float,
    seconds_1: float,
    seconds_2: float,
    seconds_3: float,
    seconds_4: float,
    item_lot: int,
    flag_1: Flag | int,
):
    """Event 1034472261"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAsset(asset)
    DisableCharacter(character)
    DisableAnimations(character)
    Kill(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, dummy_id=200, vfx_id=803160)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=ALL_PLAYERS))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ForceAnimation(asset, 1)
    DeleteAssetVFX(asset)
    Wait(1.0)
    DisableAsset(asset)
    if PlayerInOwnWorld():
        Wait(0.30000001192092896)
        AwardItemLot(item_lot, host_only=True)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_2)
    Wait(seconds_3)
    Wait(seconds_4)


@RestartOnRest(1034472262)
def Event_1034472262(
    _,
    character: uint,
    seconds: float,
    attacked_entity: Character | int,
    seconds_1: float,
    character_1: uint,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    seconds_2: float,
    seconds_3: float,
    flag: Flag | int,
):
    """Event 1034472262"""
    if FlagEnabled(character):
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character_1)
    ForceAnimation(character_1, animation_id)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=ALL_PLAYERS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=ALL_PLAYERS))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character_1, state_info=260))
    OR_2.Add(EntityWithinDistance(entity=character_1, other_entity=ALL_PLAYERS, radius=radius))
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
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EnableNetworkFlag(flag)
    SetSpecialStandbyEndedFlag(character=character_1, state=True)
    Wait(seconds_2)
    ForceAnimation(character_1, animation_id_1)
    End()
    Wait(seconds)
    Wait(seconds_1)
    Wait(seconds_3)


@RestartOnRest(1034472611)
def Event_1034472611(
    _,
    flag: Flag | int,
    destination: uint,
    left_flag: Flag | int,
    cancel_flag__right_flag: Flag | int,
):
    """Event 1034472611"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(PlayerNotInOwnWorld())
    if OR_1:
        return
    DisableFlag(left_flag)
    DisableFlag(cancel_flag__right_flag)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9523, entity=destination))
    
    AwaitDialogResponse(
        message=108186,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=destination,
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
    AND_2.Add(PlayerHasGood(8186))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 50050)
    Wait(1.5)
    DisplayDialog(text=308186, anchor_entity=destination)
    Wait(1.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Asset, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 60810)
    Wait(2.5)
    EnableNetworkFlag(flag)
    EnableNetworkFlag(1034470610)
    DisplayDialog(text=208186, anchor_entity=destination)
    RemoveGoodFromPlayer(item=8186, quantity=1)


@RestartOnRest(1034472612)
def Event_1034472612(_, flag: Flag | int, asset: Asset | int):
    """Event 1034472612"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EnableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableAsset(asset)
