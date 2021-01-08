"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 12)
    RegisterBonfire(11510920, obj=1511950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11510992, obj=1511960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RegisterBonfire(11510984, obj=1511961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11510976, obj=1511962, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=1511140)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=1511141)
    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(1511994)
    DeleteVFX(1511995, erase_root_only=False)
    DisableObject(1511310)
    DisableCollision(1513301)
    DisableCollision(1513302)
    DisableCollision(1513303)
    SkipLinesIfFlagOff(1, 11510300)
    SkipLinesIfFlagOff(6, 11510303)
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(1511300, 53)
    EnableCollision(1513303)
    SkipLines(13)
    SkipLinesIfFlagOff(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 50)
    EnableCollision(1513302)
    SkipLines(6)
    SkipLinesIfFlagOff(5, 11510301)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 51)
    EnableCollision(1513301)
    DisableObject(1511450)
    DisableFlag(11510460)
    RunEvent(11510090, slot=0, args=(1511700, 1511701, 1512600, 1512601))
    RunEvent(11510090, slot=1, args=(1511702, 1511703, 1512602, 1512603))
    RunEvent(11515040)
    RunEvent(11515041)
    RunEvent(11515042)
    RunEvent(11510200)
    RunEvent(11510201)
    RunEvent(11510100)
    RunEvent(11510210)
    RunEvent(11510211)
    RunEvent(11510220)
    RunEvent(11510300)
    RunEvent(11510319)
    RunEvent(11510340)
    RunEvent(11510350)
    RunEvent(11510310)
    RunEvent(11515250)
    RunEvent(11515251)
    RunEvent(11510110)
    RunEvent(11510400)
    RunEvent(11510401)
    RunEvent(11510230)
    RunEvent(11510240)
    RunEvent(11515050)
    RunEvent(11510120)
    RunEvent(11510130)
    RunEvent(11510131)
    RunEvent(11510460)
    RunEvent(11510462)
    RunEvent(11510461)
    RunEvent(11510140)
    RunEvent(11510150)
    RunEvent(151)
    RunEvent(11510215)
    RunEvent(11515060, slot=0, args=(1510400,))
    RunEvent(11515060, slot=1, args=(1510401,))
    RunEvent(11515060, slot=2, args=(1510402,))
    RunEvent(11515060, slot=3, args=(1510403,))
    RunEvent(11515060, slot=4, args=(1510404,))
    RunEvent(11515060, slot=5, args=(1510405,))
    RunEvent(11515060, slot=6, args=(1510406,))
    RunEvent(11515060, slot=7, args=(1510407,))
    RunEvent(11515060, slot=8, args=(1510408,))
    RunEvent(11515060, slot=9, args=(1510409,))
    RunEvent(11515060, slot=10, args=(1510410,))
    RunEvent(11515060, slot=11, args=(1510411,))
    RunEvent(11515060, slot=12, args=(1510412,))
    RunEvent(11515060, slot=13, args=(1510413,))
    RunEvent(11515080, slot=0, args=(1510450, 1510451))
    RunEvent(11515080, slot=1, args=(1510452, 1510453))
    RunEvent(11510260, slot=0, args=(11510251, 1512251, 1512250))
    RunEvent(11510260, slot=1, args=(11510257, 1512253, 1512252))
    RunEvent(11510260, slot=2, args=(11510258, 1512255, 1512254))
    DisableSoundEvent(1513800)
    SkipLinesIfFlagOff(10, 12)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)
    RunEvent(11515392)
    DisableObject(1511990)
    DeleteVFX(1511991, erase_root_only=False)
    DisableObject(1511992)
    DeleteVFX(1511993, erase_root_only=False)
    DisableObject(1511988)
    DeleteVFX(1511989, erase_root_only=False)
    SkipLines(11)
    RunEvent(11515390)
    RunEvent(11515391)
    RunEvent(11515393)
    RunEvent(11515392)
    RunEvent(11510001)
    RunEvent(11515394)
    RunEvent(11515395)
    RunEvent(11515396)
    RunEvent(11515397)
    RunEvent(11515398)
    RunEvent(11515399)
    DisableSoundEvent(1513802)
    SkipLinesIfFlagOff(6, 11510900)
    RunEvent(11515382)
    DisableObject(1511890)
    DeleteVFX(1511891, erase_root_only=False)
    DisableObject(1511892)
    DeleteVFX(1511893, erase_root_only=False)
    SkipLines(9)
    RunEvent(11515380)
    RunEvent(11515381)
    RunEvent(11516388)
    RunEvent(11515383)
    RunEvent(11515382)
    RunEvent(11510900)
    RunEvent(11515384)
    RunEvent(11515385)
    RunEvent(11515386)
    RunEvent(11510450)
    RunEvent(11510710, slot=0, args=(11510251, 1510300, 1512251, 1512250))
    RunEvent(11510710, slot=1, args=(11510251, 1510301, 1512251, 1512250))
    RunEvent(11510710, slot=2, args=(11510251, 1510302, 1512251, 1512250))
    RunEvent(11510710, slot=3, args=(11510251, 1510305, 1512251, 1512250))
    RunEvent(11510710, slot=4, args=(11510251, 1510320, 1512251, 1512250))
    RunEvent(11510710, slot=5, args=(11510251, 1510321, 1512251, 1512250))
    RunEvent(11510710, slot=6, args=(11510251, 1510322, 1512251, 1512250))
    RunEvent(11510710, slot=7, args=(11510251, 1510323, 1512251, 1512250))
    RunEvent(11510710, slot=8, args=(11510251, 1510324, 1512251, 1512250))
    RunEvent(11510710, slot=9, args=(11510251, 1510325, 1512251, 1512250))
    RunEvent(11510710, slot=10, args=(11510251, 1510326, 1512251, 1512250))
    RunEvent(11510710, slot=11, args=(11510251, 1510327, 1512251, 1512250))
    RunEvent(11510710, slot=12, args=(11510251, 1510328, 1512251, 1512250))
    RunEvent(11510710, slot=13, args=(11510251, 1510329, 1512251, 1512250))
    RunEvent(11510710, slot=20, args=(11510257, 1510300, 1512253, 1512252))
    RunEvent(11510710, slot=21, args=(11510257, 1510301, 1512253, 1512252))
    RunEvent(11510710, slot=22, args=(11510257, 1510302, 1512253, 1512252))
    RunEvent(11510710, slot=23, args=(11510257, 1510305, 1512253, 1512252))
    RunEvent(11510710, slot=24, args=(11510257, 1510320, 1512253, 1512252))
    RunEvent(11510710, slot=25, args=(11510257, 1510321, 1512253, 1512252))
    RunEvent(11510710, slot=26, args=(11510257, 1510322, 1512253, 1512252))
    RunEvent(11510710, slot=27, args=(11510257, 1510323, 1512253, 1512252))
    RunEvent(11510710, slot=28, args=(11510257, 1510324, 1512253, 1512252))
    RunEvent(11510710, slot=29, args=(11510257, 1510325, 1512253, 1512252))
    RunEvent(11510710, slot=30, args=(11510257, 1510326, 1512253, 1512252))
    RunEvent(11510710, slot=31, args=(11510257, 1510327, 1512253, 1512252))
    RunEvent(11510710, slot=32, args=(11510257, 1510328, 1512253, 1512252))
    RunEvent(11510710, slot=33, args=(11510257, 1510329, 1512253, 1512252))
    RunEvent(11510710, slot=40, args=(11510258, 1510300, 1512255, 1512254))
    RunEvent(11510710, slot=41, args=(11510258, 1510301, 1512255, 1512254))
    RunEvent(11510710, slot=42, args=(11510258, 1510302, 1512255, 1512254))
    RunEvent(11510710, slot=43, args=(11510258, 1510305, 1512255, 1512254))
    RunEvent(11510710, slot=44, args=(11510258, 1510320, 1512255, 1512254))
    RunEvent(11510710, slot=45, args=(11510258, 1510321, 1512255, 1512254))
    RunEvent(11510710, slot=46, args=(11510258, 1510322, 1512255, 1512254))
    RunEvent(11510710, slot=47, args=(11510258, 1510323, 1512255, 1512254))
    RunEvent(11510710, slot=48, args=(11510258, 1510324, 1512255, 1512254))
    RunEvent(11510710, slot=49, args=(11510258, 1510325, 1512255, 1512254))
    RunEvent(11510710, slot=50, args=(11510258, 1510326, 1512255, 1512254))
    RunEvent(11510710, slot=51, args=(11510258, 1510327, 1512255, 1512254))
    RunEvent(11510710, slot=52, args=(11510258, 1510328, 1512255, 1512254))
    RunEvent(11510710, slot=53, args=(11510258, 1510329, 1512255, 1512254))
    RunEvent(11515200, slot=0, args=(1510200,))
    RunEvent(11515210, slot=0, args=(1510200,))
    RunEvent(11515220, slot=0, args=(1510200,))
    RunEvent(11515230, slot=0, args=(1510200,))
    RunEvent(11515240, slot=0, args=(1510200, 1512010))
    RunEvent(11510850, slot=0, args=(1510200,))
    RunEvent(11515190, slot=0, args=(1510200,))
    RunEvent(11515200, slot=1, args=(1510201,))
    RunEvent(11515210, slot=1, args=(1510201,))
    RunEvent(11515220, slot=1, args=(1510201,))
    RunEvent(11515230, slot=1, args=(1510201,))
    RunEvent(11515240, slot=1, args=(1510201, 1512011))
    RunEvent(11510850, slot=1, args=(1510201,))
    RunEvent(11515190, slot=1, args=(1510201,))
    RunEvent(11515200, slot=2, args=(1510202,))
    RunEvent(11515210, slot=2, args=(1510202,))
    RunEvent(11515220, slot=2, args=(1510202,))
    RunEvent(11515230, slot=2, args=(1510202,))
    RunEvent(11515240, slot=2, args=(1510202, 1512012))
    RunEvent(11510850, slot=2, args=(1510202,))
    RunEvent(11515190, slot=2, args=(1510202,))
    RunEvent(11515200, slot=3, args=(1510203,))
    RunEvent(11515210, slot=3, args=(1510203,))
    RunEvent(11515220, slot=3, args=(1510203,))
    RunEvent(11515230, slot=3, args=(1510203,))
    RunEvent(11515240, slot=3, args=(1510203, 1512013))
    RunEvent(11510850, slot=3, args=(1510203,))
    RunEvent(11515190, slot=3, args=(1510203,))
    RunEvent(11510600, slot=1, args=(1511651, 11510601))
    RunEvent(11510600, slot=2, args=(1511652, 11510602))
    RunEvent(11510600, slot=3, args=(1511653, 11510603))
    RunEvent(11510600, slot=4, args=(1511654, 11510604))
    RunEvent(11510600, slot=6, args=(1511656, 11510606))
    RunEvent(11510600, slot=7, args=(1511657, 11510607))
    RunEvent(11510600, slot=8, args=(1511658, 11510608))
    RunEvent(11510600, slot=9, args=(1511659, 11510609))
    RunEvent(11510600, slot=10, args=(1511660, 11510610))
    RunEvent(11510600, slot=11, args=(1511661, 11510611))
    RunEvent(11510600, slot=12, args=(1511662, 11510612))
    RunEvent(11510600, slot=15, args=(1511665, 11510615))
    RunEvent(11510600, slot=16, args=(1511666, 11510616))
    RunEvent(11510600, slot=17, args=(1511667, 11510617))
    RunEvent(11510600, slot=18, args=(1511668, 11510618))
    RunEvent(11510600, slot=19, args=(1511669, 11510619))
    RunEvent(11510860, slot=0, args=(1510250, 0))
    RunEvent(11510860, slot=1, args=(1510450, 53500000))
    RunEvent(11510860, slot=2, args=(1510452, 53500000))
    RunEvent(11510860, slot=3, args=(6640, 0))
    RunEvent(11510860, slot=4, args=(6650, 0))
    RunEvent(11515843, slot=0, args=(11510902, 1511990, 1512998, 1512997))
    RunEvent(11515846, slot=0, args=(11510902, 1511990, 1511991))
    RunEvent(11515843, slot=1, args=(11510903, 1511990, 1512998, 1512997))
    RunEvent(11515846, slot=1, args=(11510903, 1511990, 1511991))
    RunEvent(11515843, slot=2, args=(11510900, 1511890, 1512898, 1512897))
    RunEvent(11515846, slot=2, args=(11510900, 1511890, 1511891))


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6640, 8258)
    HumanityRegistration(6650, 8266)
    HumanityRegistration(6543, 8310)
    RunEvent(11515030)
    RunEvent(11515029)
    RunEvent(11515032)
    RunEvent(11515033)
    RunEvent(11515990, slot=0, args=(11515031, 6543))
    HumanityRegistration(6003, 8310)
    SkipLinesIfFlagOn(2, 1008)
    SkipLinesIfFlagOn(1, 1004)
    DisableCharacter(6003)
    RunEvent(11510510, slot=0, args=(6003, 1004))
    RunEvent(11510520, slot=0, args=(6003, 1000, 1029, 1005))
    RunEvent(11510530, slot=0, args=(6003, 1000, 1029, 1008))
    HumanityRegistration(6010, 8318)
    RunEvent(11510501, slot=0, args=(6010, 1033))
    RunEvent(11510520, slot=1, args=(6010, 1030, 1036, 1034))
    RunEvent(11510531, slot=0, args=(6010, 1030, 1036, 1036))
    RunEvent(11510532, slot=0, args=(6010, 1030, 1036, 1031))
    RunEvent(11510533, slot=0, args=(6010,))
    DisableCharacter(1510600)
    RunEvent(11510520, slot=2, args=(1510600, 1230, 1239, 1232))
    SetTeamType(1510650, TeamType.Ally)
    SkipLinesIfFlagRangeAnyOn(1, (1240, 1249))
    EnableFlag(1240)
    RunEvent(11510520, slot=3, args=(1510650, 1240, 1249, 1242))
    RunEvent(11510502, slot=0, args=(1510650, 1241))
    RunEvent(11515090, slot=0, args=(6210,))
    RunEvent(11515091, slot=0, args=(6210,))
    RunEvent(11515092, slot=0, args=(6210, 1511110, 1361, 1362))
    RunEvent(11510510, slot=4, args=(6210, 1361))
    RunEvent(11510520, slot=4, args=(6210, 1360, 1363, 1362))
    HumanityRegistration(6283, 8446)
    SkipLinesIfFlagOn(3, 1512)
    SkipLinesIfFlagOn(2, 1494)
    SkipLinesIfFlagOn(1, 1493)
    DisableCharacter(6283)
    RunEvent(11510510, slot=5, args=(6283, 1512))
    RunEvent(11510520, slot=5, args=(6283, 1490, 1514, 1513))
    RunEvent(11510535, slot=0, args=(6283, 1490, 1514, 1494))
    RunEvent(11510536, slot=0, args=(6283,))
    HumanityRegistration(6302, 8462)
    HumanityRegistration(6490, 8908)
    HumanityRegistration(6500, 8916)
    DisableCharacter(6302)
    DisableCharacter(6490)
    DisableCharacter(6500)
    RunEvent(11510541, slot=0, args=(6302, 1570, 1599, 1578))
    RunEvent(11510542, slot=0, args=(6302, 1570, 1599, 1575))
    RunEvent(11510543, slot=0, args=(6302, 1570, 1599, 1572))
    RunEvent(11510544, slot=0, args=(6302, 1570, 1599, 1575))


