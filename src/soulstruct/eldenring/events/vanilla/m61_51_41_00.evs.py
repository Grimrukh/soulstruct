"""
Land of Shadow 12-10 SE NE

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
    Event_2051412200(0, character=2051410200, character_1=2051410300)
    Event_2051412201(0, character=2051410200)
    Event_2051412202(0, character=2051410200)
    Event_2051412203(0, character=2051410200)
    CommonFunc_90005301(0, flag=2051410200, character=2051410200, item_lot__unk1=2051410700, seconds=0.0, unk1=0)
    Event_2051412200(1, character=2051410201, character_1=2051410301)
    Event_2051412201(1, character=2051410201)
    Event_2051412202(1, character=2051410201)
    Event_2051412203(1, character=2051410201)
    CommonFunc_90005301(0, flag=2051410201, character=2051410201, item_lot__unk1=2051410710, seconds=0.0, unk1=0)
    Event_2051412500(0, attacked_entity=2051411550, region=2051412550)
    Event_2051412500(1, attacked_entity=2051411551, region=2051412551)
    Event_2051412500(2, attacked_entity=2051411552, region=2051412552)
    Event_2051412500(3, attacked_entity=2051411553, region=2051412553)
    Event_2051412500(4, attacked_entity=2051411554, region=2051412554)
    Event_2051412500(5, attacked_entity=2051411555, region=2051412555)
    Event_2051412500(6, attacked_entity=2051411556, region=2051412556)
    Event_2051412500(7, attacked_entity=2051411557, region=2051412557)
    Event_2051412500(8, attacked_entity=2051411558, region=2051412558)
    Event_2051412500(9, attacked_entity=2051411559, region=2051412559)
    Event_2051412500(10, attacked_entity=2051411560, region=2051412560)


@RestartOnRest(2051412200)
def Event_2051412200(_, character: Character | int, character_1: uint):
    """Event 2051412200"""
    AND_1.Add(CharacterHasSpecialEffect(character, 20011451))
    AND_1.Add(CharacterHasSpecialEffect(character, 20011450))
    
    MAIN.Await(AND_1)
    
    Move(
        character_1,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        dummy_id=12,
        copy_draw_parent=PLAYER,
    )
    SetCharacterEventTarget(character, entity=character_1)
    RemoveSpecialEffect(character, 20011450)
    Restart()


@RestartOnRest(2051412201)
def Event_2051412201(_, character: Character | int):
    """Event 2051412201"""
    AND_15.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(1, AND_15)
    End()
    AddSpecialEffect(character, 20011470)
    AddSpecialEffect(character, 19690)
    DisableHealthBar(character)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 20011471))
    
    RemoveSpecialEffect(character, 20011470)
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part10, part_health=99999)
    SetNPCPartEffects(
        character,
        npc_part_id=10,
        material_sfx_id=109,
        material_vfx_id=109,
        unk_16_20=-1,
        unk_20_24=113,
        unk_24_28=-1,
    )
    EnableHealthBar(character)
    AddSpecialEffect(character, 20011472)


@RestartOnRest(2051412202)
def Event_2051412202(_, character: Character | int):
    """Event 2051412202"""
    AND_15.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(1, AND_15)
    End()
    OR_1.Add(CharacterHasSpecialEffect(character, 20011453))
    OR_1.Add(CharacterHasSpecialEffect(character, 20011451))
    AwaitConditionTrue(OR_1)
    GotoIfCharacterHasSpecialEffect(Label.L0, character=character, special_effect=20011451)
    AddSpecialEffect(PLAYER, 20011454)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, 20011455)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(2051412203)
def Event_2051412203(_, character: Character | int):
    """Event 2051412203"""
    AND_15.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(1, AND_15)
    End()
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AwaitConditionTrue(OR_1)
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 20011458)
    AddSpecialEffect(character, 20011474)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 20011459)
    Goto(Label.L20)
    AddSpecialEffect(character, 20011474)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 20011460)
    AddSpecialEffect(character, 20011475)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(2051412500)
def Event_2051412500(_, attacked_entity: uint, region: uint):
    """Event 2051412500"""
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    PlaySoundEffect(attacked_entity, 610200888, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(vfx_id=861221, anchor_entity=attacked_entity, dummy_id=100, anchor_type=CoordEntityType.Asset)
    TriggerAISound(ai_sound_param_id=8000, anchor_entity=region, unk_8_12=1)
    Wait(1.5)
    TriggerAISound(ai_sound_param_id=8000, anchor_entity=region, unk_8_12=1)
    Wait(1.0)
    Restart()
