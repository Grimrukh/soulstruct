"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *


def Constructor():
    """ 0: Event 0 """
    CreateProjectileOwner(1500200)
    SetNetworkUpdateRate(1500100, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    RegisterBonfire(11500984, obj=1501961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11500010, stop_climbing_flag=11500011, obj=1501140)
    RegisterLadder(start_climbing_flag=11500012, stop_climbing_flag=11500013, obj=1501141)
    RegisterLadder(start_climbing_flag=11500014, stop_climbing_flag=11500015, obj=1501142)
    RegisterLadder(start_climbing_flag=11500016, stop_climbing_flag=11500017, obj=1501143)
    SkipLinesIfHost(2)
    EnableFlag(11505240)
    DisableFlag(11505360)
    SkipLinesIfClient(2)
    DisableObject(1501994)
    DeleteVFX(1501995, erase_root_only=False)
    DisableCollision(1503210)
    DisableObject(1501800)
    DisableObject(1501801)
    DisableObject(1501802)
    DisableObject(1501803)
    DisableObject(1501804)
    DisableObject(1501805)
    DisableObject(1501806)
    DisableObject(1501807)
    SkipLinesIfFlagOn(1, 11500803)
    EndOfAnimation(1501790, 3)
    SkipLinesIfFlagOff(1, 11500806)
    EndOfAnimation(1501790, 0)
    SkipLinesIfFlagOff(1, 11500809)
    EndOfAnimation(1501790, 1)
    SkipLinesIfFlagOff(1, 11500812)
    EndOfAnimation(1501790, 2)
    DisableCollision(1503200)
    DisableCollision(1503201)
    DisableCollision(1503202)
    SkipLinesIfFlagOff(3, 11500821)
    EnableObject(1501801)
    EndOfAnimation(1501801, 5)
    EnableCollision(1503200)
    SkipLinesIfFlagOff(3, 11500822)
    EnableObject(1501802)
    EndOfAnimation(1501802, 6)
    EnableCollision(1503201)
    SkipLinesIfFlagOff(3, 11500823)
    EnableObject(1501803)
    EndOfAnimation(1501803, 7)
    EnableCollision(1503202)
    SkipLinesIfFlagOff(21, 11500100)
    SkipLinesIfFlagOn(10, 11500101)
    EnableNavmeshType(1503100, NavmeshType.Wall)
    EnableNavmeshType(1503110, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503101, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503111, NavmeshType.Wall)
    EnableNavmeshType(1503102, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503112, NavmeshType.Wall)
    EnableNavmeshType(1503103, NavmeshType.Wall)
    EnableNavmeshType(1503113, NavmeshType.WallTouchingFloor)
    EndOfAnimation(1501011, 12)
    SkipLines(9)
    EnableNavmeshType(1503100, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503110, NavmeshType.Wall)
    EnableNavmeshType(1503101, NavmeshType.Wall)
    EnableNavmeshType(1503111, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503102, NavmeshType.Wall)
    EnableNavmeshType(1503112, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503103, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503113, NavmeshType.Wall)
    EndOfAnimation(1501011, 11)
    SkipLines(4)
    EnableNavmeshType(1503100, NavmeshType.Solid)
    EnableNavmeshType(1503101, NavmeshType.Solid)
    EnableNavmeshType(1503102, NavmeshType.Solid)
    EnableNavmeshType(1503103, NavmeshType.Solid)
    RunEvent(11500090, slot=0, args=(1501700, 1501701, 1502600, 1502601))
    RunEvent(11500090, slot=1, args=(1501702, 1501703, 1502602, 1502603))
    RunEvent(11505090)
    RunEvent(11505091)
    RunEvent(11505092)
    RunEvent(11500201)
    RunEvent(11505300)
    RunEvent(11500840)
    RunEvent(11500841, slot=0, args=(11500803,))
    RunEvent(11500841, slot=1, args=(11500806,))
    RunEvent(11500841, slot=2, args=(11500809,))
    RunEvent(11500841, slot=3, args=(11500812,))
    RunEvent(11500790)
    RunEvent(11500791)
    RunEvent(11500795)
    RunEvent(11500796)
    RunEvent(11500797)
    RunEvent(11500798)
    RunEvent(11500830)
    RunEvent(11500831)
    RunEvent(11500850)
    RunEvent(11505255)
    RunEvent(11500100)
    RunEvent(11500102)
    RunEvent(11500103)
    RunEvent(11500106)
    RunEvent(11500107)
    RunEvent(11500110, slot=0, args=(1501030, 11500110))
    RunEvent(11500110, slot=1, args=(1501031, 11500111))
    RunEvent(11500110, slot=2, args=(1501032, 11500112))
    RunEvent(11500110, slot=3, args=(1501033, 11500113))
    RunEvent(11500110, slot=5, args=(1501035, 11500115))
    RunEvent(11500110, slot=6, args=(1501036, 11500116))
    RunEvent(11505050)
    RunEvent(11505051)
    RunEvent(11505055)
    RunEvent(11505110)
    RunEvent(11505101)
    RunEvent(11505102)
    RunEvent(11505111, slot=0, args=(11505111, 1502700, 1))
    RunEvent(11505111, slot=1, args=(11505112, 1502701, 2))
    RunEvent(11505111, slot=2, args=(11505113, 1502702, 3))
    RunEvent(11505111, slot=3, args=(11505114, 1502703, 4))
    RunEvent(11505111, slot=4, args=(11505115, 1502704, 5))
    RunEvent(11505111, slot=5, args=(11505116, 1502705, 6))
    RunEvent(11505111, slot=6, args=(11505117, 1502710, 4294967295))
    RunEvent(11505060, slot=0, args=(1500100,))
    RunEvent(11505060, slot=1, args=(1500101,))
    RunEvent(11505060, slot=2, args=(1500102,))
    RunEvent(11505070, slot=0, args=(1500100,))
    RunEvent(11505070, slot=1, args=(1500101,))
    RunEvent(11505070, slot=2, args=(1500102,))
    RunEvent(11505080)
    RunEvent(11500210)
    RunEvent(11500835)
    DisableSoundEvent(1503800)
    SkipLinesIfFlagOff(4, 11)
    RunEvent(11505392)
    DisableObject(1501990)
    DeleteVFX(1501991, erase_root_only=False)
    SkipLines(9)
    RunEvent(11505390)
    RunEvent(11505391)
    RunEvent(11505393)
    RunEvent(11505392)
    RunEvent(11500001)
    RunEvent(11505394)
    RunEvent(11505395)
    RunEvent(11505350)
    RunEvent(11505353)
    RunEvent(11505010)
    RunEvent(11505011)
    RunEvent(11505012)
    RunEvent(11505013)
    RunEvent(11505014)
    RunEvent(11500900)
    RunEvent(11505015)
    RunEvent(11505270, slot=0, args=(1502200, 1501200, 1503500, 1501210, 0, 11505280))
    RunEvent(11505270, slot=1, args=(1502201, 1501201, 1503500, 1501211, 90, 11505281))
    RunEvent(11505270, slot=2, args=(1502202, 1501202, 1503500, 1501212, 90, 11505282))
    RunEvent(11505270, slot=3, args=(1502203, 1501203, 1503500, 1501213, 270, 11505283))
    RunEvent(11505270, slot=4, args=(1502204, 1501204, 1503500, 1501214, 180, 11505284))
    RunEvent(11505270, slot=5, args=(1502205, 1501205, 1503500, 1501213, 270, 11505285))
    RunEvent(11505260)
    RunEvent(11500860, slot=0, args=(6600,))
    RunEvent(11500860, slot=1, args=(1500300,))
    RunEvent(11500860, slot=2, args=(1500301,))
    RunEvent(11500860, slot=3, args=(1500302,))
    RunEvent(11500860, slot=4, args=(1500303,))
    RunEvent(11500860, slot=5, args=(1500100,))
    RunEvent(11500860, slot=7, args=(1500102,))
    RunEvent(11500600, slot=0, args=(1501650, 11500600))
    RunEvent(11500600, slot=2, args=(1501652, 11500602))
    RunEvent(11500600, slot=4, args=(1501654, 11500604))
    RunEvent(11500600, slot=9, args=(1501659, 11500609))
    RunEvent(11500600, slot=10, args=(1501660, 11500610))
    RunEvent(11505843, slot=0, args=(11, 1501990, 1502998, 1502997))
    RunEvent(11505846, slot=0, args=(11, 1501990, 1501991))


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6600, 8980)
    HumanityRegistration(6510, 8924)
    RunEvent(11505030)
    RunEvent(11505029)
    RunEvent(11505032)
    RunEvent(11505990, slot=0, args=(11505031, 6510))
    HumanityRegistration(6030, 8334)
    SkipLinesIfFlagOn(3, 1090)
    SkipLinesIfFlagOn(2, 1091)
    SkipLinesIfFlagOn(1, 1096)
    DisableCharacter(6030)
    RunEvent(11500510, slot=0, args=(6030, 1096))
    RunEvent(11500520, slot=0, args=(6030, 1090, 1109, 1097))
    RunEvent(11500530)
    RunEvent(11500531, slot=0, args=(6030, 1090, 1109, 1091))
    RunEvent(11500532, slot=0, args=(6030, 1090, 1109, 1092))
    SetTeamTypeAndExitStandbyAnimation(6043, TeamType.HostileAlly)
    SkipLinesIfFlagOn(1, 1117)
    DisableCharacter(6043)
    RunEvent(11500520, slot=1, args=(6043, 1110, 1119, 1115))
    RunEvent(11500533, slot=0, args=(6043, 1110, 1119, 1117))
    HumanityRegistration(6280, 8446)
    SkipLinesIfFlagOn(3, 1514)
    SkipLinesIfFlagOn(2, 1513)
    SkipLinesIfFlagRangeAnyOn(1, (1493, 1511))
    SkipLines(1)
    DisableCharacter(6280)
    SkipLinesIfFlagOn(1, 11500200)
    SkipLines(1)
    Move(6280, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SkipLinesIfFlagRangeAnyOn(1, (1491, 1492))
    SkipLines(2)
    Kill(1500120, award_souls=False)
    Kill(1500121, award_souls=False)
    RunEvent(11500510, slot=2, args=(6280, 1512))
    RunEvent(11500520, slot=2, args=(6280, 1490, 1539, 1513))
    RunEvent(11500534, slot=0, args=(6280, 1490, 1539, 1491))
    RunEvent(11500535, slot=0, args=(6280, 1490, 1539, 1492))
    RunEvent(11500536, slot=0, args=(6280, 1490, 1539, 1493))
    HumanityRegistration(6250, 8422)
    SkipLinesIfFlagRangeAnyOn(1, (1420, 1429))
    EnableFlag(1420)
    RunEvent(11500510, slot=3, args=(6250, 1421))
    RunEvent(11500520, slot=3, args=(6250, 1420, 1429, 1422))


def Event1000000000():
    """ 1000000000: Event 1000000000 """
    DisableCharacter(1500200)
    SetNetworkUpdateRate(1500100, is_fixed=True, update_rate=CharacterUpdateRate.Always)


def Event11500090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500090: Event 11500090 """
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
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11505090():
    """ 11505090: Event 11505090 """
    EndIfThisEventOn()
    DisableCharacter(1500900)
    DisableCharacter(1500901)
    DisableCharacter(1500902)
    DisableCharacter(1500903)
    DisableCharacter(1500904)
    DisableCharacter(1500905)
    DisableCharacter(1500906)
    DisableCharacter(1500907)
    DisableCharacter(1500908)
    DisableCharacter(1500909)
    IfFlagOn(0, 11500050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1500900)
    EnableCharacter(1500901)
    EnableCharacter(1500902)
    EnableCharacter(1500903)
    EnableCharacter(1500904)
    EnableCharacter(1500905)
    EnableCharacter(1500906)
    EnableCharacter(1500907)
    EnableCharacter(1500908)
    EnableCharacter(1500909)


@RestartOnRest
def Event11505091():
    """ 11505091: Event 11505091 """
    IfFlagOn(-1, 11505095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11500050)
    DisableFlag(11505095)
    EnableFlag(5001)
    Kill(1500900, award_souls=False)
    Kill(1500901, award_souls=False)
    Kill(1500902, award_souls=False)
    Kill(1500903, award_souls=False)
    Kill(1500904, award_souls=False)
    Kill(1500905, award_souls=False)
    Kill(1500906, award_souls=False)
    Kill(1500907, award_souls=False)
    Kill(1500908, award_souls=False)
    Kill(1500909, award_souls=False)


@RestartOnRest
def Event11505092():
    """ 11505092: Event 11505092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11500050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=SENS_FORTRESS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11500050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=SENS_FORTRESS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11500050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=SENS_FORTRESS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11500050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=SENS_FORTRESS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11500050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=SENS_FORTRESS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11500050)
    RestartIfConditionFalse(-6)
    EnableFlag(11500050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=SENS_FORTRESS)
    RestartIfConditionFalse(7)
    DisableFlag(11500050)
    EnableFlag(11505095)


