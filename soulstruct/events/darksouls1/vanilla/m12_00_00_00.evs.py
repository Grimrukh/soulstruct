"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11200984, obj=1201961, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=1201140)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=1201141)
    CreateSpawner(1200090)
    SkipLinesIfFlagOn(2, 11200000)
    SkipLinesIfFlagOn(1, 11200002)
    SkipLines(1)
    DisableObject(1201200)
    SkipLinesIfClient(10)
    DisableObject(1201994)
    DeleteFX(1201995, erase_root_only=False)
    DisableObject(1201996)
    DeleteFX(1201997, erase_root_only=False)
    DisableObject(1201998)
    DeleteFX(1201999, erase_root_only=False)
    DisableObject(1201988)
    DeleteFX(1201989, erase_root_only=False)
    DisableObject(1201986)
    DeleteFX(1201987, erase_root_only=False)
    RunEvent(11200090, slot=0, args=(1201700, 1201701, 1202600, 1202601))
    RunEvent(11205080)
    RunEvent(11205081)
    RunEvent(11205082)
    RunEvent(11200100, slot=0, args=(11200110, 1201000, 120020, 1202500, 0, 61200500))
    RunEvent(11200110, slot=0, args=(11200100, 1201000, 1202500, 0))
    RunEvent(11200100, slot=1, args=(11200111, 1201010, 120021, 1202501, 1, 61200501))
    RunEvent(11200110, slot=1, args=(11200101, 1201010, 1202501, 1))
    RunEvent(11200120)
    RunEvent(11205000)
    RunEvent(11200800)
    RunEvent(11200200)
    RunEvent(11200690)
    RunEvent(11200600, slot=0, args=(1201650, 11200600))
    RunEvent(11200600, slot=1, args=(1201651, 11200601))
    DisableMapSound(1203800)
    SkipLinesIfFlagOff(4, 5)
    RunEvent(11205392)
    DisableObject(1201990)
    DeleteFX(1201991, erase_root_only=False)
    SkipLines(9)
    RunEvent(11200000)
    RunEvent(11205390)
    RunEvent(11205391)
    RunEvent(11205393)
    RunEvent(11205392)
    RunEvent(11200001)
    RunEvent(11205394)
    RunEvent(11205395)
    RunEvent(11205396)
    RunEvent(11200002)
    DisableMapSound(1203801)
    SkipLinesIfFlagOff(6, 11200900)
    RunEvent(11205382)
    DisableObject(1201890)
    DeleteFX(1201891, erase_root_only=False)
    DisableObject(1201892)
    DeleteFX(1201893, erase_root_only=False)
    SkipLines(17)
    RunEvent(11205380)
    RunEvent(11205381)
    RunEvent(11205383)
    RunEvent(11205382)
    RunEvent(11200900)
    RunEvent(11205384)
    RunEvent(11205385)
    RunEvent(11205120, slot=0, args=(1202220, 1202180))
    RunEvent(11205120, slot=1, args=(1202221, 1202181))
    RunEvent(11205120, slot=2, args=(1202222, 1202182))
    RunEvent(11205120, slot=3, args=(1202223, 1202183))
    RunEvent(11205120, slot=4, args=(1202224, 1202184))
    RunEvent(11205120, slot=5, args=(1202225, 1202185))
    RunEvent(11205120, slot=6, args=(1202226, 1202186))
    RunEvent(11205120, slot=7, args=(1202227, 1202187))
    RunEvent(11205120, slot=8, args=(1202228, 1202188))
    RunEvent(11205120, slot=9, args=(1202229, 1202189))
    RunEvent(11200801)
    RunEvent(11205300, slot=0, args=(1, 3530, 3530, 1200011, 91, 0, 1, 5430), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=1, args=(2, 3531, 3531, 1200012, 92, 1, 2, 5431), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=2, args=(3, 3532, 3532, 1200013, 93, 2, 3, 5432), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=3, args=(4, 3533, 3533, 1200014, 94, 3, 4, 5433), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=4, args=(5, 3534, 3534, 1200015, 95, 4, 5, 5434), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=5, args=(6, 3535, 3535, 1200016, 96, 5, 6, 5435), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=6, args=(8, 3536, 3536, 1200017, 97, 6, 7, 5436), arg_types='hhiiiBBi')
    RunEvent(11205250, slot=0, args=(1200100, 1202110))
    RunEvent(11205290, slot=0, args=(1200101, 51200170, 0.0, 1), arg_types='iifi')
    RunEvent(11205290, slot=1, args=(1200102, 51200170, 0.20000000298023224, 1), arg_types='iifi')
    RunEvent(11205290, slot=2, args=(1200103, 51200170, 0.800000011920929, 1), arg_types='iifi')
    RunEvent(11205250, slot=1, args=(1200104, 1202111))
    RunEvent(11205290, slot=3, args=(1200105, 11205263, 0.0, 0), arg_types='iifi')
    RunEvent(11205290, slot=4, args=(1200106, 11205263, 0.6000000238418579, 0), arg_types='iifi')
    RunEvent(11205290, slot=5, args=(1200107, 11205264, 0.0, 0), arg_types='iifi')
    RunEvent(11205290, slot=6, args=(1200108, 11205264, 0.8999999761581421, 0), arg_types='iifi')
    RunEvent(11205200, slot=0, args=(1200109, 8.0), arg_types='if')
    RunEvent(11205200, slot=1, args=(1200110, 8.0), arg_types='if')
    RunEvent(11205200, slot=2, args=(1200111, 5.0), arg_types='if')
    RunEvent(11205200, slot=3, args=(1200112, 5.0), arg_types='if')
    RunEvent(11205200, slot=4, args=(1200113, 5.0), arg_types='if')
    RunEvent(11205230, slot=0, args=(1200600, 3.0), arg_types='if')
    RunEvent(11205230, slot=2, args=(1200602, 3.0), arg_types='if')
    RunEvent(11205240, slot=0, args=(1200600, 1202710))
    RunEvent(11205240, slot=2, args=(1200602, 1202712))
    RunEvent(11205280, slot=0, args=(1200650, 6.0, 1202112), arg_types='ifi')
    RunEvent(11205280, slot=1, args=(1200651, 2.0, 1202112), arg_types='ifi')
    RunEvent(11205260, slot=0, args=(1200652, 6.0), arg_types='if')
    RunEvent(11205260, slot=1, args=(1200653, 10.0), arg_types='if')
    RunEvent(11205260, slot=2, args=(1200654, 8.0), arg_types='if')
    RunEvent(11205260, slot=3, args=(1200655, 4.0), arg_types='if')
    RunEvent(11205260, slot=4, args=(1200656, 4.0), arg_types='if')
    RunEvent(11205190, slot=0, args=(1200250, 1202113, 0.0), arg_types='iif')
    RunEvent(11205190, slot=1, args=(1200251, 1202113, 0.5), arg_types='iif')
    RunEvent(11205190, slot=2, args=(1200252, 1202113, 1.2000000476837158), arg_types='iif')
    RunEvent(11205190, slot=3, args=(1200253, 1202113, 0.699999988079071), arg_types='iif')
    RunEvent(11205150, slot=0, args=(1200705,))
    RunEvent(11205150, slot=1, args=(1200706,))
    RunEvent(11205150, slot=2, args=(1200707,))
    RunEvent(11205150, slot=3, args=(1200708,))
    RunEvent(11205150, slot=4, args=(1200709,))
    RunEvent(11205150, slot=5, args=(1200710,))
    RunEvent(11205150, slot=6, args=(1200711,))
    RunEvent(11205150, slot=7, args=(1200712,))
    RunEvent(11205180, slot=0, args=(1200350, 1))
    RunEvent(11205180, slot=1, args=(1200351, 0))
    RunEvent(11205180, slot=2, args=(1200352, 0))
    RunEvent(11200810, slot=0, args=(1200000, 0, 0))
    RunEvent(11200810, slot=1, args=(1200001, 0, 0))
    RunEvent(11200810, slot=2, args=(1200400, 0, 33004000))
    RunEvent(11200810, slot=3, args=(1200350, 0, 0))
    RunEvent(11200810, slot=4, args=(1200351, 0, 0))
    RunEvent(11200810, slot=5, args=(1200352, 0, 0))
    RunEvent(11200810, slot=6, args=(1200750, 0, 27901000))
    RunEvent(11200810, slot=7, args=(1200301, 0, 0))
    RunEvent(11200810, slot=8, args=(1200304, 1, 0))
    RunEvent(11200810, slot=9, args=(1200306, 0, 0))


