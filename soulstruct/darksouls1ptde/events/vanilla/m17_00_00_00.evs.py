"""
linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    SkipLinesIfFlagDisabled(1, 14)
    RegisterBonfire(bonfire_flag=11700920, obj=1701950)
    RegisterBonfire(bonfire_flag=11700992, obj=1701960)
    RegisterBonfire(bonfire_flag=11700984, obj=1701961)
    RegisterBonfire(bonfire_flag=11700976, obj=1701962)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=1701140)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=1701141)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=1701142)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701143)
    RegisterStatue(obj=1701900, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701901, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701902, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701903, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701904, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701905, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701906, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(obj=1701907, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    SkipLinesIfClient(5)
    EnableFlag(405)
    DisableObject(1701994)
    DeleteVFX(vfx_id=1701995, erase_root_only=False)
    DisableObject(1701996)
    DeleteVFX(vfx_id=1701997, erase_root_only=False)
    SkipLinesIfFlagDisabled(1, 11700140)
    DisableFlag(405)
    SkipLinesIfClient(9)
    SkipLinesIfFlagDisabled(6, 61700105)
    IfCharacterInsideRegion(1, PLAYER, region=1702410)
    IfCharacterInsideRegion(-1, PLAYER, region=1702402)
    IfCharacterInsideRegion(-1, PLAYER, region=1702403)
    IfConditionTrue(1, input_condition=-1)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(61700105)
    SkipLines(1)
    DisableFlag(61700105)
    SkipLinesIfFlagDisabled(1, 11700002)
    EndOfAnimation(obj=1701410, animation_id=0)
    SkipLinesIfFlagDisabled(1, 61700105)
    ForceAnimation(1701400, 1)
    Event_11700083(0, 1701706, 1701707, 1702606, 1702607)
    Event_11700085()
    Event_11705080()
    Event_11705081()
    Event_11705082()
    Event_11705380()
    Event_11705381()
    Event_11705386()
    Event_11705382()
    Event_11705383()
    Event_11705384()
    Event_11705385()
    Event_11700110()
    Event_11700120(0, 11700120, 1701120, 1701121, 0, 0)
    Event_11700120(5, 11700125, 1701125, 1701126, 1, 1)
    Event_11700160(0, 11700100, 1701100, 11700210, 11700211, 11705090, 11705180, 11705181)
    Event_11700105(0, 11700100, 1701100, 1701101, 1701102, 11705090, 11705180, 11705181)
    Event_11700160(1, 11700102, 1701130, 11700220, 11700221, 11705091, 11705182, 11705183)
    Event_11700105(2, 11700102, 1701130, 1701131, 1701132, 11705091, 11705182, 11705183)
    Event_11700090(0, 11700100, 0, 1701101, 11705090)
    Event_11700090(1, 11700100, 1, 1701102, 11705090)
    Event_11700090(2, 11700102, 0, 1701131, 11705091)
    Event_11700090(3, 11700102, 1, 1701132, 11705091)
    Event_11705150(0, 11700205, 1701200, 1701210)
    Event_11700200(0, 11700205, 1701200, 1701201, 1703200, 1703201, 1703010, 1703011, 11705151)
    Event_11700200(1, 11700205, 1701210, 1701211, 1703210, 1703211, 1703012, 1703013, 11705152)
    Event_11700150(0, 1703100, 1702780)
    Event_11700150(1, 1703101, 1702781)
    Event_11705100()
    Event_11705103()
    Event_11705108()
    Event_11705101()
    Event_11705102()
    Event_11700130()
    RunEvent(11700132, slot=0, args=(0,))
    Event_11700300(0, 11700300, 10010863, 1701500)
    Event_11700300(1, 11700311, 10010879, 1701501)
    Event_11700300(2, 11700302, 10010863, 1701502)
    Event_11700300(3, 11700313, 10010879, 1701503)
    Event_11700300(4, 11700304, 10010863, 1701504)
    Event_11700300(5, 11700305, 10010863, 1701505)
    Event_11700300(6, 11700320, 10010865, 1701506)
    Event_11700140()
    Event_11700141()
    Event_11705170()
    Event_11700700()
    DisableSoundEvent(sound_id=1703800)
    SkipLinesIfFlagDisabled(5, 14)
    Event_11705392()
    DisableObject(1701800)
    DisableObject(1701990)
    DeleteVFX(vfx_id=1701991, erase_root_only=False)
    SkipLines(10)
    Event_11700000()
    Event_11705390()
    Event_11705391()
    Event_11705393()
    Event_11705392()
    Event_11700001()
    Event_11705394()
    Event_11705395()
    Event_11705396()
    Event_11705397()
    Event_11705200()
    Event_11705270(0, 1700250, 15.0)
    Event_11705270(1, 1700251, 15.0)
    Event_11705140(0, 1700102, 1702150)
    Event_11705140(1, 1700103, 1702151)
    Event_11705160(0, 1700350, 3.0)
    Event_11705160(1, 1700351, 3.0)
    Event_11705160(2, 1700352, 10.0)
    Event_11705010(0, 1700400)
    Event_11705020(0, 1700400)
    Event_11705030(0, 1700400)
    Event_11705040(0, 1700400)
    Event_11705050(0, 1700400, 1702010)
    Event_11700900(0, 1700400)
    Event_11705060(0, 1700400)
    Event_11705010(1, 1700401)
    Event_11705020(1, 1700401)
    Event_11705030(1, 1700401)
    Event_11705040(1, 1700401)
    Event_11705050(1, 1700401, 1702011)
    Event_11700900(1, 1700401)
    Event_11705060(1, 1700401)
    Event_11700810(0, 6610, 0, 0)
    Event_11700810(1, 1700450, 1, 33001000)
    Event_11700810(2, 1700451, 1, 33001000)
    Event_11700810(3, 1700452, 1, 33001000)
    Event_11700810(4, 1700453, 1, 33001000)
    Event_11700810(5, 1700190, 0, 0)
    Event_11700810(6, 1700191, 0, 0)
    Event_11700810(10, 1700501, 0, 0)
    Event_11700810(11, 1700502, 0, 0)
    Event_11700810(12, 1700150, 0, 0)
    Event_11700810(13, 1700151, 0, 0)
    Event_11705280(0, 1700350)
    Event_11705280(1, 1700351)
    Event_11700600(1, 1701651, 11700601)
    Event_11700600(2, 1701652, 11700602)
    Event_11700600(3, 1701653, 11700603)
    Event_11700600(4, 1701654, 11700604)
    Event_11700600(5, 1701655, 11700605)
    Event_11700600(6, 1701656, 11700606)
    Event_11700600(7, 1701657, 11700607)
    Event_11700600(8, 1701658, 11700608)
    Event_11700600(9, 1701659, 11700609)
    Event_11700600(10, 1701660, 11700610)
    Event_11700600(11, 1701661, 11700611)
    Event_11700600(12, 1701662, 11700612)
    Event_11700600(13, 1701663, 11700613)
    Event_11700600(14, 1701664, 11700614)
    Event_11700600(15, 1701665, 11700615)
    Event_11700600(16, 1701666, 11700616)
    Event_11705110(0, 1700110)
    Event_11705110(1, 1700111)
    Event_11705110(2, 1700112)
    Event_11705110(3, 1700113)
    Event_11705110(4, 1700114)
    Event_11705110(5, 1700115)
    Event_11705110(6, 1700116)
    Event_11705110(7, 1700117)
    Event_11705110(8, 1700118)
    Event_11705110(9, 1700119)
    Event_11705110(10, 1700120)
    Event_11705110(11, 1700121)
    Event_11705110(12, 1700122)
    Event_11705110(13, 1700123)
    Event_11705110(14, 1700124)
    Event_11705110(15, 1700125)
    Event_11705110(16, 1700126)
    Event_11705110(17, 1700127)
    Event_11705110(18, 1700908)
    Event_11705110(19, 1700909)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6610, event_flag=8988)
    HumanityRegistration(6032, event_flag=8334)
    HumanityRegistration(6033, event_flag=8334)
    SkipLinesIfFlagRangeAnyEnabled(1, (1093, 1096))
    DisableCharacter(6032)
    SkipLinesIfFlagEnabled(1, 1099)
    DisableCharacter(6033)
    SetTeamTypeAndExitStandbyAnimation(6033, team_type=TeamType.HostileAlly)
    SkipLinesIfFlagDisabled(1, 11700594)
    Move(6032, destination=1702501, destination_type=CoordEntityType.Region, set_draw_parent=1703300)
    Event_11700510(0, 6032, 1096)
    Event_11700520(0, 6032, 1090, 1109, 1097)
    Event_11700520(1, 6033, 1090, 1109, 1097)
    Event_11700530(0, 6032, 1090, 1109, 1093)
    Event_11700531(0, 6032, 1090, 1109, 1094)
    Event_11700532(0, 6032, 1090, 1109, 1095)
    Event_11700533(0, 6032, 1090, 1109, 1099, 6033)
    HumanityRegistration(6291, event_flag=8454)
    SkipLinesIfFlagEnabled(2, 1547)
    SkipLinesIfFlagEnabled(1, 1542)
    DisableCharacter(6291)
    Event_11700510(2, 6291, 1547)
    Event_11700520(2, 6291, 1540, 1569, 1548)
    Event_11700538(0, 6291, 1540, 1569, 1541)
    Event_11700539(0, 6291, 1540, 1569, 1542)
    Event_11700540(0, 6291, 1540, 1569, 1543)
    SetTeamTypeAndExitStandbyAnimation(6073, team_type=TeamType.HostileAlly)
    SkipLinesIfFlagEnabled(1, 1181)
    DisableCharacter(6073)
    Event_11700520(3, 6073, 1170, 1189, 1177)
    Event_11700545(0, 6073, 1170, 1189, 1181)


@NeverRestart(11700080)
def Event_11700080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700080"""
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
    IfFlagEnabled(3, 11700080)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11700080)
    SkipLinesIfFinishedConditionTrue(5, condition=3)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteVFX(vfx_id=arg_4_7)


