"""
linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1052520800()
    Event_1052522810()
    Event_1052522811()
    Event_1052522812()
    Event_1052522815(
        0,
        part_health=225,
        value=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0
    )
    Event_1052522816(
        0,
        part_health=225,
        value=200,
        value_1=175,
        value_2=150,
        value_3=125,
        value_4=100,
        value_5=75,
        value_6=50,
        value_7=25,
        value_8=0
    )
    Event_1052522817()
    Event_1052522849()


@RestartOnRest(1052520800)
def Event_1052520800():
    """Event 1052520800"""
    EndIfFlagEnabled(1252520800)
    IfHealthValueLessThanOrEqual(MAIN, 1052520800, value=0)
    Wait(4.0)
    PlaySoundEffect(1052520800, 888880000, sound_type=SoundType.s_SFX)
    IfCharacterDead(MAIN, 1052520800)
    Wait(4.0)
    KillBossAndDisplayBanner(character=1052520800, banner_type=BannerType.HollowArenaWin)
    EnableFlag(1252520800)
    EnableFlag(9131)
    SkipLinesIfPlayerNotInOwnWorld(1)
    EnableFlag(61131)


@RestartOnRest(1052522810)
def Event_1052522810():
    """Event 1052522810"""
    GotoIfFlagDisabled(Label.L0, flag=1252520800)
    DisableCharacter(1052525800)
    DisableAnimations(1052525800)
    Kill(1052525800, award_souls=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(1052520800)
    DisableAnimations(1052520800)
    DisableAI(1052520800)
    DisableAI(1052520801)
    SetLockOnPoint(character=1052520800, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=1052520800, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=1052520800, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=1052520800, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=1052520800, lock_on_model_point=227, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=1052520801, lock_on_model_point=227, state=False)
    GotoIfFlagEnabled(Label.L1, flag=1252520801)
    SkipLinesIfPlayerNotInOwnWorld(1)
    DisableFlag(1252520804)
    IfAttackedWithDamageType(OR_1, attacked_entity=1052520801, attacker=0)
    IfEntityWithinDistance(OR_1, entity=1052520801, other_entity=PLAYER, radius=120.0)
    IfEntityWithinDistance(OR_1, entity=1052520801, other_entity=1052530700, radius=120.0)
    IfEntityWithinDistance(OR_1, entity=1052520801, other_entity=1052530701, radius=120.0)
    IfConditionTrue(MAIN, input_condition=OR_1)
    EnableFlag(1252520801)
    SkipLinesIfPlayerNotInOwnWorld(1)
    BanishInvaders(unknown=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    IfAttackedWithDamageType(OR_1, attacked_entity=1052520801, attacker=0)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=436, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=2, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=5, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=6, unk_12_16=1)
    IfUnknownCharacterCondition_34(OR_1, character=1052520801, unk_8_12=260, unk_12_16=1)
    IfEntityWithinDistance(OR_1, entity=1052520801, other_entity=PLAYER, radius=120.0)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1052532800)
    IfCharacterInsideRegion(OR_2, character=PLAYER, region=1052532801)
    IfConditionTrue(AND_2, input_condition=OR_2)
    IfFlagEnabled(AND_2, 1252522805)
    IfConditionTrue(OR_1, input_condition=AND_2)
    IfConditionTrue(MAIN, input_condition=OR_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(1252520804)
    ReferDamageToEntity(1052520801, target_entity=1052520800)
    EnableAI(1052520801)
    EnableBossHealthBar(1052520800, name=904760000)
    DisableHealthBar(1052520801)
    SetNetworkUpdateRate(1052520801, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(1052522811)
def Event_1052522811():
    """Event 1052522811"""
    EndIfFlagEnabled(1252520800)
    IfHealthRatioLessThanOrEqual(MAIN, 1052520801, value=0.0)
    SetTeamType(1052520801, TeamType.Object)
    SkipLinesIfPlayerNotInOwnWorld(2)
    UnknownCutscene_13(
        cutscene_id=60520010,
        cutscene_flags=0,
        respawn_point=1052522810,
        move_to_region=60525200,
        player_id=10000,
        unk_16_20=65001,
        unk_20_24=0,
    )
    SkipLines(1)
    PlayCutscene(60520010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    SkipLinesIfPlayerNotInOwnWorld(1)
    UnknownCamera_4(unknown1=-32.529998779296875, unknown2=-43.560001373291016)
    EnableCharacter(1052520800)
    WaitFrames(frames=1)
    ForceAnimation(1052520800, 20000, unknown2=1.0)
    Move(1052520800, destination=1052522815, destination_type=CoordEntityType.Region, copy_draw_parent=1052520801)
    EnableGravity(1052520800)
    WaitFrames(frames=1)
    DisableCharacter(1052520801)
    DisableAnimations(1052520801)
    WaitFrames(frames=1)
    EnableAnimations(1052520800)
    EnableFlag(1252522802)


@NeverRestart(1052522812)
def Event_1052522812():
    """Event 1052522812"""
    EndIfFlagEnabled(1252520800)
    IfAttackedWithDamageType(OR_1, attacked_entity=1052520800, attacker=0)
    IfEntityWithinDistance(OR_1, entity=1052520800, other_entity=PLAYER, radius=70.0)
    IfConditionTrue(AND_1, input_condition=OR_1)
    IfFlagEnabled(AND_1, 1252522802)
    IfConditionTrue(MAIN, input_condition=AND_1)
    EnableAI(1052520800)
    SetNetworkUpdateRate(1052520800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    AddSpecialEffect(1052520800, 12780)


@RestartOnRest(1052522815)
def Event_1052522815(
    _,
    part_health: int,
    value: int,
    value_1: int,
    value_2: int,
    value_3: int,
    value_4: int,
    value_5: int,
    value_6: int,
    value_7: int,
    value_8: int,
):
    """Event 1052522815"""
    EndIfFlagEnabled(1252520800)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(AND_1, 1052520801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateNPCPart(
        1052520801,
        npc_part_id=9,
        part_index=NPCPartType.Part9,
        part_health=part_health,
        body_damage_correction=1.5,
    )
    GotoIfFlagEnabled(Label.L18, flag=1052522828)
    GotoIfFlagEnabled(Label.L17, flag=1052522827)
    GotoIfFlagEnabled(Label.L16, flag=1052522826)
    GotoIfFlagEnabled(Label.L15, flag=1052522825)
    GotoIfFlagEnabled(Label.L14, flag=1052522824)
    GotoIfFlagEnabled(Label.L13, flag=1052522823)
    GotoIfFlagEnabled(Label.L12, flag=1052522822)
    GotoIfFlagEnabled(Label.L11, flag=1052522821)
    GotoIfFlagEnabled(Label.L10, flag=1052522820)
    IfCharacterPartHealthLessThanOrEqual(OR_10, 1052520801, npc_part_id=9, value=value)
    IfConditionTrue(MAIN, input_condition=OR_10)
    EnableNetworkFlag(1052522820)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(1052520801, 12730)
    IfCharacterPartHealthLessThanOrEqual(OR_11, 1052520801, npc_part_id=9, value=value_1)
    IfConditionTrue(MAIN, input_condition=OR_11)
    EnableNetworkFlag(1052522820)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(1052520801, 12731)
    IfCharacterPartHealthLessThanOrEqual(OR_12, 1052520801, npc_part_id=9, value=value_2)
    IfConditionTrue(MAIN, input_condition=OR_12)
    EnableNetworkFlag(1052522822)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(1052520801, 12732)
    IfCharacterPartHealthLessThanOrEqual(OR_13, 1052520801, npc_part_id=9, value=value_3)
    IfConditionTrue(MAIN, input_condition=OR_13)
    EnableNetworkFlag(1052522823)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(1052520801, 12733)
    IfCharacterPartHealthLessThanOrEqual(OR_14, 1052520801, npc_part_id=9, value=value_4)
    IfConditionTrue(MAIN, input_condition=OR_14)
    EnableNetworkFlag(1052522824)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(1052520801, 12734)
    IfCharacterPartHealthLessThanOrEqual(OR_15, 1052520801, npc_part_id=9, value=value_5)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableNetworkFlag(1052522825)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(1052520801, 12735)
    IfCharacterPartHealthLessThanOrEqual(AND_10, 1052520801, npc_part_id=9, value=value_6)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EnableNetworkFlag(1052522826)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(1052520801, 12736)
    IfCharacterPartHealthLessThanOrEqual(AND_11, 1052520801, npc_part_id=9, value=value_7)
    IfConditionTrue(MAIN, input_condition=AND_11)
    EnableNetworkFlag(1052522827)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(1052520801, 12737)
    IfCharacterPartHealthLessThanOrEqual(AND_12, 1052520801, npc_part_id=9, value=value_8)
    IfConditionTrue(MAIN, input_condition=AND_12)
    EnableNetworkFlag(1052522828)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=110, anchor_type=CoordEntityType.Character)

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(1052520801, 12738)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EndIfCharacterHasSpecialEffect(character=1052520801, special_effect=12752)
    AddSpecialEffect(1052520801, 12750)


@RestartOnRest(1052522816)
def Event_1052522816(
    _,
    part_health: int,
    value: int,
    value_1: int,
    value_2: int,
    value_3: int,
    value_4: int,
    value_5: int,
    value_6: int,
    value_7: int,
    value_8: int,
):
    """Event 1052522816"""
    EndIfFlagEnabled(1252520800)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(AND_1, 1052520801)
    IfConditionTrue(MAIN, input_condition=AND_1)
    CreateNPCPart(
        1052520801,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=part_health,
        body_damage_correction=1.5,
    )
    GotoIfFlagEnabled(Label.L18, flag=1052522838)
    GotoIfFlagEnabled(Label.L17, flag=1052522837)
    GotoIfFlagEnabled(Label.L16, flag=1052522836)
    GotoIfFlagEnabled(Label.L15, flag=1052522835)
    GotoIfFlagEnabled(Label.L14, flag=1052522834)
    GotoIfFlagEnabled(Label.L13, flag=1052522833)
    GotoIfFlagEnabled(Label.L12, flag=1052522832)
    GotoIfFlagEnabled(Label.L11, flag=1052522831)
    GotoIfFlagEnabled(Label.L10, flag=1052522830)
    IfCharacterPartHealthLessThanOrEqual(OR_10, 1052520801, npc_part_id=8, value=value)
    IfConditionTrue(MAIN, input_condition=OR_10)
    EnableNetworkFlag(1052522830)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(1052520801, 12740)
    IfCharacterPartHealthLessThanOrEqual(OR_11, 1052520801, npc_part_id=8, value=value_1)
    IfConditionTrue(MAIN, input_condition=OR_11)
    EnableNetworkFlag(1052522831)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(1052520801, 12741)
    IfCharacterPartHealthLessThanOrEqual(OR_12, 1052520801, npc_part_id=8, value=value_2)
    IfConditionTrue(MAIN, input_condition=OR_12)
    EnableNetworkFlag(1052522832)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(1052520801, 12742)
    IfCharacterPartHealthLessThanOrEqual(OR_13, 1052520801, npc_part_id=8, value=value_3)
    IfConditionTrue(MAIN, input_condition=OR_13)
    EnableNetworkFlag(1052522833)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(1052520801, 12743)
    IfCharacterPartHealthLessThanOrEqual(OR_14, 1052520801, npc_part_id=8, value=value_4)
    IfConditionTrue(MAIN, input_condition=OR_14)
    EnableNetworkFlag(1052522834)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(1052520801, 12744)
    IfCharacterPartHealthLessThanOrEqual(OR_15, 1052520801, npc_part_id=8, value=value_5)
    IfConditionTrue(MAIN, input_condition=OR_15)
    EnableNetworkFlag(1052522835)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(1052520801, 12745)
    IfCharacterPartHealthLessThanOrEqual(AND_10, 1052520801, npc_part_id=8, value=value_6)
    IfConditionTrue(MAIN, input_condition=AND_10)
    EnableNetworkFlag(1052522836)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(1052520801, 12746)
    IfCharacterPartHealthLessThanOrEqual(AND_11, 1052520801, npc_part_id=8, value=value_7)
    IfConditionTrue(MAIN, input_condition=AND_11)
    EnableNetworkFlag(1052522837)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(1052520801, 12747)
    IfCharacterPartHealthLessThanOrEqual(AND_12, 1052520801, npc_part_id=8, value=value_8)
    IfConditionTrue(MAIN, input_condition=AND_12)
    EnableNetworkFlag(1052522838)
    CreateTemporaryVFX(vfx_id=647605, anchor_entity=1052520801, model_point=111, anchor_type=CoordEntityType.Character)

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(1052520801, 12748)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EndIfCharacterHasSpecialEffect(character=1052520801, special_effect=12752)
    AddSpecialEffect(1052520801, 12750)


@RestartOnRest(1052522817)
def Event_1052522817():
    """Event 1052522817"""
    EndIfFlagEnabled(1252520800)
    IfCharacterHasSpecialEffect(OR_1, 1052520801, 12752)
    IfConditionTrue(MAIN, input_condition=OR_1)
    SetNPCPartHealth(1052520801, npc_part_id=8, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(1052520801, npc_part_id=9, desired_health=0, overwrite_max=False)
    WaitFrames(frames=1)
    CreateNPCPart(
        1052520801,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=99999,
        body_damage_correction=2.0,
    )
    CreateNPCPart(
        1052520801,
        npc_part_id=9,
        part_index=NPCPartType.Part9,
        part_health=99999,
        body_damage_correction=2.0,
    )


@RestartOnRest(1052522849)
def Event_1052522849():
    """Event 1052522849"""
    RunCommonEvent(
        0,
        9005800,
        args=(1252520800, 1052531800, 1052532800, 1252522805, 1052525800, 10000, 1252520801, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005800,
        args=(1252520800, 1052531801, 1052532801, 1252522805, 1052525800, 10000, 1252520801, 0),
        arg_types="IIIIIiII",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1252520800, 1052531800, 1052532800, 1252522805, 1252522806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(
        0,
        9005801,
        args=(1252520800, 1052531801, 1052532801, 1252522805, 1252522806, 10000),
        arg_types="IIIIIi",
    )
    RunCommonEvent(0, 9005811, args=(1252520800, 1052531800, 9, 1252520804), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1252520800, 1052531801, 10, 1252520804), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1252520800, 1052521800, 0, 1252520804), arg_types="IIiI")
    RunCommonEvent(0, 9005811, args=(1252520800, 1052531802, 0, 1252520804), arg_types="IIiI")
    RunCommonEvent(
        0,
        9005822,
        args=(1252520800, 476000, 1252522805, 1252522806, 0, 1252522802, 1, 1),
        arg_types="IiIIIIii",
    )
