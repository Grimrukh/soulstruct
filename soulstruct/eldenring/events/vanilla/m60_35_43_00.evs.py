"""
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
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1035430000, obj=1035431950, unknown=5.0)
    RunCommonEvent(
        0,
        90005390,
        args=(1035430220, 1035432220, 1035430220, 1035430230, 1, 1035430100),
        arg_types="IIIIii",
    )
    RunCommonEvent(0, 90005391, args=(1035430220, 1035432220, 1035430220, 1035430230, 1), arg_types="IIIIi")


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    RunCommonEvent(
        0,
        90005211,
        args=(1035430200, 30001, 20001, 1035432200, 3.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1035430201, 30001, 20001, 1035432200, 3.0, 2.5, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1035430202, 30001, 20001, 1035432200, 3.0, 0.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )
    RunCommonEvent(
        0,
        90005211,
        args=(1035430203, 30001, 20001, 1035432200, 3.0, 1.0, 0, 0, 0, 0),
        arg_types="IiiIffIIII",
    )


@RestartOnRest(1035432390)
def Event_1035432390(_, flag: uint, flag_1: uint, character__unk_0_4: uint, character: uint, left: int):
    """Event 1035432390"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character__unk_0_4)
    DisableGravity(character__unk_0_4)
    DisableAnimations(character__unk_0_4)
    DisableAI(character__unk_0_4)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    End()
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableCharacter(character__unk_0_4)
    DisableGravity(character__unk_0_4)
    DisableAnimations(character__unk_0_4)
    DisableAI(character__unk_0_4)
    EnableCharacter(character)
    EnableGravity(character)
    EnableAnimations(character)
    EnableAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    Unknown_2004_73(entity=character, unk_4_8=1)
    IfCharacterDead(AND_1, character__unk_0_4)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character__unk_0_4, True)
    SetBackreadStateAlternate(character, True)
    Wait(0.5)
    DisableGravity(character__unk_0_4)
    DisableAnimations(character__unk_0_4)
    DisableAI(character__unk_0_4)
    Unknown_2004_70(unk_0_4=character__unk_0_4, unk_4_8=1)
    WaitFrames(frames=1)
    Move(
        character,
        destination=character__unk_0_4,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character__unk_0_4,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.5)
    AddSpecialEffect(character__unk_0_4, 4305)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=1)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=0)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601101,
        anchor_entity=character__unk_0_4,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    CreateTemporaryVFX(
        vfx_id=601100,
        anchor_entity=character__unk_0_4,
        model_point=900,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableCharacter(character)
    EnableGravity(character)
    EnableAnimations(character)
    EnableAI(character)
    DisableCharacter(character__unk_0_4)
    SetBackreadStateAlternate(character__unk_0_4, False)
    SetBackreadStateAlternate(character, False)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag_1)


@RestartOnRest(1035432395)
def Event_1035432395(
    _,
    flag: uint,
    flag_1: uint,
    character: uint,
    character_1: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 1035432395"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterDead(AND_1, character_1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)

    # --- Label 1 --- #
    DefineLabel(1)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=character_1,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=character_1,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character_1, 4305)
    Wait(3.0)
    SkipLinesIfValueEqual(2, left=item_lot_param_id, right=0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    AwardItemLot(item_lot_param_id, host_only=True)
    DisableCharacter(character)
    DisableGravity(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableCharacter(character_1)
    DisableGravity(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    EnableFlag(flag)
