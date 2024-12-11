"""
Land of Shadow 11-11 (Alternate) NW NE

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
    RegisterGrace(grace_flag=76914, asset=2045471950)
    CommonFunc_90005301(0, flag=2045470200, character=2045470200, item_lot__unk1=2045470400, seconds=0.0, unk1=0)
    CommonFunc_90005211(
        0,
        character=2045470221,
        animation_id=30000,
        animation_id_1=20001,
        region=2045472220,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=2045470220, region=2045472220, radius=1.0, seconds=0.0, animation_id=3010)
    CommonFunc_90005301(0, flag=2045470350, character=2045470350, item_lot__unk1=40916, seconds=0.0, unk1=0)
    Event_2045472542(
        0,
        flag=2045478542,
        asset=2045471542,
        asset_1=2045471543,
        obj_act_id=2045473543,
        obj_act_id_1=1464026,
        animation_id=10,
        animation_id_1=2,
        obj_act_id_2=2045473542,
        obj_act_id_3=464057,
    )
    Event_2045472690()
    Event_2045472695()
    Event_2045472699()
    Event_2045472540(0, flag=2045470540, region=2045472540)


@RestartOnRest(2045472540)
def Event_2045472540(_, flag: Flag | int, region: Region | int):
    """Event 2045472540"""
    if FlagEnabled(flag):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    End()


@RestartOnRest(2045472542)
def Event_2045472542(
    _,
    flag: Flag | int,
    asset: uint,
    asset_1: Asset | int,
    obj_act_id: uint,
    obj_act_id_1: int,
    animation_id: int,
    animation_id_1: int,
    obj_act_id_2: uint,
    obj_act_id_3: int,
):
    """Event 2045472542"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    EndOfAnimation(asset=asset, animation_id=animation_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(AssetActivated(obj_act_id=obj_act_id))
    OR_3.Add(AND_2)
    AND_3.Add(AssetActivated(obj_act_id=obj_act_id_2))
    OR_3.Add(AND_3)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_3)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    ForceAnimation(asset, animation_id)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetActivation(asset_1, obj_act_id=obj_act_id_1)
    DisableAssetActivation(asset, obj_act_id=obj_act_id_3)
    End()


