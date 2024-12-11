"""
Land of Shadow 12-09 NW SW

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
    CommonFunc_90005301(0, flag=2048380800, character=2048380800, item_lot__unk1=2048380020, seconds=5.0, unk1=0)
    Event_2048382806()
    Event_2048382815(0, character=2048380810)
    Event_2048382807(0, character=2048380800, character_1=2048380810)
    Event_2048382809(
        0,
        character=2048380800,
        entity=2048383800,
        entity_1=2048383801,
        entity_2=2048383802,
        special_effect=15300,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
    )
    Event_2048382801(0, character=2048380800, region=2048382810, special_effect=15310, flag=2048380800)
    Event_2048382801(1, character=2048380800, region=2048382811, special_effect=15311, flag=2048380800)
    Event_2048382801(2, character=2048380800, region=2048382812, special_effect=15312, flag=2048380800)
    Event_2048382800(
        0,
        character=2048380800,
        flag=2048380800,
        special_effect=15302,
        special_effect_1=15310,
        special_effect_2=15311,
        special_effect_3=15312,
        destination=2048382800,
        destination_1=2048382801,
        destination_2=2048382802,
    )
    Event_2048382808(0, flag=2048380800, character=2048380800, character_1=2048385200)
    Event_2048382870(
        0,
        character=2048380850,
        animation_id=30005,
        animation_id_1=20005,
        region=2048382850,
        flag=2048380870,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005870(0, character=2048380850, name=905860601, npc_threat_level=22)
    CommonFunc_90005860(0, flag=2048380850, left=0, character=2048380850, left_1=1, item_lot=30840, seconds=0.0)
    Event_2048382865()
    Event_2048382871()
    Event_2048382866(0, character=2048380851, special_effect=5032, entity=2048380850)
    Event_2048382866(1, character=2048380852, special_effect=5026, entity=2048380850)
    Event_2048382866(3, character=2048380854, special_effect=5026, entity=2048380850)
    Event_2048382866(6, character=2048380857, special_effect=5029, entity=2048380850)
    Event_2048382866(5, character=2048380856, special_effect=5032, entity=2048380850)
    Event_2048382866(4, character=2048380855, special_effect=5033, entity=2048380850)
    Event_2048382866(2, character=2048380853, special_effect=5034, entity=2048380850)
    Event_2048382866(7, character=2048380858, special_effect=5030, entity=2048380850)
    Event_2048382866(8, character=2048380859, special_effect=5028, entity=2048380850)
    CommonFunc_90005211(
        0,
        character=2048380306,
        animation_id=30016,
        animation_id_1=20016,
        region=2048382300,
        radius=0.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048380307,
        animation_id=30016,
        animation_id_1=20016,
        region=2048382300,
        radius=0.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=2048380308,
        animation_id=30016,
        animation_id_1=20016,
        region=2048382300,
        radius=0.0,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005780(
        0,
        flag=2048380850,
        summon_flag=2048382160,
        dismissal_flag=2048382161,
        character=2048380700,
        sign_type=20,
        region=2048382701,
        right=2051459751,
        unknown=0,
        right_1=0,
    )
    CommonFunc_90005781(0, flag=2048380850, flag_1=2048382160, flag_2=2048382161, character=2048380700)
    CommonFunc_90005783(
        0,
        flag=2048380850,
        flag_1=2048382160,
        flag_2=2048382161,
        character=2048380700,
        other_entity=2048382701,
        region=2048382400,
        left=1,
    )


@RestartOnRest(2048382800)
def Event_2048382800(
    _,
    character: uint,
    flag: Flag | int,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
    destination: uint,
    destination_1: uint,
    destination_2: uint,
):
    """Event 2048382800"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(character, special_effect))
    
    GotoIfCharacterHasSpecialEffect(Label.L1, character=character, special_effect=special_effect_1)
    GotoIfCharacterHasSpecialEffect(Label.L2, character=character, special_effect=special_effect_2)
    GotoIfCharacterHasSpecialEffect(Label.L3, character=character, special_effect=special_effect_3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3022, loop=True)
    ReplanAI(character)
    Wait(5.0)
    Restart()