def Preconstructor():
    """ 50: Event 50 """
    HumanityRegistration(6521, 8932)
    RunEvent(11205030)
    RunEvent(11205032)
    RunEvent(11200300)
    SkipLinesIfClient(2)
    DisableFlagRange((11200210, 11200213))
    DisableFlag(11200215)
    HumanityRegistration(6050, 8350)
    HumanityRegistration(6051, 8350)
    SkipLinesIfClient(6)
    SkipLinesIfFlagOff(2, 1123)
    DisableFlagRange((1120, 1139))
    EnableFlag(1122)
    SkipLinesIfFlagOff(2, 1130)
    DisableFlagRange((1120, 1139))
    EnableFlag(1129)
    SkipLinesIfFlagOn(1, 1121)
    DisableCharacter(6050)
    SkipLinesIfFlagOn(1, 1123)
    DisableCharacter(6051)
    SkipLinesIfFlagOn(1, 1130)
    DisableCharacter(6051)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    RunEvent(11200520, slot=0, args=(6050, 1120, 1139, 1125))
    RunEvent(11200520, slot=1, args=(6051, 1120, 1139, 1125))
    RunEvent(11200530, slot=0, args=(6050, 1120, 1139, 1121))
    RunEvent(11200531, slot=0, args=(6050, 1120, 1139, 1122))
    RunEvent(11200534, slot=0, args=(6050, 1120, 1139, 1123))
    RunEvent(11200532, slot=0, args=(6050, 1120, 1139, 1126))
    RunEvent(11200533)
    RunEvent(11205040, slot=0, args=(11200210, 1202000, 1203100))
    RunEvent(11205040, slot=1, args=(11200211, 1202001, 1203101))
    RunEvent(11205040, slot=2, args=(11200212, 1202002, 1203102))
    RunEvent(11205040, slot=3, args=(11200213, 1202003, 1203103))
    RunEvent(11200529, slot=0, args=(1120, 1139, 1127))
    RunEvent(11200527, slot=0, args=(6050, 1120, 1139, 1129))
    RunEvent(11200525, slot=0, args=(6050, 1120, 1139, 1130))
    RunEvent(11205070, slot=0, args=(11200210, 1202000, 1203100))
    RunEvent(11205070, slot=1, args=(11200211, 1202001, 1203101))
    RunEvent(11205070, slot=2, args=(11200212, 1202002, 1203102))
    RunEvent(11205070, slot=3, args=(11200213, 1202003, 1203103))
    DeleteFX(1202009, erase_root_only=False)
    RunEvent(11200005)
    RunEvent(11200006)
    SkipLinesIfClient(1)
    DisableFlagRange((11205050, 11205068))
    DisableCharacterCollision(6380)
    DisableGravity(6380)
    EnableImmortality(6380)
    SkipLinesIfFlagOn(2, 1710)
    SkipLinesIfFlagOn(1, 1712)
    DisableCharacter(6380)
    RunEvent(11200538, slot=0, args=(6380, 1710, 1712, 1711))
    RunEvent(11200539, slot=0, args=(6380, 1710, 1712, 1712))
    RunEvent(11200540, slot=0, args=(6380, 1710, 1712, 1711))
    RunEvent(11205058)
    RunEvent(11205054)
    RunEvent(11205056)
    RunEvent(11205057)
    RunEvent(11205060, slot=0, args=(6310,))
    RunEvent(11205060, slot=1, args=(6420,))
    RunEvent(11205060, slot=2, args=(1200300,))
    RunEvent(11205060, slot=3, args=(1200301,))
    RunEvent(11205060, slot=4, args=(1200302,))
    RunEvent(11205060, slot=5, args=(1200303,))
    RunEvent(11205060, slot=6, args=(1200304,))
    RunEvent(11205060, slot=7, args=(1200305,))
    RunEvent(11205060, slot=8, args=(1200306,))
    HumanityRegistration(6310, 8470)
    HumanityRegistration(6420, 8900)
    DisableCharacter(6310)
    DisableCharacter(6420)
    RunEvent(11200520, slot=2, args=(6310, 1600, 1619, 1604))
    RunEvent(11200520, slot=3, args=(6420, 1760, 1769, 1764))
    RunEvent(11200501, slot=0, args=(6310, 1603))
    RunEvent(11200535, slot=0, args=(6310,))