def Event11505300():
    """ 11505300: Event 11505300 """
    CreateHazard(
        11505301,
        1501850,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505302,
        1501851,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505303,
        1501852,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505304,
        1501853,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505305,
        1501854,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505306,
        1501855,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505307,
        1501856,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505308,
        1501857,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505309,
        1501858,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505310,
        1501859,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505311,
        1501860,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505312,
        1501861,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505313,
        1501862,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505314,
        1501863,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505315,
        1501864,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505316,
        1501865,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505317,
        1501866,
        model_point=101,
        behavior_param_id=5040,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    CreateHazard(
        11505290,
        1501010,
        model_point=101,
        behavior_param_id=5060,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=0.5,
    )


def Event11505390():
    """ 11505390: Event 11505390 """
    IfFlagOff(1, 11)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1501990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11505391():
    """ 11505391: Event 11505391 """
    IfFlagOff(1, 11)
    IfFlagOn(1, 11505393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1502998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1501990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1502997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11505393():
    """ 11505393: Event 11505393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1500800)


@RestartOnRest
def Event11505392():
    """ 11505392: Event 11505392 """
    SkipLinesIfFlagOff(7, 11)
    DisableCharacter(1500800)
    DropMandatoryTreasure(1500800)
    DisableBackread(1500800)
    IfCharacterBackreadEnabled(0, 1500100)
    AICommand(1500100, command_id=10, slot=0)
    ReplanAI(1500100)
    End()
    DisableAI(1500800)
    SetStandbyAnimationSettings(1500800, standby_animation=9000)
    RunEvent(11505351)
    RunEvent(11505352)
    IfFlagOn(1, 11505393)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1500800)
    SetStandbyAnimationSettings(1500800, cancel_animation=9060)
    EnableBossHealthBar(1500800, name=2320, slot=0)


def Event11500001():
    """ 11500001: Event 11500001 """
    DeleteVFX(1503010, erase_root_only=False)
    IfCharacterDead(0, 1500800)
    EnableFlag(11)
    KillBoss(1500800)
    DisableObject(1501990)
    DeleteVFX(1501991, erase_root_only=True)
    CreateVFX(1503010)
    AICommand(1500100, command_id=10, slot=0)
    ReplanAI(1500100)
    DisableFlag(11807020)
    DisableFlag(11807030)
    DisableFlag(11807040)
    DisableFlag(11807050)
    DisableNetworkSync()
    Wait(3.0)
    DisableCharacter(1500800)
    DisableBackread(1500800)


def Event11505394():
    """ 11505394: Event 11505394 """
    DisableNetworkSync()
    IfFlagOff(1, 11)
    IfFlagOn(1, 11505392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11505391)
    IfCharacterInsideRegion(1, PLAYER, region=1502996)
    IfCharacterAlive(1, 1500800)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1503800)


def Event11505395():
    """ 11505395: Event 11505395 """
    DisableNetworkSync()
    IfFlagOn(1, 11)
    IfFlagOn(1, 11505394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1503800)
    PlaySoundEffect(anchor_entity=1502990, sound_type=SoundType.a_Ambient, sound_id=150100002)


def Event11505350():
    """ 11505350: Event 11505350 """
    EndIfClient()
    IfHasTAEEvent(0, 1500800, tae_event_id=100)
    IfCharacterDead(0, 1500800)


@UnknownRestart
def Event11505351():
    """ 11505351: Event 11505351 """
    EndIfFlagOn(11)
    EnableNetworkSync()
    IfFlagOff(0, 11505355)
    CreateNPCPart(
        1500800,
        npc_part_id=2320,
        part_index=NPCPartType.Part2,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(1500800, npc_part_id=2320, material_sfx_id=56, material_vfx_id=56)
    IfCharacterPartHealthLessThanOrEqual(0, 1500800, npc_part_id=2320, value=0)
    EzstateAIRequest(1500800, command_id=1300, slot=0)
    IfHasTAEEvent(0, 1500800, tae_event_id=1204)
    EnableFlag(11505355)
    CreateNPCPart(
        1500800,
        npc_part_id=2321,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(1500800, npc_part_id=2321, material_sfx_id=56, material_vfx_id=56)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    DisableFlag(11505355)
    RestartEvent(11505352)
    SetNPCPartHealth(1500800, npc_part_id=2321, desired_health=-1, overwrite_max=False)
    EzstateAIRequest(1500800, command_id=1303, slot=0)
    Restart()


@UnknownRestart
def Event11505352():
    """ 11505352: Event 11505352 """
    EndIfFlagOn(11)
    EnableNetworkSync()
    IfFlagOn(0, 11505355)
    IfFlagOn(1, 11505355)
    IfCharacterPartHealthLessThanOrEqual(1, 1500800, npc_part_id=2321, value=0)
    IfConditionTrue(0, input_condition=1)
    RestartEvent(11505351)
    EzstateAIRequest(1500800, command_id=1301, slot=0)
    IfHasTAEEvent(0, 1500800, tae_event_id=1203)
    DisableNetworkSync()
    Wait(15.0)
    EnableNetworkSync()
    EzstateAIRequest(1500800, command_id=1304, slot=0)
    DisableFlag(11505355)
    Restart()


def Event11505353():
    """ 11505353: Event 11505353 """
    IfHasTAEEvent(1, 1500800, tae_event_id=400)
    IfHasTAEEvent(2, 1500800, tae_event_id=300)
    IfHealthLessThanOrEqual(3, 1500800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 1)
    DisableCollision(1503000)
    SkipLines(1)
    EnableCollision(1503000)
    EndIfFinishedConditionTrue(3)
    IfDoesNotHaveTAEEvent(4, 1500800, tae_event_id=400)
    IfDoesNotHaveTAEEvent(4, 1500800, tae_event_id=300)
    IfConditionTrue(0, input_condition=4)
    Restart()


def Event11500201():
    """ 11500201: Event 11500201 """
    SkipLinesIfFlagOff(1, 11500200)
    EndOfAnimation(1501000, 0)
    IfCharacterInsideRegion(0, PLAYER, region=1502050)
    IfCharacterOutsideRegion(0, PLAYER, region=1502050)
    Restart()


def Event11500790():
    """ 11500790: Event 11500790 """
    IfFlagOn(0, 11500791)
    IfFlagOff(1, 11505050)
    IfCharacterAlive(1, 1500101)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11505052)
    Wait(5.0)
    EnableObject(1501800)
    ForceAnimation(1501800, 0)
    Wait(1.5)
    EnableCollision(1503210)
    Wait(3.5)
    WaitForNetworkApproval(max_seconds=10.0)
    SkipLinesIfFlagOn(2, 11505210)
    EnableFlag(11505220)
    Restart()
    SkipLinesIfFlagOn(2, 11505211)
    EnableFlag(11505221)
    Restart()
    SkipLinesIfFlagOn(2, 11505212)
    EnableFlag(11505222)
    Restart()
    SkipLinesIfFlagOn(1, 11505213)
    EnableFlag(11505223)
    Restart()


@RestartOnRest
def Event11500791():
    """ 11500791: Event 11500791 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1500110)
    End()
    DisableAI(1500110)
    IfCharacterInsideRegion(0, PLAYER, region=1502110)
    EnableFlag(11500791)
    EnableObject(1501800)
    ForceAnimation(1500110, 500, wait_for_completion=True)
    ForceAnimation(1500110, 603, wait_for_completion=True)
    EnableAI(1500110)
    CreateHazard(
        11505200,
        1501800,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(1501800, 12, wait_for_completion=True)
    DisableObject(1501800)


def Event11500795():
    """ 11500795: Event 11500795 """
    IfFlagOn(0, 11505220)
    DisableFlag(11505220)
    EnableFlag(11505210)
    DisableObject(1501800)
    EnableObject(1501804)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(11500700, slot=0, args=(11505200, 1501804, 1, 2.5, 1501812, 11505210), arg_types="iiifii")
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(11500700, slot=10, args=(11505200, 1501804, 2, 7.5, 1501813, 11505210), arg_types="iiifii")
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(11500700, slot=20, args=(11505200, 1501804, 3, 7.5, 1501810, 11505210), arg_types="iiifii")
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(11500700, slot=30, args=(11505200, 1501804, 4, 12.5, 1501811, 11505210), arg_types="iiifii")
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(11500750, slot=0, args=(11505200, 1501801, 5, 1503200, 1501811, 11505210, 11500821, 1501804))
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(11500750, slot=1, args=(11505200, 1501802, 6, 1503201, 1501811, 11505210, 11500822, 1501804))
    IfFlagOff(0, 11505210)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(11500750, slot=2, args=(11505200, 1501803, 7, 1503202, 1501811, 11505210, 11500823, 1501804))
    IfFlagOff(0, 11505210)
    Restart()
    RunEvent(11500700, slot=40, args=(11505200, 1501804, 8, 18.5, 1501811, 11505210), arg_types="iiifii")
    IfFlagOff(0, 11505210)
    Restart()


def Event11500796():
    """ 11500796: Event 11500796 """
    IfFlagOn(0, 11505221)
    DisableFlag(11505221)
    EnableFlag(11505211)
    DisableObject(1501800)
    EnableObject(1501805)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(11500700, slot=1, args=(11505201, 1501805, 1, 2.5, 1501812, 11505211), arg_types="iiifii")
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(11500700, slot=11, args=(11505201, 1501805, 2, 7.5, 1501813, 11505211), arg_types="iiifii")
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(11500700, slot=21, args=(11505201, 1501805, 3, 7.5, 1501810, 11505211), arg_types="iiifii")
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(11500700, slot=31, args=(11505201, 1501805, 4, 12.5, 1501811, 11505211), arg_types="iiifii")
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(11500750, slot=0, args=(11505201, 1501801, 5, 1503200, 1501811, 11505211, 11500821, 1501805))
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(11500750, slot=1, args=(11505201, 1501802, 6, 1503201, 1501811, 11505211, 11500822, 1501805))
    IfFlagOff(0, 11505211)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(11500750, slot=2, args=(11505201, 1501803, 7, 1503202, 1501811, 11505211, 11500823, 1501805))
    IfFlagOff(0, 11505211)
    Restart()
    RunEvent(11500700, slot=41, args=(11505201, 1501805, 8, 18.5, 1501811, 11505211), arg_types="iiifii")
    IfFlagOff(0, 11505211)
    Restart()


def Event11500797():
    """ 11500797: Event 11500797 """
    IfFlagOn(0, 11505222)
    DisableFlag(11505222)
    EnableFlag(11505212)
    DisableObject(1501800)
    EnableObject(1501806)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(11500700, slot=2, args=(11505202, 1501806, 1, 2.5, 1501812, 11505212), arg_types="iiifii")
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(11500700, slot=12, args=(11505202, 1501806, 2, 7.5, 1501813, 11505212), arg_types="iiifii")
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(11500700, slot=22, args=(11505202, 1501806, 3, 7.5, 1501810, 11505212), arg_types="iiifii")
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(11500700, slot=32, args=(11505202, 1501806, 4, 12.5, 1501811, 11505212), arg_types="iiifii")
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(11500750, slot=0, args=(11505202, 1501801, 5, 1503200, 1501811, 11505212, 11500821, 1501806))
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(11500750, slot=1, args=(11505202, 1501802, 6, 1503201, 1501811, 11505212, 11500822, 1501806))
    IfFlagOff(0, 11505212)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(11500750, slot=2, args=(11505202, 1501803, 7, 1503202, 1501811, 11505212, 11500823, 1501806))
    IfFlagOff(0, 11505212)
    Restart()
    RunEvent(11500700, slot=42, args=(11505202, 1501806, 8, 18.5, 1501811, 11505212), arg_types="iiifii")
    IfFlagOff(0, 11505212)
    Restart()


def Event11500798():
    """ 11500798: Event 11500798 """
    IfFlagOn(0, 11505223)
    DisableFlag(11505223)
    EnableFlag(11505213)
    DisableObject(1501800)
    EnableObject(1501807)
    SkipLinesIfFlagOff(3, 11500812)
    RunEvent(11500700, slot=3, args=(11505203, 1501807, 1, 2.5, 1501812, 11505213), arg_types="iiifii")
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500803)
    RunEvent(11500700, slot=13, args=(11505203, 1501807, 2, 7.5, 1501813, 11505213), arg_types="iiifii")
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOff(3, 11500806)
    RunEvent(11500700, slot=23, args=(11505203, 1501807, 3, 7.5, 1501810, 11505213), arg_types="iiifii")
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500830)
    RunEvent(11500700, slot=33, args=(11505203, 1501807, 4, 12.5, 1501811, 11505213), arg_types="iiifii")
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500821)
    RunEvent(11500750, slot=0, args=(11505203, 1501801, 5, 1503200, 1501811, 11505213, 11500821, 1501807))
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500822)
    RunEvent(11500750, slot=1, args=(11505203, 1501802, 6, 1503201, 1501811, 11505213, 11500822, 1501807))
    IfFlagOff(0, 11505213)
    Restart()
    SkipLinesIfFlagOn(3, 11500823)
    RunEvent(11500750, slot=2, args=(11505203, 1501803, 7, 1503202, 1501811, 11505213, 11500823, 1501807))
    IfFlagOff(0, 11505213)
    Restart()
    RunEvent(11500700, slot=43, args=(11505203, 1501807, 8, 18.5, 1501811, 11505213), arg_types="iiifii")
    IfFlagOff(0, 11505213)
    Restart()


