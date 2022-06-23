"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=11200984, obj=1201961)
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=1201140)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=1201141)
    CreateProjectileOwner(entity=1200090)
    SkipLinesIfFlagEnabled(2, 11200000)
    SkipLinesIfFlagEnabled(1, 11200002)
    SkipLines(1)
    DisableObject(1201200)
    SkipLinesIfClient(10)
    DisableObject(1201994)
    DeleteVFX(vfx_id=1201995, erase_root_only=False)
    DisableObject(1201996)
    DeleteVFX(vfx_id=1201997, erase_root_only=False)
    DisableObject(1201998)
    DeleteVFX(vfx_id=1201999, erase_root_only=False)
    DisableObject(1201988)
    DeleteVFX(vfx_id=1201989, erase_root_only=False)
    DisableObject(1201986)
    DeleteVFX(vfx_id=1201987, erase_root_only=False)
    Event_11200090(0, 1201700, 1201701, 1202600, 1202601)
    Event_11205080()
    Event_11205081()
    Event_11205082()
    Event_11200100(0, 11200110, 1201000, 120020, 1202500, 0, 61200500)
    Event_11200110(0, 11200100, 1201000, 1202500, 0)
    Event_11200100(1, 11200111, 1201010, 120021, 1202501, 1, 61200501)
    Event_11200110(1, 11200101, 1201010, 1202501, 1)
    Event_11200120()
    Event_11205000()
    Event_11200800()
    Event_11200200()
    Event_11200690()
    Event_11200600(0, 1201650, 11200600)
    Event_11200600(1, 1201651, 11200601)
    DisableSoundEvent(sound_id=1203800)
    SkipLinesIfFlagDisabled(4, 5)
    Event_11205392()
    DisableObject(1201990)
    DeleteVFX(vfx_id=1201991, erase_root_only=False)
    SkipLines(9)
    Event_11200000()
    Event_11205390()
    Event_11205391()
    Event_11205393()
    Event_11205392()
    Event_11200001()
    Event_11205394()
    Event_11205395()
    Event_11205396()
    Event_11200002()
    DisableSoundEvent(sound_id=1203801)
    SkipLinesIfFlagDisabled(6, 11200900)
    Event_11205382()
    DisableObject(1201890)
    DeleteVFX(vfx_id=1201891, erase_root_only=False)
    DisableObject(1201892)
    DeleteVFX(vfx_id=1201893, erase_root_only=False)
    SkipLines(17)
    Event_11205380()
    Event_11205381()
    Event_11205383()
    Event_11205382()
    Event_11200900()
    Event_11205384()
    Event_11205385()
    Event_11205120(0, 1202220, 1202180)
    Event_11205120(1, 1202221, 1202181)
    Event_11205120(2, 1202222, 1202182)
    Event_11205120(3, 1202223, 1202183)
    Event_11205120(4, 1202224, 1202184)
    Event_11205120(5, 1202225, 1202185)
    Event_11205120(6, 1202226, 1202186)
    Event_11205120(7, 1202227, 1202187)
    Event_11205120(8, 1202228, 1202188)
    Event_11205120(9, 1202229, 1202189)
    Event_11200801()
    Event_11205300(0, 1, 3530, 3530, 1200011, 91, 0, 1, 5430)
    Event_11205300(1, 2, 3531, 3531, 1200012, 92, 1, 2, 5431)
    Event_11205300(2, 3, 3532, 3532, 1200013, 93, 2, 3, 5432)
    Event_11205300(3, 4, 3533, 3533, 1200014, 94, 3, 4, 5433)
    Event_11205300(4, 5, 3534, 3534, 1200015, 95, 4, 5, 5434)
    Event_11205300(5, 6, 3535, 3535, 1200016, 96, 5, 6, 5435)
    Event_11205300(6, 8, 3536, 3536, 1200017, 97, 6, 7, 5436)
    Event_11205250(0, 1200100, 1202110)
    Event_11205290(0, 1200101, 51200170, 0.0, 1)
    Event_11205290(1, 1200102, 51200170, 0.20000000298023224, 1)
    Event_11205290(2, 1200103, 51200170, 0.800000011920929, 1)
    Event_11205250(1, 1200104, 1202111)
    Event_11205290(3, 1200105, 11205263, 0.0, 0)
    Event_11205290(4, 1200106, 11205263, 0.6000000238418579, 0)
    Event_11205290(5, 1200107, 11205264, 0.0, 0)
    Event_11205290(6, 1200108, 11205264, 0.8999999761581421, 0)
    Event_11205200(0, 1200109, 8.0)
    Event_11205200(1, 1200110, 8.0)
    Event_11205200(2, 1200111, 5.0)
    Event_11205200(3, 1200112, 5.0)
    Event_11205200(4, 1200113, 5.0)
    Event_11205230(0, 1200600, 3.0)
    Event_11205230(2, 1200602, 3.0)
    Event_11205240(0, 1200600, 1202710)
    Event_11205240(2, 1200602, 1202712)
    Event_11205280(0, 1200650, 6.0, 1202112)
    Event_11205280(1, 1200651, 2.0, 1202112)
    Event_11205260(0, 1200652, 6.0)
    Event_11205260(1, 1200653, 10.0)
    Event_11205260(2, 1200654, 8.0)
    Event_11205260(3, 1200655, 4.0)
    Event_11205260(4, 1200656, 4.0)
    Event_11205190(0, 1200250, 1202113, 0.0)
    Event_11205190(1, 1200251, 1202113, 0.5)
    Event_11205190(2, 1200252, 1202113, 1.2000000476837158)
    Event_11205190(3, 1200253, 1202113, 0.699999988079071)
    Event_11205150(0, 1200705)
    Event_11205150(1, 1200706)
    Event_11205150(2, 1200707)
    Event_11205150(3, 1200708)
    Event_11205150(4, 1200709)
    Event_11205150(5, 1200710)
    Event_11205150(6, 1200711)
    Event_11205150(7, 1200712)
    Event_11205180(0, 1200350, 1)
    Event_11205180(1, 1200351, 0)
    Event_11205180(2, 1200352, 0)
    Event_11200810(0, 1200000, 0, 0)
    Event_11200810(1, 1200001, 0, 0)
    Event_11200810(2, 1200400, 0, 33004000)
    Event_11200810(3, 1200350, 0, 0)
    Event_11200810(4, 1200351, 0, 0)
    Event_11200810(5, 1200352, 0, 0)
    Event_11200810(6, 1200750, 0, 27901000)
    Event_11200810(7, 1200301, 0, 0)
    Event_11200810(8, 1200304, 1, 0)
    Event_11200810(9, 1200306, 0, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6521, event_flag=8932)
    Event_11205030()
    Event_11205032()
    Event_11200300()
    SkipLinesIfClient(2)
    DisableFlagRange((11200210, 11200213))
    DisableFlag(11200215)
    HumanityRegistration(6050, event_flag=8350)
    HumanityRegistration(6051, event_flag=8350)
    SkipLinesIfClient(6)
    SkipLinesIfFlagDisabled(2, 1123)
    DisableFlagRange((1120, 1139))
    EnableFlag(1122)
    SkipLinesIfFlagDisabled(2, 1130)
    DisableFlagRange((1120, 1139))
    EnableFlag(1129)
    SkipLinesIfFlagEnabled(1, 1121)
    DisableCharacter(6050)
    SkipLinesIfFlagEnabled(1, 1123)
    DisableCharacter(6051)
    SkipLinesIfFlagEnabled(1, 1130)
    DisableCharacter(6051)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    Event_11200520(0, 6050, 1120, 1139, 1125)
    Event_11200520(1, 6051, 1120, 1139, 1125)
    Event_11200530(0, 6050, 1120, 1139, 1121)
    Event_11200531(0, 6050, 1120, 1139, 1122)
    Event_11200534(0, 6050, 1120, 1139, 1123)
    Event_11200532(0, 6050, 1120, 1139, 1126)
    Event_11200533()
    Event_11205040(0, 11200210, 1202000, 1203100)
    Event_11205040(1, 11200211, 1202001, 1203101)
    Event_11205040(2, 11200212, 1202002, 1203102)
    Event_11205040(3, 11200213, 1202003, 1203103)
    Event_11200529(0, 1120, 1139, 1127)
    Event_11200527(0, 6050, 1120, 1139, 1129)
    Event_11200525(0, 6050, 1120, 1139, 1130)
    Event_11205070(0, 11200210, 1202000, 1203100)
    Event_11205070(1, 11200211, 1202001, 1203101)
    Event_11205070(2, 11200212, 1202002, 1203102)
    Event_11205070(3, 11200213, 1202003, 1203103)
    DeleteVFX(vfx_id=1202009, erase_root_only=False)
    Event_11200005()
    Event_11200006()
    SkipLinesIfClient(1)
    DisableFlagRange((11205050, 11205068))
    DisableCharacterCollision(6380)
    DisableGravity(6380)
    EnableImmortality(6380)
    SkipLinesIfFlagEnabled(2, 1710)
    SkipLinesIfFlagEnabled(1, 1712)
    DisableCharacter(6380)
    Event_11200538(0, 6380, 1710, 1712, 1711)
    Event_11200539(0, 6380, 1710, 1712, 1712)
    Event_11200540(0, 6380, 1710, 1712, 1711)
    Event_11205058()
    Event_11205054()
    Event_11205056()
    Event_11205057()
    Event_11205060(0, 6310)
    Event_11205060(1, 6420)
    Event_11205060(2, 1200300)
    Event_11205060(3, 1200301)
    Event_11205060(4, 1200302)
    Event_11205060(5, 1200303)
    Event_11205060(6, 1200304)
    Event_11205060(7, 1200305)
    Event_11205060(8, 1200306)
    HumanityRegistration(6310, event_flag=8470)
    HumanityRegistration(6420, event_flag=8900)
    DisableCharacter(6310)
    DisableCharacter(6420)
    Event_11200520(2, 6310, 1600, 1619, 1604)
    Event_11200520(3, 6420, 1760, 1769, 1764)
    Event_11200501(0, 6310, 1603)
    Event_11200535(0, 6310)


