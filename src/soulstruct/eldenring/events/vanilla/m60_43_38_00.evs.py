"""
West Limgrave (NE) (SE)

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
from soulstruct.eldenring.game_types import *
from .enums.m60_43_38_00_enums import *
from .enums.m60_43_37_00_enums import Characters as m60_43_37_00_Characters


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043380000, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, dummy_id=100, vfx_id=800, right=1043388540)
    CommonFunc_90005683(0, flag=62105, asset=Assets.AEG099_055_1000, dummy_id=208, flag_1=78194, flag_2=78194)
    CommonFunc_90005251(0, character=Characters.KaidenSellsword, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005460(0, character=Characters.GiantOctopus)
    CommonFunc_90005461(0, character=Characters.GiantOctopus)
    CommonFunc_90005462(0, character=Characters.GiantOctopus)
    Event_1043382270()
    Event_1043382270(slot=1)
    Event_1043383700(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        attacker=m60_43_37_00_Characters.BloodyFingerNerijus,
    )
    Event_1043383701(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        character_1=1043380701,
        region=1043372703,
        region_1=1043382701,
        destination=1043372705,
        destination_1=1043382702,
        destination_2=1043372708,
    )
    Event_1043383702(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1043383703(0, character=Characters.YuraHunterofBloodyFingers, flag=1043372712, distance=160.0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.YuraHunterofBloodyFingers)


@RestartOnRest(1043382270)
def Event_1043382270():
    """Event 1043382270"""
    DisableNetworkSync()
    CreateProjectileOwner(entity=Characters.Dummy)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1043382270))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=10.0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=Characters.Dummy,
            source_entity=1043382271,
            dummy_id=900,
            behavior_id=802101070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    Wait(1.0)
    Restart()


@RestartOnRest(1043382650)
def Event_1043382650(_, tutorial_param_id: int, flag: Flag | int, flag_1: Flag | int):
    """Event 1043382650"""
    if Multiplayer():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(PlayerHasGood(215000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(240000, including_storage=True))
    OR_1.Add(PlayerHasGood(243000, including_storage=True))
    OR_1.Add(PlayerHasGood(234000, including_storage=True))
    OR_1.Add(PlayerHasGood(244000, including_storage=True))
    OR_1.Add(PlayerHasGood(236000, including_storage=True))
    OR_1.Add(PlayerHasGood(232000, including_storage=True))
    OR_1.Add(PlayerHasGood(212000, including_storage=True))
    OR_1.Add(PlayerHasGood(241000, including_storage=True))
    OR_1.Add(PlayerHasGood(213000, including_storage=True))
    OR_1.Add(PlayerHasGood(233000, including_storage=True))
    OR_1.Add(PlayerHasGood(245000, including_storage=True))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9530))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(Singleplayer())
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_NE_SE))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(flag):
        return
    EnableFlag(flag)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9127, flag=flag_1, bit_count=1)


@RestartOnRest(1043383700)
def Event_1043383700(_, character: Character | int, attacker: Character | int):
    """Event 1043383700"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagDisabled(3626))
    OR_1.Add(FlagDisabled(3620))
    OR_1.Add(AND_1)
    if OR_1:
        return
    GotoIfFlagDisabled(Label.L1, flag=1043372714)
    GotoIfFlagEnabled(Label.L2, flag=1043372714)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=PLAYER, attacker=attacker))
    
    MAIN.Await(OR_2)
    
    Wait(10.0)
    if FlagDisabled(1043372714):
        return
    AND_2.Add(FlagDisabled(3625))
    AND_2.Add(FlagDisabled(3626))
    OR_2.Add(FlagDisabled(3620))
    OR_2.Add(AND_2)
    if OR_2:
        return
    EnableFlag(1043372717)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    OR_3.Add(FlagDisabled(1043372714))
    OR_3.Add(CharacterDead(character))
    
    MAIN.Await(OR_3)
    
    EnableFlag(1043372718)
    End()


@RestartOnRest(1043383701)
def Event_1043383701(
    _,
    character: uint,
    character_1: Character | int,
    region: Region | int,
    region_1: Region | int,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
):
    """Event 1043383701"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagDisabled(3626))
    OR_1.Add(FlagDisabled(3620))
    OR_1.Add(AND_1)
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(1043372717))
    
    EnableBackread(character)
    EnableBackread(character_1)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=region)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=region_1)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableCharacter(character_1)
    EnableCharacter(character)
    ForceAnimation(character, 63010)
    AddSpecialEffect(character, 9651)
    SetTeamType(character, TeamType.WhitePhantom)
    DisplayFlashingMessageWithPriority(text=80000, priority=0, should_interrupt=False)
    End()


@RestartOnRest(1043383702)
def Event_1043383702(_, character: Character | int):
    """Event 1043383702"""
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagDisabled(3626))
    OR_1.Add(FlagDisabled(3620))
    OR_1.Add(AND_1)
    if OR_1:
        return
    
    MAIN.Await(FlagEnabled(1043372718))
    
    WaitFrames(frames=1)
    AND_2.Add(CharacterDead(character))
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L2, flag=1043379262)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    DisplayFlashingMessageWithPriority(text=80002, priority=0, should_interrupt=False)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 18677)
    ClearTargetList(character)
    ReplanAI(character)
    DisplayFlashingMessageWithPriority(text=80001, priority=0, should_interrupt=False)
    Wait(10.0)
    DisableBackread(character)
    DisableCharacter(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    SetTeamType(character, TeamType.NoTeam)
    ClearTargetList(character)
    ReplanAI(character)
    Wait(1.0)
    AddSpecialEffect(character, 18677)
    DisplayFlashingMessageWithPriority(text=80003, priority=0, should_interrupt=False)
    Wait(10.0)
    DisableBackread(character)
    DisableCharacter(character)
    End()


@RestartOnRest(1043383703)
def Event_1043383703(_, character: Character | int, flag: Flag | int, distance: float):
    """Event 1043383703"""
    if PlayerNotInOwnWorld():
        return
    SetCharacterTalkRange(character=character, distance=17.0)
    WaitRealFrames(frames=1)
    if FlagDisabled(3620):
        return
    AND_1.Add(FlagDisabled(3625))
    AND_1.Add(FlagDisabled(3626))
    if AND_1:
        return
    if FlagEnabled(1043379262):
        return
    if FlagEnabled(1043372716):
        return
    AND_2.Add(FlagDisabled(1043372713))
    AND_2.Add(FlagEnabled(1043372717))
    
    MAIN.Await(AND_2)
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableNetworkFlag(flag)
    End()
