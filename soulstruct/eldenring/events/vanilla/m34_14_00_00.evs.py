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
    RegisterGrace(grace_flag=34140000, obj=34141950, unknown=5.0)
    RegisterGrace(grace_flag=34140001, obj=34141951, unknown=5.0)
    Event_34142850()
    Event_34140860()
    Event_34142899()
    RunCommonEvent(0, 90005261, args=(34140300, 34142300, 10.0, 0.0, -1), arg_types="IIffi")
    Event_34142250(
        0,
        flag=34140250,
        flag_1=34142250,
        anchor_entity=34140200,
        character=34140210,
        left=1,
        item_lot_param_id=34140720
    )
    Event_34142251(0, character=34140250, flag=34142250, character_1=34140200, character_2=34140210, left=1)
    Event_34142252(0, 34140250, 0.0, 34140200, 0.0)
    Event_34142870()
    Event_34142865()
    Event_34142875()
    Event_34142510()
    RunCommonEvent(
        0,
        90005501,
        args=(34140510, 34140511, 4, 34141510, 34141511, 34141512, 34140512),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005508,
        args=(34140515, 34141515, 0, 34141515, 34141516, 34141517, 34140517),
        arg_types="IIIIIII",
    )
    RunCommonEvent(
        0,
        90005110,
        args=(193, 9104, 34141600, 34140700, 8150, 806932, 9082, 60521, 0),
        arg_types="IIIiiiiii",
    )
    RunCommonEvent(
        0,
        90005110,
        args=(195, 9112, 34141610, 34140710, 8152, 806938, 9084, 60524, 0),
        arg_types="IIIiiiiii",
    )
    RunCommonEvent(0, 91005600, args=(34142800, 34141695, 5), arg_types="IIi")
    Event_34142550()
    Event_34140700()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(34140700)
    Event_34140519()