def Event11510090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510090: Event 11510090 """
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
def Event11515040():
    """ 11515040: Event 11515040 """
    EndIfThisEventOn()
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
    IfFlagOn(0, 11510050)
    EndIfFlagOn(735)
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


@RestartOnRest
def Event11515041():
    """ 11515041: Event 11515041 """
    IfFlagOn(-1, 11515045)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11510050)
    DisableFlag(11515045)
    EnableFlag(5001)
    Kill(1510900, award_souls=False)
    Kill(1510901, award_souls=False)
    Kill(1510902, award_souls=False)
    Kill(1510903, award_souls=False)
    Kill(1510904, award_souls=False)
    Kill(1510905, award_souls=False)
    Kill(1510906, award_souls=False)
    Kill(1510907, award_souls=False)
    Kill(1510908, award_souls=False)
    Kill(1510909, award_souls=False)


@RestartOnRest
def Event11515042():
    """ 11515042: Event 11515042 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11510050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=ANOR_LONDO)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11510050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=ANOR_LONDO)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11510050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=ANOR_LONDO)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11510050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=ANOR_LONDO)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11510050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=ANOR_LONDO)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11510050)
    RestartIfConditionFalse(-6)
    EnableFlag(11510050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=ANOR_LONDO)
    RestartIfConditionFalse(7)
    DisableFlag(11510050)
    EnableFlag(11515045)


