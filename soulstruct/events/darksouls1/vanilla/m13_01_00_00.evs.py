"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 7)
    RegisterBonfire(11310920, obj=1311950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11310992, obj=1311960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11310984, obj=1311961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11310010, stop_climbing_flag=11310011, obj=1311140)
    RegisterLadder(start_climbing_flag=11310012, stop_climbing_flag=11310013, obj=1311141)
    RegisterLadder(start_climbing_flag=11310014, stop_climbing_flag=11310015, obj=1311142)
    RegisterLadder(start_climbing_flag=11310016, stop_climbing_flag=11310017, obj=1311143)
    RegisterLadder(start_climbing_flag=11310018, stop_climbing_flag=11310019, obj=1311144)
    RegisterLadder(start_climbing_flag=11310020, stop_climbing_flag=11310021, obj=1311145)
    RegisterLadder(start_climbing_flag=11310022, stop_climbing_flag=11310023, obj=1311146)
    RegisterLadder(start_climbing_flag=11310024, stop_climbing_flag=11310025, obj=1311147)
    RegisterLadder(start_climbing_flag=11310026, stop_climbing_flag=11310027, obj=1311148)
    SkipLinesIfClient(2)
    EnableFlag(401)
    DisableFlag(11310000)
    IfClient(1)
    IfInsideMap(1, game_map=TOMB_OF_THE_GIANTS)
    SkipLinesIfConditionTrue(2, 1)
    DisableObject(1311994)
    DeleteVFX(1311995, erase_root_only=False)
    SkipLinesIfFlagOn(2, 11310810)
    DisableTreasure(1311600)
    DisableObject(1311600)
    SkipLinesIfFlagOff(1, 11310810)
    EnableTreasure(1311600)
    RunEvent(11310090, slot=0, args=(1311700, 1311701, 1312600, 1312601))
    RunEvent(11315040)
    RunEvent(11315041)
    RunEvent(11315042)
    RunEvent(11310095)
    RunEvent(11315100)
    RunEvent(11310051)
    RunEvent(11310052)
    RunEvent(11310053)
    RunEvent(11310054)
    RunEvent(11310100)
    RunEvent(11315080)
    RunEvent(11315050, slot=0, args=(1310200, 1310200, 0.0), arg_types="iif")
    RunEvent(11315050, slot=1, args=(1310201, 1310202, 0.0), arg_types="iif")
    RunEvent(11315050, slot=2, args=(1310202, 1310202, 0.0), arg_types="iif")
    RunEvent(11315060, slot=0, args=(1310203, 51310100, 0.0), arg_types="iif")
    RunEvent(11315060, slot=1, args=(1310204, 51310100, 0.20000000298023224), arg_types="iif")
    RunEvent(11315060, slot=2, args=(1310205, 51310100, 0.8999999761581421), arg_types="iif")
    RunEvent(11315060, slot=3, args=(1310206, 51310100, 1.0), arg_types="iif")
    RunEvent(11315070, slot=0, args=(1310207, 1312251, 0.0), arg_types="iif")
    RunEvent(11315070, slot=1, args=(1310208, 1312251, 0.20000000298023224), arg_types="iif")
    RunEvent(11315070, slot=2, args=(1310209, 1312251, 0.4000000059604645), arg_types="iif")
    RunEvent(11315070, slot=3, args=(1310210, 1312251, 0.6000000238418579), arg_types="iif")
    RunEvent(11315070, slot=4, args=(1310211, 1312251, 0.800000011920929), arg_types="iif")
    RunEvent(11310820, slot=0, args=(1310300, 27903000))
    RunEvent(11310820, slot=1, args=(1310400, 33005000))
    DisableSoundEvent(1313800)
    SkipLinesIfFlagOff(4, 7)
    RunEvent(11315392)
    DisableObject(1311990)
    DeleteVFX(1311991, erase_root_only=False)
    SkipLines(13)
    RunEvent(11315390)
    RunEvent(11315391)
    RunEvent(11315393)
    RunEvent(11315392)
    RunEvent(11310001)
    RunEvent(11315394)
    RunEvent(11315395)
    RunEvent(11315396)
    RunEvent(11315398)
    RunEvent(11314398)
    RunEvent(11315350, slot=0, args=(1310120,))
    RunEvent(11315350, slot=1, args=(1310121,))
    RunEvent(11315350, slot=2, args=(1310122,))
    RunEvent(11315350, slot=3, args=(1310123,))
    RunEvent(11315350, slot=4, args=(1310124,))
    RunEvent(11315350, slot=5, args=(1310125,))
    RunEvent(11315843, slot=0, args=(7, 1311990, 1312998, 1312997))
    RunEvent(11315846, slot=0, args=(7, 1311990, 1311991))


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6551, 8948)
    RunEvent(11315030)
    RunEvent(11310810)
    HumanityRegistration(6071, 8358)
    SkipLinesIfFlagOn(2, 1174)
    SkipLinesIfFlagOn(1, 1173)
    DisableCharacter(6071)
    RunEvent(11310502, slot=0, args=(6071, 1176))
    RunEvent(11310503, slot=0, args=(6071, 1179))
    RunEvent(11310533, slot=0, args=(6071, 1170, 1181, 1177))
    RunEvent(11310534, slot=0, args=(6071, 1170, 1181, 1180))
    RunEvent(11310530)
    RunEvent(11310531, slot=0, args=(6071, 1170, 1181, 1174))
    RunEvent(11310532, slot=0, args=(6071, 1170, 1181, 1175))
    SkipLinesIfFlagOn(1, 1216)
    DisableCharacter(6091)
    SetTeamType(6091, TeamType.HostileAlly)
    RunEvent(11310520, slot=1, args=(6091, 1210, 1219, 1214))
    SkipLinesIfFlagOn(1, 1226)
    DisableCharacter(6101)
    SetTeamType(6101, TeamType.HostileAlly)
    RunEvent(11310520, slot=2, args=(6101, 1220, 1229, 1224))
    HumanityRegistration(6321, 8478)
    SkipLinesIfFlagRangeAnyOn(1, (1623, 1625))
    DisableCharacter(6321)
    RunEvent(11310501, slot=0, args=(6321, 1627))
    RunEvent(11310543, slot=0, args=(6321, 1625))
    RunEvent(11310542, slot=0, args=(6321, 1628))
    RunEvent(11310540, slot=0, args=(6321, 1620, 1631, 1623))
    RunEvent(11310541, slot=0, args=(6321, 1620, 1631, 1624))
    RunEvent(11310002)