@NeverRestart(11700083)
def Event_11700083(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700083"""
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


@RestartOnRest(11705080)
def Event_11705080():
    """Event 11705080"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1700900)
    DisableCharacter(1700901)
    DisableCharacter(1700902)
    DisableCharacter(1700903)
    DisableCharacter(1700904)
    DisableCharacter(1700905)
    DisableCharacter(1700906)
    DisableCharacter(1700907)
    DisableCharacter(1700908)
    DisableCharacter(1700909)
    IfFlagEnabled(0, 11700050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1700900)
    EnableCharacter(1700901)
    EnableCharacter(1700902)
    EnableCharacter(1700903)
    EnableCharacter(1700904)
    EnableCharacter(1700905)
    EnableCharacter(1700906)
    EnableCharacter(1700907)
    EnableCharacter(1700908)
    EnableCharacter(1700909)


@RestartOnRest(11705081)
def Event_11705081():
    """Event 11705081"""
    IfFlagEnabled(-1, 11705085)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11700050)
    DisableFlag(11705085)
    EnableFlag(5001)
    Kill(1700900)
    Kill(1700901)
    Kill(1700902)
    Kill(1700903)
    Kill(1700904)
    Kill(1700905)
    Kill(1700906)
    Kill(1700907)
    Kill(1700908)
    Kill(1700909)