def Event11500700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 11500700: Event 11500700 """
    DisableCollision(1503210)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        arg_0_3,
        arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=arg_12_15,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    RemoveObjectFlag(arg_0_3)
    DisableObject(arg_4_7)
    EndOfAnimation(arg_4_7, 0)
    DisableFlag(arg_20_23)


def Event11500750(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 11500750: Event 11500750 """
    DisableCollision(1503210)
    EnableFlag(arg_24_27)
    EnableObject(arg_4_7)
    DisableObject(arg_28_31)
    ForceAnimation(arg_16_19, 1)
    CreateHazard(
        arg_0_3,
        arg_4_7,
        model_point=101,
        behavior_param_id=5050,
        target_type=DamageTargetType.Character,
        radius=1.7000000476837158,
        life=12.5,
        repetition_time=0.20000000298023224,
    )
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableCollision(arg_12_15)
    RemoveObjectFlag(arg_0_3)
    DisableFlag(arg_20_23)


def Event11500830():
    """ 11500830: Event 11500830 """
    IfCharacterInsideRegion(0, PLAYER, region=1502810)
    EnableFlag(11500830)


def Event11500831():
    """ 11500831: Event 11500831 """
    DisableNetworkSync()
    IfFlagOn(1, 11500751)
    IfCharacterInsideRegion(1, PLAYER, region=1502811)
    IfFlagOn(2, 11500752)
    IfCharacterInsideRegion(2, PLAYER, region=1502812)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Kill(PLAYER, award_souls=False)


