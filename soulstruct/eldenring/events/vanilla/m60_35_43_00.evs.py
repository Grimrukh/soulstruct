"""
Southwest Liurnia (NE) (NE)

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
from .enums.m60_35_43_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035430000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005390(
        0,
        flag=1035430220,
        flag_1=1035432220,
        anchor_entity=Characters.GiantLobster,
        character=Characters.GraftedScion,
        left=1,
        item_lot=1035430100,
    )
    CommonFunc_90005391(
        0,
        flag=1035430220,
        flag_1=1035432220,
        character=Characters.GiantLobster,
        character_1=Characters.GraftedScion,
        left=1,
    )


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    CommonFunc_90005211(
        0,
        character=1035430200,
        animation_id=30001,
        animation_id_1=20001,
        region=1035432200,
        radius=3.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=1035430201,
        animation_id=30001,
        animation_id_1=20001,
        region=1035432200,
        radius=3.0,
        seconds=2.5,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=1035430202,
        animation_id=30001,
        animation_id_1=20001,
        region=1035432200,
        radius=3.0,
        seconds=0.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )
    CommonFunc_90005211(
        0,
        character=1035430203,
        animation_id=30001,
        animation_id_1=20001,
        region=1035432200,
        radius=3.0,
        seconds=1.0,
        do_disable_gravity_and_collision=0,
        only_battle_state=0,
        only_ai_state_5=0,
        only_ai_state_4=0,
    )


@RestartOnRest(1035432390)
def Event_1035432390(_, flag: uint, flag_1: uint, character: uint, character_1: uint, left: int):
    """Event 1035432390"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    End()
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    SetCharacterFadeOnEnable(character=character_1, state=True)
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    SetBackreadStateAlternate(character, True)
    SetBackreadStateAlternate(character_1, True)
    Wait(0.5)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    SetDistanceBasedNetworkAuthorityUpdate(character=character, state=True)
    WaitFrames(frames=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=900,
        copy_draw_parent=character,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.5)
    AddSpecialEffect(character, 4305)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=1)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=0)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=601101, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    CreateTemporaryVFX(vfx_id=601100, anchor_entity=character, dummy_id=900, anchor_type=CoordEntityType.Character)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character_1)
    EnableGravity(character_1)
    EnableAnimations(character_1)
    EnableAI(character_1)
    DisableCharacter(character)
    SetBackreadStateAlternate(character, False)
    SetBackreadStateAlternate(character_1, False)
    if PlayerInOwnWorld():
        EnableNetworkFlag(flag_1)


@RestartOnRest(1035432395)
def Event_1035432395(_, flag: uint, flag_1: uint, character: uint, character_1: uint, left: int, item_lot: int):
    """Event 1035432395"""
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)

    # --- Label 1 --- #
    DefineLabel(1)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=character_1,
        dummy_id=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=character_1,
        dummy_id=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character_1, 4305)
    Wait(3.0)
    SkipLinesIfValueEqual(2, left=item_lot, right=0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AwardItemLot(item_lot, host_only=True)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    EnableFlag(flag)