@RestartOnRest(11705082)
def Event_11705082():
    """Event 11705082"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11700050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11700050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11700050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11700050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11700050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DUKES_ARCHIVES)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11700050)
    RestartIfConditionFalse(-6)
    EnableFlag(11700050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DUKES_ARCHIVES)
    RestartIfConditionFalse(7)
    DisableFlag(11700050)
    EnableFlag(11705085)


@NeverRestart(11700085)
def Event_11700085():
    """Event 11700085"""
    SkipLinesIfFlagDisabled(4, 11800100)
    EnableFlag(11700086)
    DisableObject(1701710)
    DeleteVFX(vfx_id=1701711, erase_root_only=False)
    End()
    SkipLinesIfFlagDisabled(3, 11700086)
    DisableObject(1701710)
    DeleteVFX(vfx_id=1701711, erase_root_only=False)
    End()
    EndIfClient()
    IfActionButton(
        0,
        prompt_text=10010410,
        anchor_entity=1702610,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=1701710,
    )
    DisplayStatus(10010630)
    Restart()


@RestartOnRest(11700000)
def Event_11700000():
    """Event 11700000"""
    EndIfThisEventFlagEnabled()
    DisableObject(1701990)
    DeleteVFX(vfx_id=1701991, erase_root_only=False)
    DisableCharacter(1700800)
    EnableObjectInvulnerability(1701800)
    IfThisEventFlagDisabled(1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1702999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)
    EnableFlag(11705390)
    EnableFlag(11705391)
    EnableFlag(11705393)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagEnabled(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170000, cutscene_flags=0, player_id=10000, move_to_region=1702801, game_map=DUKES_ARCHIVES)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(170000, cutscene_flags=2, player_id=10000, move_to_region=1702801, game_map=DUKES_ARCHIVES)
    SkipLines(1)
    PlayCutscene(170000, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableObjectInvulnerability(1701800)
    EnableObject(1701990)
    CreateVFX(vfx_id=1701991)
    Move(1700800, destination=1702800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1700800)


@NeverRestart(11705380)
def Event_11705380():
    """Event 11705380"""
    IfFlagDisabled(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1701890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11705381)
def Event_11705381():
    """Event 11705381"""
    IfFlagDisabled(1, 11700000)
    IfFlagEnabled(1, 11705386)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1702898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1702897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11705386)
def Event_11705386():
    """Event 11705386"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11700000)
    IfCharacterInsideRegion(1, PLAYER, region=1702896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700700)


@NeverRestart(11705382)
def Event_11705382():
    """Event 11705382"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010404,
        anchor_entity=1702895,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1702894)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    DisableBossHealthBar(1700700, name=5290)
    Restart()


@RestartOnRest(11705383)
def Event_11705383():
    """Event 11705383"""
    DisableAI(1700700)
    IfFlagDisabled(1, 11700000)
    IfFlagEnabled(1, 11705386)
    IfCharacterInsideRegion(1, PLAYER, region=1702890)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1700700)
    EnableBossHealthBar(1700700, name=5290)
    IfAllPlayersOutsideRegion(0, region=1702890)
    Restart()


@NeverRestart(11705384)
def Event_11705384():
    """Event 11705384"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=1703801)
    IfFlagDisabled(1, 11700000)
    IfFlagEnabled(1, 11705386)
    IfCharacterInsideRegion(1, PLAYER, region=1702890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1703801)
    IfFlagEnabled(-1, 11700000)
    IfCharacterOutsideRegion(-1, PLAYER, region=1702890)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest(11705385)
