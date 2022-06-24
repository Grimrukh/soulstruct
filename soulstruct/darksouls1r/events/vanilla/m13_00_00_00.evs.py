"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11300992, obj=1301960)
    RegisterBonfire(bonfire_flag=11300984, obj=1301961)
    RegisterBonfire(bonfire_flag=11300976, obj=1301962)
    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=1301140)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=1301141)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=1301142)
    SkipLinesIfFlagDisabled(1, 6)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301143)
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=1301144)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=1301145)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=1301146)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=1301147)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=1301148)
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=1301149)
    SkipLinesIfClient(3)
    DisableFlag(11300000)
    DisableObject(1301994)
    DeleteVFX(vfx_id=1301995, erase_root_only=False)
    Event_11300090(0, 1301700, 1301701, 1302650, 1302651)
    Event_11305065()
    Event_11305066()
    Event_11305067()
    Event_11300800()
    Event_11300300()
    Event_11300350()
    Event_11300900(0, 11300900, 1301000, 1301100, 1304000)
    Event_11300900(1, 11300901, 1301001, 1301101, 1304001)
    Event_11305032(0, 11300902, 11300903, 11305035, 11305036)
    Event_11305030(0, 11300402, 11305035, 11305036, 1301002, 1301102, 1304002)
    Event_11305032(1, 11300904, 11300905, 11305037, 11305038)
    Event_11305030(1, 11300403, 11305037, 11305038, 1301003, 1301103, 1304003)
    Event_11305000()
    Event_11305001()
    Event_11305002()
    Event_11305003()
    Event_11305004()
    Event_11305009()
    Event_11300420(0, 10000)
    Event_11300420(1, 10001)
    Event_11300420(2, 10002)
    Event_11300420(3, 10003)
    Event_11300420(4, 10004)
    Event_11300420(5, 10005)
    Event_11300420(6, 10006)
    Event_11300420(7, 10007)
    Event_11300420(8, 10008)
    Event_11300420(9, 10009)
    Event_11300420(10, 10010)
    Event_11300420(11, 10011)
    Event_11300420(12, 10012)
    Event_11300420(13, 10013)
    Event_11300420(14, 10014)
    Event_11300420(15, 10015)
    Event_11300420(16, 10016)
    Event_11300420(17, 10017)
    Event_11300210()
    Event_11305060()
    Event_11300200()
    Event_11305045()
    Event_11300100(0, 11300100, 1302100, 1301010, 303000000)
    Event_11300100(1, 11300101, 1302101, 1301011, 303100000)
    Event_11300100(2, 11300102, 1302102, 1301012, 303200000)
    Event_11300100(3, 11300103, 1302103, 1301013, 303300000)
    Event_11300100(4, 11300104, 1302104, 1301014, 303400000)
    Event_11300100(5, 11300105, 1302105, 1301015, 303500000)
    Event_11300150()
    Event_11300160()
    Event_11300700(0, 1301200, 11300750)
    Event_11300700(1, 1301201, 11300751)
    Event_11300700(2, 1301202, 11300752)
    Event_11300700(3, 1301203, 11300753)
    Event_11300700(4, 1301204, 11300754)
    Event_11300700(5, 1301205, 11300755)
    Event_11300700(6, 1301206, 11300756)
    Event_11300700(7, 1301207, 11300757)
    Event_11300700(8, 1301208, 11300758)
    Event_11300700(9, 1301209, 11300759)
    Event_11300700(10, 1301210, 11300760)
    Event_11300700(12, 1301212, 11300762)
    Event_11300700(13, 1301213, 11300763)
    Event_11300700(14, 1301214, 11300764)
    Event_11300700(15, 1301215, 11300765)
    Event_11300700(16, 1301216, 11300766)
    Event_11300700(17, 1301217, 11300767)
    Event_11300700(18, 1301218, 11300768)
    Event_11300700(19, 1301219, 11300769)
    Event_11300880()
    DisableSoundEvent(sound_id=1303800)
    SkipLinesIfFlagDisabled(4, 6)
    DisableObject(1301990)
    DeleteVFX(vfx_id=1301991, erase_root_only=False)
    Event_11305392()
    SkipLines(32)
    Event_11305390()
    Event_11305391()
    Event_11305393()
    Event_11305392()
    Event_11300001()
    Event_11305394()
    Event_11305395()
    Event_11300882()
    Event_11305396()
    Event_11305397()
    Event_11305398()
    Event_11305250()
    Event_11305350(0, 11305251, 11305252, 1300801, 1300802, 1302600, 1302612, 11305300)
    Event_11305350(1, 11305253, 11305254, 1300803, 1300804, 1302601, 1302611, 11305301)
    Event_11305350(2, 11305255, 11305256, 1300805, 1300806, 1302602, 1302610, 11305302)
    Event_11305350(3, 11305257, 11305258, 1300807, 1300808, 1302603, 1302609, 11305303)
    Event_11305350(4, 11305259, 11305260, 1300809, 1300810, 1302604, 1302608, 11305304)
    Event_11305350(5, 11305261, 11305262, 1300811, 1300812, 1302605, 1302607, 11305305)
    Event_11305350(6, 11305263, 11305264, 1300813, 1300814, 1302606, 1302606, 11305306)
    Event_11305370(0, 1300801, 11305251)
    Event_11305370(1, 1300802, 11305252)
    Event_11305370(2, 1300803, 11305253)
    Event_11305370(3, 1300804, 11305254)
    Event_11305370(4, 1300805, 11305255)
    Event_11305370(5, 1300806, 11305256)
    Event_11305370(6, 1300807, 11305257)
    Event_11305370(7, 1300808, 11305258)
    Event_11305370(8, 1300809, 11305259)
    Event_11305370(9, 1300810, 11305260)
    Event_11305370(10, 1300811, 11305261)
    Event_11305370(11, 1300812, 11305262)
    Event_11305370(12, 1300813, 11305263)
    Event_11305370(13, 1300814, 11305264)
    Event_11300850(0, 1300100, 0)
    Event_11300850(1, 1300120, 0)
    Event_11300850(2, 1300140, 0)
    Event_11300850(3, 1300160, 0)
    Event_11300850(4, 1300180, 0)
    Event_11300850(5, 1300200, 0)
    Event_11300850(6, 1300500, 33003000)
    Event_11300850(7, 1300501, 33003000)
    Event_11300850(8, 1300300, 0)
    Event_11300850(9, 1300400, 27902000)
    Event_11305846(0, 6, 1301990, 1301991)
    Event_11305843(0, 6, 1301990, 1302998, 1302997)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6550, event_flag=8948)
    Event_11305025()
    Event_11305029()
    Event_11305027()
    Event_11305990(0, 11305026, 6550)
    Event_11300510(0, 6200, 1341)
    Event_11300520(0, 6200, 1340, 1343, 1342)
    Event_11305061(0, 6200)
    HumanityRegistration(6320, event_flag=8478)
    SkipLinesIfFlagEnabled(2, 1627)
    SkipLinesIfFlagRangeAnyEnabled(1, (1620, 1621))
    DisableCharacter(6320)
    Event_11300510(1, 6320, 1627)
    Event_11300531(0, 6320, 1628)
    Event_11300530(0, 6320, 1620, 1631, 1621)
    Event_11300533(0, 6320, 1620, 1631, 1623)
    Event_11300592()
    Event_11300593()


