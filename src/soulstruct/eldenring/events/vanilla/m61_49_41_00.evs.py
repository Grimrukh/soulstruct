"""
Land of Shadow 12-10 SW NE

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
    RegisterGrace(grace_flag=2049410000, asset=2049411950, enemy_block_distance=0.0)
    CommonFunc_90005201(
        0,
        character=2049410800,
        animation_id=30000,
        animation_id_1=20000,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=2049410800, name=905580601, npc_threat_level=25)
    CommonFunc_90005860(0, flag=2049410800, left=0, character=2049410800, left_1=1, item_lot=30850, seconds=0.0)
    CommonFunc_90005734(
        0,
        flag=4265,
        flag_1=2048429222,
        region=2049412710,
        region_1=2049412710,
        flag_2=2048429222,
        right=-1,
    )
    Event_2049410700(0, flag=2048429224, flag_1=4260, flag_2=4265, flag_3=2048429222)


@RestartOnRest(2049412200)
def Event_2049412200(_, character: Character | int, character_1: uint):
    """Event 2049412200"""
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


@RestartOnRest(2049412201)
def Event_2049412201(_, character__character_group: Character | int):
    """Event 2049412201"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character__character_group, 20011450))
    AND_1.Add(CharacterUnknown_4_22(character_group=character__character_group))
    AwaitConditionTrue(AND_1)
    AddSpecialEffect(character__character_group, 20011450)
    RemoveSpecialEffect(character__character_group, 20011452)
    Restart()


@RestartOnRest(2049412202)
def Event_2049412202(_, character: Character | int):
    """Event 2049412202"""
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


@RestartOnRest(2049412203)
def Event_2049412203(_, character: Character | int):
    """Event 2049412203"""
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
    OR_1.Add(CharacterNotMounted(character=PLAYER))
    OR_1.Add(CharacterHasSpecialEffect(character, 20011462))
    SkipLinesIfConditionTrue(2, OR_1)
    AddSpecialEffect(PLAYER, 20011461)
    AddSpecialEffect(character, 20011462)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 20011459)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 20011460)
    OR_1.Add(CharacterNotMounted(character=PLAYER))
    OR_1.Add(CharacterHasSpecialEffect(character, 20011462))
    SkipLinesIfConditionTrue(2, OR_1)
    AddSpecialEffect(PLAYER, 20011461)
    AddSpecialEffect(character, 20011462)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(1.0)
    Restart()


@RestartOnRest(2049410700)
def Event_2049410700(_, flag: Flag | int, flag_1: Flag | int, flag_2: Flag | int, flag_3: Flag | int):
    """Event 2049410700"""
    DisableFlag(flag)
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagDisabled(flag_1))
    OR_1.Add(FlagDisabled(flag_2))
    if OR_1:
        return
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag_2))
    AND_2.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_2)
    
    EnableFlag(flag)
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_15.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    
    MAIN.Await(OR_15)
    
    Restart()