@RestartOnRest(2048382801)
def Event_2048382801(_, character: Character | int, region: Region | int, special_effect: int, flag: Flag | int):
    """Event 2048382801"""
    if FlagEnabled(flag):
        return
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect, target_count=0.0))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect)
    Restart()


@RestartOnRest(2048382805)
def Event_2048382805(_, character: uint, special_effect: int, flag: Flag | int):
    """Event 2048382805"""
    if FlagEnabled(flag):
        return
    AND_1.Add(HealthRatio(character) <= 0.20000000298023224)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 3021, wait_for_completion=True)


@RestartOnRest(2048382806)
def Event_2048382806():
    """Event 2048382806"""
    AddSpecialEffect(2048380800, 20011750)
    End()


@RestartOnRest(2048382807)
def Event_2048382807(_, character: uint, character_1: uint):
    """Event 2048382807"""
    if FlagEnabled(2048380800):
        return
    SetCharacterEventTarget(character, entity=character_1)
    SetCharacterEventTarget(character_1, entity=character)
    AND_1.Add(CharacterDead(character_1))
    AwaitConditionTrue(AND_1)
    Wait(5.0)
    AND_2.Add(CharacterAlive(character_1))
    AwaitConditionTrue(AND_2)
    Restart()


@RestartOnRest(2048382808)
def Event_2048382808(_, flag: Flag | int, character: Character | int, character_1: uint):
    """Event 2048382808"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    Kill(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    MAIN.Await(MAIN)
    
    Kill(character_1)
    DisableSpawner(entity=2048383800)
    DisableSpawner(entity=2048383801)
    DisableSpawner(entity=2048383802)
    Wait(2.0)
    Kill(character_1)
    Wait(7.0)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()


@RestartOnRest(2048382809)
def Event_2048382809(
    _,
    character: uint,
    entity: uint,
    entity_1: uint,
    entity_2: uint,
    special_effect: int,
    special_effect_1: int,
    special_effect_2: int,
    special_effect_3: int,
):
    """Event 2048382809"""
    GotoIfFlagDisabled(Label.L0, flag=2048380800)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagDisabled(character))
    
    MAIN.Await(AND_1)
    
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect_1):
        EnableSpawner(entity=entity)
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect_2):
        EnableSpawner(entity=entity_1)
    if CharacterHasSpecialEffect(character=character, special_effect=special_effect_3):
        EnableSpawner(entity=entity_2)
    Wait(1.0)
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    Wait(1.0)
    Restart()


@RestartOnRest(2048382815)
def Event_2048382815(_, character: Character | int):
    """Event 2048382815"""
    if FlagEnabled(2048380800):
        return
    AddSpecialEffect(character, 20012650)


@RestartOnRest(2048382865)
def Event_2048382865():
    """Event 2048382865"""
    if FlagEnabled(2048380850):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2048380850, 5036))
    
    ForceAnimation(2048380850, 3019)


@RestartOnRest(2048382866)
def Event_2048382866(_, character: uint, special_effect: int, entity: uint):
    """Event 2048382866"""
    DisableAI(character)
    SetBackreadStateAlternate(character, True)
    EnableInvincibility(character)
    if FlagEnabled(2048380850):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2048380850, 20011653))
    
    WaitRandomSeconds(min_seconds=0.0, max_seconds=0.30000001192092896)
    EnableAI(character)
    SetCharacterEventTarget(character, entity=entity)
    AddSpecialEffect(2048380850, 20011667)
    WaitRealFrames(frames=1)
    AddSpecialEffect(character, special_effect)
    DisableInvincibility(character)
    ForceAnimation(character, 20003)


@RestartOnRest(2048382351)
def Event_2048382351(_, character: uint):
    """Event 2048382351"""
    MAIN.Await(FlagEnabled(2048380850))
    
    Kill(character)
    DisableAnimations(character)
    DisableCharacter(character)


@RestartOnRest(2048382870)
def Event_2048382870(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    flag: Flag | int,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 2048382870"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if FlagEnabled(flag):
        return
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
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
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    EnableNetworkFlag(flag)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@ContinueOnRest(2048382871)
def Event_2048382871():
    """Event 2048382871"""
    if FlagEnabled(2048380870):
        return
    AddSpecialEffect(2048380102, 9531)
    AwaitFlagEnabled(flag=2048380870)
    AddSpecialEffect(2048380102, 9532)