@NeverRestart(11200090)
def Event_11200090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200090"""
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


@RestartOnRest(11205080)
def Event_11205080():
    """Event 11205080"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1200900)
    DisableCharacter(1200901)
    DisableCharacter(1200902)
    DisableCharacter(1200903)
    DisableCharacter(1200904)
    DisableCharacter(1200905)
    DisableCharacter(1200906)
    DisableCharacter(1200907)
    DisableCharacter(1200908)
    DisableCharacter(1200909)
    IfFlagEnabled(0, 11200050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1200900)
    EnableCharacter(1200901)
    EnableCharacter(1200902)
    EnableCharacter(1200903)
    EnableCharacter(1200904)
    EnableCharacter(1200905)
    EnableCharacter(1200906)
    EnableCharacter(1200907)
    EnableCharacter(1200908)
    EnableCharacter(1200909)


@RestartOnRest(11205081)
def Event_11205081():
    """Event 11205081"""
    IfFlagEnabled(-1, 11205085)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11200050)
    DisableFlag(11205085)
    EnableFlag(5001)
    Kill(1200900)
    Kill(1200901)
    Kill(1200902)
    Kill(1200903)
    Kill(1200904)
    Kill(1200905)
    Kill(1200906)
    Kill(1200907)
    Kill(1200908)
    Kill(1200909)