def Event11310090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310090: Event 11310090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=arg_0_3,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11315040():
    """ 11315040: Event 11315040 """
    EndIfThisEventOn()
    DisableCharacter(1310900)
    DisableCharacter(1310901)
    DisableCharacter(1310902)
    DisableCharacter(1310903)
    DisableCharacter(1310904)
    DisableCharacter(1310905)
    DisableCharacter(1310906)
    DisableCharacter(1310907)
    DisableCharacter(1310908)
    DisableCharacter(1310909)
    IfFlagOn(0, 11310060)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1310900)
    EnableCharacter(1310901)
    EnableCharacter(1310902)
    EnableCharacter(1310903)
    EnableCharacter(1310904)
    EnableCharacter(1310905)
    EnableCharacter(1310906)
    EnableCharacter(1310907)
    EnableCharacter(1310908)
    EnableCharacter(1310909)


@RestartOnRest
def Event11315041():
    """ 11315041: Event 11315041 """
    IfFlagOn(-1, 11315045)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11310060)
    DisableFlag(11315045)
    EnableFlag(5001)
    Kill(1310900, award_souls=False)
    Kill(1310901, award_souls=False)
    Kill(1310902, award_souls=False)
    Kill(1310903, award_souls=False)
    Kill(1310904, award_souls=False)
    Kill(1310905, award_souls=False)
    Kill(1310906, award_souls=False)
    Kill(1310907, award_souls=False)
    Kill(1310908, award_souls=False)
    Kill(1310909, award_souls=False)


