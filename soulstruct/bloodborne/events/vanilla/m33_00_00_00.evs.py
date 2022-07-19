"""
Nightmare Frontier

linked:
162

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_邪神
78: ボス_戦闘開始
94: ボス戦_撃破時間
112: ギミック_エレベーター起動
140: PC情報_故郷到達時
162: N:\\SPRJ\\data\\Param\\event\\common.emevd
238: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=50, args=(3300950, 3301950, 999, 13307800))
    RunEvent(7000, slot=51, args=(3300951, 3301951, 13301800, 13307820))
    RunEvent(7100, slot=50, args=(73300200, 3301950))
    RunEvent(7100, slot=51, args=(73300201, 3301951))
    RunEvent(7200, slot=50, args=(73300100, 3301950, 2102953))
    RunEvent(7200, slot=51, args=(73300101, 3301951, 2102953))
    RunEvent(7300, slot=50, args=(72103300, 3301950))
    RunEvent(7300, slot=51, args=(72103301, 3301951))
    RunEvent(9200, slot=10, args=(3303900,))
    DisableSoundEvent(sound_id=3304000)
    DisableSoundEvent(sound_id=3304001)
    StartPlayLogMeasurement(measurement_id=3300000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=3300001, name=18, overwrite=True)
    Event_13300990()
    CreateObjectVFX(3301020, vfx_id=100, model_point=8028)
    CreateObjectVFX(3301022, vfx_id=100, model_point=8028)
    CreateObjectVFX(3301023, vfx_id=100, model_point=8028)
    CreateObjectVFX(3301024, vfx_id=100, model_point=8028)
    CreateObjectVFX(3301025, vfx_id=100, model_point=8028)
    ForceAnimation(3301020, 200, loop=True)
    ForceAnimation(3301022, 200, loop=True)
    ForceAnimation(3301023, 200, loop=True)
    ForceAnimation(3301024, 200, loop=True)
    ForceAnimation(3301025, 200, loop=True)
    Event_13304872()
    Event_13304873()
    Event_13301800()
    Event_13301801()
    Event_13301802()
    Event_13304870()
    Event_13304871()
    Event_13304802()
    Event_13304803(slot=1)
    Event_13304804()
    Event_13304805()
    Event_13304807()
    Event_13304808()
    Event_13301803()
    Event_13304820(0, npc_part_id=3311, npc_part_id_1=3311, part_index=13, bit_index=9, bit_index_1=13)
    Event_13304820(1, npc_part_id=3322, npc_part_id_1=3322, part_index=14, bit_index=8, bit_index_1=14)
    Event_13304830(
        0,
        npc_part_id=3301,
        npc_part_id_1=3301,
        part_index=4,
        special_effect_id=482,
        part_health=200,
        animation_id=8020,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        1,
        npc_part_id=3302,
        npc_part_id_1=3302,
        part_index=6,
        special_effect_id=482,
        part_health=180,
        animation_id=8020,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        2,
        npc_part_id=3303,
        npc_part_id_1=3303,
        part_index=8,
        special_effect_id=482,
        part_health=150,
        animation_id=8020,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        3,
        npc_part_id=3304,
        npc_part_id_1=3304,
        part_index=5,
        special_effect_id=481,
        part_health=200,
        animation_id=8010,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        4,
        npc_part_id=3305,
        npc_part_id_1=3305,
        part_index=7,
        special_effect_id=481,
        part_health=150,
        animation_id=8010,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        5,
        npc_part_id=3306,
        npc_part_id_1=3306,
        part_index=9,
        special_effect_id=481,
        part_health=120,
        animation_id=8010,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        6,
        npc_part_id=3307,
        npc_part_id_1=3307,
        part_index=10,
        special_effect_id=481,
        part_health=120,
        animation_id=8010,
        body_damage_correction__damage_correction=1.0,
        body_damage_correction=1.5,
    )
    Event_13304830(
        7,
        npc_part_id=3308,
        npc_part_id_1=3308,
        part_index=3,
        special_effect_id=483,
        part_health=200,
        animation_id=8030,
        body_damage_correction__damage_correction=0.20000000298023224,
        body_damage_correction=0.30000001192092896,
    )
    Event_13304830(
        8,
        npc_part_id=3309,
        npc_part_id_1=3309,
        part_index=11,
        special_effect_id=484,
        part_health=100,
        animation_id=8040,
        body_damage_correction__damage_correction=0.20000000298023224,
        body_damage_correction=0.30000001192092896,
    )
    Event_13304830(
        9,
        npc_part_id=3310,
        npc_part_id_1=3310,
        part_index=12,
        special_effect_id=483,
        part_health=100,
        animation_id=8030,
        body_damage_correction__damage_correction=0.20000000298023224,
        body_damage_correction=0.30000001192092896,
    )
    Event_13304840()
    Event_13300100()
    Event_13300110()
    Event_13300111()
    Event_13300112()
    Event_13300113()
    Event_13300120()
    Event_13300130(0, character=3300551, flag=53300990)
    Event_13300130(1, character=3300590, flag=53300980)
    Event_13300130(2, character=3300591, flag=53300970)
    Event_13300130(3, character=3300555, flag=53300960)
    Event_13300130(4, character=3300558, flag=53300940)
    Event_13300130(5, character=3300560, flag=53300930)
    Event_13300130(6, character=3300561, flag=53300920)
    Event_13300130(7, character=3300562, flag=53300910)
    Event_13300130(8, character=3300565, flag=53300890)
    Event_13300130(9, character=3300569, flag=53300870)
    Event_13300130(10, character=3300573, flag=53300850)
    Event_13300130(11, character=3300575, flag=53300830)
    Event_13300130(12, character=3300576, flag=53300820)
    Event_13300130(13, character=3300578, flag=53300800)
    Event_13300130(14, character=3300581, flag=53300790)
    Event_13300130(15, character=3300582, flag=53300780)
    Event_13300130(16, character=3300583, flag=53300770)
    Event_13300130(17, character=3300587, flag=53300750)
    Event_13300130(18, character=3300588, flag=53300740)
    Event_13300130(19, character=3300589, flag=53300730)
    Event_13300130(20, character=3300593, flag=53300700)
    Event_13300130(21, character=3300250, flag=53300690)
    Event_13300130(22, character=3300251, flag=53300680)
    Event_13300130(23, character=3300252, flag=53300670)
    Event_13300130(24, character=3300253, flag=53300660)
    Event_13300130(25, character=3300254, flag=53300650)
    Event_13300130(26, character=3300257, flag=53300640)
    Event_13300130(27, character=3300258, flag=53300630)
    Event_13300130(28, character=3300259, flag=53300620)
    Event_13300130(29, character=3300261, flag=53300610)
    Event_13300130(30, character=3300262, flag=53300600)
    Event_13300200()
    Event_13300210()
    Event_13300220(0, character=3300721)
    Event_13300220(1, character=3300722)
    Event_13305150(0, character=3300411, region=3302205, radius=5.0, frames=0)
    Event_13305150(1, character=3300412, region=3302205, radius=5.0, frames=0)
    Event_13305150(2, character=3300452, region=3302205, radius=5.0, frames=0)
    Event_13305150(3, character=3300459, region=3302205, radius=5.0, frames=0)
    Event_13305150(4, character=3300500, region=3302206, radius=15.0, frames=0)
    Event_13305150(5, character=3300502, region=3302207, radius=2.0, frames=450)
    Event_13305150(6, character=3300413, region=3302210, radius=5.0, frames=0)
    Event_13305150(7, character=3300460, region=3302210, radius=5.0, frames=0)
    Event_13305150(8, character=3300413, region=3302211, radius=5.0, frames=0)
    Event_13305150(9, character=3300460, region=3302211, radius=5.0, frames=0)
    Event_13305210(
        0,
        character=3300102,
        radius=2.0,
        animation_id=7000,
        animation_id_1=7001,
        seconds=0.0,
        ai_param_id=218300,
    )
    Event_13305210(
        1,
        character=3300103,
        radius=2.0,
        animation_id=7000,
        animation_id_1=7001,
        seconds=0.0,
        ai_param_id=218300,
    )
    Event_13305210(
        2,
        character=3300104,
        radius=2.0,
        animation_id=7000,
        animation_id_1=7001,
        seconds=0.0,
        ai_param_id=218300,
    )
    Event_13305220()
    Event_13305230()
    Event_13305200(1, character=3300459, region=3302301, character_1=3300461, radius=5.0, patrol_information_id=3306001)
    Event_13305200(2, character=3300452, region=3302302, character_1=3300460, radius=5.0, patrol_information_id=3306002)
    Event_13305250(0, character=3300584, region=3302410, flag=13305255)
    Event_13305250(1, character=3300593, region=3302411, flag=13305256)
    Event_13305255(0, character=3300584, region=3302410)
    Event_13305255(1, character=3300593, region=3302411)
    Event_13305030(0, character__set_draw_parent=3300500, character=3300520)
    Event_13305030(1, character__set_draw_parent=3300501, character=3300521)
    Event_13305030(2, character__set_draw_parent=3300502, character=3300522)
    Event_13305040()
    Event_13305041()
    Event_13300700()
    Event_13304700(0, character=3300700, flag=13304701, flag_1=13304711, flag_2=3300, flag_3=13301700)
    Event_13304710(0, character=3300700, flag=13304701, flag_1=13304711, flag_2=13304721)
    Event_13304720(0, character=3300700, flag=13304701, flag_1=13304711, flag_2=13304721)
    Event_13304730(0, character=3300700, flag=13304701, flag_1=13304711, flag_2=3300, flag_3=13304800, flag_4=13301700)
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6327):
        EnableFlag(13301999)
    if FlagDisabled(13301999):
        EnableObject(3301500)
        DisableObject(3301501)
        EnableTreasure(obj=3301500)
        DisableTreasure(obj=3301501)
    else:
        DisableObject(3301500)
        EnableObject(3301501)
        DisableTreasure(obj=3301500)
        EnableTreasure(obj=3301501)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6328):
        EnableFlag(13301998)
    if FlagDisabled(13301998):
        EnableObject(3301502)
        DisableObject(3301503)
        EnableTreasure(obj=3301502)
        DisableTreasure(obj=3301503)
    else:
        DisableObject(3301502)
        EnableObject(3301503)
        DisableTreasure(obj=3301502)
        EnableTreasure(obj=3301503)
    AND_13.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_13)
    if FlagEnabled(6329):
        EnableFlag(13301997)
    if FlagDisabled(13301997):
        EnableObject(3301504)
        DisableObject(3301505)
        EnableTreasure(obj=3301504)
        DisableTreasure(obj=3301505)
    else:
        DisableObject(3301504)
        EnableObject(3301505)
        DisableTreasure(obj=3301504)
        EnableTreasure(obj=3301505)
    AND_12.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_12)
    if FlagEnabled(6330):
        EnableFlag(13301996)
    if FlagDisabled(13301996):
        EnableObject(3301506)
        DisableObject(3301507)
        EnableTreasure(obj=3301506)
        DisableTreasure(obj=3301507)
    else:
        DisableObject(3301506)
        EnableObject(3301507)
        DisableTreasure(obj=3301506)
        EnableTreasure(obj=3301507)
    AND_11.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_11)
    if FlagEnabled(6331):
        EnableFlag(13301995)
    if FlagDisabled(13301995):
        EnableObject(3301508)
        DisableObject(3301509)
        EnableTreasure(obj=3301508)
        DisableTreasure(obj=3301509)
    else:
        DisableObject(3301508)
        EnableObject(3301509)
        DisableTreasure(obj=3301508)
        EnableTreasure(obj=3301509)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(3303950)
    DisableGravity(3303950)
    DisableCharacterCollision(3303950)
    DisableAnimations(3303951)
    DisableGravity(3303951)
    DisableCharacterCollision(3303951)


@RestartOnRest(13304700)
def Event_13304700(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 13304700"""
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(flag):
        return
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    AND_1.Add(Online())
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(PlayerLevel() >= 30)
    if FlagEnabled(flag_3):
        AND_2.Add(ClientTypeCountComparison(
            client_type=ClientType.Coop,
            comparison_type=ComparisonType.GreaterThanOrEqual,
            value=1,
        ))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 9025))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    if FlagEnabled(flag_3):
        DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011, wait_for_completion=True)
    EnableAI(character)
    EnableFlag(flag)