def Event_11705385():
    """Event 11705385"""
    EnableImmortality(1700700)
    AddSpecialEffect(1700700, 5441)
    AddSpecialEffect(1700700, 5442)
    AddSpecialEffect(1700700, 5443)
    IfFlagEnabled(0, 11700000)
    DisableCharacter(1700700)
    DisableObject(1701050)
    DisableObject(1701890)
    DeleteVFX(vfx_id=1701891)


@NeverRestart(11705390)
def Event_11705390():
    """Event 11705390"""
    IfFlagDisabled(1, 14)
    IfFlagEnabled(1, 11700000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1701990,
    )
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    RotateToFaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    ActivateMultiplayerBuffs(1700800)
    Restart()


@NeverRestart(11705391)
def Event_11705391():
    """Event 11705391"""
    IfFlagDisabled(1, 14)
    IfFlagEnabled(1, 11705393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfCharacterAlive(1, 1700800)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1702998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1701990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1702997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11705393)
def Event_11705393():
    """Event 11705393"""
    SkipLinesIfThisEventFlagEnabled(8)
    IfFlagEnabled(1, 11700000)
    IfFlagDisabled(1, 14)
    IfCharacterInsideRegion(1, PLAYER, region=1702996)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1700800)


@RestartOnRest(11705392)
def Event_11705392():
    """Event 11705392"""
    SkipLinesIfFlagDisabled(5, 14)
    DisableCharacter(1700800)
    Kill(1700800)
    DisableCharacter(1700801)
    Kill(1700801)
    End()
    DisableAI(1700800)
    IfFlagEnabled(1, 11705393)
    IfCharacterInsideRegion(1, PLAYER, region=1702990)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1700800)
    EnableBossHealthBar(1700800, name=5290)


@NeverRestart(11700001)
def Event_11700001():
    """Event 11700001"""
    DisableObject(1701950)
    IfCharacterDead(0, 1700800)
    EnableFlag(14)
    KillBoss(game_area_param_id=1700800)
    SkipLinesIfClient(1)
    AwardAchievement(achievement_id=38)
    DisableObject(1701990)
    DeleteVFX(vfx_id=1701991)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1701950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1701950)
    RegisterBonfire(bonfire_flag=11700920, obj=1701950)


@NeverRestart(11705394)
def Event_11705394():
    """Event 11705394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 14)
    IfFlagEnabled(1, 11705392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11705391)
    IfCharacterInsideRegion(1, PLAYER, region=1702990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1703800)


@NeverRestart(11705395)
def Event_11705395():
    """Event 11705395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 14)
    IfFlagEnabled(1, 11705394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1703800)


@RestartOnRest(11705396)
def Event_11705396():
    """Event 11705396"""
    AddSpecialEffect(1700800, 5440)
    AddSpecialEffect(1700800, 5441)
    AddSpecialEffect(1700800, 5442)
    AddSpecialEffect(1700800, 5443)
    EnableImmortality(1700800)
    CreateObjectVFX(vfx_id=1701800, obj=100, model_point=170004)
    IfObjectDestroyed(0, 1701800)
    DeleteObjectVFX(1703100)
    ForceAnimation(1700800, 7000)
    IfCharacterHasTAEEvent(0, 1700800, tae_event_id=500)
    CancelSpecialEffect(1700800, 5440)
    CancelSpecialEffect(1700800, 5441)
    CancelSpecialEffect(1700800, 5442)
    CancelSpecialEffect(1700800, 5443)
    DisableImmortality(1700800)


