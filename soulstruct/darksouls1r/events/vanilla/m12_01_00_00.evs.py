"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11210700()
    SkipLinesIfClient(10)
    DisableObject(1211988)
    DeleteVFX(1211989, erase_root_only=False)
    DisableObject(1211994)
    DeleteVFX(1211995, erase_root_only=False)
    DisableObject(1211996)
    DeleteVFX(1211997, erase_root_only=False)
    DisableObject(1211998)
    DeleteVFX(1211999, erase_root_only=False)
    DisableObject(1211986)
    DeleteVFX(1211987, erase_root_only=False)
    DisableMapCollision(collision=1213061)
    SkipLinesIfFlagDisabled(2, 11210539)
    EnableMapCollision(collision=1213061)
    DisableMapCollision(collision=1213060)
    Event_11215090()
    Event_11215091()
    Event_11215092()
    DisableSoundEvent(sound_id=1213800)
    SkipLinesIfFlagDisabled(6, 11210000)
    Event_11210000()
    DisableObject(1211790)
    DeleteVFX(1211791, erase_root_only=False)
    DisableObject(1211792)
    DeleteVFX(1211793, erase_root_only=False)
    SkipLines(8)
    Event_11215000()
    Event_11215001()
    Event_11215002()
    Event_11215003()
    Event_11215004()
    Event_11215005()
    Event_11210000()
    Event_11215006(0, character=1210810, character_1=1210800, item_lot_param_id=34720000)
    Event_11215006(1, character=1210811, character_1=1210801, item_lot_param_id=34720010)
    Event_11215006(2, character=1210812, character_1=1210802, item_lot_param_id=34720020)
    Event_11215007()
    Event_11215008()
    Event_11215009()
    DisableSoundEvent(sound_id=1213801)
    SkipLinesIfFlagDisabled(7, 11210001)
    Event_11210001()
    DisableObject(1211890)
    DeleteVFX(1211891, erase_root_only=False)
    DisableObject(1211892)
    DeleteVFX(1211893, erase_root_only=False)
    DisableMapCollision(collision=1213001)
    SkipLines(7)
    Event_11215010()
    Event_11215011()
    Event_11215012()
    Event_11215013()
    Event_11215014()
    Event_11215015()
    Event_11210001()
    DisableSoundEvent(sound_id=1213802)
    SkipLinesIfFlagDisabled(4, 11210002)
    Event_11210002()
    DisableObject(1211990)
    DeleteVFX(1211991, erase_root_only=False)
    SkipLines(8)
    Event_11215020()
    Event_11215021()
    Event_11215022()
    Event_11215027()
    Event_11215023()
    Event_11215024()
    Event_11215025()
    Event_11210002()
    Event_11215026()
    DisableSoundEvent(sound_id=1213803)
    IfFlagEnabled(1, 11210592)
    IfFlagDisabled(1, 11210004)
    SkipLinesIfConditionTrue(3, 1)
    DisableObject(1211690)
    DeleteVFX(1211691, erase_root_only=False)
    DisableMapCollision(collision=1213001)
    SkipLinesIfFlagEnabled(8, 11210004)
    Event_11215060()
    Event_11215061()
    Event_11215062()
    Event_11215063()
    Event_11215064()
    Event_11215066()
    Event_11215065()
    Event_11210005()
    SkipLinesIfFlagDisabled(1, 11210002)
    RegisterBonfire(bonfire_flag=11210992, obj=1211950)
    RegisterBonfire(bonfire_flag=11210984, obj=1211963)
    RegisterBonfire(bonfire_flag=11210976, obj=1211961)
    RegisterBonfire(bonfire_flag=11210968, obj=1211962)
    RegisterBonfire(bonfire_flag=11210960, obj=1211964)
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=1211110)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=1211111)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=1211112)
    Event_11215100()
    Event_11215110(0, 1210101, 1212502, 0.0, 1212502)
    Event_11215110(1, 1210102, 1212502, 0.0, 1212502)
    Event_11215110(2, 1210103, 1212502, 10.0, 1212506)
    Event_11215110(3, 1210104, 1212502, 10.0, 1212506)
    Event_11215115(0, character=1210101, region=1212502, region_1=1212501)
    Event_11215115(1, character=1210102, region=1212502, region_1=1212501)
    Event_11215120(0, character=1210105, character_1=1210106, character_2=1210107, flag=51210030)
    Event_11215140(
        0,
        character=1210150,
        region=1212503,
        region_1=1212504,
        region_2=1212505,
        flag=11215151,
        flag_1=11215152,
        flag_2=11215153
    )
    Event_11215140(
        1,
        character=1210151,
        region=1212523,
        region_1=1212524,
        region_2=1212525,
        flag=11215154,
        flag_1=11215155,
        flag_2=11215156
    )
    Event_11210050()
    Event_11210051()
    Event_11210052()
    Event_11210053()
    Event_11210054()
    Event_11210055()
    Event_11210056()
    Event_11210057()
    Event_11210040()
    Event_11210041()
    Event_11210042()
    Event_11210043()
    Event_11210004()
    Event_11215050()
    Event_11215051()
    Event_11215052()
    Event_11210025()
    Event_11210021()
    Event_11215040()
    Event_11215041()
    Event_11210020()
    Event_11215043()
    Event_11215044()
    Event_11210330(0, first_flag=11210310, last_flag=11210315, flag=11210330)
    Event_11210310(0, character=1210300, flag=11210310)
    Event_11210310(1, character=1210301, flag=11210311)
    Event_11210310(2, character=1210302, flag=11210312)
    Event_11210310(3, character=1210303, flag=11210313)
    Event_11210310(4, character=1210304, flag=11210314)
    Event_11210310(5, character=1210305, flag=11210315)
    Event_11210600(0, obj=1211600, obj_act_id=11210600)
    Event_11210600(1, obj=1211601, obj_act_id=11210601)
    Event_11210600(2, obj=1211602, obj_act_id=11210602)
    Event_11210600(4, obj=1211604, obj_act_id=11210604)
    Event_11210600(5, obj=1211605, obj_act_id=11210605)
    Event_11210230(0, obj=1211210, obj_1=1211650, animation_id=125, animation_id_1=126)
    Event_11210350(0, character=1210200, item_lot_param_id=33007200)
    Event_11210350(1, character=1210201, item_lot_param_id=33007000)
    Event_11210350(2, character=1210202, item_lot_param_id=33007100)
    Event_11210350(3, character=1210203, item_lot_param_id=33007300)
    Event_11210350(4, character=1210204, item_lot_param_id=33007100)
    Event_11210350(5, character=1210260, item_lot_param_id=41601000)
    Event_11210100()
    Event_11210103()
    Event_11210110()
    Event_11210120()
    Event_11210123()
    Event_11210130()
    Event_11210133()
    Event_11210140()
    Event_11210150()
    Event_11219100(0, flag=11218102, obj=1211000, animation_id=0, state=1, anchor_entity=1211001)
    Event_11219100(1, flag=11218103, obj=1211000, animation_id=10, state=0, anchor_entity=1211002)
    Event_11210170(0, left=11215220, collision=1213050, region=1212105)
    Event_11210170(1, left=11215221, collision=1213051, region=1212115)
    Event_11210170(2, left=11215222, collision=1213052, region=1212125)
    Event_11210170(3, left=11215223, collision=1213053, region=1212135)
    Event_11210170(4, left=11215224, collision=1213054, region=1212145)
    DisableSoundEvent(sound_id=1213810)
    DisableSoundEvent(sound_id=1213811)
    Event_11210200(0, obj=1211200, region=1212200)
    Event_11210200(1, obj=1211201, region=1212201)
    Event_11210205(0, anchor_entity=1211200, region=1212200, flag=11210200)
    Event_11210205(1, anchor_entity=1211201, region=1212201, flag=11210201)
    Event_11210300()
    Event_11215250(0, obj=1211300, vfx_id=1213160)
    Event_11215250(1, obj=1211301, vfx_id=1213161)
    Event_11215250(2, obj=1211302, vfx_id=1213162)
    Event_11215250(3, obj=1211303, vfx_id=1213163)
    Event_11215250(4, obj=1211304, vfx_id=1213164)
    Event_11215250(5, obj=1211305, vfx_id=1213165)
    Event_11215250(6, obj=1211306, vfx_id=1213166)
    Event_11215250(7, obj=1211307, vfx_id=1213167)
    Event_11215250(8, obj=1211308, vfx_id=1213168)
    Event_11215250(9, obj=1211309, vfx_id=1213169)
    Event_11215250(10, obj=1211310, vfx_id=1213170)
    Event_11215250(11, obj=1211311, vfx_id=1213171)
    Event_11215250(12, obj=1211312, vfx_id=1213172)
    Event_11215250(13, obj=1211313, vfx_id=1213173)
    Event_11215250(14, obj=1211314, vfx_id=1213174)
    Event_11215250(15, obj=1211315, vfx_id=1213175)
    Event_11215250(16, obj=1211316, vfx_id=1213176)
    Event_11215250(17, obj=1211317, vfx_id=1213177)
    Event_11215250(18, obj=1211318, vfx_id=1213178)
    Event_11215250(19, obj=1211319, vfx_id=1213179)
    Event_11215250(20, obj=1211320, vfx_id=1213180)
    Event_11215250(21, obj=1211321, vfx_id=1213181)
    Event_11215250(22, obj=1211322, vfx_id=1213182)
    Event_11215250(23, obj=1211323, vfx_id=1213183)
    Event_11215160(0, character=1210600)
    Event_11215165(0, character=1210600)
    Event_11215170(0, character=1210600)
    Event_11215175(0, character=1210600)
    Event_11215180(0, character=1210600, region=1212180)
    Event_11210680(0, character=1210600)
    Event_11215185(0, character=1210600)
    SetNetworkUpdateRate(1210601, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Event_11215160(1, character=1210601)
    Event_11215165(1, character=1210601)
    Event_11215170(1, character=1210601)
    Event_11215175(1, character=1210601)
    Event_11215180(1, character=1210601, region=1212181)
    Event_11210680(1, character=1210601)
    Event_11215185(1, character=1210601)
    Event_11219113()
    Event_11219114()
    RunEvent(4294967295, slot=0, args=(0,))
    Event_11213888()
    Event_11215846(0, left=11210000, obj=1211790, vfx_id=1211791)
    Event_11215843(0, left=11210000, line_intersects=1211790, anchor_entity=1212888, target_entity=1212887)
    Event_11215846(1, left=11210001, obj=1211890, vfx_id=1211891)
    Event_11215843(1, left=11210001, line_intersects=1211890, anchor_entity=1212898, target_entity=1212897)
    Event_11215846(2, left=11210004, obj=1211690, vfx_id=1211691)
    Event_11215843(2, left=11210004, line_intersects=1211690, anchor_entity=1212908, target_entity=1212907)
    Event_11215846(3, left=11210002, obj=1211990, vfx_id=1211991)
    Event_11215843(3, 11210002, 1211990, 1212998, 1212997)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableCharacter(6731)
    Event_11215030(
        1,
        character=6732,
        flag=11215036,
        flag_1=11215035,
        flag_2=11210901,
        anchor_entity=1212082,
        region=1212083,
        flag_3=11215032,
        flag_4=11210900
    )
    Event_11210900(0, character=6731)
    Event_11210900(1, character=6732)
    Event_11210905(
        0,
        character=6731,
        flag=11215035,
        destination=1212080,
        set_draw_parent=1213030,
        flag_1=11210900,
        flag_2=11215032
    )
    Event_11210905(
        1,
        character=6732,
        flag=11215036,
        destination=1212082,
        set_draw_parent=1213031,
        flag_1=11210901,
        flag_2=11215033
    )
    Event_11210510(0, character=6720, flag=1822)
    Event_11210520(0, character=6720, first_flag=1820, last_flag=1839, flag=1823)
    Event_11210530(0, character=6720, first_flag=1820, last_flag=1839, flag=1821)
    Event_11210535()
    Event_11210910()
    Event_11210912()
    Event_11210915()
    SkipLinesIfFlagDisabled(2, 1842)
    DisableObject(1211130)
    DeleteVFX(1213150, erase_root_only=False)
    Event_11210510(1, character=6730, flag=1841)
    Event_11210520(1, character=6730, first_flag=1840, last_flag=1859, flag=1842)
    Event_11210544()
    Event_11210538()
    Event_11210520(2, character=6750, first_flag=1870, last_flag=1889, flag=1872)
    SkipLinesIfFlagEnabled(1, 11210001)
    DisableObject(1211220)
    IfFlagEnabled(-1, 1861)
    IfFlagEnabled(-1, 1862)
    SkipLinesIfConditionTrue(1, -1)
    DisableCharacter(6740)
    Event_11210510(3, character=6740, flag=1863)
    Event_11210520(3, character=6740, first_flag=1860, last_flag=1869, flag=1864)
    Event_11210531(0, character=6740, first_flag=1860, last_flag=1869, flag=1861)
    Event_11210532(0, character=6740, first_flag=1860, last_flag=1869, flag=1862)
    Event_11210533(0, character=6740, first_flag=1860, last_flag=1869, flag=1865)
    Event_11210534(0, character=6740, first_flag=1860, last_flag=1869, flag=1865)
    Event_11210543()
    DisableCharacter(6700)
    SkipLinesIfClient(3)
    Event_11210540()
    Event_11210541()
    Event_11210542()
    SkipLinesIfFlagEnabled(1, 11210345)
    DisableFlagRange((11210340, 11210345))
    DisableGravity(6760)
    EnableImmortality(6760)
    DisableHealthBar(6760)
    AddSpecialEffect(6760, 5300)
    EnableObjectInvulnerability(1211250)
    Event_11210340()
    Event_11210341()
    Event_11210345()
    Event_11210346()
    Event_11210347()
    EndOfAnimation(obj=1211606, animation_id=0)
    EndOfAnimation(obj=1211607, animation_id=0)
    Event_11217000()
    Event_11210015()


@NeverRestart(11210090)
def Event_11210090(_, line_intersects__obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11210090"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    End()
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=line_intersects__obj,
    )
    IfActionButton(
        2,
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        line_intersects=line_intersects__obj,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(line_intersects__obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11215090)
def Event_11215090():
    """Event 11215090"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1210900)
    DisableCharacter(1210901)
    DisableCharacter(1210902)
    DisableCharacter(1210903)
    DisableCharacter(1210904)
    DisableCharacter(1210905)
    DisableCharacter(1210906)
    DisableCharacter(1210907)
    DisableCharacter(1210908)
    DisableCharacter(1210909)
    DisableCharacter(1210910)
    DisableCharacter(1210911)
    DisableCharacter(1210912)
    DisableCharacter(1210913)
    DisableCharacter(1210914)
    DisableCharacter(1210915)
    DisableCharacter(1210916)
    DisableCharacter(1210917)
    DisableCharacter(1210918)
    DisableCharacter(1210919)
    DisableCharacter(1210920)
    DisableCharacter(1210921)
    DisableCharacter(1210922)
    DisableCharacter(1210923)
    DisableCharacter(1210924)
    DisableCharacter(1210925)
    IfFlagEnabled(0, 11210080)
    EndIfFlagEnabled(735)
    EnableFlag(5000)
    EnableCharacter(1210900)
    EnableCharacter(1210901)
    EnableCharacter(1210902)
    EnableCharacter(1210903)
    EnableCharacter(1210904)
    EnableCharacter(1210905)
    EnableCharacter(1210906)
    EnableCharacter(1210907)
    EnableCharacter(1210908)
    EnableCharacter(1210909)
    EnableCharacter(1210910)
    EnableCharacter(1210911)
    EnableCharacter(1210912)
    EnableCharacter(1210913)
    EnableCharacter(1210914)
    EnableCharacter(1210915)
    EnableCharacter(1210916)
    EnableCharacter(1210917)
    EnableCharacter(1210918)
    EnableCharacter(1210919)
    EnableCharacter(1210920)
    EnableCharacter(1210921)
    EnableCharacter(1210922)
    EnableCharacter(1210923)
    EnableCharacter(1210924)
    EnableCharacter(1210925)


@RestartOnRest(11215091)
def Event_11215091():
    """Event 11215091"""
    IfFlagEnabled(-1, 11215095)
    IfFlagEnabled(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagDisabled(1, 735)
    DisableFlag(735)
    DisableFlag(11210080)
    DisableFlag(11215095)
    EnableFlag(5001)
    Kill(1210900)
    Kill(1210901)
    Kill(1210902)
    Kill(1210903)
    Kill(1210904)
    Kill(1210905)
    Kill(1210906)
    Kill(1210907)
    Kill(1210908)
    Kill(1210909)
    Kill(1210910)
    Kill(1210911)
    Kill(1210912)
    Kill(1210913)
    Kill(1210914)
    Kill(1210915)
    Kill(1210916)
    Kill(1210917)
    Kill(1210918)
    Kill(1210919)
    Kill(1210920)
    Kill(1210921)
    Kill(1210922)
    Kill(1210923)
    Kill(1210924)
    Kill(1210925)


@RestartOnRest(11215092)
def Event_11215092():
    """Event 11215092"""
    EndIfClient()
    IfBlackWorldTendencyComparison(1, ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=OOLACILE)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, 11210080)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(2, ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=OOLACILE)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, 11210080)
    RestartIfConditionFalse(-2)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(3, ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=OOLACILE)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 11210080)
    RestartIfConditionFalse(-3)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(4, ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=OOLACILE)
    IfConditionTrue(-4, input_condition=4)
    IfFlagEnabled(-4, 11210080)
    RestartIfConditionFalse(-4)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(5, ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=OOLACILE)
    IfConditionTrue(-5, input_condition=5)
    IfFlagEnabled(-5, 11210080)
    RestartIfConditionFalse(-5)
    WaitFrames(frames=1)
    IfBlackWorldTendencyComparison(6, ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=OOLACILE)
    IfConditionTrue(-6, input_condition=6)
    IfFlagEnabled(-6, 11210080)
    RestartIfConditionFalse(-6)
    EnableFlag(11210080)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=OOLACILE)
    RestartIfConditionFalse(7)
    DisableFlag(11210080)
    EnableFlag(11215095)


@RestartOnRest(11215000)
def Event_11215000():
    """Event 11215000"""
    IfFlagDisabled(1, 11210000)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212888,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1211790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=1)
    Restart()


@NeverRestart(11215001)
def Event_11215001():
    """Event 11215001"""
    IfFlagDisabled(1, 11210000)
    IfFlagEnabled(1, 11215003)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212888,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211790,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212887)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11215002)
def Event_11215002():
    """Event 11215002"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11210000)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210800, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210800)


@RestartOnRest(11215003)
def Event_11215003():
    """Event 11215003"""
    SkipLinesIfThisEventFlagEnabled(5)
    DisableAI(1210800)
    IfFlagEnabled(1, 11215002)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1210800)
    EnableBossHealthBar(1210800, name=3471)
    ForceAnimation(1210800, 3017, wait_for_completion=1)


@NeverRestart(11215004)
def Event_11215004():
    """Event 11215004"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11210000)
    IfFlagEnabled(1, 11215003)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11215001)
    IfCharacterInsideRegion(1, PLAYER, region=1212886)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1213800)


@NeverRestart(11215005)
def Event_11215005():
    """Event 11215005"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215004)
    IfFlagEnabled(1, 11210000)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1213800)


@RestartOnRest(11210000)
def Event_11210000():
    """Event 11210000"""
    SkipLinesIfThisEventFlagDisabled(5)
    DisableCharacter(1210800)
    Kill(1210800)
    DisableCharacter(1210810)
    Kill(1210810)
    End()
    IfHealthLessThanOrEqual(0, 1210800, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1210800, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1210800)
    EnableFlag(11210000)
    KillBoss(game_area_param_id=1210800)
    DisableObject(1211790)
    DeleteVFX(1211791)
    DisableObject(1211792)
    DeleteVFX(1211793)


