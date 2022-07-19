"""
West Weeping Peninsula (NE) (NE)

linked:
0
84
156
238

strings:
0: N:\\GR\\data\\Param\\event\\common_macro.emevd
84: N:\\GR\\data\\Param\\event\\common.emevd
156: N:\\GR\\data\\Param\\event\\common_func.emevd
238: N:\\GR\\data\\Param\\event\\m60.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_43_35_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043350000, asset=Assets.AEG099_060_9000)
    Event_1043352270(0, attacker__character=1043355270, region=1043352270)
    Event_1043350652(
        0,
        tutorial_param_id=1520,
        flag=710520,
        tutorial_param_id_1=1770,
        flag_1=710770,
        flag_2=69090,
        flag_3=69370,
    )
    Event_1043353750(0, character=1043350700, character_1=1043350703)
    CommonFunc_90005704(
        0,
        attacked_entity=Characters.YuraHunterofBloodyFingers,
        flag=3621,
        flag_1=3620,
        flag_2=1043359251,
        right=3,
    )
    CommonFunc_90005703(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        flag=3621,
        flag_1=3622,
        flag_2=1043359251,
        flag_3=3621,
        first_flag=3620,
        last_flag=3624,
        right=-1,
    )
    CommonFunc_90005702(
        0,
        character=Characters.YuraHunterofBloodyFingers,
        flag=1043359259,
        first_flag=1043359259,
        last_flag=1043359259,
    )
    Event_1043353710(0, character=Characters.YuraHunterofBloodyFingers)
    Event_1043353711(0, 1043350710)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.YuraHunterofBloodyFingers)
    Event_1043352200()


@RestartOnRest(1043352200)
def Event_1043352200():
    """Event 1043352200"""
    DropMandatoryTreasure(1043355200)


@RestartOnRest(1043352270)
def Event_1043352270(_, attacker__character: uint, region: uint):
    """Event 1043352270"""
    EnableNetworkSync()
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5653)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1043352270):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5653)
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
    
    EnableNetworkFlag(1043352270)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5653)


@RestartOnRest(1043350652)
def Event_1043350652(
    _,
    tutorial_param_id: int,
    flag: uint,
    tutorial_param_id_1: int,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
):
    """Event 1043350652"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(PlayerHasGood(130))
    AND_1.Add(InsideMap(game_map=WEST_WEEPING_PENINSULA_NE_NE))
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


@RestartOnRest(1043353710)
def Event_1043353710(_, character: uint):
    """Event 1043353710"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3620):
        DisableFlag(1043379255)

    # --- Label 10 --- #
    DefineLabel(10)
    OR_1.Add(FlagDisabled(1043369200))
    OR_1.Add(FlagEnabled(1043360800))
    AND_1.Add(FlagEnabled(3626))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L5, input_condition=AND_1)
    DisableCharacter(character)
    DisableBackread(character)
    OR_3.Add(FlagDisabled(1043369200))
    OR_3.Add(FlagEnabled(1043360800))
    AND_3.Add(FlagEnabled(3626))
    AND_3.Add(OR_3)
    
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
    OR_4.Add(FlagDisabled(1043369200))
    OR_4.Add(FlagEnabled(1043360800))
    AND_4.Add(FlagEnabled(3626))
    AND_4.Add(OR_4)
    
    MAIN.Await(not AND_4)
    
    Restart()


@RestartOnRest(1043353711)
def Event_1043353711(_, character: uint):
    """Event 1043353711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1044389209):
        return
    if FlagEnabled(1035469209):
        return
    if FlagEnabled(1039529209):
        return
    GotoIfFlagEnabled(Label.L1, flag=1043359259)
    
    MAIN.Await(FlagEnabled(1043359259))
    
    DisableNetworkConnectedFlagRange(flag_range=(3620, 3624))
    EnableNetworkFlag(3623)
    SaveRequest()
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    if FlagEnabled(3626):
        return
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@RestartOnRest(1043353750)
def Event_1043353750(_, character: uint, character_1: uint):
    """Event 1043353750"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    DisableBackread(character_1)
    DisableCharacter(character_1)
    DisableCharacter(1043350701)
    DisableCharacter(1043350702)
    DisableBackread(1043350701)
    DisableBackread(1043350702)
    DisableAI(1043350701)
    DisableAI(1043350702)
