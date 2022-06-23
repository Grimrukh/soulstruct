"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    SkipLinesIfFlagDisabled(1, 12)
    RegisterBonfire(bonfire_flag=11510920, obj=1511950)
    RegisterBonfire(bonfire_flag=11510992, obj=1511960, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11510984, obj=1511961)
    RegisterBonfire(bonfire_flag=11510976, obj=1511962)
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=1511140)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=1511141)
    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(1511994)
    DeleteVFX(vfx_id=1511995, erase_root_only=False)
    DisableObject(1511310)
    DisableMapCollision(collision=1513301)
    DisableMapCollision(collision=1513302)
    DisableMapCollision(collision=1513303)
    SkipLinesIfFlagDisabled(1, 11510300)
    SkipLinesIfFlagDisabled(6, 11510303)
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=53)
    EnableMapCollision(collision=1513303)
    SkipLines(13)
    SkipLinesIfFlagDisabled(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=50)
    EnableMapCollision(collision=1513302)
    SkipLines(6)
    SkipLinesIfFlagDisabled(5, 11510301)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=51)
    EnableMapCollision(collision=1513301)
    DisableObject(1511450)
    DisableFlag(11510460)
    Event_11510090(0, 1511700, 1511701, 1512600, 1512601)
    Event_11510090(1, 1511702, 1511703, 1512602, 1512603)
    Event_11515040()
    Event_11515041()
    Event_11515042()
    Event_11510200()
    Event_11510201()
    Event_11510100()
    Event_11510210()
    Event_11510211()
    Event_11510220()
    Event_11510300()
    Event_11510319()
    Event_11510340()
    Event_11510350()
    Event_11510310()
    Event_11515250()
    Event_11515251()
    Event_11510110()
    Event_11510400()
    Event_11510401()
    Event_11510230()
    Event_11510240()
    Event_11515050()
    Event_11510120()
    Event_11510130()
    Event_11510131()
    Event_11510460()
    Event_11510462()
    Event_11510461()
    Event_11510140()
    Event_11510150()
    Event_151()
    Event_11510215()
    Event_11515060(0, 1510400)
    Event_11515060(1, 1510401)
    Event_11515060(2, 1510402)
    Event_11515060(3, 1510403)
    Event_11515060(4, 1510404)
    Event_11515060(5, 1510405)
    Event_11515060(6, 1510406)
    Event_11515060(7, 1510407)
    Event_11515060(8, 1510408)
    Event_11515060(9, 1510409)
    Event_11515060(10, 1510410)
    Event_11515060(11, 1510411)
    Event_11515060(12, 1510412)
    Event_11515060(13, 1510413)
    Event_11515080(0, 1510450, 1510451)
    Event_11515080(1, 1510452, 1510453)
    Event_11510260(0, 11510251, 1512251, 1512250)
    Event_11510260(1, 11510257, 1512253, 1512252)
    Event_11510260(2, 11510258, 1512255, 1512254)
    DisableSoundEvent(sound_id=1513800)
    SkipLinesIfFlagDisabled(10, 12)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)
    Event_11515392()
    DisableObject(1511990)
    DeleteVFX(vfx_id=1511991, erase_root_only=False)
    DisableObject(1511992)
    DeleteVFX(vfx_id=1511993, erase_root_only=False)
    DisableObject(1511988)
    DeleteVFX(vfx_id=1511989, erase_root_only=False)
    SkipLines(11)
    Event_11515390()
    Event_11515391()
    Event_11515393()
    Event_11515392()
    Event_11510001()
    Event_11515394()
    Event_11515395()
    Event_11515396()
    Event_11515397()
    Event_11515398()
    Event_11515399()
    DisableSoundEvent(sound_id=1513802)
    SkipLinesIfFlagDisabled(6, 11510900)
    Event_11515382()
    DisableObject(1511890)
    DeleteVFX(vfx_id=1511891, erase_root_only=False)
    DisableObject(1511892)
    DeleteVFX(vfx_id=1511893, erase_root_only=False)
    SkipLines(9)
    Event_11515380()
    Event_11515381()
    Event_11516388()
    Event_11515383()
    Event_11515382()
    Event_11510900()
    Event_11515384()
    Event_11515385()
    Event_11515386()
    Event_11510450()
    Event_11510710(0, 11510251, 1510300, 1512251, 1512250)
    Event_11510710(1, 11510251, 1510301, 1512251, 1512250)
    Event_11510710(2, 11510251, 1510302, 1512251, 1512250)
    Event_11510710(3, 11510251, 1510305, 1512251, 1512250)
    Event_11510710(4, 11510251, 1510320, 1512251, 1512250)
    Event_11510710(5, 11510251, 1510321, 1512251, 1512250)
    Event_11510710(6, 11510251, 1510322, 1512251, 1512250)
    Event_11510710(7, 11510251, 1510323, 1512251, 1512250)
    Event_11510710(8, 11510251, 1510324, 1512251, 1512250)
    Event_11510710(9, 11510251, 1510325, 1512251, 1512250)
    Event_11510710(10, 11510251, 1510326, 1512251, 1512250)
    Event_11510710(11, 11510251, 1510327, 1512251, 1512250)
    Event_11510710(12, 11510251, 1510328, 1512251, 1512250)
    Event_11510710(13, 11510251, 1510329, 1512251, 1512250)
    Event_11510710(20, 11510257, 1510300, 1512253, 1512252)
    Event_11510710(21, 11510257, 1510301, 1512253, 1512252)
    Event_11510710(22, 11510257, 1510302, 1512253, 1512252)
    Event_11510710(23, 11510257, 1510305, 1512253, 1512252)
    Event_11510710(24, 11510257, 1510320, 1512253, 1512252)
    Event_11510710(25, 11510257, 1510321, 1512253, 1512252)
    Event_11510710(26, 11510257, 1510322, 1512253, 1512252)
    Event_11510710(27, 11510257, 1510323, 1512253, 1512252)
    Event_11510710(28, 11510257, 1510324, 1512253, 1512252)
    Event_11510710(29, 11510257, 1510325, 1512253, 1512252)
    Event_11510710(30, 11510257, 1510326, 1512253, 1512252)
    Event_11510710(31, 11510257, 1510327, 1512253, 1512252)
    Event_11510710(32, 11510257, 1510328, 1512253, 1512252)
    Event_11510710(33, 11510257, 1510329, 1512253, 1512252)
    Event_11510710(40, 11510258, 1510300, 1512255, 1512254)
    Event_11510710(41, 11510258, 1510301, 1512255, 1512254)
    Event_11510710(42, 11510258, 1510302, 1512255, 1512254)
    Event_11510710(43, 11510258, 1510305, 1512255, 1512254)
    Event_11510710(44, 11510258, 1510320, 1512255, 1512254)
    Event_11510710(45, 11510258, 1510321, 1512255, 1512254)
    Event_11510710(46, 11510258, 1510322, 1512255, 1512254)
    Event_11510710(47, 11510258, 1510323, 1512255, 1512254)
    Event_11510710(48, 11510258, 1510324, 1512255, 1512254)
    Event_11510710(49, 11510258, 1510325, 1512255, 1512254)
    Event_11510710(50, 11510258, 1510326, 1512255, 1512254)
    Event_11510710(51, 11510258, 1510327, 1512255, 1512254)
    Event_11510710(52, 11510258, 1510328, 1512255, 1512254)
    Event_11510710(53, 11510258, 1510329, 1512255, 1512254)
    Event_11515200(0, 1510200)
    Event_11515210(0, 1510200)
    Event_11515220(0, 1510200)
    Event_11515230(0, 1510200)
    Event_11515240(0, 1510200, 1512010)
    Event_11510850(0, 1510200)
    Event_11515190(0, 1510200)
    Event_11515200(1, 1510201)
    Event_11515210(1, 1510201)
    Event_11515220(1, 1510201)
    Event_11515230(1, 1510201)
    Event_11515240(1, 1510201, 1512011)
    Event_11510850(1, 1510201)
    Event_11515190(1, 1510201)
    Event_11515200(2, 1510202)
    Event_11515210(2, 1510202)
    Event_11515220(2, 1510202)
    Event_11515230(2, 1510202)
    Event_11515240(2, 1510202, 1512012)
    Event_11510850(2, 1510202)
    Event_11515190(2, 1510202)
    Event_11515200(3, 1510203)
    Event_11515210(3, 1510203)
    Event_11515220(3, 1510203)
    Event_11515230(3, 1510203)
    Event_11515240(3, 1510203, 1512013)
    Event_11510850(3, 1510203)
    Event_11515190(3, 1510203)
    Event_11510600(1, 1511651, 11510601)
    Event_11510600(2, 1511652, 11510602)
    Event_11510600(3, 1511653, 11510603)
    Event_11510600(4, 1511654, 11510604)
    Event_11510600(6, 1511656, 11510606)
    Event_11510600(7, 1511657, 11510607)
    Event_11510600(8, 1511658, 11510608)
    Event_11510600(9, 1511659, 11510609)
    Event_11510600(10, 1511660, 11510610)
    Event_11510600(11, 1511661, 11510611)
    Event_11510600(12, 1511662, 11510612)
    Event_11510600(15, 1511665, 11510615)
    Event_11510600(16, 1511666, 11510616)
    Event_11510600(17, 1511667, 11510617)
    Event_11510600(18, 1511668, 11510618)
    Event_11510600(19, 1511669, 11510619)
    Event_11510860(0, 1510250, 0)
    Event_11510860(1, 1510450, 53500000)
    Event_11510860(2, 1510452, 53500000)
    Event_11510860(3, 6640, 0)
    Event_11510860(4, 6650, 0)
    Event_11515843(0, 11510902, 1511990, 1512998, 1512997)
    Event_11515846(0, 11510902, 1511990, 1511991)
    Event_11515843(1, 11510903, 1511990, 1512998, 1512997)
    Event_11515846(1, 11510903, 1511990, 1511991)
    Event_11515843(2, 11510900, 1511890, 1512898, 1512897)
    Event_11515846(2, 11510900, 1511890, 1511891)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6640, event_flag=8258)
    HumanityRegistration(6650, event_flag=8266)
    HumanityRegistration(6543, event_flag=8310)
    Event_11515030()
    Event_11515029()
    Event_11515032()
    Event_11515033()
    Event_11515990(0, 11515031, 6543)
    HumanityRegistration(6003, event_flag=8310)
    SkipLinesIfFlagEnabled(2, 1008)
    SkipLinesIfFlagEnabled(1, 1004)
    DisableCharacter(6003)
    Event_11510510(0, 6003, 1004)
    Event_11510520(0, 6003, 1000, 1029, 1005)
    Event_11510530(0, 6003, 1000, 1029, 1008)
    HumanityRegistration(6010, event_flag=8318)
    Event_11510501(0, 6010, 1033)
    Event_11510520(1, 6010, 1030, 1036, 1034)
    Event_11510531(0, 6010, 1030, 1036, 1036)
    Event_11510532(0, 6010, 1030, 1036, 1031)
    Event_11510533(0, 6010)
    DisableCharacter(1510600)
    Event_11510520(2, 1510600, 1230, 1239, 1232)
    SetTeamType(1510650, TeamType.Ally)
    SkipLinesIfFlagRangeAnyEnabled(1, (1240, 1249))
    EnableFlag(1240)
    Event_11510520(3, 1510650, 1240, 1249, 1242)
    Event_11510502(0, 1510650, 1241)
    Event_11515090(0, 6210)
    Event_11515091(0, 6210)
    Event_11515092(0, 6210, 1511110, 1361, 1362)
    Event_11510510(4, 6210, 1361)
    Event_11510520(4, 6210, 1360, 1363, 1362)
    HumanityRegistration(6283, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1494)
    SkipLinesIfFlagEnabled(1, 1493)
    DisableCharacter(6283)
    Event_11510510(5, 6283, 1512)
    Event_11510520(5, 6283, 1490, 1514, 1513)
    Event_11510535(0, 6283, 1490, 1514, 1494)
    Event_11510536(0, 6283)
    HumanityRegistration(6302, event_flag=8462)
    HumanityRegistration(6490, event_flag=8908)
    HumanityRegistration(6500, event_flag=8916)
    DisableCharacter(6302)
    DisableCharacter(6490)
    DisableCharacter(6500)
    Event_11510541(0, 6302, 1570, 1599, 1578)
    Event_11510542(0, 6302, 1570, 1599, 1575)
    Event_11510543(0, 6302, 1570, 1599, 1572)
    Event_11510544(0, 6302, 1570, 1599, 1575)


