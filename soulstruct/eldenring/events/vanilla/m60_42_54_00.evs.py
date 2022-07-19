"""
North Altus Plateau (NE) (SW)

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
from .entities.m60_42_54_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterLadder(start_climbing_flag=1042540580, stop_climbing_flag=1042540581, asset=Assets.AEG110_012_1000)
    RegisterLadder(start_climbing_flag=1042540582, stop_climbing_flag=1042540583, asset=Assets.AEG110_012_1001)
    RegisterLadder(start_climbing_flag=1042540584, stop_climbing_flag=1042540585, asset=Assets.AEG110_012_1002)
    CommonFunc_90005633(
        0,
        character=580350,
        flag=580050,
        character_1=Characters.WanderingNoble,
        animation_id=30017,
        animation_id_1=20017,
        asset=Assets.AEG099_166_9000,
        asset_1=Assets.AEG099_990_9000,
    )
    CommonFunc_90005706(0, 1042540700, 30025, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1042540700)
    CommonFunc_90005250(0, character=Characters.SmallerDog0, region=1042542200, seconds=0.0, animation_id=3005)
    Event_1042542350(0, character=Characters.DominulaCelebrant0, region=1042542300, character_1=1042545300)
    Event_1042542350(1, character=Characters.DominulaCelebrant1, region=1042542301, character_1=1042545300)
    Event_1042542350(2, character=Characters.DominulaCelebrant2, region=1042542302, character_1=1042545300)
    Event_1042542350(3, character=Characters.DominulaCelebrant6, region=1042542310, character_1=1042545310)
    Event_1042542350(4, character=Characters.DominulaCelebrant7, region=1042542311, character_1=1042545310)
    Event_1042542350(5, character=Characters.DominulaCelebrant8, region=1042542312, character_1=1042545310)
    Event_1042542350(6, character=Characters.DominulaCelebrant9, region=1042542313, character_1=1042545310)
    Event_1042542350(7, character=Characters.DominulaCelebrant10, region=1042542314, character_1=1042545310)
    Event_1042542350(8, character=Characters.DominulaCelebrant11, region=1042542315, character_1=1042545310)
    Event_1042542350(9, character=Characters.DominulaCelebrant12, region=1042542316, character_1=1042545310)
    Event_1042542350(10, character=Characters.DominulaCelebrant13, region=1042542317, character_1=1042545310)
    Event_1042542350(11, character=Characters.DominulaCelebrant14, region=1042542318, character_1=1042545310)
    Event_1042542350(12, character=Characters.DominulaCelebrant17, region=1042542327, character_1=1042545327)
    Event_1042542350(13, character=Characters.DominulaCelebrant18, region=1042542328, character_1=1042545327)
    Event_1042542350(14, character=Characters.DominulaCelebrant19, region=1042542329, character_1=1042545327)
    CommonFunc_90005251(0, character=Characters.DominulaCelebrant20, radius=4.0, seconds=0.0, animation_id=3004)
    Event_1042542350(15, character=Characters.DominulaCelebrant23, region=1042542338, character_1=1042545338)
    Event_1042542350(16, character=Characters.DominulaCelebrant24, region=1042542339, character_1=1042545338)
    Event_1042542350(17, character=Characters.DominulaCelebrant3, region=1042542303, character_1=1042545303)
    Event_1042542350(18, character=Characters.DominulaCelebrant4, region=1042542304, character_1=1042545303)
    Event_1042542350(19, character=Characters.DominulaCelebrant5, region=1042542305, character_1=1042545303)
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellSoldier0,
        animation_id=30004,
        animation_id_1=20004,
        region=1042542651,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LeyndellSoldier1,
        animation_id=30004,
        animation_id_1=20004,
        region=1042542651,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(0, 1042540653, 30004, 20004, 1042542651, 0.0, 0, 0, 0, 0)


@RestartOnRest(1042542350)
def Event_1042542350(_, character: uint, region: uint, character_1: uint):
    """Event 1042542350"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    ForceAnimation(character, 20018)
    Wait(1.600000023841858)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 30008, loop=True)
    DisableAI(character)
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
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    
    MAIN.Await(OR_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    Wait(0.10000000149011612)
    ForceAnimation(character, 20008)
    EnableAI(character)
    Wait(5.0)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_2.Add(CharacterInsideRegion(character=character, region=region))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterDead(character))
    AwaitConditionTrue(OR_2)
    Restart()