def Event11515380():
    """ 11515380: Event 11515380 """
    IfFlagOff(1, 11510900)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        line_intersects=1511890,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    EnableFlag(743)
    RotateToFaceEntity(PLAYER, 1512897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11515381():
    """ 11515381: Event 11515381 """
    DisableNetworkSync()
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11515383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1511890,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1512897)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150151, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1512901, move_to_map=ANOR_LONDO
    )
    SkipLines(1)
    PlayCutscene(
        150156, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1512901, move_to_map=ANOR_LONDO
    )
    WaitFrames(1)
    EnableCharacter(1510650)
    EnableFlag(11515388)
    Restart()


def Event11516388():
    """ 11516388: Event 11516388 """
    IfFlagOn(1, 11515388)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 7410)
    DisableFlag(11515388)
    Restart()


def Event11515383():
    """ 11515383: Event 11515383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11510900)
    IfCharacterInsideRegion(1, PLAYER, region=1512896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1510650, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1510650)


@RestartOnRest
def Event11515382():
    """ 11515382: Event 11515382 """
    SkipLinesIfFlagOff(2, 11510900)
    DisableCharacter(1510650)
    End()
    DisableAI(1510650)
    IfFlagOn(1, 11515383)
    IfCharacterInsideRegion(1, PLAYER, region=1512896)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11515386)
    IfFlagOn(0, 11515387)
    SkipLinesIfClient(2)
    ForceAnimation(PLAYER, -1)
    ResetAnimation(PLAYER, disable_interpolation=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    SkipLinesIfConditionFalse(6, 2)
    BetrayCurrentCovenant()
    SkipLinesIfFlagOn(2, 9002)
    IncrementPvPSin()
    EnableFlag(9002)
    EnableFlag(742)
    SaveRequest()
    EnableAI(1510650)
    SetTeamType(1510650, TeamType.Boss)
    EnableBossHealthBar(1510650, name=5320, slot=0)


def Event11510900():
    """ 11510900: Event 11510900 """
    IfHealthLessThanOrEqual(0, 1510650, 0.0)
    WaitFrames(1)
    SkipLinesIfClient(7)
    EnableFlag(11515389)
    IfFlagOn(0, 11515389)
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150152, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1512897, move_to_map=ANOR_LONDO
    )
    SkipLines(1)
    PlayCutscene(
        150157, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1512897, move_to_map=ANOR_LONDO
    )
    EnableFlag(4047)
    WaitFrames(10)
    SkipLinesIfFlagOff(1, 12)
    EnableFlag(120)
    EnableFlag(11510900)
    KillBoss(1510650)
    DisableObject(1511890)
    DeleteVFX(1511891, erase_root_only=True)
    EndIfClient()
    DisableFlag(11807170)
    DisableFlag(11807180)
    DisableFlag(11807190)
    DisableFlag(11807230)
    AwardAchievement(39)


def Event11515384():
    """ 11515384: Event 11515384 """
    DisableNetworkSync()
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11515382)
    IfCharacterInsideRegion(1, PLAYER, region=1512890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1513802)


def Event11515385():
    """ 11515385: Event 11515385 """
    DisableNetworkSync()
    IfHealthLessThanOrEqual(1, 1510650, 0.0)
    IfFlagOn(1, 11515384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1513802)


@RestartOnRest
def Event11515386():
    """ 11515386: Event 11515386 """
    IfThisEventOn(1)
    IfFlagOn(1, 11510400)
    IfHost(1)
    IfThisEventOn(2)
    IfHost(2)
    IfPlayerCovenant(2, Covenant.DarkmoonBlade)
    IfThisEventOn(3)
    IfHost(3)
    IfConditionFalse(3, input_condition=1)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterType(-2, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-2, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-2)
    SkipLinesIfFinishedConditionFalse(10, 1)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150155, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150155, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(1)
    PlayCutscene(150155, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()
    SkipLinesIfFinishedConditionFalse(10, 2)
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150161, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150161, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(1)
    PlayCutscene(150161, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()
    SkipLinesIfUnknownPlayerType4(2)
    PlayCutscene(
        150160, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150160, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1512900, move_to_map=ANOR_LONDO
    )
    SkipLines(1)
    PlayCutscene(150160, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11515387)
    End()


def Event11515390():
    """ 11515390: Event 11515390 """
    IfFlagOff(1, 12)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1511990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11515391():
    """ 11515391: Event 11515391 """
    IfFlagOff(1, 12)
    IfFlagOn(1, 11515393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1511990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11515393():
    """ 11515393: Event 11515393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 12)
    IfCharacterInsideRegion(1, PLAYER, region=1512996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1510800)
    ActivateMultiplayerBuffs(1510801)
    ActivateMultiplayerBuffs(1510810)
    ActivateMultiplayerBuffs(1510811)


