"""
North Altus Plateau (NW) (NE)

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
from .entities.m60_41_55_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    ConnectCharacterToCaravan(character=Characters.WanderingNoble0, caravan_asset=1041552000)
    ConnectCharacterToCaravan(character=Characters.WanderingNoble1, caravan_asset=1041552000)
    ConnectCharacterToCaravan(character=Characters.WanderingNoble2, caravan_asset=1041552000)
    ConnectCharacterToCaravan(character=1041550403, caravan_asset=1041552000)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1041552400(0, character=Characters.WanderingNoble0)
    Event_1041552400(1, character=Characters.WanderingNoble1)
    Event_1041552400(2, character=Characters.WanderingNoble2)
    Event_1041552400(3, character=Characters.WanderingNoble3)
    Event_1041552400(4, character=Characters.WanderingNoble5)
    Event_1041552400(5, character=Characters.WanderingNoble6)
    CommonFunc_90005201(
        0,
        character=Characters.ScalyMisbegotten,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SmallerDog0,
        animation_id=30000,
        animation_id_1=20000,
        region=1041552351,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.SmallerDog1, region=1041552352, seconds=0.0, animation_id=3000)
    Event_1041552350(0, character=Characters.DominulaCelebrant0, region=1041552200, character_1=1041555200)
    Event_1041552350(1, character=Characters.DominulaCelebrant1, region=1041552201, character_1=1041555200)
    Event_1041552350(2, character=Characters.DominulaCelebrant2, region=1041552202, character_1=1041555200)
    Event_1041552350(3, character=Characters.DominulaCelebrant3, region=1041552203, character_1=1041555200)
    Event_1041552350(4, character=Characters.DominulaCelebrant4, region=1041552204, character_1=1041555200)
    Event_1041552350(5, character=Characters.DominulaCelebrant5, region=1041552205, character_1=1041555200)
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse0,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse1,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse2,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse3,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.8999999761581421,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse4,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.PutridCorpse5,
        animation_id=30001,
        animation_id_1=20001,
        region=1041552250,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@RestartOnRest(1041552350)
def Event_1041552350(_, character: uint, region: uint, character_1: uint):
    """Event 1041552350"""
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
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
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


@RestartOnRest(1041552400)
def Event_1041552400(_, character: uint):
    """Event 1041552400"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableAI(character)
    ForceAnimation(character, 30012, loop=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=character, state_info=260))
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
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    
    MAIN.Await(OR_1)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableAI(character)