@RestartOnRest(11205082)
def Event_11205082():
    """Event 11205082"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11200050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11200050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11200050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11200050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11200050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11200050)
    RestartIfConditionFalse(-6)
    EnableFlag(11200050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DARKROOT_GARDEN)
    RestartIfConditionFalse(7)
    DisableFlag(11200050)
    EnableFlag(11205085)


@RestartOnRest(11200000)
def Event_11200000():
    """Event 11200000"""
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(11200002)
    DisableCharacter(1200800)
    DisableObject(1201990)
    DeleteVFX(vfx_id=1201991, erase_root_only=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=1202999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagEnabled(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120000, cutscene_flags=0, player_id=10000, move_to_region=1202801, move_to_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120000, cutscene_flags=2, player_id=10000, move_to_region=1202801, move_to_map=DARKROOT_GARDEN)
    SkipLines(1)
    PlayCutscene(120000, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1201200)
    Move(1200800, destination=1202800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateVFX(vfx_id=1201991)
    EnableFlag(11200002)


@NeverRestart(11200002)
def Event_11200002():
    """Event 11200002"""
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(11200000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=1202999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagEnabled(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120003, cutscene_flags=0, player_id=10000, move_to_region=1202802, move_to_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120003, cutscene_flags=2, player_id=10000, move_to_region=1202802, move_to_map=DARKROOT_GARDEN)
    SkipLines(1)
    PlayCutscene(120003, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1201200)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateVFX(vfx_id=1201991)
    EnableFlag(11200000)


@NeverRestart(11205390)
def Event_11205390():
    """Event 11205390"""
    IfFlagDisabled(1, 5)
    IfFlagEnabled(1, 11200000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1201990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11205391)
def Event_11205391():
    """Event 11205391"""
    IfFlagDisabled(1, 5)
    IfFlagEnabled(1, 11205393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11205393)
def Event_11205393():
    """Event 11205393"""
    SkipLinesIfThisEventFlagEnabled(8)
    IfFlagEnabled(1, 11200000)
    IfFlagDisabled(1, 5)
    IfCharacterInsideRegion(1, PLAYER, region=1202996)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)


@RestartOnRest(11205392)
def Event_11205392():
    """Event 11205392"""
    SkipLinesIfFlagDisabled(3, 5)
    DisableCharacter(1200800)
    Kill(1200800)
    End()
    DisableAI(1200800)
    IfFlagEnabled(1, 11200000)
    IfFlagEnabled(1, 11205393)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1200800)
    EnableBossHealthBar(1200800, name=5210, slot=0)


@NeverRestart(11200001)
def Event_11200001():
    """Event 11200001"""
    IfCharacterDead(0, 1200800)
    EnableFlag(5)
    KillBoss(game_area_param_id=1200800)
    DisableObject(1201990)
    DeleteVFX(vfx_id=1201991)


@NeverRestart(11205394)
def Event_11205394():
    """Event 11205394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 5)
    IfFlagEnabled(1, 11205392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11205391)
    IfCharacterInsideRegion(1, PLAYER, region=1202990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1203800)


