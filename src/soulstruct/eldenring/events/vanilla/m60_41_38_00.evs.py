"""
West Limgrave (NW) (SE)

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
from .enums.m60_41_38_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1041380000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=71001,
        flag_1=76102,
        asset=Assets.AEG099_090_9001,
        source_flag=77100,
        value=3,
        flag_2=78100,
        flag_3=78101,
        flag_4=78102,
        flag_5=78103,
        flag_6=78104,
        flag_7=78105,
        flag_8=78106,
        flag_9=78107,
        flag_10=78108,
        flag_11=78109,
    )
    Event_1041382650(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    CommonFunc_90005460(0, character=1041380240)
    CommonFunc_90005461(0, character=1041380240)
    CommonFunc_90005462(0, character=1041380240)
    CommonFunc_90005300(0, flag=1041380230, character=Characters.Scarab, item_lot=40104, seconds=0.0, left=0)
    Event_1041382200(0, character=Characters.Wolf0, region=1041382250, owner_entity=Characters.Dummy)
    Event_1041382200(1, character=Characters.Wolf1, region=1041382250, owner_entity=Characters.Dummy)
    Event_1041382200(2, character=Characters.Wolf2, region=1041382250, owner_entity=Characters.Dummy)
    Event_1041382200(3, character=Characters.Wolf3, region=1041382250, owner_entity=Characters.Dummy)
    Event_1041383710(0, flag=4720, flag_1=1042389201, flag_2=1041389370)
    Event_1041383730(0, character=Characters.Roderika)
    CommonFunc_90005752(0, asset=Assets.AEG099_320_9000, dummy_id=200, vfx_id=120, seconds=3.0)
    Event_1041383731()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9003,
        action_button_id=4350,
        item_lot=101910,
        first_flag=400191,
        last_flag=400191,
        flag=1041389414,
        vfx_id=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9003,
        action_button_id=4350,
        item_lot=101910,
        first_flag=400191,
        last_flag=400191,
        flag=3708,
        vfx_id=0,
    )
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_090_9003,
        action_button_id=4350,
        item_lot=101910,
        first_flag=400191,
        last_flag=400191,
        flag=3709,
        vfx_id=0,
    )
    Event_1041383750(0, character=1041380705)
    Event_1041383760(0, flag=78103, other_entity=Characters.TalkDummy0, flag_1=1041389500)
    Event_1041383761(0, other_entity=Characters.TalkDummy0, flag=1041389500)
    Event_1041383762(0, other_entity=Characters.TalkDummy0, flag=1041389501)
    Event_1041383763(0, other_entity=Characters.TalkDummy0, flag=1041389501)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Roderika)
    DisableBackread(1041380730)
    DisableAsset(Assets.AEG099_320_9000)
    CommonFunc_90005251(0, character=Characters.GodrickFootSoldier, radius=100.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GodrickSoldier, radius=25.0, seconds=0.0, animation_id=1704)


@RestartOnRest(1041382200)
def Event_1041382200(_, character: uint, region: uint, owner_entity: uint):
    """Event 1041382200"""
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableCharacter(character)
    CreateProjectileOwner(entity=owner_entity)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
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
    
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    PlaySoundEffect(region, 407008100, sound_type=SoundType.c_CharacterMotion)
    Wait(1.0)
    OR_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_7.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_11.Add(CharacterOutsideRegion(character=PLAYER, region=region))
    AND_11.Add(OR_7)
    GotoIfConditionTrue(Label.L0, input_condition=AND_11)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.5)
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=PLAYER,
        dummy_id=900,
        behavior_id=100920,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    ForceAnimation(character, 20011)
    AddSpecialEffect(character, 8090)
    Wait(5.0)
    RemoveSpecialEffect(character, 8090)


@RestartOnRest(1041382650)
def Event_1041382650(
    _,
    tutorial_param_id: int,
    flag: Flag | int,
    tutorial_param_id_1: int,
    flag_1: Flag | int,
    flag_2: Flag | int,
    flag_3: Flag | int,
):
    """Event 1041382650"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NW_SE))
    AND_1.Add(PlayerDoesNotHaveGood(9109))
    OR_1.Add(Multiplayer())
    OR_1.Add(MultiplayerPending())
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 100690))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9640))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id_1, unk_4_5=True, unk_5_6=True)
    if FlagEnabled(flag_2):
        return
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9109, flag=flag, bit_count=1)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9137, flag=flag_1, bit_count=1)
    EnableFlag(flag_2)
    EnableFlag(flag_3)


