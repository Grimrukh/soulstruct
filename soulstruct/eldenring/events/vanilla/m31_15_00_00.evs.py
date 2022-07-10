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
    RegisterGrace(grace_flag=31150000, obj=31151950, unknown=5.0)
    RunCommonEvent(0, 90005250, args=(31155800, 31152500, 0.0, 0), arg_types="IIfi")
    Event_31152800()
    Event_31152810()
    Event_31152820(0, character=31150800)
    Event_31152820(1, character=31150801)
    Event_31152849()
    Event_31152816()
    Event_31152830(0, flag=31150815, character=31150100)
    Event_31152811()
    RunCommonEvent(
        0,
        90005780,
        args=(31150800, 31152160, 31152161, 31150710, 20, 31152701, 31159250, 1, 0),
        arg_types="IIIIiIIBi",
    )
    RunCommonEvent(0, 90005781, args=(31150800, 31152160, 31152161, 31150710), arg_types="IIII")
    Event_31152825(
        0,
        flag=31152160,
        region=31152805,
        character=31150710,
        target_entity=31152500,
        region_1=31152809,
        animation=0
    )
    RunCommonEvent(
        0,
        90005646,
        args=(31150800, 31152840, 31152841, 31151840, 31152840, 31, 15, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 90005702, args=(31150700, 3943, 3940, 3944), arg_types="IIII")
    Event_31153700(0, character=31150700)
    Event_31153701(0, 30.0)
    Event_31153710()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(31150700)
    RunCommonEvent(0, 90005250, args=(31150800, 31152800, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(31150801, 31152800, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005251, args=(31150213, 7.0, 0.0, 0), arg_types="Iffi")
    RunCommonEvent(0, 90005211, args=(31150217, 30000, 20000, 31152217, 2.0, 0.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005211, args=(31150230, 30001, 20001, 31152217, 2.0, 1.0, 0, 0, 0, 0), arg_types="IiiIffIIII")
    RunCommonEvent(0, 90005261, args=(31150219, 31152219, 2.0, 1.0, 0), arg_types="IIffi")
    RunCommonEvent(0, 90005261, args=(31150220, 31152219, 2.0, 0.0, 0), arg_types="IIffi")
    Event_31152570()


@RestartOnRest(31152570)
def Event_31152570():
    """Event 31152570"""
    WaitFramesAfterCutscene(frames=1)
    EndIfFlagEnabled(31152570)
    DisableObject(31151700)
    DeleteObjectVFX(31151700)
    SkipLinesIfFlagDisabled(1, 3946)
    EnableObject(31151700)


@RestartOnRest(31152650)
def Event_31152650(_, tutorial_param_id: int, flag: uint, flag_1: uint):
    """Event 31152650"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(700690)
    IfFlagEnabled(AND_1, flag_1)
    IfFlagDisabled(AND_1, 700690)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(flag)
    Wait(1.0)
    DisplayTutorialMessage(tutorial_param_id=tutorial_param_id, unk_4_5=True, unk_5_6=True)
    GivePlayerItemAmountSpecifiedByFlagValue(item_type=ItemType.Good, item=9126, flag=flag, bit_count=1)
    EnableFlag(700690)


@RestartOnRest(31152800)
def Event_31152800():
    """Event 31152800"""
    EndIfFlagEnabled(31150800)
    IfCharacterDead(AND_2, 31150800)
    IfCharacterDead(AND_2, 31150801)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(2.0)
    PlaySoundEffect(31150800, 888880000, sound_type=SoundType.s_SFX)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=31152810, unk_8_12=1)
    TriggerAISound(ai_sound_param_id=4132, anchor_entity=31152811, unk_8_12=1)
    KillBossAndDisplayBanner(character=31150800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(31150800)
    EnableFlag(9234)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61234)
    Wait(5.0)
    AwardItemLot(20340, host_only=True)
    End()


@RestartOnRest(31152810)
def Event_31152810():
    """Event 31152810"""
    GotoIfFlagDisabled(Label.L0, flag=31150800)
    DisableCharacter(31150800)
    DisableAnimations(31150800)
    Kill(31150800)
    Kill(31155800)
    DisableCharacter(31150801)
    DisableAnimations(31150801)
    Kill(31150801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=31150815)
    DisableCharacter(31150800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31152800)
    IfCharacterAlive(AND_1, 31150800)
    IfCharacterBackreadEnabled(AND_1, 31150800)
    IfPlayerInOwnWorld(AND_2)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=31152800)
    IfCharacterAlive(AND_2, 31150801)
    IfCharacterBackreadEnabled(AND_2, 31150801)
    IfAttackedWithDamageType(OR_1, attacked_entity=31150800, attacker=PLAYER)
    IfAttackedWithDamageType(OR_1, attacked_entity=31150801, attacker=PLAYER)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(31150815)
    EnableCharacter(31150800)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_1, 31152805)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=31152800)
    IfAttackedWithDamageType(OR_1, attacked_entity=31150800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetNetworkUpdateRate(31150800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31150800, name=904120310)
    SetNetworkUpdateRate(31150801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31150801, name=904120311, bar_slot=1)
    EnableFlag(31152815)
    EnableNetworkFlag(31152805)
    BanishInvaders(unknown=0)
    CancelSpecialEffect(31155200, 8081)


@RestartOnRest(31152816)
def Event_31152816():
    """Event 31152816"""
    IfFlagEnabled(OR_1, 31150815)
    IfFlagEnabled(OR_1, 31150800)
    EndIfConditionTrue(input_condition=OR_1)
    IfHasAIStatus(OR_2, 31150801, ai_status=AIStatusType.Battle)
    IfHasAIStatus(OR_2, 31150800, ai_status=AIStatusType.Battle)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkUpdateRate(31150800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31150800, name=904120310)
    SetNetworkUpdateRate(31150801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(31150801, name=904120311, bar_slot=1)
    EnableFlag(31152815)
    CancelSpecialEffect(31155200, 8081)
    SetAIParamID(0, ai_param_id=0)


@RestartOnRest(31152811)
def Event_31152811():
    """Event 31152811"""
    EndIfFlagEnabled(31150800)
    IfCharacterDead(OR_15, 31150800)
    IfCharacterDead(OR_15, 31150801)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableFlag(31152842)


@RestartOnRest(31152820)
def Event_31152820(_, character: uint):
    """Event 31152820"""
    EndIfFlagEnabled(31150800)
    IfCharacterHasSpecialEffect(AND_1, character, 4306)
    IfConditionTrue(MAIN, input_condition=AND_1)
    AddSpecialEffect(character, 4305)


@NeverRestart(31152825)
def Event_31152825(_, flag: uint, region: uint, character: uint, target_entity: uint, region_1: uint, animation: int):
    """Event 31152825"""
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(AND_1, flag)
    IfFlagEnabled(AND_1, region)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableMapCollision(collision=31151835)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    SetEventPoint(character, region=region_1, reaction_range=0.0)
    IfTimeElapsed(OR_15, seconds=4.0)
    IfConditionTrue(OR_14, input_condition=OR_15)
    IfCharacterInsideRegion(OR_14, character=character, region=region_1)
    IfConditionTrue(MAIN, input_condition=OR_14)
    RestartIfFinishedConditionTrue(input_condition=OR_15)
    SkipLinesIfValueEqual(2, left=animation, right=0)
    RotateToFaceEntity(character, target_entity, animation=animation, wait_for_completion=True)
    SkipLines(1)
    RotateToFaceEntity(character, target_entity, animation=60060, wait_for_completion=True)
    IfTimeElapsed(OR_4, seconds=3.0)
    IfConditionTrue(OR_5, input_condition=OR_4)
    IfCharacterInsideRegion(OR_5, character=character, region=region)
    IfConditionTrue(MAIN, input_condition=OR_5)
    RestartIfFinishedConditionTrue(input_condition=OR_4)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(2.0)
    EnableMapCollision(collision=31151835)


@RestartOnRest(31152830)
def Event_31152830(_, flag: uint, character: uint):
    """Event 31152830"""
    EndIfFlagEnabled(flag)
    AddSpecialEffect(character, 9531)
    AwaitFlagEnabled(flag=flag)
    AddSpecialEffect(character, 9532)


@RestartOnRest(31152849)
def Event_31152849():
    """Event 31152849"""
    RunCommonEvent(
        0,
        9005800,
        args=(31150800, 31151800, 31152804, 31152805, 31155800, 10000, 31150815, 31152500),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(31150800, 31151800, 31152804, 31152805, 31152806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(31150800, 31151800, 3, 31150815), arg_types="IIiI")
    RunCommonEvent(0, 9005812, args=(31150800, 31151801, 3, 31150815, 806760), arg_types="IIiIi")
    RunCommonEvent(
        0,
        9005822,
        args=(31150800, 931000, 31152805, 31152806, 31152815, 31152842, 0, 0),
        arg_types="IiIIIIii",
    )


@RestartOnRest(31153700)
def Event_31153700(_, character: uint):
    """Event 31153700"""
    WaitFrames(frames=1)
    DisableFlag(31159200)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    IfFlagEnabled(AND_1, 3940)
    IfFlagEnabled(AND_1, 1043379353)
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(1043379353)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    IfFlagEnabled(OR_1, 3946)
    GotoIfConditionFalse(Label.L20, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L1, flag=3940)
    GotoIfFlagEnabled(Label.L2, flag=3941)
    GotoIfFlagEnabled(Label.L3, flag=3942)
    GotoIfFlagEnabled(Label.L4, flag=3943)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(character)
    EnableCharacter(character)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 930020, unknown2=1.0)
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
    IfFlagEnabled(MAIN, 31159200)
    Restart()


@RestartOnRest(31153701)
def Event_31153701(_, seconds: float):
    """Event 31153701"""
    WaitFrames(frames=1)
    EndIfPlayerNotInOwnWorld()
    EndIfFlagDisabled(3946)
    EndIfFlagEnabled(31159205)
    IfFlagEnabled(MAIN, 31152700)
    Wait(seconds)
    DisableFlag(31152700)
    Restart()


@RestartOnRest(31153710)
def Event_31153710():
    """Event 31153710"""
    EndIfPlayerNotInOwnWorld()
    DisableFlag(31159250)
    EndIfFlagEnabled(31150800)
    EndIfFlagEnabled(7602)
    EnableFlag(31159250)
    End()