@NeverRestart(11510090)
def Event_11510090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510090"""
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


@RestartOnRest(11515040)
def Event_11515040():
    """Event 11515040"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1510900)
    DisableCharacter(1510901)
    DisableCharacter(1510902)
    DisableCharacter(1510903)
    DisableCharacter(1510904)
    DisableCharacter(1510905)
    DisableCharacter(1510906)
    DisableCharacter(1510907)
    DisableCharacter(1510908)
    DisableCharacter(1510909)
    IfFlagEnabled(0, 11510050)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1510900)
    EnableCharacter(1510901)
    EnableCharacter(1510902)
    EnableCharacter(1510903)
    EnableCharacter(1510904)
    EnableCharacter(1510905)
    EnableCharacter(1510906)
    EnableCharacter(1510907)
    EnableCharacter(1510908)
    EnableCharacter(1510909)


@RestartOnRest(11515041)
def Event_11515041():
    """Event 11515041"""
    IfFlagEnabled(-1, 11515045)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11510050)
    DisableFlag(11515045)
    EnableFlag(5001)
    Kill(1510900)
    Kill(1510901)
    Kill(1510902)
    Kill(1510903)
    Kill(1510904)
    Kill(1510905)
    Kill(1510906)
    Kill(1510907)
    Kill(1510908)
    Kill(1510909)