@NeverRestart(11205395)
def Event_11205395():
    """Event 11205395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 5)
    IfFlagEnabled(1, 11205394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1203800)


@RestartOnRest(11205396)
def Event_11205396():
    """Event 11205396"""
    SkipLinesIfThisEventFlagEnabled(1)
    IfHealthLessThanOrEqual(0, 1200800, value=0.10000000149011612)
    AddSpecialEffect(1200800, 5401)


@NeverRestart(11205380)
def Event_11205380():
    """Event 11205380"""
    IfFlagDisabled(1, 11200900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1201890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11205381)
def Event_11205381():
    """Event 11205381"""
    IfFlagDisabled(1, 11200900)
    IfFlagEnabled(1, 11205383)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11205383)
def Event_11205383():
    """Event 11205383"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11200900)
    IfCharacterInsideRegion(1, PLAYER, region=1202896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    AddSpecialEffect(PLAYER, 5500)
    ActivateMultiplayerBuffs(1200801)


@RestartOnRest(11205382)
def Event_11205382():
    """Event 11205382"""
    DisableCharacter(1200090)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1200801, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagDisabled(3, 11200900)
    DisableCharacter(1200801)
    Kill(1200801)
    End()
    DisableHealthBar(1200801)
    DisableAI(1200801)
    SetStandbyAnimationSettings(1200801, standby_animation=7000)
    IfFlagEnabled(0, 11205383)
    SetStandbyAnimationSettings(1200801, cancel_animation=7001)
    EnableAI(1200801)
    EnableBossHealthBar(1200801, name=3230, slot=0)


@NeverRestart(11200900)
def Event_11200900():
    """Event 11200900"""
    IfCharacterDead(0, 1200801)
    CancelSpecialEffect(PLAYER, 5500)
    EnableFlag(11200900)
    KillBoss(game_area_param_id=1200801)
    DisableObject(1201890)
    DeleteVFX(vfx_id=1201891)
    DisableObject(1201892)
    DeleteVFX(vfx_id=1201893)


@NeverRestart(11205384)
def Event_11205384():
    """Event 11205384"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11200900)
    IfFlagEnabled(1, 11205382)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11205381)
    IfCharacterInsideRegion(1, PLAYER, region=1202890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1203801)


@NeverRestart(11205385)
def Event_11205385():
    """Event 11205385"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11200900)
    IfFlagEnabled(1, 11205384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1203801)


@NeverRestart(11205120)
def Event_11205120(_, arg_0_3: int, arg_4_7: int):
    """Event 11205120"""
    IfCharacterInsideRegion(1, 1200801, region=arg_0_3)
    IfCharacterHasTAEEvent(1, 1200801, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(1200801, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterDoesNotHaveTAEEvent(0, 1200801, tae_event_id=10)
    Restart()


@NeverRestart(11200100)
def Event_11200100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11200100"""
    SkipLinesIfFlagEnabled(1, arg_20_23)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EndOfAnimation(obj=arg_4_7, animation_id=1)
    End()
    CreateObjectVFX(vfx_id=arg_4_7, obj=200, model_point=arg_8_11)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    IfPlayerHasGood(1, 2002)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_12_15,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=arg_4_7,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_20_23)
    RotateToFaceEntity(PLAYER, target_entity=arg_4_7)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    SkipLinesIfClient(1)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisplayDialog(text=10010861, anchor_entity=arg_4_7, button_type=ButtonType.Yes_or_No)
    ForceAnimation(arg_4_7, 1)
    DeleteObjectVFX(arg_4_7)


@NeverRestart(11200110)
def Event_11200110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200110"""
    DisableNetworkSync()
    IfFlagEnabled(-1, arg_0_3)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfFlagEnabled(1, 703)
    SkipLinesIfEqual(1, left=arg_12_15, right=1)
    IfPlayerDoesNotHaveGood(1, 2002)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=arg_4_7,
    )
    IfClient(2)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=arg_4_7,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(arg_0_3)
    DisplayDialog(text=10010160, anchor_entity=arg_4_7, button_type=ButtonType.Yes_or_No)
    Restart()


@NeverRestart(11200120)
def Event_11200120():
    """Event 11200120"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1201300)
    End()
    IfObjectDestroyed(0, 1201300)
    EnableFlag(11200120)


@RestartOnRest(11205150)
def Event_11205150(_, arg_0_3: int):
    """Event 11205150"""
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.800000011920929)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest(11205180)
def Event_11205180(_, arg_0_3: int, arg_4_7: int):
    """Event 11205180"""
    SkipLinesIfEqual(3, left=arg_4_7, right=0)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    SetNest(arg_0_3, region=1202732)
    End()
    SkipLinesIfThisEventSlotFlagEnabled(6)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    DisableAI(arg_0_3)
    IfHealthLessThanOrEqual(0, 1200350, value=0.4000000059604645)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, region=1202732)


@RestartOnRest(11205190)
def Event_11205190(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """Event 11205190"""
    EndIfThisEventSlotFlagEnabled()
    DisableGravity(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    EnableGravity(arg_0_3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 7000, wait_for_completion=True)
    EnableAI(arg_0_3)


@RestartOnRest(11205200)
def Event_11205200(_, arg_0_3: int, arg_4_7: float):
    """Event 11205200"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=6521)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest(11205250)
def Event_11205250(_, arg_0_3: int, arg_4_7: int):
    """Event 11205250"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=6521)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, 6521, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest(11205290)
def Event_11205290(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """Event 11205290"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=6521)
    SkipLinesIfEqual(1, left=0, right=arg_12_15)
    SkipLinesIfClient(1)
    IfFlagEnabled(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest(11205230)
def Event_11205230(_, arg_0_3: int, arg_4_7: float):
    """Event 11205230"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=6521, radius=arg_4_7)
    IfAttacked(-2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfAttacked(-2, attacked_entity=arg_0_3, attacker=6521)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    EndIfFinishedConditionTrue(input_condition=2)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9063)


@RestartOnRest(11205240)
def Event_11205240(_, arg_0_3: int, arg_4_7: int):
    """Event 11205240"""
    IfCharacterHasSpecialEffect(0, arg_0_3, 5110)
    SetNest(arg_0_3, region=arg_4_7)


@RestartOnRest(11205260)
def Event_11205260(_, arg_0_3: int, arg_4_7: float):
    """Event 11205260"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=6521, radius=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest(11205280)
def Event_11205280(_, arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """Event 11205280"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=6521, radius=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, 6521, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest(11205000)
def Event_11205000():
    """Event 11205000"""
    DisableGravity(1200000)
    DisableCharacterCollision(1200000)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(0, PLAYER, region=1202100)
    EnableGravity(1200000)
    EnableCharacterCollision(1200000)
    SetNest(1200000, region=1202101)


@RestartOnRest(11200800)
def Event_11200800():
    """Event 11200800"""
    DisableCharacter(1200200)
    EndIfThisEventFlagEnabled()
    SkipLinesIfFlagEnabled(1, 11200801)
    IfFlagEnabled(0, 703)
    EnableCharacter(1200200)
    IfCharacterBackreadEnabled(0, 1200200)
    SetDisplayMask(1200200, bit_index=0, switch_type=OnOffChange.Off)
    IfCharacterDead(0, 1200200)
    EnableFlag(11200800)


@RestartOnRest(11200801)
def Event_11200801():
    """Event 11200801"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1200010)
    End()
    IfCharacterDead(-1, 1200010)
    IfCharacterDead(1, 1200011)
    IfCharacterDead(1, 1200012)
    IfCharacterDead(1, 1200013)
    IfCharacterDead(1, 1200014)
    IfCharacterDead(1, 1200015)
    IfCharacterDead(1, 1200016)
    IfCharacterDead(1, 1200017)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Kill(1200010, award_souls=True)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(35300100, host_only=True)


@RestartOnRest(11205300)
def Event_11205300(
    _,
    arg_0_1: short,
    arg_2_3: short,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_16: uchar,
    arg_17_17: uchar,
    arg_20_23: int,
):
    """Event 11205300"""
    DisableCharacter(arg_8_11)
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(1200010, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1200010, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1200010, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, 1200010)
    CreateNPCPart(1200010, npc_part_id=arg_2_3, part_index=arg_0_1, part_health=176)
    IfCharacterPartHealthComparison(1, 1200010, npc_part_id=arg_4_7, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, 1200010, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(1200010)
    Move(
        arg_8_11,
        destination=1200010,
        destination_type=CoordEntityType.Character,
        model_point=arg_12_15,
        copy_draw_parent=1200010,
    )
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(1200010, 8000)
    SetDisplayMask(1200010, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1200010, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1200010, arg_20_23)


@NeverRestart(11200200)
def Event_11200200():
    """Event 11200200"""
    DisableNetworkSync()
    EndIfClient()
    IfHost(1)
    IfPlayerCovenant(2, Covenant.ForestHunter)
    IfConditionFalse(1, input_condition=2)
    IfStandingOnCollision(-1, 1203500)
    IfStandingOnCollision(-1, 1203501)
    IfStandingOnCollision(-1, 1203502)
    IfStandingOnCollision(-1, 1203503)
    IfStandingOnCollision(-1, 1203504)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4500)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11200810)
def Event_11200810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11200810"""
    SkipLinesIfThisEventSlotFlagDisabled(6)
    SkipLinesIfEqual(3, left=arg_4_7, right=1)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    DropMandatoryTreasure(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_8_11, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)


@NeverRestart(11200600)
def Event_11200600(_, arg_0_3: int, arg_4_7: int):
    """Event 11200600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@NeverRestart(11200690)
def Event_11200690():
    """Event 11200690"""
    SkipLinesIfThisEventFlagEnabled(6)
    DisableTreasure(obj=1201600)
    DisableObject(1201600)
    IfFlagEnabled(-1, 1123)
    IfFlagEnabled(-1, 1130)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(1201600)
    EnableTreasure(obj=1201600)


@NeverRestart(11200510)
def Event_11200510(_, arg_0_3: int, arg_4_7: int):
    """Event 11200510"""
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


@NeverRestart(11200520)
def Event_11200520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11200501)
def Event_11200501(_, arg_0_3: int, arg_4_7: int):
    """Event 11200501"""
    IfFlagDisabled(1, 1603)
    IfFlagEnabled(1, 1600)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfThisEventFlagDisabled(1)
    IfFlagDisabled(2, 1763)
    IfFlagEnabled(2, 1760)
    IfHealthLessThanOrEqual(2, 6420, value=0.8999999761581421)
    IfHealthGreaterThan(2, 6420, value=0.0)
    IfAttacked(2, attacked_entity=6420, attacker=PLAYER)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(3, 746)
    IfThisEventFlagDisabled(3)
    IfFlagEnabled(-2, arg_4_7)
    IfFlagEnabled(-2, 1763)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventFlagEnabled(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=4)
    SkipLinesIfFlagEnabled(1, 1604)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagEnabled(1, 1764)
    EnableFlag(1763)
    SkipLinesIfFlagEnabled(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagEnabled(1, 1764)
    EnableCharacter(6420)
    SetTeamType(arg_0_3, TeamType.Enemy)
    SetTeamType(6420, TeamType.Enemy)
    SaveRequest()
    EnableFlag(1766)


@NeverRestart(11200530)
def Event_11200530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200530"""
    IfFlagEnabled(1, 1120)
    IfFlagEnabled(1, 11200800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=1200200,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=1200200,
    )
    EnableCharacter(arg_0_3)
    Wait(0.5)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7875)
    ForceAnimation(arg_0_3, 7876)


@NeverRestart(11200531)
def Event_11200531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200531"""
    IfFlagEnabled(1, 1121)
    IfFlagEnabled(1, 11200590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


@NeverRestart(11200532)
def Event_11200532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200532"""
    IfFlagEnabled(1, 1121)
    IfFlagEnabled(1, 11200591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


@NeverRestart(11200533)
def Event_11200533():
    """Event 11200533"""
    DeleteVFX(vfx_id=1203100, erase_root_only=False)
    DeleteVFX(vfx_id=1203101, erase_root_only=False)
    DeleteVFX(vfx_id=1203102, erase_root_only=False)
    DeleteVFX(vfx_id=1203103, erase_root_only=False)
    EndIfClient()
    IfPlayerDoesNotHaveGood(1, 2520)
    IfFlagEnabled(1, 1122)
    IfFlagEnabled(2, 1129)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableRandomFlagInRange(flag_range=(11200210, 11200213))
    SkipLinesIfFlagDisabled(1, 11200210)
    CreateVFX(vfx_id=1203100)
    SkipLinesIfFlagDisabled(1, 11200211)
    CreateVFX(vfx_id=1203101)
    SkipLinesIfFlagDisabled(1, 11200212)
    CreateVFX(vfx_id=1203102)
    SkipLinesIfFlagDisabled(1, 11200213)
    CreateVFX(vfx_id=1203103)


@NeverRestart(11205040)
def Event_11205040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11205040"""
    SkipLinesIfFlagDisabled(2, 11200215)
    EnableCharacter(6051)
    End()
    IfFlagEnabled(1, 1122)
    IfFlagEnabled(1, arg_0_3)
    IfActionButton(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteVFX(vfx_id=arg_8_11)
    Move(6051, destination=arg_4_7, destination_type=CoordEntityType.Region, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205310)


@NeverRestart(11200534)
def Event_11200534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200534"""
    IfFlagEnabled(1, 1122)
    IfFlagEnabled(1, 11205310)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11200529)
def Event_11200529(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11200529"""
    EndIfFlagEnabled(17)
    IfFlagEnabled(-1, 1122)
    IfFlagEnabled(-1, 1125)
    IfFlagEnabled(-1, 1126)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(2, 1125)
    SkipLinesIfFlagEnabled(1, 1126)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


@NeverRestart(11200527)
def Event_11200527(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200527"""
    IfFlagEnabled(0, 1128)
    SkipLinesIfFlagEnabled(5, 1125)
    SkipLinesIfFlagEnabled(8, 1126)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(1125)
    DisableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(1126)
    DisableCharacter(arg_0_3)


@NeverRestart(11205070)
def Event_11205070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11205070"""
    SkipLinesIfFlagDisabled(2, 11200215)
    EnableCharacter(6051)
    End()
    IfFlagEnabled(1, 1129)
    IfFlagEnabled(1, arg_0_3)
    IfActionButton(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteVFX(vfx_id=arg_8_11)
    Move(6051, destination=arg_4_7, destination_type=CoordEntityType.Region, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205311)


@NeverRestart(11200525)
def Event_11200525(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200525"""
    IfFlagEnabled(1, 1129)
    IfFlagEnabled(1, 11205311)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11200535)
def Event_11200535(_, arg_0_3: int):
    """Event 11200535"""
    SkipLinesIfClient(1)
    DisableFlag(11205021)
    SkipLinesIfHost(1)
    SkipLinesIfFlagEnabled(5, 11205021)
    IfFlagDisabled(1, 1603)
    IfFlagDisabled(1, 1601)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagEnabled(2, 1764)
    EnableCharacter(6420)
    EnableFlag(1766)
    EnableFlag(11205021)


@NeverRestart(11200538)
def Event_11200538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200538"""
    IfAttacked(0, attacked_entity=arg_0_3, attacker=PLAYER)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 9030, wait_for_completion=True)
    DisableCharacter(arg_0_3)


@NeverRestart(11200539)
def Event_11200539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200539"""
    IfFlagEnabled(1, 1710)
    IfFlagEnabled(1, 746)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11200540)
def Event_11200540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11200540"""
    IfFlagEnabled(1, 1712)
    IfFlagEnabled(1, 11200596)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7003, wait_for_completion=True)
    DisableCharacter(arg_0_3)


@NeverRestart(11205054)
def Event_11205054():
    """Event 11205054"""
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagDisabled(1, 11205055)
    IfFlagEnabled(1, 11205053)
    IfConditionTrue(1, input_condition=-7)
    IfConditionFalse(1, input_condition=7)
    IfFlagDisabled(1, 11205050)
    IfFlagDisabled(2, 11205055)
    IfFlagEnabled(2, 11205053)
    IfConditionTrue(2, input_condition=-7)
    IfConditionTrue(2, input_condition=7)
    IfAttacked(-6, attacked_entity=6380, attacker=PLAYER)
    IfFlagEnabled(-6, 11205060)
    IfFlagEnabled(-6, 11205061)
    IfFlagEnabled(-6, 11205062)
    IfFlagEnabled(-6, 11205063)
    IfFlagEnabled(-6, 11205064)
    IfFlagEnabled(-6, 11205065)
    IfFlagEnabled(-6, 11205066)
    IfFlagEnabled(-6, 11205067)
    IfFlagEnabled(-6, 11205068)
    IfFlagEnabled(-6, 745)
    IfConditionTrue(2, input_condition=-6)
    IfFlagDisabled(3, 11205055)
    IfFlagDisabled(3, 11205053)
    IfConditionTrue(3, input_condition=-7)
    IfConditionFalse(3, input_condition=7)
    IfFlagEnabled(3, 11205050)
    IfFlagDisabled(4, 11205055)
    IfFlagDisabled(4, 11205053)
    IfConditionTrue(4, input_condition=-7)
    IfConditionTrue(4, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11205055)
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    EnableFlag(11205052)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    EnableFlag(11205052)
    Restart()


@RestartOnRest(11205056)
def Event_11205056():
    """Event 11205056"""
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagEnabled(1, 11205051)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(1, input_condition=7)
    IfFlagEnabled(2, 11205051)
    IfConditionTrue(2, input_condition=-7)
    IfConditionFalse(2, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11205051)
    DisableFlag(11205053)
    SkipLinesIfFinishedConditionTrue(9, condition=2)
    IfCharacterHuman(-6, PLAYER)
    IfCharacterHollow(-6, PLAYER)
    SkipLinesIfConditionFalse(3, -6)
    BetrayCurrentCovenant()
    SkipLinesIfFlagEnabled(2, 9001)
    IncrementPvPSin()
    EnableFlag(9001)
    EnableFlag(742)
    EnableFlag(746)
    SetTeamType(6310, TeamType.Enemy)
    SetTeamType(6420, TeamType.Enemy)
    SetTeamType(1200300, TeamType.Enemy)
    SetTeamType(1200301, TeamType.Enemy)
    SetTeamType(1200302, TeamType.Enemy)
    SetTeamType(1200303, TeamType.Enemy)
    SetTeamType(1200304, TeamType.Enemy)
    SetTeamType(1200305, TeamType.Enemy)
    SetTeamType(1200306, TeamType.Enemy)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


@RestartOnRest(11205057)
def Event_11205057():
    """Event 11205057"""
    IfFlagEnabled(0, 11205052)
    DisableFlag(11205052)
    EnableFlag(11205053)
    SetTeamType(6310, TeamType.Ally)
    SetTeamType(6420, TeamType.Ally)
    SetTeamType(1200300, TeamType.Ally)
    SetTeamType(1200301, TeamType.Ally)
    SetTeamType(1200302, TeamType.Ally)
    SetTeamType(1200303, TeamType.Ally)
    SetTeamType(1200304, TeamType.Ally)
    SetTeamType(1200305, TeamType.Ally)
    SetTeamType(1200306, TeamType.Ally)
    ClearTargetList(6310)
    ClearTargetList(6420)
    ClearTargetList(1200300)
    ClearTargetList(1200301)
    ClearTargetList(1200302)
    ClearTargetList(1200303)
    ClearTargetList(1200304)
    ClearTargetList(1200305)
    ClearTargetList(1200306)
    ReplanAI(6310)
    ReplanAI(6420)
    ReplanAI(1200300)
    ReplanAI(1200301)
    ReplanAI(1200302)
    ReplanAI(1200303)
    ReplanAI(1200304)
    ReplanAI(1200305)
    ReplanAI(1200306)
    SaveRequest()
    DisableFlag(11205055)
    Restart()


@NeverRestart(11205058)
def Event_11205058():
    """Event 11205058"""
    SkipLinesIfFlagDisabled(2, 11205053)
    EnableFlag(11205052)
    End()
    SetTeamType(6310, TeamType.Enemy)
    SetTeamType(6420, TeamType.Enemy)
    SetTeamType(1200300, TeamType.Enemy)
    SetTeamType(1200301, TeamType.Enemy)
    SetTeamType(1200302, TeamType.Enemy)
    SetTeamType(1200303, TeamType.Enemy)
    SetTeamType(1200304, TeamType.Enemy)
    SetTeamType(1200305, TeamType.Enemy)
    SetTeamType(1200306, TeamType.Enemy)
    SaveRequest()


@RestartOnRest(11205060)
def Event_11205060(_, arg_0_3: int):
    """Event 11205060"""
    SkipLinesIfFlagDisabled(1, 746)
    SetTeamType(arg_0_3, TeamType.Enemy)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfConditionTrue(0, input_condition=1)
    End()


@NeverRestart(11205030)
def Event_11205030():
    """Event 11205030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6521, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11205033)
    IfClient(2)
    IfFlagEnabled(2, 11205031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6521)
    EndIfFlagEnabled(11200900)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6521)
    IfEntityWithinDistance(1, entity=6521, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6521,
        region=1202010,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


@NeverRestart(11205032)
def Event_11205032():
    """Event 11205032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11205031)
    IfFlagEnabled(1, 11205383)
    IfConditionTrue(0, input_condition=1)
    AICommand(6521, command_id=10, slot=0)
    ReplanAI(6521)
    IfCharacterInsideRegion(0, 6521, region=1202898)
    RotateToFaceEntity(6521, target_entity=1202894)
    ForceAnimation(6521, 7410)
    AICommand(6521, command_id=-1, slot=0)
    ReplanAI(6521)


@NeverRestart(11200300)
def Event_11200300():
    """Event 11200300"""
    IfFlagEnabled(0, 11205031)
    EnableFlag(11200300)


@NeverRestart(11200005)
def Event_11200005():
    """Event 11200005"""
    IfFlagEnabled(-1, 1125)
    IfFlagEnabled(-1, 1126)
    IfFlagEnabled(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520)
    IfFlagDisabled(1, 17)
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    IfSingleplayer(0)
    CreateVFX(vfx_id=1202009)
    IfMultiplayer(0)
    DeleteVFX(vfx_id=1202009)
    Restart()


@NeverRestart(11200006)
def Event_11200006():
    """Event 11200006"""
    IfFlagEnabled(-1, 1125)
    IfFlagEnabled(-1, 1126)
    IfFlagEnabled(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520)
    IfFlagDisabled(1, 17)
    IfSingleplayer(1)
    IfActionButton(1, prompt_text=10010100, anchor_entity=1202008, anchor_type=CoordEntityType.Region)
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    PlayCutscene(120002, cutscene_flags=0, player_id=10000, move_to_region=1212510, move_to_map=OOLACILE)
    WaitFrames(frames=1)
    SaveRequest()
    Restart()