def Event11200090(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200090: Event 11200090 """
    SkipLinesIfThisEventSlotOff(3)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=False)
    End()
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, 
                            line_intersects=arg_0_3)
    IfDialogPromptActivated(2, prompt_text=10010407, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True, 
                            line_intersects=arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=arg_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def Event11205080():
    """ 11205080: Event 11205080 """
    EndIfThisEventOn()
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
    IfFlagOn(0, 11200050)
    EndIfFlagOn(735)
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


@RestartOnRest
def Event11205081():
    """ 11205081: Event 11205081 """
    IfFlagOn(-1, 11205085)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11200050)
    DisableFlag(11205085)
    EnableFlag(5001)
    Kill(1200900, award_souls=False)
    Kill(1200901, award_souls=False)
    Kill(1200902, award_souls=False)
    Kill(1200903, award_souls=False)
    Kill(1200904, award_souls=False)
    Kill(1200905, award_souls=False)
    Kill(1200906, award_souls=False)
    Kill(1200907, award_souls=False)
    Kill(1200908, award_souls=False)
    Kill(1200909, award_souls=False)


@RestartOnRest
def Event11205082():
    """ 11205082: Event 11205082 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11200050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11200050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11200050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11200050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11200050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=DARKROOT_GARDEN)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11200050)
    RestartIfConditionFalse(-6)
    EnableFlag(11200050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=DARKROOT_GARDEN)
    RestartIfConditionFalse(7)
    DisableFlag(11200050)
    EnableFlag(11205085)


