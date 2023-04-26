"""
North Altus Plateau (NW) (SE)

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
from .enums.m60_41_54_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=76308, asset=Assets.AEG099_060_9000, enemy_block_distance=3.0)
    CommonFunc_90005100(
        0,
        flag=76314,
        flag_1=76308,
        asset=Assets.AEG099_060_9001,
        source_flag=77310,
        value=1,
        flag_2=78310,
        flag_3=78311,
        flag_4=78312,
        flag_5=78313,
        flag_6=78314,
        flag_7=78315,
        flag_8=78316,
        flag_9=78317,
        flag_10=78318,
        flag_11=78319,
    )
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930025, left=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)
    CommonFunc_90005251(0, character=Characters.DominulaCelebrant5, radius=90.0, seconds=0.0, animation_id=0)
    Event_1041542200()
    Event_1041542230(0, character=Characters.DominulaCelebrant1, animation_id=30006, animation_id_1=20006, radius=3.0)
    Event_1041542230(1, character=Characters.DominulaCelebrant2, animation_id=30006, animation_id_1=20006, radius=3.0)
    Event_1041542230(2, character=Characters.DominulaCelebrant3, animation_id=30006, animation_id_1=20006, radius=3.0)
    Event_1041542230(3, character=1041540204, animation_id=30006, animation_id_1=20006, radius=5.0)
    Event_1041542230(4, character=Characters.DominulaCelebrant4, animation_id=30006, animation_id_1=20006, radius=3.0)


@RestartOnRest(1041542200)
def Event_1041542200():
    """Event 1041542200"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(Characters.DominulaCelebrant0, 12054)
    AddSpecialEffect(Characters.DominulaCelebrant0, 8092)
    EnableThisNetworkSlotFlag()


@RestartOnRest(1041542230)
def Event_1041542230(_, character: uint, animation_id: int, animation_id_1: int, radius: float):
    """Event 1041542230"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
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
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterHasSpecialEffect(Characters.DominulaCelebrant0, 12051))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    ForceAnimation(character, animation_id_1, loop=True)
    End()