@RestartOnRest
def Event11315042():
    """ 11315042: Event 11315042 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11310060)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11310060)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11310060)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11310060)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11310060)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=TOMB_OF_THE_GIANTS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11310060)
    RestartIfConditionFalse(-6)
    EnableFlag(11310060)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=TOMB_OF_THE_GIANTS)
    RestartIfConditionFalse(7)
    DisableFlag(11310060)
    EnableFlag(11315045)


def Event11310095():
    """ 11310095: Event 11310095 """
    SkipLinesIfFlagOff(5, 11800100)
    EnableFlag(11310096)
    DisableObject(1311710)
    DeleteVFX(1311711, erase_root_only=False)
    DisableFlag(401)
    End()
    SkipLinesIfFlagOff(3, 11310096)
    DisableObject(1311710)
    DeleteVFX(1311711, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=1312610,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=1311710,
    )
    DisplayStatus(10010630, pad_enabled=True)
    Restart()


def Event11315390():
    """ 11315390: Event 11315390 """
    IfFlagOff(1, 7)
    IfCharacterAlive(1, 1310800)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1312998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1311990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1312997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11315391():
    """ 11315391: Event 11315391 """
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1312998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1311990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1312997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11315393():
    """ 11315393: Event 11315393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315390)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1310800)
    DisableFlag(11310050)


@RestartOnRest
def Event11315392():
    """ 11315392: Event 11315392 """
    SkipLinesIfFlagOff(17, 7)
    DisableCharacter(1310800)
    Kill(1310800, award_souls=False)
    DisableCharacter(1310810)
    Kill(1310810, award_souls=False)
    DisableCharacter(1310120)
    DisableCharacter(1310121)
    DisableCharacter(1310122)
    DisableCharacter(1310123)
    DisableCharacter(1310124)
    DisableCharacter(1310125)
    Kill(1310120, award_souls=False)
    Kill(1310121, award_souls=False)
    Kill(1310122, award_souls=False)
    Kill(1310123, award_souls=False)
    Kill(1310124, award_souls=False)
    Kill(1310125, award_souls=False)
    End()
    SkipLinesIfThisEventOn(1)
    SkipLinesIfFlagOn(1, 11310000)
    DisableCharacter(1310800)
    DisableAI(1310800)
    SetStandbyAnimationSettings(1310120, standby_animation=9001)
    SetStandbyAnimationSettings(1310121, standby_animation=9001)
    SetStandbyAnimationSettings(1310122, standby_animation=9001)
    SetStandbyAnimationSettings(1310123, standby_animation=9001)
    SetStandbyAnimationSettings(1310124, standby_animation=9001)
    SetStandbyAnimationSettings(1310125, standby_animation=9001)
    IfHost(1)
    IfFlagOff(1, 11310050)
    IfCharacterInsideRegion(1, PLAYER, region=1312999)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(1310810)
    SkipLinesIfFlagOn(7, 11310000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130100, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1310800)
    EnableFlag(11310000)
    EnableAI(1310800)
    EnableBossHealthBar(1310800, name=5220, slot=0)
    EnableFlag(11315392)
    DisableNetworkSync()
    ResetStandbyAnimationSettings(1310120)
    ForceAnimation(1310120, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(1310121, cancel_animation=9061)
    ForceAnimation(1310121, 9061)
    Wait(0.5)
    SetStandbyAnimationSettings(1310122, cancel_animation=9061)
    ForceAnimation(1310122, 9061)
    Wait(0.20000000298023224)
    SetStandbyAnimationSettings(1310123, cancel_animation=9061)
    ForceAnimation(1310123, 9061)
    Wait(0.30000001192092896)
    SetStandbyAnimationSettings(1310124, cancel_animation=9061)
    ForceAnimation(1310124, 9061)
    Wait(0.699999988079071)
    SetStandbyAnimationSettings(1310125, cancel_animation=9061)
    ForceAnimation(1310125, 9061)


def Event11310001():
    """ 11310001: Event 11310001 """
    DisableObject(1311950)
    IfCharacterDead(0, 1310800)
    EnableFlag(7)
    KillBoss(1310800)
    SkipLinesIfClient(1)
    AwardAchievement(35)
    DisableObject(1311990)
    DeleteVFX(1311991, erase_root_only=True)
    Kill(1310810, award_souls=False)
    CreateTemporaryVFX(90014, anchor_entity=1311950, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1311950)
    RegisterBonfire(11310920, obj=1311950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


def Event11315394():
    """ 11315394: Event 11315394 """
    DisableNetworkSync()
    IfFlagOff(1, 7)
    IfFlagOn(1, 11315392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11315391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1313800)


def Event11315395():
    """ 11315395: Event 11315395 """
    DisableNetworkSync()
    IfFlagOn(1, 7)
    IfFlagOn(1, 11315394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1313800)


def Event11315396():
    """ 11315396: Event 11315396 """
    IfHealthLessThanOrEqual(0, 1310800, 0.0)
    SkipLinesIfFlagOff(7, 11315370)
    Kill(1310110, award_souls=False)
    Kill(1310111, award_souls=False)
    Kill(1310112, award_souls=False)
    Kill(1310113, award_souls=False)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    SkipLinesIfFlagOff(7, 11315371)
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=False)
    Kill(1310113, award_souls=False)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    SkipLinesIfFlagOff(7, 11315372)
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=True)
    Kill(1310113, award_souls=True)
    Kill(1310114, award_souls=False)
    Kill(1310115, award_souls=False)
    End()
    Kill(1310110, award_souls=True)
    Kill(1310111, award_souls=True)
    Kill(1310112, award_souls=True)
    Kill(1310113, award_souls=True)
    Kill(1310114, award_souls=True)
    Kill(1310115, award_souls=True)