@RestartOnRest(11705397)
def Event_11705397():
    """Event 11705397"""
    DisableCharacter(1700801)
    EndIfFlagEnabled(14)
    SkipLinesIfThisEventFlagDisabled(4)
    SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1700800, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1700800)
    CreateNPCPart(1700800, npc_part_id=5290, part_index=NPCPartType.Part1, part_health=330)
    IfHealthGreaterThan(1, 1700800, value=0.0)
    IfCharacterPartHealthComparison(1, 1700800, npc_part_id=5290, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, 1700800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(1700800, 8000)
    IfCharacterHasTAEEvent(0, 1700800, tae_event_id=400)
    Move(
        1700801,
        destination=1700800,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=1700800,
    )
    EnableCharacter(1700801)
    SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
    ForceAnimation(1700801, 8100)
    AICommand(1700800, command_id=20, slot=0)
    ReplanAI(1700800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52910000, host_only=True)


@NeverRestart(11700160)
def Event_11700160(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11700160"""
    IfFlagDisabled(1, arg_16_19)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfObjectActivated(2, obj_act_id=arg_8_11)
    IfObjectActivated(3, obj_act_id=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionTrue(2, condition=3)
    SkipLinesIfFinishedConditionTrue(9, condition=2)
    SkipLinesIfFlagEnabled(8, arg_0_3)
    SkipLinesIfFinishedConditionFalse(4, condition=1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 0)
    WaitFrames(frames=105)
    EnableFlag(arg_20_23)
    IfFlagDisabled(0, arg_16_19)
    Restart()
    SkipLinesIfFinishedConditionFalse(4, condition=1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 2)
    WaitFrames(frames=105)
    EnableFlag(arg_24_27)
    IfFlagDisabled(0, arg_16_19)
    Restart()


@NeverRestart(11700105)
def Event_11700105(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """Event 11700105"""
    SkipLinesIfFlagDisabled(4, arg_0_3)
    EndOfAnimation(obj=arg_4_7, animation_id=11)
    EnableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLines(2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EnableObjectActivation(arg_12_15, obj_act_id=-1)
    IfHost(1)
    IfFlagEnabled(1, arg_20_23)
    IfHost(2)
    IfFlagEnabled(2, arg_24_27)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_20_23)
    DisableFlag(arg_24_27)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 1)
    WaitFrames(frames=300)
    DisableFlag(arg_16_19)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 3)
    WaitFrames(frames=344)
    DisableFlag(arg_16_19)
    Restart()


@NeverRestart(11700090)
def Event_11700090(_, arg_0_3: int, arg_4_4: uchar, arg_8_11: int, arg_12_15: int):
    """Event 11700090"""
    DisableNetworkSync()
    IfFlagState(1, arg_4_4, FlagType.Absolute, arg_0_3)
    IfFlagDisabled(1, arg_12_15)
    IfActionButton(
        1,
        prompt_text=10010501,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=195,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010170, anchor_entity=arg_8_11)
    Restart()


@NeverRestart(11705150)
def Event_11705150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11705150"""
    IfActionButton(
        1,
        prompt_text=10010503,
        anchor_entity=arg_4_7,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfActionButton(
        2,
        prompt_text=10010503,
        anchor_entity=arg_8_11,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(7, condition=1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagEnabled(2, arg_0_3)
    ForceAnimation(arg_4_7, 0)
    SkipLines(1)
    ForceAnimation(arg_4_7, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    SkipLinesIfFinishedConditionFalse(7, condition=2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagEnabled(2, arg_0_3)
    ForceAnimation(arg_8_11, 0)
    SkipLines(1)
    ForceAnimation(arg_8_11, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(frames=105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    IfFlagDisabled(3, 11705151)
    IfFlagDisabled(3, 11705152)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(11700200)
def Event_11700200(
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
    """Event 11700200"""
    DisableObject(arg_8_11)
    SkipLinesIfFlagEnabled(5, arg_0_3)
    EndOfAnimation(obj=arg_4_7, animation_id=3)
    DisableMapCollision(collision=arg_16_19)
    DisableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=arg_24_27, navmesh_type=NavmeshType.Solid)
    SkipLines(4)
    EndOfAnimation(obj=arg_4_7, animation_id=1)
    DisableMapCollision(collision=arg_12_15)
    EnableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=arg_24_27, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, arg_28_31)
    SkipLinesIfFlagEnabled(11, arg_0_3)
    ForceAnimation(arg_4_7, 1)
    DisableMapCollision(collision=arg_12_15)
    EnableObject(arg_8_11)
    EnableNavmeshType(navmesh_id=arg_20_23, navmesh_type=NavmeshType.Solid)
    ForceAnimation(arg_8_11, 1)
    WaitFrames(frames=180)
    DisableObject(arg_8_11)
    EnableMapCollision(collision=arg_16_19)
    EnableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()
    ForceAnimation(arg_4_7, 3)
    DisableMapCollision(collision=arg_16_19)
    EnableObject(arg_8_11)
    EnableNavmeshType(navmesh_id=arg_24_27, navmesh_type=NavmeshType.Solid)
    ForceAnimation(arg_8_11, 3)
    WaitFrames(frames=180)
    DisableObject(arg_8_11)
    EnableMapCollision(collision=arg_12_15)
    DisableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()


@NeverRestart(11700110)
def Event_11700110():
    """Event 11700110"""
    SkipLinesIfThisEventFlagDisabled(5)
    DisableObjectActivation(1701111, obj_act_id=-1)
    EndOfAnimation(obj=1701110, animation_id=0)
    DisableObject(1701109)
    DisableMapCollision(collision=1703220)
    End()
    DisableObject(1701109)
    DisableMapCollision(collision=1703221)
    IfObjectActivated(0, obj_act_id=11700110)
    DisableMapCollision(collision=1703220)
    EnableObject(1701109)
    ForceAnimation(1701110, 0)
    ForceAnimation(1701109, 0, wait_for_completion=True)
    DisableObject(1701109)
    EnableMapCollision(collision=1703221)


@NeverRestart(11700120)
def Event_11700120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11700120"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EndOfAnimation(obj=arg_4_7, animation_id=arg_12_15)
    End()
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfFlagEnabled(-1, 11700140)
    IfObjectActivated(-1, obj_act_id=arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15)


@NeverRestart(11700150)
def Event_11700150(_, arg_0_3: int, arg_4_7: int):
    """Event 11700150"""
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    EnableMapCollision(collision=arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    DisableMapCollision(collision=arg_0_3)
    Restart()


@NeverRestart(11705100)
def Event_11705100():
    """Event 11705100"""
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=1702890)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(respawn_point=1702900)
    SaveRequest()


@NeverRestart(11705101)
def Event_11705101():
    """Event 11705101"""
    IfHost(1)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 51700990)
    IfFlagDisabled(1, 11705101)
    IfFlagDisabled(1, 11700133)
    IfCharacterInsideRegion(1, PLAYER, region=1702100)
    IfHost(2)
    IfFlagEnabled(2, 11705106)
    IfHost(3)
    IfFlagEnabled(3, 11705107)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFlagEnabled(9, 11700002)
    SkipLinesIfFinishedConditionFalse(8, condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(170010, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(170010, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    ForceAnimation(1701410, 0)
    EnableFlag(11700002)
    EnableFlag(61700105)
    SkipLinesIfFinishedConditionTrue(1, condition=1)
    SkipLinesIfFinishedConditionTrue(9, condition=3)
    SkipLinesIfFlagEnabled(2, 61700105)
    Event_11705108()
    Restart()
    EnableSoundEvent(sound_id=1703500)
    ForceAnimation(1701400, 0)
    WaitFrames(frames=150)
    ForceAnimation(1701400, 1)
    Event_11705108()
    Restart()
    SkipLinesIfFlagDisabled(2, 61700105)
    Event_11705108()
    Restart()
    DisableSoundEvent(sound_id=1703500)
    EnableFlag(11700133)
    ForceAnimation(1701400, 2)
    WaitFrames(frames=50)
    Event_11705108()
    Restart()


@NeverRestart(11705102)
def Event_11705102():
    """Event 11705102"""
    DisableNetworkSync()
    SkipLinesIfFlagEnabled(1, 61700105)
    DisableSoundEvent(sound_id=1703500)


@NeverRestart(11705103)
def Event_11705103():
    """Event 11705103"""
    IfFlagEnabled(1, 61700105)
    IfObjectActivated(1, obj_act_id=11705105)
    IfFlagDisabled(2, 61700105)
    IfObjectActivated(2, obj_act_id=11705105)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11705106)
    DisableFlag(11705107)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableFlag(11705106)
    Restart()
    EnableFlag(11705107)
    Restart()


@NeverRestart(11705108)
def Event_11705108():
    """Event 11705108"""
    DisableNetworkSync()
    IfFramesElapsed(1, frames=10)
    IfInsideMap(1, game_map=DUKES_ARCHIVES)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1701401, obj_act_id=-1)


@RestartOnRest(11705110)
def Event_11705110(_, arg_0_3: int):
    """Event 11705110"""
    IfFlagEnabled(1, 61700105)
    IfCharacterInsideRegion(-7, PLAYER, region=1702100)
    IfCharacterInsideRegion(-7, PLAYER, region=1702101)
    IfConditionTrue(1, input_condition=-7)
    IfFlagEnabled(2, 61700105)
    IfAllPlayersOutsideRegion(2, region=1702100)
    IfAllPlayersOutsideRegion(2, region=1702101)
    IfFlagDisabled(3, 61700105)
    IfFlagEnabled(3, 11700002)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(8, condition=1)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfAllPlayersOutsideRegion(7, region=1702100)
    IfAllPlayersOutsideRegion(7, region=1702101)
    IfConditionTrue(-2, input_condition=7)
    IfFlagDisabled(-2, 61700105)
    IfConditionTrue(0, input_condition=-2)
    Restart()
    SkipLinesIfFinishedConditionFalse(7, condition=2)
    AICommand(arg_0_3, command_id=2, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-3, PLAYER, region=1702100)
    IfCharacterInsideRegion(-3, PLAYER, region=1702101)
    IfFlagDisabled(-3, 61700105)
    IfConditionTrue(0, input_condition=-3)
    Restart()
    AICommand(arg_0_3, command_id=3, slot=0)
    ReplanAI(arg_0_3)
    IfFlagEnabled(0, 61700105)
    Restart()


@RestartOnRest(11700130)
def Event_11700130():
    """Event 11700130"""
    EndIfClient()
    SkipLinesIfFlagDisabled(3, 51700990)
    DisableCharacter(1700100)
    Kill(1700100)
    End()
    DisableCharacterCollision(1700100)
    DisableGravity(1700100)


@RestartOnRest(11705140)
def Event_11705140(_, arg_0_3: int, arg_4_7: int):
    """Event 11705140"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, 11705101)
    SetNest(arg_0_3, region=arg_4_7)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfThisEventSlotFlagEnabled(-1)
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    ClearTargetList(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@NeverRestart(11700140)
def Event_11700140():
    """Event 11700140"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1701300, animation_id=0)
    End()
    IfPlayerHasGood(1, 2005)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
    )
    IfFlagEnabled(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(405)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=1701300, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1701300, 0)
    EndIfClient()
    DisplayDialog(text=10010864, anchor_entity=1701300, button_type=ButtonType.Yes_or_No)
    End()


@NeverRestart(11700141)
def Event_11700141():
    """Event 11700141"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11700140)
    IfPlayerDoesNotHaveGood(1, 2005)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(2, 11700140)
    IfActionButton(
        2,
        prompt_text=10010400,
        anchor_entity=1701300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010163, anchor_entity=1701300)
    Restart()


@RestartOnRest(11705170)
def Event_11705170():
    """Event 11705170"""
    DisableNetworkSync()
    EndIfClient()
    DisableFlag(11705170)
    IfCharacterInsideRegion(0, PLAYER, region=1702402)
    EnableFlag(11705170)
    IfCharacterOutsideRegion(0, PLAYER, region=1702402)
    Restart()


@RestartOnRest(11705160)
def Event_11705160(_, arg_0_3: int, arg_4_7: float):
    """Event 11705160"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(0, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=13000)


@RestartOnRest(11705250)
def Event_11705250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11705250"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, attacked_entity=arg_4_7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableAI(arg_4_7)


@RestartOnRest(11705270)
def Event_11705270(_, arg_0_3: int, arg_4_7: float):
    """Event 11705270"""
    EndIfThisEventSlotFlagEnabled()
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    IfEntityWithinDistance(-1, entity=arg_0_3, other_entity=PLAYER, radius=arg_4_7)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@NeverRestart(11700300)
def Event_11700300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11700300"""
    EndIfClient()
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisplayDialog(text=arg_4_7, anchor_entity=arg_8_11, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11705200)
def Event_11705200():
    """Event 11705200"""
    Event_11705240(0, 1700900)
    Event_11705240(1, 1700901)
    Event_11705240(2, 1700902)
    Event_11705240(3, 1700903)
    Event_11705201(0, 11705200, 1700300, 1702301, 11705202)
    Event_11705201(1, 11705201, 1700300, 1702306, 11705202)
    Event_11705201(2, 11705202, 1700300, 1702305, 11705202)
    EnableFlag(11705210)
    Event_11705201(10, 11705210, 1700301, 1702311, 11705213)
    Event_11705201(11, 11705211, 1700301, 1702312, 11705213)
    Event_11705201(12, 11705212, 1700301, 1702313, 11705213)
    Event_11705201(13, 11705213, 1700301, 1702314, 11705213)
    EnableFlag(11705220)
    Event_11705201(20, 11705220, 1700302, 1702321, 11705221)
    Event_11705201(21, 11705221, 1700302, 1702322, 11705221)


@RestartOnRest(11705240)
def Event_11705240(_, arg_0_3: int):
    """Event 11705240"""
    DisableNetworkSync()
    IfCharacterBackreadEnabled(0, arg_0_3)
    AICommand(arg_0_3, command_id=1, slot=0)


@UnknownRestart(11705201)
def Event_11705201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11705201"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHasTAEEvent(1, arg_4_7, tae_event_id=1000)
    IfConditionTrue(0, input_condition=1)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    SetNest(arg_4_7, region=arg_8_11)
    ForceAnimation(arg_4_7, 7000, wait_for_completion=True)
    SkipLinesIfFlagDisabled(1, arg_12_15)
    AICommand(arg_4_7, command_id=1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest(11700810)
def Event_11700810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11700810"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    SkipLinesIfEqual(4, left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)
    End()


@RestartOnRest(11705280)
def Event_11705280(_, arg_0_3: int):
    """Event 11705280"""
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(32300100, host_only=True)


@NeverRestart(11700600)
def Event_11700600(_, arg_0_3: int, arg_4_7: int):
    """Event 11700600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@RestartOnRest(11705010)
def Event_11705010(_, arg_0_3: int):
    """Event 11705010"""
    IfCharacterAlive(1, arg_0_3)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=arg_0_3,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    Restart()


@RestartOnRest(11705020)
def Event_11705020(_, arg_0_3: int):
    """Event 11705020"""
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 5420)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    IfCharacterBackreadDisabled(7, arg_0_3)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, arg_0_3, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, arg_0_3, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(arg_0_3, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, arg_0_3, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(arg_0_3, 3006, wait_for_completion=True)
    ReplanAI(arg_0_3)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    Restart()


@RestartOnRest(11705030)
def Event_11705030(_, arg_0_3: int):
    """Event 11705030"""
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterHasSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(arg_0_3, command_id=200, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(arg_0_3, command_id=210, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11705040)
def Event_11705040(_, arg_0_3: int):
    """Event 11705040"""
    IfCharacterHasSpecialEffect(1, arg_0_3, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(arg_0_3, command_id=201, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(arg_0_3, command_id=211, slot=0)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11705050)
def Event_11705050(_, arg_0_3: int, arg_4_7: int):
    """Event 11705050"""
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, 5421)
    ClearTargetList(arg_0_3)
    ReplanAI(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Restart()


@RestartOnRest(11700900)
def Event_11700900(_, arg_0_3: int):
    """Event 11700900"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest(11705060)
def Event_11705060(_, arg_0_3: int):
    """Event 11705060"""
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


@RestartOnRest(11700700)
def Event_11700700():
    """Event 11700700"""
    IfCharacterAlive(0, 1700510)
    EndIfFlagEnabled(11700700)
    IfDLCOwned(1)
    IfCharacterDead(1, 1700510)
    IfFlagEnabled(1, 11200530)
    IfFlagDisabled(1, 1121)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(27100200, host_only=True)


@NeverRestart(11700510)
def Event_11700510(_, arg_0_3: int, arg_4_7: int):
    """Event 11700510"""
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


@NeverRestart(11700520)
def Event_11700520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11700530)
def Event_11700530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700530"""
    IfFlagDisabled(1, 1096)
    IfFlagEnabled(1, 1092)
    IfCharacterInsideRegion(1, PLAYER, region=1702410)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11020694)
    EnableCharacter(arg_0_3)
    DisableFlag(61700320)
    EndOfAnimation(obj=1701506, animation_id=1)
    EnableObjectActivation(1701506, obj_act_id=27401, relative_index=0)
    EnableObjectActivation(1701506, obj_act_id=27401, relative_index=1)
    DisableObjectActivation(1701506, obj_act_id=27401, relative_index=2)
    DisableObjectActivation(1701506, obj_act_id=27401, relative_index=3)


@NeverRestart(11700531)
def Event_11700531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700531"""
    IfFlagDisabled(1, 1096)
    IfFlagEnabled(1, 1093)
    IfFlagEnabled(1, 61700320)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11700594)


@NeverRestart(11700532)
def Event_11700532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700532"""
    IfFlagDisabled(1, 1096)
    IfFlagEnabled(1, 1094)
    IfHost(1)
    IfCharacterOutsideRegion(1, PLAYER, region=1702410)
    IfFlagDisabled(2, 1096)
    IfFlagEnabled(2, 1093)
    IfFlagEnabled(2, 14)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11700594)
    EnableCharacter(arg_0_3)
    Move(arg_0_3, destination=1702501, destination_type=CoordEntityType.Region, set_draw_parent=1703300)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, region=1702501)


@NeverRestart(11700533)
def Event_11700533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """Event 11700533"""
    SkipLinesIfFlagEnabled(2, 11700595)
    DisableObject(1701664)
    DisableObjectActivation(1701664, obj_act_id=-1)
    IfFlagDisabled(1, 1096)
    IfThisEventFlagDisabled(1)
    IfFlagEnabled(1, 1095)
    IfFlagEnabled(1, 14)
    IfFlagEnabled(1, 728)
    IfFlagEnabled(1, 11700592)
    IfFlagDisabled(2, 1096)
    IfFlagEnabled(2, 1095)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(arg_16_19)
    EnableFlag(11700595)


@NeverRestart(11700538)
def Event_11700538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700538"""
    DisableCharacter(1700500)
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1540)
    IfFlagDisabled(1, 1512)
    IfFlagDisabled(1, 1513)
    IfFlagRangeAnyEnabled(1, flag_range=(1501, 1511))
    IfCharacterAlive(1, arg_0_3)
    IfFlagEnabled(2, 1541)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(1700500)
    SetDisplayMask(1700500, bit_index=1, switch_type=OnOffChange.Off)


@NeverRestart(11700539)
def Event_11700539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700539"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1541)
    IfCharacterDead(1, 1700500)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(
        arg_0_3,
        destination=1700500,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=1700500,
    )
    EnableCharacter(arg_0_3)


@NeverRestart(11700540)
def Event_11700540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700540"""
    IfFlagDisabled(1, 1547)
    IfFlagEnabled(1, 1542)
    IfFlagEnabled(1, 11700593)
    IfThisEventFlagDisabled(1)
    IfHost(2)
    IfFlagDisabled(2, 1547)
    IfFlagEnabled(2, 1542)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


@NeverRestart(11700545)
def Event_11700545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11700545"""
    IfFlagDisabled(1, 1176)
    IfFlagDisabled(1, 1179)
    IfFlagEnabled(1, 1175)
    IfFlagEnabled(1, 724)
    IfFlagEnabled(2, 1181)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