@RestartOnRest
def Event11515392():
    """ 11515392: Event 11515392 """
    SkipLinesIfFlagOff(9, 12)
    DisableCharacter(1510800)
    DisableCharacter(1510801)
    DisableCharacter(1510810)
    DisableCharacter(1510811)
    Kill(1510800, award_souls=False)
    Kill(1510801, award_souls=False)
    Kill(1510810, award_souls=False)
    Kill(1510811, award_souls=False)
    End()
    DisableCharacter(1510801)
    DisableCharacter(1510811)
    DisableBackread(1510801)
    SkipLinesIfFlagOn(1, 11510000)
    DisableCharacter(1510800)
    DisableAI(1510800)
    DisableAI(1510810)
    IfFlagOn(1, 11515393)
    IfCharacterInsideRegion(1, PLAYER, region=1512990)
    IfConditionTrue(0, input_condition=1)
    IfCharacterType(-1, PLAYER, CharacterType.BlackPhantom)
    IfCharacterType(-1, PLAYER, CharacterType.Intruder)
    EndIfConditionTrue(-1)
    SkipLinesIfFlagOn(8, 11510000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150140, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150140, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1510800)
    EnableCharacter(1510810)
    EnableFlag(11510000)
    EnableAI(1510800)
    EnableAI(1510810)
    EnableBossHealthBar(1510800, name=5270, slot=1)
    EnableBossHealthBar(1510810, name=2360, slot=0)


def Event11510001():
    """ 11510001: Event 11510001 """
    DisableObject(1511950)
    IfCharacterDead(1, 1510800)
    IfCharacterDead(2, 1510810)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(10, 1)
    IfCharacterDead(0, 1510801)
    EnableFlag(11510902)
    PlaySoundEffect(anchor_entity=1510801, sound_type=SoundType.s_SFX, sound_id=777777777)
    Kill(1510811, award_souls=False)
    KillBoss(1510801)
    DisableFlag(11807100)
    DisableFlag(11807110)
    DisableFlag(11807120)
    DisableFlag(11807130)
    SkipLines(9)
    IfCharacterDead(0, 1510811)
    EnableFlag(11510903)
    PlaySoundEffect(anchor_entity=1510811, sound_type=SoundType.s_SFX, sound_id=777777777)
    Kill(1510801, award_souls=False)
    KillBoss(1510811)
    DisableFlag(11807060)
    DisableFlag(11807070)
    DisableFlag(11807080)
    DisableFlag(11807090)
    EnableFlag(12)
    EnableFlag(120)
    DisableObject(1511990)
    DeleteVFX(1511991, erase_root_only=True)
    DisableObject(1511992)
    DeleteVFX(1511993, erase_root_only=True)
    DisableObject(1511988)
    DeleteVFX(1511989, erase_root_only=True)
    EnableObject(1511950)
    RegisterBonfire(11510920, obj=1511950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    DisableNetworkSync()
    Wait(3.0)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)


def Event11515394():
    """ 11515394: Event 11515394 """
    DisableNetworkSync()
    IfFlagOff(1, 12)
    IfFlagOn(1, 11515392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11515391)
    IfCharacterInsideRegion(1, PLAYER, region=1512990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1513800)
    EnableBackread(1510801)


def Event11515395():
    """ 11515395: Event 11515395 """
    DisableNetworkSync()
    IfFlagOn(1, 12)
    IfFlagOn(1, 11515394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1513800)