@RestartOnRest(11215006)
def Event_11215006(_, character: int, character_1: int, item_lot_param_id: int):
    """Event 11215006"""
    DisableCharacter(character)
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(character_1, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character_1, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(character_1, command_id=20, command_slot=0)
    End()
    SkipLinesIfFlagEnabled(1, 11210000)
    IfFlagEnabled(1, 11215002)
    IfCharacterBackreadEnabled(1, character_1)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character_1, npc_part_id=3471, part_index=NPCPartType.Part1, part_health=200)
    IfCharacterPartHealthLessThanOrEqual(2, character_1, npc_part_id=3471, value=0)
    IfHealthLessThanOrEqual(3, character_1, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    Move(
        character,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=character_1,
    )
    EnableCharacter(character)
    ResetAnimation(character_1)
    ForceAnimation(character_1, 8000)
    ForceAnimation(character, 8100)
    SetDisplayMask(character_1, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character_1, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(character_1, command_id=20, command_slot=0)
    ReplanAI(character_1)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)


@RestartOnRest(11215008)
def Event_11215008():
    """Event 11215008"""
    IfFlagEnabled(0, 11215007)
    IfPlayerStandingOnCollision(-1, 1213020)
    IfPlayerStandingOnCollision(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=1212003)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(3, condition=-1)
    SetNest(1210801, region=1212010)
    SetNest(1210802, region=1212011)
    SkipLines(2)
    SetNest(1210801, region=1212007)
    SetNest(1210802, region=1212008)
    AICommand(1210801, command_id=10, command_slot=1)
    AICommand(1210802, command_id=10, command_slot=1)
    IfPlayerStandingOnCollision(-2, 1213020)
    IfPlayerStandingOnCollision(-2, 1213021)
    IfCharacterInsideRegion(-2, PLAYER, region=1212003)
    IfConditionFalse(0, input_condition=-2)
    AICommand(1210801, command_id=-1, command_slot=1)
    AICommand(1210802, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(11215007)
def Event_11215007():
    """Event 11215007"""
    IfFlagEnabled(0, 11210001)
    DisableAI(1210801)
    DisableAI(1210802)
    IfCharacterInsideRegion(1, PLAYER, region=1212004)
    IfCharacterOutsideRegion(1, PLAYER, region=1212001)
    IfCharacterOutsideRegion(1, PLAYER, region=1212002)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, attacked_entity=1210801, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1210802, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1210801)
    ForceAnimation(1210801, 3017)
    WaitFrames(frames=15)
    EnableAI(1210802)
    ForceAnimation(1210802, 3017)
    WaitFrames(frames=15)
    ReplanAI(1210801)
    ReplanAI(1210802)


@RestartOnRest(11215009)
def Event_11215009():
    """Event 11215009"""
    IfFlagEnabled(0, 11210001)
    IfCharacterInsideRegion(0, PLAYER, region=1212006)
    Move(1210801, destination=1212007, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    Move(1210802, destination=1212008, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    SetNest(1210801, region=1212007)
    SetNest(1210802, region=1212008)
    IfCharacterInsideRegion(0, PLAYER, region=1212009)
    Move(1210801, destination=1212010, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    Move(1210802, destination=1212011, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    SetNest(1210801, region=1212010)
    SetNest(1210802, region=1212011)
    Restart()


@NeverRestart(11217000)
def Event_11217000():
    """Event 11217000"""
    IfCharacterInsideRegion(3, PLAYER, region=1212005)
    IfCharacterOutsideRegion(4, PLAYER, region=1212005)
    EndIfConditionTrue(4)
    IfCharacterDead(1, 1210801)
    IfCharacterDead(2, 1210802)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    Move(1210801, destination=1212007, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    SetNest(1210801, region=1212007)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    Move(1210802, destination=1212008, destination_type=CoordEntityType.Region, copy_draw_parent=1210800)
    SetNest(1210802, region=1212008)


@RestartOnRest(11215010)
def Event_11215010():
    """Event 11215010"""
    IfFlagDisabled(1, 11210001)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212898,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1211890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=1)
    Restart()


@NeverRestart(11215011)
def Event_11215011():
    """Event 11215011"""
    IfFlagDisabled(1, 11210001)
    IfFlagEnabled(1, 11215013)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211890,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212897)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11215012)
def Event_11215012():
    """Event 11215012"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11210001)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210820, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210820)
    EnableFlag(11210537)


@RestartOnRest(11215013)
def Event_11215013():
    """Event 11215013"""
    SkipLinesIfFlagDisabled(3, 11210001)
    DisableCharacter(1210820)
    Kill(1210820)
    End()
    SkipLinesIfFlagEnabled(3, 11210030)
    DisableCharacter(1210820)
    DisableObject(1211100)
    DisableObject(1211101)
    DisableAI(1210820)
    SkipLinesIfThisEventFlagEnabled(11)
    IfFlagEnabled(1, 11215012)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(9, 11210030)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120110, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(120110, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableObject(1211100)
    EnableObject(1211101)
    EnableCharacter(1210820)
    EnableFlag(11210030)
    EnableAI(1210820)
    EnableBossHealthBar(1210820, name=4100)
    EnableMapCollision(collision=1213001)


@NeverRestart(11215014)
def Event_11215014():
    """Event 11215014"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11210001)
    IfFlagEnabled(1, 11215013)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 11215011)
    IfCharacterInsideRegion(1, PLAYER, region=1212896)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1213801)


@NeverRestart(11215015)
def Event_11215015():
    """Event 11215015"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215014)
    IfFlagEnabled(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1213801)


@RestartOnRest(11210001)
def Event_11210001():
    """Event 11210001"""
    SkipLinesIfThisEventFlagDisabled(6)
    DisableCharacter(1210820)
    Kill(1210820)
    DisableBackread(1210820)
    EnableCharacter(1210801)
    EnableCharacter(1210802)
    End()
    DisableBackread(6720)
    DisableCharacter(1210801)
    DisableCharacter(1210802)
    IfHealthLessThanOrEqual(0, 1210820, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1210820, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1210820)
    EnableFlag(11210001)
    EnableFlag(121)
    KillBoss(game_area_param_id=1210820)
    DisableFlag(11217060)
    DisableFlag(11217070)
    DisableFlag(11217080)
    DisableFlag(11217090)
    DisableObject(1211890)
    DeleteVFX(1211891)
    DisableObject(1211892)
    DeleteVFX(1211893)
    DisableMapCollision(collision=1213001)
    Wait(17.0)
    DisableBackread(1210820)
    EnableBackread(6720)
    EnableCharacter(1210801)
    EnableCharacter(1210802)


@NeverRestart(11210015)
def Event_11210015():
    """Event 11210015"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11210001)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=6720, radius=80.0)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(6720)
    IfFlagEnabled(2, 11210001)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=6720, radius=80.0)
    IfConditionTrue(0, input_condition=2)
    EnableBackread(6720)
    Restart()


@RestartOnRest(11215020)
def Event_11215020():
    """Event 11215020"""
    IfFlagDisabled(1, 11210002)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212998,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1211990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=1)
    Restart()


@NeverRestart(11215021)
def Event_11215021():
    """Event 11215021"""
    IfFlagDisabled(1, 11210002)
    IfFlagEnabled(1, 11215023)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211990,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11215022)
def Event_11215022():
    """Event 11215022"""
    SkipLinesIfThisEventFlagEnabled(3)
    IfFlagDisabled(1, 11210002)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210840, authority_level=UpdateAuthority.Forced)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagEnabled(0, 703)
    ActivateMultiplayerBuffs(1210840)


@NeverRestart(11215027)
def Event_11215027():
    """Event 11215027"""
    IfFlagEnabled(1, 11215020)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120140, cutscene_flags=0, player_id=10000, move_to_region=1212022, game_map=OOLACILE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120140,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1212022,
        game_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutscene(120140, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11210031)


@RestartOnRest(11215026)
def Event_11215026():
    """Event 11215026"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@RestartOnRest(11215023)
def Event_11215023():
    """Event 11215023"""
    EndIfFlagEnabled(17)
    SkipLinesIfThisEventFlagEnabled(3)
    DisableAI(1210840)
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableAI(1210840)
    EnableBossHealthBar(1210840, name=4500)


@NeverRestart(11215024)
def Event_11215024():
    """Event 11215024"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11210002)
    IfFlagEnabled(1, 11215023)
    SkipLinesIfHost(3)
    IfFlagEnabled(1, 11215021)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1213802)


@NeverRestart(11215025)
def Event_11215025():
    """Event 11215025"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215024)
    IfFlagEnabled(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1213802)


@NeverRestart(11210002)
def Event_11210002():
    """Event 11210002"""
    DisableObject(1211950)
    DisableObject(1211950)
    SkipLinesIfThisEventFlagDisabled(4)
    DisableCharacter(1210840)
    Kill(1210840)
    EnableObject(1211950)
    End()
    IfHealthLessThanOrEqual(0, 1210840, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1210840, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1210840)
    EnableFlag(11210002)
    EnableFlag(17)
    KillBoss(game_area_param_id=1210840)
    DisableObject(1211990)
    DeleteVFX(1211991)
    DeleteVFX(1213100)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1211950, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1211950)
    RegisterBonfire(bonfire_flag=11210992, obj=1211950)


@NeverRestart(11215250)
def Event_11215250(_, obj: int, vfx_id: int):
    """Event 11215250"""
    DeleteVFX(vfx_id, erase_root_only=False)
    SkipLinesIfFlagDisabled(2, 11210002)
    DisableObject(obj)
    End()
    IfObjectDestroyed(-1, obj)
    IfCharacterDead(-1, 1210840)
    IfConditionTrue(0, input_condition=-1)
    DestroyObject(obj)
    ForceAnimation(obj, 0, wait_for_completion=1)
    DisableObject(obj)


@RestartOnRest(11215060)
def Event_11215060():
    """Event 11215060"""
    IfFlagEnabled(1, 11210592)
    IfFlagDisabled(1, 11210004)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=1211690,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212907)
    ForceAnimation(PLAYER, 7410, wait_for_completion=1)
    Restart()


@NeverRestart(11215061)
def Event_11215061():
    """Event 11215061"""
    IfFlagEnabled(1, 11210592)
    IfFlagDisabled(1, 11210004)
    IfFlagEnabled(1, 11215062)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211690,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=1212907)
    ForceAnimation(PLAYER, 7410)
    Restart()


@NeverRestart(11215062)
def Event_11215062():
    """Event 11215062"""
    SkipLinesIfThisEventFlagEnabled(4)
    IfFlagEnabled(1, 11210592)
    IfFlagDisabled(1, 11210004)
    IfCharacterInsideRegion(1, PLAYER, region=1212909)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210401, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210401)


@RestartOnRest(11215063)
def Event_11215063():
    """Event 11215063"""
    EnableInvincibility(1210401)
    SkipLinesIfThisEventFlagEnabled(9)
    DisableAI(1210401)
    IfFlagEnabled(1, 11215062)
    IfCharacterInsideRegion(1, PLAYER, region=1212906)
    IfPlayerStandingOnCollision(-1, 1213003)
    IfPlayerStandingOnCollision(-1, 1213004)
    IfPlayerStandingOnCollision(-1, 1213009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1210401)
    DisableInvincibility(1210401)
    EnableBossHealthBar(1210401, name=4510)
    EnableMapCollision(collision=1213001)


@NeverRestart(11215064)
def Event_11215064():
    """Event 11215064"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11210004)
    IfFlagEnabled(1, 11215063)
    SkipLinesIfHost(2)
    IfFlagEnabled(1, 11215061)
    IfFlagEnabled(1, 11215067)
    IfCharacterInsideRegion(1, PLAYER, region=1212900)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=1213803)


@NeverRestart(11215065)
def Event_11215065():
    """Event 11215065"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215064)
    IfFlagEnabled(1, 11210004)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(sound_id=1213803)


@NeverRestart(11215066)
def Event_11215066():
    """Event 11215066"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11210592)
    IfFlagDisabled(1, 11210004)
    IfFlagEnabled(1, 11215062)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=1212908,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1211690,
    )
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=75)
    EnableFlag(11215067)


@NeverRestart(11210005)
def Event_11210005():
    """Event 11210005"""
    EndIfThisEventFlagEnabled()
    IfHealthLessThanOrEqual(0, 1210401, value=0.0)
    Wait(1.0)
    PlaySoundEffect(1210401, 777777777, sound_type=SoundType.s_SFX)
    IfCharacterDead(0, 1210401)
    EnableFlag(11210004)
    EnableFlag(11210005)
    EnableFlag(121)
    KillBoss(game_area_param_id=1210401)
    DisableObject(1211690)
    DeleteVFX(1211691)
    DisableMapCollision(collision=1213001)


@NeverRestart(11210340)
def Event_11210340():
    """Event 11210340"""
    SkipLinesIfThisEventFlagDisabled(3)
    EndIfFlagEnabled(11210341)
    Move(6760, destination=1212331, destination_type=CoordEntityType.Region, copy_draw_parent=6760)
    End()
    IfHost(1)
    IfEntityWithinDistance(-1, entity=6760, other_entity=PLAYER, radius=7.0)
    IfAttacked(-1, attacked_entity=6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_Unknown_2003_46(
        entity=6760,
        animation=7003,
        loop=0,
        wait_for_completion=1,
        skip_transition=0,
        unk1=5.0,
    )
    DisableCharacter(6760)
    Move(6760, destination=1212331, destination_type=CoordEntityType.Region, copy_draw_parent=6760)
    EnableCharacter(6760)


@NeverRestart(11210341)
def Event_11210341():
    """Event 11210341"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    Move(6760, destination=1212332, destination_type=CoordEntityType.Region, copy_draw_parent=6760)
    End()
    IfHost(1)
    IfFlagEnabled(1, 11210340)
    IfEntityWithinDistance(-1, entity=6760, other_entity=PLAYER, radius=12.0)
    IfAttacked(-1, attacked_entity=6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_Unknown_2003_46(
        entity=6760,
        animation=7003,
        loop=0,
        wait_for_completion=1,
        skip_transition=0,
        unk1=5.0,
    )
    DisableCharacter(6760)
    Move(6760, destination=1212332, destination_type=CoordEntityType.Region, copy_draw_parent=6760)
    EnableCharacter(6760)


@NeverRestart(11210345)
def Event_11210345():
    """Event 11210345"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableCharacter(6760)
    DeleteVFX(1213125, erase_root_only=False)
    End()
    IfHost(1)
    IfFlagEnabled(1, 11210341)
    IfEntityWithinDistance(-1, entity=6760, other_entity=PLAYER, radius=12.0)
    IfAttacked(-1, attacked_entity=6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_Unknown_2003_46(
        entity=6760,
        animation=7003,
        loop=0,
        wait_for_completion=1,
        skip_transition=0,
        unk1=5.0,
    )
    DisableCharacter(6760)
    DeleteVFX(1213125)


@NeverRestart(11210346)
def Event_11210346():
    """Event 11210346"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11210345)
    IfCharacterInsideRegion(1, PLAYER, region=1212335)
    IfFlagEnabled(2, 11210345)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    AddSpecialEffect(PLAYER, 4161)
    Restart()


@NeverRestart(11210347)
def Event_11210347():
    """Event 11210347"""
    SkipLinesIfFlagEnabled(1, 11215045)
    SkipLinesIfFlagDisabled(2, 11210345)
    DisableObject(1211250)
    End()
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212336)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215045)
    EndIfObjectDestroyed(1211250)
    DisableObjectInvulnerability(1211250)
    DestroyObject(1211250)
    ForceAnimation(1211250, 0)
    PlaySoundEffect(1211250, 262000000, sound_type=SoundType.o_Object)


@NeverRestart(11210025)
def Event_11210025():
    """Event 11210025"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(1211240)
    End()
    IfObjectDestroyed(0, 1211240)
    End()


@RestartOnRest(11210310)
def Event_11210310(_, character: int, flag: int):
    """Event 11210310"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(character)
    Kill(character)
    End()
    IfCharacterDead(0, character)
    EnableFlag(flag)


@NeverRestart(11210330)
def Event_11210330(_, first_flag: int, last_flag: int, flag: int):
    """Event 11210330"""
    IfFlagRangeAllEnabled(0, flag_range=(first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210021)
def Event_11210021():
    """Event 11210021"""
    DisableAI(1210502)
    EnableInvincibility(1210502)
    SkipLinesIfFlagDisabled(5, 11210330)
    DisableCharacter(1210502)
    DropMandatoryTreasure(1210502)
    DeleteVFX(1213110, erase_root_only=False)
    DisableObject(1211230)
    End()
    IfFlagEnabled(0, 11210330)
    Wait(6.0)
    ForceAnimation(1210502, 7010, wait_for_completion=1)
    DisableCharacter(1210502)
    DropMandatoryTreasure(1210502)
    DeleteVFX(1213110)
    DisableObject(1211230)


@RestartOnRest(11215040)
def Event_11215040():
    """Event 11215040"""
    DisableAI(1210500)
    DisableCharacter(1210500)
    IfFlagDisabled(1, 17)
    IfFlagEnabled(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfActionButton(1, prompt_text=50000000, anchor_entity=1212300, anchor_type=CoordEntityType.Region, model_point=0)
    IfConditionTrue(0, input_condition=1)
    DisplayBattlefieldMessage(140010, display_location_index=0)
    SkipLinesIfClient(1)
    ForceAnimation(1210501, 7008)
    WaitFrames(frames=30)
    DisableCharacter(1210501)
    EnableFlag(11215042)
    DeleteVFX(1213100)
    Wait(10.0)
    EnableCharacter(1210500)
    EnableAI(1210500)
    SetTeamType(1210500, TeamType.WhitePhantom)
    ForceAnimation(1210500, 7004)
    SkipLinesIfClient(2)
    DisplayBattlefieldMessage(20001110, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(20001111, display_location_index=0)
    WaitFrames(frames=140)


@RestartOnRest(11215041)
def Event_11215041():
    """Event 11215041"""
    DisableCharacter(1210501)
    DisableAI(1210501)
    DisableAnimations(1210501)
    EndIfClient()
    IfFlagEnabled(1, 11210021)
    IfFlagDisabled(1, 17)
    IfCharacterInsideRegion(1, PLAYER, region=1212300)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagEnabled(11215042)
    EnableCharacter(1210501)
    ForceAnimation(1210501, 7006, wait_for_completion=1)
    ForceAnimation(1210501, 7007, loop=1)
    IfCharacterOutsideRegion(2, PLAYER, region=1212300)
    IfFlagEnabled(2, 11215020)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(1210501, 7008, wait_for_completion=1)
    DisableCharacter(1210501)
    Restart()


@RestartOnRest(11215044)
def Event_11215044():
    """Event 11215044"""
    DeleteVFX(1213100)
    EndIfClient()
    IfFlagDisabled(1, 17)
    IfFlagEnabled(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(1213100)
    IfFlagDisabled(2, 17)
    IfFlagEnabled(2, 11210021)
    IfCharacterHuman(2, PLAYER)
    IfConditionFalse(0, input_condition=2)
    Restart()


@NeverRestart(11210020)
def Event_11210020():
    """Event 11210020"""
    EndIfFlagEnabled(17)
    IfCharacterDead(1, 1210840)
    IfCharacterAlive(1, 1210500)
    IfFlagEnabled(1, 11215040)
    IfCharacterDead(2, 1210500)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    DisableAI(1210500)
    WaitFrames(frames=120)
    ForceAnimation(1210500, 7005, wait_for_completion=1)
    DisableCharacter(1210500)
    End()
    DisplayBattlefieldMessage(20001115, display_location_index=0)


@RestartOnRest(11215043)
def Event_11215043():
    """Event 11215043"""
    SkipLinesIfThisEventFlagEnabled(1)
    IfHealthLessThanOrEqual(0, 1210500, value=0.30000001192092896)
    AddSpecialEffect(1210500, 5401)


@RestartOnRest(11215100)
def Event_11215100():
    """Event 11215100"""
    EndIfThisEventFlagEnabled()
    DisableAI(1210100)
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(3, input_condition=7)
    IfCharacterInsideRegion(3, PLAYER, region=1212502)
    IfConditionTrue(-3, input_condition=3)
    IfAttacked(-3, attacked_entity=1210100, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-3)
    IfConditionFalse(2, input_condition=7)
    IfCharacterInsideRegion(2, PLAYER, region=1212500)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(1210100, cancel_animation=9060)
    EnableAI(1210100)
    EndIfFinishedConditionTrue(input_condition=1)
    SetNest(1210100, region=1212501)
    AICommand(1210100, command_id=10, command_slot=0)
    ReplanAI(1210100)
    Wait(6.0)
    IfCharacterInsideRegion(-2, PLAYER, region=1212502)
    IfAttacked(-2, attacked_entity=1210100, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1210100, command_id=-1, command_slot=0)
    ReplanAI(1210100)


@RestartOnRest(11215110)
def Event_11215110(_, character: int, region: int, radius: float, region_1: int):
    """Event 11215110"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    DisableAI(character)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=character, radius=radius)
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11215115)
def Event_11215115(_, character: int, region: int, region_1: int):
    """Event 11215115"""
    IfCharacterInsideRegion(0, character, region=region)
    SetNest(character, region=region_1)


@RestartOnRest(11215120)
def Event_11215120(_, character: int, character_1: int, character_2: int, flag: int):
    """Event 11215120"""
    SkipLinesIfThisEventFlagDisabled(4)
    SetStandbyAnimationSettings(character)
    SetStandbyAnimationSettings(character_1)
    SetStandbyAnimationSettings(character_2)
    End()
    DisableAI(character)
    DisableAI(character_1)
    DisableAI(character_2)
    IfHost(1)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=character_1, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=character_2, attacker=PLAYER)
    SkipLinesIfClient(2)
    SkipLinesIfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(character)
    EnableAI(character_1)
    EnableAI(character_2)
    SetStandbyAnimationSettings(character, cancel_animation=9060)
    SetStandbyAnimationSettings(character_1, cancel_animation=9060)
    SetStandbyAnimationSettings(character_2, cancel_animation=9060)