@NeverRestart(11300090)
def Event_11300090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7, erase_root_only=False)
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
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)


@RestartOnRest(11305065)
def Event_11305065():
    """Event 11305065"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1300900)
    DisableCharacter(1300901)
    DisableCharacter(1300902)
    DisableCharacter(1300903)
    DisableCharacter(1300904)
    DisableCharacter(1300905)
    DisableCharacter(1300906)
    DisableCharacter(1300907)
    DisableCharacter(1300908)
    DisableCharacter(1300909)
    DisableCharacter(1300910)
    IfFlagEnabled(0, 11300050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1300900)
    EnableCharacter(1300901)
    EnableCharacter(1300902)
    EnableCharacter(1300903)
    EnableCharacter(1300904)
    EnableCharacter(1300905)
    EnableCharacter(1300906)
    EnableCharacter(1300907)
    EnableCharacter(1300908)
    EnableCharacter(1300909)
    EnableCharacter(1300910)


@RestartOnRest(11305066)
def Event_11305066():
    """Event 11305066"""
    IfFlagEnabled(-1, 11305069)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11300050)
    DisableFlag(11305069)
    EnableFlag(5001)
    Kill(1300900)
    Kill(1300901)
    Kill(1300902)
    Kill(1300903)
    Kill(1300904)
    Kill(1300905)
    Kill(1300906)
    Kill(1300907)
    Kill(1300908)
    Kill(1300909)
    Kill(1300910)


@RestartOnRest(11305067)
def Event_11305067():
    """Event 11305067"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=CATACOMBS)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11300050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=CATACOMBS)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11300050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=CATACOMBS)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11300050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=CATACOMBS)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11300050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=CATACOMBS)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11300050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=CATACOMBS)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11300050)
    RestartIfConditionFalse(-6)
    EnableFlag(11300050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=CATACOMBS)
    RestartIfConditionFalse(7)
    DisableFlag(11300050)
    EnableFlag(11305069)


@NeverRestart(11305390)
def Event_11305390():
    """Event 11305390"""
    IfFlagDisabled(1, 6)
    IfCharacterAlive(1, 1300800)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1301990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11305391)
def Event_11305391():
    """Event 11305391"""
    IfFlagDisabled(1, 6)
    IfFlagEnabled(1, 11305393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1302998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1301990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11305393)
def Event_11305393():
    """Event 11305393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 6)
    IfFlagEnabled(1, 11305390)
    IfCharacterInsideRegion(1, PLAYER, region=1302996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1300800)


@RestartOnRest(11305392)
def Event_11305392():
    """Event 11305392"""
    SkipLinesIfFlagDisabled(3, 6)
    DisableCharacter(1300800)
    Kill(1300800)
    End()
    SkipLinesIfFlagEnabled(1, 11300000)
    DisableCharacter(1300800)
    DisableAI(1300800)
    IfFlagDisabled(1, 6)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1302999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(8, 11300000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(130000, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1300800)
    EnableFlag(11300000)
    EnableFlag(11300005)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1300800, authority_level=UpdateAuthority.Forced)
    EnableAI(1300800)
    EnableBossHealthBar(1300800, name=3320)


@NeverRestart(11300001)
def Event_11300001():
    """Event 11300001"""
    IfHealthLessThanOrEqual(0, 1300800, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1300800, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1300800)
    EnableFlag(6)
    KillBoss(game_area_param_id=1300800)
    DisableObject(1301990)
    DeleteVFX(vfx_id=1301991)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301143)
    Event_11300880()


@NeverRestart(11305394)
def Event_11305394():
    """Event 11305394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 6)
    IfFlagEnabled(1, 11305392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11305391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1303800)


