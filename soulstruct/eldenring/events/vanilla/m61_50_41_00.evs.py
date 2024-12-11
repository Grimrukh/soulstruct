"""
Land of Shadow 12-10 SE NW

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
    Event_2050412200(0, character=2050410200, character_1=2050410300)
    Event_2050412201(0, character=2050410200)
    Event_2050412202(0, character=2050410200)
    Event_2050412203(0, character=2050410200)
    CommonFunc_90005301(0, flag=2050410200, character=2050410200, item_lot__unk1=2050410700, seconds=0.0, unk1=0)


@RestartOnRest(2050412200)
def Event_2050412200(_, character: Character | int, character_1: uint):
    """Event 2050412200"""
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


@RestartOnRest(2050412201)
def Event_2050412201(_, character: Character | int):
    """Event 2050412201"""
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


@RestartOnRest(2050412202)
def Event_2050412202(_, character: Character | int):
    """Event 2050412202"""
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


@RestartOnRest(2050412203)
def Event_2050412203(_, character: Character | int):
    """Event 2050412203"""
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
