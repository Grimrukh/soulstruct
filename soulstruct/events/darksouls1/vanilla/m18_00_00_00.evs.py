"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 11800100)
    RegisterBonfire(11800992, obj=1801960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    SkipLinesIfFlagOff(1, 11800210)
    RegisterBonfire(11800992, obj=1801960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)
    SkipLinesIfClient(2)
    DisableObject(1801994)
    DeleteFX(1801995, erase_root_only=False)
    SkipLinesIfFlagOff(3, 15)
    DisableObject(1801960)
    DisableObject(1801110)
    EnableObject(1801111)
    RunEvent(11805090)
    RunEvent(11805091)
    RunEvent(11805092)
    RunEvent(20)
    RunEvent(21)
    RunEvent(11800100)
    RunEvent(11800101)
    RunEvent(11800200)
    RunEvent(11800230, slot=0, args=(1, 180005, 1801960))
    RunEvent(11800230, slot=1, args=(2, 180006, 1801960))
    RunEvent(11800230, slot=2, args=(3, 180007, 1801960))
    RunEvent(11800230, slot=3, args=(4, 180008, 1801960))
    RunEvent(11800210)
    RunEvent(11800220)
    RunEvent(11806100, slot=0, args=(1800100, 1802000))
    RunEvent(11806100, slot=1, args=(1800101, 1802001))
    RunEvent(11806100, slot=2, args=(1800102, 1802002))
    RunEvent(11806100, slot=3, args=(1800103, 1802003))
    RunEvent(11806100, slot=4, args=(1800104, 1802004))
    RunEvent(11806100, slot=5, args=(1800105, 1802005))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11800002)
    DisableSoundEvent(1803800)
    SkipLinesIfFlagOff(4, 15)
    RunEvent(11805392)
    DisableObject(1801990)
    DeleteFX(1801991, erase_root_only=False)
    SkipLines(7)
    RunEvent(11805390)
    RunEvent(11805391)
    RunEvent(11805393)
    RunEvent(11805392)
    RunEvent(11800001)
    RunEvent(11805394)
    RunEvent(11805395)
    HumanityRegistration(6544, 8310)
    RunEvent(11805030)
    RunEvent(11805029)
    RunEvent(11805032)
    RunEvent(11805990, slot=0, args=(11805031, 6544))
    RunEvent(11800550, slot=0, args=(1000, 1029, 1012))
    EnableImmortality(6331)
    SkipLinesIfFlagOn(1, 830)
    DisableCharacter(6331)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800539, slot=0, args=(6331, 1640, 1647, 1647))
    RunEvent(11800530, slot=0, args=(6331, 1640, 1647, 1644))
    RunEvent(11800531, slot=0, args=(6331, 1640, 1647, 1645))
    RunEvent(11800537, slot=0, args=(6331, 1640, 1647, 1649))
    RunEvent(11800541, slot=0, args=(6331,))
    RunEvent(11806200)
    EnableImmortality(6341)
    SkipLinesIfFlagOn(1, 831)
    DisableCharacter(6341)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800540, slot=0, args=(6341, 1670, 1677, 1677))
    RunEvent(11800533, slot=0, args=(6341, 1670, 1677, 1673))
    RunEvent(11800534, slot=0, args=(6341, 1670, 1677, 1674))
    RunEvent(11800538, slot=0, args=(6341, 1670, 1677, 1678))
    RunEvent(11800542, slot=0, args=(6341,))
    RunEvent(11806201)