@RestartOnRest(11215130)
def Event_11215130(_, character: int, other_entity: int, radius: float, seconds: float):
    """Event 11215130"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    SetStandbyAnimationSettings(character)
    End()
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=other_entity, radius=radius)
    IfAttacked(-1, attacked_entity=1210108, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1210109, attacker=PLAYER)
    IfAttacked(-1, attacked_entity=1210110, attacker=PLAYER)
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(seconds)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11215140)
def Event_11215140(_, character: int, region: int, region_1: int, region_2: int, flag: int, flag_1: int, flag_2: int):
    """Event 11215140"""
    IfCharacterInsideRegion(1, character, region=region)
    IfFlagDisabled(1, flag)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(2, character, region=region_1)
    IfFlagDisabled(2, flag_1)
    IfHasAIStatus(2, character, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(3, character, region=region_2)
    IfFlagDisabled(3, flag_2)
    IfHasAIStatus(3, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(3, condition=1)
    EnableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionFalse(3, condition=2)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)
    SkipLinesIfFinishedConditionFalse(3, condition=3)
    DisableFlag(flag)
    DisableFlag(flag_1)
    EnableFlag(flag_2)
    ResetAnimation(character)
    ForceAnimation(character, 7000, skip_transition=1)
    WaitFrames(frames=25)
    ForceAnimation(character, 9000, skip_transition=1)
    WaitFrames(frames=190)
    ForceAnimation(character, 9060)
    WaitFrames(frames=35)
    Restart()


@NeverRestart(11210600)
def Event_11210600(_, obj: int, obj_act_id: int):
    """Event 11210600"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj, animation_id=0)
    SetObjectActivation(obj, obj_act_id=-1, state=0)
    EnableTreasure(obj=obj)
    End()
    DisableTreasure(obj=obj)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11210350)
def Event_11210350(_, character: int, item_lot_param_id: int):
    """Event 11210350"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableCharacter(character)
    Kill(character)
    End()
    IfCharacterDead(0, character)
    EndIfEqual(left=item_lot_param_id, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot_param_id, host_only=True)


@RestartOnRest(11210150)
def Event_11210150():
    """Event 11210150"""
    EndIfFlagEnabled(11210160)
    Move(1210350, destination=1212143, destination_type=CoordEntityType.Region, set_draw_parent=1213040)
    Move(1210350, destination=1212150, destination_type=CoordEntityType.Region, set_draw_parent=1213040)
    SetNest(1210350, region=1212150)


@NeverRestart(11210100)
def Event_11210100():
    """Event 11210100"""
    SkipLinesIfFlagDisabled(1, 11210101)
    EndOfAnimation(obj=1211000, animation_id=0)
    SkipLinesIfFlagEnabled(1, 11210101)
    EndOfAnimation(obj=1211000, animation_id=10)
    IfFlagEnabled(0, 11210103)
    IfFlagDisabled(0, 11215220)
    IfFlagDisabled(1, 11210101)
    IfCharacterInsideRegion(1, PLAYER, region=1212101)
    IfFlagEnabled(2, 11210102)
    IfFlagEnabled(2, 11210101)
    IfCharacterInsideRegion(2, PLAYER, region=1212100)
    IfFlagEnabled(3, 11210102)
    IfFlagDisabled(3, 11210101)
    IfCharacterInsideRegion(3, PLAYER, region=1212102)
    IfFlagEnabled(4, 11210101)
    IfCharacterInsideRegion(4, PLAYER, region=1212103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionTrue(26, condition=2)
    SkipLinesIfFinishedConditionTrue(25, condition=4)
    EnableFlag(11210102)
    EnableFlag(11218102)
    SkipLinesIfFinishedConditionTrue(11, condition=1)
    IfAllPlayersOutsideRegion(-2, region=1212102)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagDisabled(7, 11218102)
    IfFlagDisabled(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212100)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagDisabled(7, 11218102)
    IfFlagDisabled(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    EnableFlag(11218103)
    SkipLinesIfFinishedConditionTrue(11, condition=2)
    IfAllPlayersOutsideRegion(-3, region=1212103)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagDisabled(8, 11218102)
    IfFlagDisabled(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212101)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagDisabled(8, 11218102)
    IfFlagDisabled(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()


@NeverRestart(11219100)
def Event_11219100(_, flag: int, obj: int, animation_id: int, state: uchar, anchor_entity: int):
    """Event 11219100"""
    IfFlagEnabled(0, flag)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=anchor_entity, model_point=101, anchor_type=CoordEntityType.Object)
    SetFlagState(11210101, state)
    CreateObjectVFX(obj, vfx_id=191, model_point=120029)
    ForceAnimation(obj, animation_id)
    WaitFrames(frames=180)
    DeleteObjectVFX(obj, erase_root=False)
    DisableFlag(flag)
    Restart()


@NeverRestart(11210103)
def Event_11210103():
    """Event 11210103"""
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1212104)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210103)


@NeverRestart(11210110)
def Event_11210110():
    """Event 11210110"""
    SkipLinesIfFlagDisabled(1, 11210111)
    EndOfAnimation(obj=1211010, animation_id=11)
    SkipLinesIfFlagEnabled(1, 11210111)
    EndOfAnimation(obj=1211010, animation_id=1)
    IfFlagDisabled(0, 11215221)
    IfFlagEnabled(1, 11210111)
    IfCharacterInsideRegion(1, PLAYER, region=1212111)
    IfFlagDisabled(2, 11210111)
    IfCharacterInsideRegion(2, PLAYER, region=1212110)
    IfFlagEnabled(3, 11210111)
    IfCharacterInsideRegion(3, PLAYER, region=1212112)
    IfFlagDisabled(4, 11210111)
    IfCharacterInsideRegion(4, PLAYER, region=1212113)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215221)
    SkipLinesIfFinishedConditionTrue(24, condition=2)
    SkipLinesIfFinishedConditionTrue(23, condition=4)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211011, model_point=101, anchor_type=CoordEntityType.Object)
    DisableFlag(11210111)
    CreateObjectVFX(1211010, vfx_id=191, model_point=120029)
    ForceAnimation(1211010, 1)
    WaitFrames(frames=140)
    DeleteObjectVFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=1)
    IfAllPlayersOutsideRegion(-2, region=1212112)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212110)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211012, model_point=101, anchor_type=CoordEntityType.Object)
    EnableFlag(11210111)
    CreateObjectVFX(1211010, vfx_id=191, model_point=120029)
    ForceAnimation(1211010, 11)
    WaitFrames(frames=140)
    DeleteObjectVFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=2)
    IfAllPlayersOutsideRegion(-3, region=1212113)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212111)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()


@NeverRestart(11210120)
def Event_11210120():
    """Event 11210120"""
    SkipLinesIfFlagDisabled(1, 11210121)
    EndOfAnimation(obj=1211020, animation_id=2)
    SkipLinesIfFlagEnabled(1, 11210121)
    EndOfAnimation(obj=1211020, animation_id=12)
    IfFlagEnabled(0, 11210123)
    IfFlagDisabled(0, 11215222)
    IfFlagDisabled(1, 11210121)
    IfCharacterInsideRegion(1, PLAYER, region=1212121)
    IfFlagEnabled(2, 11210122)
    IfFlagEnabled(2, 11210121)
    IfCharacterInsideRegion(2, PLAYER, region=1212120)
    IfFlagEnabled(3, 11210122)
    IfFlagDisabled(3, 11210121)
    IfCharacterInsideRegion(3, PLAYER, region=1212122)
    IfFlagEnabled(4, 11210121)
    IfCharacterInsideRegion(4, PLAYER, region=1212123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215222)
    SkipLinesIfFinishedConditionTrue(25, condition=2)
    SkipLinesIfFinishedConditionTrue(24, condition=4)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211021, model_point=101, anchor_type=CoordEntityType.Object)
    EnableFlag(11210121)
    EnableFlag(11210122)
    CreateObjectVFX(1211020, vfx_id=191, model_point=120029)
    ForceAnimation(1211020, 2)
    WaitFrames(frames=140)
    DeleteObjectVFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=1)
    IfAllPlayersOutsideRegion(-2, region=1212122)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212120)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211022, model_point=101, anchor_type=CoordEntityType.Object)
    DisableFlag(11210121)
    CreateObjectVFX(1211020, vfx_id=191, model_point=120029)
    ForceAnimation(1211020, 12)
    WaitFrames(frames=140)
    DeleteObjectVFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=2)
    IfAllPlayersOutsideRegion(-3, region=1212123)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212121)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()


@NeverRestart(11210123)
def Event_11210123():
    """Event 11210123"""
    IfCharacterType(7, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1212124)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210123)


@NeverRestart(11210130)
def Event_11210130():
    """Event 11210130"""
    SkipLinesIfFlagDisabled(1, 11210131)
    EndOfAnimation(obj=1211030, animation_id=3)
    SkipLinesIfFlagEnabled(1, 11210131)
    EndOfAnimation(obj=1211030, animation_id=13)
    IfFlagEnabled(0, 11210133)
    IfFlagDisabled(0, 11215223)
    IfFlagDisabled(1, 11210131)
    IfCharacterInsideRegion(1, PLAYER, region=1212131)
    IfFlagEnabled(2, 11210132)
    IfFlagEnabled(2, 11210131)
    IfCharacterInsideRegion(2, PLAYER, region=1212130)
    IfFlagEnabled(3, 11210132)
    IfFlagDisabled(3, 11210131)
    IfCharacterInsideRegion(3, PLAYER, region=1212132)
    IfFlagEnabled(4, 11210131)
    IfCharacterInsideRegion(4, PLAYER, region=1212133)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215223)
    SkipLinesIfFinishedConditionTrue(25, condition=2)
    SkipLinesIfFinishedConditionTrue(24, condition=4)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211031, model_point=101, anchor_type=CoordEntityType.Object)
    EnableFlag(11210131)
    EnableFlag(11210132)
    CreateObjectVFX(1211030, vfx_id=191, model_point=120029)
    ForceAnimation(1211030, 3)
    WaitFrames(frames=240)
    DeleteObjectVFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=1)
    IfAllPlayersOutsideRegion(-2, region=1212132)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212130)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211032, model_point=101, anchor_type=CoordEntityType.Object)
    DisableFlag(11210131)
    CreateObjectVFX(1211030, vfx_id=191, model_point=120029)
    ForceAnimation(1211030, 13)
    WaitFrames(frames=240)
    DeleteObjectVFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=2)
    IfAllPlayersOutsideRegion(-3, region=1212133)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212131)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()


@NeverRestart(11210133)
def Event_11210133():
    """Event 11210133"""
    IfCharacterInsideRegion(0, PLAYER, region=1212134)
    EnableFlag(11210133)


@NeverRestart(11210140)
def Event_11210140():
    """Event 11210140"""
    SkipLinesIfFlagDisabled(1, 11210141)
    EndOfAnimation(obj=1211040, animation_id=4)
    SkipLinesIfFlagEnabled(1, 11210141)
    EndOfAnimation(obj=1211040, animation_id=14)
    IfFlagDisabled(0, 11215224)
    IfFlagDisabled(1, 11210141)
    IfCharacterInsideRegion(1, PLAYER, region=1212141)
    IfFlagEnabled(2, 11210141)
    IfCharacterInsideRegion(2, PLAYER, region=1212140)
    IfFlagDisabled(3, 11210141)
    IfCharacterInsideRegion(3, PLAYER, region=1212142)
    IfFlagEnabled(4, 11210141)
    IfCharacterInsideRegion(4, PLAYER, region=1212143)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215224)
    EnableFlag(11210160)
    SkipLinesIfFinishedConditionTrue(24, condition=2)
    SkipLinesIfFinishedConditionTrue(23, condition=4)
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211041, model_point=101, anchor_type=CoordEntityType.Object)
    EnableFlag(11210141)
    CreateObjectVFX(1211040, vfx_id=191, model_point=120029)
    ForceAnimation(1211040, 4)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=1)
    IfAllPlayersOutsideRegion(-2, region=1212142)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212140)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, seconds=1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    CreateTemporaryVFX(vfx_id=120030, anchor_entity=1211042, model_point=101, anchor_type=CoordEntityType.Object)
    DisableFlag(11210141)
    CreateObjectVFX(1211040, vfx_id=191, model_point=120029)
    ForceAnimation(1211040, 14)
    WaitFrames(frames=180)
    DeleteObjectVFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, condition=2)
    IfAllPlayersOutsideRegion(-3, region=1212143)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212141)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, seconds=1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()


@NeverRestart(11210170)
def Event_11210170(_, left: int, collision: int, region: int):
    """Event 11210170"""
    DisableMapCollision(collision=collision)
    SkipLinesIfNotEqual(1, left=left, right=11215220)
    IfAllPlayersOutsideRegion(1, region=1212100)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(1, left)
    IfConditionTrue(0, input_condition=1)
    EnableMapCollision(collision=collision)
    SkipLinesIfNotEqual(3, left=left, right=11215220)
    IfCharacterInsideRegion(7, PLAYER, region=1212100)
    IfTimeElapsed(7, seconds=2.0)
    IfConditionTrue(-1, input_condition=7)
    IfAllPlayersOutsideRegion(-1, region=region)
    IfFlagDisabled(-1, left)
    IfConditionTrue(0, input_condition=-1)
    Wait(5.0)
    Restart()


@NeverRestart(11210300)
def Event_11210300():
    """Event 11210300"""
    EndIfClient()
    EndIfThisEventFlagEnabled()
    IfObjectActivated(0, obj_act_id=11210650)
    EnableFlag(11210650)
    DisplayDialog(text=10010884, anchor_entity=1211120, button_type=ButtonType.Yes_or_No)


@RestartOnRest(11210050)
def Event_11210050():
    """Event 11210050"""
    DisableGravity(1210400)
    EnableInvincibility(1210400)
    DisableCharacterCollision(1210400)
    DisableCharacter(1210400)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1210400, authority_level=UpdateAuthority.Forced)
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=1212050)
    EnableFlag(11210050)
    SetNetworkUpdateRate(1210400, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(1210400)
    Move(1210400, destination=1212051, destination_type=CoordEntityType.Region, set_draw_parent=1213000)
    ForceAnimation(1210400, 7000)
    WaitFrames(frames=420)
    DisableCharacter(1210400)


@RestartOnRest(11210051)
def Event_11210051():
    """Event 11210051"""
    DisableAI(1210402)
    EnableImmortality(1210402)
    DisableGravity(1210402)
    DisableCharacterCollision(1210402)
    SkipLinesIfThisEventFlagEnabled(1)
    DisableCharacter(1210402)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1210402, authority_level=UpdateAuthority.Forced)
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(1, PLAYER, region=1212052)
    IfFlagDisabled(1, 11210535)
    IfConditionTrue(0, input_condition=1)
    SetNetworkUpdateRate(1210402, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(1210402)
    ForceAnimation(1210402, 7006, skip_transition=1)
    WaitFrames(frames=240)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    EnableFlag(11210062)
    EnableFlag(11210069)
    End()


@RestartOnRest(11210052)
def Event_11210052():
    """Event 11210052"""
    SkipLinesIfFlagDisabled(3, 11210535)
    DisableFlagRange((11210063, 11210067))
    DisableCharacter(1210402)
    End()
    DisableFlagRange((11210070, 11210073))
    SkipLinesIfClient(1)
    EnableRandomFlagInRange(flag_range=(11210070, 11210073))
    EnableFlag(11210068)
    IfHealthLessThanOrEqual(1, 1210402, value=0.009999999776482582)
    IfFlagEnabled(1, 11210062)
    IfFlagDisabled(1, 11210535)
    IfFlagDisabled(1, 11210067)
    IfFlagEnabled(-2, 11215056)
    IfFlagEnabled(-2, 11215058)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 11210062)
    IfFlagDisabled(2, 11210535)
    IfFlagDisabled(2, 11210067)
    IfFlagEnabled(-3, 11215055)
    IfFlagEnabled(-3, 11215057)
    IfConditionTrue(3, input_condition=-3)
    IfFlagEnabled(3, 11210062)
    IfFlagDisabled(3, 11210535)
    IfFlagDisabled(3, 11210067)
    IfConditionFalse(4, input_condition=1)
    IfConditionFalse(4, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfFlagEnabled(4, 11210062)
    IfFlagDisabled(4, 11210535)
    IfFlagDisabled(4, 11210067)
    IfConditionTrue(-5, input_condition=1)
    IfConditionTrue(-5, input_condition=2)
    IfConditionTrue(-5, input_condition=3)
    IfConditionTrue(-5, input_condition=4)
    IfConditionTrue(0, input_condition=-5)
    SkipLinesIfFinishedConditionTrue(3, condition=1)
    SkipLinesIfFinishedConditionTrue(4, condition=2)
    SkipLinesIfFinishedConditionTrue(5, condition=3)
    SkipLinesIfFinishedConditionTrue(6, condition=4)
    EnableFlag(11210063)
    SkipLines(5)
    EnableFlag(11210065)
    SkipLines(3)
    EnableFlag(11210064)
    SkipLines(1)
    EnableFlag(11210066)
    EnableFlag(11210067)
    Restart()


@RestartOnRest(11210053)
def Event_11210053():
    """Event 11210053"""
    SkipLinesIfThisEventFlagDisabled(3)
    DisableCharacter(1210401)
    DisableCharacter(1210402)
    End()
    IfFlagEnabled(1, 11210063)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(1210402, 7004, skip_transition=1)
    WaitFrames(frames=176)
    DisableCharacter(1210402)
    Kill(1210402, award_souls=1)


@RestartOnRest(11210054)
def Event_11210054():
    """Event 11210054"""
    IfFlagDisabled(1, 11210065)
    IfFlagEnabled(1, 11210064)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(3, 11210069)
    ForceAnimation(1210402, 7010, skip_transition=1)
    WaitFrames(frames=561)
    SkipLines(2)
    ForceAnimation(1210402, 7002, skip_transition=1)
    WaitFrames(frames=461)
    IfHealthLessThanOrEqual(2, 1210402, value=0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagEnabled(3, 11210070)
    SkipLinesIfFlagEnabled(7, 11210071)
    SkipLinesIfFlagEnabled(12, 11210072)
    SkipLinesIfFlagEnabled(17, 11210073)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7001, skip_transition=1)
    WaitFrames(frames=269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210064)
    Restart()


@RestartOnRest(11210055)
def Event_11210055():
    """Event 11210055"""
    IfFlagEnabled(1, 11210065)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(3, 11210069)
    ForceAnimation(1210402, 7011, skip_transition=1)
    WaitFrames(frames=514)
    SkipLines(2)
    ForceAnimation(1210402, 7003, skip_transition=1)
    WaitFrames(frames=414)
    IfHealthLessThanOrEqual(2, 1210402, value=0.009999999776482582)
    SkipLinesIfConditionTrue(26, 2)
    SkipLinesIfFlagEnabled(3, 11210070)
    SkipLinesIfFlagEnabled(7, 11210071)
    SkipLinesIfFlagEnabled(12, 11210072)
    SkipLinesIfFlagEnabled(17, 11210073)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7001, skip_transition=1)
    WaitFrames(frames=269)
    DisableFlag(11210069)
    SkipLines(17)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=60)
    EnableFlag(11210069)
    SkipLines(11)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=120)
    EnableFlag(11210069)
    SkipLines(5)
    WaitFrames(frames=6)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=194)
    WaitFrames(frames=180)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210065)
    Restart()


@RestartOnRest(11210056)
def Event_11210056():
    """Event 11210056"""
    IfFlagDisabled(1, 11210064)
    IfFlagDisabled(1, 11210065)
    IfFlagEnabled(1, 11210066)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(11, 11210069)
    ForceAnimation(1210402, 7009, skip_transition=1)
    WaitFrames(frames=30)
    SkipLinesIfFlagEnabled(1, 11210070)
    WaitFrames(frames=15)
    SkipLinesIfFlagEnabled(1, 11210071)
    WaitFrames(frames=30)
    SkipLinesIfFlagEnabled(1, 11210072)
    WaitFrames(frames=45)
    SkipLinesIfFlagEnabled(1, 11210073)
    WaitFrames(frames=60)
    SkipLines(11)
    ForceAnimation(1210402, 7008, skip_transition=1)
    WaitFrames(frames=200)
    SkipLinesIfFlagEnabled(1, 11210070)
    WaitFrames(frames=15)
    SkipLinesIfFlagEnabled(1, 11210071)
    WaitFrames(frames=30)
    SkipLinesIfFlagEnabled(1, 11210072)
    WaitFrames(frames=45)
    SkipLinesIfFlagEnabled(1, 11210073)
    WaitFrames(frames=60)
    EnableFlag(11210069)
    DisableFlag(11210067)
    DisableFlag(11210066)
    Restart()


@RestartOnRest(11210057)
def Event_11210057():
    """Event 11210057"""
    IfFlagEnabled(1, 11210070)
    IfFlagEnabled(1, 11210068)
    IfFlagEnabled(2, 11210071)
    IfFlagEnabled(2, 11210068)
    IfFlagEnabled(3, 11210072)
    IfFlagEnabled(3, 11210068)
    IfFlagEnabled(4, 11210073)
    IfFlagEnabled(4, 11210068)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, condition=1)
    SkipLinesIfFinishedConditionTrue(8, condition=2)
    SkipLinesIfFinishedConditionTrue(13, condition=3)
    SkipLinesIfFinishedConditionTrue(18, condition=4)
    EnableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    EnableFlag(11210071)
    DisableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    EnableFlag(11210072)
    DisableFlag(11210073)
    DisableFlag(11210068)
    Restart()
    DisableFlag(11210070)
    DisableFlag(11210071)
    DisableFlag(11210072)
    EnableFlag(11210073)
    DisableFlag(11210068)
    Restart()


@RestartOnRest(11210040)
def Event_11210040():
    """Event 11210040"""
    IfHost(1)
    IfCharacterInsideRegion(-1, PLAYER, region=1212054)
    IfCharacterInsideRegion(-1, PLAYER, region=1212062)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215055)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=1212054)
    IfCharacterOutsideRegion(2, PLAYER, region=1212062)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215055)
    Restart()


@RestartOnRest(11210041)
def Event_11210041():
    """Event 11210041"""
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212055)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215056)
    IfHost(2)
    IfCharacterOutsideRegion(2, PLAYER, region=1212055)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(11215056)
    Restart()


@RestartOnRest(11210042)
def Event_11210042():
    """Event 11210042"""
    IfClient(1)
    IfCharacterWhitePhantom(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=1212054)
    IfCharacterInsideRegion(-1, PLAYER, region=1212062)
    IfConditionTrue(1, input_condition=-1)
    IfFramesElapsed(1, frames=30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215057)
    WaitFrames(frames=90)
    DisableFlag(11215057)
    Restart()


@RestartOnRest(11210043)
def Event_11210043():
    """Event 11210043"""
    IfClient(1)
    IfCharacterWhitePhantom(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=1212055)
    IfFramesElapsed(1, frames=30)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215058)
    WaitFrames(frames=90)
    DisableFlag(11215058)
    Restart()


@NeverRestart(11210004)
def Event_11210004():
    """Event 11210004"""
    SkipLinesIfThisEventFlagDisabled(2)
    DisableCharacter(1210401)
    End()
    IfCharacterDead(-1, 1210401)
    IfCharacterDead(-1, 1210402)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11210004)


@RestartOnRest(11215050)
def Event_11215050():
    """Event 11215050"""
    IfCharacterInsideRegion(1, PLAYER, region=1212057)
    IfCharacterInsideRegion(2, PLAYER, region=1212059)
    IfAllPlayersOutsideRegion(2, region=1212057)
    IfCharacterInsideRegion(3, PLAYER, region=1212058)
    IfAllPlayersOutsideRegion(3, region=1212057)
    IfAllPlayersOutsideRegion(3, region=1212059)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(4, input_condition=-1)
    IfFlagEnabled(4, 11215063)
    IfConditionTrue(0, input_condition=4)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    SkipLinesIfFinishedConditionTrue(4, condition=3)
    SetEventPoint(1210401, region=1212060, reaction_range=2.0)
    SkipLines(3)
    SetEventPoint(1210401, region=1212060, reaction_range=2.0)
    SkipLines(1)
    SetEventPoint(1210401, region=1212061, reaction_range=2.0)
    Wait(1.0)
    Restart()


@RestartOnRest(11215051)
def Event_11215051():
    """Event 11215051"""
    DisableCharacter(1210410)
    SkipLinesIfFlagEnabled(7, 11215054)
    SkipLinesIfThisEventSlotFlagDisabled(4)
    SetDisplayMask(1210401, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1210401, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1210401, command_id=20, command_slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1210401)
    CreateNPCPart(1210401, npc_part_id=4510, part_index=NPCPartType.Part1, part_health=200)
    DisableFlag(11215054)
    IfCharacterPartHealthLessThanOrEqual(1, 1210401, npc_part_id=4510, value=0)
    IfHealthLessThanOrEqual(2, 1210401, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfFlagDisabled(3, 11215053)
    SetNPCPartHealth(1210401, npc_part_id=4510, desired_health=10, overwrite_max=False)
    EnableFlag(11215054)
    Restart()
    Move(
        1210410,
        destination=1210401,
        destination_type=CoordEntityType.Character,
        model_point=150,
        copy_draw_parent=1210401,
    )
    EnableCharacter(1210410)
    ResetAnimation(1210401)
    ForceAnimation(1210401, 8000)
    ForceAnimation(1210410, 8100)
    SetDisplayMask(1210401, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1210401, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1210401, 5434)
    AICommand(1210401, command_id=20, command_slot=0)
    ReplanAI(1210401)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(45110000, host_only=True)


@RestartOnRest(11215052)
def Event_11215052():
    """Event 11215052"""
    IfCharacterHasTAEEvent(0, 1210401, tae_event_id=10)
    EnableFlag(11215053)
    IfCharacterHasTAEEvent(0, 1210401, tae_event_id=20)
    DisableFlag(11215053)
    Restart()


@RestartOnRest(11215160)
def Event_11215160(_, character: int):
    """Event 11215160"""
    IfHealthGreaterThan(1, character, value=0.0)
    IfCharacterBackreadEnabled(1, character)
    IfCharacterHasSpecialEffect(1, character, 5421)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=character,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        model_point=7,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=character,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11215165)
def Event_11215165(_, character: int):
    """Event 11215165"""
    IfCharacterDoesNotHaveSpecialEffect(1, character, 5420)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(character, 3150)
    CancelSpecialEffect(character, 3151)
    IfCharacterBackreadDisabled(7, character)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, character, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(character, 3001, wait_for_completion=1)
    IfCharacterHasSpecialEffect(3, character, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(character, 3001, wait_for_completion=1)
    IfCharacterHasSpecialEffect(4, character, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(character, 3001, wait_for_completion=1)
    IfCharacterHasSpecialEffect(5, character, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(character, 3006, wait_for_completion=1)
    ReplanAI(character)
    CancelSpecialEffect(character, 3150)
    CancelSpecialEffect(character, 3151)
    Restart()


@RestartOnRest(11215170)
def Event_11215170(_, character: int):
    """Event 11215170"""
    IfCharacterHasSpecialEffect(1, character, 5421)
    IfCharacterHasSpecialEffect(1, character, 3150)
    IfCharacterHasSpecialEffect(2, character, 5420)
    IfCharacterHasSpecialEffect(2, character, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(character, command_id=200, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=210, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    IfCharacterHasSpecialEffect(-2, character, 5420)
    IfCharacterHasSpecialEffect(-2, character, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11215175)
def Event_11215175(_, character: int):
    """Event 11215175"""
    IfCharacterHasSpecialEffect(1, character, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, character, 3150)
    IfCharacterHasSpecialEffect(2, character, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, character, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(character, 3150)
    CancelSpecialEffect(character, 3151)
    SkipLinesIfFinishedConditionTrue(5, condition=2)
    AICommand(character, command_id=201, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=211, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    IfCharacterHasSpecialEffect(-2, character, 5420)
    IfCharacterHasSpecialEffect(-2, character, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest(11215180)
def Event_11215180(_, character: int, region: int):
    """Event 11215180"""
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, character, region=region)
    IfCharacterBackreadDisabled(1, character)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(character, 5421)
    ClearTargetList(character)
    ReplanAI(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, character)
    Restart()


@RestartOnRest(11210680)
def Event_11210680(_, character: int):
    """Event 11210680"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfCharacterDead(0, character)
    End()