@RestartOnRest(34142250)
def Event_34142250(
    _,
    flag: uint,
    flag_1: uint,
    anchor_entity: uint,
    character: uint,
    left: int,
    item_lot_param_id: int,
):
    """Event 34142250"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(AND_1, flag_1)
    IfCharacterDead(AND_1, character)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(1.0)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(
        vfx_id=601111,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(
        vfx_id=601110,
        anchor_entity=anchor_entity,
        model_point=960,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(1.0)
    EndIfPlayerNotInOwnWorld()
    SkipLinesIfValueEqual(1, left=item_lot_param_id, right=0)
    AwardItemLot(item_lot_param_id, host_only=True)
    EnableNetworkFlag(flag)


@RestartOnRest(34142251)
def Event_34142251(_, character: uint, flag: uint, character_1: uint, character_2: uint, left: int):
    """Event 34142251"""
    EnableImmortality(character_1)
    GotoIfFlagDisabled(Label.L0, flag=character)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_2)
    DisableAnimations(character_2)
    DisableGravity(character_2)
    DisableAI(character_2)
    Unknown_2004_73(entity=character_2, unk_4_8=1)
    IfCharacterHasSpecialEffect(AND_1, character_1, 12610)
    IfConditionTrue(MAIN, input_condition=AND_1)
    SetBackreadStateAlternate(character_1, True)
    SetBackreadStateAlternate(character_2, True)
    Move(
        character_2,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character_1,
    )
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=0)
    CreateTemporaryVFX(vfx_id=641912, anchor_entity=character_1, model_point=10, anchor_type=CoordEntityType.Character)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    CreateTemporaryVFX(vfx_id=641911, anchor_entity=character_1, model_point=10, anchor_type=CoordEntityType.Character)

    # --- Label 3 --- #
    DefineLabel(3)
    Wait(0.20000000298023224)
    DisableCharacter(character)
    EnableCharacter(character_2)
    EnableGravity(character_2)
    EnableAnimations(character_2)
    EnableAI(character_2)
    DisableCharacter(character_1)
    SetBackreadStateAlternate(character_1, False)
    SetBackreadStateAlternate(character_2, False)
    ForceAnimation(character_2, 20026, wait_for_completion=True, unknown2=1.0)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableNetworkFlag(flag)
    End()


@RestartOnRest(34142252)
def Event_34142252(_, flag: uint, seconds: float, character: uint, seconds_1: float):
    """Event 34142252"""
    EndIfFlagEnabled(flag)
    IfHealthValueEqual(AND_1, character, value=1)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableInvincibility(character)
    AddSpecialEffect(character, 12614)
    End()
    Wait(seconds)
    Wait(seconds_1)


@NeverRestart(34142510)
def Event_34142510():
    """Event 34142510"""
    RunCommonEvent(
        0,
        90005500,
        args=(
            34140510,
            34140511,
            4,
            34141510,
            34141511,
            34143511,
            34141512,
            34143512,
            34142511,
            34142512,
            34140512,
            34140513,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )
    RunCommonEvent(
        0,
        90005507,
        args=(
            34140515,
            34141515,
            0,
            34141515,
            34141516,
            34142518,
            34141517,
            34142519,
            34142516,
            34142517,
            34140517,
            34142517,
            0,
        ),
        arg_types="IIIIIIIIIIIII",
    )


@NeverRestart(34140519)
def Event_34140519():
    """Event 34140519"""
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(34140510)
    DisableThisSlotFlag()


@RestartOnRest(34142550)
def Event_34142550():
    """Event 34142550"""
    GotoIfFlagDisabled(Label.L0, flag=34140550)
    DisableObject(34141550)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    GotoIfFlagEnabled(Label.L2, flag=34142550)
    DeleteObjectVFX(34141550)
    CreateObjectVFX(34141550, vfx_id=101, model_point=1541)
    EnableNetworkFlag(34142550)

    # --- Label 2 --- #
    DefineLabel(2)
    IfPlayerInOwnWorld(AND_1)
    IfActionButtonParamActivated(AND_1, action_button_id=9505, entity=34141550)
    IfFlagEnabled(AND_2, 400001)
    IfConditionTrue(OR_3, input_condition=AND_1)
    IfConditionTrue(OR_3, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_3)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=AND_2)
    DisplayDialog(text=20005, anchor_entity=34141550, button_type=ButtonType.Yes_or_No)
    Wait(1.0)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableNetworkFlag(34140550)
    DeleteObjectVFX(34141550)
    DisableObject(34141550)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteObjectVFX(34141550)
    CreateObjectVFX(34141550, vfx_id=101, model_point=1541)
    End()


@RestartOnRest(34142850)
def Event_34142850():
    """Event 34142850"""
    EndIfFlagEnabled(34140850)
    IfHealthValueLessThanOrEqual(AND_1, 34140850, value=0)
    IfHealthValueLessThanOrEqual(AND_1, 34140851, value=0)
    IfConditionTrue(MAIN, input_condition=AND_1)
    Wait(4.0)
    PlaySoundEffect(34140850, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(AND_2, 34140850)
    IfCharacterDead(AND_2, 34140851)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(1.5)
    KillBossAndDisplayBanner(character=34140850, banner_type=BannerType.DutyFulfilled)
    EnableFlag(34140850)
    EnableFlag(9174)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(10740)
    End()


@RestartOnRest(34140860)
def Event_34140860():
    """Event 34140860"""
    GotoIfFlagDisabled(Label.L0, flag=34140850)
    DisableCharacter(34140850)
    DisableAnimations(34140850)
    Kill(34140850)
    DisableCharacter(34140851)
    DisableAnimations(34140851)
    Kill(34140851)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(34140850)
    DisableAI(34140851)
    DisableCharacter(34140850)
    DisableCharacter(34140851)
    GotoIfFlagEnabled(Label.L1, flag=34140851)
    IfPlayerInOwnWorld(AND_1)
    IfCharacterInsideRegion(AND_1, character=PLAYER, region=34142855)
    IfConditionTrue(OR_1, input_condition=AND_1)
    IfAttackedWithDamageType(OR_1, attacked_entity=34140850, attacker=PLAYER)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableNetworkFlag(34140851)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=34142856)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Wait(1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(34142855)
    EnableCharacter(34140850)
    EnableCharacter(34140851)
    EnableAI(34140850)
    EnableAI(34140851)
    SetNetworkUpdateRate(34140850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(34140851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(34140850, name=902140000, bar_slot=1)
    EnableBossHealthBar(34140851, name=902140001)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(34142865)
def Event_34142865():
    """Event 34142865"""
    EndIfFlagEnabled(34140865)
    IfFlagEnabled(MAIN, 34140850)
    Unknown_2003_68(unknown1=-1, unknown2=-1.0, unknown3=0)
    Wait(4.0)
    AddSpecialEffect(20000, 8870)
    Wait(2.0)
    EnableFlag(34140865)
    WarpToMap(game_map=DIVINE_TOWER_OF_EAST_ALTUS, player_start=34142852)


@RestartOnRest(34142870)
def Event_34142870():
    """Event 34142870"""
    DisableNetworkSync()
    EndIfFlagEnabled(34140850)
    IfFlagEnabled(AND_1, 34142885)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    IfCharacterInsideRegion(AND_2, character=PLAYER, region=34142870)
    IfConditionTrue(MAIN, input_condition=AND_2)
    Unknown_2003_68(unknown1=4, unknown2=10.0, unknown3=0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(2.0)
    Unknown_2004_74(
        character=PLAYER,
        unknown1=1,
        region=34142851,
        unknown2=-1,
        character_2=PLAYER,
        unknown3=0,
        unknown4=1,
    )
    Unknown_2003_68(unknown1=0, unknown2=-1.0, unknown3=0)
    Unknown_2003_76(
        unk_0_4=237109504,
        unk_4_8=0,
        unk_8_12=481.9800109863281,
        unk_12_16=26.1299991607666,
        unk_16_20=-267.3299865722656,
    )


@RestartOnRest(34142875)
def Event_34142875():
    """Event 34142875"""
    EndIfFlagDisabled(34140850)
    MoveRemains(source_region=34142875, destination_region=34142876)


@NeverRestart(34142899)
def Event_34142899():
    """Event 34142899"""
    RunCommonEvent(0, 9005822, args=(34140850, 921200, 34142855, 34142856, 0, 0, 0, 0), arg_types="IiIIIIii")


@RestartOnRest(34140700)
def Event_34140700():
    """Event 34140700"""
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(34149200)
    IfFlagEnabled(MAIN, 11109687)
    IfCharacterInsideRegion(MAIN, character=20000, region=34142700)
    EnableFlag(34149200)