@RestartOnRest
def Event11315397():
    """ 11315397: Event 11315397 """
    DisableObject(1311200)
    DisableObject(1311201)
    DisableObject(1311202)
    DisableCharacter(1310110)
    DisableCharacter(1310111)
    DisableCharacter(1310112)
    DisableCharacter(1310113)
    DisableCharacter(1310114)
    DisableCharacter(1310115)
    RunEvent(11315370, slot=0, args=(11315392, 2, 5220, 5220, 1311200, 1310110, 1310113, 8000), arg_types="ihhiiiii")
    RunEvent(11315370, slot=1, args=(11315370, 3, 5221, 5221, 1311201, 1310111, 1310114, 8010), arg_types="ihhiiiii")
    RunEvent(11315370, slot=2, args=(11315371, 4, 5222, 5222, 1311202, 1310112, 1310115, 8020), arg_types="ihhiiiii")
    IfCharacterBackreadEnabled(0, 1310800)
    SetDisplayMask(1310800, bit_index=0, switch_type=OnOffChange.On)


@RestartOnRest
def Event11315398():
    """ 11315398: Event 11315398 """
    DisableNetworkSync()
    IfFlagOn(1, 11315390)
    IfCharacterTargeting(1, 1310800, PLAYER)
    IfHasTAEEvent(1, 1310800, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11313398)
    IfHasTAEEvent(0, 1310800, tae_event_id=710)
    EnableFlag(11313399)
    Restart()


@RestartOnRest
def Event11314398():
    """ 11314398: Event 11314398 """
    IfFlagOn(0, 11313398)
    MoveObjectToCharacter(1311250, character=PLAYER, model_point=-1)
    DisableFlag(11313398)
    IfFlagOn(0, 11313399)
    CreateHazard(
        11315399,
        1311250,
        model_point=1,
        behavior_param_id=11300,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.30000001192092896,
        repetition_time=0.0,
    )
    CreateTemporaryVFX(15224, anchor_entity=1311250, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11313399)
    Restart()