@NeverRestart(11305395)
def Event_11305395():
    """Event 11305395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 6)
    IfFlagEnabled(1, 11305394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1303800)


@NeverRestart(11305396)
def Event_11305396():
    """Event 11305396"""
    IfCharacterHasTAEEvent(0, 1300800, tae_event_id=600)
    DisableCharacter(1300800)
    DisableFlagRange((11305320, 11305326))
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1300800, authority_level=UpdateAuthority.Forced)
    EnableRandomFlagInRange(flag_range=(11305320, 11305326))
    EnableFlag(11305329)
    IfFlagDisabled(-1, 11305329)
    IfTimeElapsed(-1, seconds=5.0)
    IfConditionTrue(0, input_condition=-1)
    Wait(3.0)
    EnableCharacter(1300800)
    SkipLinesIfFlagDisabled(1, 11305320)
    Move(1300800, destination=1302600, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305321)
    Move(1300800, destination=1302602, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305322)
    Move(1300800, destination=1302604, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305323)
    Move(1300800, destination=1302605, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305324)
    Move(1300800, destination=1302606, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305325)
    Move(1300800, destination=1302608, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfFlagDisabled(1, 11305326)
    Move(1300800, destination=1302612, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=1)
    EnableCharacter(1300800)
    ForceAnimation(1300800, 7000, wait_for_completion=True)
    Restart()


@NeverRestart(11300882)
def Event_11300882():
    """Event 11300882"""
    IfFlagEnabled(1, 11305329)
    IfFlagEnabled(2, 11305329)
    IfFlagEnabled(3, 11305329)
    IfFlagEnabled(4, 11305329)
    IfFlagEnabled(5, 11305329)
    IfFlagEnabled(6, 11305329)
    IfFlagEnabled(7, 11305329)
    IfFlagEnabled(1, 11305320)
    IfFlagEnabled(2, 11305321)
    IfFlagEnabled(3, 11305322)
    IfFlagEnabled(4, 11305323)
    IfFlagEnabled(5, 11305324)
    IfFlagEnabled(6, 11305325)
    IfFlagEnabled(7, 11305326)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    EnableFlag(11305320)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    EnableFlag(11305321)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    EnableFlag(11305322)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    EnableFlag(11305323)
    SkipLinesIfFinishedConditionFalse(1, condition=5)
    EnableFlag(11305324)
    SkipLinesIfFinishedConditionFalse(1, condition=6)
    EnableFlag(11305325)
    SkipLinesIfFinishedConditionFalse(1, condition=7)
    EnableFlag(11305326)
    DisableFlag(11305329)
    Restart()


@NeverRestart(11305397)
def Event_11305397():
    """Event 11305397"""
    EndIfClient()
    SkipLinesIfFlagEnabled(4, 11305310)
    IfFlagDisabled(1, 11305399)
    IfCharacterHasTAEEvent(1, 1300800, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305310)
    DisableFlagRange((11305300, 11305306))
    EnableRandomFlagInRange(flag_range=(11305300, 11305306))
    SkipLinesIfFlagDisabled(2, 11305300)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305251, 11305252))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305301)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305253, 11305254))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305302)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305255, 11305256))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305303)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305257, 11305258))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305304)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305259, 11305260))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305305)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305261, 11305262))
    DisableFlag(11305310)
    SkipLinesIfFlagDisabled(2, 11305306)
    SkipLinesIfFlagRangeAnyEnabled(1, (11305263, 11305264))
    DisableFlag(11305310)
    RestartIfFlagEnabled(11305310)
    IfCharacterDoesNotHaveTAEEvent(0, 1300800, tae_event_id=700)
    Restart()


@NeverRestart(11305398)
def Event_11305398():
    """Event 11305398"""
    IfHealthLessThanOrEqual(0, 1300800, value=0.30000001192092896)
    EnableFlag(11305399)
    AICommand(1300800, command_id=1, slot=1)
    ReplanAI(1300800)
    Event_11305330(0, 1300801, 11305251)
    Event_11305330(1, 1300802, 11305252)
    Event_11305330(2, 1300803, 11305253)
    Event_11305330(3, 1300804, 11305254)
    Event_11305330(4, 1300805, 11305255)
    Event_11305330(5, 1300806, 11305256)
    Event_11305330(6, 1300807, 11305257)
    Event_11305330(7, 1300808, 11305258)
    Event_11305330(8, 1300809, 11305259)
    Event_11305330(9, 1300810, 11305260)
    Event_11305330(10, 1300811, 11305261)
    Event_11305330(11, 1300812, 11305262)
    Event_11305330(12, 1300813, 11305263)
    Event_11305330(13, 1300814, 11305264)
    IfFlagRangeAllDisabled(0, flag_range=(11305251, 11305264))
    AICommand(1300800, command_id=2, slot=1)
    ReplanAI(1300800)
    IfFlagEnabled(1, 11305399)
    IfCharacterHasTAEEvent(1, 1300800, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    AICommand(1300800, command_id=1, slot=1)
    ReplanAI(1300800)
    Event_11305350(10, 11305251, 11305252, 1300801, 1300802, 1302602, 1302603, 11305300)
    Event_11305350(11, 11305253, 11305254, 1300803, 1300804, 1302604, 1302605, 11305301)
    Event_11305350(12, 11305255, 11305256, 1300805, 1300806, 1302607, 1302608, 11305302)
    Event_11305350(13, 11305257, 11305258, 1300807, 1300808, 1302609, 1302612, 11305303)


@NeverRestart(11305330)
def Event_11305330(_, arg_0_3: int, arg_4_7: int):
    """Event 11305330"""
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfFlagDisabled(0, arg_4_7)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)


@NeverRestart(11305350)
def Event_11305350(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11305350"""
    SkipLinesIfFlagEnabled(5, 11305399)
    IfHost(1)
    IfFlagDisabled(1, 11305310)
    IfFlagEnabled(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    WaitForNetworkApproval(max_seconds=3.0)
    DisableFlag(arg_24_27)
    AddSpecialEffect(arg_8_11, 5450)
    AddSpecialEffect(arg_12_15, 5450)
    Move(arg_8_11, destination=arg_16_19, destination_type=CoordEntityType.Region, short_move=True)
    Move(arg_12_15, destination=arg_20_23, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ReplanAI(arg_8_11)
    ReplanAI(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    EndIfFlagEnabled(11305399)
    RestartEvent(event_id=11305250)
    Restart()


@NeverRestart(11305370)
def Event_11305370(_, arg_0_3: int, arg_4_7: int):
    """Event 11305370"""
    IfFlagEnabled(1, arg_4_7)
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=710)
    IfHealthLessThanOrEqual(2, 1300800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(3, condition=1)
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=710)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    DisableCharacter(arg_0_3)
    DisableFlag(arg_4_7)
    EndIfFinishedConditionTrue(input_condition=2)
    RestartEvent(event_id=11305250)
    RestartIfFlagDisabled(arg_4_7)


@NeverRestart(11305250)
def Event_11305250():
    """Event 11305250"""
    IfFlagEnabled(0, 11305392)
    AIEvent(1300800, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300801, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300802, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300803, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300804, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300805, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300806, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300807, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300808, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300809, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300810, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300811, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300812, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300813, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300814, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    ReplanAI(1300800)
    ReplanAI(1300801)
    ReplanAI(1300802)
    ReplanAI(1300803)
    ReplanAI(1300804)
    ReplanAI(1300805)
    ReplanAI(1300806)
    ReplanAI(1300807)
    ReplanAI(1300808)
    ReplanAI(1300809)
    ReplanAI(1300810)
    ReplanAI(1300811)
    ReplanAI(1300812)
    ReplanAI(1300813)
    ReplanAI(1300814)
    IfCharacterDead(0, 1300800)
    End()


@RestartOnRest(11300880)
def Event_11300880():
    """Event 11300880"""
    DisableHealthBar(1300801)
    DisableHealthBar(1300802)
    DisableHealthBar(1300803)
    DisableHealthBar(1300804)
    DisableHealthBar(1300805)
    DisableHealthBar(1300806)
    DisableHealthBar(1300807)
    DisableHealthBar(1300808)
    DisableHealthBar(1300809)
    DisableHealthBar(1300810)
    DisableHealthBar(1300811)
    DisableHealthBar(1300812)
    DisableHealthBar(1300813)
    DisableHealthBar(1300814)
    DisableCharacter(1300801)
    DisableCharacter(1300802)
    DisableCharacter(1300803)
    DisableCharacter(1300804)
    DisableCharacter(1300805)
    DisableCharacter(1300806)
    DisableCharacter(1300807)
    DisableCharacter(1300808)
    DisableCharacter(1300809)
    DisableCharacter(1300810)
    DisableCharacter(1300811)
    DisableCharacter(1300812)
    DisableCharacter(1300813)
    DisableCharacter(1300814)
    SkipLinesIfFlagEnabled(14, 6)
    EnableImmortality(1300801)
    EnableImmortality(1300802)
    EnableImmortality(1300803)
    EnableImmortality(1300804)
    EnableImmortality(1300805)
    EnableImmortality(1300806)
    EnableImmortality(1300807)
    EnableImmortality(1300808)
    EnableImmortality(1300809)
    EnableImmortality(1300810)
    EnableImmortality(1300811)
    EnableImmortality(1300812)
    EnableImmortality(1300813)
    EnableImmortality(1300814)
    EndIfFlagDisabled(6)
    Kill(1300801)
    Kill(1300802)
    Kill(1300803)
    Kill(1300804)
    Kill(1300805)
    Kill(1300806)
    Kill(1300807)
    Kill(1300808)
    Kill(1300809)
    Kill(1300810)
    Kill(1300811)
    Kill(1300812)
    Kill(1300813)
    Kill(1300814)


@NeverRestart(11300700)
def Event_11300700(_, arg_0_3: int, arg_4_7: int):
    """Event 11300700"""
    IfEntityWithinDistance(0, entity=arg_0_3, other_entity=PLAYER, radius=1.5)
    CreateHazard(
        obj_flag=arg_4_7,
        obj=arg_0_3,
        model_point=100,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=arg_4_7,
        obj=arg_0_3,
        model_point=101,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=arg_4_7,
        obj=arg_0_3,
        model_point=102,
        behavior_param_id=5120,
        target_type=DamageTargetType.Character,
        radius=0.10000000149011612,
        life=1.0,
        repetition_time=0.0,
    )
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


@NeverRestart(11300300)
def Event_11300300():
    """Event 11300300"""
    IfFlagDisabled(0, 11300402)
    CreateHazard(
        obj_flag=11300301,
        obj=1301102,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300302,
        obj=1301102,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300303,
        obj=1301102,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300304,
        obj=1301102,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300305,
        obj=1301102,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300306,
        obj=1301102,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300307,
        obj=1301102,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300308,
        obj=1301102,
        model_point=15,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    IfFlagEnabled(0, 11300402)
    RemoveObjectFlag(obj_flag=11300301)
    RemoveObjectFlag(obj_flag=11300302)
    RemoveObjectFlag(obj_flag=11300303)
    RemoveObjectFlag(obj_flag=11300304)
    RemoveObjectFlag(obj_flag=11300305)
    RemoveObjectFlag(obj_flag=11300306)
    RemoveObjectFlag(obj_flag=11300307)
    RemoveObjectFlag(obj_flag=11300308)
    Restart()


@NeverRestart(11300350)
def Event_11300350():
    """Event 11300350"""
    IfFlagDisabled(0, 11300403)
    CreateHazard(
        obj_flag=11300351,
        obj=1301103,
        model_point=2,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300352,
        obj=1301103,
        model_point=4,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300353,
        obj=1301103,
        model_point=6,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300354,
        obj=1301103,
        model_point=8,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300355,
        obj=1301103,
        model_point=10,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300356,
        obj=1301103,
        model_point=12,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300357,
        obj=1301103,
        model_point=14,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300358,
        obj=1301103,
        model_point=33,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300359,
        obj=1301103,
        model_point=35,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300360,
        obj=1301103,
        model_point=37,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=10.0,
        repetition_time=5.0,
    )
    CreateHazard(
        obj_flag=11300361,
        obj=1301103,
        model_point=39,
        behavior_param_id=5100,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=10.0,
        repetition_time=5.0,
    )
    IfFlagEnabled(0, 11300403)
    RemoveObjectFlag(obj_flag=11300351)
    RemoveObjectFlag(obj_flag=11300352)
    RemoveObjectFlag(obj_flag=11300353)
    RemoveObjectFlag(obj_flag=11300354)
    RemoveObjectFlag(obj_flag=11300355)
    RemoveObjectFlag(obj_flag=11300356)
    RemoveObjectFlag(obj_flag=11300357)
    RemoveObjectFlag(obj_flag=11300358)
    RemoveObjectFlag(obj_flag=11300359)
    RemoveObjectFlag(obj_flag=11300360)
    RemoveObjectFlag(obj_flag=11300361)
    Restart()


@NeverRestart(11300900)
def Event_11300900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300900"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_8_11, animation_id=2)
    EndOfAnimation(obj=arg_4_7, animation_id=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    End()
    EnableNavmeshType(navmesh_id=arg_12_15, navmesh_type=NavmeshType.Solid)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    ForceAnimation(arg_8_11, 1)
    DisableNavmeshType(navmesh_id=arg_12_15, navmesh_type=NavmeshType.Solid)


@NeverRestart(11305030)
def Event_11305030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11305030"""
    SkipLinesIfFlagDisabled(4, arg_0_3)
    DisableObjectActivation(arg_12_15, obj_act_id=3011)
    EndOfAnimation(obj=arg_16_19, animation_id=0)
    EndOfAnimation(obj=arg_12_15, animation_id=2)
    SkipLines(2)
    DisableObjectActivation(arg_12_15, obj_act_id=3012)
    EnableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    SkipLinesIfFinishedConditionTrue(6, condition=2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 3)
    WaitFrames(frames=140)
    EnableObjectActivation(arg_12_15, obj_act_id=3012)
    DisableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 1)
    WaitFrames(frames=140)
    EnableObjectActivation(arg_12_15, obj_act_id=3011)
    EnableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    Restart()


@NeverRestart(11305032)
def Event_11305032(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11305032"""
    IfObjectActivated(1, obj_act_id=arg_0_3)
    IfObjectActivated(2, obj_act_id=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableFlag(arg_8_11)
    Restart()
    EnableFlag(arg_12_15)
    Restart()


@NeverRestart(11305000)
def Event_11305000():
    """Event 11305000"""
    DisableNetworkSync()
    IfSingleplayer(1)
    IfInsideMap(1, game_map=CATACOMBS)
    IfCharacterInsideRegion(1, PLAYER, region=1302700)
    IfFlagDisabled(1, 11310000)
    IfPlayerHasGood(1, 109)
    IfConditionTrue(0, input_condition=1)
    Wait(30.0)
    RestartIfMultiplayer()
    IfCharacterInsideRegion(6, PLAYER, region=1302700)
    RestartIfConditionFalse(6)
    IfHealthLessThanOrEqual(7, PLAYER, value=0.0)
    RestartIfConditionTrue(7)
    EnableFlag(11310050)
    PlayCutscene(130020, cutscene_flags=0, player_id=10000, move_to_region=1312110, game_map=TOMB_OF_THE_GIANTS)
    PlayCutscene(130120, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    EnableObjectActivation(1311300, obj_act_id=-1)
    SetStandbyAnimationSettings(PLAYER)
    Restart()


@RestartOnRest(11305001)
def Event_11305001():
    """Event 11305001"""
    IfCharacterInsideRegion(1, PLAYER, region=1302700)
    IfTimeElapsed(1, seconds=2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305006)
    DisableObjectActivation(1301104, obj_act_id=3060)
    EnableObjectActivation(1301104, obj_act_id=3061)
    RestartEvent(event_id=11305002)
    RestartEvent(event_id=11305009)
    Restart()


@RestartOnRest(11305002)
def Event_11305002():
    """Event 11305002"""
    DisableNetworkSync()
    IfFlagEnabled(0, 11305006)
    DisableFlag(11305006)
    Wait(5.0)
    EnableFlag(11305008)
    Restart()


@NeverRestart(11305003)
def Event_11305003():
    """Event 11305003"""
    IfFlagEnabled(0, 11305008)
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    DisableFlag(11305006)
    DisableFlag(11305008)
    RestartEvent(event_id=11305000)
    RestartEvent(event_id=11305001)
    RestartEvent(event_id=11305002)
    Restart()


@RestartOnRest(11305004)
def Event_11305004():
    """Event 11305004"""
    IfCharacterTargeting(1, targeting_character=1300300, targeted_character=PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 4130)
    IfConditionTrue(0, input_condition=1)
    ClearTargetList(1300300)
    ReplanAI(1300300)
    Restart()


@NeverRestart(11305009)
def Event_11305009():
    """Event 11305009"""
    IfAllPlayersOutsideRegion(1, region=1302700)
    IfEntityWithinDistance(1, entity=1301104, other_entity=PLAYER, radius=10.0)
    IfTimeElapsed(1, seconds=2.0)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    Restart()


@NeverRestart(11300420)
def Event_11300420(_, arg_0_3: int):
    """Event 11300420"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    IfEntityWithinDistance(1, entity=1301104, other_entity=arg_0_3, radius=10.0)
    IfCharacterInsideRegion(1, arg_0_3, region=1302700)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7151, death_animation=6082)
    IfEntityWithinDistance(2, entity=1301104, other_entity=arg_0_3, radius=10.0)
    IfCharacterOutsideRegion(2, arg_0_3, region=1302700)
    IfConditionTrue(0, input_condition=2)
    SetStandbyAnimationSettings(arg_0_3)
    Restart()


@NeverRestart(11300100)
def Event_11300100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300100"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(arg_8_11)
    End()
    IfFlagDisabled(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    DestroyObject(arg_8_11)
    CreateTemporaryVFX(vfx_id=130000, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(arg_8_11, arg_12_15, sound_type=SoundType.o_Object)


@NeverRestart(11300150)
def Event_11300150():
    """Event 11300150"""
    SkipLinesIfThisEventFlagDisabled(2)
    PostDestruction(1301020)
    End()
    DisableAI(1300050)
    IfCharacterInsideRegion(0, PLAYER, region=1302020)
    EnableAI(1300050)
    DestroyObject(1301020)
    PlaySoundEffect(1301020, 303600000, sound_type=SoundType.a_Ambient)


@NeverRestart(11300160)
def Event_11300160():
    """Event 11300160"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1301050)
    End()
    IfObjectDestroyed(0, 1301050)
    EnableFlag(11300160)


@NeverRestart(11300200)
def Event_11300200():
    """Event 11300200"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1301040, animation_id=0)
    End()
    IfFlagEnabled(0, 6)
    ForceAnimation(1301040, 0)


@NeverRestart(11300210)
def Event_11300210():
    """Event 11300210"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableObject(1301030)
    DisableObject(1301031)
    End()
    IfCharacterInsideRegion(1, PLAYER, region=1302030)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(3)
    PlayCutscene(130010, cutscene_flags=0, player_id=10000, move_to_region=1302030, game_map=CATACOMBS)
    WaitFrames(frames=1)
    SkipLines(5)
    SkipLinesIfFlagDisabled(2, 11305060)
    PlayCutscene(130010, cutscene_flags=2, player_id=10000, move_to_region=1302030, game_map=CATACOMBS)
    SkipLines(1)
    PlayCutscene(130010, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1301030)
    DisableObject(1301031)


@NeverRestart(11305060)
def Event_11305060():
    """Event 11305060"""
    EndIfFlagEnabled(11300210)
    DisableNetworkSync()
    DisableFlag(11305060)
    IfCharacterInsideRegion(0, PLAYER, region=1302030)
    EnableFlag(11305060)
    IfCharacterOutsideRegion(0, PLAYER, region=1302030)
    Restart()


@RestartOnRest(11300800)
def Event_11300800():
    """Event 11300800"""
    EnableFlag(11305200)
    EnableFlag(11305040)
    Event_11305050(1, 11305040, 1300100, 1302202, 10.0)
    Event_11305050(2, 11305051, 1300100, 1302203, 10.0)
    Event_11305050(3, 11305052, 1300100, 1302204, 10.0)
    Event_11305050(4, 11305053, 1300100, 1302205, 10.0)
    Event_11300801(0, 1300100)
    Event_11300801(1, 1300120)
    Event_11300801(2, 1300140)
    Event_11300801(3, 1300160)
    Event_11300801(4, 1300180)
    Event_11300801(5, 1300200)
    Event_11305100(0, 1300100, 1300101)
    Event_11305100(1, 1300100, 1300102)
    Event_11305100(2, 1300100, 1300103)
    Event_11305100(3, 1300100, 1300104)
    Event_11305100(4, 1300100, 1300105)
    Event_11305100(5, 1300100, 1300106)
    Event_11305100(6, 1300100, 1300107)
    Event_11305100(7, 1300100, 1300108)
    Event_11305100(8, 1300100, 1300109)
    Event_11305100(9, 1300100, 1300110)
    Event_11305100(10, 1300100, 1300111)
    Event_11305100(11, 1300100, 1300112)
    Event_11305100(12, 1300100, 1300113)
    Event_11305100(13, 1300100, 1300114)
    Event_11305100(14, 1300120, 1300121)
    Event_11305100(15, 1300120, 1300122)
    Event_11305100(16, 1300120, 1300123)
    Event_11305100(17, 1300120, 1300124)
    Event_11305100(18, 1300120, 1300125)
    Event_11305100(19, 1300120, 1300126)
    Event_11305100(20, 1300120, 1300127)
    Event_11305100(21, 1300120, 1300020)
    Event_11305100(22, 1300140, 1300141)
    Event_11305100(23, 1300140, 1300142)
    Event_11305100(24, 1300140, 1300143)
    Event_11305100(25, 1300140, 1300144)
    Event_11305100(26, 1300140, 1300145)
    Event_11305100(27, 1300140, 1300146)
    Event_11305100(28, 1300140, 1300147)
    Event_11305100(29, 1300160, 1300161)
    Event_11305100(30, 1300160, 1300162)
    Event_11305100(31, 1300160, 1300163)
    Event_11305100(32, 1300160, 1300164)
    Event_11305100(33, 1300160, 1300165)
    Event_11305100(34, 1300160, 1300166)
    Event_11305100(35, 1300180, 1300181)
    Event_11305100(36, 1300180, 1300182)
    Event_11305100(37, 1300180, 1300183)
    Event_11305100(38, 1300180, 1300184)
    Event_11305100(39, 1300180, 1300185)
    Event_11305100(40, 1300180, 1300000)
    Event_11305100(41, 1300180, 1300001)
    Event_11305100(44, 1300200, 1300201)
    Event_11305100(45, 1300200, 1300202)
    Event_11305100(46, 1300200, 1300203)
    Event_11305100(47, 1300200, 1300204)
    Event_11305100(48, 1300200, 1300205)
    Event_11305100(49, 1300200, 1300206)
    Event_11305100(50, 1300200, 1300207)
    Event_11305070(0, 1300107, 5.0)
    Event_11305070(1, 1300109, 5.0)
    Event_11305070(2, 1300110, 5.0)
    Event_11305070(3, 1300113, 5.0)
    Event_11305070(4, 1300121, 5.0)
    Event_11305070(5, 1300122, 5.0)
    Event_11305070(6, 1300123, 5.0)
    Event_11305070(7, 1300124, 5.0)
    Event_11305070(8, 1300125, 5.0)
    Event_11305070(9, 1300147, 5.0)
    Event_11305070(10, 1300181, 5.0)
    Event_11305070(11, 1300182, 5.0)
    Event_11305070(12, 1300000, 5.0)
    Event_11305070(13, 1300001, 5.0)
    Event_11305070(16, 1300163, 5.0)
    Event_11305070(17, 1300164, 5.0)
    Event_11305070(18, 1300020, 5.0)
    Event_11305210(0, 1300350)
    Event_11305210(1, 1300351)
    Event_11305210(2, 1300352)
    Event_11305210(3, 1300353)
    Event_11305210(4, 1300354)
    Event_11305210(5, 1300355)
    Event_11305210(6, 1300356)
    Event_11305210(7, 1300357)
    Event_11305210(8, 1300358)
    Event_11305210(9, 1300359)
    Event_11305210(10, 1300360)
    Event_11305210(13, 1300363)


@UnknownRestart(11305050)
def Event_11305050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """Event 11305050"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfEntityWithinDistance(1, entity=arg_4_7, other_entity=PLAYER, radius=arg_12_15)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_4_7, region=arg_8_11)
    AICommand(arg_4_7, command_id=10, slot=0)
    ReplanAI(arg_4_7)
    IfCharacterInsideRegion(0, arg_4_7, region=arg_8_11)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest(11300801)
def Event_11300801(_, arg_0_3: int):
    """Event 11300801"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@UnknownRestart(11305070)
def Event_11305070(_, arg_0_3: int, arg_4_7: float):
    """Event 11305070"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(0, entity=PLAYER, other_entity=arg_0_3, radius=arg_4_7)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9061)


@UnknownRestart(11305100)
def Event_11305100(_, arg_0_3: int, arg_4_7: int):
    """Event 11305100"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    CancelSpecialEffect(arg_4_7, 5451)
    End()
    EnableImmortality(arg_4_7)
    IfCharacterDead(0, arg_0_3)
    CancelSpecialEffect(arg_4_7, 5451)
    DisableImmortality(arg_4_7)


@UnknownRestart(11305210)
def Event_11305210(_, arg_0_3: int):
    """Event 11305210"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=400)
    DisableCharacter(arg_0_3)


@RestartOnRest(11305045)
def Event_11305045():
    """Event 11305045"""
    EndIfThisEventFlagEnabled()
    DisableAI(1300300)
    SetStandbyAnimationSettings(1300300, standby_animation=9000)
    IfEntityWithinDistance(-1, entity=1300300, other_entity=PLAYER, radius=5.0)
    IfAttacked(-1, attacked_entity=1300300, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1300300)
    EnableAI(1300300)


@RestartOnRest(11300850)
def Event_11300850(_, arg_0_3: int, arg_4_7: int):
    """Event 11300850"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


@NeverRestart(11300510)
def Event_11300510(_, arg_0_3: int, arg_4_7: int):
    """Event 11300510"""
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11300520)
def Event_11300520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11300530)
def Event_11300530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300530"""
    IfFlagDisabled(1, 1622)
    IfFlagDisabled(1, 1625)
    IfFlagDisabled(1, 1627)
    IfFlagDisabled(1, 1628)
    IfFlagEnabled(1, 1620)
    IfFlagEnabled(1, 11300593)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11300531)
def Event_11300531(_, arg_0_3: int, arg_4_7: int):
    """Event 11300531"""
    IfFlagEnabled(1, 1620)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.0)
    IfFlagEnabled(2, 1621)
    IfHealthLessThanOrEqual(2, arg_0_3, value=0.0)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventFlagEnabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(1627)
    EnableFlag(arg_4_7)
    EndIfFinishedConditionFalse(input_condition=3)
    DropMandatoryTreasure(arg_0_3)


@NeverRestart(11300533)
def Event_11300533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11300533"""
    IfFlagDisabled(1, 1627)
    IfFlagDisabled(1, 1628)
    IfFlagEnabled(-7, 1620)
    IfFlagEnabled(-7, 1621)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(2, input_condition=1)
    IfFlagEnabled(2, 6)
    IfConditionTrue(3, input_condition=1)
    IfFlagEnabled(3, 1173)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11305025)
def Event_11305025():
    """Event 11305025"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6550, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11305028)
    IfClient(2)
    IfFlagEnabled(2, 11305026)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6550)
    EndIfFlagEnabled(6)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6550)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6550,
        region=1302050,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    IfFlagEnabled(0, 11305026)
    SetNest(6550, region=1302051)


@NeverRestart(11305990)
def Event_11305990(_, arg_0_3: int, arg_4_7: int):
    """Event 11305990"""
    IfFlagEnabled(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagDisabled(0, arg_0_3)
    Restart()


@NeverRestart(11305029)
def Event_11305029():
    """Event 11305029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6550, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11305028)
    IfClient(2)
    IfFlagEnabled(2, 11305026)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6550)
    EndIfFlagEnabled(6)
    If_Unknown_3_24(1, unk1=4, unk2=3)
    IfHost(1)
    IfFlagDisabled(1, 11305026)
    IfFlagDisabled(1, 11305028)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6550)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6550,
        region=1302050,
        summon_flag=11305026,
        dismissal_flag=11305028,
    )
    IfFlagEnabled(0, 11305026)
    SetNest(6550, region=1302051)


