"""
Southeast Mountaintops (SW) (SW)

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_52_52_00_entities import *
from .entities.m60_52_53_00_entities import Assets as m60_52_Assets, Characters as m60_52_Characters


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
        value_8=0,
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
        value_8=0,
    )
    Event_1052522817()
    Event_1052522849()


@RestartOnRest(1052520800)
def Event_1052520800():
    """Event 1052520800"""
    if FlagEnabled(1252520800):
        return
    
    MAIN.Await(HealthValue(Characters.FireGiant1) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.FireGiant1, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.FireGiant1))
    
    Wait(4.0)
    KillBossAndDisplayBanner(character=Characters.FireGiant1, banner_type=BannerType.LegendFelled)
    EnableFlag(1252520800)
    EnableFlag(9131)
    if PlayerInOwnWorld():
        EnableFlag(61131)


@RestartOnRest(1052522810)
def Event_1052522810():
    """Event 1052522810"""
    GotoIfFlagDisabled(Label.L0, flag=1252520800)
    DisableCharacter(1052525800)
    DisableAnimations(1052525800)
    Kill(1052525800, award_runes=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(Characters.FireGiant1)
    DisableAnimations(Characters.FireGiant1)
    DisableAI(Characters.FireGiant1)
    DisableAI(Characters.FireGiant0)
    SetLockOnPoint(character=Characters.FireGiant1, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.FireGiant1, lock_on_model_point=222, state=False)
    SetLockOnPoint(character=Characters.FireGiant1, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.FireGiant1, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.FireGiant1, lock_on_model_point=227, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=221, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=223, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=224, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=225, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=226, state=False)
    SetLockOnPoint(character=Characters.FireGiant0, lock_on_model_point=227, state=False)
    GotoIfFlagEnabled(Label.L1, flag=1252520801)
    if PlayerInOwnWorld():
        DisableFlag(1252520804)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiant0, attacker=0))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiant0, other_entity=PLAYER, radius=120.0))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiant0, other_entity=m60_52_Characters.LivingPot0, radius=120.0))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiant0, other_entity=m60_52_Characters.LivingPot1, radius=120.0))
    
    MAIN.Await(OR_1)
    
    EnableFlag(1252520801)
    if PlayerInOwnWorld():
        BanishInvaders(unknown=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiant0, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiant0, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiant0, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiant0, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiant0, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.FireGiant0, state_info=260))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiant0, other_entity=PLAYER, radius=120.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532800))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=1052532801))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1252522805))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableNetworkFlag(1252520804)
    ReferDamageToEntity(Characters.FireGiant0, target_entity=Characters.FireGiant1)
    EnableAI(Characters.FireGiant0)
    EnableBossHealthBar(Characters.FireGiant1, name=904760000)
    DisableHealthBar(Characters.FireGiant0)
    SetNetworkUpdateRate(Characters.FireGiant0, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(1052522811)
def Event_1052522811():
    """Event 1052522811"""
    if FlagEnabled(1252520800):
        return
    
    MAIN.Await(HealthRatio(Characters.FireGiant0) <= 0.0)
    
    SetTeamType(Characters.FireGiant0, TeamType.Object)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
            cutscene_id=60520010,
            cutscene_flags=0,
            move_to_region=1052522810,
            map_id=60525200,
            player_id=10000,
            unk_16_20=65001,
            unk_20_21=False,
            update_stable_position=False,
        )
    else:
        PlayCutscene(60520010, cutscene_flags=0, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    if PlayerInOwnWorld():
        SetCameraAngle(x_angle=-32.529998779296875, y_angle=-43.560001373291016)
    EnableCharacter(Characters.FireGiant1)
    WaitFrames(frames=1)
    ForceAnimation(Characters.FireGiant1, 20000)
    Move(
        Characters.FireGiant1,
        destination=1052522815,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=Characters.FireGiant0,
    )
    EnableGravity(Characters.FireGiant1)
    WaitFrames(frames=1)
    DisableCharacter(Characters.FireGiant0)
    DisableAnimations(Characters.FireGiant0)
    WaitFrames(frames=1)
    EnableAnimations(Characters.FireGiant1)
    EnableFlag(1252522802)


@NeverRestart(1052522812)
def Event_1052522812():
    """Event 1052522812"""
    if FlagEnabled(1252520800):
        return
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.FireGiant1, attacker=0))
    OR_1.Add(EntityWithinDistance(entity=Characters.FireGiant1, other_entity=PLAYER, radius=70.0))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1252522802))
    
    MAIN.Await(AND_1)
    
    EnableAI(Characters.FireGiant1)
    SetNetworkUpdateRate(Characters.FireGiant1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitFrames(frames=1)
    AddSpecialEffect(Characters.FireGiant1, 12780)


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
    if FlagEnabled(1252520800):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterBackreadEnabled(Characters.FireGiant0))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(
        Characters.FireGiant0,
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
    OR_10.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value)
    
    MAIN.Await(OR_10)
    
    EnableNetworkFlag(1052522820)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(Characters.FireGiant0, 12730)
    OR_11.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_1)
    
    MAIN.Await(OR_11)
    
    EnableNetworkFlag(1052522820)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(Characters.FireGiant0, 12731)
    OR_12.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_2)
    
    MAIN.Await(OR_12)
    
    EnableNetworkFlag(1052522822)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(Characters.FireGiant0, 12732)
    OR_13.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_3)
    
    MAIN.Await(OR_13)
    
    EnableNetworkFlag(1052522823)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(Characters.FireGiant0, 12733)
    OR_14.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_4)
    
    MAIN.Await(OR_14)
    
    EnableNetworkFlag(1052522824)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(Characters.FireGiant0, 12734)
    OR_15.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_5)
    
    MAIN.Await(OR_15)
    
    EnableNetworkFlag(1052522825)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(Characters.FireGiant0, 12735)
    AND_10.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_6)
    
    MAIN.Await(AND_10)
    
    EnableNetworkFlag(1052522826)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(Characters.FireGiant0, 12736)
    AND_11.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_7)
    
    MAIN.Await(AND_11)
    
    EnableNetworkFlag(1052522827)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(Characters.FireGiant0, 12737)
    AND_12.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=9) <= value_8)
    
    MAIN.Await(AND_12)
    
    EnableNetworkFlag(1052522828)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=110,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(Characters.FireGiant0, 12738)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    if CharacterHasSpecialEffect(character=Characters.FireGiant0, special_effect=12752):
        return
    AddSpecialEffect(Characters.FireGiant0, 12750)


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
    if FlagEnabled(1252520800):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterBackreadEnabled(Characters.FireGiant0))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(
        Characters.FireGiant0,
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
    OR_10.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value)
    
    MAIN.Await(OR_10)
    
    EnableNetworkFlag(1052522830)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 10 --- #
    DefineLabel(10)
    AddSpecialEffect(Characters.FireGiant0, 12740)
    OR_11.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_1)
    
    MAIN.Await(OR_11)
    
    EnableNetworkFlag(1052522831)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 11 --- #
    DefineLabel(11)
    AddSpecialEffect(Characters.FireGiant0, 12741)
    OR_12.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_2)
    
    MAIN.Await(OR_12)
    
    EnableNetworkFlag(1052522832)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 12 --- #
    DefineLabel(12)
    AddSpecialEffect(Characters.FireGiant0, 12742)
    OR_13.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_3)
    
    MAIN.Await(OR_13)
    
    EnableNetworkFlag(1052522833)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 13 --- #
    DefineLabel(13)
    AddSpecialEffect(Characters.FireGiant0, 12743)
    OR_14.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_4)
    
    MAIN.Await(OR_14)
    
    EnableNetworkFlag(1052522834)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 14 --- #
    DefineLabel(14)
    AddSpecialEffect(Characters.FireGiant0, 12744)
    OR_15.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_5)
    
    MAIN.Await(OR_15)
    
    EnableNetworkFlag(1052522835)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 15 --- #
    DefineLabel(15)
    AddSpecialEffect(Characters.FireGiant0, 12745)
    AND_10.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_6)
    
    MAIN.Await(AND_10)
    
    EnableNetworkFlag(1052522836)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 16 --- #
    DefineLabel(16)
    AddSpecialEffect(Characters.FireGiant0, 12746)
    AND_11.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_7)
    
    MAIN.Await(AND_11)
    
    EnableNetworkFlag(1052522837)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 17 --- #
    DefineLabel(17)
    AddSpecialEffect(Characters.FireGiant0, 12747)
    AND_12.Add(CharacterPartHealth(Characters.FireGiant0, npc_part_id=8) <= value_8)
    
    MAIN.Await(AND_12)
    
    EnableNetworkFlag(1052522838)
    CreateTemporaryVFX(
        vfx_id=647605,
        anchor_entity=Characters.FireGiant0,
        model_point=111,
        anchor_type=CoordEntityType.Character,
    )

    # --- Label 18 --- #
    DefineLabel(18)
    AddSpecialEffect(Characters.FireGiant0, 12748)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    if CharacterHasSpecialEffect(character=Characters.FireGiant0, special_effect=12752):
        return
    AddSpecialEffect(Characters.FireGiant0, 12750)


@RestartOnRest(1052522817)
def Event_1052522817():
    """Event 1052522817"""
    if FlagEnabled(1252520800):
        return
    OR_1.Add(CharacterHasSpecialEffect(Characters.FireGiant0, 12752))
    
    MAIN.Await(OR_1)
    
    SetNPCPartHealth(Characters.FireGiant0, npc_part_id=8, desired_health=0, overwrite_max=False)
    SetNPCPartHealth(Characters.FireGiant0, npc_part_id=9, desired_health=0, overwrite_max=False)
    WaitFrames(frames=1)
    CreateNPCPart(
        Characters.FireGiant0,
        npc_part_id=8,
        part_index=NPCPartType.Part8,
        part_health=99999,
        body_damage_correction=2.0,
    )
    CreateNPCPart(
        Characters.FireGiant0,
        npc_part_id=9,
        part_index=NPCPartType.Part9,
        part_health=99999,
        body_damage_correction=2.0,
    )


@RestartOnRest(1052522849)
def Event_1052522849():
    """Event 1052522849"""
    CommonFunc_9005800(
        0,
        flag=1252520800,
        entity=m60_52_Assets.AEG099_002_9000,
        region=1052532800,
        flag_1=1252522805,
        character=1052525800,
        action_button_id=10000,
        left=1252520801,
        region_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=1252520800,
        entity=m60_52_Assets.AEG099_003_9001,
        region=1052532801,
        flag_1=1252522805,
        character=1052525800,
        action_button_id=10000,
        left=1252520801,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=1252520800,
        entity=m60_52_Assets.AEG099_002_9000,
        region=1052532800,
        flag_1=1252522805,
        flag_2=1252522806,
        action_button_id=10000,
    )
    CommonFunc_9005801(
        0,
        flag=1252520800,
        entity=m60_52_Assets.AEG099_003_9001,
        region=1052532801,
        flag_1=1252522805,
        flag_2=1252522806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=1252520800, asset=m60_52_Assets.AEG099_002_9000, model_point=9, right=1252520804)
    CommonFunc_9005811(0, flag=1252520800, asset=m60_52_Assets.AEG099_003_9001, model_point=10, right=1252520804)
    CommonFunc_9005811(0, flag=1252520800, asset=Assets.AEG099_019_1000, model_point=0, right=1252520804)
    CommonFunc_9005811(0, flag=1252520800, asset=m60_52_Assets.AEG099_017_1000, model_point=0, right=1252520804)
    CommonFunc_9005822(0, 1252520800, 476000, 1252522805, 1252522806, 0, 1252522802, 1, 1)