def Event11515396():
    """ 11515396: Event 11515396 """
    IfCharacterDead(1, 1510800)
    IfCharacterDead(2, 1510810)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(12, 2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150121, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150121, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(1510800)
    DisableCharacter(1510810)
    DisableImmortality(1510810)
    Kill(1510810, award_souls=False)
    EnableCharacter(1510811)
    EnableBossHealthBar(1510811, name=2360, slot=0)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150120, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150120, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(1510810)
    DisableCharacter(1510800)
    DisableImmortality(1510800)
    Kill(1510800, award_souls=False)
    EnableCharacter(1510801)
    EnableBossHealthBar(1510801, name=5270, slot=1)


def Event11515397():
    """ 11515397: Event 11515397 """
    IfHealthLessThanOrEqual(1, 1510800, 0.0)
    IfHealthLessThanOrEqual(2, 1510810, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableImmortality(1510810)
    End()
    EnableImmortality(1510800)


@RestartOnRest
def Event11515398():
    """ 11515398: Event 11515398 """
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
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(1510810, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(1510810, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, 1510810, 0.0)
    SetNPCPartHealth(1510810, npc_part_id=2360, desired_hp=0, overwrite_max=False)


@RestartOnRest
def Event11515399():
    """ 11515399: Event 11515399 """
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
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(1510811, npc_part_id=2360, desired_scaling=0.0)
    SetNPCPartEffects(1510811, npc_part_id=2360, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, 1510811, 0.0)
    SetNPCPartHealth(1510811, npc_part_id=2360, desired_hp=0, overwrite_max=False)


@RestartOnRest
def Event11515060(_, arg_0_3: int):
    """ 11515060: Event 11515060 """
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
        start_in_stop_state=False,
    )
    SetNPCPartBulletDamageScaling(arg_0_3, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(arg_0_3, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2870, desired_hp=0, overwrite_max=False)


@RestartOnRest
def Event11515080(_, arg_0_3: int, arg_4_7: int):
    """ 11515080: Event 11515080 """
    DisableCharacter(arg_4_7)
    SkipLinesIfThisEventSlotOff(5)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, 5434)
    AICommand(arg_0_3, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=5351,
        part_index=NPCPartType.Part1,
        part_health=65,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=5351, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
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


def Event11510100():
    """ 11510100: Event 11510100 """
    SkipLinesIfThisEventOff(8)
    PostDestruction(1511100, slot=1)
    PostDestruction(1511102, slot=1)
    EndOfAnimation(1511600, 111)
    EndOfAnimation(1511101, 0)
    EndOfAnimation(1511102, 1)
    EnableObjectInvulnerability(1511101)
    EnableTreasure(1511600)
    End()
    DisableTreasure(1511600)
    SkipLinesIfClient(1)
    CreateObjectVFX(99010, obj=1511600, model_point=90)
    ForceAnimation(1511600, 110, loop=True)
    IfObjectDestroyed(0, 1511100)
    ForceAnimation(1511600, 111)
    ForceAnimation(1511101, 0)
    ForceAnimation(1511102, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(1511600, erase_root=True)
    EnableTreasure(1511600)
    DestroyObject(1511102, slot=1)


def Event11510110():
    """ 11510110: Event 11510110 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1511010, 0)
    End()
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=1511010,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=255,
    )
    Move(PLAYER, destination=1511010, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1511010, 0)


def Event11510200():
    """ 11510200: Event 11510200 """
    SkipLinesIfThisEventOff(4)
    DisableObjectActivation(1511001, obj_act_id=-1)
    EndOfAnimation(1511000, 0)
    EndOfAnimation(1511001, 0)
    End()
    IfFlagOff(1, 11510700)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=255,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1511001, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511001, 0, wait_for_completion=True)
    ForceAnimation(1511000, 0)


def Event11510201():
    """ 11510201: Event 11510201 """
    DisableNetworkSync()
    IfFlagOff(1, 11510200)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1512000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1511000,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510210():
    """ 11510210: Event 11510210 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1511200, 0)
    End()
    EnableNavmeshType(1513200, NavmeshType.Solid)
    IfActionButton(
        0,
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=101,
        trigger_attribute=255,
    )
    Move(PLAYER, destination=1511200, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1511200, 0)
    DisableNavmeshType(1513200, NavmeshType.Solid)


def Event11510211():
    """ 11510211: Event 11510211 """
    DisableNetworkSync()
    IfFlagOff(1, 11510210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=100,
        trigger_attribute=255,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010161,
        anchor_entity=1511200,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510220():
    """ 11510220: Event 11510220 """
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(0, PLAYER, region=1512350)
    ForceAnimation(1511050, 0)


def Event11510260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11510260: Event 11510260 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, arg_0_3)
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


def Event11510710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510710: Event 11510710 """
    SkipLinesIfThisEventSlotOn(2)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_8_11)
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_4_7, 4150)
    Wait(3.0)
    Restart()


def Event11510300():
    """ 11510300: Event 11510300 """
    IfFlagOff(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=255,
    )
    IfFlagOff(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=255,
    )
    IfFlagOn(3, 11510305)
    IfFlagOff(3, 11510303)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOn(4, 11510305)
    IfFlagOn(4, 11510303)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOn(5, 11510305)
    IfFlagOff(5, 11510301)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOn(6, 11510305)
    IfFlagOff(6, 11510302)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
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
    SkipLinesIfFlagOn(20, 11510305)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10, wait_for_completion=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        cutscene_id=150100,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(4)
    SkipLinesIfFlagOff(2, 11510304)
    PlayCutscene(
        cutscene_id=150100,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(1)
    PlayCutscene(150100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(1511300, 0)
    DisableCollision(1513303)
    EnableCollision(1513302)
    DisableFlag(11510303)
    EnableFlag(11510302)
    DisableFlag(11510304)
    EnableFlag(11510305)
    DisableFlag(11515300)
    Restart()
    SkipLinesIfFlagOff(33, 11510303)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=0, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 4)
    Move(PLAYER, destination=1511302, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511302, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=1, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=0, args=(0, 1, 1513301, 11510303, 11510301, 11, 180, 360))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=2, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(32, 11510302)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=3, args=(1, 1513302, 1513301, 11510302, 11510301, 360))
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=4, args=(3, 1513302, 1513303, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=5, args=(3, 1513302, 1513303, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=6, args=(1, 1513302, 1513301, 11510302, 11510301, 360))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(25, 11510301)
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=7, args=(2, 1513301, 1513302, 11510301, 11510302, 360))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=1, args=(2, 3, 1513303, 11510301, 11510303, 13, 360, 180))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=8, args=(2, 1513301, 1513302, 11510301, 11510302, 360))
    IfFlagOff(0, 11515300)
    Restart()
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510319():
    """ 11510319: Event 11510319 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1512310)
    EnableFlag(11510304)
    IfCharacterOutsideRegion(0, PLAYER, region=1512310)
    DisableFlag(11510304)
    Restart()


def Event11515320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11515320: Event 11515320 """
    DisableCollision(arg_4_7)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(arg_20_23)
    IfTimeElapsed(0, 0.0)
    DisableObject(1511310)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11515330(
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
    """ 11515330: Event 11515330 """
    DisableCollision(1513301)
    DisableCollision(1513302)
    DisableCollision(1513303)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(arg_24_27)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(1511300, arg_20_23)
    WaitFrames(130)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(1511300, arg_4_7)
    ForceAnimation(1511310, arg_4_7)
    WaitFrames(arg_28_31)
    IfTimeElapsed(0, 0.0)
    DisableObject(1511310)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11510340():
    """ 11510340: Event 11510340 """
    SkipLinesIfFlagOff(8, 11515300)
    EnableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    EnableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510303)
    EnableCollision(1513310)
    DisableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    EnableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510302)
    DisableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    DisableNavmeshType(1513351, NavmeshType.Solid)
    DisableNavmeshType(1513352, NavmeshType.Solid)
    DisableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510301)
    EnableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    DisableNavmeshType(1513353, NavmeshType.Solid)
    DisableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    DisplayDialog(
        10010105,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11510350():
    """ 11510350: Event 11510350 """
    IfHost(1)
    IfFlagOn(1, 11515301)
    IfFlagOn(1, 11510301)
    IfHost(2)
    IfFlagOn(2, 11515301)
    IfFlagOn(2, 11510302)
    IfHost(3)
    IfFlagOn(3, 11515301)
    IfFlagOn(3, 11510303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11515301)
    RestartIfSingleplayer()
    SkipLinesIfFinishedConditionFalse(6, 1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 51)
    EnableCollision(1513301)
    Restart()
    SkipLinesIfFinishedConditionFalse(6, 2)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 50)
    EnableCollision(1513302)
    Restart()
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(1511300, 53)
    EnableCollision(1513303)
    Restart()


def Event11510310():
    """ 11510310: Event 11510310 """
    DisableNetworkSync()
    IfFlagOn(1, 11510301)
    IfActionButton(
        1,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=102,
        trigger_attribute=255,
    )
    IfFlagOn(2, 11510303)
    IfActionButton(
        2,
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=104,
        trigger_attribute=255,
    )
    IfFlagOff(-2, 11510305)
    IfFlagOn(-2, 11510303)
    IfConditionTrue(3, input_condition=-2)
    IfActionButton(
        3,
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOff(-3, 11510305)
    IfFlagOff(-3, 11510303)
    IfConditionTrue(4, input_condition=-3)
    IfActionButton(
        4,
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOff(-4, 11510305)
    IfFlagOn(-4, 11510301)
    IfConditionTrue(5, input_condition=-4)
    IfActionButton(
        5,
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOff(-5, 11510305)
    IfFlagOn(-5, 11510302)
    IfConditionTrue(6, input_condition=-5)
    IfActionButton(
        6,
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        model_point=192,
        trigger_attribute=255,
    )
    IfFlagOn(7, 11515300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 7)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    IfFlagOff(0, 11515300)
    Restart()


def Event11510400():
    """ 11510400: Event 11510400 """
    DisableMapPiece(1513401)
    SkipLinesIfThisEventOff(7)
    DisableSoundEvent(1513801)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(1511400)
    End()
    EnableCharacter(1510600)
    IfCharacterDead(1, 1510600)
    IfEntityWithinDistance(1, 1510600, PLAYER, radius=15.0)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DisableSoundEvent(1513801)
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
    SkipLinesIfFlagOn(2, 11510900)
    PlayCutscene(150110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150111, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(1511400)
    IfPlayerHasGood(2, 2510, including_box=False)
    EndIfConditionTrue(2)
    AwardItemLot(1090, host_only=True)


def Event11510401():
    """ 11510401: Event 11510401 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1511400)
    End()
    EnableObjectInvulnerability(1511400)
    IfFlagOn(1, 11510400)
    IfEntityWithinDistance(1, 1511400, PLAYER, radius=15.0)
    IfHost(2)
    IfCharacterHasSpecialEffect(2, PLAYER, 2310)
    IfEntityWithinDistance(2, 1511400, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(1511400)
    DestroyObject(1511400, slot=1)
    ForceAnimation(1511400, 0)
    PlaySoundEffect(anchor_entity=1511400, sound_type=SoundType.o_Object, sound_id=590000000)


@RestartOnRest
def Event11510450():
    """ 11510450: Event 11510450 """
    IfDoesNotHaveTAEEvent(0, 1510650, tae_event_id=600)
    IfHasTAEEvent(0, 1510650, tae_event_id=600)
    DisableCharacter(1510650)
    Wait(1.0)
    SkipLinesIfFlagOn(2, 11515110)
    RunEvent(11515110, slot=0, args=(1512710, 11515110))
    Restart()
    SkipLinesIfFlagOn(2, 11515111)
    RunEvent(11515110, slot=1, args=(1512711, 11515111))
    Restart()
    SkipLinesIfFlagOn(2, 11515112)
    RunEvent(11515110, slot=2, args=(1512712, 11515112))
    Restart()
    SkipLinesIfFlagOn(2, 11515113)
    RunEvent(11515110, slot=3, args=(1512713, 11515113))
    Restart()
    SkipLinesIfFlagOn(2, 11515114)
    RunEvent(11515110, slot=4, args=(1512714, 11515114))
    Restart()
    SkipLinesIfFlagOn(2, 11515115)
    RunEvent(11515110, slot=5, args=(1512715, 11515115))
    Restart()
    SkipLinesIfFlagOn(2, 11515116)
    RunEvent(11515110, slot=6, args=(1512716, 11515116))
    Restart()
    SkipLinesIfFlagOn(2, 11515117)
    RunEvent(11515110, slot=7, args=(1512717, 11515117))
    Restart()
    SkipLinesIfFlagOn(2, 11515118)
    RunEvent(11515110, slot=8, args=(1512718, 11515118))
    Restart()
    SkipLinesIfFlagOn(2, 11515119)
    RunEvent(11515110, slot=9, args=(1512719, 11515119))
    Restart()
    SkipLinesIfFlagOn(2, 11515120)
    RunEvent(11515110, slot=10, args=(1512720, 11515120))
    Restart()
    SkipLinesIfFlagOn(2, 11515121)
    RunEvent(11515110, slot=11, args=(1512721, 11515121))
    Restart()
    SkipLinesIfFlagOn(2, 11515122)
    RunEvent(11515110, slot=12, args=(1512722, 11515122))
    Restart()
    SkipLinesIfFlagOn(2, 11515123)
    RunEvent(11515110, slot=13, args=(1512723, 11515123))
    Restart()
    SkipLinesIfFlagOn(2, 11515124)
    RunEvent(11515110, slot=14, args=(1512724, 11515124))
    Restart()
    SkipLinesIfFlagOn(2, 11515125)
    RunEvent(11515110, slot=15, args=(1512725, 11515125))
    Restart()
    SkipLinesIfFlagOn(2, 11515126)
    RunEvent(11515110, slot=16, args=(1512726, 11515126))
    Restart()
    SkipLinesIfFlagOn(2, 11515127)
    RunEvent(11515110, slot=17, args=(1512727, 11515127))
    Restart()
    SkipLinesIfFlagOn(2, 11515128)
    RunEvent(11515110, slot=18, args=(1512728, 11515128))
    Restart()
    SkipLinesIfFlagOn(2, 11515129)
    RunEvent(11515110, slot=19, args=(1512729, 11515129))
    Restart()
    SkipLinesIfFlagOn(2, 11515130)
    RunEvent(11515110, slot=20, args=(1512730, 11515130))
    Restart()
    SkipLinesIfFlagOn(2, 11515131)
    RunEvent(11515110, slot=21, args=(1512731, 11515131))
    Restart()
    SkipLinesIfFlagOn(2, 11515132)
    RunEvent(11515110, slot=22, args=(1512732, 11515132))
    Restart()
    SkipLinesIfFlagOn(2, 11515133)
    RunEvent(11515110, slot=23, args=(1512733, 11515133))
    Restart()
    SkipLinesIfFlagOn(2, 11515134)
    RunEvent(11515110, slot=24, args=(1512734, 11515134))
    Restart()
    SkipLinesIfFlagOn(2, 11515135)
    RunEvent(11515110, slot=25, args=(1512735, 11515135))
    Restart()
    SkipLinesIfFlagOn(2, 11515136)
    RunEvent(11515110, slot=26, args=(1512736, 11515136))
    Restart()
    SkipLinesIfFlagOn(2, 11515137)
    RunEvent(11515110, slot=27, args=(1512737, 11515137))
    Restart()
    SkipLinesIfFlagOn(2, 11515138)
    RunEvent(11515110, slot=28, args=(1512738, 11515138))
    Restart()
    SkipLinesIfFlagOn(2, 11515139)
    RunEvent(11515110, slot=29, args=(1512739, 11515139))
    Restart()


@UnknownRestart
def Event11515110(_, arg_0_3: int, arg_4_7: int):
    """ 11515110: Event 11515110 """
    Move(1510650, destination=arg_0_3, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableCharacter(1510650)
    ReplanAI(1510650)
    ForceAnimation(1510650, 7000, wait_for_completion=True)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOff(2, 11515132)
    AICommand(1510650, command_id=1, slot=0)
    ReplanAI(1510650)


def Event11510230():
    """ 11510230: Event 11510230 """
    IfActionButton(0, prompt_text=10010100, anchor_entity=1512510, anchor_type=CoordEntityType.Region)
    IfSingleplayer(1)
    IfHost(1)
    IfPlayerHasGood(1, 384, including_box=False)
    SkipLinesIfConditionTrue(3, 1)
    SkipLinesIfClient(1)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    PlayCutscene(
        150135, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1102510, move_to_map=PAINTED_WORLD
    )
    WaitFrames(1)
    SetRespawnPoint(1102511)
    SaveRequest()
    Restart()


def Event11510240():
    """ 11510240: Event 11510240 """
    EndIfClient()
    IfInsideMap(0, game_map=ANOR_LONDO)
    IfTimeElapsed(0, 5.0)
    IfFlagOff(2, 11515050)
    IfActionButton(
        2, prompt_text=10010200, anchor_entity=1510100, anchor_type=CoordEntityType.Character, max_distance=7.0
    )
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfSingleplayer(2)
    DisplayDialog(
        10010170,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()
    SkipLinesIfFlagOn(2, 11510400)
    PlayCutscene(
        150130, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1502500, move_to_map=SENS_FORTRESS
    )
    SkipLines(1)
    PlayCutscene(
        150132, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1502500, move_to_map=SENS_FORTRESS
    )
    WaitFrames(1)
    SetMapDrawParamSlot(15, slot=0)
    Restart()


def Event11515050():
    """ 11515050: Event 11515050 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1510100)
    End()
    DisableImmortality(1510100)
    SetStandbyAnimationSettings(1510100, standby_animation=9000)
    IfAttacked(-1, 1510100, attacking_character=PLAYER)
    IfFlagOn(-1, 11515050)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11515050)
    ResetAnimation(1510100, disable_interpolation=True)
    ForceAnimation(1510100, 9060, wait_for_completion=True)
    DisableCharacter(1510100)


def Event11510120():
    """ 11510120: Event 11510120 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 743)
    IfFlagOn(1, 12)
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11510400)
    IfCharacterInsideRegion(-1, PLAYER, region=1512400)
    IfStandingOnCollision(-1, 1513405)
    IfStandingOnCollision(-1, 1513100)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event11510130():
    """ 11510130: Event 11510130 """
    SkipLinesIfFlagOn(5, 11510400)
    DisableCharacter(6640)
    DisableCharacter(6650)
    IfFlagOn(0, 11510400)
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
    EndIfFlagOn(1034)
    Move(6010, destination=1512450, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=1510452)
    SetNest(6010, 1512450)
    ResetStandbyAnimationSettings(6010)


def Event11510131():
    """ 11510131: Event 11510131 """
    EndIfClient()
    IfFlagOn(1, 11510400)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(1512960)
    SaveRequest()


def Event11510140():
    """ 11510140: Event 11510140 """
    IfFlagOn(0, 11510900)
    MoveRemains(source_region=1512420, destination_region=1512421)


def Event11510150():
    """ 11510150: Event 11510150 """
    DisableNetworkSync()
    IfHost(1)
    IfPlayerHasGood(1, 115, including_box=False)
    IfCharacterInsideRegion(1, PLAYER, region=1512101)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11510460():
    """ 11510460: Event 11510460 """
    IfFlagOn(-7, 11510593)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOff(1, 11515352)
    IfFlagOff(1, 11515350)
    IfFlagOff(1, 743)
    IfFlagOn(1, 1240)
    IfActionButton(1, prompt_text=10010210, anchor_entity=1512410, anchor_type=CoordEntityType.Region)
    IfConditionTrue(2, input_condition=-7)
    IfFlagOn(2, 11515352)
    IfFlagOff(2, 11515350)
    IfConditionTrue(3, input_condition=-7)
    IfFlagOn(3, 11515352)
    IfFlagOn(3, 11515350)
    IfHost(3)
    IfCharacterOutsideRegion(3, PLAYER, region=1512411)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(10, 1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, 1512897)
    EnableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11515352)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    DisableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11515352)
    Restart()


