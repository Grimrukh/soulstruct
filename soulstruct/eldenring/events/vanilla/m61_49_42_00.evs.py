"""
Land of Shadow 12-10 NW SE

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
    CommonFunc_90005261(0, character=2049420200, region=2049422200, radius=45.0, seconds=0.0, animation_id=-1)
    Event_2049422200(0, character=2049420200, character_1=2049420300)
    Event_2049422201(0, character=2049420200)
    Event_2049422202(0, character=2049420200)
    Event_2049422203(0, character=2049420200)
    CommonFunc_90005301(0, flag=2049420200, character=2049420200, item_lot__unk1=2049420700, seconds=0.0, unk1=0)
    Event_2049422200(1, character=2049420202, character_1=2049420302)
    Event_2049422201(1, character=2049420202)
    Event_2049422202(1, character=2049420202)
    Event_2049422203(1, character=2049420202)
    CommonFunc_90005301(0, flag=2049420202, character=2049420202, item_lot__unk1=2049420720, seconds=0.0, unk1=0)
    CommonFunc_90005638(0, flag=2049420600, asset=2049421600, asset_1=2049421601)
    Event_2049422500(0, attacked_entity=2049421550, region=2049422550)
    Event_2049422500(1, attacked_entity=2049421551, region=2049422551)
    Event_2049422500(2, attacked_entity=2049421552, region=2049422552)
    Event_2049422500(3, attacked_entity=2049421553, region=2049422553)
    Event_2049422500(4, attacked_entity=2049421554, region=2049422554)
    Event_2049422500(6, attacked_entity=2049421556, region=2049422556)
    Event_2049422500(7, attacked_entity=2049421557, region=2049422557)
    Event_2049422500(8, attacked_entity=2049421558, region=2049422558)
    Event_2049422500(9, attacked_entity=2049421559, region=2049422559)
    Event_2049422500(10, attacked_entity=2049421560, region=2049422560)
    Event_2049422500(11, attacked_entity=2049421561, region=2049422561)
    Event_2049422500(12, attacked_entity=2049421562, region=2049422562)
    Event_2049422500(13, attacked_entity=2049421563, region=2049422563)
    Event_2049422500(14, attacked_entity=2049421564, region=2049422564)
    CommonFunc_90005706(0, character=2049420700, animation_id=30011, left=2049422700)
    Event_2049420700(0, asset=2049421700, character=2049420700)


@RestartOnRest(2049422200)
def Event_2049422200(_, character: Character | int, character_1: uint):
    """Event 2049422200"""
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


@RestartOnRest(2049422201)
def Event_2049422201(_, character: Character | int):
    """Event 2049422201"""
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


@RestartOnRest(2049422202)
def Event_2049422202(_, character: Character | int):
    """Event 2049422202"""
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


@RestartOnRest(2049422203)
def Event_2049422203(_, character: Character | int):
    """Event 2049422203"""
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


@RestartOnRest(2049422500)
def Event_2049422500(_, attacked_entity: uint, region: uint):
    """Event 2049422500"""
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


@RestartOnRest(2049420700)
def Event_2049420700(_, asset: Asset | int, character: Character | int):
    """Event 2049420700"""
    WaitFrames(frames=1)
    EnableAssetInvulnerability(asset)
    MoveAssetToCharacter(asset, character=character)
    End()