@RestartOnRest
def Event11805090():
    """ 11805090: Event 11805090 """
    EndIfThisEventOn()
    DisableCharacter(1800900)
    DisableCharacter(1800901)
    DisableCharacter(1800902)
    DisableCharacter(1800903)
    DisableCharacter(1800904)
    IfFlagOn(0, 11800050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(1800900)
    EnableCharacter(1800901)
    EnableCharacter(1800902)
    EnableCharacter(1800903)
    EnableCharacter(1800904)


@RestartOnRest
def Event11805091():
    """ 11805091: Event 11805091 """
    IfFlagOn(-1, 11805095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11800050)
    DisableFlag(11805095)
    EnableFlag(5001)
    Kill(1800900, award_souls=False)
    Kill(1800901, award_souls=False)
    Kill(1800902, award_souls=False)
    Kill(1800903, award_souls=False)
    Kill(1800904, award_souls=False)


@RestartOnRest
def Event11805092():
    """ 11805092: Event 11805092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11800050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11800050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11800050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11800050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11800050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11800050)
    RestartIfConditionFalse(-6)
    EnableFlag(11800050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=KILN_OF_THE_FIRST_FLAME)
    RestartIfConditionFalse(7)
    DisableFlag(11800050)
    EnableFlag(11805095)


def Event11805390():
    """ 11805390: Event 11805390 """
    IfFlagOff(1, 15)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        line_intersects=1801990,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805391():
    """ 11805391: Event 11805391 """
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1802998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1801990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1802997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805393():
    """ 11805393: Event 11805393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 15)
    IfCharacterInsideRegion(1, PLAYER, region=1802996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1800800)


@RestartOnRest
def Event11805392():
    """ 11805392: Event 11805392 """
    SkipLinesIfFlagOff(3, 15)
    DisableCharacter(1800800)
    Kill(1800800, award_souls=False)
    End()
    DisableAI(1800800)
    IfFlagOn(1, 11805393)
    IfCharacterInsideRegion(1, PLAYER, region=1802996)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1800800)
    EnableBossHealthBar(1800800, name=5370, slot=0)


def Event11800001():
    """ 11800001: Event 11800001 """
    DisableObject(1801111)
    DisableObject(1801950)
    IfCharacterDead(0, 1800800)
    EnableFlag(15)
    KillBoss(1800800)
    DisableObject(1801990)
    DeleteFX(1801991, erase_root_only=True)
    SkipLinesIfClient(2)
    SetRespawnPoint(1802130)
    SaveRequest()
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    DisableObject(1801960)
    DisableObject(1801110)
    EnableObject(1801111)
    DeleteObjectFX(1801960, erase_root=True)
    CreateTemporaryFX(90014, anchor_entity=1801950, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1801950)


def Event20():
    """ 20: Event 20 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfActionButton(1, prompt_text=10010108, anchor_entity=1801950, anchor_type=CoordEntityType.Object, max_distance=1.5)
    IfConditionTrue(0, input_condition=1)
    IncrementNewGameCycle(1)
    PlayCutscene(180000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(1)
    EnableFlag(20)


def Event21():
    """ 21: Event 21 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfCharacterOutsideRegion(1, PLAYER, region=1802990)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180001, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    IncrementNewGameCycle(1)
    AwardAchievement(2)
    EnableFlag(21)


def Event11805394():
    """ 11805394: Event 11805394 """
    DisableNetworkSync()
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11805391)
    IfCharacterInsideRegion(1, PLAYER, region=1802990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1803800)


def Event11805395():
    """ 11805395: Event 11805395 """
    DisableNetworkSync()
    IfFlagOn(1, 15)
    IfFlagOn(1, 11805394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1803800)


@RestartOnRest
def Event11800002():
    """ 11800002: Event 11800002 """
    IfFlagOn(0, 15)
    DisableCharacter(1800200)
    DisableCharacter(1800201)
    DisableCharacter(1800202)
    DisableCharacter(1800203)
    DisableCharacter(1800204)
    DisableCharacter(1800900)
    DisableCharacter(1800901)
    DisableCharacter(1800902)
    DisableCharacter(1800903)
    DisableCharacter(1800904)
    DisableCharacter(1803900)
    DisableCharacter(1803901)
    DisableCharacter(1803902)
    Kill(1800200, award_souls=False)
    Kill(1800201, award_souls=False)
    Kill(1800202, award_souls=False)
    Kill(1800203, award_souls=False)
    Kill(1800204, award_souls=False)
    Kill(1800900, award_souls=False)
    Kill(1800901, award_souls=False)
    Kill(1800902, award_souls=False)
    Kill(1800903, award_souls=False)
    Kill(1800904, award_souls=False)
    Kill(1803900, award_souls=False)
    Kill(1803901, award_souls=False)
    Kill(1803902, award_souls=False)


