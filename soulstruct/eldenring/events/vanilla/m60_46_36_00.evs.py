"""
East Limgrave (SE) (SW)

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
from .entities.m60_46_36_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005261(
        0,
        character=Characters.GodrickKnight,
        region=1046362250,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Commoner, region=1046362240, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(
        0,
        character=Characters.MadPumpkinHead,
        region=1046362300,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9003, vfx_id=100, model_point=800, right=0)
    Event_1046362260(0, attacker__character=1046365260, region=1046362260)
    Event_1046362203()
    Event_1046362300()
    Event_1046362310()
    CommonFunc_90005704(0, attacked_entity=Characters.KennethHaight, flag=3581, flag_1=3580, flag_2=1046369201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.KennethHaight,
        flag=3581,
        flag_1=3582,
        flag_2=1046369201,
        flag_3=3581,
        first_flag=3580,
        last_flag=3583,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.KennethHaight, flag=3583, first_flag=3580, last_flag=3583)
    Event_1046360700(0, 1046360700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.KennethHaight)
    Event_1046362220()


@NeverRestart(1046362203)
def Event_1046362203():
    """Event 1046362203"""
    RegisterLadder(start_climbing_flag=46360580, stop_climbing_flag=46360851, asset=Assets.AEG030_902_2001)


@RestartOnRest(1046362220)
def Event_1046362220():
    """Event 1046362220"""
    DropMandatoryTreasure(1046365120)


@RestartOnRest(1046362260)
def Event_1046362260(_, attacker__character: uint, region: uint):
    """Event 1046362260"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1046362260):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
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
    
    EnableNetworkFlag(1046362260)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5650)


@RestartOnRest(1046362300)
def Event_1046362300():
    """Event 1046362300"""
    AND_1.Add(FlagEnabled(1046360705))
    AND_1.Add(FlagDisabled(1046362320))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableNetworkFlag(1046360320)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(1046362320)
    GotoIfFlagDisabled(Label.L1, flag=1046360320)
    DisableCharacter(1046365300)
    DisableAnimations(1046365300)
    DisableAI(1046365300)
    EnableCharacterCollision(1046365300)
    DisableGravity(1046365300)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDead(Characters.GodrickKnight))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(1046360705)
    AwardItemLot(1046360700, host_only=True)


@RestartOnRest(1046362310)
def Event_1046362310():
    """Event 1046362310"""
    DisableCharacter(1046365310)
    DisableAnimations(1046365310)
    DisableAI(1046365310)
    EnableCharacterCollision(1046365310)
    DisableGravity(1046365310)
    AND_1.Add(FlagEnabled(1046360706))
    AND_1.Add(FlagDisabled(1046362330))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableNetworkFlag(1046360330)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(1046362330)
    GotoIfFlagDisabled(Label.L1, flag=1046360330)
    DisableCharacter(1046365300)
    DisableAnimations(1046365300)
    DisableAI(1046365300)
    EnableCharacterCollision(1046365300)
    DisableGravity(1046365300)
    EnableCharacter(1046365310)
    EnableAnimations(1046365310)
    EnableAI(1046365310)
    DisableCharacterCollision(1046365310)
    EnableGravity(1046365310)
    End()

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(1046362620)
def Event_1046362620(_, tutorial_param_id: int, flag: uint):
    """Event 1046362620"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerHasGood(9500))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(1046360700)
def Event_1046360700(_, character: uint):
    """Event 1046360700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    AND_1.Add(FlagEnabled(3580))
    AND_1.Add(FlagEnabled(1045389203))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1045389203)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3586)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3586))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=3580)
    GotoIfFlagEnabled(Label.L2, flag=3581)
    GotoIfFlagEnabled(Label.L4, flag=3583)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90101)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(character)
    EnableBackread(character)
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
    
    MAIN.Await(FlagDisabled(3586))
    
    Restart()