@NeverRestart(11305027)
def Event_11305027():
    """Event 11305027"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11305026)
    IfFlagEnabled(1, 11305393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6550, command_id=10, slot=0)
    ReplanAI(6550)
    IfCharacterInsideRegion(0, 6550, region=1302998)
    RotateToFaceEntity(6550, target_entity=1302997)
    ForceAnimation(6550, 7410)
    AICommand(6550, command_id=-1, slot=0)
    ReplanAI(6550)


@RestartOnRest(11305061)
def Event_11305061(_, arg_0_3: int):
    """Event 11305061"""
    EndIfThisEventFlagEnabled()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    WaitFrames(frames=10)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)


@NeverRestart(11300592)
def Event_11300592():
    """Event 11300592"""
    IfHost(1)
    IfFlagEnabled(1, 1620)
    IfFlagDisabled(1, 11300403)
    IfCharacterInsideRegion(1, PLAYER, region=1302000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11300592)
    ActivateObject(1301003, obj_act_id=3011, relative_index=-1)


@NeverRestart(11300593)
def Event_11300593():
    """Event 11300593"""
    IfHost(1)
    IfFlagEnabled(1, 1620)
    IfFlagEnabled(1, 11300592)
    IfFlagEnabled(1, 11300403)
    IfCharacterInsideRegion(1, PLAYER, region=1302001)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11300593)
    ActivateObject(1301003, obj_act_id=3012, relative_index=-1)


@NeverRestart(11305843)
def Event_11305843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11305843"""
    IfHost(1)
    IfMultiplayer(1)
    IfFlagEnabled(1, arg_0_3)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=arg_4_7,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=arg_12_15)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@NeverRestart(11305846)
def Event_11305846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11305846"""
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(vfx_id=arg_8_11)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(arg_4_7)
    DeleteVFX(vfx_id=arg_8_11)
    Restart()
