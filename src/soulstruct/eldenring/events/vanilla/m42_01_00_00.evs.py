"""
m42_01_00_00

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
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=42010000, asset=42011950)
    CommonFunc_90005200(
        0,
        character=42010230,
        animation_id=30001,
        animation_id_1=20001,
        region=42012230,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42010231, region=42012231, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42010233,
        animation_id=30002,
        animation_id_1=20002,
        region=42012233,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010234,
        animation_id=30002,
        animation_id_1=20002,
        region=42012234,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=42010229, region=42012230, seconds=0.30000001192092896, animation_id=0)
    CommonFunc_90005200(
        0,
        character=42010227,
        animation_id=30001,
        animation_id_1=20001,
        region=42012227,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010228,
        animation_id=30001,
        animation_id_1=20001,
        region=42012227,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010200,
        animation_id=30001,
        animation_id_1=20001,
        region=42012200,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010201,
        animation_id=30001,
        animation_id_1=20001,
        region=42012201,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010202,
        animation_id=30001,
        animation_id_1=20001,
        region=42012201,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010203,
        animation_id=30001,
        animation_id_1=20001,
        region=42012201,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010205,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010209,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010211,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010213,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010214,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010215,
        animation_id=30001,
        animation_id_1=20001,
        region=42012205,
        seconds=0.0,
        left=8,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010210,
        animation_id=30000,
        animation_id_1=20000,
        region=42012205,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010207,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.10000000149011612,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010208,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.4000000059604645,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010216,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010217,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010218,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010220,
        animation_id=30001,
        animation_id_1=20001,
        region=42012207,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010224,
        animation_id=30001,
        animation_id_1=20001,
        region=42012233,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010225,
        animation_id=30001,
        animation_id_1=20001,
        region=42012233,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010204,
        animation_id=30000,
        animation_id_1=20000,
        region=42012204,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010222,
        animation_id=30000,
        animation_id_1=20000,
        region=42012204,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010212,
        animation_id=30000,
        animation_id_1=20000,
        region=42012212,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010206,
        animation_id=30001,
        animation_id_1=20001,
        region=42012206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=42010223,
        animation_id=30001,
        animation_id_1=20001,
        region=42012206,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_42012300(0, character=42010212, region=42012212)
    Event_42012330(0, character=42010212, region=42012212)
    CommonFunc_90005555(0, flag=42017000, item_lot=42010000, asset=42011610)


@RestartOnRest(42012610)
def Event_42012610():
    """Event 42012610"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(42017000):
        return
    CreateAssetVFX(42011610, dummy_id=100, vfx_id=834010)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=209200, entity=42011610))
    
    MAIN.Await(AND_1)
    
    FaceEntityAndForceAnimation(PLAYER, 42011610, wait_for_completion=True)
    ForceAnimation(PLAYER, 60100)
    Wait(1.0)
    CreateAssetVFX(42011610, dummy_id=100, vfx_id=800380)
    Wait(1.0)
    DeleteAssetVFX(42011610)
    Wait(2.5)
    AwardItemLot(42010000, host_only=True)


@RestartOnRest(42012300)
def Event_42012300(_, character: Character | int, region: Region | int):
    """Event 42012300"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4080)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4080)
    Restart()


@RestartOnRest(42012330)
def Event_42012330(_, character: Character | int, region: Region | int):
    """Event 42012330"""
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4085)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4085)
    Restart()


@RestartOnRest(42012360)
def Event_42012360(_, character: uint, region: Region | int, radius: float, seconds: float, animation_id: int):
    """Event 42012360"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
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
    
    EnableThisNetworkSlotFlag()
    GotoIfLastConditionResultFalse(Label.L1, input_condition=AND_1)
    Wait(seconds)
    if ValueNotEqual(left=animation_id, right=-1):
        ForceAnimation(character, animation_id, loop=True)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    if not LastResult(AND_1):
        return
    if CharacterOutsideRegion(character=PLAYER, region=region):
        return
    Wait(0.5)
    ForceAnimation(character, 3013)
