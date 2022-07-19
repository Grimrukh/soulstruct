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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_51_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76300, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76300,
        asset=Assets.AEG099_060_9001,
        source_flag=77300,
        value=0,
        flag_2=78300,
        flag_3=78301,
        flag_4=78302,
        flag_5=78303,
        flag_6=78304,
        flag_7=78305,
        flag_8=78306,
        flag_9=78307,
        flag_10=78308,
        flag_11=78309,
    )
    CommonFunc_90005870(0, character=Characters.AncientDragon, name=904510600, npc_threat_level=28)
    CommonFunc_90005860(
        0,
        flag=1037510800,
        left=0,
        character=Characters.AncientDragon,
        left_1=1,
        item_lot__item_lot_param_id=30300,
        seconds=0.0,
    )
    Event_1037512208(0, character=Characters.Omen1, region=1037512208, radius=5.0, seconds=0.0, animation_id=20005)
    CommonFunc_90005251(0, character=1037510200, radius=45.0, seconds=0.0, animation_id=0)
    CommonFunc_90005300(0, flag=1037510210, character=Characters.Scarab0, item_lot_param_id=40224, seconds=0.0, left=0)
    CommonFunc_90005300(0, flag=1037510500, character=Characters.Scarab1, item_lot_param_id=40300, seconds=0.0, left=0)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=39200514)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=39200514)
    CommonFunc_90005771(0, 1037510950, 1037512700)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_1037512350(0, character=Characters.AncientDragon)
    Event_1037512301(0, 1037510800)


@RestartOnRest(1037512208)
def Event_1037512208(_, character: uint, region: uint, radius: float, seconds: float, animation_id: int):
    """Event 1037512208"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
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
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
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
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(seconds)
    ForceAnimation(character, animation_id, loop=True)
    EnableAI(character)


@RestartOnRest(1037512301)
def Event_1037512301(_, character: uint):
    """Event 1037512301"""
    if FlagEnabled(1037510810):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, 14887))
    
    EnableFlag(1037510810)
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@RestartOnRest(1037512350)
def Event_1037512350(_, character: uint):
    """Event 1037512350"""
    GotoIfFlagEnabled(Label.L0, flag=1037510810)
    GotoIfFlagEnabled(Label.L0, flag=1037510800)
    GotoIfFlagEnabled(Label.L0, flag=1041520820)
    DisableCharacter(character)
    DisableAnimations(character)
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1037512300))
    
    MAIN.Await(AND_1)
    
    SetCharacterFadeOnEnable(character=character, state=True)
    EnableCharacter(character)
    EnableAnimations(character)
    ForceAnimation(character, 20019)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableAnimations(character)
    End()