@RestartOnRest(13304710)
def Event_13304710(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13304710"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Invader, comparison_type=ComparisonType.Equal, value=0))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(RandomTimeElapsed(min_seconds=10.0, max_seconds=10.0))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    EnableFlag(flag_2)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(ClientTypeCountComparison(
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    ))
    
    MAIN.Await(OR_1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RemoveSpecialEffect(PLAYER, 9020)
    Restart()


@RestartOnRest(13304720)
def Event_13304720(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13304720"""
    if FlagEnabled(flag_1):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(ClientTypeCountComparison(
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    ))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RemoveSpecialEffect(PLAYER, 9020)
    RemoveSpecialEffect(character, 9100)
    ReplanAI(character)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(13304730)
def Event_13304730(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13304730"""
    OR_15.Add(FlagEnabled(flag_1))
    OR_15.Add(FlagEnabled(flag_2))
    OR_15.Add(FlagEnabled(flag_3))
    if OR_15:
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(HealthRatio(character) == 0.0)
    AND_3.Add(FlagEnabled(flag_3))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_3)
    EnableFlag(flag_4)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@NeverRestart(13301800)
def Event_13301800():
    """Event 13301800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=3303802)
    DisableSoundEvent(sound_id=3303803)
    DisableCharacter(3300800)
    Kill(3300800, award_souls=True)
    DisableObject(3301800)
    DisableObject(3301801)
    DeleteVFX(3303800)
    DeleteVFX(3303801)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(3300800))
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3301800)
    DisableObject(3301801)
    DeleteVFX(3303800)
    DeleteVFX(3303801)
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=3300800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=25)
    AwardItemLot(80000200, host_only=False)
    EnableFlag(3300)
    EnableFlag(9466)
    StopPlayLogMeasurement(measurement_id=3300000)
    StopPlayLogMeasurement(measurement_id=3300001)
    StopPlayLogMeasurement(measurement_id=3300010)
    CreatePlayLog(name=40)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@NeverRestart(13301801)
def Event_13301801():
    """Event 13301801"""
    DisableNetworkSync()
    if FlagEnabled(13301800):
        return
    AND_1.Add(FlagEnabled(13301800))
    AND_2.Add(CharacterBackreadDisabled(3300800))
    AND_2.Add(HealthRatio(3300800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(3302800, 0, sound_type=SoundType.c_CharacterMotion)


@RestartOnRest(13301802)
def Event_13301802():
    """Event 13301802"""
    if FlagEnabled(13301800):
        return
    if ThisEventFlagEnabled():
        return
    DisableCharacterCollision(3300800)
    DisableGravity(3300800)
    EnableInvincibility(3300800)
    ForceAnimation(3300800, 7003, loop=True)
    AND_1.Add(FlagDisabled(13301800))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302805))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13304800)
    ForceAnimation(3300800, 7006)
    WaitFrames(frames=30)
    ForceAnimation(3300800, 7002)
    WaitFrames(frames=160)
    EnableGravity(3300800)
    DisableInvincibility(3300800)
    EnableCharacterCollision(3300800)
    if FlagEnabled(9302):
        return
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(9302)


@NeverRestart(13301803)
def Event_13301803():
    """Event 13301803"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(13304800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableFlag(13304800)
    EnableFlag(13301802)


@NeverRestart(13304870)
def Event_13304870():
    """Event 13304870"""
    if FlagEnabled(13301800):
        return
    GotoIfFlagEnabled(Label.L0, flag=13301802)
    SkipLinesIfClient(2)
    DisableObject(3301800)
    DeleteVFX(3303800, erase_root_only=False)
    DisableObject(3301801)
    DeleteVFX(3303801, erase_root_only=False)
    AND_1.Add(FlagDisabled(13301800))
    AND_1.Add(FlagEnabled(13301802))
    OR_1.Add(AND_1)
    AND_2.Add(FlagDisabled(13301800))
    AND_2.Add(FlagEnabled(13304800))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableObject(3301800)
    EnableObject(3301801)
    CreateVFX(3303800)
    CreateVFX(3303801)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(CharacterHuman(PLAYER))
    AND_3.Add(ActionButtonParamActivated(action_button_id=3300800, entity=3301800))
    AND_3.Add(FlagDisabled(13301800))
    AND_4.Add(FlagEnabled(13301800))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    RotateToFaceEntity(PLAYER, 3302800, animation=101130)
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(CharacterInsideRegion(PLAYER, region=3302801))
    AND_6.Add(CharacterHuman(PLAYER))
    AND_6.Add(TimeElapsed(seconds=2.0))
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_6)
    EnableFlag(13304800)
    Restart()


