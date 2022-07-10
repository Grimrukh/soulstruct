"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(0, 90005261, args=(1046360250, 1046362250, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1046360240, 1046362240, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(1046360300, 1046362300, 10.0, 0.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 900005610, args=(1046361650, 100, 800, 0), arg_types="IiiI")
    Event_1046362260(0, attacker__character=1046365260, region=1046362260)
    Event_1046362203()
    Event_1046362300()
    Event_1046362310()
    RunCommonEvent(0, 90005704, args=(1046360700, 3581, 3580, 1046369201, 3), arg_types="IIIIi")
    RunCommonEvent(0, 90005703, args=(1046360700, 3581, 3582, 1046369201, 3581, 3580, 3583, -1), arg_types="IIIIIIIi")
    RunCommonEvent(0, 90005702, args=(1046360700, 3583, 3580, 3583), arg_types="IIII")
    Event_1046360700(0, 1046360700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1046360700)
    Event_1046362220()


@NeverRestart(1046362203)
def Event_1046362203():
    """Event 1046362203"""
    RegisterLadder(start_climbing_flag=46360580, stop_climbing_flag=46360851, obj=1046361580)


@RestartOnRest(1046362220)
def Event_1046362220():
    """Event 1046362220"""
    DropMandatoryTreasure(1046365120)


@RestartOnRest(1046362260)
def Event_1046362260(_, attacker__character: uint, region: uint):
    """Event 1046362260"""
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)
    AddSpecialEffect(attacker__character, 4802)
    EndIfFlagEnabled(1046362260)
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5650)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=PLAYER)
    IfAttackedWithDamageType(OR_2, attacked_entity=attacker__character, attacker=35000)
    IfAttackedWithDamageType(OR_2, attacked_entity=35000, attacker=attacker__character)
    IfEntityWithinDistance(OR_2, entity=PLAYER, other_entity=attacker__character, radius=10.0)
    IfEntityWithinDistance(OR_2, entity=35000, other_entity=attacker__character, radius=10.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=region)
    IfCharacterInsideRegion(OR_2, character=35000, region=region)
    IfConditionTrue(AND_1, input_condition=OR_2)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableNetworkFlag(1046362260)
    CancelSpecialEffect(attacker__character, 4800)
    CancelSpecialEffect(attacker__character, 5650)


@RestartOnRest(1046362300)
def Event_1046362300():
    """Event 1046362300"""
    IfFlagEnabled(AND_1, 1046360705)
    IfFlagDisabled(AND_1, 1046362320)
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
    IfPlayerInOwnWorld(AND_2)
    IfCharacterDead(AND_2, 1046360250)
    IfConditionTrue(MAIN, input_condition=AND_2)
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
    IfFlagEnabled(AND_1, 1046360706)
    IfFlagDisabled(AND_1, 1046362330)
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
    EndIfPlayerNotInOwnWorld()
    IfPlayerHasGood(AND_1, 9500)
    IfPlayerInOwnWorld(AND_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=False)


@RestartOnRest(1046360700)
def Event_1046360700(_, character: uint):
    """Event 1046360700"""
    WaitFrames(frames=1)
    DisableNetworkSync()
    GotoIfPlayerNotInOwnWorld(Label.L19)
    IfFlagEnabled(AND_1, 3580)
    IfFlagEnabled(AND_1, 1045389203)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1045389203)

    # --- Label 19 --- #
    DefineLabel(19)
    GotoIfFlagEnabled(Label.L6, flag=3586)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(MAIN, 3586)
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
    ForceAnimation(character, 90101, unknown2=1.0)
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
    IfFlagDisabled(MAIN, 3586)
    Restart()