@RestartOnRest(2045472690)
def Event_2045472690():
    """Event 2045472690"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2045472691)
    DisableFlag(2045472692)
    if FlagEnabled(2045470690):
        return
    GotoIfFlagEnabled(Label.L10, flag=2050460690)
    GotoIfFlagEnabled(Label.L10, flag=40000690)
    DeleteAssetVFX(2045471690)
    CreateAssetVFX(2045471690, dummy_id=100, vfx_id=6102)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209524, entity=2045471690))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60071)
    AwardItemLot(2045470900, host_only=True)
    EnableFlag(2045470690)
    DeleteAssetVFX(2045471690)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(ActionButtonParamActivated(action_button_id=209525, entity=2045471691))
    OR_1.Add(PlayerHasWeapon(2540000))
    OR_1.Add(PlayerHasWeapon(2540001))
    OR_1.Add(PlayerHasWeapon(2540002))
    OR_1.Add(PlayerHasWeapon(2540003))
    OR_1.Add(PlayerHasWeapon(2540004))
    OR_1.Add(PlayerHasWeapon(2540005))
    OR_1.Add(PlayerHasWeapon(2540006))
    OR_1.Add(PlayerHasWeapon(2540007))
    OR_1.Add(PlayerHasWeapon(2540008))
    OR_1.Add(PlayerHasWeapon(2540009))
    OR_1.Add(PlayerHasWeapon(2540010))
    AND_3.Add(OR_1)
    OR_2.Add(AND_3)
    OR_2.Add(not OR_1)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_3)
    AwaitDialogResponse(
        message=2020025,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2045471691,
        display_distance=2.0,
        left_flag=2045472691,
        right_flag=2045472692,
        cancel_flag=2045472692,
    )
    if FlagDisabled(2045472691):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    AND_14.Add(PlayerHasWeapon(2540010))
    SkipLinesIfConditionFalse(5, AND_14)
    RemoveWeaponFromPlayer(item=2540010, quantity=1)
    AwardItemLot(2045470600, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477600)
    Goto(Label.L11)
    AND_13.Add(PlayerHasWeapon(2540009))
    SkipLinesIfConditionFalse(5, AND_13)
    RemoveWeaponFromPlayer(item=2540009, quantity=1)
    AwardItemLot(2045470590, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477590)
    Goto(Label.L11)
    AND_12.Add(PlayerHasWeapon(2540008))
    SkipLinesIfConditionFalse(5, AND_12)
    RemoveWeaponFromPlayer(item=2540008, quantity=1)
    AwardItemLot(2045470580, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477580)
    Goto(Label.L11)
    AND_11.Add(PlayerHasWeapon(2540007))
    SkipLinesIfConditionFalse(5, AND_11)
    RemoveWeaponFromPlayer(item=2540007, quantity=1)
    AwardItemLot(2045470570, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477570)
    Goto(Label.L11)
    AND_10.Add(PlayerHasWeapon(2540006))
    SkipLinesIfConditionFalse(5, AND_10)
    RemoveWeaponFromPlayer(item=2540006, quantity=1)
    AwardItemLot(2045470560, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477560)
    Goto(Label.L11)
    AND_9.Add(PlayerHasWeapon(2540005))
    SkipLinesIfConditionFalse(5, AND_9)
    RemoveWeaponFromPlayer(item=2540005, quantity=1)
    AwardItemLot(2045470550, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477550)
    Goto(Label.L11)
    AND_8.Add(PlayerHasWeapon(2540004))
    SkipLinesIfConditionFalse(5, AND_8)
    RemoveWeaponFromPlayer(item=2540004, quantity=1)
    AwardItemLot(2045470540, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477540)
    Goto(Label.L11)
    AND_7.Add(PlayerHasWeapon(2540003))
    SkipLinesIfConditionFalse(5, AND_7)
    RemoveWeaponFromPlayer(item=2540003, quantity=1)
    AwardItemLot(2045470530, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477530)
    Goto(Label.L11)
    AND_6.Add(PlayerHasWeapon(2540002))
    SkipLinesIfConditionFalse(5, AND_6)
    RemoveWeaponFromPlayer(item=2540002, quantity=1)
    AwardItemLot(2045470520, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477520)
    Goto(Label.L11)
    AND_5.Add(PlayerHasWeapon(2540001))
    SkipLinesIfConditionFalse(5, AND_5)
    RemoveWeaponFromPlayer(item=2540001, quantity=1)
    AwardItemLot(2045470510, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477510)
    Goto(Label.L11)
    AND_4.Add(PlayerHasWeapon(2540000))
    SkipLinesIfConditionFalse(5, AND_4)
    RemoveWeaponFromPlayer(item=2540000, quantity=1)
    AwardItemLot(2045470500, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477500)
    Goto(Label.L11)

    # --- Label 11 --- #
    DefineLabel(11)
    Wait(2.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ClearMainCondition()
    OR_1.Add(PlayerHasWeapon(2540000))
    OR_1.Add(PlayerHasWeapon(2540001))
    OR_1.Add(PlayerHasWeapon(2540002))
    OR_1.Add(PlayerHasWeapon(2540003))
    OR_1.Add(PlayerHasWeapon(2540004))
    OR_1.Add(PlayerHasWeapon(2540005))
    OR_1.Add(PlayerHasWeapon(2540006))
    OR_1.Add(PlayerHasWeapon(2540007))
    OR_1.Add(PlayerHasWeapon(2540008))
    OR_1.Add(PlayerHasWeapon(2540009))
    OR_1.Add(PlayerHasWeapon(2540010))
    
    MAIN.Await(OR_1)
    
    Restart()


@RestartOnRest(2045472695)
def Event_2045472695():
    """Event 2045472695"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(2045472693)
    DisableFlag(2045472694)
    if FlagEnabled(2045470690):
        return
    GotoIfFlagEnabled(Label.L10, flag=2050460690)
    GotoIfFlagEnabled(Label.L10, flag=40000690)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209525, entity=2045471691))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_1.Add(PlayerHasWeapon(2560000))
    OR_1.Add(PlayerHasWeapon(2560001))
    OR_1.Add(PlayerHasWeapon(2560002))
    OR_1.Add(PlayerHasWeapon(2560003))
    OR_1.Add(PlayerHasWeapon(2560004))
    OR_1.Add(PlayerHasWeapon(2560005))
    OR_1.Add(PlayerHasWeapon(2560006))
    OR_1.Add(PlayerHasWeapon(2560007))
    OR_1.Add(PlayerHasWeapon(2560008))
    OR_1.Add(PlayerHasWeapon(2560009))
    OR_1.Add(PlayerHasWeapon(2560010))
    AND_3.Add(OR_1)
    AND_1.Add(AND_3)
    OR_2.Add(AND_1)
    OR_2.Add(not AND_3)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_1)
    AwaitDialogResponse(
        message=2020027,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=2045471691,
        display_distance=2.0,
        left_flag=2045472693,
        right_flag=2045472694,
        cancel_flag=2045472694,
    )
    if FlagDisabled(2045472693):
        return RESTART
    ForceAnimation(PLAYER, 60071)
    AND_14.Add(PlayerHasWeapon(2560010))
    SkipLinesIfConditionFalse(5, AND_14)
    RemoveWeaponFromPlayer(item=2560010, quantity=1)
    AwardItemLot(2045470600, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477600)
    Goto(Label.L11)
    AND_13.Add(PlayerHasWeapon(2560009))
    SkipLinesIfConditionFalse(5, AND_13)
    RemoveWeaponFromPlayer(item=2560009, quantity=1)
    AwardItemLot(2045470590, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477590)
    Goto(Label.L11)
    AND_12.Add(PlayerHasWeapon(2560008))
    SkipLinesIfConditionFalse(5, AND_12)
    RemoveWeaponFromPlayer(item=2560008, quantity=1)
    AwardItemLot(2045470580, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477580)
    Goto(Label.L11)
    AND_11.Add(PlayerHasWeapon(2560007))
    SkipLinesIfConditionFalse(5, AND_11)
    RemoveWeaponFromPlayer(item=2560007, quantity=1)
    AwardItemLot(2045470570, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477570)
    Goto(Label.L11)
    AND_10.Add(PlayerHasWeapon(2560006))
    SkipLinesIfConditionFalse(5, AND_10)
    RemoveWeaponFromPlayer(item=2560006, quantity=1)
    AwardItemLot(2045470560, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477560)
    Goto(Label.L11)
    AND_9.Add(PlayerHasWeapon(2560005))
    SkipLinesIfConditionFalse(5, AND_9)
    RemoveWeaponFromPlayer(item=2560005, quantity=1)
    AwardItemLot(2045470550, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477550)
    Goto(Label.L11)
    AND_8.Add(PlayerHasWeapon(2560004))
    SkipLinesIfConditionFalse(5, AND_8)
    RemoveWeaponFromPlayer(item=2560004, quantity=1)
    AwardItemLot(2045470540, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477540)
    Goto(Label.L11)
    AND_7.Add(PlayerHasWeapon(2560003))
    SkipLinesIfConditionFalse(5, AND_7)
    RemoveWeaponFromPlayer(item=2560003, quantity=1)
    AwardItemLot(2045470530, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477530)
    Goto(Label.L11)
    AND_6.Add(PlayerHasWeapon(2560002))
    SkipLinesIfConditionFalse(5, AND_6)
    RemoveWeaponFromPlayer(item=2560002, quantity=1)
    AwardItemLot(2045470520, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477520)
    Goto(Label.L11)
    AND_5.Add(PlayerHasWeapon(2560001))
    SkipLinesIfConditionFalse(5, AND_5)
    RemoveWeaponFromPlayer(item=2560001, quantity=1)
    AwardItemLot(2045470510, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477510)
    Goto(Label.L11)
    AND_4.Add(PlayerHasWeapon(2560000))
    SkipLinesIfConditionFalse(5, AND_4)
    RemoveWeaponFromPlayer(item=2560000, quantity=1)
    AwardItemLot(2045470500, host_only=True)
    WaitRealFrames(frames=1)
    DisableFlag(2045477500)
    Goto(Label.L11)

    # --- Label 11 --- #
    DefineLabel(11)
    Wait(2.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ClearMainCondition()
    AND_3.Add(PlayerDoesNotHaveWeapon(2540000))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540001))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540002))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540003))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540004))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540005))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540006))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540007))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540008))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540009))
    AND_3.Add(PlayerDoesNotHaveWeapon(2540010))
    OR_1.Add(PlayerHasWeapon(2560000))
    OR_1.Add(PlayerHasWeapon(2560001))
    OR_1.Add(PlayerHasWeapon(2560002))
    OR_1.Add(PlayerHasWeapon(2560003))
    OR_1.Add(PlayerHasWeapon(2560004))
    OR_1.Add(PlayerHasWeapon(2560005))
    OR_1.Add(PlayerHasWeapon(2560006))
    OR_1.Add(PlayerHasWeapon(2560007))
    OR_1.Add(PlayerHasWeapon(2560008))
    OR_1.Add(PlayerHasWeapon(2560009))
    OR_1.Add(PlayerHasWeapon(2560010))
    AND_3.Add(OR_1)
    
    MAIN.Await(AND_3)
    
    Restart()


@RestartOnRest(2045472699)
def Event_2045472699():
    """Event 2045472699"""
    GotoIfPlayerNotInOwnWorld(Label.L15)
    GotoIfFlagEnabled(Label.L10, flag=2050460690)
    GotoIfFlagEnabled(Label.L10, flag=40000690)
    EnableNetworkFlag(2045472697)
    EnableAsset(2045471690)
    DisableAsset(2045471691)
    DisableAsset(2045471692)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    EnableNetworkFlag(2045472698)
    DisableAsset(2045471690)
    EnableAsset(2045471691)
    DisableAsset(2045471692)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    EnableAsset(2045471690)
    DisableAsset(2045471691)
    DisableAsset(2045471692)
    OR_1.Add(FlagEnabled(2045472697))
    OR_1.Add(FlagEnabled(2045472698))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(2045472697):
        return
    DisableAsset(2045471690)
    EnableAsset(2045471691)
    DisableAsset(2045471692)
