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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_44_31_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_1044312200(0, character=Characters.SpiritJellyfish0, region=1044312200)
    Event_1044312200(1, character=Characters.SpiritJellyfish1, region=1044312200)
    Event_1044312200(2, character=Characters.SpiritJellyfish2, region=1044312200)
    Event_1044312200(3, character=Characters.SpiritJellyfish3, region=1044312200)
    Event_1044312340()
    CommonFunc_90005300(
        0,
        flag=1044310350,
        character=Characters.GuardianGolem,
        item_lot_param_id=0,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005550(0, flag=1044310200, asset=1044311200, obj_act_id=44313200)
    CommonFunc_90005631(0, 1044311640, 61012)


@RestartOnRest(1044312200)
def Event_1044312200(_, character: uint, region: uint):
    """Event 1044312200"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
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
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1044310340, radius=0.0))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=1044310340, attacker=0))
    OR_2.Add(FlagEnabled(1044310200))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 1044310200, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(0.0)
    if ValueNotEqual(left=1700, right=-1):
        ForceAnimation(1044310340, 1700, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(1044310340)


@RestartOnRest(1044312350)
def Event_1044312350():
    """Event 1044312350"""
    if FlagEnabled(1044310350):
        return
    DisableHealthBar(Characters.GuardianGolem)
    AddSpecialEffect(Characters.GuardianGolem, 12189)
    Wait(3.0)
    RemoveSpecialEffect(Characters.GuardianGolem, 12189)
    EnableHealthBar(Characters.GuardianGolem)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005485(0, character=Characters.GuardianGolem)
    CommonFunc_90005251(0, 1044310350, 340.0, 0.0, -1)
    Event_1044312350()