def Event11510462():
    """ 11510462: Event 11510462 """
    DisableNetworkSync()
    WaitFrames(2)
    EnableFlag(11510460)


@RestartOnRest
def Event11510860(_, arg_0_3: int, arg_4_7: int):
    """ 11510860: Event 11510860 """
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


def Event11510461():
    """ 11510461: Event 11510461 """
    IfFlagOn(0, 11515351)
    AddSpecialEffect(PLAYER, 4170)
    RotateToFaceEntity(PLAYER, 1510600)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    IfFlagOff(0, 11515351)
    CancelSpecialEffect(PLAYER, 4170)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    Restart()


def Event11510600(_, arg_0_3: int, arg_4_7: int):
    """ 11510600: Event 11510600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11515200(_, arg_0_3: int):
    """ 11515200: Event 11515200 """
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=arg_0_3,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=255,
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


@RestartOnRest
def Event11515210(_, arg_0_3: int):
    """ 11515210: Event 11515210 """
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 5420)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
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


@RestartOnRest
def Event11515220(_, arg_0_3: int):
    """ 11515220: Event 11515220 """
    IfCharacterHasSpecialEffect(1, arg_0_3, 5421)
    IfCharacterHasSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5420)
    IfCharacterHasSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
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


@RestartOnRest
def Event11515230(_, arg_0_3: int):
    """ 11515230: Event 11515230 """
    IfCharacterHasSpecialEffect(1, arg_0_3, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 3150)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(arg_0_3, 3150)
    CancelSpecialEffect(arg_0_3, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
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


@RestartOnRest
def Event11515240(_, arg_0_3: int, arg_4_7: int):
    """ 11515240: Event 11515240 """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, 5421)
    ClearTargetList(arg_0_3)
    ReplanAI(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Restart()


@RestartOnRest
def Event11510850(_, arg_0_3: int):
    """ 11510850: Event 11510850 """
    SkipLinesIfThisEventSlotOff(2)
    DisableCharacter(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event11515190(_, arg_0_3: int):
    """ 11515190: Event 11515190 """
    EndIfHost()
    IfCharacterBackreadDisabled(1, arg_0_3)
    EndIfConditionTrue(1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11515250():
    """ 11515250: Event 11515250 """
    EndIfThisEventOn()
    DisableAI(1510310)
    IfCharacterInsideRegion(1, PLAYER, region=1512050)
    IfAttacked(2, 1510310, attacking_character=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(1510310, 500)
    EnableAI(1510310)


@RestartOnRest
def Event11515251():
    """ 11515251: Event 11515251 """
    EndIfThisEventOn()
    DisableAI(1510305)
    IfCharacterInsideRegion(-1, PLAYER, region=1512060)
    IfAttacked(-1, 1510305, attacking_character=PLAYER)
    IfEntityWithinDistance(-1, 1510305, PLAYER, radius=4.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1510305)


def Event11510215():
    """ 11510215: Event 11510215 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1511210)
    End()
    IfObjectDestroyed(0, 1511210)
    End()


