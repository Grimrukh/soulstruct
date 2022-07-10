"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1044312200(0, character=1044310200, region=1044312200)
    Event_1044312200(1, character=1044310201, region=1044312200)
    Event_1044312200(2, character=1044310202, region=1044312200)
    Event_1044312200(3, character=1044310203, region=1044312200)
    Event_1044312340()
    RunCommonEvent(0, 90005300, args=(1044310350, 1044310350, 0, 0.0, 0), arg_types="IIifi")
    RunCommonEvent(0, 90005550, args=(1044310200, 1044311200, 44313200), arg_types="III")
    RunCommonEvent(0, 90005631, args=(1044311640, 61012), arg_types="Ii")


@RestartOnRest(1044312200)
def Event_1044312200(_, character: uint, region: uint):
    """Event 1044312200"""
    IfCharacterDead(AND_1, character)
    EndIfConditionTrue(input_condition=AND_1)
    IfCharacterInsideRegion(MAIN, character=PLAYER, region=region)
    AddSpecialEffect(character, 14200)


@RestartOnRest(1044312210)
def Event_1044312210(_, character: uint):
    """Event 1044312210"""
    Kill(character)
    End()


@RestartOnRest(1044312340)
def Event_1044312340():
    """Event 1044312340"""
    ReturnIfFlagState(EventReturnType.End, FlagSetting.On, FlagType.RelativeToThisEventSlot, 1044310200)
    DisableAI(1044310340)
    IfCharacterType(AND_9, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterHasSpecialEffect(AND_9, PLAYER, 3710)
    IfConditionTrue(OR_1, input_condition=AND_9)
    IfCharacterHuman(OR_1, PLAYER)
    IfCharacterHollow(OR_1, PLAYER)
    IfCharacterWhitePhantom(OR_1, PLAYER)
    IfEntityWithinDistance(AND_1, entity=PLAYER, other_entity=1044310340, radius=0.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfAttackedWithDamageType(OR_2, attacked_entity=1044310340, attacker=0)
    IfFlagEnabled(OR_2, 1044310200)
    IfConditionTrue(OR_2, input_condition=AND_1)
    IfConditionTrue(MAIN, input_condition=OR_2)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 1044310200, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(0.0)
    SkipLinesIfValueEqual(1, left=1700, right=-1)
    ForceAnimation(1044310340, 1700, loop=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(1044310340)


@RestartOnRest(1044312350)
def Event_1044312350():
    """Event 1044312350"""
    EndIfFlagEnabled(1044310350)
    DisableHealthBar(1044310350)
    AddSpecialEffect(1044310350, 12189)
    Wait(3.0)
    CancelSpecialEffect(1044310350, 12189)
    EnableHealthBar(1044310350)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    RunCommonEvent(0, 90005485, args=(1044310350,))
    RunCommonEvent(0, 90005251, args=(1044310350, 340.0, 0.0, -1), arg_types="Iffi")
    Event_1044312350()