@RestartOnRest(13304871)
def Event_13304871():
    """Event 13304871"""
    DisableNetworkSync()
    if FlagEnabled(13301800):
        return
    AND_1.Add(FlagDisabled(13301800))
    AND_1.Add(FlagEnabled(13301802))
    AND_1.Add(FlagEnabled(13304800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3300800, entity=3301800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 3302800, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3302801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(13304801)
    Restart()


@NeverRestart(13304872)
def Event_13304872():
    """Event 13304872"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3301800, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(13304873)
def Event_13304873():
    """Event 13304873"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=3301800, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@RestartOnRest(13304802)
def Event_13304802():
    """Event 13304802"""
    if FlagEnabled(13301800):
        return
    DisableAI(3300800)
    DisableHealthBar(3300800)
    
    MAIN.Await(FlagEnabled(13304800))
    
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3300800, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13304800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3300800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3300800)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3300800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=3300800)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(3300800)
    EnableBossHealthBar(3300800, name=512000)
    CreatePlayLog(name=78)
    StartPlayLogMeasurement(measurement_id=3300010, name=94, overwrite=True)


@NeverRestart(13304803)
def Event_13304803():
    """Event 13304803"""
    DisableNetworkSync()
    if FlagEnabled(13301800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=3303802)
    DisableSoundEvent(sound_id=3303803)
    AND_1.Add(FlagDisabled(13301800))
    AND_1.Add(FlagEnabled(13304802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(13304801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=3303802)
    AND_2.Add(CharacterHasTAEEvent(3300800, tae_event_id=10))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(13301800))
    AND_2.Add(FlagEnabled(13304802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(13304801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3302802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=3303802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=3303803)


@NeverRestart(13304804)
def Event_13304804():
    """Event 13304804"""
    if FlagEnabled(13301800):
        return
    DisableNetworkSync()
    AND_1.Add(HealthRatio(3300800) > 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=3300800, radius=14.0))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=1)
    AND_1.Add(HealthRatio(3300800) > 0.0)
    
    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=3300800, radius=17.0))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=NIGHTMARE_FRONTIER, camera_slot=0)
    Restart()