def Event11500850():
    """ 11500850: Event 11500850 """
    DisableFlag(11505250)
    IfFlagOff(1, 11505250)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOff(2, 11505250)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1501790,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    DisableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFinishedConditionFalse(23, 1)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    SkipLinesIfFlagOff(4, 11500812)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(1501790, 3, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500812)
    ForceAnimation(1501790, 2, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500806)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOn(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500806)
    ForceAnimation(1501790, 0, wait_for_completion=True)
    Restart()
    RestartIfFinishedConditionFalse(2)
    Move(PLAYER, destination=1501790, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    SkipLinesIfFlagOff(4, 11500812)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(1501790, 5, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOn(4, 11500803)
    EnableFlag(11500803)
    EnableFlag(11500812)
    ForceAnimation(1501790, 4, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500806)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    Restart()
    SkipLinesIfFlagOff(4, 11500809)
    DisableFlag(11500809)
    EnableFlag(11500806)
    ForceAnimation(1501790, 6, wait_for_completion=True)
    Restart()
    EnableFlag(11500802)
    Restart()


def Event11505255():
    """ 11505255: Event 11505255 """
    IfFlagOff(1, 11505250)
    IfFlagOff(1, 11505251)
    IfFlagOff(1, 11500809)
    IfTimeElapsed(1, 2.0)
    IfCharacterInsideRegion(1, PLAYER, region=1502800)
    IfFlagOff(2, 11505250)
    IfFlagOff(2, 11505252)
    IfFlagOn(2, 11500803)
    IfTimeElapsed(2, 2.0)
    IfCharacterInsideRegion(2, PLAYER, region=1502801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11505250)
    SkipLinesIfFinishedConditionTrue(19, 2)
    EnableFlag(11505251)
    DisableFlag(11505252)
    SkipLinesIfFlagOn(5, 11500803)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    EnableFlag(11500803)
    EnableFlag(11500809)
    ForceAnimation(1501790, 0, wait_for_completion=True)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500806)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500806)
    EnableFlag(11500809)
    ForceAnimation(1501790, 1, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500812)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500812)
    EnableFlag(11500809)
    ForceAnimation(1501790, 5, wait_for_completion=True)
    SkipLines(18)
    DisableFlag(11505251)
    EnableFlag(11505252)
    SkipLinesIfFlagOff(5, 11500809)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500809)
    DisableFlag(11500803)
    ForceAnimation(1501790, 6, wait_for_completion=True)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500806)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500806)
    DisableFlag(11500803)
    ForceAnimation(1501790, 7, wait_for_completion=True)
    SkipLinesIfFlagOff(4, 11500812)
    CreateTemporaryVFX(150001, anchor_entity=1501790, anchor_type=CoordEntityType.Object, model_point=-1)
    DisableFlag(11500812)
    DisableFlag(11500803)
    ForceAnimation(1501790, 3, wait_for_completion=True)
    DisableFlag(11505250)
    Restart()