@UnknownRestart
def Event11315370(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_6_7: short,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 11315370: Event 11315370 """
    IfFlagOn(0, arg_0_3)
    CreateNPCPart(
        1310800,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthGreaterThan(1, 1310800, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, 1310800, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, 1310800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(5, 11315370)
    SetCollisionMask(1310800, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(1310800, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=4, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=7, switch_type=OnOffChange.On)
    SkipLines(10)
    SkipLinesIfFlagOn(5, 11315371)
    SetCollisionMask(1310800, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(1310800, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=5, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=8, switch_type=OnOffChange.On)
    SkipLines(4)
    SetCollisionMask(1310800, bit_index=3, switch_type=OnOffChange.Off)
    SetDisplayMask(1310800, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=6, switch_type=OnOffChange.On)
    SetDisplayMask(1310800, bit_index=9, switch_type=OnOffChange.On)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_12_15, character=1310800, model_point=50)
    DestroyObject(arg_12_15, slot=1)
    EnableCharacter(arg_16_19)
    Move(
        arg_16_19,
        destination=1310800,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=1310800,
    )
    ForceAnimation(arg_16_19, 7000)
    EnableCharacter(arg_20_23)
    Move(
        arg_20_23,
        destination=1310800,
        destination_type=CoordEntityType.Character,
        model_point=51,
        copy_draw_parent=1310800,
    )
    ForceAnimation(arg_20_23, 7000)
    ForceAnimation(1310800, arg_24_27, wait_for_completion=True)


@RestartOnRest
def Event11315350(_, arg_0_3: int):
    """ 11315350: Event 11315350 """
    EndIfFlagOn(7)
    EndIfThisEventSlotOn()
    EnableImmortality(arg_0_3)
    IfHealthLessThanOrEqual(0, 1310800, 0.0)
    CancelSpecialEffect(arg_0_3, 5451)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=True)


@RestartOnRest
def Event11315100():
    """ 11315100: Event 11315100 """
    RunEvent(11315091)
    RunEvent(11315092)
    RunEvent(11315150, slot=0, args=(11315100, 1313200, 11315101))
    RunEvent(11315150, slot=1, args=(11315101, 1313201, 11315102))
    RunEvent(11315150, slot=2, args=(11315102, 1313202, 11315103))
    RunEvent(11315150, slot=3, args=(11315103, 1313203, 11315104))
    RunEvent(11315150, slot=4, args=(11315104, 1313204, 11315105))
    RunEvent(11315150, slot=5, args=(11315105, 1313205, 11315106))
    RunEvent(11315150, slot=6, args=(11315106, 1313206, 11315107))
    RunEvent(11315150, slot=7, args=(11315107, 1313207, 11315108))
    RunEvent(11315150, slot=8, args=(11315108, 1313208, 11315109))
    RunEvent(11315150, slot=9, args=(11315109, 1313209, 11315110))
    RunEvent(11315150, slot=10, args=(11315110, 1313210, 11315111))
    RunEvent(11315150, slot=11, args=(11315111, 1313211, 11315112))
    RunEvent(11315150, slot=12, args=(11315112, 1313212, 11315113))
    RunEvent(11315150, slot=13, args=(11315113, 1313213, 11315114))
    RunEvent(11315150, slot=14, args=(11315114, 1313214, 11315115))
    RunEvent(11315150, slot=15, args=(11315115, 1313215, 11315116))
    RunEvent(11315150, slot=16, args=(11315116, 1313216, 11315117))
    RunEvent(11315150, slot=17, args=(11315117, 1313217, 11315118))
    RunEvent(11315150, slot=18, args=(11315118, 1313218, 11315119))
    RunEvent(11315150, slot=19, args=(11315119, 1313219, 11315120))
    RunEvent(11315150, slot=20, args=(11315120, 1313220, 11315121))
    RunEvent(11315150, slot=21, args=(11315121, 1313221, 11315122))
    RunEvent(11315150, slot=22, args=(11315122, 1313222, 11315123))
    RunEvent(11315150, slot=23, args=(11315123, 1313223, 11315124))
    RunEvent(11315150, slot=24, args=(11315100, 1313224, 11315125))
    RunEvent(11315150, slot=25, args=(11315125, 1313225, 11315126))
    RunEvent(11315150, slot=26, args=(11315126, 1313226, 11315127))
    RunEvent(11315150, slot=27, args=(11315127, 1313227, 11315128))
    RunEvent(11315150, slot=28, args=(11315128, 1313228, 11315129))
    RunEvent(11315150, slot=29, args=(11315129, 1313229, 11315130))
    RunEvent(11315150, slot=30, args=(11315130, 1313230, 11315131))
    RunEvent(11315150, slot=31, args=(11315131, 1313231, 11315132))
    RunEvent(11315150, slot=32, args=(11315132, 1313232, 11315133))
    RunEvent(11315150, slot=33, args=(11315133, 1313233, 11315134))
    RunEvent(11315150, slot=34, args=(11315134, 1313234, 11315135))
    RunEvent(11315150, slot=35, args=(11315135, 1313235, 11315136))
    RunEvent(11315150, slot=36, args=(11315136, 1313236, 11315137))
    RunEvent(11315150, slot=37, args=(11315137, 1313237, 11315138))
    RunEvent(11315150, slot=38, args=(11315138, 1313238, 11315139))
    RunEvent(11315150, slot=39, args=(11315139, 1313239, 11315140))
    RunEvent(11315150, slot=40, args=(11315140, 1313240, 11315141))
    RunEvent(11315150, slot=41, args=(11315141, 1313241, 11315142))
    RunEvent(11315150, slot=42, args=(11315142, 1313242, 11315143))
    RunEvent(11315150, slot=43, args=(11315143, 1313243, 11315144))
    RunEvent(11315150, slot=44, args=(11315144, 1313244, 11315145))
    RunEvent(11315150, slot=45, args=(11315145, 1313245, 11315146))
    RunEvent(11315150, slot=46, args=(11315146, 1313246, 11315147))
    RunEvent(11315150, slot=47, args=(11315147, 1313247, 11315148))
    RunEvent(11315150, slot=48, args=(11315148, 1313248, 11315149))


@UnknownRestart
def Event11315150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11315150: Event 11315150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, 11315090)
    DeleteVFX(arg_4_7, erase_root_only=False)
    IfFlagOn(1, 11315090)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(arg_4_7)
    EnableFlag(arg_8_11)
    IfFlagOff(0, 11315090)
    DeleteVFX(arg_4_7, erase_root_only=True)
    DisableFlag(arg_8_11)
    Restart()


@UnknownRestart
def Event11315091():
    """ 11315091: Event 11315091 """
    IfSkullLanternActive(1)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11315090)
    RestartEvent(11315092, slot=0)
    Restart()


@UnknownRestart
def Event11315092():
    """ 11315092: Event 11315092 """
    DisableNetworkSync()
    IfFlagOn(0, 11315090)
    Wait(3.0)
    DisableFlag(11315090)
    Restart()


@RestartOnRest
def Event11315050(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315050: Event 11315050 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(0, arg_4_7, PLAYER, radius=5.0)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315060(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315060: Event 11315060 """
    SkipLinesIfFlagOff(2, arg_4_7)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315070(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11315070: Event 11315070 """
    SkipLinesIfFlagOff(2, arg_4_7)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11315080():
    """ 11315080: Event 11315080 """
    EndIfThisEventOn()
    DisableAI(1310250)
    IfEntityWithinDistance(1, 1310250, PLAYER, radius=7.0)
    IfAttacked(2, 1310250, attacking_character=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1310250)
    EndIfFinishedConditionTrue(2)
    SetStandbyAnimationSettings(1310250, standby_animation=9000)
    ForceAnimation(1310250, 9070, wait_for_completion=True)
    Move(1310250, destination=1312250, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    IfEntityWithinDistance(-1, 1310251, PLAYER, radius=5.0)
    IfAttacked(-1, 1310251, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1310250, cancel_animation=9060)


def Event11310051():
    """ 11310051: Event 11310051 """
    DisableCharacter(1310810)
    DisableObject(1311300)
    DisableObjectActivation(1311300, obj_act_id=-1)
    IfFlagOn(0, 11310050)
    SkipLinesIfFlagOn(1, 7)
    EnableCharacter(1310810)
    EnableObject(1311300)
    EnableObjectActivation(1311300, obj_act_id=-1)
    DisableCharacter(1310120)
    DisableCharacter(1310121)
    DisableCharacter(1310122)
    DisableCharacter(1310123)
    DisableCharacter(1310124)
    DisableCharacter(1310125)
    IfFlagOff(0, 11310050)
    EnableCharacter(1310120)
    EnableCharacter(1310121)
    EnableCharacter(1310122)
    EnableCharacter(1310123)
    EnableCharacter(1310124)
    EnableCharacter(1310125)
    Restart()


def Event11310052():
    """ 11310052: Event 11310052 """
    IfObjectActivated(0, obj_act_id=11315340)
    SetStandbyAnimationSettings(PLAYER, standby_animation=7151, death_animation=6082)
    Wait(3.0)
    PlayCutscene(
        130121, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1302010, move_to_map=CATACOMBS
    )
    PlayCutscene(130021, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    ResetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(1311300, obj_act_id=-1)
    Restart()


def Event11310053():
    """ 11310053: Event 11310053 """
    IfFlagOn(0, 11315020)
    RotateToFaceEntity(PLAYER, 1310810)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagOff(0, 11315020)
    ResetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()


def Event11310054():
    """ 11310054: Event 11310054 """
    DisableNetworkSync()
    IfSingleplayer(1)
    IfFlagOn(1, 11310050)
    IfEntityWithinDistance(1, 1311300, PLAYER, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    Wait(1.0)
    ResetStandbyAnimationSettings(PLAYER)
    EnableObjectActivation(1311300, obj_act_id=-1)
    IfEntityBeyondDistance(0, 1311300, PLAYER, radius=3.0)
    Restart()


def Event11310100():
    """ 11310100: Event 11310100 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1311400)
    End()
    IfObjectDestroyed(0, 1311400)
    End()


@RestartOnRest
def Event11310820(_, arg_0_3: int, arg_4_7: int):
    """ 11310820: Event 11310820 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11310510(_, arg_0_3: int, arg_4_7: int):
    """ 11310510: Event 11310510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11310520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310520: Event 11310520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310501(_, arg_0_3: int, arg_4_7: int):
    """ 11310501: Event 11310501 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(-7, 1623)
    IfFlagOn(-7, 1624)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11310502(_, arg_0_3: int, arg_4_7: int):
    """ 11310502: Event 11310502 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1173)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11310503(_, arg_0_3: int, arg_4_7: int):
    """ 11310503: Event 11310503 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SetAIParamID(arg_0_3, 1)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11310530():
    """ 11310530: Event 11310530 """
    IfFlagRangeAllOff(7, (1176, 1181))
    IfFlagOn(7, 1171)
    IfFlagRangeAllOff(7, (1195, 1198))
    IfFlagOn(7, 1202)
    IfFlagRangeAllOff(7, (1213, 1215))
    IfFlagOn(7, 1211)
    IfFlagRangeAllOff(7, (1223, 1225))
    IfFlagOn(7, 1221)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(1, 11020600)
    IfThisEventOff(1)
    IfConditionTrue(2, input_condition=7)
    IfFlagOn(2, 11300005)
    IfConditionTrue(3, input_condition=7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ClearEventValue(600, bit_count=4)
    EnableFlag(11020693)
    DisableFlagRange((1170, 1189))
    EnableFlag(1173)
    EnableCharacter(6071)
    DisableFlagRange((1190, 1209))
    EnableFlag(1192)
    DisableFlagRange((1210, 1219))
    EnableFlag(1216)
    EnableCharacter(6091)
    DisableFlagRange((1220, 1229))
    EnableFlag(1226)
    EnableCharacter(6101)


def Event11310531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310531: Event 11310531 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1173)
    IfFlagOn(1, 1214)
    IfFlagOn(1, 1224)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310532: Event 11310532 """
    IfHost(1)
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfFlagOn(1, 11310590)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    ClearEventValue(600, bit_count=4)