def Event11510510(_, arg_0_3: int, arg_4_7: int):
    """ 11510510: Event 11510510 """
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


def Event11510520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510520: Event 11510520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510501(_, arg_0_3: int, arg_4_7: int):
    """ 11510501: Event 11510501 """
    IfFlagOn(-2, 1030)
    IfFlagOn(-2, 1031)
    IfFlagOn(-2, 1036)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfThisEventOff(1)
    IfFlagOff(2, 1034)
    IfFlagOn(-3, 1232)
    IfFlagOn(-3, 1241)
    IfFlagOn(-3, 1242)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterBackreadEnabled(2, arg_0_3)
    IfThisEventOff(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11510502(_, arg_0_3: int, arg_4_7: int):
    """ 11510502: Event 11510502 """
    IfFlagOn(1, 1240)
    IfFlagOn(-2, 1232)
    IfFlagOn(-2, 11515382)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterAlive(1, arg_0_3)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.Boss)


def Event11510530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510530: Event 11510530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1001)
    IfFlagOn(1, 11010590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11510531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510531: Event 11510531 """
    IfFlagOff(1, 1033)
    IfFlagOn(1, 1030)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510532: Event 11510532 """
    IfFlagOff(1, 1033)
    IfFlagOn(-1, 1030)
    IfFlagOn(-1, 1036)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 711)
    IfFlagOn(1, 712)
    IfFlagOn(1, 713)
    IfFlagOn(1, 714)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11510533(_, arg_0_3: int):
    """ 11510533: Event 11510533 """
    EndIfThisEventOn()
    IfCharacterDead(0, arg_0_3)
    EnableFlag(151)