def Event11500840():
    """ 11500840: Event 11500840 """
    IfFlagOn(0, 11505240)
    EnableFlag(11505240)
    IfFlagOff(0, 11505240)
    Restart()


def Event11500841(_, arg_0_3: int):
    """ 11500841: Event 11500841 """
    IfHost(1)
    IfFlagOn(1, 11505240)
    IfFlagOff(1, arg_0_3)
    IfHost(2)
    IfFlagOn(2, 11505240)
    IfFlagOn(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11505240)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableFlag(arg_0_3)
    SkipLines(1)
    EnableFlag(arg_0_3)
    Restart()


def Event11500835():
    """ 11500835: Event 11500835 """
    EndIfHost()
    WaitFrames(10)
    EnableFlag(11505360)
    IfFlagOn(1, 11505250)
    IfFlagOff(2, 11505250)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    Wait(3.0)
    SkipLinesIfFlagOn(1, 11500803)
    EndOfAnimation(1501790, 3)
    SkipLinesIfFlagOff(1, 11500806)
    EndOfAnimation(1501790, 0)
    SkipLinesIfFlagOff(1, 11500809)
    EndOfAnimation(1501790, 1)
    SkipLinesIfFlagOff(1, 11500812)
    EndOfAnimation(1501790, 2)