def Event11310533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310533: Event 11310533 """
    IfFlagOff(1, 1179)
    IfFlagOn(-7, 1173)
    IfFlagOn(-7, 1176)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionFalse(2)
    DropMandatoryTreasure(arg_0_3)


def Event11310534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310534: Event 11310534 """
    IfFlagOff(1, 1176)
    IfFlagOn(-7, 1174)
    IfFlagOn(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionFalse(2)
    DropMandatoryTreasure(arg_0_3)


def Event11310540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310540: Event 11310540 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagRangeAnyOn(2, (1620, 1621))
    IfFlagOn(2, 6)
    IfFlagOn(3, 1173)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11310541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11310541: Event 11310541 """
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1623)
    IfFlagOn(1, 11310002)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11310542(_, arg_0_3: int, arg_4_7: int):
    """ 11310542: Event 11310542 """
    IfFlagOn(1, 1623)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1624)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfFlagOn(3, arg_4_7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(1625)
    DisableFlag(1627)
    EnableFlag(arg_4_7)
    EndIfFinishedConditionFalse(3)
    DropMandatoryTreasure(arg_0_3)


def Event11310543(_, arg_0_3: int, arg_4_7: int):
    """ 11310543: Event 11310543 """
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1624)
    IfFlagOn(1, 11310595)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()
    EnableCharacter(arg_0_3)


def Event11315030():
    """ 11315030: Event 11315030 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11315031)
    EndIfFlagOn(7)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11310810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1312001)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6551, region=1312000, summon_flag=11315031, dismissal_flag=11315032)
    Wait(20.0)
    Restart()