@NeverRestart(13304805)
def Event_13304805():
    """Event 13304805"""
    DisableNetworkSync()
    if FlagEnabled(13301800):
        return
    
    MAIN.Await(FlagEnabled(13301800))
    
    DisableBossMusic(sound_id=3303802)
    DisableBossMusic(sound_id=3303803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(13304807)
def Event_13304807():
    """Event 13304807"""
    if FlagEnabled(13301800):
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(HealthRatio(3300800) < 0.699999988079071)
    
    Wait(0.10000000149011612)
    ResetAnimation(3300800, disable_interpolation=True)
    AICommand(3300800, command_id=100, command_slot=0)
    ReplanAI(3300800)
    
    MAIN.Await(CharacterHasTAEEvent(3300800, tae_event_id=10))
    
    AICommand(3300800, command_id=-1, command_slot=0)
    ReplanAI(3300800)


@NeverRestart(13304808)
def Event_13304808():
    """Event 13304808"""
    if FlagEnabled(13301800):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(HealthRatio(3300800) < 0.30000001192092896)
    AND_1.Add(FlagEnabled(13304807))
    
    MAIN.Await(AND_1)
    
    Wait(0.10000000149011612)
    ResetAnimation(3300800, disable_interpolation=True)
    AICommand(3300800, command_id=110, command_slot=0)
    ReplanAI(3300800)
    
    MAIN.Await(CharacterHasTAEEvent(3300800, tae_event_id=10))
    
    AICommand(3300800, command_id=-1, command_slot=0)
    ReplanAI(3300800)


@RestartOnRest(13304820)
def Event_13304820(_, npc_part_id: short, npc_part_id_1: int, part_index: short, bit_index: uchar, bit_index_1: uchar):
    """Event 13304820"""
    if FlagEnabled(13301800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    SetCollisionMask(3300800, bit_index=bit_index_1, switch_type=OnOffChange.Off)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterHasSpecialEffect(3300800, 5402))
    
    SetCollisionMask(3300800, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(3300800, bit_index=bit_index_1, switch_type=OnOffChange.On)
    CreateNPCPart(
        3300800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartEffects(3300800, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)


@RestartOnRest(13304830)
def Event_13304830(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    special_effect_id: int,
    part_health: int,
    animation_id: int,
    body_damage_correction__damage_correction: float,
    body_damage_correction: float,
):
    """Event 13304830"""
    if FlagEnabled(13301800):
        return
    CreateNPCPart(
        3300800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        damage_correction=body_damage_correction__damage_correction,
        body_damage_correction=body_damage_correction__damage_correction,
    )
    SetNPCPartEffects(3300800, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    AND_2.Add(CharacterPartHealth(3300800, npc_part_id=npc_part_id_1) <= 0)
    AND_3.Add(HealthRatio(3300800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    CreateNPCPart(
        3300800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=body_damage_correction,
    )
    SetNPCPartEffects(3300800, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    WaitFrames(frames=1)
    ResetAnimation(3300800)
    ForceAnimation(3300800, animation_id)
    AddSpecialEffect(3300800, special_effect_id)
    ReplanAI(3300800)
    Wait(30.0)
    AICommand(3300800, command_id=100, command_slot=1)
    ReplanAI(3300800)
    
    MAIN.Await(CharacterHasTAEEvent(3300800, tae_event_id=300))
    
    SetNPCPartHealth(3300800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    RemoveSpecialEffect(3300800, special_effect_id)
    AICommand(3300800, command_id=-1, command_slot=1)
    ReplanAI(3300800)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(13304840)
def Event_13304840():
    """Event 13304840"""
    if FlagEnabled(13301800):
        return
    CreateNPCPart(
        3300800,
        npc_part_id=3300,
        part_index=NPCPartType.Part1,
        part_health=300,
        damage_correction=1.399999976158142,
        body_damage_correction=1.399999976158142,
    )
    SetNPCPartEffects(3300800, npc_part_id=3300, material_sfx_id=60, material_vfx_id=60)
    AND_2.Add(CharacterPartHealth(3300800, npc_part_id=3300) <= 0)
    AND_3.Add(HealthRatio(3300800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    CreateNPCPart(
        3300800,
        npc_part_id=3300,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=2.0999999046325684,
    )
    SetNPCPartEffects(3300800, npc_part_id=3300, material_sfx_id=60, material_vfx_id=60)
    WaitFrames(frames=1)
    ResetAnimation(3300800)
    ForceAnimation(3300800, 8000)
    AddSpecialEffect(3300800, 480)
    ReplanAI(3300800)
    Wait(30.0)
    AICommand(3300800, command_id=100, command_slot=1)
    ReplanAI(3300800)
    
    MAIN.Await(CharacterHasTAEEvent(3300800, tae_event_id=300))
    
    SetNPCPartHealth(3300800, npc_part_id=3300, desired_health=-1, overwrite_max=True)
    RemoveSpecialEffect(3300800, 480)
    AICommand(3300800, command_id=-1, command_slot=1)
    ReplanAI(3300800)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(13300100)
def Event_13300100():
    """Event 13300100"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=3301100, animation_id=1)
        End()
    ForceAnimation(3301100, 0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3302710))
    
    ForceAnimation(3301100, 1)


@NeverRestart(13300110)
def Event_13300110():
    """Event 13300110"""
    AND_1.Add(FlagEnabled(13300115))
    AND_2.Add(FlagDisabled(13300115))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_1)
    EndOfAnimation(obj=3301000, animation_id=6)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)
    SkipLines(3)
    EndOfAnimation(obj=3301000, animation_id=2)
    EnableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    if FlagDisabled(13300111):
        EndOfAnimation(obj=3301000, animation_id=2)
        EnableFlag(13300115)
        DisableObjectActivation(3301010, obj_act_id=3300000)
        DisableObjectActivation(3301011, obj_act_id=3300000)


@NeverRestart(13300111)
def Event_13300111():
    """Event 13300111"""
    if ThisEventSlotFlagEnabled():
        return
    DisableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3302702))
    
    CreatePlayLog(name=112)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)


@NeverRestart(13300112)
def Event_13300112():
    """Event 13300112"""
    AND_3.Add(FlagDisabled(13300115))
    AND_3.Add(FlagEnabled(13300116))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(13300111))
    
    AND_1.Add(FlagDisabled(13300115))
    AND_1.Add(FlagDisabled(13300116))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302700))
    AND_2.Add(FlagDisabled(13300115))
    AND_2.Add(FlagDisabled(13300116))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3302706))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13300116)
    ForceAnimation(3301011, 1)
    ForceAnimation(3301000, 1)
    WaitFrames(frames=10)
    ForceAnimation(3301000, 2)
    WaitFrames(frames=150)
    AND_4.Add(AllPlayersOutsideRegion(region=3302706))
    AND_4.Add(AllPlayersOutsideRegion(region=3302701))
    
    MAIN.Await(AND_4)
    
    ForceAnimation(3301011, 3)
    ForceAnimation(3301000, 3)
    WaitFrames(frames=10)
    EnableFlag(13300115)
    DisableFlag(13300116)
    EnableObjectActivation(3301010, obj_act_id=3300000)
    DisableObjectActivation(3301011, obj_act_id=3300000)
    Restart()


@NeverRestart(13300113)
def Event_13300113():
    """Event 13300113"""
    AND_3.Add(FlagEnabled(13300115))
    AND_3.Add(FlagEnabled(13300116))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(13300111))
    
    AND_1.Add(FlagEnabled(13300115))
    AND_1.Add(FlagDisabled(13300116))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302701))
    AND_2.Add(FlagEnabled(13300115))
    AND_2.Add(FlagDisabled(13300116))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=3302705))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13300116)
    ForceAnimation(3301010, 1)
    ForceAnimation(3301000, 5)
    WaitFrames(frames=10)
    ForceAnimation(3301000, 6)
    WaitFrames(frames=150)
    AND_4.Add(AllPlayersOutsideRegion(region=3302705))
    AND_4.Add(AllPlayersOutsideRegion(region=3302700))
    
    MAIN.Await(AND_4)
    
    ForceAnimation(3301010, 3)
    ForceAnimation(3301000, 7)
    WaitFrames(frames=10)
    DisableFlag(13300115)
    DisableFlag(13300116)
    DisableObjectActivation(3301010, obj_act_id=3300000)
    EnableObjectActivation(3301011, obj_act_id=3300000)
    Restart()


@NeverRestart(13300120)
def Event_13300120():
    """Event 13300120"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DeleteVFX(3303002)
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=3303000))
    
    DeleteVFX(3303010)
    CreateVFX(3303002)
    Wait(4.0)
    CreateVFX(3303010)


@RestartOnRest(13300130)
def Event_13300130(_, character: int, flag: int):
    """Event 13300130"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(0.0)


@NeverRestart(13300200)
def Event_13300200():
    """Event 13300200"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(1431):
        return
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302170))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9180)
    GotoIfMultiplayer(Label.L0)
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(33000000, cutscene_flags=0, player_id=10000, move_to_region=3302171, game_map=NIGHTMARE_FRONTIER)
    SkipLines(1)
    PlayCutscene(33001000, cutscene_flags=0, player_id=10000, move_to_region=3302171, game_map=NIGHTMARE_FRONTIER)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfClient(Label.L2)
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(
        33000000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3302171,
        game_map=NIGHTMARE_FRONTIER,
    )
    SkipLines(1)
    PlayCutscene(
        33001000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=3302171,
        game_map=NIGHTMARE_FRONTIER,
    )
    Goto(Label.L1)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(33000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(1)
    PlayCutscene(33001000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)


@RestartOnRest(13300210)
def Event_13300210():
    """Event 13300210"""
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(13300200))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSoapstoneMessage(3304020)
    DeleteVFX(3303020)


@RestartOnRest(13300220)
def Event_13300220(_, character: int):
    """Event 13300220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DropMandatoryTreasure(character)
    DisableBackread(character)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    DisableBackread(2300720)


@RestartOnRest(13305150)
def Event_13305150(_, character: int, region: int, radius: float, frames: int):
    """Event 13305150"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_3)
    WaitFrames(frames=frames)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(13305030)
def Event_13305030(_, character__set_draw_parent: int, character: int):
    """Event 13305030"""
    DisableGravity(character)
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterBackreadEnabled(character__set_draw_parent))
    
        Wait(1.0)
    AND_1.Add(HealthRatio(character__set_draw_parent) <= 0.0)
    SkipLinesIfConditionFalse(2, AND_1)
    DisableBackread(character)
    End()
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=character__set_draw_parent,
    )
    Restart()


@RestartOnRest(13305040)
def Event_13305040():
    """Event 13305040"""
    DisableNetworkSync()
    AND_10.Add(CharacterHasSpecialEffect(PLAYER, 4691))
    GotoIfConditionTrue(Label.L0, input_condition=AND_10)
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 4690))
    
    Wait(2.0)
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4690))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4690))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13305041)
def Event_13305041():
    """Event 13305041"""
    DisableNetworkSync()
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4690))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 4691))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest(13305200)
def Event_13305200(_, character: int, region: int, character_1: int, radius: float, patrol_information_id: int):
    """Event 13305200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=radius))
    OR_2.Add(CharacterInsideRegion(character, region=region))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character_1, patrol_information_id=patrol_information_id)


@RestartOnRest(13305210)
def Event_13305210(
    _,
    character: int,
    radius: float,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    ai_param_id: int,
):
    """Event 13305210"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=218390)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_3)
    
    Wait(seconds)
    ForceAnimation(character, animation_id_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ReplanAI(character)


@RestartOnRest(13305220)
def Event_13305220():
    """Event 13305220"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=3302150))
    AND_1.Add(FlagDisabled(13305212))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3300104, 7001)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(3300104, ai_param_id=218311)
    StopEvent(event_id=13305210, event_slot=2)


@RestartOnRest(13305230)
def Event_13305230():
    """Event 13305230"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(13305220))
    
    SetCharacterEventTarget(3300104, region=PLAYER)
    AICommand(3300104, command_id=50, command_slot=0)
    OR_1.Add(EntityWithinDistance(entity=3300104, other_entity=PLAYER, radius=5.0))
    OR_1.Add(TimeElapsed(seconds=10.0))
    
    MAIN.Await(OR_1)
    
    AICommand(3300104, command_id=-1, command_slot=0)


@RestartOnRest(13305250)
def Event_13305250(_, character: int, region: int, flag: int):
    """Event 13305250"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13305255)
def Event_13305255(_, character: int, region: int):
    """Event 13305255"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    ForceAnimation(character, 3000)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(13300700)
def Event_13300700():
    """Event 13300700"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DropMandatoryTreasure(3300710)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3300710)
    DisableGravity(3300710)
    DisableHealthBar(3300710)
    EnableImmortality(3300710)
    WaitFrames(frames=1)
    ForceAnimation(3300710, 9002, loop=True)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=3300710))
    
    ForceAnimation(3300710, 7006)
    WaitFrames(frames=45)
    Move(3300710, destination=3302160, destination_type=CoordEntityType.Region, copy_draw_parent=0)
    WaitFrames(frames=1)
    DropMandatoryTreasure(3300710)


@NeverRestart(13300990)
def Event_13300990():
    """Event 13300990"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    
    MAIN.Await(PlayerStandingOnCollision(3303500))
    
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=140,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=140,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=140,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=140,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    RunEvent(9350, slot=0, args=(2,))