@RestartOnRest
def Event11200000():
    """ 11200000: Event 11200000 """
    EndIfThisEventOn()
    EndIfFlagOn(11200002)
    DisableCharacter(1200800)
    DisableObject(1201990)
    DeleteFX(1201991, erase_root_only=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=1202999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120000, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1202801, 
                 move_to_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1202801, 
                 move_to_map=DARKROOT_GARDEN)
    SkipLines(1)
    PlayCutscene(120000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(1201200)
    Move(1200800, destination=1202800, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateFX(1201991)
    EnableFlag(11200002)


def Event11200002():
    """ 11200002: Event 11200002 """
    EndIfThisEventOn()
    EndIfFlagOn(11200000)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11210021)
    IfCharacterInsideRegion(1, PLAYER, region=1202999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120003, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1202802, 
                 move_to_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120003, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1202802, 
                 move_to_map=DARKROOT_GARDEN)
    SkipLines(1)
    PlayCutscene(120003, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(1201200)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateFX(1201991)
    EnableFlag(11200000)


def Event11205390():
    """ 11205390: Event 11205390 """
    IfFlagOff(1, 5)
    IfFlagOn(1, 11200000)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202998, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1201990, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205391():
    """ 11205391: Event 11205391 """
    IfFlagOff(1, 5)
    IfFlagOn(1, 11205393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202998, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1201990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205393():
    """ 11205393: Event 11205393 """
    SkipLinesIfThisEventOn(8)
    IfFlagOn(1, 11200000)
    IfFlagOff(1, 5)
    IfCharacterInsideRegion(1, PLAYER, region=1202996)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)


@RestartOnRest
def Event11205392():
    """ 11205392: Event 11205392 """
    SkipLinesIfFlagOff(3, 5)
    DisableCharacter(1200800)
    Kill(1200800, award_souls=False)
    End()
    DisableAI(1200800)
    IfFlagOn(1, 11200000)
    IfFlagOn(1, 11205393)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1200800)
    EnableBossHealthBar(1200800, name=5210, slot=0)


def Event11200001():
    """ 11200001: Event 11200001 """
    IfCharacterDead(0, 1200800)
    EnableFlag(5)
    KillBoss(1200800)
    DisableObject(1201990)
    DeleteFX(1201991, erase_root_only=True)


def Event11205394():
    """ 11205394: Event 11205394 """
    DisableNetworkSync()
    IfFlagOff(1, 5)
    IfFlagOn(1, 11205392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11205391)
    IfCharacterInsideRegion(1, PLAYER, region=1202990)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1203800)


def Event11205395():
    """ 11205395: Event 11205395 """
    DisableNetworkSync()
    IfFlagOn(1, 5)
    IfFlagOn(1, 11205394)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1203800)


@RestartOnRest
def Event11205396():
    """ 11205396: Event 11205396 """
    SkipLinesIfThisEventOn(1)
    IfHealthLessThanOrEqual(0, 1200800, 0.10000000149011612)
    AddSpecialEffect(1200800, 5401)


