"""
Liurnia to Altus Plateau (NW) (NW)

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
from .entities.m60_36_51_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005683(0, flag=62313, asset=Assets.AEG099_055_3000, vfx_id=208, flag_1=78390, flag_2=78390)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=1036518600)
    CommonFunc_90005620(
        0,
        flag=1036510570,
        asset=Assets.AEG027_078_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=Assets.AEG027_217_9000,
        left_flag=1036512570,
        cancel_flag__right_flag=1036512571,
        right=1036512572,
    )
    Event_1036512575()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_1036512400(0, character=Characters.MirandaFlower0, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512400(1, character=Characters.MirandaFlower1, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512400(2, character=Characters.MirandaFlower8, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512400(3, character=Characters.MirandaFlower9, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512400(4, character=Characters.MirandaFlower10, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(5, character=Characters.MirandaFlower5, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(6, character=Characters.MirandaFlower6, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(7, character=Characters.MirandaFlower7, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(8, character=Characters.MirandaFlower11, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(9, character=Characters.MirandaFlower12, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(10, character=Characters.MirandaFlower13, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(11, character=Characters.MirandaFlower14, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(12, character=Characters.MirandaFlower15, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(13, character=Characters.MirandaFlower16, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(14, character=Characters.MirandaFlower17, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(15, character=Characters.MirandaFlower0, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(16, character=Characters.MirandaFlower1, radius=2.0, seconds=0.0, animation_id=0)
    Event_1036512450(17, character=Characters.MirandaFlower4, radius=2.0, seconds=0.0, animation_id=0)
    CommonFunc_90005251(0, character=Characters.GiantMirandaFlower, radius=5.0, seconds=0.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.DepravedPerfurmer, region=1036512300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.DepravedPerfurmer, region=1036512301, seconds=0.0, animation_id=-1)
    Event_1036512300()
    CommonFunc_90005261(0, character=Characters.Omenkiller, region=1036512300, radius=3.0, seconds=1.0, animation_id=-1)


@RestartOnRest(1036512300)
def Event_1036512300():
    """Event 1036512300"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1036512300))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=1036512301))
    
    ChangePatrolBehavior(Characters.DepravedPerfurmer, patrol_information_id=1036513301)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(1036512400)
def Event_1036512400(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036512400"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_10.Add(CharacterInsideRegion(character=Characters.DepravedPerfurmer, region=1036512400))
    AND_10.Add(HasAIStatus(Characters.DepravedPerfurmer, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_10)
    AND_11.Add(CharacterInsideRegion(character=1036510304, region=1036512400))
    AND_11.Add(HasAIStatus(1036510304, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_11)
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
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
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
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1036512450)
def Event_1036512450(_, character: uint, radius: float, seconds: float, animation_id: int):
    """Event 1036512450"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_8.Add(EntityWithinDistance(entity=Characters.DepravedPerfurmer, other_entity=character, radius=8.0))
    AND_8.Add(HasAIStatus(Characters.DepravedPerfurmer, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_8)
    AND_7.Add(EntityWithinDistance(entity=1036510304, other_entity=character, radius=8.0))
    AND_7.Add(HasAIStatus(1036510304, ai_status=AIStatusType.Battle))
    OR_2.Add(AND_7)
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    GotoIfFinishedConditionFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(1036512575)
def Event_1036512575():
    """Event 1036512575"""
    DisableNetworkSync()
    if FlagDisabled(1036510570):
        DisableAssetActivation(Assets.AEG110_063_3000, obj_act_id=110063)
    
        MAIN.Await(FlagEnabled(1036510570))
    
        EnableAssetActivation(Assets.AEG110_063_3000, obj_act_id=110063)