def Event11500100():
    """ 11500100: Event 11500100 """
    IfThisEventOff(1)
    IfCharacterInsideRegion(1, PLAYER, region=1502060)
    IfThisEventOn(2)
    IfFlagOff(2, 11500101)
    IfCharacterInsideRegion(2, PLAYER, region=1502061)
    IfThisEventOn(3)
    IfFlagOff(3, 11500101)
    IfCharacterInsideRegion(3, PLAYER, region=1502062)
    IfThisEventOn(4)
    IfFlagOn(4, 11500101)
    IfCharacterInsideRegion(4, PLAYER, region=1502060)
    IfThisEventOn(5)
    IfFlagOn(5, 11500101)
    IfCharacterInsideRegion(5, PLAYER, region=1502063)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableNavmeshType(1503100, NavmeshType.Solid)
    EnableNavmeshType(1503101, NavmeshType.Solid)
    EnableNavmeshType(1503102, NavmeshType.Solid)
    EnableNavmeshType(1503103, NavmeshType.Solid)
    SkipLinesIfFinishedConditionFalse(16, 1)
    EnableFlag(11500100)
    ForceAnimation(1501011, 0, wait_for_completion=True)
    DisableNavmeshType(1503100, NavmeshType.Solid)
    DisableNavmeshType(1503101, NavmeshType.Solid)
    DisableNavmeshType(1503102, NavmeshType.Solid)
    DisableNavmeshType(1503103, NavmeshType.Solid)
    EnableNavmeshType(1503100, NavmeshType.Wall)
    EnableNavmeshType(1503110, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503101, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503111, NavmeshType.Wall)
    EnableNavmeshType(1503102, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503112, NavmeshType.Wall)
    EnableNavmeshType(1503103, NavmeshType.Wall)
    EnableNavmeshType(1503113, NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(0, region=1502062)
    Restart()
    SkipLinesIfFinishedConditionTrue(27, 4)
    SkipLinesIfFinishedConditionTrue(26, 5)
    EnableFlag(11500101)
    DisableNavmeshType(1503100, NavmeshType.Wall)
    DisableNavmeshType(1503110, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503101, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503111, NavmeshType.Wall)
    DisableNavmeshType(1503102, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503112, NavmeshType.Wall)
    DisableNavmeshType(1503103, NavmeshType.Wall)
    DisableNavmeshType(1503113, NavmeshType.WallTouchingFloor)
    ForceAnimation(1501011, 1, wait_for_completion=True)
    DisableNavmeshType(1503100, NavmeshType.Solid)
    DisableNavmeshType(1503101, NavmeshType.Solid)
    DisableNavmeshType(1503102, NavmeshType.Solid)
    DisableNavmeshType(1503103, NavmeshType.Solid)
    EnableNavmeshType(1503100, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503110, NavmeshType.Wall)
    EnableNavmeshType(1503101, NavmeshType.Wall)
    EnableNavmeshType(1503111, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503102, NavmeshType.Wall)
    EnableNavmeshType(1503112, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503103, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503113, NavmeshType.Wall)
    IfAllPlayersOutsideRegion(6, region=1502060)
    IfAllPlayersOutsideRegion(6, region=1502063)
    IfConditionTrue(0, input_condition=6)
    Restart()
    DisableFlag(11500101)
    DisableNavmeshType(1503100, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503110, NavmeshType.Wall)
    DisableNavmeshType(1503101, NavmeshType.Wall)
    DisableNavmeshType(1503111, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503102, NavmeshType.Wall)
    DisableNavmeshType(1503112, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503103, NavmeshType.WallTouchingFloor)
    DisableNavmeshType(1503113, NavmeshType.Wall)
    ForceAnimation(1501011, 2, wait_for_completion=True)
    DisableNavmeshType(1503100, NavmeshType.Solid)
    DisableNavmeshType(1503101, NavmeshType.Solid)
    DisableNavmeshType(1503102, NavmeshType.Solid)
    DisableNavmeshType(1503103, NavmeshType.Solid)
    EnableNavmeshType(1503100, NavmeshType.Wall)
    EnableNavmeshType(1503110, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503101, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503111, NavmeshType.Wall)
    EnableNavmeshType(1503102, NavmeshType.WallTouchingFloor)
    EnableNavmeshType(1503112, NavmeshType.Wall)
    EnableNavmeshType(1503103, NavmeshType.Wall)
    EnableNavmeshType(1503113, NavmeshType.WallTouchingFloor)
    IfAllPlayersOutsideRegion(7, region=1502061)
    IfAllPlayersOutsideRegion(7, region=1502062)
    IfConditionTrue(0, input_condition=7)
    Restart()


def Event11500102():
    """ 11500102: Event 11500102 """
    SkipLinesIfThisEventOff(4)
    SkipLinesIfFlagOn(1, 11500100)
    EndOfAnimation(1501011, 20)
    End()
    IfThisEventOff(1)
    IfPlayerHasGood(1, 2003, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1501011, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7111)
    ForceAnimation(1501011, 10)
    EndIfClient()
    DisplayDialog(
        10010862,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11500103():
    """ 11500103: Event 11500103 """
    DisableNetworkSync()
    IfFlagOff(1, 11500102)
    IfPlayerDoesNotHaveGood(1, 2003, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501011,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        model_point=105,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010163,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11500106():
    """ 11500106: Event 11500106 """
    DisableNetworkSync()
    IfFlagOff(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=1501001,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11500107():
    """ 11500107: Event 11500107 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1501001, 0)
    End()
    IfFlagOff(1, 11500105)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1501001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11500105)
    Move(PLAYER, destination=1501001, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7112)
    ForceAnimation(1501001, 0)


def Event11500110(_, arg_0_3: int, arg_4_7: int):
    """ 11500110: Event 11500110 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    EnableFlag(arg_4_7)
    EndIfClient()
    IfPlayerHasGood(1, 2003, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(
        10010883,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(1)
    DisplayDialog(
        10010862,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )


def Event11505270(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11505270: Event 11505270 """
    SkipLinesIfFlagOff(2, arg_20_23)
    EndOfAnimation(arg_4_7, 0)
    SkipLines(12)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfObjectDamagedBy(-1, arg_4_7, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_20_23)
    CreateTemporaryVFX(150005, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, model_point=101)
    DeleteVFX(arg_8_11, erase_root_only=False)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    SkipLinesIfEqual(5, left=arg_20_23, right=11505284)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    IfTrueFlagCountGreaterThanOrEqual(0, 2, (11505280, 11505285))
    DisableFlag(arg_20_23)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    Restart()


def Event11505260():
    """ 11505260: Event 11505260 """
    IfFlagOn(0, 11505284)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501214,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501215,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501216,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1501217,
        model_point=101,
        behavior_id=5070,
        launch_angle_x=0,
        launch_angle_y=180,
        launch_angle_z=0,
    )
    IfFlagOff(0, 11505284)
    Restart()


@RestartOnRest
def Event11505050():
    """ 11505050: Event 11505050 """
    EndIfThisEventOn()
    DisableAI(1500101)
    IfCharacterInsideRegion(-1, PLAYER, region=1502101)
    IfAttacked(-1, 1500101, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11505050)
    IfFlagOff(0, 11505052)
    EnableAI(1500101)


@RestartOnRest
def Event11505051():
    """ 11505051: Event 11505051 """
    IfFlagOn(1, 11505050)
    IfFlagOn(2, 11505052)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    Move(1500101, destination=1502100, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1500101, 9001, wait_for_completion=True)
    DisableFlag(11505052)
    Restart()


@RestartOnRest
def Event11505055():
    """ 11505055: Event 11505055 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1500100, UpdateAuthority.Forced)
    IfObjectDestroyed(1, 1501100)
    IfObjectDestroyed(1, 1501101)
    IfObjectDestroyed(1, 1501102)
    IfObjectDestroyed(1, 1501103)
    IfObjectDestroyed(1, 1501104)
    IfObjectDestroyed(1, 1501105)
    IfObjectDestroyed(1, 1501106)
    IfObjectDestroyed(1, 1501107)
    IfObjectDestroyed(1, 1501108)
    IfConditionTrue(0, input_condition=1)
    AICommand(1500100, command_id=20, slot=1)
    ReplanAI(1500100)


def Event11505110():
    """ 11505110: Event 11505110 """
    IfFlagOn(1, 11505100)
    IfFlagOn(2, 11505100)
    IfFlagOn(3, 11505100)
    IfFlagOn(4, 11505100)
    IfFlagOn(5, 11505100)
    IfFlagOn(6, 11505100)
    IfFlagOn(7, 11505100)
    IfFlagOn(1, 11505111)
    IfFlagOn(2, 11505112)
    IfFlagOn(3, 11505113)
    IfFlagOn(4, 11505114)
    IfFlagOn(5, 11505115)
    IfFlagOn(6, 11505116)
    IfFlagRangeAllOff(7, (11505111, 11505116))
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, 6)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5305,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 5)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 4)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5303,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 3)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5302,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 2)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5301,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    SkipLinesIfFinishedConditionFalse(8, 1)
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()
    ShootProjectile(
        owner_entity=1500200,
        projectile_id=1500100,
        model_point=50,
        behavior_id=5304,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DisableFlagRange((11505111, 11505116))
    AICommand(1500100, command_id=-1, slot=2)
    DisableFlag(11505105)
    RestartEvent(11505102)
    Wait(1.0)
    DisableFlag(11505100)
    Restart()


def Event11505111(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11505111: Event 11505111 """
    IfFlagOff(1, 11505100)
    IfFlagOff(1, 11505105)
    IfTimeElapsed(1, 2.0)
    IfFlagOff(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505112)
    IfAllPlayersOutsideRegion(1, region=1502701)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505113)
    IfAllPlayersOutsideRegion(1, region=1502702)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505114)
    IfAllPlayersOutsideRegion(1, region=1502703)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505115)
    IfAllPlayersOutsideRegion(1, region=1502704)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505116)
    IfAllPlayersOutsideRegion(1, region=1502705)
    SkipLinesIfGreaterThanOrEqual(1, left=arg_0_3, right=11505117)
    IfAllPlayersOutsideRegion(1, region=1502710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((11505111, 11505116))
    EnableFlag(arg_0_3)
    AICommand(1500100, command_id=arg_8_11, slot=2)
    Restart()


def Event11505101():
    """ 11505101: Event 11505101 """
    IfFlagOn(0, 11505105)
    EnableFlag(11505105)
    IfFlagOff(0, 11505105)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


def Event11505102():
    """ 11505102: Event 11505102 """
    DisableNetworkSync()
    IfFlagOn(0, 11505105)
    Wait(30.0)
    DisableFlag(11505105)
    DisableFlag(11505100)
    Restart()


@RestartOnRest
def Event11505060(_, arg_0_3: int):
    """ 11505060: Event 11505060 """
    IfHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest
def Event11505070(_, arg_0_3: int):
    """ 11505070: Event 11505070 """
    DisableNetworkSync()
    IfHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest
def Event11505080():
    """ 11505080: Event 11505080 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(1500122)
    End()
    IfAttacked(-1, 1500122, attacker=PLAYER)
    IfHealthNotEqual(-1, 1500122, 1.0)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(1500122)
    ForceAnimation(1500122, 2000)


@RestartOnRest
def Event11505010():
    """ 11505010: Event 11505010 """
    IfCharacterAlive(1, 1500010)
    IfCharacterBackreadEnabled(1, 1500010)
    IfCharacterHasSpecialEffect(1, 1500010, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1500010,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=1500010,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=1500010,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(1500010, command_id=10, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event11505011():
    """ 11505011: Event 11505011 """
    IfCharacterDoesNotHaveSpecialEffect(1, 1500010, 5420)
    IfAttacked(1, 1500010, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    IfCharacterBackreadDisabled(7, 1500010)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, 1500010, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, 1500010, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, 1500010, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(1500010, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, 1500010, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(1500010, 3006, wait_for_completion=True)
    ReplanAI(1500010)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    Restart()


@RestartOnRest
def Event11505012():
    """ 11505012: Event 11505012 """
    IfCharacterHasSpecialEffect(1, 1500010, 5421)
    IfCharacterHasSpecialEffect(1, 1500010, 3150)
    IfCharacterHasSpecialEffect(2, 1500010, 5420)
    IfCharacterHasSpecialEffect(2, 1500010, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(1500010, command_id=200, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=210, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, 1500010, 5420)
    IfCharacterHasSpecialEffect(-2, 1500010, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11505013():
    """ 11505013: Event 11505013 """
    IfCharacterHasSpecialEffect(1, 1500010, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, 1500010, 3150)
    IfCharacterHasSpecialEffect(2, 1500010, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, 1500010, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(1500010, 3150)
    CancelSpecialEffect(1500010, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(1500010, command_id=201, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(1500010, command_id=211, slot=0)
    ReplanAI(1500010)
    Wait(0.10000000149011612)
    AICommand(1500010, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, 1500010, 5420)
    IfCharacterHasSpecialEffect(-2, 1500010, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event11505014():
    """ 11505014: Event 11505014 """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, 1500010, region=1502010)
    IfCharacterBackreadDisabled(1, 1500010)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(1500010, 5421)
    ClearTargetList(1500010)
    ReplanAI(1500010)
    Move(1500010, destination=1502010, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, 1500010)
    Restart()


@RestartOnRest
def Event11505015():
    """ 11505015: Event 11505015 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, 1500010)
    EndIfConditionTrue(1)
    ResetAnimation(1500010, disable_interpolation=True)
    ForceAnimation(1500010, 0)
    ReplanAI(1500010)


@RestartOnRest
def Event11500900():
    """ 11500900: Event 11500900 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(1500010)
    End()
    IfCharacterDead(0, 1500010)
    End()


def Event11500210():
    """ 11500210: Event 11500210 """
    EndIfClient()
    IfInsideMap(0, game_map=SENS_FORTRESS)
    IfTimeElapsed(0, 5.0)
    IfFlagOn(0, 11)
    IfActionButton(0, prompt_text=10010120, anchor_entity=1502505, anchor_type=CoordEntityType.Region)
    DisableBackread(1500201)
    WaitFrames(1)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150000,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1502501,
        move_to_map=ANOR_LONDO,
    )
    SkipLines(2)
    SetMapDrawParamSlot(15, slot=2)
    PlayCutscene(
        150002,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=1502501,
        move_to_map=ANOR_LONDO,
    )
    WaitFrames(1)
    AwardAchievement(33)
    Restart()


@RestartOnRest
def Event11500860(_, arg_0_3: int):
    """ 11500860: Event 11500860 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


def Event11500600(_, arg_0_3: int, arg_4_7: int):
    """ 11500600: Event 11500600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11500510(_, arg_0_3: int, arg_4_7: int):
    """ 11500510: Event 11500510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
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


def Event11500520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500520: Event 11500520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11500530():
    """ 11500530: Event 11500530 """
    SkipLinesIfFlagOn(3, 11500593)
    DisableObjectActivation(1501032, obj_act_id=-1)
    IfFlagOn(0, 11500593)
    EnableObjectActivation(1501032, obj_act_id=-1)
    EndIfThisEventOn()
    IfFlagOn(0, 11500112)
    DisableFlag(71500021)


def Event11500531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500531: Event 11500531 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1090)
    IfFlagOn(1, 11500112)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11500532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500532: Event 11500532 """
    IfFlagOff(1, 1096)
    IfFlagOn(1, 1092)
    IfFlagOn(1, 11500594)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11500533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500533: Event 11500533 """
    IfFlagOff(1, 1114)
    IfFlagOn(1, 1113)
    IfFlagOn(1, 723)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11500534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500534: Event 11500534 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1490)
    IfFlagOn(1, 11500591)
    IfFlagOn(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(arg_0_3, 1502510)
    Kill(1500120, award_souls=False)
    Kill(1500121, award_souls=False)


def Event11500535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500535: Event 11500535 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1490)
    IfFlagOff(1, 11500591)
    IfFlagOn(1, 11500200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1502510, destination_type=CoordEntityType.Region, set_draw_parent=1503300)
    SetNest(arg_0_3, 1502510)
    Kill(1500120, award_souls=False)
    Kill(1500121, award_souls=False)


def Event11500536(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11500536: Event 11500536 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1491)
    IfFlagOn(1, 11500850)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfHost(2)
    IfFlagOff(2, 1512)
    IfFlagOn(2, 1492)
    IfFlagOn(2, 11500592)
    IfFlagOn(2, 11500850)
    IfCharacterBackreadDisabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11505030():
    """ 11505030: Event 11505030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6510, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11505033)
    IfClient(2)
    IfFlagOn(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6510)
    EndIfFlagOn(11)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6510)
    IfEntityWithinDistance(1, 6510, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6510, region=1502000, summon_flag=11505031, dismissal_flag=11505033)


def Event11505990(_, arg_0_3: int, arg_4_7: int):
    """ 11505990: Event 11505990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11505029():
    """ 11505029: Event 11505029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6510, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11505033)
    IfClient(2)
    IfFlagOn(2, 11505031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6510)
    EndIfFlagOn(11)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfFlagOff(1, 11505031)
    IfFlagOff(1, 11505033)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6510)
    IfEntityWithinDistance(1, 6510, PLAYER, radius=10.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6510, region=1502000, summon_flag=11505031, dismissal_flag=11505033)


def Event11505032():
    """ 11505032: Event 11505032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11505031)
    IfFlagOn(1, 11505393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6510, command_id=10, slot=0)
    ReplanAI(6510)
    IfCharacterInsideRegion(0, 6510, region=1502998)
    RotateToFaceEntity(6510, 1502997)
    ForceAnimation(6510, 7410)
    AICommand(6510, command_id=-1, slot=0)
    ReplanAI(6510)


def Event11505843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11505843: Event 11505843 """
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


def Event11505846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11505846: Event 11505846 """
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