def Event11510535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510535: Event 11510535 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1493)
    IfCharacterDead(1, 1510300)
    IfCharacterDead(1, 1510301)
    IfCharacterDead(1, 1510302)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11510536(_, arg_0_3: int):
    """ 11510536: Event 11510536 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1494)
    IfFlagOn(1, 11510590)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11510541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510541: Event 11510541 """
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11510700)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetTeamType(6490, TeamType.WhitePhantom)
    SetTeamType(6500, TeamType.WhitePhantom)
    DisableAI(arg_0_3)
    DisableAI(6490)
    DisableAI(6500)
    IfFlagOn(-1, 11510598)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfAttacked(-1, 6490, attacking_character=PLAYER)
    IfAttacked(-1, 6500, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    EnableAI(6490)
    EnableAI(6500)


def Event11510542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510542: Event 11510542 """
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(8102)


def Event11510543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510543: Event 11510543 """
    DisableObject(1511750)
    DeleteVFX(1511751, erase_root_only=False)
    DisableObject(1511752)
    DeleteVFX(1511753, erase_root_only=False)
    DisableObject(1511754)
    DeleteVFX(1511755, erase_root_only=False)
    IfFlagOn(0, 11510700)
    EnableObject(1511750)
    CreateVFX(1511751)
    EnableObject(1511752)
    CreateVFX(1511753)
    EnableObject(1511754)
    CreateVFX(1511755)
    DisableFlag(8104)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(1510412)
    DisableCharacter(1510413)
    DisableCharacter(1510500)
    EnableCharacter(arg_0_3)
    EnableCharacter(6490)
    EnableCharacter(6500)
    SkipLinesIfFlagOn(2, 8101)
    EnableFlag(8101)
    End()
    EnableFlag(8100)


def Event11510544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11510544: Event 11510544 """
    SkipLinesIfThisEventOff(2)
    EnableTreasure(1511601)
    End()
    DisableObject(1511601)
    DisableTreasure(1511601)
    IfHost(1)
    IfFlagOff(1, 11510700)
    IfFlagOn(1, 8102)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    SkipLinesIfConditionFalse(3, -1)
    AwardItemLot(2060, host_only=True)
    AwardItemLot(6300, host_only=True)
    RemoveGoodFromPlayer(115)
    EnableObject(1511601)
    EnableTreasure(1511601)
    DisableCharacter(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event151():
    """ 151: Event 151 """
    DisableNetworkSync()
    IfThisEventOn(1)
    IfActionButton(
        1,
        prompt_text=10010182,
        anchor_entity=1511960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
    )
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010184,
        anchor_entity=1511960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11515090(_, arg_0_3: int):
    """ 11515090: Event 11515090 """
    IfHasTAEEvent(0, arg_0_3, tae_event_id=500)
    EzstateAIRequest(arg_0_3, command_id=1500, slot=0)
    IfDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=500)
    Restart()


@RestartOnRest
def Event11515091(_, arg_0_3: int):
    """ 11515091: Event 11515091 """
    DisableNetworkSync()
    IfHasTAEEvent(0, arg_0_3, tae_event_id=1400)
    Wait(10.0)
    EzstateAIRequest(arg_0_3, command_id=1501, slot=0)
    Restart()


@RestartOnRest
def Event11515092(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11515092: Event 11515092 """
    EndIfFlagOn(arg_8_11)
    EndIfFlagOn(arg_12_15)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    EnableObjectInvulnerability(arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfFlagOn(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    DisableObjectInvulnerability(arg_4_7)
    WaitFrames(1)
    DestroyObject(arg_4_7, slot=1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=596500000)


def Event11515030():
    """ 11515030: Event 11515030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6543, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6003)
    SkipLinesIfFlagOn(3, 11515034)
    IfClient(2)
    IfFlagOn(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6543)
    EndIfFlagOn(12)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6543)
    IfEntityWithinDistance(1, 6543, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6543, region=1512001, summon_flag=11515031, dismissal_flag=11515034)
    DisableCharacter(6003)
    IfFlagOn(0, 11515031)
    SetNest(6543, 1512002)


def Event11515990(_, arg_0_3: int, arg_4_7: int):
    """ 11515990: Event 11515990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11515029():
    """ 11515029: Event 11515029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6543, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6003)
    SkipLinesIfFlagOn(3, 11515034)
    IfClient(2)
    IfFlagOn(2, 11515031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6543)
    EndIfFlagOn(12)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11515031)
    IfFlagOff(1, 11515034)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6543)
    IfEntityWithinDistance(1, 6543, PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6543, region=1512001, summon_flag=11515031, dismissal_flag=11515034)
    DisableCharacter(6003)
    IfFlagOn(0, 11515031)
    SetNest(6543, 1512002)


def Event11515032():
    """ 11515032: Event 11515032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11515031)
    IfFlagOn(1, 11515393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6543, command_id=10, slot=0)
    ReplanAI(6543)
    IfCharacterInsideRegion(0, 6543, region=1512998)
    RotateToFaceEntity(6543, 1512997)
    ForceAnimation(6543, 7410)
    AICommand(6543, command_id=-1, slot=0)
    ReplanAI(6543)


def Event11515033():
    """ 11515033: Event 11515033 """
    IfFlagOn(1, 11515031)
    IfFlagOff(1, 11515390)
    IfCharacterInsideRegion(1, PLAYER, region=1512801)
    IfConditionTrue(0, input_condition=1)
    AICommand(6543, command_id=8, slot=0)
    ReplanAI(6543)
    IfAllPlayersOutsideRegion(0, region=1512801)
    AICommand(6543, command_id=-1, slot=0)
    ReplanAI(6543)
    Restart()


def Event11515843(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11515843: Event 11515843 """
    IfFlagOn(1, 120)
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


def Event11515846(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11515846: Event 11515846 """
    IfFlagOn(1, 120)
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
