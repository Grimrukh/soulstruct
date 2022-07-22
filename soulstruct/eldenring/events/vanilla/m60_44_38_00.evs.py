"""
East Limgrave (NW) (SW)

linked:
0
72
154
238

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\common_macro.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_44_38_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044380000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005460(0, character=Characters.Skeleton0)
    CommonFunc_90005461(0, character=Characters.Skeleton0)
    CommonFunc_90005462(0, character=Characters.Skeleton0)
    CommonFunc_90005300(0, flag=1044380210, character=Characters.Scarab, item_lot=40142, seconds=0.0, left=0)
    CommonFunc_90005632(0, flag=580000, asset=Assets.AEG099_371_1001, item_lot=80000)
    Event_1044382220()
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.YuraHunterofBloodyFingers,
        flag=3621,
        flag_1=3620,
        flag_2=1043379251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        flag=3621,
        flag_1=3622,
        flag_2=1043379251,
        flag_3=3621,
        first_flag=3620,
        last_flag=3624,
        right=-1,
    )
    CommonFunc_90005702(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        flag=1044389209,
        first_flag=1044389209,
        last_flag=1044389209,
    )
    Event_1044383720(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1044383721(0, 1044380710)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044380700)
    DisableBackread(1044380701)
    DisableBackread(1044380702)
    DisableBackread(Characters.YuraHunterofBloodyFingers)
    CommonFunc_90005251(0, character=1044380340, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Skeleton0, region=1044382200, seconds=1.0, animation_id=1700)
    CommonFunc_90005250(
        0,
        character=Characters.Skeleton1,
        region=1044382200,
        seconds=0.30000001192092896,
        animation_id=1700,
    )
    CommonFunc_90005250(0, character=Characters.Skeleton2, region=1044382200, seconds=0.0, animation_id=1700)
    CommonFunc_90005250(0, character=Characters.Skeleton3, region=1044382200, seconds=0.0, animation_id=1700)
    CommonFunc_90005250(0, 1044380204, 1044382200, 0.5, 1700)


@RestartOnRest(1044382220)
def Event_1044382220():
    """Event 1044382220"""
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagEnabled(1044380220))
    SkipLinesIfConditionFalse(3, AND_1)
    EnableCharacter(1044385220)
    EnableAnimations(1044385220)
    End()
    
    MAIN.Await(FlagEnabled(3625))
    
    DisableCharacter(1044385220)
    DisableAnimations(1044385220)
    EnableFlag(1044380220)
    Wait(1.0)
    Restart()


@RestartOnRest(1044382600)
def Event_1044382600(_, asset: uint, item_lot: int, flag: uint):
    """Event 1044382600"""
    if FlagEnabled(flag):
        return
    CreateAssetVFX(asset, vfx_id=200, model_point=806840)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9310, entity=asset))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 806841, sound_type=SoundType.s_SFX)
    Wait(0.10000000149011612)
    AwardItemLot(item_lot, host_only=False)
    EnableFlag(flag)


@RestartOnRest(1044383720)
def Event_1044383720(_, character: uint):
    """Event 1044383720"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3620):
        DisableFlag(1043379255)
    DisableFlag(1043369200)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(FlagDisabled(1043372717))
    OR_1.Add(FlagEnabled(1043372718))
    AND_1.Add(OR_1)
    OR_11.Add(FlagDisabled(1043369200))
    OR_11.Add(FlagEnabled(1043360800))
    AND_1.Add(OR_11)
    AND_1.Add(FlagEnabled(3625))
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagDisabled(1043372717))
    OR_3.Add(FlagEnabled(1043372718))
    AND_3.Add(OR_3)
    OR_13.Add(FlagDisabled(1043369200))
    OR_13.Add(FlagEnabled(1043360800))
    AND_3.Add(OR_13)
    AND_3.Add(FlagEnabled(3625))
    
    MAIN.Await(AND_3)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L1, flag=3620)
    GotoIfFlagEnabled(Label.L2, flag=3621)
    GotoIfFlagEnabled(Label.L3, flag=3622)
    GotoIfFlagEnabled(Label.L4, flag=3623)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 90100)
    GotoIfConditionTrue(Label.L20, input_condition=MAIN)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    OR_4.Add(FlagDisabled(1043372717))
    OR_4.Add(FlagEnabled(1043372718))
    AND_4.Add(OR_4)
    OR_14.Add(FlagDisabled(1043369200))
    OR_14.Add(FlagEnabled(1043360800))
    AND_4.Add(OR_14)
    AND_4.Add(FlagEnabled(3625))
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(1044383721)
def Event_1044383721(_, character: uint):
    """Event 1044383721"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043359259):
        return
    if FlagEnabled(1035469209):
        return
    if FlagEnabled(1039529209):
        return
    GotoIfFlagEnabled(Label.L1, flag=1044389209)
    
    MAIN.Await(FlagEnabled(1044389209))
    
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    if FlagEnabled(3625):
        return
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()