@RestartOnRest(11215185)
def Event_11215185(_, character: int):
    """Event 11215185"""
    EndIfHost()
    IfCharacterBackreadDisabled(1, character)
    EndIfConditionTrue(1)
    ResetAnimation(character, disable_interpolation=1)
    ForceAnimation(character, 0)
    ReplanAI(character)


@NeverRestart(11210200)
def Event_11210200(_, obj: int, region: int):
    """Event 11210200"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DisableObject(obj)
    End()
    IfCharacterHasSpecialEffect(-1, PLAYER, 620)
    IfCharacterHasSpecialEffect(-1, PLAYER, 6950)
    IfSkullLanternActive(-1)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(obj, 262000000, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 1, wait_for_completion=1)
    DisableObject(obj)


@NeverRestart(11210205)
def Event_11210205(_, anchor_entity: int, region: int, flag: int):
    """Event 11210205"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    EndIfFlagEnabled(flag)
    PlaySoundEffect(anchor_entity, 120199999, sound_type=SoundType.o_Object)
    Wait(2.0)
    Restart()


@NeverRestart(11210230)
def Event_11210230(_, obj: int, obj_1: int, animation_id: int, animation_id_1: int):
    """Event 11210230"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=obj_1, animation_id=animation_id_1)
    PostDestruction(obj)
    EnableTreasure(obj=obj_1)
    End()
    DisableTreasure(obj=obj_1)
    SkipLinesIfClient(1)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=99005)
    ForceAnimation(obj_1, animation_id, loop=1)
    IfObjectDestroyed(0, obj)
    ForceAnimation(obj_1, animation_id_1, wait_for_completion=1)
    SkipLinesIfClient(1)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)


@NeverRestart(11210510)
def Event_11210510(_, character: int, flag: int):
    """Event 11210510"""
    IfHealthLessThanOrEqual(1, character, value=0.8999999761581421)
    IfHealthGreaterThan(1, character, value=0.0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfThisEventSlotFlagEnabled(2)
    IfFlagEnabled(3, flag)
    IfThisEventSlotFlagDisabled(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, condition=3)
    DisableCharacter(character)
    IfFlagEnabled(0, 703)
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@NeverRestart(11210910)
def Event_11210910():
    """Event 11210910"""
    SkipLinesIfThisEventFlagEnabled(1)
    SetAIParamID(6720, ai_param_id=411001)
    IfFlagEnabled(0, 11210911)
    SetAIParamID(6720, ai_param_id=411000)


@NeverRestart(11210912)
def Event_11210912():
    """Event 11210912"""
    IfFlagEnabled(0, 1822)
    IfCharacterOutsideRegion(0, PLAYER, region=1212040)
    SetAIParamID(6720, ai_param_id=411001)
    SetNest(6720, region=1212041)
    AICommand(6720, command_id=10, command_slot=0)
    ReplanAI(6720)
    IfCharacterInsideRegion(0, PLAYER, region=1212040)
    WaitFrames(frames=30)
    SetAIParamID(6720, ai_param_id=411000)
    AICommand(6720, command_id=-1, command_slot=0)
    ReplanAI(6720)
    Restart()


@NeverRestart(11210915)
def Event_11210915():
    """Event 11210915"""
    EndIfFlagEnabled(1822)
    IfFlagEnabled(0, 1822)
    ForceAnimation(6720, 9060)


@NeverRestart(11210520)
def Event_11210520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210520"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    DropMandatoryTreasure(character)
    End()
    IfHealthLessThanOrEqual(0, character, value=0.0)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210530)
def Event_11210530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210530"""
    IfFlagDisabled(1, 1822)
    IfFlagEnabled(1, 1820)
    IfFlagEnabled(1, 11210300)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210535)