def Event11205380():
    """ 11205380: Event 11205380 """
    IfFlagOff(1, 11200900)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202898, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1201890, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205381():
    """ 11205381: Event 11205381 """
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202898, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1201890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205383():
    """ 11205383: Event 11205383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11200900)
    IfCharacterInsideRegion(1, PLAYER, region=1202896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    AddSpecialEffect(PLAYER, 5500)
    ActivateMultiplayerBuffs(1200801)


@RestartOnRest
def Event11205382():
    """ 11205382: Event 11205382 """
    DisableCharacter(1200090)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1200801, UpdateAuthority.Forced)
    SkipLinesIfFlagOff(3, 11200900)
    DisableCharacter(1200801)
    Kill(1200801, award_souls=False)
    End()
    DisableHealthBar(1200801)
    DisableAI(1200801)
    SetStandbyAnimationSettings(1200801, standby_animation=7000)
    IfFlagOn(0, 11205383)
    SetStandbyAnimationSettings(1200801, cancel_animation=7001)
    EnableAI(1200801)
    EnableBossHealthBar(1200801, name=3230, slot=0)


def Event11200900():
    """ 11200900: Event 11200900 """
    IfCharacterDead(0, 1200801)
    CancelSpecialEffect(PLAYER, 5500)
    EnableFlag(11200900)
    KillBoss(1200801)
    DisableObject(1201890)
    DeleteFX(1201891, erase_root_only=True)
    DisableObject(1201892)
    DeleteFX(1201893, erase_root_only=True)


def Event11205384():
    """ 11205384: Event 11205384 """
    DisableNetworkSync()
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11205381)
    IfCharacterInsideRegion(1, PLAYER, region=1202890)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(1203801)


def Event11205385():
    """ 11205385: Event 11205385 """
    DisableNetworkSync()
    IfFlagOn(1, 11200900)
    IfFlagOn(1, 11205384)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(1203801)


def Event11205120(arg_0_3: int, arg_4_7: int):
    """ 11205120: Event 11205120 """
    IfCharacterInsideRegion(1, 1200801, region=arg_0_3)
    IfHasTAEEvent(1, 1200801, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(1200801, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    IfDoesNotHaveTAEEvent(0, 1200801, tae_event_id=10)
    Restart()


def Event11200100(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11200100: Event 11200100 """
    SkipLinesIfFlagOn(1, arg_20_23)
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_4_7, 1)
    End()
    CreateObjectFX(arg_8_11, obj=arg_4_7, model_point=200)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    IfPlayerHasGood(1, 2002, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=arg_4_7, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_20_23)
    RotateToFaceEntity(PLAYER, arg_4_7)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    SkipLinesIfClient(1)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisplayDialog(10010861, anchor_entity=arg_4_7, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    ForceAnimation(arg_4_7, 1)
    DeleteObjectFX(arg_4_7, erase_root=True)


def Event11200110(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200110: Event 11200110 """
    DisableNetworkSync()
    IfFlagOn(-1, arg_0_3)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfFlagOn(1, 703)
    SkipLinesIfEqual(1, left=arg_12_15, right=1)
    IfPlayerDoesNotHaveGood(1, 2002, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=arg_4_7)
    IfClient(2)
    IfDialogPromptActivated(2, prompt_text=10010400, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_0_3)
    DisplayDialog(10010160, anchor_entity=arg_4_7, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11200120():
    """ 11200120: Event 11200120 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1201300)
    End()
    IfObjectDestroyed(0, 1201300)
    EnableFlag(11200120)


@RestartOnRest
def Event11205150(arg_0_3: int):
    """ 11205150: Event 11205150 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.800000011920929)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event11205180(arg_0_3: int, arg_4_7: int):
    """ 11205180: Event 11205180 """
    SkipLinesIfEqual(3, left=arg_4_7, right=0)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    SetNest(arg_0_3, 1202732)
    End()
    SkipLinesIfThisEventSlotOn(6)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)
    DisableAI(arg_0_3)
    IfHealthLessThanOrEqual(0, 1200350, 0.4000000059604645)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, 1202732)


@RestartOnRest
def Event11205190(arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 11205190: Event 11205190 """
    EndIfThisEventSlotOn()
    DisableGravity(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    Wait(arg_8_11)
    EnableGravity(arg_0_3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 7000, wait_for_completion=True)
    EnableAI(arg_0_3)


@RestartOnRest
def Event11205200(arg_0_3: int, arg_4_7: float):
    """ 11205200: Event 11205200 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfAttacked(-1, arg_0_3, attacking_character=6521)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205250(arg_0_3: int, arg_4_7: int):
    """ 11205250: Event 11205250 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfAttacked(-1, arg_0_3, attacking_character=6521)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, 6521, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205290(arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 11205290: Event 11205290 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableAI(arg_0_3)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfAttacked(-1, arg_0_3, attacking_character=6521)
    SkipLinesIfEqual(1, left=0, right=arg_12_15)
    SkipLinesIfClient(1)
    IfFlagOn(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_8_11)
    EnableAI(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205230(arg_0_3: int, arg_4_7: float):
    """ 11205230: Event 11205230 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, 6521, radius=arg_4_7)
    IfAttacked(-2, arg_0_3, attacking_character=PLAYER)
    IfAttacked(-2, arg_0_3, attacking_character=6521)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableCharacterCollision(arg_0_3)
    EnableGravity(arg_0_3)
    EndIfFinishedConditionTrue(2)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9063)


@RestartOnRest
def Event11205240(arg_0_3: int, arg_4_7: int):
    """ 11205240: Event 11205240 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5110)
    SetNest(arg_0_3, arg_4_7)


@RestartOnRest
def Event11205260(arg_0_3: int, arg_4_7: float):
    """ 11205260: Event 11205260 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, 6521, radius=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205280(arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """ 11205280: Event 11205280 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfEntityWithinDistance(-1, arg_0_3, 6521, radius=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, 6521, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


@RestartOnRest
def Event11205000():
    """ 11205000: Event 11205000 """
    DisableGravity(1200000)
    DisableCharacterCollision(1200000)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(0, PLAYER, region=1202100)
    EnableGravity(1200000)
    EnableCharacterCollision(1200000)
    SetNest(1200000, 1202101)


@RestartOnRest
def Event11200800():
    """ 11200800: Event 11200800 """
    DisableCharacter(1200200)
    EndIfThisEventOn()
    SkipLinesIfFlagOn(1, 11200801)
    IfFlagOn(0, 703)
    EnableCharacter(1200200)
    IfCharacterBackreadEnabled(0, 1200200)
    SetDisplayMask(1200200, bit_index=0, switch_type=OnOffChange.Off)
    IfCharacterDead(0, 1200200)
    EnableFlag(11200800)


@RestartOnRest
def Event11200801():
    """ 11200801: Event 11200801 """
    SkipLinesIfThisEventOff(2)
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


@RestartOnRest
def Event11205300(arg_0_1: short, arg_2_3: short, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, 
                  arg_17_17: uchar, arg_20_23: int):
    """ 11205300: Event 11205300 """
    DisableCharacter(arg_8_11)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(1200010, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1200010, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1200010, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, 1200010)
    CreateNPCPart(1200010, npc_part_id=arg_2_3, part_index=arg_0_1, part_health=176, damage_correction=1.0, 
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, 1200010, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, 1200010, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(1200010, disable_interpolation=False)
    Move(arg_8_11, destination=1200010, destination_type=CoordEntityType.Character, model_point=arg_12_15, 
         copy_draw_parent=1200010)
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(1200010, 8000)
    SetDisplayMask(1200010, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1200010, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1200010, arg_20_23)


def Event11200200():
    """ 11200200: Event 11200200 """
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
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event11200810(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11200810: Event 11200810 """
    SkipLinesIfThisEventSlotOff(6)
    SkipLinesIfEqual(3, left=arg_4_7, right=1)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    DropMandatoryTreasure(arg_0_3)
    End()
    IfCharacterDead(0, arg_0_3)
    EndIfEqual(left=arg_8_11, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)


def Event11200600(arg_0_3: int, arg_4_7: int):
    """ 11200600: Event 11200600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11200690():
    """ 11200690: Event 11200690 """
    SkipLinesIfThisEventOn(6)
    DisableTreasure(1201600)
    DisableObject(1201600)
    IfFlagOn(-1, 1123)
    IfFlagOn(-1, 1130)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(1201600)
    EnableTreasure(1201600)


def Event11200510(arg_0_3: int, arg_4_7: int):
    """ 11200510: Event 11200510 """
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


def Event11200520(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200520: Event 11200520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200501(arg_0_3: int, arg_4_7: int):
    """ 11200501: Event 11200501 """
    IfFlagOff(1, 1603)
    IfFlagOn(1, 1600)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfThisEventOff(1)
    IfFlagOff(2, 1763)
    IfFlagOn(2, 1760)
    IfHealthLessThanOrEqual(2, 6420, 0.8999999761581421)
    IfHealthGreaterThan(2, 6420, 0.0)
    IfAttacked(2, 6420, attacking_character=PLAYER)
    IfThisEventOff(2)
    IfFlagOn(3, 746)
    IfThisEventOff(3)
    IfFlagOn(-2, arg_4_7)
    IfFlagOn(-2, 1763)
    IfConditionTrue(4, input_condition=-2)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 4)
    SkipLinesIfFlagOn(1, 1604)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOn(1, 1764)
    EnableFlag(1763)
    SkipLinesIfFlagOn(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagOn(1, 1764)
    EnableCharacter(6420)
    SetTeamType(arg_0_3, TeamType.Enemy)
    SetTeamType(6420, TeamType.Enemy)
    SaveRequest()
    EnableFlag(1766)


def Event11200530(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200530: Event 11200530 """
    IfFlagOn(1, 1120)
    IfFlagOn(1, 11200800)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1200200, destination_type=CoordEntityType.Character, model_point=101, 
         copy_draw_parent=1200200)
    EnableCharacter(arg_0_3)
    Wait(0.5)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7875)
    ForceAnimation(arg_0_3, 7876)


def Event11200531(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200531: Event 11200531 """
    IfFlagOn(1, 1121)
    IfFlagOn(1, 11200590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200532(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200532: Event 11200532 """
    IfFlagOn(1, 1121)
    IfFlagOn(1, 11200591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7877, wait_for_completion=True)
    ForceAnimation(arg_0_3, 8289, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200533():
    """ 11200533: Event 11200533 """
    DeleteFX(1203100, erase_root_only=False)
    DeleteFX(1203101, erase_root_only=False)
    DeleteFX(1203102, erase_root_only=False)
    DeleteFX(1203103, erase_root_only=False)
    EndIfClient()
    IfPlayerDoesNotHaveGood(1, 2520, including_box=False)
    IfFlagOn(1, 1122)
    IfFlagOn(2, 1129)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableRandomFlagInRange((11200210, 11200213))
    SkipLinesIfFlagOff(1, 11200210)
    CreateFX(1203100)
    SkipLinesIfFlagOff(1, 11200211)
    CreateFX(1203101)
    SkipLinesIfFlagOff(1, 11200212)
    CreateFX(1203102)
    SkipLinesIfFlagOff(1, 11200213)
    CreateFX(1203103)


def Event11205040(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11205040: Event 11205040 """
    SkipLinesIfFlagOff(2, 11200215)
    EnableCharacter(6051)
    End()
    IfFlagOn(1, 1122)
    IfFlagOn(1, arg_0_3)
    IfDialogPromptActivated(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteFX(arg_8_11, erase_root_only=True)
    Move(6051, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryFX(120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=-1)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205310)


def Event11200534(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200534: Event 11200534 """
    IfFlagOn(1, 1122)
    IfFlagOn(1, 11205310)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200529(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11200529: Event 11200529 """
    EndIfFlagOn(17)
    IfFlagOn(-1, 1122)
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(2, 1125)
    SkipLinesIfFlagOn(1, 1126)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11200527(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200527: Event 11200527 """
    IfFlagOn(0, 1128)
    SkipLinesIfFlagOn(5, 1125)
    SkipLinesIfFlagOn(8, 1126)
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


def Event11205070(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11205070: Event 11205070 """
    SkipLinesIfFlagOff(2, 11200215)
    EnableCharacter(6051)
    End()
    IfFlagOn(1, 1129)
    IfFlagOn(1, arg_0_3)
    IfDialogPromptActivated(1, prompt_text=50000000, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, model_point=0, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11200215)
    DeleteFX(arg_8_11, erase_root_only=True)
    Move(6051, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryFX(120, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Region, model_point=-1)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205311)


def Event11200525(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200525: Event 11200525 """
    IfFlagOn(1, 1129)
    IfFlagOn(1, 11205311)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200535(arg_0_3: int):
    """ 11200535: Event 11200535 """
    SkipLinesIfClient(1)
    DisableFlag(11205021)
    SkipLinesIfHost(1)
    SkipLinesIfFlagOn(5, 11205021)
    IfFlagOff(1, 1603)
    IfFlagOff(1, 1601)
    IfHost(1)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(1, 1604)
    EnableCharacter(arg_0_3)
    SkipLinesIfFlagOn(2, 1764)
    EnableCharacter(6420)
    EnableFlag(1766)
    EnableFlag(11205021)


def Event11200538(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200538: Event 11200538 """
    IfAttacked(0, arg_0_3, attacking_character=PLAYER)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 9030, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11200539(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200539: Event 11200539 """
    IfFlagOn(1, 1710)
    IfFlagOn(1, 746)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11200540(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200540: Event 11200540 """
    IfFlagOn(1, 1712)
    IfFlagOn(1, 11200596)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7003, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11205054():
    """ 11205054: Event 11205054 """
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagOff(1, 11205055)
    IfFlagOn(1, 11205053)
    IfConditionTrue(1, input_condition=-7)
    IfConditionFalse(1, input_condition=7)
    IfFlagOff(1, 11205050)
    IfFlagOff(2, 11205055)
    IfFlagOn(2, 11205053)
    IfConditionTrue(2, input_condition=-7)
    IfConditionTrue(2, input_condition=7)
    IfAttacked(-6, 6380, attacking_character=PLAYER)
    IfFlagOn(-6, 11205060)
    IfFlagOn(-6, 11205061)
    IfFlagOn(-6, 11205062)
    IfFlagOn(-6, 11205063)
    IfFlagOn(-6, 11205064)
    IfFlagOn(-6, 11205065)
    IfFlagOn(-6, 11205066)
    IfFlagOn(-6, 11205067)
    IfFlagOn(-6, 11205068)
    IfFlagOn(-6, 745)
    IfConditionTrue(2, input_condition=-6)
    IfFlagOff(3, 11205055)
    IfFlagOff(3, 11205053)
    IfConditionTrue(3, input_condition=-7)
    IfConditionFalse(3, input_condition=7)
    IfFlagOn(3, 11205050)
    IfFlagOff(4, 11205055)
    IfFlagOff(4, 11205053)
    IfConditionTrue(4, input_condition=-7)
    IfConditionTrue(4, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11205055)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11205052)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11205052)
    Restart()


@RestartOnRest
def Event11205056():
    """ 11205056: Event 11205056 """
    IfPlayerCovenant(7, Covenant.ForestHunter)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfFlagOn(1, 11205051)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(2, 11205051)
    IfConditionTrue(2, input_condition=-7)
    IfConditionFalse(2, input_condition=7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11205051)
    DisableFlag(11205053)
    SkipLinesIfFinishedConditionTrue(9, 2)
    IfCharacterHuman(-6, PLAYER)
    IfCharacterHollow(-6, PLAYER)
    SkipLinesIfConditionFalse(3, -6)
    BetrayCurrentCovenant()
    SkipLinesIfFlagOn(2, 9001)
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


@RestartOnRest
def Event11205057():
    """ 11205057: Event 11205057 """
    IfFlagOn(0, 11205052)
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


def Event11205058():
    """ 11205058: Event 11205058 """
    SkipLinesIfFlagOff(2, 11205053)
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


@RestartOnRest
def Event11205060(arg_0_3: int):
    """ 11205060: Event 11205060 """
    SkipLinesIfFlagOff(1, 746)
    SetTeamType(arg_0_3, TeamType.Enemy)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfPlayerCovenant(1, Covenant.ForestHunter)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(0, input_condition=1)
    End()


def Event11205030():
    """ 11205030: Event 11205030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6521, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11205033)
    IfClient(2)
    IfFlagOn(2, 11205031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6521)
    EndIfFlagOn(11200900)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterBackreadEnabled(1, 6521)
    IfEntityWithinDistance(1, 6521, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6521, region=1202010, summon_flag=11205031, dismissal_flag=11205033)


def Event11205032():
    """ 11205032: Event 11205032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11205031)
    IfFlagOn(1, 11205383)
    IfConditionTrue(0, input_condition=1)
    AICommand(6521, command_id=10, slot=0)
    ReplanAI(6521)
    IfCharacterInsideRegion(0, 6521, region=1202898)
    RotateToFaceEntity(6521, 1202894)
    ForceAnimation(6521, 7410)
    AICommand(6521, command_id=-1, slot=0)
    ReplanAI(6521)


def Event11200300():
    """ 11200300: Event 11200300 """
    IfFlagOn(0, 11205031)
    EnableFlag(11200300)


def Event11200005():
    """ 11200005: Event 11200005 """
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfFlagOn(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfFlagOff(1, 17)
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    IfSingleplayer(0)
    CreateFX(1202009)
    IfMultiplayer(0)
    DeleteFX(1202009, erase_root_only=True)
    Restart()


def Event11200006():
    """ 11200006: Event 11200006 """
    IfFlagOn(-1, 1125)
    IfFlagOn(-1, 1126)
    IfFlagOn(-1, 1127)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerHasGood(1, 2520, including_box=False)
    IfFlagOff(1, 17)
    IfSingleplayer(1)
    IfDialogPromptActivated(1, prompt_text=10010100, anchor_entity=1202008, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True)
    IfConditionTrue(0, input_condition=1)
    EndIfClient()
    PlayCutscene(120002, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1212510, move_to_map=OOLACILE)
    WaitFrames(1)
    SaveRequest()
    Restart()