def Event11800100():
    """ 11800100: Event 11800100 """
    EndIfThisEventOn()
    DisableObject(1801110)
    IfHost(1)
    IfPlayerHasGood(1, 2510, including_box=False)
    IfActionButton(1, prompt_text=10010105, anchor_entity=1801960, anchor_type=CoordEntityType.Object, model_point=150)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180015, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObject(1801110)
    RegisterBonfire(11800992, obj=1801960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RemoveGoodFromPlayer(2510)


def Event11800101():
    """ 11800101: Event 11800101 """
    DisableNetworkSync()
    IfFlagOff(1, 11800100)
    IfPlayerDoesNotHaveGood(1, 2510, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=1801960,
        anchor_type=CoordEntityType.Object,
        model_point=150,
        trigger_attribute=255,
    )
    IfFlagOn(2, 11800100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisplayDialog(
        10010174,
        anchor_entity=1801960,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11800200():
    """ 11800200: Event 11800200 """
    IfFlagOn(0, 756)
    ForceAnimation(PLAYER, 7697)
    WaitFrames(75)
    IfFlagOff(1, 11800201)
    IfPlayerHasGood(1, 2500, including_box=False)
    IfFlagOff(2, 11800202)
    IfPlayerHasGood(2, 2501, including_box=False)
    IfFlagOff(3, 11800203)
    IfPlayerHasGood(3, 2502, including_box=False)
    IfFlagOff(4, 11800204)
    IfPlayerHasGood(4, 2503, including_box=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 1)
    EnableFlag(11800201)
    RemoveGoodFromPlayer(2500)
    SkipLinesIfFinishedConditionFalse(2, 2)
    EnableFlag(11800202)
    RemoveGoodFromPlayer(2501)
    SkipLinesIfFinishedConditionFalse(2, 3)
    EnableFlag(11800203)
    RemoveGoodFromPlayer(2502)
    SkipLinesIfFinishedConditionFalse(2, 4)
    EnableFlag(11800204)
    RemoveGoodFromPlayer(2503)
    EnableFlag(11805111)
    IfFlagOff(0, 11805111)
    WaitFrames(10)
    EndIfFlagOn(11800211)
    DisableFlag(756)
    Restart()


def Event11800230(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800230: Event 11800230 """
    IfFlagOn(1, 11805111)
    IfTrueFlagCountEqual(1, arg_0_3, (11800201, 11800204))
    IfConditionTrue(0, input_condition=1)
    DeleteObjectFX(arg_8_11, erase_root=True)
    CreateObjectFX(arg_4_7, obj=arg_8_11, model_point=100)
    WaitFrames(95)
    SkipLinesIfFlagRangeAllOn(1, (11800201, 11800204))
    ForceAnimation(PLAYER, 7701, loop=True)
    DisableFlag(11805111)


def Event11800210():
    """ 11800210: Event 11800210 """
    SkipLinesIfFlagOn(17, 15)
    IfTrueFlagCountEqual(2, 1, (11800201, 11800204))
    IfTrueFlagCountEqual(3, 2, (11800201, 11800204))
    IfTrueFlagCountEqual(4, 3, (11800201, 11800204))
    IfTrueFlagCountEqual(5, 4, (11800201, 11800204))
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 2)
    CreateObjectFX(180005, obj=1801960, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 3)
    CreateObjectFX(180006, obj=1801960, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 4)
    CreateObjectFX(180007, obj=1801960, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 5)
    CreateObjectFX(180008, obj=1801960, model_point=100)
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1801101, 1)
    End()
    IfFlagOn(1, 11800201)
    IfFlagOn(1, 11800202)
    IfFlagOn(1, 11800203)
    IfFlagOn(1, 11800204)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11800211)
    DisableFlag(756)
    PlayCutscene(180010, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(1801101, 1)
    RegisterBonfire(11800992, obj=1801960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)


def Event11800220():
    """ 11800220: Event 11800220 """
    DisableNetworkSync()
    IfFlagOff(1, 11800210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=1802100,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=255,
        line_intersects=1801101,
    )
    IfFlagOn(2, 11805110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisplayDialog(
        10010160,
        anchor_entity=1801101,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(2)
    DisableFlag(11805110)
    DisplayDialog(
        10010171,
        anchor_entity=1801960,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11806100(_, arg_0_3: int, arg_4_7: int):
    """ 11806100: Event 11806100 """
    DisableNetworkSync()
    SkipLinesIfThisEventSlotOn(3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 200, loop=True)
    IfCharacterInsideRegion(0, arg_0_3, region=1802006)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Restart()


@RestartOnRest
def Event11805100(_, arg_0_3: int, arg_4_7: int):
    """ 11805100: Event 11805100 """
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11800510(_, arg_0_3: int, arg_4_7: int):
    """ 11800510: Event 11800510 """
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
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11800520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800520: Event 11800520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800530: Event 11800530 """
    IfFlagOn(1, 1643)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800531: Event 11800531 """
    IfFlagOn(1, 1644)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800533: Event 11800533 """
    IfFlagOn(1, 1672)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800534: Event 11800534 """
    IfFlagOn(1, 1673)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800537: Event 11800537 """
    IfFlagOn(-1, 1642)
    IfFlagOn(-1, 1643)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800538: Event 11800538 """
    IfFlagOn(-1, 1671)
    IfFlagOn(-1, 1672)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800539: Event 11800539 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11020598)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacking_character=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7009, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800540: Event 11800540 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11600590)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacking_character=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800541(_, arg_0_3: int):
    """ 11800541: Event 11800541 """
    IfFlagOn(1, 830)
    IfFlagOff(1, 1647)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 830)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800542(_, arg_0_3: int):
    """ 11800542: Event 11800542 """
    IfFlagOn(1, 831)
    IfFlagOff(1, 1676)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 831)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800550: Event 11800550 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11806200():
    """ 11806200: Event 11806200 """
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 824)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(824)
    PlayCutscene(
        180050, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1022110, move_to_map=FIRELINK_SHRINE
    )
    PlayCutscene(100250, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(6331)
    DisableFlag(830)
    Restart()


def Event11806201():
    """ 11806201: Event 11806201 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1673)
    IfFlagOn(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 825)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(825)
    PlayCutscene(
        180051, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1602110, move_to_map=NEW_LONDO_RUINS
    )
    PlayCutscene(160050, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(6341)
    DisableFlag(831)
    Restart()


def Event11805029():
    """ 11805029: Event 11805029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6544, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6544)
    EndIfFlagOn(15)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11805031)
    IfFlagOff(1, 11805033)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, 6544)
    IfEntityWithinDistance(1, 6544, PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6544, region=1802050, summon_flag=11805031, dismissal_flag=11805033)


def Event11805990(_, arg_0_3: int, arg_4_7: int):
    """ 11805990: Event 11805990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11805030():
    """ 11805030: Event 11805030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6544, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6544)
    EndIfFlagOn(15)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, 6544)
    IfEntityWithinDistance(1, 6544, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6544, region=1802050, summon_flag=11805031, dismissal_flag=11805033)


def Event11805032():
    """ 11805032: Event 11805032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11805031)
    IfFlagOn(1, 11805393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6544, command_id=10, slot=0)
    ReplanAI(6544)
    IfEntityWithinDistance(0, 6544, 1801990, radius=1.5)
    RotateToFaceEntity(6544, 1802997)
    ForceAnimation(6544, 7410)
    AICommand(6544, command_id=-1, slot=0)
    ReplanAI(6544)


@RestartOnRest
def Event11805200():
    """ 11805200: Event 11805200 """
    DisableAI(1800999)
    IfMovingOnCollision(1, 1803000)
    IfRunningOnCollision(2, 1803000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    RequestAnimation(1800999, 1750, loop=False, wait_for_completion=True)
    Restart()
    RequestAnimation(1800999, 2000, loop=False, wait_for_completion=True)
    Restart()