def Event11310810():
    """ 11310810: Event 11310810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, 11315031)
    IfFlagOff(1, 11315032)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(6551)
    EndIfThisEventOn()
    IfCharacterDead(0, 6551)
    EnableFlag(11310810)


def Event11310002():
    """ 11310002: Event 11310002 """
    EndIfThisEventOn()
    IfHost(1)
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1623)
    IfFlagOff(1, 1638)
    IfCharacterInsideRegion(1, PLAYER, region=1313400)
    IfHost(2)
    IfFlagOff(2, 1625)
    IfFlagOff(2, 1627)
    IfFlagOff(2, 1628)
    IfFlagOn(2, 1623)
    IfFlagOn(2, 1638)
    IfCharacterInsideRegion(2, PLAYER, region=1313400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfMultiplayer(7)
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(
        130111, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1312120, move_to_map=TOMB_OF_THE_GIANTS
    )
    SkipLines(1)
    PlayCutscene(
        130110, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1312120, move_to_map=TOMB_OF_THE_GIANTS
    )
    WaitFrames(1)
    Move(6321, destination=1312121, model_point=-1, destination_type=CoordEntityType.Region)
    End()
    SkipLinesIfClient(7)
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(
        130111,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1312120,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    SkipLines(1)
    PlayCutscene(
        130110,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1312120,
        move_to_map=TOMB_OF_THE_GIANTS,
    )
    WaitFrames(1)
    Move(6321, destination=1312121, model_point=-1, destination_type=CoordEntityType.Region)
    End()
    SkipLinesIfFinishedConditionTrue(2, 2)
    PlayCutscene(130111, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130110, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Move(6321, destination=1312121, model_point=-1, destination_type=CoordEntityType.Region)


def Event11315843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11315843: Event 11315843 """
    IfHost(1)
    IfMultiplayer(1)
    IfFlagOn(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        line_intersects=arg_4_7,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


def Event11315846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11315846: Event 11315846 """
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Restart()