@RestartOnRest(11515042)
def Event_11515042():
    """Event 11515042"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11510050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=ANOR_LONDO)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11510050)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=ANOR_LONDO)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11510050)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=ANOR_LONDO)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11510050)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=ANOR_LONDO)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11510050)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=ANOR_LONDO)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11510050)
    RestartIfConditionFalse(-6)
    EnableFlag(11510050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=ANOR_LONDO)
    RestartIfConditionFalse(7)
    DisableFlag(11510050)
    EnableFlag(11515045)


@NeverRestart(11515380)
def Event_11515380():
    """Event 11515380"""
    IfFlagDisabled(1, 11510900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1511890,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(743)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@NeverRestart(11515381)
def Event_11515381():
    """Event 11515381"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11510900)
    IfFlagEnabled(1, 11515383)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        boss_version=True,
        line_intersects=1511890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    SkipLinesIfFlagEnabled(2, 11510400)
    PlayCutscene(150151, cutscene_flags=2, player_id=10000, move_to_region=1512901, game_map=ANOR_LONDO)
    SkipLines(1)
    PlayCutscene(150156, cutscene_flags=2, player_id=10000, move_to_region=1512901, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    EnableCharacter(1510650)
    EnableFlag(11515388)
    Restart()


@NeverRestart(11516388)
def Event_11516388():
    """Event 11516388"""
    IfFlagEnabled(1, 11515388)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 7410)
    DisableFlag(11515388)
    Restart()


@NeverRestart(11515383)
def Event_11515383():
    """Event 11515383"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11510900)
    IfCharacterInsideRegion(1, PLAYER, region=1512896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1510650, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1510650)


@RestartOnRest(11515382)
def Event_11515382():
    """Event 11515382"""
    SkipLinesIfFlagDisabled(2, 11510900)
    DisableCharacter(1510650)
    End()
    DisableAI(1510650)
    IfFlagEnabled(1, 11515383)
    IfCharacterInsideRegion(1, PLAYER, region=1512896)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11515386)
    IfFlagEnabled(0, 11515387)
    SkipLinesIfClient(2)
    ForceAnimation(PLAYER, -1)
    ResetAnimation(PLAYER, disable_interpolation=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    SkipLinesIfConditionFalse(6, 2)
    BetrayCurrentCovenant()
    SkipLinesIfFlagEnabled(2, 9002)
    IncrementPvPSin()
    EnableFlag(9002)
    EnableFlag(742)
    SaveRequest()
    EnableAI(1510650)
    SetTeamType(1510650, TeamType.Boss)
    EnableBossHealthBar(1510650, name=5320, slot=0)


@NeverRestart(11510900)
def Event_11510900():
    """Event 11510900"""
    IfHealthLessThanOrEqual(0, 1510650, value=0.0)
    WaitFrames(frames=1)
    SkipLinesIfClient(7)
    EnableFlag(11515389)
    IfFlagEnabled(0, 11515389)
    SkipLinesIfFlagEnabled(2, 11510400)
    PlayCutscene(150152, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    SkipLines(1)
    PlayCutscene(150157, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    EnableFlag(4047)
    WaitFrames(frames=10)
    SkipLinesIfFlagDisabled(1, 12)
    EnableFlag(120)
    EnableFlag(11510900)
    KillBoss(game_area_param_id=1510650)
    DisableObject(1511890)
    DeleteVFX(vfx_id=1511891)
    EndIfClient()
    DisableFlag(11807170)
    DisableFlag(11807180)
    DisableFlag(11807190)
    DisableFlag(11807230)
    AwardAchievement(achievement_id=39)


@NeverRestart(11515384)
def Event_11515384():
    """Event 11515384"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11510900)
    IfFlagEnabled(1, 11515382)
    IfCharacterInsideRegion(1, PLAYER, region=1512890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1513802)


@NeverRestart(11515385)
def Event_11515385():
    """Event 11515385"""
    DisableNetworkSync()
    IfHealthLessThanOrEqual(1, 1510650, value=0.0)
    IfFlagEnabled(1, 11515384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1513802)