def Event_11210535():
    """Event 11210535"""
    EndIfThisEventFlagEnabled()
    DisableCharacter(1210401)
    IfFlagEnabled(1, 1821)
    IfFlagEnabled(1, 11210592)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(121)
    SkipLinesIfMultiplayer(1)
    PlayCutscene(120100, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(120100, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11210539)
    EnableCharacter(1210401)
    DisableCharacter(1210402)
    EnableObject(1211690)
    CreateVFX(1211691)
    EnableMapCollision(collision=1213061)
    DisableMapCollision(collision=1213060)


@NeverRestart(11210544)
def Event_11210544():
    """Event 11210544"""
    IfObjectDestroyed(0, 1211130)
    DeleteVFX(1213150)


@NeverRestart(11210531)
def Event_11210531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210531"""
    IfHost(1)
    IfPlayerHasGood(1, 710)
    IfFlagEnabled(1, 1860)
    IfFlagEnabled(1, 11210001)
    IfConditionTrue(0, input_condition=1)
    EndIfThisEventFlagDisabled()
    EnableCharacter(character)
    EnableObject(1211220)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210532)
def Event_11210532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210532"""
    IfFlagDisabled(1, 1863)
    IfFlagEnabled(1, 1861)
    IfFlagEnabled(1, 11210590)
    IfCharacterAlive(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@NeverRestart(11210533)
def Event_11210533(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210533"""
    IfHost(1)
    IfFlagDisabled(1, 1863)
    IfFlagDisabled(1, 1865)
    IfFlagEnabled(1, 1862)
    IfCharacterBackreadDisabled(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210534)
def Event_11210534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11210534"""
    IfHost(1)
    IfFlagDisabled(1, 1863)
    IfFlagDisabled(1, 1864)
    IfFlagDisabled(1, 1865)
    IfFlagEnabled(1, 11210591)
    IfCharacterBackreadDisabled(1, character)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@NeverRestart(11210543)
def Event_11210543():
    """Event 11210543"""
    IfFlagDisabled(1, 11215210)
    IfCharacterInsideRegion(1, 6740, region=1212351)
    IfFlagEnabled(2, 11215210)
    IfCharacterInsideRegion(2, 6740, region=1212350)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, condition=2)
    EnableFlag(11215210)
    SetNest(6740, region=1212353)
    Restart()
    DisableFlag(11215210)
    SetNest(6740, region=1212352)
    Restart()


@NeverRestart(11210540)
def Event_11210540():
    """Event 11210540"""
    IfFlagEnabled(1, 1127)
    IfFlagEnabled(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(2, 1126)
    SkipLinesIfFlagEnabled(1, 1125)
    DisableFlagRange((1120, 1139))
    DisableFlag(1127)
    EnableFlag(1128)
    Move(
        6700,
        destination=1210840,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=1210840,
    )
    RequestAnimation(6700, animation_id=7915, loop=1)
    EnableCharacter(6700)


@NeverRestart(11210541)
def Event_11210541():
    """Event 11210541"""
    SkipLinesIfThisEventFlagDisabled(2)
    DropMandatoryTreasure(6700)
    End()
    EnableImmortality(6700)
    IfHealthLessThanOrEqual(0, 6700, value=0.009999999776482582)
    ForceAnimation(6700, 7917, wait_for_completion=1)
    DisableCharacter(6700)
    DisableImmortality(6700)
    Kill(6700, award_souls=1)
    Kill(6750)
    DisableFlagRange((1120, 1139))
    EnableFlag(1125)


@NeverRestart(11210542)
def Event_11210542():
    """Event 11210542"""
    SkipLinesIfFlagDisabled(1, 11210541)
    End()
    IfAttacked(0, attacked_entity=6700, attacker=PLAYER)
    ForceAnimation(6700, 7916, wait_for_completion=1)
    Restart()


@NeverRestart(11210538)
def Event_11210538():
    """Event 11210538"""
    SkipLinesIfThisEventFlagDisabled(2)
    DropMandatoryTreasure(6750)
    End()
    IfFlagEnabled(0, 1125)
    DropMandatoryTreasure(6750)
    DisableFlagRange((1870, 1889))
    EnableFlag(1872)


@NeverRestart(11215030)
def Event_11215030(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    anchor_entity: int,
    region: int,
    flag_3: int,
    flag_4: int,
):
    """Event 11215030"""
    EndIfFlagEnabled(flag)
    DisableCharacter(character)
    EndIfFlagEnabled(17)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, 1842)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(-1, flag_1)
    IfFlagEnabled(2, flag_1)
    IfFlagEnabled(-2, flag_3)
    IfFlagEnabled(-2, flag_4)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(6730)
    EnableCharacter(character)
    DisplayBattlefieldMessage(20001100, display_location_index=0)
    SkipLinesIfThisEventSlotFlagEnabled(3)
    CreateTemporaryVFX(vfx_id=130, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    ForceAnimation(character, 7000)
    ReplanAI(character)
    EnableFlag(flag)
    EnableFlag(11210536)


@NeverRestart(11210900)
def Event_11210900(_, character: int):
    """Event 11210900"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterDead(0, character)
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    EndIfConditionTrue(-1)
    DisplayBattlefieldMessage(20001105, display_location_index=0)
    EnableCharacter(6730)


@NeverRestart(11210905)
def Event_11210905(_, character: int, flag: int, destination: int, set_draw_parent: int, flag_1: int, flag_2: int):
    """Event 11210905"""
    SkipLinesIfFlagDisabled(2, flag_2)
    DisableCharacter(character)
    End()
    IfHost(1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(-1, PLAYER, region=1212084)
    IfCharacterInsideRegion(-1, PLAYER, region=1212085)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_2)
    ForceAnimation(character, 7001)
    WaitFrames(frames=80)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=set_draw_parent)
    DisplayBattlefieldMessage(20001101, display_location_index=0)
    EnableCharacter(6730)


@NeverRestart(11219010)
def Event_11219010():
    """Event 11219010"""
    IfFlagRangeAnyEnabled(2, flag_range=(7000, 7749))
    IfCharacterOutsideRegion(2, PLAYER, region=1212715)
    IfCharacterOutsideRegion(2, PLAYER, region=1212714)
    IfCharacterOutsideRegion(2, PLAYER, region=1212713)
    IfCharacterOutsideRegion(2, PLAYER, region=1212797)
    IfCharacterOutsideRegion(2, PLAYER, region=1212793)
    IfCharacterOutsideRegion(2, PLAYER, region=1212702)
    IfCharacterOutsideRegion(2, PLAYER, region=1212701)
    IfCharacterOutsideRegion(2, PLAYER, region=1212700)
    IfCharacterOutsideRegion(2, PLAYER, region=1212794)
    IfCharacterOutsideRegion(2, PLAYER, region=1212796)
    IfCharacterOutsideRegion(2, PLAYER, region=1218900)
    IfConditionTrue(0, input_condition=2)
    DisableFlagRange((7000, 7749))


@NeverRestart(11219111)
def Event_11219111():
    """Event 11219111"""
    IfArenaMatchmaking(1)
    IfFlagDisabled(1, 11211900)
    IfConditionTrue(0, input_condition=1)
    EnableObject(1211900)
    CreateVFX(1211901)
    EnableFlag(11211900)
    Restart()


@NeverRestart(11219112)
def Event_11219112():
    """Event 11219112"""
    IfArenaMatchmaking(1)
    IfConditionFalse(2, input_condition=1)
    IfFlagEnabled(2, 11211900)
    IfConditionTrue(0, input_condition=2)
    DisableObject(1211900)
    DeleteVFX(1211901)
    DisableFlag(11211900)
    Restart()


@NeverRestart(11219114)
def Event_11219114():
    """Event 11219114"""
    EndIfMultiplayer()
    IfPlayerDoesNotHaveGood(1, 118)
    IfActionButton(
        1,
        prompt_text=60000112,
        anchor_entity=1219001,
        anchor_type=CoordEntityType.Region,
        button=1211690,
        trigger_attribute=TriggerAttribute.All,
    )
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1219001, destination_type=CoordEntityType.Region, short_move=True)
    RotateToFaceEntity(PLAYER, target_entity=1212777)
    ForceAnimation(PLAYER, 7410)
    DisableObject(1211900)
    DeleteVFX(1211901)
    Wait(1.5)
    AwardItemLot(2200, host_only=False)
    Restart()


@NeverRestart(11219113)
def Event_11219113():
    """Event 11219113"""
    IfClient(2)
    EndIfConditionTrue(2)
    IfHost(1)
    IfPlayerHasGood(1, 118)
    IfConditionTrue(0, input_condition=1)
    DisableObject(1211900)
    DeleteVFX(1211901, erase_root_only=False)
    End()


@NeverRestart(11212787)
def Event_11212787():
    """Event 11212787"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1212778)
    EnableFlag(11212785)
    IfCharacterOutsideRegion(0, PLAYER, region=1212778)
    DisableFlag(11212785)
    Restart()


@NeverRestart(11212786)
def Event_11212786():
    """Event 11212786"""
    IfFlagEnabled(0, 11212785)
    IfFlagDisabled(0, 11212785)
    Restart()


@NeverRestart(11213888)
def Event_11213888():
    """Event 11213888"""
    IfCharacterOutsideRegion(1, PLAYER, region=1218900)
    EndIfConditionTrue(1)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    End()


@NeverRestart(11215843)
def Event_11215843(_, left: int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11215843"""
    SkipLinesIfEqual(1, left=left, right=11210001)
    SkipLines(3)
    IfFlagEnabled(2, 11210592)
    IfFlagDisabled(2, 11210004)
    IfConditionFalse(1, input_condition=2)
    IfHost(1)
    IfMultiplayer(1)
    IfFlagEnabled(1, left)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        boss_version=True,
        line_intersects=line_intersects,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, 7410, wait_for_completion=1)
    Unknown_2003_47()
    Restart()


@NeverRestart(11215846)
def Event_11215846(_, left: int, obj: int, vfx_id: int):
    """Event 11215846"""
    SkipLinesIfEqual(1, left=left, right=11210001)
    SkipLines(3)
    IfFlagEnabled(4, 11210592)
    IfFlagDisabled(4, 11210004)
    IfConditionFalse(1, input_condition=4)
    IfMultiplayer(-1)
    IfUnknownPlayerType5(-1)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, left)
    IfConditionTrue(0, input_condition=1)
    EnableObject(obj)
    CreateVFX(vfx_id)
    IfUnknownPlayerType5(3)
    IfConditionFalse(2, input_condition=3)
    IfSingleplayer(2)
    IfConditionTrue(0, input_condition=2)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    Restart()


@NeverRestart(11210700)
def Event_11210700():
    """Event 11210700"""
    Event_7999()
    Event_7998()
    Event_11219010()
    SkipLinesIfClient(1)
    DisableFlagRange((11215350, 11215365))
    DisableFlag(11215891)
    DisableFlag(11219902)
    DisableFlag(11215398)
    DisableFlagRange((11215342, 11215345))
    DisableFlagRange((11214350, 11214359))
    DisableFlag(11210810)
    DisableFlag(11218145)
    DeleteVFX(1213403, erase_root_only=False)
    DeleteVFX(1213404, erase_root_only=False)
    DeleteVFX(1213405, erase_root_only=False)
    DeleteVFX(1213406, erase_root_only=False)
    DeleteVFX(1213407, erase_root_only=False)
    DeleteVFX(1213408, erase_root_only=False)
    DeleteVFX(1213409, erase_root_only=False)
    DeleteVFX(1213410, erase_root_only=False)
    DeleteVFX(1213411, erase_root_only=False)
    DeleteVFX(1213412, erase_root_only=False)
    DeleteVFX(1213416, erase_root_only=False)
    DeleteVFX(1213417, erase_root_only=False)
    DeleteVFX(1213418, erase_root_only=False)
    DeleteVFX(1213419, erase_root_only=False)
    DeleteVFX(1213420, erase_root_only=False)
    DeleteVFX(1213421, erase_root_only=False)
    DeleteVFX(1213422, erase_root_only=False)
    DeleteVFX(1213423, erase_root_only=False)
    DeleteVFX(1213424, erase_root_only=False)
    DeleteVFX(1213425, erase_root_only=False)
    Event_11210838()
    Event_11210839()
    Event_11210876()
    Event_11210932()
    Event_11210830()
    Event_11210828(0, flag=11218990, flag_1=11215360, flag_2=11215362, region=1212700)
    Event_11210828(1, flag=11218991, flag_1=11215360, flag_2=11215362, region=1212713)
    Event_11210827(0, flag=11218992, first_flag=11215360, last_flag=11215363, region=1212701)
    Event_11210827(1, flag=11218993, first_flag=11215360, last_flag=11215363, region=1212714)
    Event_11210827(2, flag=11218994, first_flag=11215360, last_flag=11215363, region=1212702)
    Event_11210827(3, flag=11218995, first_flag=11215360, last_flag=11215363, region=1212715)
    Event_11210827(4, flag=11218996, first_flag=11215360, last_flag=11215365, region=1212796)
    Event_11210827(5, flag=11218997, first_flag=11215360, last_flag=11215365, region=1212793)
    Event_11210827(6, flag=11218998, first_flag=11215360, last_flag=11215365, region=1212794)
    Event_11210827(7, flag=11218999, first_flag=11215360, last_flag=11215365, region=1212797)
    Event_11210835(0, 150.0, 30.0, 270.0, 30.0)
    Event_11210836()
    Event_11210877()
    Event_11210878()
    Event_11215398()
    Event_11210875(0, left=6980, message_id=60000102, concatenator_base_flag=7290)
    Event_11210875(1, left=6981, message_id=60000103, concatenator_base_flag=7340)
    Event_11210875(2, left=6982, message_id=60000105, concatenator_base_flag=7440)
    Event_11210875(3, left=6983, message_id=60000109, concatenator_base_flag=7390)
    Event_11210875(4, left=6984, message_id=60000106, concatenator_base_flag=7490)
    Event_11210875(5, left=6985, message_id=60000107, concatenator_base_flag=7540)
    Event_11210875(6, left=6986, message_id=60000108, concatenator_base_flag=7590)
    Event_11210875(7, left=6987, message_id=60000110, concatenator_base_flag=7690)
    Event_11210875(8, left=6988, message_id=60000104, concatenator_base_flag=7640)
    Event_11210875(9, left=6989, message_id=60000111, concatenator_base_flag=7740)
    Event_11210875(10, left=6990, message_id=0, concatenator_base_flag=0)
    Event_11210727()
    Event_11210845()
    Event_11210846()
    Event_11210847()
    Event_11210848()
    Event_11210860()
    Event_11210861()
    Event_11210849()
    Event_11210826()
    Event_11210837()
    Event_11210817()
    Event_11210401()
    Event_11210402()
    Event_11219901()
    Event_11219111()
    Event_11219112()
    Event_11210404(0, flag=7290, flag_1=11215408, flag_2=11218001)
    Event_11210404(1, flag=7340, flag_1=11215392, flag_2=11218001)
    Event_11210404(2, flag=7390, flag_1=11215402, flag_2=11218001)
    Event_11210404(3, flag=7440, flag_1=11215395, flag_2=11218001)
    Event_11210404(4, flag=7490, flag_1=11215405, flag_2=11218001)
    Event_11210404(5, flag=7540, flag_1=11215408, flag_2=11218000)
    Event_11210404(6, flag=7590, flag_1=11215392, flag_2=11218000)
    Event_11210404(7, flag=7640, flag_1=11215402, flag_2=11218000)
    Event_11210404(8, flag=7690, flag_1=11215395, flag_2=11218000)
    Event_11210404(9, flag=7740, flag_1=11215405, flag_2=11218000)
    Event_11210800(0, region=1217700, flag=11215350, unk1=0)
    Event_11210800(1, region=1217701, flag=11215352, unk1=0)
    Event_11210800(2, region=1217600, flag=11215350, unk1=1)
    Event_11210800(3, region=1217601, flag=11215351, unk1=1)
    Event_11210800(4, region=1217602, flag=11215352, unk1=1)
    Event_11210800(5, region=1217603, flag=11215353, unk1=1)
    Event_11210800(6, region=1217800, flag=11215350, unk1=1)
    Event_11210800(7, region=1217801, flag=11215351, unk1=1)
    Event_11210800(8, region=1217802, flag=11215352, unk1=1)
    Event_11210800(9, region=1217803, flag=11215353, unk1=1)
    Event_11210800(10, region=1217804, flag=11215354, unk1=1)
    Event_11210800(11, region=1217805, flag=11215355, unk1=1)
    Event_11210800(12, region=1217500, flag=11215350, unk1=1)
    Event_11210800(13, region=1217501, flag=11215351, unk1=1)
    Event_11210800(14, region=1217502, flag=11215352, unk1=1)
    Event_11210800(15, region=1217503, flag=11215353, unk1=1)
    Event_11210800(16, region=1217900, flag=11215350, unk1=1)
    Event_11210800(17, region=1217901, flag=11215351, unk1=1)
    Event_11210800(18, region=1217902, flag=11215352, unk1=1)
    Event_11210800(19, region=1217903, flag=11215353, unk1=1)
    Event_11210800(20, region=1217904, flag=11215354, unk1=1)
    Event_11210800(21, region=1217905, flag=11215355, unk1=1)
    Event_11210800(22, region=1217200, flag=11215350, unk1=0)
    Event_11210800(23, region=1217201, flag=11215352, unk1=0)
    Event_11210800(24, region=1217100, flag=11215350, unk1=1)
    Event_11210800(25, region=1217101, flag=11215351, unk1=1)
    Event_11210800(26, region=1217102, flag=11215352, unk1=1)
    Event_11210800(27, region=1217103, flag=11215353, unk1=1)
    Event_11210800(28, region=1217300, flag=11215350, unk1=1)
    Event_11210800(29, region=1217301, flag=11215351, unk1=1)
    Event_11210800(30, region=1217302, flag=11215352, unk1=1)
    Event_11210800(31, region=1217303, flag=11215353, unk1=1)
    Event_11210800(32, region=1217304, flag=11215354, unk1=1)
    Event_11210800(33, region=1217305, flag=11215355, unk1=1)
    Event_11210800(34, region=1217000, flag=11215350, unk1=1)
    Event_11210800(35, region=1217001, flag=11215351, unk1=1)
    Event_11210800(36, region=1217002, flag=11215352, unk1=1)
    Event_11210800(37, region=1217003, flag=11215353, unk1=1)
    Event_11210800(38, region=1217400, flag=11215350, unk1=1)
    Event_11210800(39, region=1217401, flag=11215351, unk1=1)
    Event_11210800(40, region=1217402, flag=11215352, unk1=1)
    Event_11210800(41, region=1217403, flag=11215353, unk1=1)
    Event_11210800(42, region=1217404, flag=11215354, unk1=1)
    Event_11210800(43, region=1217405, flag=11215355, unk1=1)
    Event_11210820(0, left=11215350, flag=11215360, event_id=11210825, event_slot=0)
    Event_11210820(1, left=11215351, flag=11215361, event_id=11210825, event_slot=1)
    Event_11210820(2, left=11215352, flag=11215362, event_id=11210825, event_slot=2)
    Event_11210820(3, left=11215353, flag=11215363, event_id=11210825, event_slot=3)
    Event_11210820(4, left=11215354, flag=11215364, event_id=11210825, event_slot=4)
    Event_11210820(5, left=11215355, flag=11215365, event_id=11210825, event_slot=5)
    Event_11219950(0, flag=11215360)
    Event_11219950(1, flag=11215361)
    Event_11219950(2, flag=11215362)
    Event_11219950(3, flag=11215363)
    Event_11219950(4, flag=11215364)
    Event_11219950(5, flag=11215365)
    Event_11210825(0, flag=11215360, flag_1=11218501)
    Event_11210825(1, flag=11215361, flag_1=11218502)
    Event_11210825(2, flag=11215362, flag_1=11218503)
    Event_11210825(3, flag=11215363, flag_1=11218504)
    Event_11210825(4, flag=11215364, flag_1=11218505)
    Event_11210825(5, flag=11215365, flag_1=11218506)
    Event_11210701(0, flag=11215350, flag_1=11218348, flag_2=11218354, flag_3=11218355, flag_4=11218501)
    Event_11210701(1, flag=11215351, flag_1=11218349, flag_2=11218354, flag_3=11218355, flag_4=11218502)
    Event_11210701(2, flag=11215352, flag_1=11218350, flag_2=11218355, flag_3=11218354, flag_4=11218503)
    Event_11210701(3, flag=11215353, flag_1=11218351, flag_2=11218355, flag_3=11218354, flag_4=11218504)
    Event_11210701(4, flag=11215354, flag_1=11218352, flag_2=11218354, flag_3=11218355, flag_4=11218505)
    Event_11210701(5, flag=11215355, flag_1=11218353, flag_2=11218355, flag_3=11218354, flag_4=11218506)
    Event_11210434()
    Event_11210430(0, flag=11215350, flag_1=11218348, flag_2=11218350, flag_3=11218354, flag_4=11218355, flag_5=11218501)
    Event_11210430(1, flag=11215351, flag_1=11218349, flag_2=11218351, flag_3=11218354, flag_4=11218355, flag_5=11218502)
    Event_11210430(2, flag=11215352, flag_1=11218350, flag_2=11218348, flag_3=11218355, flag_4=11218354, flag_5=11218503)
    Event_11210430(3, flag=11215353, flag_1=11218351, flag_2=11218349, flag_3=11218355, flag_4=11218354, flag_5=11218504)
    Event_11210430(4, flag=11215354, flag_1=11218352, flag_2=11218353, flag_3=11218354, flag_4=11218355, flag_5=11218505)
    Event_11210430(5, flag=11215355, flag_1=11218353, flag_2=11218352, flag_3=11218355, flag_4=11218354, flag_5=11218506)
    Event_11210435(
        0,
        flag=11215350,
        flag_1=11218348,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218501
    )
    Event_11210435(
        1,
        flag=11215351,
        flag_1=11218349,
        flag_2=11218348,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218502
    )
    Event_11210435(
        2,
        flag=11215352,
        flag_1=11218350,
        flag_2=11218349,
        flag_3=11218348,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218503
    )
    Event_11210435(
        3,
        flag=11215353,
        flag_1=11218351,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218348,
        flag_5=11218352,
        flag_6=11218353,
        flag_7=11218504
    )
    Event_11210435(
        4,
        flag=11215354,
        flag_1=11218352,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218348,
        flag_6=11218353,
        flag_7=11218505
    )
    Event_11210435(
        5,
        flag=11215355,
        flag_1=11218353,
        flag_2=11218349,
        flag_3=11218350,
        flag_4=11218351,
        flag_5=11218352,
        flag_6=11218348,
        flag_7=11218506
    )
    Event_11214435(0, flag=11215350, flag_1=11218501)
    Event_11214435(1, flag=11215351, flag_1=11218502)
    Event_11214435(2, flag=11215352, flag_1=11218503)
    Event_11214435(3, flag=11215353, flag_1=11218504)
    Event_11214435(4, flag=11215354, flag_1=11218505)
    Event_11214435(5, flag=11215355, flag_1=11218506)
    Event_11210870(0, flag=11215350, flag_1=11218348, flag_2=11218354, flag_3=11218355)
    Event_11210870(1, flag=11215351, flag_1=11218349, flag_2=11218354, flag_3=11218355)
    Event_11210870(2, flag=11215352, flag_1=11218350, flag_2=11218355, flag_3=11218354)
    Event_11210870(3, flag=11215353, flag_1=11218351, flag_2=11218355, flag_3=11218354)
    Event_11210870(4, flag=11215354, flag_1=11218352, flag_2=11218354, flag_3=11218355)
    Event_11210870(5, flag=11215355, flag_1=11218353, flag_2=11218355, flag_3=11218354)
    Event_11210831(0, flag=11215360, flag_1=11218348)
    Event_11210831(1, flag=11215361, flag_1=11218349)
    Event_11210831(2, flag=11215362, flag_1=11218350)
    Event_11210831(3, flag=11215363, flag_1=11218351)
    Event_11210831(4, flag=11215364, flag_1=11218352)
    Event_11210831(5, flag=11215365, flag_1=11218353)
    Event_11210891(
        0,
        flag=11218342,
        flag_1=11215350,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347
    )
    Event_11210891(
        1,
        flag=11218343,
        flag_1=11215351,
        flag_2=11218342,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347
    )
    Event_11210891(
        2,
        flag=11218344,
        flag_1=11215352,
        flag_2=11218343,
        flag_3=11218342,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218347
    )
    Event_11210891(
        3,
        flag=11218345,
        flag_1=11215353,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218342,
        flag_5=11218346,
        flag_6=11218347
    )
    Event_11210891(
        4,
        flag=11218346,
        flag_1=11215354,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218342,
        flag_6=11218347
    )
    Event_11210891(
        5,
        flag=11218347,
        flag_1=11215355,
        flag_2=11218343,
        flag_3=11218344,
        flag_4=11218345,
        flag_5=11218346,
        flag_6=11218342
    )
    Event_11210840(0, flag=11215350, flag_1=11218501, flag_2=11218511)
    Event_11210840(1, flag=11215351, flag_1=11218502, flag_2=11218512)
    Event_11210840(2, flag=11215352, flag_1=11218503, flag_2=11218513)
    Event_11210840(3, flag=11215353, flag_1=11218504, flag_2=11218514)
    Event_11210840(4, flag=11215354, flag_1=11218505, flag_2=11218515)
    Event_11210840(5, flag=11215355, flag_1=11218506, flag_2=11218516)
    Event_11210777(0, flag=11215350, flag_1=11218511)
    Event_11210777(1, flag=11215351, flag_1=11218512)
    Event_11210777(2, flag=11215352, flag_1=11218513)
    Event_11210777(3, flag=11215353, flag_1=11218514)
    Event_11210777(4, flag=11215354, flag_1=11218515)
    Event_11210777(5, flag=11215355, flag_1=11218516)
    Event_11210850(0, flag=11215350, flag_1=11218511, region=1212700, first_region=1215700, last_region=1215725)
    Event_11210850(1, flag=11215352, flag_1=11218513, region=1212700, first_region=1215700, last_region=1215725)
    Event_11210850(2, flag=11215350, flag_1=11218511, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(3, flag=11215351, flag_1=11218512, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(4, flag=11215352, flag_1=11218513, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(5, flag=11215353, flag_1=11218514, region=1212701, first_region=1215600, last_region=1215621)
    Event_11210850(6, flag=11215350, flag_1=11218511, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(7, flag=11215351, flag_1=11218512, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(8, flag=11215352, flag_1=11218513, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(9, flag=11215353, flag_1=11218514, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(10, flag=11215354, flag_1=11218515, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(11, flag=11215355, flag_1=11218516, region=1212793, first_region=1215800, last_region=1215826)
    Event_11210850(12, flag=11215350, flag_1=11218511, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(13, flag=11215351, flag_1=11218512, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(14, flag=11215352, flag_1=11218513, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(15, flag=11215353, flag_1=11218514, region=1212702, first_region=1215500, last_region=1215523)
    Event_11210850(16, flag=11215350, flag_1=11218511, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(17, flag=11215351, flag_1=11218512, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(18, flag=11215352, flag_1=11218513, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(19, flag=11215353, flag_1=11218514, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(20, flag=11215354, flag_1=11218515, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(21, flag=11215355, flag_1=11218516, region=1212794, first_region=1215900, last_region=1215921)
    Event_11210850(22, flag=11215350, flag_1=11218511, region=1212713, first_region=1215200, last_region=1215233)
    Event_11210850(23, flag=11215352, flag_1=11218513, region=1212713, first_region=1215200, last_region=1215233)
    Event_11210850(24, flag=11215350, flag_1=11218511, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(25, flag=11215351, flag_1=11218512, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(26, flag=11215352, flag_1=11218513, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(27, flag=11215353, flag_1=11218514, region=1212714, first_region=1215100, last_region=1215133)
    Event_11210850(28, flag=11215350, flag_1=11218511, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(29, flag=11215351, flag_1=11218512, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(30, flag=11215352, flag_1=11218513, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(31, flag=11215353, flag_1=11218514, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(32, flag=11215354, flag_1=11218515, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(33, flag=11215355, flag_1=11218516, region=1212796, first_region=1215300, last_region=1215339)
    Event_11210850(34, flag=11215350, flag_1=11218511, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(35, flag=11215351, flag_1=11218512, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(36, flag=11215352, flag_1=11218513, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(37, flag=11215353, flag_1=11218514, region=1212715, first_region=1215000, last_region=1215033)
    Event_11210850(38, flag=11215350, flag_1=11218511, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(39, flag=11215351, flag_1=11218512, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(40, flag=11215352, flag_1=11218513, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(41, flag=11215353, flag_1=11218514, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(42, flag=11215354, flag_1=11218515, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210850(43, flag=11215355, flag_1=11218516, region=1212797, first_region=1215400, last_region=1215445)
    Event_11210886(0, flag=11215350, flag_1=11218511)
    Event_11210886(1, flag=11215351, flag_1=11218512)
    Event_11210886(2, flag=11215352, flag_1=11218513)
    Event_11210886(3, flag=11215353, flag_1=11218514)
    Event_11210886(4, flag=11215354, flag_1=11218515)
    Event_11210886(5, flag=11215355, flag_1=11218516)
    Event_11210688(0, flag=11215350, flag_1=11218511)
    Event_11210688(1, flag=11215351, flag_1=11218512)
    Event_11210688(2, flag=11215352, flag_1=11218513)
    Event_11210688(3, flag=11215353, flag_1=11218514)
    Event_11210688(4, flag=11215354, flag_1=11218515)
    Event_11210688(5, flag=11215355, flag_1=11218516)
    Event_11210890()
    Event_11219877()
    Event_11219121()
    Event_11219122()
    Event_11210702()
    Event_11210829()
    Event_11210832()


@NeverRestart(11210702)
def Event_11210702():
    """Event 11210702"""
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


@NeverRestart(11210878)
def Event_11210878():
    """Event 11210878"""
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4610)
    SkipLinesIfFlagEnabled(1, 11215398)
    AddSpecialEffect(PLAYER, 4613)
    Wait(1.0)
    Restart()


@NeverRestart(11215398)
def Event_11215398():
    """Event 11215398"""
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212740)
    IfCharacterInsideRegion(-1, PLAYER, region=1212741)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 4613)
    Restart()


@NeverRestart(11210876)
def Event_11210876():
    """Event 11210876"""
    DisableNetworkSync()
    IfFlagEnabled(0, 11215394)
    Wait(5.0)
    DisableFlag(11215394)
    SkipLinesIfFlagEnabled(2, 11215391)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 90000)
    Restart()


@NeverRestart(11210800)
def Event_11210800(_, region: int, flag: int, unk1: int):
    """Event 11210800"""
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    Unknown_2008_04()
    DisableFlagRange((11215350, 11215355))
    EnableFlag(flag)
    DisableAI(PLAYER)
    Unknown_2004_50()
    EqualRecovery()
    Unknown_2004_51(unk1=unk1)
    IfFlagDisabled(0, flag)
    Restart()


@NeverRestart(11210820)
def Event_11210820(_, left: int, flag: int, event_id: int, event_slot: int):
    """Event 11210820"""
    IfMultiplayer(1)
    SkipLinesIfEqual(1, left=left, right=11215350)
    IfClient(1)
    IfFlagEnabled(1, left)
    IfTimeElapsed(1, seconds=3.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)
    RestartEvent(event_id=event_id, event_slot=event_slot)
    Restart()


@NeverRestart(11210825)
def Event_11210825(_, flag: int, flag_1: int):
    """Event 11210825"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfTimeElapsed(1, seconds=10.0)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagEnabled(flag_1)
    DisableFlag(flag)
    Restart()


@NeverRestart(11210827)
def Event_11210827(_, flag: int, first_flag: int, last_flag: int, region: int):
    """Event 11210827"""
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagRangeAllEnabled(1, flag_range=(first_flag, last_flag))
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfMultiplayer(2)
    IfTrueFlagCountGreaterThanOrEqual(2, FlagType.Absolute, flag_range=(11215360, 11215365), value=2)
    IfFlagDisabled(2, 11215390)
    IfTimeElapsed(2, seconds=40.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((11218990, 11218999))
    EnableFlag(flag)
    RestartIfFlagDisabled(flag)


@NeverRestart(11210828)
def Event_11210828(_, flag: int, flag_1: int, flag_2: int, region: int):
    """Event 11210828"""
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((11218990, 11218999))
    EnableFlag(flag)
    RestartIfFlagDisabled(flag)


@NeverRestart(11210829)
def Event_11210829():
    """Event 11210829"""
    If_Unknown_3_23(1, unk1=0, unk2=0)
    IfFlagEnabled(2, 11215390)
    IfFlagDisabled(2, 6990)
    IfConditionFalse(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    EnableFlag(6990)
    Restart()


@NeverRestart(11210832)
def Event_11210832():
    """Event 11210832"""
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfConditionTrue(1, input_condition=-1)
    IfSingleplayer(1)
    IfFlagEnabled(1, 6990)
    IfConditionTrue(0, input_condition=1)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Restart()


@NeverRestart(11210932)
def Event_11210932():
    """Event 11210932"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215390)
    IfFlagRangeAllDisabled(1, flag_range=(11215350, 11215355))
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    DisplayBattlefieldMessage(150001, display_location_index=1)
    DisableFlagRange((6980, 6990))
    Wait(3.0)
    EnableAI(PLAYER)
    ArenaExitRequest()


@NeverRestart(11210830)
def Event_11210830():
    """Event 11210830"""
    IfFlagEnabled(-1, 11218990)
    IfFlagEnabled(-1, 11218991)
    IfFlagEnabled(-1, 11218992)
    IfFlagEnabled(-1, 11218993)
    IfFlagEnabled(-1, 11218994)
    IfFlagEnabled(-1, 11218995)
    IfFlagEnabled(-1, 11218996)
    IfFlagEnabled(-1, 11218997)
    IfFlagEnabled(-1, 11218998)
    IfFlagEnabled(-1, 11218999)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11215340)
    DisableFlag(11215392)
    DisableFlag(11215395)
    DisableFlag(11215402)
    DisableFlag(11215405)
    DisableFlag(11218000)
    DisableFlag(11218001)
    EnableFlagRange((6980, 6989))
    DisableFlag(6990)
    If_Unknown_3_23(3, unk1=0, unk2=0)
    SkipLinesIfConditionTrue(1, 3)
    DisableFlagRange((6980, 6989))
    IfCharacterInsideRegion(-2, PLAYER, region=1212715)
    IfCharacterInsideRegion(-2, PLAYER, region=1212714)
    IfCharacterInsideRegion(-2, PLAYER, region=1212713)
    IfCharacterInsideRegion(-2, PLAYER, region=1212797)
    IfCharacterInsideRegion(-2, PLAYER, region=1212793)
    IfCharacterInsideRegion(-3, PLAYER, region=1212702)
    IfCharacterInsideRegion(-3, PLAYER, region=1212701)
    IfCharacterInsideRegion(-3, PLAYER, region=1212700)
    IfCharacterInsideRegion(-3, PLAYER, region=1212794)
    IfCharacterInsideRegion(-3, PLAYER, region=1212796)
    SkipLinesIfConditionTrue(1, -2)
    SkipLines(2)
    EnableFlag(11218000)
    DisableFlagRange((6980, 6984))
    SkipLinesIfConditionTrue(1, -3)
    SkipLines(2)
    EnableFlag(11218001)
    DisableFlagRange((6985, 6989))
    SkipLinesIfFlagEnabled(2, 11218990)
    SkipLinesIfFlagEnabled(1, 11218991)
    SkipLines(5)
    EnableFlag(11215408)
    DisableFlagRange((6981, 6984))
    DisableFlagRange((6986, 6989))
    EnableFlag(11218348)
    EnableFlag(11218350)
    SkipLinesIfFlagEnabled(2, 11218992)
    SkipLinesIfFlagEnabled(1, 11218993)
    SkipLines(7)
    EnableFlag(11215392)
    DisableFlag(6980)
    DisableFlag(6985)
    DisableFlagRange((6982, 6984))
    DisableFlagRange((6987, 6989))
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagEnabled(2, 11218994)
    SkipLinesIfFlagEnabled(1, 11218995)
    SkipLines(6)
    EnableFlag(11215395)
    DisableFlagRange((6980, 6981))
    DisableFlagRange((6985, 6986))
    DisableFlagRange((6983, 6984))
    DisableFlagRange((6988, 6989))
    EnableFlagRange((11218348, 11218351))
    SkipLinesIfFlagEnabled(2, 11218996)
    SkipLinesIfFlagEnabled(1, 11218997)
    SkipLines(7)
    EnableFlag(11215402)
    DisableFlagRange((6980, 6982))
    DisableFlagRange((6985, 6987))
    DisableFlag(6984)
    DisableFlag(6989)
    EnableFlag(11218354)
    EnableFlag(11218355)
    SkipLinesIfFlagEnabled(2, 11218998)
    SkipLinesIfFlagEnabled(1, 11218999)
    SkipLines(4)
    EnableFlag(11215405)
    DisableFlagRange((6980, 6983))
    DisableFlagRange((6985, 6988))
    EnableFlagRange((11218348, 11218353))
    Wait(8.0)
    SkipLinesIfFlagEnabled(5, 11215402)
    SkipLinesIfFlagEnabled(4, 11215405)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    DisplayBattlefieldMessage(150215, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(150205, display_location_index=1)
    Wait(2.0)
    DisplayBanner(BannerType.BeginMatch)
    EnableFlag(11215390)
    IfFlagDisabled(0, 11215390)
    Restart()


@NeverRestart(11210831)
def Event_11210831(_, flag: int, flag_1: int):
    """Event 11210831"""
    IfHost(1)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(2, 11215402)
    SkipLinesIfFlagEnabled(1, 11215392)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11210835)
def Event_11210835(_, seconds: float, seconds_1: float, seconds_2: float, seconds_3: float):
    """Event 11210835"""
    DisableNetworkSync()
    IfHost(1)
    IfFlagDisabled(1, 11215391)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagEnabled(5, 11215405)
    SkipLinesIfFlagEnabled(4, 11215402)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    Wait(seconds)
    SkipLines(1)
    Wait(seconds_2)
    SkipLinesIfFlagEnabled(1, 904)
    EnableFlag(11215396)
    SkipLinesIfFlagEnabled(5, 11215405)
    SkipLinesIfFlagEnabled(4, 11215402)
    SkipLinesIfFlagEnabled(3, 11215395)
    SkipLinesIfFlagEnabled(2, 11215392)
    Wait(seconds_1)
    SkipLines(1)
    Wait(seconds_3)
    IfFlagDisabled(0, 904)
    EnableFlag(11215391)
    Restart()


@NeverRestart(11210836)
def Event_11210836():
    """Event 11210836"""
    IfFlagEnabled(0, 11215396)
    EnableFlag(11215396)
    DisplayBattlefieldMessage(150110, display_location_index=0)
    IfFlagEnabled(0, 11215391)
    EnableFlag(11215391)
    DisplayBattlefieldMessage(150300, display_location_index=0)
    IfFlagDisabled(0, 11215391)
    Restart()


@NeverRestart(11210887)
def Event_11210887(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 11210887"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Unknown_4_15(0, unk1=1)
    SkipLinesIfFlagEnabled(4, 11215392)
    SkipLinesIfFlagEnabled(3, 11215402)
    SkipLinesIfFlagDisabled(2, flag_4)
    EqualRecovery()
    Unknown_2004_51(unk1=1)
    IfFlagDisabled(2, 11215392)
    IfFlagDisabled(2, 11215402)
    SkipLinesIfConditionTrue(1, 2)
    Unknown_2004_51(unk1=1)
    EnableFlag(flag_1)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    EnableFlag(flag_2)
    SkipLinesIfFlagEnabled(1, 11215408)
    EnableFlag(flag_3)
    IfFlagDisabled(0, flag_1)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    Restart()


@NeverRestart(11210889)
def Event_11210889(_, flag: int):
    """Event 11210889"""
    IfFlagDisabled(0, flag)
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    Restart()


@NeverRestart(11210888)
def Event_11210888(_, flag: int, flag_1: int):
    """Event 11210888"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, 11215391)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    IncrementEventValue(flag_1, bit_count=6, max_value=63)
    DisableFlag(flag)
    Restart()


@NeverRestart(11210891)
def Event_11210891(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int, flag_6: int):
    """Event 11210891"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfFlagDisabled(1, flag_4)
    IfFlagDisabled(1, flag_5)
    IfFlagDisabled(1, flag_6)
    IfConditionTrue(0, input_condition=1)
    Unknown_2007_13(unk1=10000)
    Restart()


@NeverRestart(11210892)
def Event_11210892(
    _,
    flag: int,
    left_flag: int,
    right_flag: int,
    right_flag_1: int,
    right_flag_2: int,
    right_flag_3: int,
    right_flag_4: int,
    flag_1: int,
):
    """Event 11210892"""
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagDisabled(1, 11215392)
    IfFlagDisabled(1, 11215402)
    IfFlagEnabled(1, flag)
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_1,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_2,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_3,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_4,
        right_bit_count=6,
    )
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    Restart()


@NeverRestart(11210893)
def Event_11210893():
    """Event 11210893"""
    IfFlagEnabled(0, 11218360)
    WaitFrames(frames=6)
    DisableFlag(11218360)
    Restart()


@NeverRestart(11210894)
def Event_11210894(
    _,
    flag: int,
    left_flag: int,
    right_flag: int,
    right_flag_1: int,
    right_flag_2: int,
    right_flag_3: int,
    right_flag_4: int,
    flag_1: int,
):
    """Event 11210894"""
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagDisabled(1, 11215392)
    IfFlagDisabled(1, 11215402)
    IfFlagEnabled(1, flag)
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_1,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_2,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_3,
        right_bit_count=6,
    )
    IfEventsComparison(
        -1,
        left_flag=left_flag,
        left_bit_count=6,
        comparison_type=ComparisonType.LessThan,
        right_flag=right_flag_4,
        right_bit_count=6,
    )
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11210895)
def Event_11210895(_, flag: int, flag_1: int):
    """Event 11210895"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11215392)
    IfFlagDisabled(1, 11215402)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EqualRecovery()
    Unknown_2004_51(unk1=1)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11212222)
def Event_11212222(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int, flag_6: int):
    """Event 11212222"""
    IfFlagEnabled(1, flag)
    IfHealthValueEqual(1, PLAYER, value=1)
    IfConditionTrue(0, input_condition=1)
    Unknown_4_16(2, unk1=0, unk2=0, unk3=0)
    SkipLinesIfConditionTrue(2, 2)
    WaitFrames(frames=7)
    Restart()
    SkipLinesIfFlagEnabled(7, 11215392)
    SkipLinesIfFlagEnabled(6, 11215402)
    EnableFlag(flag_2)
    SkipLinesIfFlagEnabled(6, 11215408)
    EnableFlag(flag_1)
    EnableFlag(flag_3)
    EnableFlag(flag_4)
    EnableFlag(flag_5)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    EnableFlag(flag_6)
    WaitFrames(frames=7)
    Restart()


@NeverRestart(11210840)
def Event_11210840(_, flag: int, flag_1: int, flag_2: int):
    """Event 11210840"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfHealthValueEqual(1, PLAYER, value=1)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90001)
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    AddSpecialEffect(PLAYER, 4611)
    SkipLinesIfFlagDisabled(1, flag)
    DisplayBattlefieldMessage(506107, display_location_index=3)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    IfFlagDisabled(0, flag_2)
    DisableFlag(flag_2)
    SkipLinesIfFlagEnabled(1, flag)
    DisableInvincibility(PLAYER)
    CancelSpecialEffect(PLAYER, 4611)
    ResetAnimation(PLAYER, disable_interpolation=1)
    SkipLinesIfFlagEnabled(2, flag)
    ForceAnimation_Unknown_2003_44(
        entity=PLAYER,
        animation=6951,
        loop=0,
        wait_for_completion=1,
        skip_transition=0,
        unk1=0,
    )
    SkipLines(1)
    ForceAnimation_Unknown_2003_44(
        entity=PLAYER,
        animation=6951,
        loop=0,
        wait_for_completion=1,
        skip_transition=0,
        unk1=0,
    )
    ResetAnimation(PLAYER, disable_interpolation=1)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(11210833)
def Event_11210833():
    """Event 11210833"""
    DisableNetworkSync()
    IfHealthValueEqual(0, PLAYER, value=1)
    WaitFrames(frames=6)
    EqualRecovery()
    SkipLinesIfFlagEnabled(1, 11215408)
    Unknown_2004_51(unk1=1)
    Restart()


@NeverRestart(11210777)
def Event_11210777(_, flag: int, flag_1: int):
    """Event 11210777"""
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    Wait(2.0)
    IfFlagDisabled(2, flag_1)
    IfFlagEnabled(2, flag)
    IfFramesElapsed(2, frames=120)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfFlagEnabled(2, flag)
    CreateTemporaryVFX(vfx_id=20176, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    SkipLines(1)
    Unknown_2003_48(
        entity=PLAYER,
        unk1=0,
        model_point=220,
        magic_id=5310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@NeverRestart(11210850)
def Event_11210850(_, flag: int, flag_1: int, region: int, first_region: int, last_region: int):
    """Event 11210850"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    Wait(2.0)
    SkipLinesIfFlagEnabled(3, 11215392)
    SkipLinesIfFlagEnabled(2, 11215402)
    PlayCutsceneAndRandomlyWarpPlayer_2002_6(
        120130,
        cutscene_flags=CutsceneFlags.Unskippable,
        first_region=first_region,
        last_region=last_region,
        game_map=OOLACILE,
    )
    SkipLines(1)
    PlayCutsceneAndRandomlyWarpPlayer_2002_7(
        120130,
        cutscene_flags=CutsceneFlags.Unskippable,
        first_region=first_region,
        last_region=last_region,
        game_map=OOLACILE,
    )
    WaitFrames(frames=1)
    EnableAI(PLAYER)
    EqualRecovery()
    SkipLinesIfFlagEnabled(1, 11215408)
    Unknown_2004_51(unk1=1)
    DisableFlag(flag_1)
    Wait(6.0)
    CancelSpecialEffect(PLAYER, 90001)
    DisableInvincibility(PLAYER)
    Restart()


@NeverRestart(11210886)
def Event_11210886(_, flag: int, flag_1: int):
    """Event 11210886"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    FadeOutCharacter(character=PLAYER, duration=2.0)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfTimeElapsed(2, seconds=3.0)
    IfConditionTrue(0, input_condition=2)
    FadeInCharacter(character=PLAYER, duration=1.0)
    Restart()


@NeverRestart(11210688)
def Event_11210688(_, flag: int, flag_1: int):
    """Event 11210688"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, flag)
    IfFramesElapsed(2, frames=30)
    IfConditionTrue(0, input_condition=2)
    CancelSpecialEffect(PLAYER, 4611)
    IfFlagEnabled(3, flag)
    IfFlagDisabled(3, flag_1)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart(11210870)
def Event_11210870(_, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 11210870"""
    DisableNetworkSync()
    If_Unknown_3_23(7, unk1=0, unk2=0)
    SkipLinesIfConditionFalse(1, 7)
    EnableFlag(11219000)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, 11215390)
    IfFlagEnabled(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    AddSpecialEffect(PLAYER, 90000)
    Wait(6.0)
    EnableFlag(11215397)
    SkipLinesIfFlagEnabled(2, 11215392)
    SkipLinesIfFlagEnabled(1, 11215402)
    IfFlagEnabled(3, flag_1)
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215405)
    SkipLinesIfFlagEnabled(1, 11215395)
    IfFlagEnabled(3, flag_2)
    SkipLinesIfFlagEnabled(2, 11215392)
    SkipLinesIfFlagEnabled(1, 11215402)
    IfFlagDisabled(5, flag_1)
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215405)
    SkipLinesIfFlagEnabled(1, 11215395)
    IfFlagDisabled(5, flag_2)
    SkipLinesIfFlagEnabled(13, 11215402)
    SkipLinesIfFlagEnabled(12, 11215392)
    SkipLinesIfFlagEnabled(1, 11215350)
    IfFlagEnabled(-1, 11218348)
    SkipLinesIfFlagEnabled(1, 11215351)
    IfFlagEnabled(-1, 11218349)
    SkipLinesIfFlagEnabled(1, 11215352)
    IfFlagEnabled(-1, 11218350)
    SkipLinesIfFlagEnabled(1, 11215353)
    IfFlagEnabled(-1, 11218351)
    SkipLinesIfFlagEnabled(1, 11215354)
    IfFlagEnabled(-1, 11218352)
    SkipLinesIfFlagEnabled(1, 11215355)
    IfFlagEnabled(-1, 11218353)
    SkipLinesIfFlagEnabled(3, 11215408)
    SkipLinesIfFlagEnabled(2, 11215395)
    SkipLinesIfFlagEnabled(1, 11215405)
    IfFlagEnabled(-1, flag_3)
    IfConditionTrue(6, input_condition=3)
    IfConditionTrue(6, input_condition=-1)
    IfConditionTrue(2, input_condition=3)
    IfConditionFalse(2, input_condition=-1)
    SkipLinesIfFlagRangeAllDisabled(1, (11218342, 11218347))
    DisplayBattlefieldMessage(150420, display_location_index=3)
    SkipLinesIfConditionTrue(3, 2)
    SkipLinesIfConditionTrue(17, 5)
    SkipLinesIfConditionTrue(9, 6)
    SkipLines(8)
    EnableFlag(11215393)
    DisplayBanner(BannerType.YouWin)
    Wait(2.0)
    SkipLinesIfFlagDisabled(1, 11219000)
    DisplayBattlefieldMessage(150050, display_location_index=1)
    SkipLinesIfFlagEnabled(1, 11219000)
    DisplayBattlefieldMessage(150051, display_location_index=1)
    SkipLines(38)
    DisplayBanner(BannerType.Draw)
    Wait(2.0)
    SkipLinesIfFlagDisabled(1, 11219000)
    DisplayBattlefieldMessage(150055, display_location_index=1)
    SkipLinesIfFlagEnabled(1, 11219000)
    DisplayBattlefieldMessage(150056, display_location_index=1)
    SkipLines(7)
    Event_11210871()
    DisplayBanner(BannerType.YouLose)
    Wait(2.0)
    SkipLinesIfFlagDisabled(1, 11219000)
    DisplayBattlefieldMessage(150060, display_location_index=1)
    SkipLinesIfFlagEnabled(1, 11219000)
    DisplayBattlefieldMessage(150061, display_location_index=1)
    SkipLinesIfConditionTrue(1, 5)
    SkipLines(10)
    SkipLinesIfFlagDisabled(1, 11215408)
    Unknown_2003_43(flag=6040, bit_count=10, unk1=0, unk2=2)
    SkipLinesIfFlagDisabled(1, 11215392)
    Unknown_2003_43(flag=6090, bit_count=10, unk1=1, unk2=2)
    SkipLinesIfFlagDisabled(1, 11215402)
    Unknown_2003_43(flag=6140, bit_count=10, unk1=2, unk2=2)
    SkipLinesIfFlagDisabled(1, 11215395)
    Unknown_2003_43(flag=6190, bit_count=10, unk1=3, unk2=2)
    SkipLinesIfFlagDisabled(1, 11215405)
    Unknown_2003_43(flag=6240, bit_count=10, unk1=4, unk2=2)
    SkipLinesIfConditionTrue(1, -1)
    SkipLines(10)
    SkipLinesIfFlagDisabled(1, 11215408)
    Unknown_2003_43(flag=6040, bit_count=10, unk1=0, unk2=1)
    SkipLinesIfFlagDisabled(1, 11215392)
    Unknown_2003_43(flag=6090, bit_count=10, unk1=1, unk2=1)
    SkipLinesIfFlagDisabled(1, 11215402)
    Unknown_2003_43(flag=6140, bit_count=10, unk1=2, unk2=1)
    SkipLinesIfFlagDisabled(1, 11215395)
    Unknown_2003_43(flag=6190, bit_count=10, unk1=3, unk2=1)
    SkipLinesIfFlagDisabled(1, 11215405)
    Unknown_2003_43(flag=6240, bit_count=10, unk1=4, unk2=1)
    Wait(8.0)
    EnableFlag(11215891)
    DisableInvincibility(PLAYER)
    Unknown_2004_52()
    EqualRecovery()
    CancelSpecialEffect(PLAYER, 90000)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    ArenaExitRequest()
    DisableFlag(11219000)
    EnableFlag(11218900)


@NeverRestart(11210871)
def Event_11210871():
    """Event 11210871"""
    SkipLinesIfFlagDisabled(3, 11215408)
    DisableFlagRange((7040, 7049))
    DisableFlagRange((7250, 7299))
    DisableFlagRange((7500, 7549))
    SkipLinesIfFlagDisabled(3, 11215392)
    DisableFlagRange((7090, 7099))
    DisableFlagRange((7300, 7349))
    DisableFlagRange((7550, 7599))
    SkipLinesIfFlagDisabled(3, 11215402)
    DisableFlagRange((7140, 7149))
    DisableFlagRange((7350, 7399))
    DisableFlagRange((7600, 7649))
    SkipLinesIfFlagDisabled(3, 11215395)
    DisableFlagRange((7190, 7199))
    DisableFlagRange((7400, 7449))
    DisableFlagRange((7650, 7699))
    SkipLinesIfFlagDisabled(3, 11215405)
    DisableFlagRange((7240, 7249))
    DisableFlagRange((7450, 7499))
    DisableFlagRange((7700, 7749))


@NeverRestart(11210875)
def Event_11210875(_, left: int, message_id: int, concatenator_base_flag: int):
    """Event 11210875"""
    IfCharacterInsideRegion(2, PLAYER, region=1218900)
    IfFlagEnabled(2, left)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(left)
    EqualRecovery()
    AddSpecialEffect(PLAYER, 101)
    AddSpecialEffect(PLAYER, 102)
    AddSpecialEffect(PLAYER, 103)
    AddSpecialEffect(PLAYER, 104)
    Wait(0.0)
    SkipLinesIfEqual(1, left=left, right=6990)
    DisplayConcatenatedMessage(
        message_id=message_id,
        pad_enabled=1,
        concatenator_base_flag=concatenator_base_flag,
        bit_count=10,
    )
    Restart()


@NeverRestart(11210705)
def Event_11210705():
    """Event 11210705"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11215392)
    IfFlagDisabled(1, 11215395)
    IfFlagEnabled(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(2, 11215380)
    IncrementEventValue(7000, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7000,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6000,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215381)
    IncrementEventValue(7050, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7050,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6050,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215382)
    IncrementEventValue(7100, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7100,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6100,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215383)
    IncrementEventValue(7150, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7150,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6150,
        right_bit_count=10,
    )
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagDisabled(1, 11215380)
    IncrementEventValue(6000, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215381)
    IncrementEventValue(6050, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215382)
    IncrementEventValue(6100, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215383)
    IncrementEventValue(6150, bit_count=10, max_value=1000)
    IfEventsComparison(
        3,
        left_flag=7200,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6200,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6200, bit_count=10, max_value=1000)
    ArenaRankingRequest1v1()
    DisableFlag(11215393)
    Restart()


@NeverRestart(11210706)
def Event_11210706():
    """Event 11210706"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215392)
    IfFlagDisabled(1, 11215395)
    IfFlagEnabled(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(2, 11215380)
    IncrementEventValue(7250, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7250,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6250,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215381)
    IncrementEventValue(7300, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7300,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6300,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215382)
    IncrementEventValue(7350, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7350,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6350,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215383)
    IncrementEventValue(7400, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7400,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6400,
        right_bit_count=10,
    )
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagDisabled(1, 11215380)
    IncrementEventValue(6250, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215381)
    IncrementEventValue(6300, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215382)
    IncrementEventValue(6350, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215383)
    IncrementEventValue(6400, bit_count=10, max_value=1000)
    IfEventsComparison(
        3,
        left_flag=7450,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6450,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6450, bit_count=10, max_value=1000)
    ArenaRankingRequest2v2()
    DisableFlag(11215393)
    Restart()


@NeverRestart(11210707)
def Event_11210707():
    """Event 11210707"""
    DisableNetworkSync()
    IfFlagDisabled(1, 11215392)
    IfFlagEnabled(1, 11215395)
    IfFlagEnabled(1, 11215393)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(2, 11215380)
    IncrementEventValue(7500, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7500,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6500,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215381)
    IncrementEventValue(7550, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7550,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6550,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215382)
    IncrementEventValue(7600, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7600,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6600,
        right_bit_count=10,
    )
    SkipLinesIfFlagDisabled(2, 11215383)
    IncrementEventValue(7650, bit_count=10, max_value=1000)
    IfEventsComparison(
        2,
        left_flag=7650,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6650,
        right_bit_count=10,
    )
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    SkipLinesIfConditionTrue(3, 2)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()
    SkipLinesIfFlagDisabled(1, 11215380)
    IncrementEventValue(6500, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215381)
    IncrementEventValue(6550, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215382)
    IncrementEventValue(6600, bit_count=10, max_value=1000)
    SkipLinesIfFlagDisabled(1, 11215383)
    IncrementEventValue(6650, bit_count=10, max_value=1000)
    IfEventsComparison(
        3,
        left_flag=7700,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=6700,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(6700, bit_count=10, max_value=1000)
    ArenaRankingRequestFFA()
    DisableFlag(11215393)
    Restart()


@NeverRestart(11210727)
def Event_11210727():
    """Event 11210727"""
    DisableNetworkSync()
    If_Unknown_3_23(1, unk1=0, unk2=0)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, 11215393)
    SkipLinesIfFlagDisabled(55, 11218001)
    SkipLinesIfFlagDisabled(10, 11215408)
    IncrementEventValue(7290, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7290, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7250,
        destination_flag__left_flag__right_flag__source_flag=6250,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6000
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7260,
        destination_flag__left_flag__right_flag__source_flag=6260,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6010
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7270,
        destination_flag__left_flag__right_flag__source_flag=6270,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6020
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7280,
        destination_flag__left_flag__right_flag__source_flag=6280,
        unk1=0,
        left_flag__source_flag_1=7290,
        destination_flag__right_flag=6290,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6030
    )
    SkipLinesIfFlagDisabled(10, 11215392)
    IncrementEventValue(7340, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7340, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7300,
        destination_flag__left_flag__right_flag__source_flag=6300,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6050
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7310,
        destination_flag__left_flag__right_flag__source_flag=6310,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6060
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7320,
        destination_flag__left_flag__right_flag__source_flag=6320,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6070
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7330,
        destination_flag__left_flag__right_flag__source_flag=6330,
        unk1=1,
        left_flag__source_flag_1=7340,
        destination_flag__right_flag=6340,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6080
    )
    SkipLinesIfFlagDisabled(10, 11215402)
    IncrementEventValue(7390, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7390, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7350,
        destination_flag__left_flag__right_flag__source_flag=6350,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6100
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7360,
        destination_flag__left_flag__right_flag__source_flag=6360,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6110
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7370,
        destination_flag__left_flag__right_flag__source_flag=6370,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6120
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7380,
        destination_flag__left_flag__right_flag__source_flag=6380,
        unk1=2,
        left_flag__source_flag_1=7390,
        destination_flag__right_flag=6390,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6130
    )
    SkipLinesIfFlagDisabled(10, 11215395)
    IncrementEventValue(7440, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7440, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7400,
        destination_flag__left_flag__right_flag__source_flag=6400,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6150
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7410,
        destination_flag__left_flag__right_flag__source_flag=6410,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6160
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7420,
        destination_flag__left_flag__right_flag__source_flag=6420,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6170
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7430,
        destination_flag__left_flag__right_flag__source_flag=6430,
        unk1=3,
        left_flag__source_flag_1=7440,
        destination_flag__right_flag=6440,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6180
    )
    SkipLinesIfFlagDisabled(10, 11215405)
    IncrementEventValue(7490, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7490, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7450,
        destination_flag__left_flag__right_flag__source_flag=6450,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6200
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7460,
        destination_flag__left_flag__right_flag__source_flag=6460,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6210
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7470,
        destination_flag__left_flag__right_flag__source_flag=6470,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6220
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7480,
        destination_flag__left_flag__right_flag__source_flag=6480,
        unk1=4,
        left_flag__source_flag_1=7490,
        destination_flag__right_flag=6490,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6230
    )
    SkipLinesIfFlagDisabled(55, 11218000)
    SkipLinesIfFlagDisabled(10, 11215408)
    IncrementEventValue(7540, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7540, destination_flag=7040, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7500,
        destination_flag__left_flag__right_flag__source_flag=6500,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6000
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7510,
        destination_flag__left_flag__right_flag__source_flag=6510,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6010
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7520,
        destination_flag__left_flag__right_flag__source_flag=6520,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6020
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7530,
        destination_flag__left_flag__right_flag__source_flag=6530,
        unk1=0,
        left_flag__source_flag_1=7540,
        destination_flag__right_flag=6540,
        destination_flag__right_flag_1=6040,
        destination_flag__right_flag_2=6030
    )
    SkipLinesIfFlagDisabled(10, 11215392)
    IncrementEventValue(7590, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7590, destination_flag=7090, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7550,
        destination_flag__left_flag__right_flag__source_flag=6550,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6050
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7560,
        destination_flag__left_flag__right_flag__source_flag=6560,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6060
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7570,
        destination_flag__left_flag__right_flag__source_flag=6570,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6070
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7580,
        destination_flag__left_flag__right_flag__source_flag=6580,
        unk1=1,
        left_flag__source_flag_1=7590,
        destination_flag__right_flag=6590,
        destination_flag__right_flag_1=6090,
        destination_flag__right_flag_2=6080
    )
    SkipLinesIfFlagDisabled(10, 11215402)
    IncrementEventValue(7640, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7640, destination_flag=7140, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7600,
        destination_flag__left_flag__right_flag__source_flag=6600,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6100
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7610,
        destination_flag__left_flag__right_flag__source_flag=6610,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6110
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7620,
        destination_flag__left_flag__right_flag__source_flag=6620,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6120
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7630,
        destination_flag__left_flag__right_flag__source_flag=6630,
        unk1=2,
        left_flag__source_flag_1=7640,
        destination_flag__right_flag=6640,
        destination_flag__right_flag_1=6140,
        destination_flag__right_flag_2=6130
    )
    SkipLinesIfFlagDisabled(10, 11215395)
    IncrementEventValue(7690, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7690, destination_flag=7190, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7650,
        destination_flag__left_flag__right_flag__source_flag=6650,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6150
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7660,
        destination_flag__left_flag__right_flag__source_flag=6660,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6160
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7670,
        destination_flag__left_flag__right_flag__source_flag=6670,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6170
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7680,
        destination_flag__left_flag__right_flag__source_flag=6680,
        unk1=3,
        left_flag__source_flag_1=7690,
        destination_flag__right_flag=6690,
        destination_flag__right_flag_1=6190,
        destination_flag__right_flag_2=6180
    )
    SkipLinesIfFlagDisabled(10, 11215405)
    IncrementEventValue(7740, bit_count=10, max_value=1000)
    CopyEventValue(source_flag=7740, destination_flag=7240, bit_count=10)
    SkipLinesIfFlagDisabled(1, 11215380)
    Event_11210717(
        0,
        left_flag__source_flag=7700,
        destination_flag__left_flag__right_flag__source_flag=6700,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6200
    )
    SkipLinesIfFlagDisabled(1, 11215381)
    Event_11210717(
        0,
        left_flag__source_flag=7710,
        destination_flag__left_flag__right_flag__source_flag=6710,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6210
    )
    SkipLinesIfFlagDisabled(1, 11215382)
    Event_11210717(
        0,
        left_flag__source_flag=7720,
        destination_flag__left_flag__right_flag__source_flag=6720,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6220
    )
    SkipLinesIfFlagDisabled(1, 11215383)
    Event_11210717(
        0,
        left_flag__source_flag=7730,
        destination_flag__left_flag__right_flag__source_flag=6730,
        unk1=4,
        left_flag__source_flag_1=7740,
        destination_flag__right_flag=6740,
        destination_flag__right_flag_1=6240,
        destination_flag__right_flag_2=6230
    )
    DisableFlag(11215393)
    Restart()


@NeverRestart(11210717)
def Event_11210717(
    _,
    left_flag__source_flag: int,
    destination_flag__left_flag__right_flag__source_flag: int,
    unk1: uchar,
    left_flag__source_flag_1: int,
    destination_flag__right_flag: int,
    destination_flag__right_flag_1: int,
    destination_flag__right_flag_2: int,
):
    """Event 11210717"""
    DisableNetworkSync()
    IncrementEventValue(left_flag__source_flag, bit_count=10, max_value=1000)
    IfEventsComparison(
        1,
        left_flag=left_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__left_flag__right_flag__source_flag,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 1)
    CopyEventValue(
        source_flag=left_flag__source_flag,
        destination_flag=destination_flag__left_flag__right_flag__source_flag,
        bit_count=10,
    )
    IfEventsComparison(
        4,
        left_flag=destination_flag__left_flag__right_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag_2,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 4)
    CopyEventValue(
        source_flag=destination_flag__left_flag__right_flag__source_flag,
        destination_flag=destination_flag__right_flag_2,
        bit_count=10,
    )
    IfEventsComparison(
        2,
        left_flag=left_flag__source_flag_1,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 2)
    CopyEventValue(source_flag=left_flag__source_flag_1, destination_flag=destination_flag__right_flag, bit_count=10)
    IfEventsComparison(
        3,
        left_flag=destination_flag__left_flag__right_flag__source_flag,
        left_bit_count=10,
        comparison_type=ComparisonType.GreaterThan,
        right_flag=destination_flag__right_flag_1,
        right_bit_count=10,
    )
    SkipLinesIfConditionFalse(1, 3)
    CopyEventValue(
        source_flag=destination_flag__left_flag__right_flag__source_flag,
        destination_flag=destination_flag__right_flag_1,
        bit_count=10,
    )
    Unknown_2003_43(flag=destination_flag__right_flag_1, bit_count=10, unk1=unk1, unk2=0)
    End()


@NeverRestart(11210838)
def Event_11210838():
    """Event 11210838"""
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfConditionTrue(0, input_condition=-1)
    EqualRecovery()


@NeverRestart(11210839)
def Event_11210839():
    """Event 11210839"""
    DisableNetworkSync()
    DisableFlagRange((8140, 8146))


@NeverRestart(11210877)
def Event_11210877():
    """Event 11210877"""
    DisableNetworkSync()
    IfFlagEnabled(7, 11215390)
    IfFlagRangeAllDisabled(7, flag_range=(11215380, 11215383))
    IfConditionTrue(0, input_condition=7)
    IfPlayerLevelLessThanOrEqual(1, value=50)
    SkipLinesIfConditionFalse(2, 1)
    EnableFlag(11215380)
    Restart()
    IfPlayerLevelGreaterThan(2, value=50)
    IfPlayerLevelLessThanOrEqual(2, value=100)
    SkipLinesIfConditionFalse(2, 2)
    EnableFlag(11215381)
    Restart()
    IfPlayerLevelGreaterThan(3, value=100)
    IfPlayerLevelLessThanOrEqual(3, value=200)
    SkipLinesIfConditionFalse(2, 3)
    EnableFlag(11215382)
    Restart()
    EnableFlag(11215383)
    Restart()


@NeverRestart(11210890)
def Event_11210890():
    """Event 11210890"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfFlagDisabled(1, 8146)
    IfSingleplayer(1)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    SkipLinesIfFlagEnabled(3, 11218145)
    SkipLinesIfFlagEnabled(2, 8140)
    SkipLinesIfFlagEnabled(1, 11215350)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    Wait(3.0)
    ArenaExitRequest()
    Restart()


@NeverRestart(11210701)
def Event_11210701(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 11210701"""
    IfMultiplayer(1)
    IfFlagDisabled(-1, 11215396)
    IfFlagEnabled(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215891)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_4)
    IfFlagDisabled(2, 11215408)
    IfFlagDisabled(2, 11215395)
    IfFlagDisabled(2, 11215405)
    IfFlagDisabled(2, flag_3)
    IfFlagEnabled(2, flag_2)
    IfFlagEnabled(-5, 11215395)
    IfFlagEnabled(-5, 11215405)
    IfFlagEnabled(-5, 11215408)
    IfConditionTrue(3, input_condition=-5)
    IfFlagEnabled(3, flag_1)
    SkipLinesIfFlagEnabled(1, 11215350)
    IfFlagDisabled(3, 11218348)
    SkipLinesIfFlagEnabled(1, 11215352)
    IfFlagDisabled(3, 11218350)
    SkipLinesIfFlagEnabled(10, 11215408)
    SkipLinesIfFlagEnabled(1, 11215351)
    IfFlagDisabled(3, 11218349)
    SkipLinesIfFlagEnabled(1, 11215353)
    IfFlagDisabled(3, 11218351)
    SkipLinesIfFlagEnabled(5, 11215408)
    SkipLinesIfFlagEnabled(4, 11215395)
    SkipLinesIfFlagEnabled(1, 11215354)
    IfFlagDisabled(3, 11218352)
    SkipLinesIfFlagEnabled(1, 11215355)
    IfFlagDisabled(3, 11218353)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(4, 11215342)
    IfFlagEnabled(5, 11215343)
    IfFlagEnabled(6, 11215344)
    IfFlagEnabled(7, 11215345)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionFalse(1, condition=4)
    AddSpecialEffect(PLAYER, 4615)
    SkipLinesIfFinishedConditionFalse(1, condition=5)
    AddSpecialEffect(PLAYER, 4616)
    SkipLinesIfFinishedConditionFalse(1, condition=6)
    AddSpecialEffect(PLAYER, 4617)
    SkipLinesIfFinishedConditionFalse(1, condition=7)
    AddSpecialEffect(PLAYER, 4618)
    SkipLinesIfFinishedConditionTrue(4, condition=4)
    SkipLinesIfFinishedConditionTrue(3, condition=5)
    SkipLinesIfFinishedConditionTrue(2, condition=6)
    SkipLinesIfFinishedConditionTrue(1, condition=7)
    AddSpecialEffect(PLAYER, 4612)
    Wait(5.0)
    Restart()


@NeverRestart(11210430)
def Event_11210430(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int):
    """Event 11210430"""
    IfMultiplayer(1)
    IfFlagDisabled(-1, 11215396)
    IfFlagEnabled(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215891)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_5)
    IfFlagDisabled(2, 11215395)
    IfFlagDisabled(2, 11215405)
    IfFlagEnabled(2, 11215408)
    IfFlagEnabled(2, flag_1)
    IfFlagEnabled(2, flag_2)
    IfFlagEnabled(-4, 11215392)
    IfFlagEnabled(-4, 11215402)
    IfConditionTrue(3, input_condition=-4)
    IfFlagEnabled(3, flag_3)
    IfFlagEnabled(3, flag_4)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(-3, 11215399)
    IfFlagEnabled(-3, 11215397)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@NeverRestart(11210435)
def Event_11210435(
    _,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
    flag_7: int,
):
    """Event 11210435"""
    IfMultiplayer(1)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215891)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_7)
    IfFlagEnabled(-5, 11215395)
    IfFlagEnabled(-5, 11215405)
    IfConditionTrue(1, input_condition=-5)
    IfFlagEnabled(-1, 11215399)
    IfFlagEnabled(-1, 11215397)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(-2, 11215396)
    IfFlagEnabled(-2, 11215397)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(-3, flag_2)
    IfFlagEnabled(-3, flag_3)
    IfFlagEnabled(-3, flag_4)
    SkipLinesIfFlagDisabled(2, 11215405)
    IfFlagEnabled(-3, flag_5)
    IfFlagEnabled(-3, flag_6)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4614)
    Wait(5.0)
    Restart()


@NeverRestart(11214435)
def Event_11214435(_, flag: int, flag_1: int):
    """Event 11214435"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(2, 11215391)
    IfSingleplayer(2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 4612)
    CancelSpecialEffect(PLAYER, 4614)
    CancelSpecialEffect(PLAYER, 4615)
    CancelSpecialEffect(PLAYER, 4616)
    CancelSpecialEffect(PLAYER, 4617)
    CancelSpecialEffect(PLAYER, 4618)
    IfFlagEnabled(3, flag)
    IfFlagDisabled(3, flag_1)
    IfFlagDisabled(-2, 11215391)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@NeverRestart(11210434)
def Event_11210434():
    """Event 11210434"""
    EnableFlag(11215399)
    End()
    IfFlagEnabled(1, 11215390)
    IfFlagEnabled(1, 11215408)
    IfFlagRangeAnyEnabled(-2, flag_range=(11215300, 11215305))
    IfFlagRangeAnyEnabled(-2, flag_range=(11215312, 11215317))
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(2, 11215390)
    IfFlagEnabled(-1, 11215392)
    IfFlagEnabled(-1, 11215395)
    IfConditionTrue(2, input_condition=-1)
    IfFlagRangeAnyEnabled(-3, flag_range=(11215300, 11215305))
    IfFlagRangeAnyEnabled(-3, flag_range=(11215306, 11215311))
    IfFlagRangeAnyEnabled(-3, flag_range=(11215312, 11215317))
    IfFlagRangeAnyEnabled(-3, flag_range=(11215318, 11215323))
    IfConditionTrue(2, input_condition=-3)
    IfFlagEnabled(3, 11215390)
    IfFlagEnabled(-5, 11215402)
    IfFlagEnabled(-5, 11215405)
    IfConditionTrue(3, input_condition=-1)
    IfFlagRangeAnyEnabled(-5, flag_range=(11215300, 11215305))
    IfFlagRangeAnyEnabled(-5, flag_range=(11215306, 11215311))
    IfFlagRangeAnyEnabled(-5, flag_range=(11215312, 11215317))
    IfFlagRangeAnyEnabled(-5, flag_range=(11215318, 11215323))
    IfFlagRangeAnyEnabled(-5, flag_range=(11215324, 11215329))
    IfFlagRangeAnyEnabled(-5, flag_range=(11215330, 11215335))
    IfConditionTrue(3, input_condition=-5)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(0, input_condition=-7)
    EnableFlag(11215399)


@NeverRestart(11210845)
def Event_11210845():
    """Event 11210845"""
    IfFlagEnabled(1, 11215350)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag1(player_id=10000)


@NeverRestart(11210846)
def Event_11210846():
    """Event 11210846"""
    IfFlagEnabled(1, 11215351)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag2(player_id=10000)


@NeverRestart(11210847)
def Event_11210847():
    """Event 11210847"""
    IfFlagEnabled(1, 11215352)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag3(player_id=10000)


@NeverRestart(11210848)
def Event_11210848():
    """Event 11210848"""
    IfFlagEnabled(1, 11215353)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag4(player_id=10000)


@NeverRestart(11210860)
def Event_11210860():
    """Event 11210860"""
    IfFlagEnabled(1, 11215354)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag5(player_id=10000)


@NeverRestart(11210861)
def Event_11210861():
    """Event 11210861"""
    IfFlagEnabled(1, 11215355)
    IfFlagEnabled(1, 11215390)
    IfConditionTrue(0, input_condition=1)
    ArenaSetNametag6(player_id=10000)


@NeverRestart(11219121)
def Event_11219121():
    """Event 11219121"""
    IfHost(1)
    IfFlagDisabled(1, 9121)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9121)


@NeverRestart(11219122)
def Event_11219122():
    """Event 11219122"""
    IfFlagEnabled(1, 9121)
    IfFlagEnabled(-1, 11810000)
    IfFlagEnabled(-1, 257)
    IfFlagEnabled(-1, 710)
    IfConditionTrue(1, input_condition=-1)
    DisableFlag(9121)


@NeverRestart(11210849)
def Event_11210849():
    """Event 11210849"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(0, PLAYER, 17)
    EnableFlag(11215891)
    EnableFlag(8146)
    IfHost(1)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(8144)
    SkipLines(1)
    EnableFlag(8145)
    DisplayBattlefieldMessage(150031, display_location_index=1)
    Wait(1.0)
    DisableFlagRange((7000, 7749))
    Unknown_2004_52()
    ArenaExitRequest()
    EqualRecovery()
    Wait(3.0)
    WarpToMap(game_map=OOLACILE, player_start=1218146)
    Restart()


@NeverRestart(11210826)
def Event_11210826():
    """Event 11210826"""
    IfFlagEnabled(0, 8145)
    EnableFlag(8140)
    EnableFlag(11215891)


@NeverRestart(11210837)
def Event_11210837():
    """Event 11210837"""
    IfFlagEnabled(1, 8145)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    Unknown_2000_6(unk1=0)
    SkipLinesIfFlagEnabled(4, 11218145)
    SkipLinesIfFlagDisabled(1, 8145)
    SkipLinesIfFlagEnabled(2, 11215350)
    SkipLinesIfFlagEnabled(1, 8145)
    DisplayBattlefieldMessage(150040, display_location_index=1)
    SkipLinesIfFlagDisabled(2, 8145)
    Wait(3.0)
    ArenaExitRequest()
    Restart()


@NeverRestart(11210817)
def Event_11210817():
    """Event 11210817"""
    IfFlagEnabled(1, 8144)
    IfFlagEnabled(1, 11215390)
    IfFlagDisabled(1, 11215391)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(1, 8145)
    SkipLinesIfFlagEnabled(2, 11215350)
    SkipLinesIfFlagEnabled(1, 8144)
    DisplayBattlefieldMessage(20000437, display_location_index=1)
    Restart()


@NeverRestart(11210401)
def Event_11210401():
    """Event 11210401"""
    DisableNetworkSync()
    IfMultiplayer(1)
    IfTrueFlagCountGreaterThanOrEqual(1, FlagType.Absolute, flag_range=(11215360, 11215365), value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 4613)
    IfFlagDisabled(1, 11215340)
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    RestartIfFlagEnabled(11215340)
    RestartIfSingleplayer()
    DisplayBattlefieldMessage(150000, display_location_index=1)
    Wait(5.0)
    Restart()


@NeverRestart(11210402)
def Event_11210402():
    """Event 11210402"""
    DisableNetworkSync()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2320)
    IfCharacterHasSpecialEffect(-2, PLAYER, 2330)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 2320)
    CancelSpecialEffect(PLAYER, 2330)
    Restart()


@NeverRestart(11210404)
def Event_11210404(_, flag: int, flag_1: int, flag_2: int):
    """Event 11210404"""
    DisableNetworkSync()
    IfFlagEnabled(6, 11215340)
    IfFlagEnabled(6, flag_1)
    IfFlagEnabled(6, flag_2)
    IfConditionTrue(0, input_condition=6)
    IfEventValueLessThan(1, flag=flag, bit_count=10, value=10)
    IfEventValueGreaterThanOrEqual(2, flag=flag, bit_count=10, value=10)
    IfEventValueLessThan(2, flag=flag, bit_count=10, value=30)
    IfEventValueGreaterThanOrEqual(3, flag=flag, bit_count=10, value=30)
    IfEventValueLessThan(3, flag=flag, bit_count=10, value=50)
    IfEventValueGreaterThanOrEqual(4, flag=flag, bit_count=10, value=50)
    IfEventValueLessThan(4, flag=flag, bit_count=10, value=100)
    IfEventValueGreaterThanOrEqual(5, flag=flag, bit_count=10, value=100)
    SkipLinesIfConditionFalse(1, 2)
    EnableFlag(11215342)
    SkipLinesIfConditionFalse(1, 3)
    EnableFlag(11215343)
    SkipLinesIfConditionFalse(1, 4)
    EnableFlag(11215344)
    SkipLinesIfConditionFalse(1, 5)
    EnableFlag(11215345)


@NeverRestart(11210407)
def Event_11210407():
    """Event 11210407"""
    DisableNetworkSync()
    SkipLinesIfFlagDisabled(2, 11210709)
    DisableFlag(11210709)
    End()
    EndIfMultiplayer()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    EndIfConditionFalse(-1)
    Wait(2.0)
    Event_11216300()
    Event_11216301()
    Event_11216200(0, value=1, text=60000001)
    Event_11216200(1, value=2, text=60000002)
    Event_11216200(2, value=3, text=60000003)
    Event_11216200(3, value=4, text=60000004)
    Event_11216200(4, value=5, text=60000005)
    Event_11216200(5, value=6, text=60000006)
    Event_11216200(6, value=7, text=60000007)
    Event_11216200(7, value=8, text=60000008)
    Event_11216200(8, value=9, text=60000009)
    Event_11216200(9, value=10, text=60000010)
    Event_11216200(10, value=11, text=60000011)
    Event_11216200(11, value=12, text=60000012)
    Event_11216200(12, value=13, text=60000013)
    Event_11216200(13, value=14, text=60000014)
    Event_11216200(14, value=15, text=60000015)
    Event_11216200(15, value=16, text=60000016)
    Event_11216200(16, value=17, text=60000017)
    Event_11216200(17, value=18, text=60000018)
    Event_11216200(18, value=19, text=60000019)
    Event_11216200(19, value=20, text=60000020)
    Event_11216200(20, value=21, text=60000021)
    Event_11216200(21, value=22, text=60000022)
    Event_11216200(22, value=23, text=60000023)
    Event_11216200(23, value=24, text=60000024)
    Event_11216200(24, value=25, text=60000025)
    Event_11216200(25, value=26, text=60000026)
    Event_11216200(26, value=27, text=60000027)
    Event_11216200(27, value=28, text=60000028)
    Event_11216200(28, value=29, text=60000029)
    Event_11216200(29, value=30, text=60000030)
    Event_11216200(30, value=31, text=60000031)
    Event_11216200(31, value=32, text=60000032)
    Event_11216200(32, value=33, text=60000033)
    Event_11216200(33, value=34, text=60000034)
    Event_11216200(34, value=35, text=60000035)
    Event_11216200(35, value=36, text=60000036)
    Event_11216200(36, value=37, text=60000037)
    Event_11216200(37, value=38, text=60000038)
    Event_11216200(38, value=39, text=60000039)
    Event_11216200(39, value=40, text=60000040)
    Event_11216200(40, value=41, text=60000041)
    Event_11216200(41, value=42, text=60000042)
    Event_11216200(42, value=43, text=60000043)
    Event_11216200(43, value=44, text=60000044)
    Event_11216200(44, value=45, text=60000045)
    Event_11216200(45, value=46, text=60000046)
    Event_11216200(46, value=47, text=60000047)
    Event_11216200(47, value=48, text=60000048)
    Event_11216200(48, value=49, text=60000049)
    Event_11216200(49, value=50, text=60000050)
    Event_11216200(50, value=51, text=60000051)
    Event_11216200(51, value=52, text=60000052)
    Event_11216200(52, value=53, text=60000053)
    Event_11216200(53, value=54, text=60000054)
    Event_11216200(54, value=55, text=60000055)
    Event_11216200(55, value=56, text=60000056)
    Event_11216200(56, value=57, text=60000057)
    Event_11216200(57, value=58, text=60000058)
    Event_11216200(58, value=59, text=60000059)
    Event_11216200(59, value=60, text=60000060)
    Event_11216200(60, value=61, text=60000061)
    Event_11216200(61, value=62, text=60000062)
    Event_11216200(62, value=63, text=60000063)
    Event_11216200(63, value=64, text=60000064)
    Event_11216200(64, value=65, text=60000065)
    Event_11216200(65, value=66, text=60000066)
    Event_11216200(66, value=67, text=60000067)
    Event_11216200(67, value=68, text=60000068)
    Event_11216200(68, value=69, text=60000069)
    Event_11216200(69, value=70, text=60000070)
    Event_11216200(70, value=71, text=60000071)
    Event_11216200(71, value=72, text=60000072)
    Event_11216200(72, value=73, text=60000073)
    Event_11216200(73, value=74, text=60000074)
    Event_11216200(74, value=75, text=60000075)
    Event_11216200(75, value=76, text=60000076)
    Event_11216200(76, value=77, text=60000077)
    Event_11216200(77, value=78, text=60000078)
    Event_11216200(78, value=79, text=60000079)
    Event_11216200(79, value=80, text=60000080)
    Event_11216200(80, value=81, text=60000081)
    Event_11216200(81, value=82, text=60000082)
    Event_11216200(82, value=83, text=60000083)
    Event_11216200(83, value=84, text=60000084)
    Event_11216200(84, value=85, text=60000085)
    Event_11216200(85, value=86, text=60000086)
    Event_11216200(86, value=87, text=60000087)
    Event_11216200(87, value=88, text=60000088)
    Event_11216200(88, value=89, text=60000089)
    Event_11216200(89, value=90, text=60000090)
    Event_11216200(90, value=91, text=60000091)
    Event_11216200(91, value=92, text=60000092)
    Event_11216200(92, value=93, text=60000093)
    Event_11216200(93, value=94, text=60000094)
    Event_11216200(94, value=95, text=60000095)
    Event_11216200(95, value=96, text=60000096)
    Event_11216200(96, value=97, text=60000097)
    Event_11216200(97, value=98, text=60000098)
    Event_11216200(98, value=99, text=60000099)
    Event_11216200(99, 100, 60000100)


@NeverRestart(11216200)
def Event_11216200(_, value: uint, text: int):
    """Event 11216200"""
    DisableNetworkSync()
    IfEventValueEqual(-1, flag=7200, bit_count=10, value=value)
    IfEventValueEqual(-1, flag=7450, bit_count=10, value=value)
    IfEventValueEqual(-1, flag=7700, bit_count=10, value=value)
    EndIfConditionFalse(-1)
    DisplayStatus(text)


@NeverRestart(11216300)
def Event_11216300():
    """Event 11216300"""
    DisableNetworkSync()
    IfEventValueEqual(1, flag=7200, bit_count=10, value=0)
    IfEventValueEqual(1, flag=7450, bit_count=10, value=0)
    IfEventValueEqual(1, flag=7700, bit_count=10, value=0)
    EndIfConditionFalse(1)
    DisplayStatus(60000000)


@NeverRestart(11216301)
def Event_11216301():
    """Event 11216301"""
    DisableNetworkSync()
    IfEventValueGreaterThan(-1, flag=7200, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, flag=7450, bit_count=10, value=100)
    IfEventValueGreaterThan(-1, flag=7700, bit_count=10, value=100)
    EndIfConditionFalse(-1)
    DisplayStatus(59999999)


@NeverRestart(11210439)
def Event_11210439():
    """Event 11210439"""
    EndIfClient()
    IfCharacterInsideRegion(-1, PLAYER, region=1212700)
    IfCharacterInsideRegion(-1, PLAYER, region=1212701)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212713)
    IfCharacterInsideRegion(-1, PLAYER, region=1212714)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfCharacterInsideRegion(-1, PLAYER, region=1212793)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfCharacterInsideRegion(-1, PLAYER, region=1212796)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    EndIfConditionFalse(-1)
    SetTeamType(PLAYER, TeamType.Human)


@NeverRestart(11219999)
def Event_11219999():
    """Event 11219999"""
    IfCharacterInsideRegion(1, PLAYER, region=1219999)
    IfFlagDisabled(1, 11219898)
    IfConditionTrue(0, input_condition=1)
    DisableAI(PLAYER)
    EnableFlag(11219898)
    RotateToFaceEntity(PLAYER, target_entity=1212510)
    Wait(10.0)
    EnableAI(PLAYER)
    Restart()


@NeverRestart(11219900)
def Event_11219900():
    """Event 11219900"""
    IfMultiplayer(1)
    IfTrueFlagCountGreaterThanOrEqual(1, FlagType.Absolute, flag_range=(11215360, 11215365), value=2)
    IfFlagDisabled(1, 11215390)
    IfTimeElapsed(1, seconds=60.0)
    IfConditionTrue(0, input_condition=1)


@NeverRestart(11219901)
def Event_11219901():
    """Event 11219901"""
    IfMultiplayer(1)
    IfFlagEnabled(1, 11215360)
    IfFlagDisabled(1, 11215390)
    IfCharacterInsideRegion(-1, PLAYER, region=1212794)
    IfCharacterInsideRegion(-1, PLAYER, region=1212797)
    IfCharacterInsideRegion(-1, PLAYER, region=1212702)
    IfCharacterInsideRegion(-1, PLAYER, region=1212715)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11219902)


@NeverRestart(11219950)
def Event_11219950(_, flag: int):
    """Event 11219950"""
    DisableNetworkSync()
    IfFlagEnabled(1, 11215390)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    EnableAI(PLAYER)


@NeverRestart(7999)
def Event_7999():
    """Event 7999"""
    DisableNetworkSync()
    IfFlagEnabled(1, 905)
    IfFlagEnabled(2, 906)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagEnabled(3, 906)
    DisableFlag(905)
    AddSpecialEffect(PLAYER, 4611)
    Restart()
    DisableFlag(906)
    AddSpecialEffect(PLAYER, 4612)
    Restart()


@NeverRestart(7998)
def Event_7998():
    """Event 7998"""
    IfFlagEnabled(1, 5100)
    IfFlagEnabled(2, 5101)
    IfFlagEnabled(3, 5102)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((5100, 5102))
    SkipLinesIfFinishedConditionFalse(1, condition=1)
    IncrementEventValue(7200, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, condition=2)
    IncrementEventValue(7450, bit_count=10, max_value=1000)
    SkipLinesIfFinishedConditionFalse(1, condition=3)
    IncrementEventValue(7700, bit_count=10, max_value=1000)
    Restart()


@NeverRestart(11219876)
def Event_11219876():
    """Event 11219876"""
    IfCharacterInsideRegion(1, PLAYER, region=1212778)
    IfFlagDisabled(1, 11212778)
    IfConditionTrue(0, input_condition=1)
    Unknown_2003_43(flag=6000, bit_count=10, unk1=0, unk2=0)
    EnableFlag(11212778)
    Restart()
    IfCharacterInsideRegion(2, PLAYER, region=1212778)
    IfFlagEnabled(2, 11212778)
    IfConditionTrue(0, input_condition=2)
    Unknown_2003_43(flag=6000, bit_count=10, unk1=0, unk2=1)
    DisableFlag(11212778)
    Restart()


@NeverRestart(11219877)
def Event_11219877():
    """Event 11219877"""
    IfFlagEnabled(1, 11215390)
    IfFlagEnabled(-1, 11215392)
    IfFlagEnabled(-1, 11215402)
    IfFlagDisabled(2, 11215360)
    IfFlagDisabled(2, 11215361)
    IfFlagDisabled(2, 11215364)
    IfFlagDisabled(3, 11215362)
    IfFlagDisabled(3, 11215363)
    IfFlagDisabled(3, 11215365)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11218145)
    Unknown_2000_6(unk1=2)
    Wait(3.0)
    Unknown_2004_52()
    ArenaExitRequest()