@RestartOnRest(1041383700)
def Event_1041383700(_, character: Character | int):
    """Event 1041383700"""
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1041383701)
def Event_1041383701(_, entity: uint):
    """Event 1041383701"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(3223):
        return
    
    MAIN.Await(FlagEnabled(3221))
    
    ForceAnimation(entity, 20015)


@RestartOnRest(1041383710)
def Event_1041383710(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int):
    """Event 1041383710"""
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    SkipLinesIfConditionFalse(2, OR_1)
    DisableNetworkFlag(flag_2)
    End()
    EnableNetworkFlag(flag_2)
    OR_2.Add(FlagDisabled(flag))
    OR_2.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_2)
    
    DisableNetworkFlag(flag_2)
    End()


@RestartOnRest(1041383730)
def Event_1041383730(_, character: uint):
    """Event 1041383730"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3705)
    DisableCharacter(character)
    DisableBackread(character)
    EnableAsset(Assets.AEG099_139_9000)
    DisableAsset(Assets.AEG099_320_9000)
    DeleteVFX(120)
    if FlagDisabled(1041389412):
        EnableNetworkFlag(1041389414)
    
    MAIN.Await(FlagEnabled(3705))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3700)
    GotoIfFlagEnabled(Label.L2, flag=3701)
    GotoIfFlagEnabled(Label.L4, flag=3703)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    EnableInvincibility(character)
    DisableAsset(Assets.AEG099_139_9000)
    EnableAsset(Assets.AEG099_320_9000)
    ForceAnimation(character, 90100)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    DisableAsset(Assets.AEG099_139_9000)
    EnableAsset(Assets.AEG099_320_9000)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    DisableAsset(Assets.AEG099_320_9000)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3705))
    
    Restart()


@RestartOnRest(1041383731)
def Event_1041383731():
    """Event 1041383731"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(3705):
        return
    GotoIfFlagDisabled(Label.L1, flag=1041382731)
    GotoIfFlagDisabled(Label.L2, flag=1041382732)
    GotoIfFlagDisabled(Label.L3, flag=1041382733)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=1041381700, attacker=ALL_PLAYERS))
    AwaitConditionTrue(AND_1)
    EnableNetworkFlag(1041382736)
    Wait(20.0)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=1041381700, attacker=ALL_PLAYERS))
    AwaitConditionTrue(AND_2)
    EnableNetworkFlag(1041382737)
    Wait(15.0)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_3.Add(AttackedWithDamageType(attacked_entity=1041381700, attacker=ALL_PLAYERS))
    AwaitConditionTrue(AND_3)
    EnableNetworkFlag(1041382738)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Restart()


@RestartOnRest(1041383750)
def Event_1041383750(_, character: Character | int):
    """Event 1041383750"""
    WaitFrames(frames=1)
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(1041383760)
def Event_1041383760(_, flag: Flag | int, other_entity: uint, flag_1: Flag | int):
    """Event 1041383760"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372701)
    OR_1.Add(FlagDisabled(flag))
    OR_1.Add(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(1042372701)
    Restart()


@RestartOnRest(1041383761)
def Event_1041383761(_, other_entity: uint, flag: Flag | int):
    """Event 1041383761"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(4680):
        return
    
    MAIN.Await(FlagEnabled(4680))
    
    AND_2.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1041383762)
def Event_1041383762(_, other_entity: uint, flag: Flag | int):
    """Event 1041383762"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379203):
        return
    
    MAIN.Await(FlagEnabled(1042379203))
    
    AND_2.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    SkipLinesIfConditionFalse(1, AND_2)
    EnableFlag(flag)
    End()


@RestartOnRest(1041383763)
def Event_1041383763(_, other_entity: uint, flag: Flag | int):
    """Event 1041383763"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1042379207):
        return
    AND_1.Add(EntityWithinDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1042372702)
    
    MAIN.Await(EntityBeyondDistance(entity=ALL_PLAYERS, other_entity=other_entity, radius=5.0))
    
    DisableFlag(1042372702)
    Restart()