@RestartOnRest(11515386)
def Event_11515386():
    """Event 11515386"""
    IfThisEventFlagEnabled(1)
    IfFlagEnabled(1, 11510400)
    IfHost(1)
    IfThisEventFlagEnabled(2)
    IfHost(2)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    IfThisEventFlagEnabled(3)
    IfHost(3)
    IfConditionFalse(3, input_condition=1)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterType(-2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(-2, PLAYER, character_type=CharacterType.Intruder)
    EndIfConditionTrue(-2)
    SkipLinesIfFinishedConditionFalse(10, condition=1)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150155, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(150155, cutscene_flags=2, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(1)
    PlayCutscene(150155, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfFinishedConditionFalse(10, condition=2)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150161, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(150161, cutscene_flags=2, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(1)
    PlayCutscene(150161, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(150160, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(150160, cutscene_flags=2, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(1)
    PlayCutscene(150160, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()


@NeverRestart(11515390)
def Event_11515390():
    """Event 11515390"""
    IfFlagDisabled(1, 12)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1511990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11515391)
def Event_11515391():
    """Event 11515391"""
    IfFlagDisabled(1, 12)
    IfFlagEnabled(1, 11515393)
    IfCharacterType(1, PLAYER, character_type=CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11515393)
def Event_11515393():
    """Event 11515393"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 12)
    IfCharacterInsideRegion(1, PLAYER, region=1512996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1510800)
    ActivateMultiplayerBuffs(1510801)
    ActivateMultiplayerBuffs(1510810)
    ActivateMultiplayerBuffs(1510811)


@RestartOnRest(11515392)
def Event_11515392():
    """Event 11515392"""
    SkipLinesIfFlagDisabled(9, 12)
    DisableCharacter(1510800)
    DisableCharacter(1510801)
    DisableCharacter(1510810)
    DisableCharacter(1510811)
    Kill(1510800)
    Kill(1510801)
    Kill(1510810)
    Kill(1510811)
    End()
    DisableCharacter(1510801)
    DisableCharacter(1510811)
    DisableBackread(1510801)
    SkipLinesIfFlagEnabled(1, 11510000)
    DisableCharacter(1510800)
    DisableAI(1510800)
    DisableAI(1510810)
    IfFlagEnabled(1, 11515393)
    IfCharacterInsideRegion(1, PLAYER, region=1512990)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, character_type=CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, character_type=CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagEnabled(8, 11510000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150140, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150140, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1510800)
    EnableCharacter(1510810)
    EnableFlag(11510000)
    EnableAI(1510800)
    EnableAI(1510810)
    EnableBossHealthBar(1510800, name=5270, slot=1)
    EnableBossHealthBar(1510810, name=2360, slot=0)


@NeverRestart(11510001)
def Event_11510001():
    """Event 11510001"""
    DisableObject(1511950)
    IfCharacterDead(1, 1510800)
    IfCharacterDead(2, 1510810)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(10, condition=1)
    IfCharacterDead(0, 1510801)
    EnableFlag(11510902)
    PlaySoundEffect(anchor_entity=1510801, sound_id=777777777, sound_type=SoundType.s_SFX)
    Kill(1510811)
    KillBoss(game_area_param_id=1510801)
    DisableFlag(11807100)
    DisableFlag(11807110)
    DisableFlag(11807120)
    DisableFlag(11807130)
    SkipLines(9)
    IfCharacterDead(0, 1510811)
    EnableFlag(11510903)
    PlaySoundEffect(anchor_entity=1510811, sound_id=777777777, sound_type=SoundType.s_SFX)
    Kill(1510801)
    KillBoss(game_area_param_id=1510811)
    DisableFlag(11807060)
    DisableFlag(11807070)
    DisableFlag(11807080)
    DisableFlag(11807090)
    EnableFlag(12)
    EnableFlag(120)
    DisableObject(1511990)
    DeleteVFX(vfx_id=1511991)
    DisableObject(1511992)
    DeleteVFX(vfx_id=1511993)
    DisableObject(1511988)
    DeleteVFX(vfx_id=1511989)
    EnableObject(1511950)
    RegisterBonfire(bonfire_flag=11510920, obj=1511950)
    DisableNetworkSync()
    Wait(3.0)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)


@NeverRestart(11515394)
def Event_11515394():
    """Event 11515394"""
    DisableNetworkSync()
    IfFlagDisabled(1, 12)
    IfFlagEnabled(1, 11515392)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11515391)
    IfCharacterInsideRegion(1, PLAYER, region=1512990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1513800)
    EnableBackread(1510801)


@NeverRestart(11515395)
def Event_11515395():
    """Event 11515395"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12)
    IfFlagEnabled(1, 11515394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1513800)


@NeverRestart(11515396)
def Event_11515396():
    """Event 11515396"""
    IfCharacterDead(1, 1510800)
    IfCharacterDead(2, 1510810)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(12, condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150121, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150121, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1510800)
    DisableCharacter(1510810)
    DisableImmortality(1510810)
    Kill(1510810)
    EnableCharacter(1510811)
    EnableBossHealthBar(1510811, name=2360, slot=0)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150120, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150120, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1510810)
    DisableCharacter(1510800)
    DisableImmortality(1510800)
    Kill(1510800)
    EnableCharacter(1510801)
    EnableBossHealthBar(1510801, name=5270, slot=1)


@NeverRestart(11515397)
def Event_11515397():
    """Event 11515397"""
    IfHealthLessThanOrEqual(1, 1510800, value=0.0)
    IfHealthLessThanOrEqual(2, 1510810, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    EnableImmortality(1510810)
    End()
    EnableImmortality(1510800)


@RestartOnRest(11515398)
def Event_11515398():
    """Event 11515398"""
    IfCharacterDead(1, 1510810)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, 1510810)
    CreateNPCPart(
        1510810,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(1510810, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(1510810, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, 1510810, value=0.0)
    SetNPCPartHealth(1510810, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515399)
def Event_11515399():
    """Event 11515399"""
    IfCharacterDead(1, 1510811)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, 1510811)
    CreateNPCPart(
        1510811,
        npc_part_id=2360,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(1510811, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(1510811, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, 1510811, value=0.0)
    SetNPCPartHealth(1510811, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515060)
def Event_11515060(_, arg_0_3: int):
    """Event 11515060"""
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2870,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(arg_0_3, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(arg_0_3, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2870, desired_health=0, overwrite_max=False)


@RestartOnRest(11515080)
def Event_11515080(_, arg_0_3: int, arg_4_7: int):
    """Event 11515080"""
    DisableCharacter(arg_4_7)
    SkipLinesIfThisEventSlotFlagDisabled(5)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(arg_0_3, npc_part_id=5351, part_index=NPCPartType.Part1, part_health=65)
    IfCharacterPartHealthComparison(1, arg_0_3, npc_part_id=5351, comparison_type=ComparisonType.Equal, value=5)
    IfHealthLessThanOrEqual(2, arg_0_3, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(arg_0_3)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=110,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    ForceAnimation(arg_0_3, 8000)
    ForceAnimation(arg_4_7, 8100)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=1510450)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(53530000, host_only=True)


@NeverRestart(11510100)
def Event_11510100():
    """Event 11510100"""
    SkipLinesIfThisEventFlagDisabled(8)
    PostDestruction(1511100)
    PostDestruction(1511102)
    EndOfAnimation(obj=1511600, animation_id=111)
    EndOfAnimation(obj=1511101, animation_id=0)
    EndOfAnimation(obj=1511102, animation_id=1)
    EnableObjectInvulnerability(1511101)
    EnableTreasure(obj=1511600)
    End()
    DisableTreasure(obj=1511600)
    SkipLinesIfClient(1)
    CreateObjectVFX(vfx_id=1511600, obj=90, model_point=99010)
    ForceAnimation(1511600, 110, loop=True)
    IfObjectDestroyed(0, 1511100)
    ForceAnimation(1511600, 111)
    ForceAnimation(1511101, 0)
    ForceAnimation(1511102, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(1511600)
    EnableTreasure(obj=1511600)
    DestroyObject(1511102)


@NeverRestart(11510110)
def Event_11510110():
    """Event 11510110"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1511010, animation_id=0)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=1511010,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(PLAYER, destination=1511010, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1511010, 0)


@NeverRestart(11510200)
def Event_11510200():
    """Event 11510200"""
    SkipLinesIfThisEventFlagDisabled(4)
    DisableObjectActivation(1511001, obj_act_id=-1)
    EndOfAnimation(obj=1511000, animation_id=0)
    EndOfAnimation(obj=1511001, animation_id=0)
    End()
    IfFlagDisabled(1, 11510700)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1511001, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511001, 0, wait_for_completion=True)
    ForceAnimation(1511000, 0)


@NeverRestart(11510201)
def Event_11510201():
    """Event 11510201"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11510200)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1512000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511000,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010160)
    Restart()


@NeverRestart(11510210)
def Event_11510210():
    """Event 11510210"""
    SkipLinesIfThisEventFlagDisabled(2)
    EndOfAnimation(obj=1511200, animation_id=0)
    End()
    EnableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Solid)
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=TriggerAttribute.All,
    )
    Move(PLAYER, destination=1511200, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1511200, 0)
    DisableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Solid)


@NeverRestart(11510211)
def Event_11510211():
    """Event 11510211"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11510210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010161, anchor_entity=1511200)
    Restart()


@NeverRestart(11510220)
def Event_11510220():
    """Event 11510220"""
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterInsideRegion(0, PLAYER, region=1512350)
    ForceAnimation(1511050, 0)


@NeverRestart(11510260)
def Event_11510260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11510260"""
    DisableNetworkSync()
    SkipLinesIfFlagEnabled(4, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11510710)
def Event_11510710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510710"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_8_11)
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_4_7, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(11510300)
def Event_11510300():
    """Event 11510300"""
    IfFlagDisabled(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(3, 11510305)
    IfFlagDisabled(3, 11510303)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(4, 11510305)
    IfFlagEnabled(4, 11510303)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(5, 11510305)
    IfFlagDisabled(5, 11510301)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(6, 11510305)
    IfFlagDisabled(6, 11510302)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11515300)
    SkipLinesIfFlagEnabled(20, 11510305)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10, wait_for_completion=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        cutscene_id=150100,
        cutscene_flags=0,
        player_id=10000,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(4)
    SkipLinesIfFlagDisabled(2, 11510304)
    PlayCutscene(
        cutscene_id=150100,
        cutscene_flags=2,
        player_id=10000,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(1)
    PlayCutscene(150100, cutscene_flags=2, player_id=10000)
    WaitFrames(frames=1)
    EndOfAnimation(obj=1511300, animation_id=0)
    DisableMapCollision(collision=1513303)
    EnableMapCollision(collision=1513302)
    DisableFlag(11510303)
    EnableFlag(11510302)
    DisableFlag(11510304)
    EnableFlag(11510305)
    DisableFlag(11515300)
    Restart()
    SkipLinesIfFlagDisabled(33, 11510303)
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(0, 0, 1513303, 1513302, 11510303, 11510302, 180)
    SkipLinesIfFinishedConditionFalse(7, condition=4)
    Move(PLAYER, destination=1511302, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511302, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(1, 0, 1513303, 1513302, 11510303, 11510302, 180)
    SkipLinesIfFinishedConditionFalse(7, condition=5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515330(0, 0, 1, 1513301, 11510303, 11510301, 11, 180, 360)
    SkipLinesIfFinishedConditionFalse(7, condition=6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(2, 0, 1513303, 1513302, 11510303, 11510302, 180)
    IfFlagDisabled(0, 11515300)
    Restart()
    SkipLinesIfFlagDisabled(32, 11510302)
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 11)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(3, 1, 1513302, 1513301, 11510302, 11510301, 360)
    SkipLinesIfFinishedConditionFalse(6, condition=2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 13)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(4, 3, 1513302, 1513303, 11510302, 11510303, 180)
    SkipLinesIfFinishedConditionFalse(7, condition=3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 13)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(5, 3, 1513302, 1513303, 11510302, 11510303, 180)
    SkipLinesIfFinishedConditionFalse(7, condition=5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 11)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(6, 1, 1513302, 1513301, 11510302, 11510301, 360)
    IfFlagDisabled(0, 11515300)
    Restart()
    SkipLinesIfFlagDisabled(25, 11510301)
    SkipLinesIfFinishedConditionFalse(6, condition=2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(7, 2, 1513301, 1513302, 11510301, 11510302, 360)
    SkipLinesIfFinishedConditionFalse(7, condition=3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515330(1, 2, 3, 1513303, 11510301, 11510303, 13, 360, 180)
    SkipLinesIfFinishedConditionFalse(7, condition=6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    IfFramesElapsed(0, frames=0)
    Event_11515320(8, 2, 1513301, 1513302, 11510301, 11510302, 360)
    IfFlagDisabled(0, 11515300)
    Restart()
    DisplayDialog(text=10010170)
    Restart()


@NeverRestart(11510319)
def Event_11510319():
    """Event 11510319"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1512310)
    EnableFlag(11510304)
    IfCharacterOutsideRegion(0, PLAYER, region=1512310)
    DisableFlag(11510304)
    Restart()


@NeverRestart(11515320)
def Event_11515320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """Event 11515320"""
    DisableMapCollision(collision=arg_4_7)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(frames=arg_20_23)
    IfTimeElapsed(0, seconds=0.0)
    DisableObject(1511310)
    EnableMapCollision(collision=arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@NeverRestart(11515330)
def Event_11515330(
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
    """Event 11515330"""
    DisableMapCollision(collision=1513301)
    DisableMapCollision(collision=1513302)
    DisableMapCollision(collision=1513303)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(frames=arg_24_27)
    IfTimeElapsed(0, seconds=0.0)
    ForceAnimation(1511300, arg_20_23)
    WaitFrames(frames=130)
    IfTimeElapsed(0, seconds=0.0)
    ForceAnimation(1511300, arg_4_7)
    ForceAnimation(1511310, arg_4_7)
    WaitFrames(frames=arg_28_31)
    IfTimeElapsed(0, seconds=0.0)
    DisableObject(1511310)
    EnableMapCollision(collision=arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@NeverRestart(11510340)
def Event_11510340():
    """Event 11510340"""
    SkipLinesIfFlagDisabled(8, 11515300)
    EnableMapCollision(collision=1513310)
    EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    IfFlagDisabled(0, 11515300)
    Restart()
    SkipLinesIfFlagDisabled(8, 11510303)
    EnableMapCollision(collision=1513310)
    DisableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, 11515300)
    Restart()
    SkipLinesIfFlagDisabled(8, 11510302)
    DisableMapCollision(collision=1513310)
    EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, 11515300)
    Restart()
    SkipLinesIfFlagDisabled(8, 11510301)
    EnableMapCollision(collision=1513310)
    EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Solid)
    EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Solid)
    DisableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, 11515300)
    Restart()
    DisplayDialog(text=10010105)
    Restart()


@NeverRestart(11510350)
def Event_11510350():
    """Event 11510350"""
    IfHost(1)
    IfFlagEnabled(1, 11515301)
    IfFlagEnabled(1, 11510301)
    IfHost(2)
    IfFlagEnabled(2, 11515301)
    IfFlagEnabled(2, 11510302)
    IfHost(3)
    IfFlagEnabled(3, 11515301)
    IfFlagEnabled(3, 11510303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11515301)
    RestartIfSingleplayer()
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=51)
    EnableMapCollision(collision=1513301)
    Restart()
    SkipLinesIfFinishedConditionFalse(6, condition=2)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=50)
    EnableMapCollision(collision=1513302)
    Restart()
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=53)
    EnableMapCollision(collision=1513303)
    Restart()


@NeverRestart(11510310)
def Event_11510310():
    """Event 11510310"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(-2, 11510305)
    IfFlagEnabled(-2, 11510303)
    IfConditionTrue(3, input_condition=-2)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(-3, 11510305)
    IfFlagDisabled(-3, 11510303)
    IfConditionTrue(4, input_condition=-3)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(-4, 11510305)
    IfFlagEnabled(-4, 11510301)
    IfConditionTrue(5, input_condition=-4)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagDisabled(-5, 11510305)
    IfFlagEnabled(-5, 11510302)
    IfConditionTrue(6, input_condition=-5)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagEnabled(7, 11515300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=7)
    DisplayDialog(text=10010170)
    Restart()
    IfFlagDisabled(0, 11515300)
    Restart()


@NeverRestart(11510400)
def Event_11510400():
    """Event 11510400"""
    DisableMapPiece(map_piece_id=1513401)
    SkipLinesIfThisEventFlagDisabled(7)
    DisableSoundEvent(sound_id=1513801)
    SetMapDrawParamSlot(map_area_id=15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(map_piece_id=1513400)
    EnableMapPiece(map_piece_id=1513401)
    DisableObject(1511400)
    End()
    EnableCharacter(1510600)
    IfCharacterDead(1, 1510600)
    IfEntityWithinDistance(1, entity=1510600, other_entity=PLAYER, radius=15.0)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DisableSoundEvent(sound_id=1513801)
    EnableFlag(743)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.PrincessGuard)
    SkipLinesIfConditionFalse(4, 1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()
    DisableFlag(120)
    SkipLinesIfFlagEnabled(2, 11510900)
    PlayCutscene(150110, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150111, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    SetMapDrawParamSlot(map_area_id=15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(map_piece_id=1513400)
    EnableMapPiece(map_piece_id=1513401)
    DisableObject(1511400)
    IfPlayerHasGood(2, 2510)
    EndIfConditionTrue(2)
    AwardItemLot(1090, host_only=True)


@NeverRestart(11510401)
def Event_11510401():
    """Event 11510401"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1511400)
    End()
    EnableObjectInvulnerability(1511400)
    IfFlagEnabled(1, 11510400)
    IfEntityWithinDistance(1, entity=1511400, other_entity=PLAYER, radius=15.0)
    IfHost(2)
    IfCharacterHasSpecialEffect(2, PLAYER, 2310)
    IfEntityWithinDistance(2, entity=1511400, other_entity=PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(1511400)
    DestroyObject(1511400)
    ForceAnimation(1511400, 0)
    PlaySoundEffect(anchor_entity=1511400, sound_id=590000000, sound_type=SoundType.o_Object)


@RestartOnRest(11510450)
def Event_11510450():
    """Event 11510450"""
    IfCharacterDoesNotHaveTAEEvent(0, 1510650, tae_event_id=600)
    IfCharacterHasTAEEvent(0, 1510650, tae_event_id=600)
    DisableCharacter(1510650)
    Wait(1.0)
    SkipLinesIfFlagEnabled(2, 11515110)
    Event_11515110(0, 1512710, 11515110)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515111)
    Event_11515110(1, 1512711, 11515111)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515112)
    Event_11515110(2, 1512712, 11515112)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515113)
    Event_11515110(3, 1512713, 11515113)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515114)
    Event_11515110(4, 1512714, 11515114)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515115)
    Event_11515110(5, 1512715, 11515115)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515116)
    Event_11515110(6, 1512716, 11515116)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515117)
    Event_11515110(7, 1512717, 11515117)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515118)
    Event_11515110(8, 1512718, 11515118)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515119)
    Event_11515110(9, 1512719, 11515119)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515120)
    Event_11515110(10, 1512720, 11515120)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515121)
    Event_11515110(11, 1512721, 11515121)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515122)
    Event_11515110(12, 1512722, 11515122)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515123)
    Event_11515110(13, 1512723, 11515123)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515124)
    Event_11515110(14, 1512724, 11515124)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515125)
    Event_11515110(15, 1512725, 11515125)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515126)
    Event_11515110(16, 1512726, 11515126)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515127)
    Event_11515110(17, 1512727, 11515127)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515128)
    Event_11515110(18, 1512728, 11515128)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515129)
    Event_11515110(19, 1512729, 11515129)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515130)
    Event_11515110(20, 1512730, 11515130)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515131)
    Event_11515110(21, 1512731, 11515131)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515132)
    Event_11515110(22, 1512732, 11515132)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515133)
    Event_11515110(23, 1512733, 11515133)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515134)
    Event_11515110(24, 1512734, 11515134)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515135)
    Event_11515110(25, 1512735, 11515135)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515136)
    Event_11515110(26, 1512736, 11515136)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515137)
    Event_11515110(27, 1512737, 11515137)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515138)
    Event_11515110(28, 1512738, 11515138)
    Restart()
    SkipLinesIfFlagEnabled(2, 11515139)
    Event_11515110(29, 1512739, 11515139)
    Restart()


@UnknownRestart(11515110)
def Event_11515110(_, arg_0_3: int, arg_4_7: int):
    """Event 11515110"""
    Move(1510650, destination=arg_0_3, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1510650)
    ReplanAI(1510650)
    ForceAnimation(1510650, 7000, wait_for_completion=True)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagDisabled(2, 11515132)
    AICommand(1510650, command_id=1, slot=0)
    ReplanAI(1510650)


@NeverRestart(11510230)
def Event_11510230():
    """Event 11510230"""
    IfActionButton(0, prompt_text=10010100, anchor_entity=1512510, anchor_type=CoordEntityType.Region)
    IfSingleplayer(1)
    IfHost(1)
    IfPlayerHasGood(1, 384)
    SkipLinesIfConditionTrue(3, 1)
    SkipLinesIfClient(1)
    DisplayDialog(text=10010170)
    Restart()
    PlayCutscene(150135, cutscene_flags=0, player_id=10000, move_to_region=1102510, game_map=PAINTED_WORLD)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=1102511)
    SaveRequest()
    Restart()


@NeverRestart(11510240)
def Event_11510240():
    """Event 11510240"""
    EndIfClient()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfTimeElapsed(0, seconds=5.0)
    IfFlagDisabled(2, 11515050)
    IfActionButton(
        2,
        prompt_text=10010200,
        anchor_entity=1510100,
        anchor_type=CoordEntityType.Character,
        max_distance=7.0,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfSingleplayer(2)
    DisplayDialog(text=10010170)
    Restart()
    SkipLinesIfFlagEnabled(2, 11510400)
    PlayCutscene(150130, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    SkipLines(1)
    PlayCutscene(150132, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    WaitFrames(frames=1)
    SetMapDrawParamSlot(map_area_id=15, slot=0)
    Restart()


@NeverRestart(11515050)
def Event_11515050():
    """Event 11515050"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1510100)
    End()
    DisableImmortality(1510100)
    SetStandbyAnimationSettings(1510100, standby_animation=9000)
    IfAttacked(-1, attacked_entity=1510100, attacker=PLAYER)
    IfFlagEnabled(-1, 11515050)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11515050)
    ResetAnimation(1510100, disable_interpolation=True)
    ForceAnimation(1510100, 9060, wait_for_completion=True)
    DisableCharacter(1510100)


@NeverRestart(11510120)
def Event_11510120():
    """Event 11510120"""
    DisableNetworkSync()
    EndIfClient()
    IfFlagEnabled(1, 743)
    IfFlagEnabled(1, 12)
    IfFlagDisabled(1, 11510900)
    IfFlagEnabled(1, 11510400)
    IfCharacterInsideRegion(-1, PLAYER, region=1512400)
    IfStandingOnCollision(-1, 1513405)
    IfStandingOnCollision(-1, 1513100)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11510130)
def Event_11510130():
    """Event 11510130"""
    SkipLinesIfFlagEnabled(5, 11510400)
    DisableCharacter(6640)
    DisableCharacter(6650)
    IfFlagEnabled(0, 11510400)
    EnableCharacter(6640)
    EnableCharacter(6650)
    DisableCharacter(1510500)
    DisableCharacter(1510450)
    DisableCharacter(1510452)
    DisableCharacter(1510110)
    DisableCharacter(1510111)
    DisableCharacter(1510112)
    DisableCharacter(1510113)
    DisableCharacter(1510114)
    DisableCharacter(1510115)
    DisableCharacter(1510116)
    DisableCharacter(1510117)
    DisableCharacter(1510118)
    DisableCharacter(1510119)
    DisableCharacter(1510400)
    DisableCharacter(1510401)
    DisableCharacter(1510402)
    DisableCharacter(1510403)
    DisableCharacter(1510404)
    DisableCharacter(1510405)
    DisableCharacter(1510406)
    DisableCharacter(1510407)
    DisableCharacter(1510408)
    DisableCharacter(1510409)
    DisableCharacter(1510410)
    DisableCharacter(1510411)
    DisableCharacter(1510412)
    DisableCharacter(1510413)
    EndIfFlagEnabled(1034)
    Move(6010, destination=1512450, destination_type=CoordEntityType.Region, copy_draw_parent=1510452)
    SetNest(6010, region=1512450)
    SetStandbyAnimationSettings(6010)


@NeverRestart(11510131)
def Event_11510131():
    """Event 11510131"""
    EndIfClient()
    IfFlagEnabled(1, 11510400)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(respawn_point=1512960)
    SaveRequest()


@NeverRestart(11510140)
def Event_11510140():
    """Event 11510140"""
    IfFlagEnabled(0, 11510900)
    MoveRemains(source_region=1512420, destination_region=1512421)


@NeverRestart(11510150)
def Event_11510150():
    """Event 11510150"""
    DisableNetworkSync()
    IfHost(1)
    IfPlayerHasGood(1, 115)
    IfCharacterInsideRegion(1, PLAYER, region=1512101)
    IfConditionTrue(0, input_condition=1)
    End()


@NeverRestart(11510460)
def Event_11510460():
    """Event 11510460"""
    IfFlagEnabled(-7, 11510593)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagDisabled(1, 11515352)
    IfFlagDisabled(1, 11515350)
    IfFlagDisabled(1, 743)
    IfFlagEnabled(1, 1240)
    IfActionButton(1, prompt_text=10010210, anchor_entity=1512410, anchor_type=CoordEntityType.Region)
    IfConditionTrue(2, input_condition=-7)
    IfFlagEnabled(2, 11515352)
    IfFlagDisabled(2, 11515350)
    IfConditionTrue(3, input_condition=-7)
    IfFlagEnabled(3, 11515352)
    IfFlagEnabled(3, 11515350)
    IfHost(3)
    IfCharacterOutsideRegion(3, PLAYER, region=1512411)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(10, condition=1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    EnableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11515352)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    DisableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11515352)
    Restart()


@NeverRestart(11510462)
def Event_11510462():
    """Event 11510462"""
    DisableNetworkSync()
    WaitFrames(frames=2)
    EnableFlag(11510460)


@RestartOnRest(11510860)
def Event_11510860(_, arg_0_3: int, arg_4_7: int):
    """Event 11510860"""
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


@NeverRestart(11510461)
def Event_11510461():
    """Event 11510461"""
    IfFlagEnabled(0, 11515351)
    AddSpecialEffect(PLAYER, 4170)
    RotateToFaceEntity(PLAYER, target_entity=1510600)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    IfFlagDisabled(0, 11515351)
    CancelSpecialEffect(PLAYER, 4170)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    Restart()


@NeverRestart(11510600)
def Event_11510600(_, arg_0_3: int, arg_4_7: int):
    """Event 11510600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=arg_0_3, animation_id=0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(obj=arg_0_3)
    End()
    DisableTreasure(obj=arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(frames=10)
    EnableTreasure(obj=arg_0_3)


@RestartOnRest(11515200)
def Event_11515200(_, arg_0_3: int):
    """Event 11515200"""
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
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


@RestartOnRest(11515210)
def Event_11515210(_, arg_0_3: int):
    """Event 11515210"""
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


@RestartOnRest(11515220)
def Event_11515220(_, arg_0_3: int):
    """Event 11515220"""
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


@RestartOnRest(11515230)
def Event_11515230(_, arg_0_3: int):
    """Event 11515230"""
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


@RestartOnRest(11515240)
def Event_11515240(_, arg_0_3: int, arg_4_7: int):
    """Event 11515240"""
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


@RestartOnRest(11510850)
def Event_11510850(_, arg_0_3: int):
    """Event 11510850"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest(11515190)
def Event_11515190(_, arg_0_3: int):
    """Event 11515190"""
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


@RestartOnRest(11515250)
def Event_11515250():
    """Event 11515250"""
    EndIfThisEventFlagEnabled()
    DisableAI(1510310)
    IfCharacterInsideRegion(1, PLAYER, region=1512050)
    IfAttacked(2, attacked_entity=1510310, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(1510310, 500)
    EnableAI(1510310)


@RestartOnRest(11515251)
def Event_11515251():
    """Event 11515251"""
    EndIfThisEventFlagEnabled()
    DisableAI(1510305)
    IfCharacterInsideRegion(-1, PLAYER, region=1512060)
    IfAttacked(-1, attacked_entity=1510305, attacker=PLAYER)
    IfEntityWithinDistance(-1, entity=1510305, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1510305)


@NeverRestart(11510215)
def Event_11510215():
    """Event 11510215"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1511210)
    End()
    IfObjectDestroyed(0, 1511210)
    End()


@NeverRestart(11510510)
def Event_11510510(_, arg_0_3: int, arg_4_7: int):
    """Event 11510510"""
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


@NeverRestart(11510520)
def Event_11510520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11510501)
def Event_11510501(_, arg_0_3: int, arg_4_7: int):
    """Event 11510501"""
    IfFlagEnabled(-2, 1030)
    IfFlagEnabled(-2, 1031)
    IfFlagEnabled(-2, 1036)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, value=0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, value=0.0)
    IfAttacked(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfThisEventFlagDisabled(1)
    IfFlagDisabled(2, 1034)
    IfFlagEnabled(-3, 1232)
    IfFlagEnabled(-3, 1241)
    IfFlagEnabled(-3, 1242)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterBackreadEnabled(2, arg_0_3)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(3, arg_4_7)
    IfThisEventFlagEnabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11510502)
def Event_11510502(_, arg_0_3: int, arg_4_7: int):
    """Event 11510502"""
    IfFlagEnabled(1, 1240)
    IfFlagEnabled(-2, 1232)
    IfFlagEnabled(-2, 11515382)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterAlive(1, arg_0_3)
    IfFlagEnabled(2, arg_4_7)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.Boss)


@NeverRestart(11510530)
def Event_11510530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510530"""
    IfFlagDisabled(1, 1004)
    IfFlagEnabled(1, 1001)
    IfFlagEnabled(1, 11010590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11510531)
def Event_11510531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510531"""
    IfFlagDisabled(1, 1033)
    IfFlagEnabled(1, 1030)
    IfFlagEnabled(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11510532)
def Event_11510532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510532"""
    IfFlagDisabled(1, 1033)
    IfFlagEnabled(-1, 1030)
    IfFlagEnabled(-1, 1036)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 711)
    IfFlagEnabled(1, 712)
    IfFlagEnabled(1, 713)
    IfFlagEnabled(1, 714)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(11510533)
def Event_11510533(_, arg_0_3: int):
    """Event 11510533"""
    EndIfThisEventFlagEnabled()
    IfCharacterDead(0, arg_0_3)
    EnableFlag(151)


@NeverRestart(11510535)
def Event_11510535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510535"""
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1493)
    IfCharacterDead(1, 1510300)
    IfCharacterDead(1, 1510301)
    IfCharacterDead(1, 1510302)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


@NeverRestart(11510536)
def Event_11510536(_, arg_0_3: int):
    """Event 11510536"""
    IfHost(1)
    IfFlagDisabled(1, 1512)
    IfFlagEnabled(1, 1494)
    IfFlagEnabled(1, 11510590)
    SkipLinesIfThisEventFlagEnabled(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


@NeverRestart(11510541)
def Event_11510541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510541"""
    IfFlagEnabled(-1, 1572)
    IfFlagEnabled(-1, 1573)
    IfFlagEnabled(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 11510700)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetTeamType(6490, TeamType.WhitePhantom)
    SetTeamType(6500, TeamType.WhitePhantom)
    DisableAI(arg_0_3)
    DisableAI(6490)
    DisableAI(6500)
    IfFlagEnabled(-1, 11510598)
    IfAttacked(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=6490, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=6500, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    EnableAI(6490)
    EnableAI(6500)


@NeverRestart(11510542)
def Event_11510542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510542"""
    IfHealthLessThanOrEqual(0, arg_0_3, value=0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8102)


@NeverRestart(11510543)
def Event_11510543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510543"""
    DisableObject(1511750)
    DeleteVFX(vfx_id=1511751, erase_root_only=False)
    DisableObject(1511752)
    DeleteVFX(vfx_id=1511753, erase_root_only=False)
    DisableObject(1511754)
    DeleteVFX(vfx_id=1511755, erase_root_only=False)
    IfFlagEnabled(0, 11510700)
    EnableObject(1511750)
    CreateVFX(vfx_id=1511751)
    EnableObject(1511752)
    CreateVFX(vfx_id=1511753)
    EnableObject(1511754)
    CreateVFX(vfx_id=1511755)
    DisableFlag(8104)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(1510412)
    DisableCharacter(1510413)
    DisableCharacter(1510500)
    EnableCharacter(arg_0_3)
    EnableCharacter(6490)
    EnableCharacter(6500)
    SkipLinesIfFlagEnabled(2, 8101)
    EnableFlag(8101)
    End()
    EnableFlag(8100)


@NeverRestart(11510544)
def Event_11510544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11510544"""
    SkipLinesIfThisEventFlagDisabled(2)
    EnableTreasure(obj=1511601)
    End()
    DisableObject(1511601)
    DisableTreasure(obj=1511601)
    IfHost(1)
    IfFlagDisabled(1, 11510700)
    IfFlagEnabled(1, 8102)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    SkipLinesIfConditionFalse(3, -1)
    AwardItemLot(2060, host_only=True)
    AwardItemLot(6300, host_only=True)
    RemoveGoodFromPlayer(item=115)
    EnableObject(1511601)
    EnableTreasure(obj=1511601)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


@NeverRestart(151)
def Event_151():
    """Event 151"""
    DisableNetworkSync()
    IfThisEventFlagEnabled(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=1511960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        text=10010184,
        anchor_entity=1511960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@RestartOnRest(11515090)
def Event_11515090(_, arg_0_3: int):
    """Event 11515090"""
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfCharacterDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest(11515091)
def Event_11515091(_, arg_0_3: int):
    """Event 11515091"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest(11515092)
def Event_11515092(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11515092"""
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_12_15)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    EnableObjectInvulnerability(arg_4_7)
    IfFlagEnabled(-1, arg_8_11)
    IfFlagEnabled(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    DisableObjectInvulnerability(arg_4_7)
    WaitFrames(frames=1)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_id=596500000, sound_type=SoundType.o_Object)


@NeverRestart(11515030)
def Event_11515030():
    """Event 11515030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6543, authority_level=UpdateAuthority.Forced)
    SkipLinesIfThisEventFlagDisabled(1)
    DisableCharacter(6003)
    SkipLinesIfFlagEnabled(3, 11515034)
    IfClient(2)
    IfFlagEnabled(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6543)
    EndIfFlagEnabled(12)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(-1, 1004)
    IfFlagEnabled(-1, 1005)
    IfFlagEnabled(-1, 1006)
    IfFlagEnabled(-1, 1010)
    IfFlagEnabled(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6543)
    IfEntityWithinDistance(1, entity=6543, other_entity=PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6543,
        region=1512001,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(6003)
    IfFlagEnabled(0, 11515031)
    SetNest(6543, region=1512002)


@NeverRestart(11515990)
def Event_11515990(_, arg_0_3: int, arg_4_7: int):
    """Event 11515990"""
    IfFlagEnabled(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagDisabled(0, arg_0_3)
    Restart()


@NeverRestart(11515029)
def Event_11515029():
    """Event 11515029"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6543, authority_level=UpdateAuthority.Forced)
    SkipLinesIfThisEventFlagDisabled(1)
    DisableCharacter(6003)
    SkipLinesIfFlagEnabled(3, 11515034)
    IfClient(2)
    IfFlagEnabled(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6543)
    EndIfFlagEnabled(12)
    If_Unknown_3_24(1, unk1=4, unk2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 11515031)
    IfFlagDisabled(1, 11515034)
    IfFlagEnabled(-1, 1004)
    IfFlagEnabled(-1, 1005)
    IfFlagEnabled(-1, 1006)
    IfFlagEnabled(-1, 1010)
    IfFlagEnabled(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6543)
    IfEntityWithinDistance(1, entity=6543, other_entity=PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6543,
        region=1512001,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(6003)
    IfFlagEnabled(0, 11515031)
    SetNest(6543, region=1512002)


@NeverRestart(11515032)
def Event_11515032():
    """Event 11515032"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 11515031)
    IfFlagEnabled(1, 11515393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6543, command_id=10, slot=0)
    ReplanAI(6543)
    IfCharacterInsideRegion(0, 6543, region=1512998)
    RotateToFaceEntity(6543, target_entity=1512997)
    ForceAnimation(6543, 7410)
    AICommand(6543, command_id=-1, slot=0)
    ReplanAI(6543)


@NeverRestart(11515033)
def Event_11515033():
    """Event 11515033"""
    IfFlagEnabled(1, 11515031)
    IfFlagDisabled(1, 11515390)
    IfCharacterInsideRegion(1, PLAYER, region=1512801)
    IfConditionTrue(0, input_condition=1)
    AICommand(6543, command_id=8, slot=0)
    ReplanAI(6543)
    IfAllPlayersOutsideRegion(0, region=1512801)
    AICommand(6543, command_id=-1, slot=0)
    ReplanAI(6543)
    Restart()


@NeverRestart(11515843)
def Event_11515843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """Event 11515843"""
    IfFlagEnabled(1, 120)
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


@NeverRestart(11515846)
def Event_11515846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """Event 11515846"""
    IfFlagEnabled(1, 120)
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
