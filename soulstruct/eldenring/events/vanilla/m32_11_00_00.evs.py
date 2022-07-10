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
    RegisterGrace(grace_flag=32110000, obj=32111950, unknown=5.0)
    Event_32112800()
    Event_32112810()
    Event_32112811()
    Event_32112849()
    Event_32112820(1, character=32110801, destination=32111821)
    Event_32112820(2, character=32110802, destination=32111822)
    Event_32112820(3, character=32110803, destination=32111823)
    Event_32112820(4, character=32110804, destination=32111824)
    Event_32112820(5, character=32110805, destination=32111825)
    Event_32112820(6, character=32110806, destination=32111826)
    Event_32112820(7, character=32110807, destination=32111827)
    Event_32112820(8, character=32110808, destination=32111828)
    Event_32112830(1, character=32110801)
    Event_32112830(2, character=32110802)
    Event_32112830(3, character=32110803)
    Event_32112830(4, character=32110804)
    Event_32112830(5, character=32110805)
    Event_32112830(6, character=32110806)
    Event_32112830(7, character=32110807)
    Event_32112830(8, character=32110808)
    Event_32112510()
    RunCommonEvent(
        0,
        90005501,
        args=(32110510, 32110511, 0, 32111510, 32111511, 32111512, 32110512),
        arg_types="IIIIIII",
    )
    Event_32112580()
    RunCommonEvent(0, 90005511, args=(32110560, 32111550, 32113560, 257013, 0), arg_types="IIIiI")
    RunCommonEvent(0, 90005512, args=(32110560, 32112550, 32112551), arg_types="III")
    RunCommonEvent(
        0,
        90005646,
        args=(32110800, 32112840, 32112841, 32111840, 32112840, 32, 11, 0, 0),
        arg_types="IIIIIBBbb",
    )
    RunCommonEvent(0, 900005610, args=(32111680, 100, 800, 0), arg_types="IiiI")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_32110519()
    RunCommonEvent(0, 90005200, args=(32110200, 30007, 20007, 32112200, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32110201, 30007, 20007, 32112200, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32110205, 30007, 20007, 32112205, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32110206, 30007, 20007, 32112206, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(32110206, 32112206, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(32110207, 30007, 20007, 32112206, 0.5, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005200, args=(32110208, 30007, 20007, 32112208, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(32110208, 32112208, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(32110209, 30007, 20007, 32112209, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(
        0,
        90005200,
        args=(32110210, 30007, 20007, 32112209, 0.20000000298023224, 0, 0, 0, 0),
        arg_types="IiiIfIIII",
    )
    RunCommonEvent(0, 90005250, args=(32110210, 32112209, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005201, args=(32110211, 30006, 20006, 5.0, 0.0, 0, 1, 0, 0), arg_types="IiiffIIII")
    RunCommonEvent(0, 90005200, args=(32110215, 30007, 20007, 32112215, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(32110215, 32112215, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005200, args=(32110216, 30007, 20007, 32112216, 0.0, 0, 0, 0, 0), arg_types="IiiIfIIII")
    RunCommonEvent(0, 90005250, args=(32110300, 32112300, 0.0, -1), arg_types="IIfi")
    RunCommonEvent(0, 90005250, args=(32110301, 32112301, 0.0, -1), arg_types="IIfi")


@NeverRestart(32112510)
def Event_32112510():
    """Event 32112510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            32110510,
            32110511,
            0,
            32111510,
            32111511,
            32113511,
            32111512,
            32113512,
            32112511,
            32112512,
            32110512,
            32110513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(32110519)
def Event_32110519():
    """Event 32110519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(32110510)
    DisableThisSlotFlag()


@NeverRestart(32112580)
def Event_32112580():
    """Event 32112580"""
    RegisterLadder(start_climbing_flag=32110580, stop_climbing_flag=32110581, obj=32111580)
    RegisterLadder(start_climbing_flag=32110582, stop_climbing_flag=32110583, obj=32111582)
    RegisterLadder(start_climbing_flag=32110584, stop_climbing_flag=32110585, obj=32111584)


@RestartOnRest(32112800)
def Event_32112800():
    """Event 32112800"""
    EndIfFlagEnabled(32110800)
    IfHealthValueLessThanOrEqual(MAIN, 32110800, value=0)
    Wait(4.0)
    PlaySoundEffect(32048000, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 32110800)
    KillBossAndDisplayBanner(character=32110800, banner_type=BannerType.DutyFulfilled)
    EnableFlag(32110800)
    EnableFlag(9268)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61268)


@RestartOnRest(32112810)
def Event_32112810():
    """Event 32112810"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(32110800)
    DisableAnimations(32110800)
    Kill(32110800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(32110800)
    SetCharacterEventTarget(32110800, region=32110810)
    SetBackreadStateAlternate(32110810, True)
    GotoIfFlagEnabled(Label.L1, flag=32110801)
    DisableCharacter(32110800)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=32112801)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=32110800, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(32110801)
    EnableCharacter(32110800)
    ForceAnimation(32110800, 20016, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfFlagEnabled(AND_2, 32112805)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=32112800)
    IfConditionTrue(MAIN, input_condition=AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(32110800)
    SetNetworkUpdateRate(32110800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(32110800, name=904620320)


@RestartOnRest(32112811)
def Event_32112811():
    """Event 32112811"""
    EndIfFlagEnabled(32110800)
    IfHealthLessThanOrEqual(AND_1, 32110800, value=0.6000000238418579)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableFlag(32112802)


@RestartOnRest(32112820)
def Event_32112820(_, character: uint, destination: uint):
    """Event 32112820"""
    IfCharacterHasSpecialEffect(MAIN, character, 16714)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Object,
        model_point=100,
        copy_draw_parent=character,
    )
    Wait(1.0)
    CancelSpecialEffect(character, 16714)
    Restart()


@RestartOnRest(32112830)
def Event_32112830(_, character: uint):
    """Event 32112830"""
    GotoIfFlagDisabled(Label.L0, flag=32110800)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IfCharacterDoesNotHaveSpecialEffect(AND_1, character, 5038)
    IfCharacterDead(AND_1, 32110800)
    IfConditionTrue(MAIN, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)


@RestartOnRest(32112849)
def Event_32112849():
    """Event 32112849"""
    RunCommonEvent(
        0,
        9005800,
        args=(32110800, 32111800, 32112800, 32112805, 32115800, 10000, 32110801, 32112801),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(0, 9005801, args=(32110800, 32111800, 32112800, 32112805, 32112806, 10000), arg_types="IIIIIi")
    RunCommonEvent(0, 9005811, args=(32110800, 32111800, 7, 32110801), arg_types="IIiI")
    RunCommonEvent(0, 9005822, args=(32110800, 920700, 32112805, 32112806, 0, 32112802, 0, 0), arg_types="IiIIIIii")
