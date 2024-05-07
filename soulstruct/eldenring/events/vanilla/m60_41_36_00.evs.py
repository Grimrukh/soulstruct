"""
West Limgrave (SW) (SE)

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
from .enums.m60_41_36_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_900005610(0, asset=Assets.AEG003_316_9000, vfx_id=100, dummy_id=800, right=0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus0)
    CommonFunc_90005461(0, character=Characters.GiantOctopus0)
    CommonFunc_90005462(0, character=Characters.GiantOctopus0)
    CommonFunc_90005460(0, character=Characters.GiantOctopus1)
    CommonFunc_90005461(0, character=Characters.GiantOctopus1)
    CommonFunc_90005462(0, character=Characters.GiantOctopus1)
    Event_1041362650(0, tutorial_param_id=1550, flag=710550)
    CommonFunc_90005725(
        0,
        flag=4730,
        flag_1=4731,
        flag_2=4733,
        flag_3=1041369205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1041366700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4731,
        flag_1=4732,
        flag_2=1041369206,
        flag_3=4731,
        first_flag=4730,
        last_flag=4734,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4731, flag_1=4730, flag_2=1041369206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4733, first_flag=4730, last_flag=4734)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4731,
        flag_1=4732,
        flag_2=1041369207,
        flag_3=4731,
        first_flag=4730,
        last_flag=4734,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4731, flag_1=4730, flag_2=1041369207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1041362706, flag_1=1041362707)
    CommonFunc_90005727(
        0,
        flag=4731,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        first_flag=4730,
        last_flag=4733,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    CommonFunc_90005251(0, character=Characters.Troll, radius=80.0, seconds=0.0, animation_id=-1)


@RestartOnRest(1041362650)
def Event_1041362650(_, tutorial_param_id: int, flag: uint):
    """Event 1041362650"""
    if Multiplayer():
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
    AND_1.Add(Singleplayer())
    AND_1.Add(PlayerDoesNotHaveGood(9111, including_storage=True))
    AND_1.Add(InsideMap(game_map=WEST_LIMGRAVE_SW_SE))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if Multiplayer():
        return
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9111, flag=flag, bit_count=1)


@RestartOnRest(1041363700)
def Event_1041363700(_, character: uint, character_1: uint, character_2: uint, asset: uint):
    """Event 1041363700"""
    WaitFrames(frames=1)
    DisableFlag(1041369200)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_10.Add(FlagEnabled(4740))
    AND_10.Add(FlagEnabled(1041369203))
    SkipLinesIfConditionFalse(1, AND_10)
    DisableFlag(1041369203)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    OR_1.Add(FlagEnabled(4745))
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=4740)
    GotoIfFlagEnabled(Label.L2, flag=4741)
    GotoIfFlagEnabled(Label.L4, flag=4743)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    ForceAnimation(character, 30003)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableAsset(asset)
    EnableBackread(character)
    EnableBackread(character_1)
    EnableBackread(character_2)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    DropMandatoryTreasure(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    EnableAsset(asset)
    DisableBackread(character)
    DisableBackread(character_1)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagEnabled(1041369200))
    
    Restart()


@RestartOnRest(1041363706)
def Event_1041363706(_, attacked_entity: uint):
    """Event 1041363706"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=40000))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(1041362701))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1041362708)
    End()


@ContinueOnRest(1041363707)
def Event_1041363707(
    _,
    character: uint,
    first_flag: uint,
    flag: uint,
    flag_1: uint,
    last_flag: uint,
    character_1: uint,
    flag_2: uint,
):
    """Event 1041363707"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(first_flag):
        return
    DisableNetworkFlag(flag_2)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=20000))
    AND_1.Add(HealthValue(character) < 1)
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_3.Add(FlagEnabled(flag_2))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=20000))
    AND_3.Add(HealthValue(character_1) < 1)
    OR_4.Add(OR_3)
    OR_4.Add(AND_3)
    OR_5.Add(OR_2)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    GotoIfFinishedConditionTrue(Label.L5, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(flag_2)
    SetTeamType(character_1, TeamType.HostileNPC)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    SetTeamType(character, TeamType.HostileNPC)
    EnableAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    EnableNetworkFlag(flag)
    SaveRequest()
    if CharacterHasSpecialEffect(character=character, special_effect=9603):
        ForceAnimation(character, 20009)
    Goto(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    WaitFrames(frames=1)
    DisableNetworkFlag(flag_2)
    
    MAIN.Await(FlagEnabled(flag_2))
    
    DisableNetworkFlag(flag_2)
    End()
