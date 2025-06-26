"""
Land of Shadow 12-10 NE SW

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
    RegisterGrace(grace_flag=2050420000, asset=2050421950)
    Event_2050422200(0, character=2050420200, character_1=2050420300)
    Event_2050422201(0, character=2050420200)
    Event_2050422202(0, character=2050420200)
    Event_2050422203(0, character=2050420200)
    CommonFunc_90005301(0, flag=2050420200, character=2050420200, item_lot__unk1=2050420700, seconds=0.0, unk1=0)
    CommonFunc_90005250(0, character=2050420201, region=2050422201, seconds=0.5, animation_id=0)
    Event_2050422500(0, attacked_entity=2050421550, region=2050422550)
    Event_2050422500(1, attacked_entity=2050421551, region=2050422551)
    Event_2050422500(2, attacked_entity=2050421552, region=2050422552)
    Event_2050422500(3, attacked_entity=2050421553, region=2050422553)
    Event_2050422500(4, attacked_entity=2050421554, region=2050422554)
    Event_2050422500(5, attacked_entity=2050421555, region=2050422555)
    Event_2050422500(6, attacked_entity=2050421556, region=2050422556)
    Event_2050422500(7, attacked_entity=2050421557, region=2050422557)
    Event_2050422500(8, attacked_entity=2050421558, region=2050422558)
    Event_2050422500(9, attacked_entity=2050421559, region=2050422559)
    Event_2050422500(10, attacked_entity=2050421560, region=2050422560)
    Event_2050422500(11, attacked_entity=2050421561, region=2050422561)
    Event_2050422500(12, attacked_entity=2050421562, region=2050422562)
    Event_2050422500(13, attacked_entity=2050421563, region=2050422563)
    Event_2050422500(14, attacked_entity=2050421564, region=2050422564)
    Event_2050422500(15, attacked_entity=2050421565, region=2050422565)
    Event_2050422500(16, attacked_entity=2050421566, region=2050422566)
    Event_2050422500(17, attacked_entity=2050421567, region=2050422567)
    Event_2050422500(18, attacked_entity=2050421568, region=2050422568)
    Event_2050422500(19, attacked_entity=2050421569, region=2050422569)
    Event_2050422500(20, attacked_entity=2050421570, region=2050422570)
    Event_2050422500(21, attacked_entity=2050421571, region=2050422571)
    Event_2050422500(22, attacked_entity=2050421572, region=2050422572)
    Event_2050422500(23, attacked_entity=2050421573, region=2050422573)


@RestartOnRest(2050422200)
def Event_2050422200(_, character: Character | int, character_1: uint):
    """Event 2050422200"""
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


@RestartOnRest(2050422201)
def Event_2050422201(_, character: Character | int):
    """Event 2050422201"""
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


@RestartOnRest(2050422202)
def Event_2050422202(_, character: Character | int):
    """Event 2050422202"""
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


@RestartOnRest(2050422203)
def Event_2050422203(_, character: Character | int):
    """Event 2050422203"""
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


@RestartOnRest(2050422500)
def Event_2050422500(_, attacked_entity: uint, region: uint):
    """Event 2050422500"""
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
