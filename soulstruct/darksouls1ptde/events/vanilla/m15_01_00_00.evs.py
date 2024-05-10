"""
Anor Londo

linked:


strings:

"""
from soulstruct.darksouls1ptde.events import *
from soulstruct.darksouls1ptde.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    if FlagEnabled(12):
        RegisterBonfire(bonfire_flag=11510920, obj=1511950)
    RegisterBonfire(bonfire_flag=11510992, obj=1511960, initial_kindle_level=10)
    RegisterBonfire(bonfire_flag=11510984, obj=1511961)
    RegisterBonfire(bonfire_flag=11510976, obj=1511962)
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=1511140)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=1511141)
    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(1511994)
    DeleteVFX(1511995, erase_root_only=False)
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
    if FlagEnabled(11510301):
        EnableFlag(11510301)
        DisableFlag(11510302)
        DisableFlag(11510303)
        EndOfAnimation(obj=1511300, animation_id=51)
        EnableMapCollision(collision=1513301)
    DisableObject(1511450)
    DisableFlag(11510460)
    Event_11510090(0, obj=1511700, vfx_id=1511701, destination=1512600, destination_1=1512601)
    Event_11510090(1, obj=1511702, vfx_id=1511703, destination=1512602, destination_1=1512603)
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
    Event_11515060(0, character=1510400)
    Event_11515060(1, character=1510401)
    Event_11515060(2, character=1510402)
    Event_11515060(3, character=1510403)
    Event_11515060(4, character=1510404)
    Event_11515060(5, character=1510405)
    Event_11515060(6, character=1510406)
    Event_11515060(7, character=1510407)
    Event_11515060(8, character=1510408)
    Event_11515060(9, character=1510409)
    Event_11515060(10, character=1510410)
    Event_11515060(11, character=1510411)
    Event_11515060(12, character=1510412)
    Event_11515060(13, character=1510413)
    Event_11515080(0, character=1510450, character_1=1510451)
    Event_11515080(1, character=1510452, character_1=1510453)
    Event_11510260(0, flag=11510251, region=1512251, region_1=1512250)
    Event_11510260(1, flag=11510257, region=1512253, region_1=1512252)
    Event_11510260(2, flag=11510258, region=1512255, region_1=1512254)
    DisableSoundEvent(sound_id=1513800)
    if FlagEnabled(12):
        ForceAnimation(1511401, 0, loop=True)
        ForceAnimation(1511402, 0, loop=True)
        Event_11515392()
        DisableObject(1511990)
        DeleteVFX(1511991, erase_root_only=False)
        DisableObject(1511992)
        DeleteVFX(1511993, erase_root_only=False)
        DisableObject(1511988)
        DeleteVFX(1511989, erase_root_only=False)
    else:
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
    if FlagEnabled(11510900):
        Event_11515382()
        DisableObject(1511890)
        DeleteVFX(1511891, erase_root_only=False)
        DisableObject(1511892)
        DeleteVFX(1511893, erase_root_only=False)
    else:
        Event_11515380()
        Event_11515381()
        Event_11515383()
        Event_11515382()
        Event_11510900()
        Event_11515384()
        Event_11515385()
        Event_11515386()
        Event_11510450()
    Event_11510710(0, obj_act_id=11510251, character=1510300, region=1512251, region_1=1512250)
    Event_11510710(1, obj_act_id=11510251, character=1510301, region=1512251, region_1=1512250)
    Event_11510710(2, obj_act_id=11510251, character=1510302, region=1512251, region_1=1512250)
    Event_11510710(3, obj_act_id=11510251, character=1510305, region=1512251, region_1=1512250)
    Event_11510710(4, obj_act_id=11510251, character=1510320, region=1512251, region_1=1512250)
    Event_11510710(5, obj_act_id=11510251, character=1510321, region=1512251, region_1=1512250)
    Event_11510710(6, obj_act_id=11510251, character=1510322, region=1512251, region_1=1512250)
    Event_11510710(7, obj_act_id=11510251, character=1510323, region=1512251, region_1=1512250)
    Event_11510710(8, obj_act_id=11510251, character=1510324, region=1512251, region_1=1512250)
    Event_11510710(9, obj_act_id=11510251, character=1510325, region=1512251, region_1=1512250)
    Event_11510710(10, obj_act_id=11510251, character=1510326, region=1512251, region_1=1512250)
    Event_11510710(11, obj_act_id=11510251, character=1510327, region=1512251, region_1=1512250)
    Event_11510710(12, obj_act_id=11510251, character=1510328, region=1512251, region_1=1512250)
    Event_11510710(13, obj_act_id=11510251, character=1510329, region=1512251, region_1=1512250)
    Event_11510710(20, obj_act_id=11510257, character=1510300, region=1512253, region_1=1512252)
    Event_11510710(21, obj_act_id=11510257, character=1510301, region=1512253, region_1=1512252)
    Event_11510710(22, obj_act_id=11510257, character=1510302, region=1512253, region_1=1512252)
    Event_11510710(23, obj_act_id=11510257, character=1510305, region=1512253, region_1=1512252)
    Event_11510710(24, obj_act_id=11510257, character=1510320, region=1512253, region_1=1512252)
    Event_11510710(25, obj_act_id=11510257, character=1510321, region=1512253, region_1=1512252)
    Event_11510710(26, obj_act_id=11510257, character=1510322, region=1512253, region_1=1512252)
    Event_11510710(27, obj_act_id=11510257, character=1510323, region=1512253, region_1=1512252)
    Event_11510710(28, obj_act_id=11510257, character=1510324, region=1512253, region_1=1512252)
    Event_11510710(29, obj_act_id=11510257, character=1510325, region=1512253, region_1=1512252)
    Event_11510710(30, obj_act_id=11510257, character=1510326, region=1512253, region_1=1512252)
    Event_11510710(31, obj_act_id=11510257, character=1510327, region=1512253, region_1=1512252)
    Event_11510710(32, obj_act_id=11510257, character=1510328, region=1512253, region_1=1512252)
    Event_11510710(33, obj_act_id=11510257, character=1510329, region=1512253, region_1=1512252)
    Event_11510710(40, obj_act_id=11510258, character=1510300, region=1512255, region_1=1512254)
    Event_11510710(41, obj_act_id=11510258, character=1510301, region=1512255, region_1=1512254)
    Event_11510710(42, obj_act_id=11510258, character=1510302, region=1512255, region_1=1512254)
    Event_11510710(43, obj_act_id=11510258, character=1510305, region=1512255, region_1=1512254)
    Event_11510710(44, obj_act_id=11510258, character=1510320, region=1512255, region_1=1512254)
    Event_11510710(45, obj_act_id=11510258, character=1510321, region=1512255, region_1=1512254)
    Event_11510710(46, obj_act_id=11510258, character=1510322, region=1512255, region_1=1512254)
    Event_11510710(47, obj_act_id=11510258, character=1510323, region=1512255, region_1=1512254)
    Event_11510710(48, obj_act_id=11510258, character=1510324, region=1512255, region_1=1512254)
    Event_11510710(49, obj_act_id=11510258, character=1510325, region=1512255, region_1=1512254)
    Event_11510710(50, obj_act_id=11510258, character=1510326, region=1512255, region_1=1512254)
    Event_11510710(51, obj_act_id=11510258, character=1510327, region=1512255, region_1=1512254)
    Event_11510710(52, obj_act_id=11510258, character=1510328, region=1512255, region_1=1512254)
    Event_11510710(53, obj_act_id=11510258, character=1510329, region=1512255, region_1=1512254)
    Event_11515200(0, character=1510200)
    Event_11515210(0, character=1510200)
    Event_11515220(0, character=1510200)
    Event_11515230(0, character=1510200)
    Event_11515240(0, character=1510200, region=1512010)
    Event_11510850(0, character=1510200)
    Event_11515190(0, character=1510200)
    Event_11515200(1, character=1510201)
    Event_11515210(1, character=1510201)
    Event_11515220(1, character=1510201)
    Event_11515230(1, character=1510201)
    Event_11515240(1, character=1510201, region=1512011)
    Event_11510850(1, character=1510201)
    Event_11515190(1, character=1510201)
    Event_11515200(2, character=1510202)
    Event_11515210(2, character=1510202)
    Event_11515220(2, character=1510202)
    Event_11515230(2, character=1510202)
    Event_11515240(2, character=1510202, region=1512012)
    Event_11510850(2, character=1510202)
    Event_11515190(2, character=1510202)
    Event_11515200(3, character=1510203)
    Event_11515210(3, character=1510203)
    Event_11515220(3, character=1510203)
    Event_11515230(3, character=1510203)
    Event_11515240(3, character=1510203, region=1512013)
    Event_11510850(3, character=1510203)
    Event_11515190(3, character=1510203)
    Event_11510600(1, obj=1511651, obj_act_id=11510601)
    Event_11510600(2, obj=1511652, obj_act_id=11510602)
    Event_11510600(3, obj=1511653, obj_act_id=11510603)
    Event_11510600(4, obj=1511654, obj_act_id=11510604)
    Event_11510600(6, obj=1511656, obj_act_id=11510606)
    Event_11510600(7, obj=1511657, obj_act_id=11510607)
    Event_11510600(8, obj=1511658, obj_act_id=11510608)
    Event_11510600(9, obj=1511659, obj_act_id=11510609)
    Event_11510600(10, obj=1511660, obj_act_id=11510610)
    Event_11510600(11, obj=1511661, obj_act_id=11510611)
    Event_11510600(12, obj=1511662, obj_act_id=11510612)
    Event_11510600(15, obj=1511665, obj_act_id=11510615)
    Event_11510600(16, obj=1511666, obj_act_id=11510616)
    Event_11510600(17, obj=1511667, obj_act_id=11510617)
    Event_11510600(18, obj=1511668, obj_act_id=11510618)
    Event_11510600(19, obj=1511669, obj_act_id=11510619)
    Event_11510860(0, character=1510250, item_lot=0)
    Event_11510860(1, character=1510450, item_lot=53500000)
    Event_11510860(2, character=1510452, item_lot=53500000)
    Event_11510860(3, character=6640, item_lot=0)
    Event_11510860(4, character=6650, item_lot=0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6640, event_flag=8258)
    HumanityRegistration(6650, event_flag=8266)
    HumanityRegistration(6543, event_flag=8310)
    Event_11515030()
    Event_11515032()
    Event_11515033()
    HumanityRegistration(6003, event_flag=8310)
    SkipLinesIfFlagEnabled(2, 1008)
    SkipLinesIfFlagEnabled(1, 1004)
    DisableCharacter(6003)
    Event_11510510(0, character=6003, flag=1004)
    Event_11510520(0, character=6003, first_flag=1000, last_flag=1029, flag=1005)
    Event_11510530(0, character=6003, first_flag=1000, last_flag=1029, flag=1008)
    HumanityRegistration(6010, event_flag=8318)
    Event_11510501(0, character=6010, flag=1033)
    Event_11510520(1, character=6010, first_flag=1030, last_flag=1036, flag=1034)
    Event_11510531(0, character=6010, first_flag=1030, last_flag=1036, flag=1036)
    Event_11510532(0, character=6010, first_flag=1030, last_flag=1036, flag=1031)
    Event_11510533(0, character=6010)
    DisableCharacter(1510600)
    Event_11510520(2, character=1510600, first_flag=1230, last_flag=1239, flag=1232)
    SetTeamType(1510650, TeamType.Ally)
    SkipLinesIfFlagRangeAnyEnabled(1, (1240, 1249))
    EnableFlag(1240)
    Event_11510520(3, character=1510650, first_flag=1240, last_flag=1249, flag=1242)
    Event_11510502(0, character=1510650, flag=1241)
    Event_11515090(0, character=6210)
    Event_11515091(0, character=6210)
    Event_11515092(0, character=6210, obj=1511110, flag=1361, flag_1=1362)
    Event_11510510(4, character=6210, flag=1361)
    Event_11510520(4, character=6210, first_flag=1360, last_flag=1363, flag=1362)
    HumanityRegistration(6283, event_flag=8446)
    SkipLinesIfFlagEnabled(3, 1512)
    SkipLinesIfFlagEnabled(2, 1494)
    SkipLinesIfFlagEnabled(1, 1493)
    DisableCharacter(6283)
    Event_11510510(5, character=6283, flag=1512)
    Event_11510520(5, character=6283, first_flag=1490, last_flag=1514, flag=1513)
    Event_11510535(0, character=6283, first_flag=1490, last_flag=1514, flag=1494)
    Event_11510536(0, character=6283)
    HumanityRegistration(6302, event_flag=8462)
    HumanityRegistration(6490, event_flag=8908)
    HumanityRegistration(6500, event_flag=8916)
    DisableCharacter(6302)
    DisableCharacter(6490)
    DisableCharacter(6500)
    Event_11510541(0, character=6302, first_flag=1570, last_flag=1599, flag=1578)
    Event_11510542(0, character=6302, first_flag=1570, last_flag=1599, flag=1575)
    Event_11510543(0, character=6302, first_flag=1570, last_flag=1599, flag=1572)
    Event_11510544(0, character=6302, first_flag=1570, last_flag=1599, flag=1575)


@ContinueOnRest(11510090)
def Event_11510090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11510090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        dummy_id=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11515040)
def Event_11515040():
    """Event 11515040"""
    if ThisEventFlagEnabled():
        return
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
    
    MAIN.Await(FlagEnabled(11510050))
    
    if FlagEnabled(735):
        return
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
    OR_1.Add(FlagEnabled(11515045))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
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
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=ANOR_LONDO))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11510050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=ANOR_LONDO))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11510050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=ANOR_LONDO))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11510050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=ANOR_LONDO))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11510050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=ANOR_LONDO))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11510050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=ANOR_LONDO))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11510050))
    if not OR_6:
        return RESTART
    EnableFlag(11510050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=ANOR_LONDO))
    if not AND_7:
        return RESTART
    DisableFlag(11510050)
    EnableFlag(11515045)


@ContinueOnRest(11515380)
def Event_11515380():
    """Event 11515380"""
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1511890,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(743)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


@ContinueOnRest(11515381)
def Event_11515381():
    """Event 11515381"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(11515383))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    if FlagDisabled(11510400):
        PlayCutscene(
            150151,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1512901,
            game_map=ANOR_LONDO,
        )
    else:
        PlayCutscene(
            150156,
            cutscene_flags=CutsceneFlags.Unskippable,
            player_id=10000,
            move_to_region=1512901,
            game_map=ANOR_LONDO,
        )
    WaitFrames(frames=1)
    EnableCharacter(1510650)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11515383)
def Event_11515383():
    """Event 11515383"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11510900))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1512896))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1510650, authority_level=UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1510650)


@RestartOnRest(11515382)
def Event_11515382():
    """Event 11515382"""
    if FlagEnabled(11510900):
        DisableCharacter(1510650)
        End()
    DisableAI(1510650)
    AND_1.Add(FlagEnabled(11515383))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512896))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11515386)
    
    MAIN.Await(FlagEnabled(11515387))
    
    SkipLinesIfClient(2)
    ForceAnimation(PLAYER, -1)
    ResetAnimation(PLAYER, disable_interpolation=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(PlayerCovenant(Covenant.DarkmoonBlade))
    SkipLinesIfConditionFalse(6, AND_2)
    BetrayCurrentCovenant()
    if FlagDisabled(9002):
        IncrementPvPSin()
        EnableFlag(9002)
    EnableFlag(742)
    SaveRequest()
    EnableAI(1510650)
    SetTeamType(1510650, TeamType.Boss)
    EnableBossHealthBar(1510650, name=5320)


@ContinueOnRest(11510900)
def Event_11510900():
    """Event 11510900"""
    MAIN.Await(HealthRatio(1510650) <= 0.0)
    
    WaitFrames(frames=1)
    SkipLinesIfClient(7)
    EnableFlag(11515389)
    
    MAIN.Await(FlagEnabled(11515389))
    
    if FlagDisabled(11510400):
        PlayCutscene(150152, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    else:
        PlayCutscene(150157, cutscene_flags=0, player_id=10000, move_to_region=1512897, game_map=ANOR_LONDO)
    WaitFrames(frames=1)
    if FlagEnabled(12):
        EnableFlag(120)
    EnableFlag(11510900)
    KillBoss(game_area_param_id=1510650)
    DisableObject(1511890)
    DeleteVFX(1511891)
    if Client():
        return
    DisableFlag(11807170)
    DisableFlag(11807180)
    DisableFlag(11807190)
    DisableFlag(11807230)
    AwardAchievement(achievement_id=39)


@ContinueOnRest(11515384)
def Event_11515384():
    """Event 11515384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(11515382))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1513802)


@ContinueOnRest(11515385)
def Event_11515385():
    """Event 11515385"""
    DisableNetworkSync()
    AND_1.Add(HealthRatio(1510650) <= 0.0)
    AND_1.Add(FlagEnabled(11515384))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1513802)


@RestartOnRest(11515386)
def Event_11515386():
    """Event 11515386"""
    AND_1.Add(ThisEventFlagEnabled())
    AND_1.Add(FlagEnabled(11510400))
    AND_2.Add(ThisEventFlagEnabled())
    AND_2.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.DarkmoonBlade))
    AND_3.Add(ThisEventFlagEnabled())
    AND_3.Add(not AND_1)
    AND_3.Add(not AND_2)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(10, input_condition=AND_1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150155, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150155,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150155, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfLastConditionResultFalse(10, input_condition=AND_2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150161, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150161,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150161, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150160, cutscene_flags=0, player_id=10000, move_to_region=1512900, game_map=ANOR_LONDO)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        150160,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1512900,
        game_map=ANOR_LONDO,
    )
    SkipLines(1)
    PlayCutscene(150160, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableFlag(11515387)
    End()


@ContinueOnRest(11515390)
def Event_11515390():
    """Event 11515390"""
    AND_1.Add(FlagDisabled(12))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1511990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11515391)
def Event_11515391():
    """Event 11515391"""
    AND_1.Add(FlagDisabled(12))
    AND_1.Add(FlagEnabled(11515393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1512998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1512997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11515393)
def Event_11515393():
    """Event 11515393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(12))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1512996))
    
        MAIN.Await(AND_1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1510800)
    ActivateMultiplayerBuffs(1510801)
    ActivateMultiplayerBuffs(1510810)
    ActivateMultiplayerBuffs(1510811)


@RestartOnRest(11515392)
def Event_11515392():
    """Event 11515392"""
    if FlagEnabled(12):
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
    if FlagDisabled(11510000):
        DisableCharacter(1510800)
    DisableAI(1510800)
    DisableAI(1510810)
    AND_1.Add(FlagEnabled(11515393))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512990))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(8, 11510000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150140, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150140, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    EnableCharacter(1510800)
    EnableCharacter(1510810)
    EnableFlag(11510000)
    EnableAI(1510800)
    EnableAI(1510810)
    EnableBossHealthBar(1510800, name=5270, bar_slot=1)
    EnableBossHealthBar(1510810, name=2360)


@ContinueOnRest(11510001)
def Event_11510001():
    """Event 11510001"""
    DisableObject(1511950)
    AND_1.Add(CharacterDead(1510800))
    AND_2.Add(CharacterDead(1510810))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(10, input_condition=AND_1)
    
    MAIN.Await(CharacterDead(1510801))
    
    EnableFlag(11510902)
    PlaySoundEffect(1510801, 777777777, sound_type=SoundType.s_SFX)
    Kill(1510811)
    KillBoss(game_area_param_id=1510801)
    DisableFlag(11807100)
    DisableFlag(11807110)
    DisableFlag(11807120)
    DisableFlag(11807130)
    SkipLines(9)
    
    MAIN.Await(CharacterDead(1510811))
    
    EnableFlag(11510903)
    PlaySoundEffect(1510811, 777777777, sound_type=SoundType.s_SFX)
    Kill(1510801)
    KillBoss(game_area_param_id=1510811)
    DisableFlag(11807060)
    DisableFlag(11807070)
    DisableFlag(11807080)
    DisableFlag(11807090)
    EnableFlag(12)
    EnableFlag(120)
    DisableObject(1511990)
    DeleteVFX(1511991)
    DisableObject(1511992)
    DeleteVFX(1511993)
    DisableObject(1511988)
    DeleteVFX(1511989)
    EnableObject(1511950)
    RegisterBonfire(bonfire_flag=11510920, obj=1511950)
    DisableNetworkSync()
    Wait(3.0)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)


@ContinueOnRest(11515394)
def Event_11515394():
    """Event 11515394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(12))
    AND_1.Add(FlagEnabled(11515392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11515391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1513800)
    EnableBackread(1510801)


@ContinueOnRest(11515395)
def Event_11515395():
    """Event 11515395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12))
    AND_1.Add(FlagEnabled(11515394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1513800)


@ContinueOnRest(11515396)
def Event_11515396():
    """Event 11515396"""
    AND_1.Add(CharacterDead(1510800))
    AND_2.Add(CharacterDead(1510810))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(12, input_condition=AND_2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150121, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150121, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1510800)
    DisableCharacter(1510810)
    DisableImmortality(1510810)
    Kill(1510810)
    EnableCharacter(1510811)
    EnableBossHealthBar(1510811, name=2360)
    End()
    SkipLinesIfMultiplayer(2)
    PlayCutscene(150120, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(150120, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableCharacter(1510810)
    DisableCharacter(1510800)
    DisableImmortality(1510800)
    Kill(1510800)
    EnableCharacter(1510801)
    EnableBossHealthBar(1510801, name=5270, bar_slot=1)


@ContinueOnRest(11515397)
def Event_11515397():
    """Event 11515397"""
    AND_1.Add(HealthRatio(1510800) <= 0.0)
    AND_2.Add(HealthRatio(1510810) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    EnableImmortality(1510810)
    End()
    EnableImmortality(1510800)


@RestartOnRest(11515398)
def Event_11515398():
    """Event 11515398"""
    AND_1.Add(CharacterDead(1510810))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(1510810))
    
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
    
    MAIN.Await(HealthRatio(1510810) <= 0.0)
    
    SetNPCPartHealth(1510810, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515399)
def Event_11515399():
    """Event 11515399"""
    AND_1.Add(CharacterDead(1510811))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(1510811))
    
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
    
    MAIN.Await(HealthRatio(1510811) <= 0.0)
    
    SetNPCPartHealth(1510811, npc_part_id=2360, desired_health=0, overwrite_max=False)


@RestartOnRest(11515060)
def Event_11515060(_, character: int):
    """Event 11515060"""
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(
        character,
        npc_part_id=2870,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartBulletDamageScaling(character, npc_part_id=2870, desired_scaling=0.0)
    SetNPCPartEffects(character, npc_part_id=2870, material_sfx_id=50, material_vfx_id=50)
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    SetNPCPartHealth(character, npc_part_id=2870, desired_health=0, overwrite_max=False)


@RestartOnRest(11515080)
def Event_11515080(_, character: int, character_1: int):
    """Event 11515080"""
    DisableCharacter(character_1)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
        SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
        AddSpecialEffect(character, 5434)
        AICommand(character, command_id=20, command_slot=0)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    CreateNPCPart(character, npc_part_id=5351, part_index=NPCPartType.Part1, part_health=65)
    AND_1.Add(CharacterPartHealth(character, npc_part_id=5351) <= 0)
    AND_2.Add(HealthRatio(character) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    ResetAnimation(character)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=110,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    ForceAnimation(character, 8000)
    ForceAnimation(character_1, 8100)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, 5434)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)
    if ValueNotEqual(left=character, right=1510450):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(53530000, host_only=True)


@ContinueOnRest(11510100)
def Event_11510100():
    """Event 11510100"""
    if ThisEventFlagEnabled():
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
    CreateObjectVFX(1511600, vfx_id=90, dummy_id=99010)
    ForceAnimation(1511600, 110, loop=True)
    
    MAIN.Await(ObjectDestroyed(1511100))
    
    ForceAnimation(1511600, 111)
    ForceAnimation(1511101, 0)
    ForceAnimation(1511102, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(1511600)
    EnableTreasure(obj=1511600)
    DestroyObject(1511102)


@ContinueOnRest(11510110)
def Event_11510110():
    """Event 11510110"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1511010, animation_id=0)
        End()
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1511010,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1511010, destination_type=CoordEntityType.Object, dummy_id=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1511010, 0)


@ContinueOnRest(11510200)
def Event_11510200():
    """Event 11510200"""
    if ThisEventFlagEnabled():
        DisableObjectActivation(1511001, obj_act_id=-1)
        EndOfAnimation(obj=1511000, animation_id=0)
        EndOfAnimation(obj=1511001, animation_id=0)
        End()
    AND_1.Add(FlagDisabled(11510700))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1511001,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=1511001, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511001, 0, wait_for_completion=True)
    ForceAnimation(1511000, 0)


@ContinueOnRest(11510201)
def Event_11510201():
    """Event 11510201"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510200))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1512000,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1511000,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010160)
    Restart()


@ContinueOnRest(11510210)
def Event_11510210():
    """Event 11510210"""
    if ThisEventFlagEnabled():
        EndOfAnimation(obj=1511200, animation_id=0)
        End()
    EnableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Disable)
    
    MAIN.Await(ActionButton(
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=101,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    Move(PLAYER, destination=1511200, destination_type=CoordEntityType.Object, dummy_id=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1511200, 0)
    DisableNavmeshType(navmesh_id=1513200, navmesh_type=NavmeshType.Disable)


@ContinueOnRest(11510211)
def Event_11510211():
    """Event 11510211"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11510210))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=1511200,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=100,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010161, anchor_entity=1511200)
    Restart()


@ContinueOnRest(11510220)
def Event_11510220():
    """Event 11510220"""
    if ThisEventFlagDisabled():
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1512350))
    ForceAnimation(1511050, 0)


@ContinueOnRest(11510260)
def Event_11510260(_, flag: int, region: int, region_1: int):
    """Event 11510260"""
    DisableNetworkSync()
    if FlagDisabled(flag):
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
        AddSpecialEffect(PLAYER, 4150)
        Wait(3.0)
        Restart()
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(11510710)
def Event_11510710(_, obj_act_id: int, character: int, region: int, region_1: int):
    """Event 11510710"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
        EnableFlag(obj_act_id)
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterInsideRegion(character, region=region_1))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(11510300)
def Event_11510300():
    """Event 11510300"""
    AND_1.Add(FlagDisabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagDisabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_3.Add(FlagEnabled(11510305))
    AND_3.Add(FlagDisabled(11510303))
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_4.Add(FlagEnabled(11510305))
    AND_4.Add(FlagEnabled(11510303))
    AND_4.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_5.Add(FlagEnabled(11510305))
    AND_5.Add(FlagDisabled(11510301))
    AND_5.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_6.Add(FlagEnabled(11510305))
    AND_6.Add(FlagDisabled(11510302))
    AND_6.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11515300)
    SkipLinesIfFlagEnabled(20, 11510305)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
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
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        rotation=-90,
        relative_rotation_axis_x=337.5,
        relative_rotation_axis_z=255.0,
        vertical_translation=-12.0,
    )
    SkipLines(1)
    PlayCutscene(150100, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
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
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        0,
        animation_id=0,
        collision=1513303,
        collision_1=1513302,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_4)
    Move(PLAYER, destination=1511302, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511302, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        1,
        animation_id=0,
        collision=1513303,
        collision_1=1513302,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        0,
        animation_id=0,
        animation_id_1=1,
        collision=1513301,
        flag=11510303,
        flag_1=11510301,
        animation_id_2=11,
        frames=180,
        frames_1=360,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        2,
        animation_id=0,
        collision=1513303,
        collision_1=1513302,
        flag=11510303,
        flag_1=11510302,
        frames=180,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(32, 11510302)
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, dummy_id=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        3,
        animation_id=1,
        collision=1513302,
        collision_1=1513301,
        flag=11510302,
        flag_1=11510301,
        frames=360,
    )
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, dummy_id=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        4,
        animation_id=3,
        collision=1513302,
        collision_1=1513303,
        flag=11510302,
        flag_1=11510303,
        frames=180,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 13)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        5,
        animation_id=3,
        collision=1513302,
        collision_1=1513303,
        flag=11510302,
        flag_1=11510303,
        frames=180,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 11)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        6,
        animation_id=1,
        collision=1513302,
        collision_1=1513301,
        flag=11510302,
        flag_1=11510301,
        frames=360,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    SkipLinesIfFlagDisabled(25, 11510301)
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, dummy_id=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        7,
        animation_id=2,
        collision=1513301,
        collision_1=1513302,
        flag=11510301,
        flag_1=11510302,
        frames=360,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515330(
        1,
        animation_id=2,
        animation_id_1=3,
        collision=1513303,
        flag=11510301,
        flag_1=11510303,
        animation_id_2=13,
        frames=360,
        frames_1=180,
    )
    SkipLinesIfLastConditionResultFalse(7, input_condition=AND_6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, dummy_id=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(frames=130)
    
    MAIN.Await(FramesElapsed(frames=0))
    
    Event_11515320(
        8,
        animation_id=2,
        collision=1513301,
        collision_1=1513302,
        flag=11510301,
        flag_1=11510302,
        frames=360,
    )
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()
    DisplayDialog(text=10010170)
    Restart()


@ContinueOnRest(11510319)
def Event_11510319():
    """Event 11510319"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1512310))
    
    EnableFlag(11510304)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=1512310))
    
    DisableFlag(11510304)
    Restart()


@ContinueOnRest(11515320)
def Event_11515320(_, animation_id: int, collision: int, collision_1: int, flag: int, flag_1: int, frames: int):
    """Event 11515320"""
    DisableMapCollision(collision=collision)
    EnableObject(1511310)
    ForceAnimation(1511300, animation_id)
    ForceAnimation(1511310, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(1511310)
    EnableMapCollision(collision=collision_1)
    DisableFlag(flag)
    EnableFlag(flag_1)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@ContinueOnRest(11515330)
def Event_11515330(
    _,
    animation_id: int,
    animation_id_1: int,
    collision: int,
    flag: int,
    flag_1: int,
    animation_id_2: int,
    frames: int,
    frames_1: int,
):
    """Event 11515330"""
    DisableMapCollision(collision=1513301)
    DisableMapCollision(collision=1513302)
    DisableMapCollision(collision=1513303)
    EnableObject(1511310)
    ForceAnimation(1511300, animation_id)
    ForceAnimation(1511310, animation_id)
    WaitFrames(frames=frames)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(1511300, animation_id_2)
    WaitFrames(frames=130)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    ForceAnimation(1511300, animation_id_1)
    ForceAnimation(1511310, animation_id_1)
    WaitFrames(frames=frames_1)
    
    MAIN.Await(TimeElapsed(seconds=0.0))
    
    DisableObject(1511310)
    EnableMapCollision(collision=collision)
    DisableFlag(flag)
    EnableFlag(flag_1)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


@ContinueOnRest(11510340)
def Event_11510340():
    """Event 11510340"""
    if FlagEnabled(11515300):
        EnableMapCollision(collision=1513310)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Disable)
    
        MAIN.Await(FlagDisabled(11515300))
    
        Restart()
    if FlagEnabled(11510303):
        EnableMapCollision(collision=1513310)
        DisableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Disable)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510302):
        DisableMapCollision(collision=1513310)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Disable)
        DisableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Disable)
        DisableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Disable)
        DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Disable)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    if FlagEnabled(11510301):
        EnableMapCollision(collision=1513310)
        EnableNavmeshType(navmesh_id=1513350, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513351, navmesh_type=NavmeshType.Disable)
        EnableNavmeshType(navmesh_id=1513352, navmesh_type=NavmeshType.Disable)
        DisableNavmeshType(navmesh_id=1513353, navmesh_type=NavmeshType.Disable)
        DisableNavmeshType(navmesh_id=1513354, navmesh_type=NavmeshType.Disable)
    
        MAIN.Await(FlagEnabled(11515300))
    
        Restart()
    DisplayDialog(text=10010105)
    Restart()


@ContinueOnRest(11510350)
def Event_11510350():
    """Event 11510350"""
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(11515301))
    AND_1.Add(FlagEnabled(11510301))
    AND_2.Add(Host())
    AND_2.Add(FlagEnabled(11515301))
    AND_2.Add(FlagEnabled(11510302))
    AND_3.Add(Host())
    AND_3.Add(FlagEnabled(11515301))
    AND_3.Add(FlagEnabled(11510303))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11515301)
    if Singleplayer():
        return RESTART
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(obj=1511300, animation_id=51)
    EnableMapCollision(collision=1513301)
    Restart()
    SkipLinesIfLastConditionResultFalse(6, input_condition=AND_2)
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


@ContinueOnRest(11510310)
def Event_11510310():
    """Event 11510310"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11510301))
    AND_1.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=102,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_2.Add(FlagEnabled(11510303))
    AND_2.Add(ActionButton(
        prompt_text=10010502,
        anchor_entity=1511300,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=104,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_2.Add(FlagDisabled(11510305))
    OR_2.Add(FlagEnabled(11510303))
    AND_3.Add(OR_2)
    AND_3.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511301,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_3.Add(FlagDisabled(11510305))
    OR_3.Add(FlagDisabled(11510303))
    AND_4.Add(OR_3)
    AND_4.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511302,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_4.Add(FlagDisabled(11510305))
    OR_4.Add(FlagEnabled(11510301))
    AND_5.Add(OR_4)
    AND_5.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511303,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    OR_5.Add(FlagDisabled(11510305))
    OR_5.Add(FlagEnabled(11510302))
    AND_6.Add(OR_5)
    AND_6.Add(ActionButton(
        prompt_text=10010501,
        anchor_entity=1511304,
        anchor_type=CoordEntityType.Object,
        facing_angle=60.0,
        max_distance=1.5,
        dummy_id=192,
        trigger_attribute=TriggerAttribute.All,
    ))
    AND_7.Add(FlagEnabled(11515300))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_7)
    DisplayDialog(text=10010170)
    Restart()
    
    MAIN.Await(FlagDisabled(11515300))
    
    Restart()


@ContinueOnRest(11510400)
def Event_11510400():
    """Event 11510400"""
    DisableMapPiece(map_piece_id=1513401)
    if ThisEventFlagEnabled():
        DisableSoundEvent(sound_id=1513801)
        SetMapDrawParamSlot(map_area_id=15, draw_param_slot=1)
        SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
        DisableMapPiece(map_piece_id=1513400)
        EnableMapPiece(map_piece_id=1513401)
        DisableObject(1511400)
        End()
    EnableCharacter(1510600)
    AND_1.Add(CharacterDead(1510600))
    AND_1.Add(EntityWithinDistance(entity=1510600, other_entity=PLAYER, radius=15.0))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    DisableSoundEvent(sound_id=1513801)
    EnableFlag(743)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerCovenant(Covenant.PrincessGuard))
    SkipLinesIfConditionFalse(4, AND_1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()
    DisableFlag(120)
    if FlagDisabled(11510900):
        PlayCutscene(150110, cutscene_flags=0, player_id=10000)
    else:
        PlayCutscene(150111, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    SetMapDrawParamSlot(map_area_id=15, draw_param_slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(map_piece_id=1513400)
    EnableMapPiece(map_piece_id=1513401)
    DisableObject(1511400)
    AND_2.Add(PlayerHasGood(2510))
    if AND_2:
        return
    AwardItemLot(1090, host_only=True)


@ContinueOnRest(11510401)
def Event_11510401():
    """Event 11510401"""
    if ThisEventFlagEnabled():
        DisableObject(1511400)
        End()
    EnableObjectInvulnerability(1511400)
    AND_1.Add(FlagEnabled(11510400))
    AND_1.Add(EntityWithinDistance(entity=1511400, other_entity=PLAYER, radius=15.0))
    AND_2.Add(Host())
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 2310))
    AND_2.Add(EntityWithinDistance(entity=1511400, other_entity=PLAYER, radius=15.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableObjectInvulnerability(1511400)
    DestroyObject(1511400)
    ForceAnimation(1511400, 0)
    PlaySoundEffect(1511400, 590000000, sound_type=SoundType.o_Object)


@RestartOnRest(11510450)
def Event_11510450():
    """Event 11510450"""
    MAIN.Await(CharacterDoesNotHaveTAEEvent(1510650, tae_event_id=600))
    
    MAIN.Await(CharacterHasTAEEvent(1510650, tae_event_id=600))
    
    DisableCharacter(1510650)
    Wait(1.0)
    if FlagDisabled(11515110):
        Event_11515110(0, destination=1512710, flag=11515110)
        Restart()
    if FlagDisabled(11515111):
        Event_11515110(1, destination=1512711, flag=11515111)
        Restart()
    if FlagDisabled(11515112):
        Event_11515110(2, destination=1512712, flag=11515112)
        Restart()
    if FlagDisabled(11515113):
        Event_11515110(3, destination=1512713, flag=11515113)
        Restart()
    if FlagDisabled(11515114):
        Event_11515110(4, destination=1512714, flag=11515114)
        Restart()
    if FlagDisabled(11515115):
        Event_11515110(5, destination=1512715, flag=11515115)
        Restart()
    if FlagDisabled(11515116):
        Event_11515110(6, destination=1512716, flag=11515116)
        Restart()
    if FlagDisabled(11515117):
        Event_11515110(7, destination=1512717, flag=11515117)
        Restart()
    if FlagDisabled(11515118):
        Event_11515110(8, destination=1512718, flag=11515118)
        Restart()
    if FlagDisabled(11515119):
        Event_11515110(9, destination=1512719, flag=11515119)
        Restart()
    if FlagDisabled(11515120):
        Event_11515110(10, destination=1512720, flag=11515120)
        Restart()
    if FlagDisabled(11515121):
        Event_11515110(11, destination=1512721, flag=11515121)
        Restart()
    if FlagDisabled(11515122):
        Event_11515110(12, destination=1512722, flag=11515122)
        Restart()
    if FlagDisabled(11515123):
        Event_11515110(13, destination=1512723, flag=11515123)
        Restart()
    if FlagDisabled(11515124):
        Event_11515110(14, destination=1512724, flag=11515124)
        Restart()
    if FlagDisabled(11515125):
        Event_11515110(15, destination=1512725, flag=11515125)
        Restart()
    if FlagDisabled(11515126):
        Event_11515110(16, destination=1512726, flag=11515126)
        Restart()
    if FlagDisabled(11515127):
        Event_11515110(17, destination=1512727, flag=11515127)
        Restart()
    if FlagDisabled(11515128):
        Event_11515110(18, destination=1512728, flag=11515128)
        Restart()
    if FlagDisabled(11515129):
        Event_11515110(19, destination=1512729, flag=11515129)
        Restart()
    if FlagDisabled(11515130):
        Event_11515110(20, destination=1512730, flag=11515130)
        Restart()
    if FlagDisabled(11515131):
        Event_11515110(21, destination=1512731, flag=11515131)
        Restart()
    if FlagDisabled(11515132):
        Event_11515110(22, destination=1512732, flag=11515132)
        Restart()
    if FlagDisabled(11515133):
        Event_11515110(23, destination=1512733, flag=11515133)
        Restart()
    if FlagDisabled(11515134):
        Event_11515110(24, destination=1512734, flag=11515134)
        Restart()
    if FlagDisabled(11515135):
        Event_11515110(25, destination=1512735, flag=11515135)
        Restart()
    if FlagDisabled(11515136):
        Event_11515110(26, destination=1512736, flag=11515136)
        Restart()
    if FlagDisabled(11515137):
        Event_11515110(27, destination=1512737, flag=11515137)
        Restart()
    if FlagDisabled(11515138):
        Event_11515110(28, destination=1512738, flag=11515138)
        Restart()
    if FlagDisabled(11515139):
        Event_11515110(29, destination=1512739, flag=11515139)
        Restart()


@EndOnRest(11515110)
def Event_11515110(_, destination: int, flag: int):
    """Event 11515110"""
    Move(1510650, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1510650)
    ReplanAI(1510650)
    ForceAnimation(1510650, 7000, wait_for_completion=True)
    EnableFlag(flag)
    if FlagEnabled(11515132):
        AICommand(1510650, command_id=1, command_slot=0)
        ReplanAI(1510650)


@ContinueOnRest(11510230)
def Event_11510230():
    """Event 11510230"""
    MAIN.Await(ActionButton(
        prompt_text=10010100,
        anchor_entity=1512510,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    AND_1.Add(Singleplayer())
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(384))
    SkipLinesIfConditionTrue(3, AND_1)
    SkipLinesIfClient(1)
    DisplayDialog(text=10010170)
    Restart()
    PlayCutscene(150135, cutscene_flags=0, player_id=10000, move_to_region=1102510, game_map=PAINTED_WORLD)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=1102511)
    SaveRequest()
    Restart()


@ContinueOnRest(11510240)
def Event_11510240():
    """Event 11510240"""
    if Client():
        return
    
    MAIN.Await(InsideMap(game_map=ANOR_LONDO))
    
    MAIN.Await(TimeElapsed(seconds=5.0))
    
    AND_2.Add(FlagDisabled(11515050))
    AND_2.Add(ActionButton(
        prompt_text=10010200,
        anchor_entity=1510100,
        anchor_type=CoordEntityType.Character,
        max_distance=7.0,
        dummy_id=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_2)
    
    SkipLinesIfSingleplayer(2)
    DisplayDialog(text=10010170)
    Restart()
    if FlagDisabled(11510400):
        PlayCutscene(150130, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    else:
        PlayCutscene(150132, cutscene_flags=0, player_id=10000, move_to_region=1502500, game_map=SENS_FORTRESS)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(11515050)
def Event_11515050():
    """Event 11515050"""
    if ThisEventFlagEnabled():
        DisableCharacter(1510100)
        End()
    DisableImmortality(1510100)
    SetStandbyAnimationSettings(1510100, standby_animation=9000)
    OR_1.Add(Attacked(attacked_entity=1510100, attacker=PLAYER))
    OR_1.Add(FlagEnabled(11515050))
    
    MAIN.Await(OR_1)
    
    EnableFlag(11515050)
    ResetAnimation(1510100, disable_interpolation=True)
    ForceAnimation(1510100, 9060, wait_for_completion=True)
    DisableCharacter(1510100)


@ContinueOnRest(11510120)
def Event_11510120():
    """Event 11510120"""
    DisableNetworkSync()
    if Client():
        return
    AND_1.Add(FlagEnabled(743))
    AND_1.Add(FlagEnabled(12))
    AND_1.Add(FlagDisabled(11510900))
    AND_1.Add(FlagEnabled(11510400))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1512400))
    OR_1.Add(PlayerStandingOnCollision(1513405))
    OR_1.Add(PlayerStandingOnCollision(1513100))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11510130)
def Event_11510130():
    """Event 11510130"""
    if FlagDisabled(11510400):
        DisableCharacter(6640)
        DisableCharacter(6650)
    
        MAIN.Await(FlagEnabled(11510400))
    
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
    if FlagEnabled(1034):
        return
    Move(6010, destination=1512450, destination_type=CoordEntityType.Region, copy_draw_parent=1510452)
    SetNest(6010, region=1512450)
    SetStandbyAnimationSettings(6010)


@ContinueOnRest(11510131)
def Event_11510131():
    """Event 11510131"""
    if Client():
        return
    AND_1.Add(FlagEnabled(11510400))
    AND_1.Add(InsideMap(game_map=ANOR_LONDO))
    AND_1.Add(Host())
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetRespawnPoint(respawn_point=1512960)
    SaveRequest()


@ContinueOnRest(11510140)
def Event_11510140():
    """Event 11510140"""
    MAIN.Await(FlagEnabled(11510900))
    
    MoveRemains(source_region=1512420, destination_region=1512421)


@ContinueOnRest(11510150)
def Event_11510150():
    """Event 11510150"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(PlayerHasGood(115))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512101))
    
    MAIN.Await(AND_1)
    
    End()


@ContinueOnRest(11510460)
def Event_11510460():
    """Event 11510460"""
    OR_7.Add(FlagEnabled(11510593))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_7)
    AND_1.Add(FlagDisabled(11515352))
    AND_1.Add(FlagDisabled(11515350))
    AND_1.Add(FlagDisabled(743))
    AND_1.Add(FlagEnabled(1240))
    AND_1.Add(ActionButton(
        prompt_text=10010210,
        anchor_entity=1512410,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(OR_7)
    AND_2.Add(FlagEnabled(11515352))
    AND_2.Add(FlagDisabled(11515350))
    AND_3.Add(OR_7)
    AND_3.Add(FlagEnabled(11515352))
    AND_3.Add(FlagEnabled(11515350))
    AND_3.Add(Host())
    AND_3.Add(CharacterOutsideRegion(PLAYER, region=1512410))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(10, input_condition=AND_1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, target_entity=1512897)
    EnableFlag(11515350)
    SkipLinesIfHost(1)
    if ThisEventFlagEnabled():
        ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11515352)
    Restart()
    RemoveSpecialEffect(PLAYER, 4170)
    DisableFlag(11515350)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventFlagDisabled(2)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11515352)
    Restart()


@ContinueOnRest(11510462)
def Event_11510462():
    """Event 11510462"""
    DisableNetworkSync()
    WaitFrames(frames=2)
    EnableFlag(11510460)


@RestartOnRest(11510860)
def Event_11510860(_, character: int, item_lot: int):
    """Event 11510860"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        Kill(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot, host_only=True)


@ContinueOnRest(11510461)
def Event_11510461():
    """Event 11510461"""
    MAIN.Await(FlagEnabled(11515351))
    
    AddSpecialEffect(PLAYER, 4170)
    RotateToFaceEntity(PLAYER, target_entity=1510600)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    
    MAIN.Await(FlagDisabled(11515351))
    
    RemoveSpecialEffect(PLAYER, 4170)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    Restart()


@ContinueOnRest(11510600)
def Event_11510600(_, obj: int, obj_act_id: int):
    """Event 11510600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(11515200)
def Event_11515200(_, character: int):
    """Event 11515200"""
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(not AND_2)
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=character,
        anchor_type=CoordEntityType.Character,
        facing_angle=45.0,
        max_distance=1.2000000476837158,
        dummy_id=7,
        trigger_attribute=TriggerAttribute.All,
    ))
    
    MAIN.Await(AND_1)
    
    Move(
        PLAYER,
        destination=character,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        copy_draw_parent=character,
    )
    ForceAnimation(PLAYER, 7521)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(11515210)
def Event_11515210(_, character: int):
    """Event 11515210"""
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 5420))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    AND_7.Add(CharacterBackreadDisabled(character))
    if AND_7:
        return RESTART
    AND_2.Add(CharacterHasSpecialEffect(character, 5421))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_3.Add(CharacterHasSpecialEffect(character, 5422))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_4.Add(CharacterHasSpecialEffect(character, 5423))
    SkipLinesIfConditionFalse(1, AND_4)
    ForceAnimation(character, 3001, wait_for_completion=True)
    AND_5.Add(CharacterHasSpecialEffect(character, 5424))
    SkipLinesIfConditionFalse(1, AND_5)
    ForceAnimation(character, 3006, wait_for_completion=True)
    ReplanAI(character)
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    Restart()


@RestartOnRest(11515220)
def Event_11515220(_, character: int):
    """Event 11515220"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5421))
    AND_1.Add(CharacterHasSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5420))
    AND_2.Add(CharacterHasSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(character, command_id=200, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=210, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11515230)
def Event_11515230(_, character: int):
    """Event 11515230"""
    AND_1.Add(CharacterHasSpecialEffect(character, 5422))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    AND_2.Add(CharacterHasSpecialEffect(character, 5423))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 3150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 3150)
    RemoveSpecialEffect(character, 3151)
    SkipLinesIfLastConditionResultTrue(5, input_condition=AND_2)
    AICommand(character, command_id=201, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    SkipLines(4)
    AICommand(character, command_id=211, command_slot=0)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=-1, command_slot=0)
    OR_2.Add(CharacterHasSpecialEffect(character, 5420))
    OR_2.Add(CharacterHasSpecialEffect(character, 5421))
    
    MAIN.Await(OR_2)
    
    Restart()


@RestartOnRest(11515240)
def Event_11515240(_, character: int, region: int):
    """Event 11515240"""
    AND_1.Add(Singleplayer())
    AND_1.Add(CharacterInsideRegion(character, region=region))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 5421)
    ClearTargetList(character)
    ReplanAI(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    Restart()


@RestartOnRest(11510850)
def Event_11510850(_, character: int):
    """Event 11510850"""
    if ThisEventSlotFlagEnabled():
        DisableCharacter(character)
        End()
    
    MAIN.Await(CharacterDead(character))
    
    End()


@RestartOnRest(11515190)
def Event_11515190(_, character: int):
    """Event 11515190"""
    if Host():
        return
    AND_1.Add(CharacterBackreadDisabled(character))
    if AND_1:
        return
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 0)
    ReplanAI(character)


@RestartOnRest(11515250)
def Event_11515250():
    """Event 11515250"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1510310)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512050))
    AND_2.Add(Attacked(attacked_entity=1510310, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    ForceAnimation(1510310, 500)
    EnableAI(1510310)


@RestartOnRest(11515251)
def Event_11515251():
    """Event 11515251"""
    if ThisEventFlagEnabled():
        return
    DisableAI(1510305)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1512060))
    OR_1.Add(Attacked(attacked_entity=1510305, attacker=PLAYER))
    OR_1.Add(EntityWithinDistance(entity=1510305, other_entity=PLAYER, radius=4.0))
    
    MAIN.Await(OR_1)
    
    EnableAI(1510305)


@ContinueOnRest(11510215)
def Event_11510215():
    """Event 11510215"""
    if ThisEventFlagEnabled():
        DisableObject(1511210)
        End()
    
    MAIN.Await(ObjectDestroyed(1511210))
    
    End()


@ContinueOnRest(11510510)
def Event_11510510(_, character: int, flag: int):
    """Event 11510510"""
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventSlotFlagDisabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11510520)
def Event_11510520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510501)
def Event_11510501(_, character: int, flag: int):
    """Event 11510501"""
    OR_2.Add(FlagEnabled(1030))
    OR_2.Add(FlagEnabled(1031))
    OR_2.Add(FlagEnabled(1036))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1034))
    OR_3.Add(FlagEnabled(1232))
    OR_3.Add(FlagEnabled(1241))
    OR_3.Add(FlagEnabled(1242))
    AND_2.Add(OR_3)
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(ThisEventFlagDisabled())
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    EnableCharacter(character)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11510502)
def Event_11510502(_, character: int, flag: int):
    """Event 11510502"""
    AND_1.Add(FlagEnabled(1240))
    OR_2.Add(FlagEnabled(1232))
    OR_2.Add(FlagEnabled(11515382))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    SetTeamType(character, TeamType.Boss)


@ContinueOnRest(11510530)
def Event_11510530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510530"""
    AND_1.Add(FlagDisabled(1004))
    AND_1.Add(FlagEnabled(1001))
    AND_1.Add(FlagEnabled(11010590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11510531)
def Event_11510531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510531"""
    AND_1.Add(FlagDisabled(1033))
    AND_1.Add(FlagEnabled(1030))
    AND_1.Add(FlagEnabled(710))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510532)
def Event_11510532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510532"""
    AND_1.Add(FlagDisabled(1033))
    OR_1.Add(FlagEnabled(1030))
    OR_1.Add(FlagEnabled(1036))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(FlagEnabled(712))
    AND_1.Add(FlagEnabled(713))
    AND_1.Add(FlagEnabled(714))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11510533)
def Event_11510533(_, character: int):
    """Event 11510533"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    EnableFlag(151)


@ContinueOnRest(11510535)
def Event_11510535(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510535"""
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1493))
    AND_1.Add(CharacterDead(1510300))
    AND_1.Add(CharacterDead(1510301))
    AND_1.Add(CharacterDead(1510302))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableCharacter(character)


@ContinueOnRest(11510536)
def Event_11510536(_, character: int):
    """Event 11510536"""
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(1512))
    AND_1.Add(FlagEnabled(1494))
    AND_1.Add(FlagEnabled(11510590))
    if ThisEventFlagDisabled():
        AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)


@ContinueOnRest(11510541)
def Event_11510541(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510541"""
    OR_1.Add(FlagEnabled(1572))
    OR_1.Add(FlagEnabled(1573))
    OR_1.Add(FlagEnabled(1577))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11510700))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SetTeamType(6490, TeamType.WhitePhantom)
    SetTeamType(6500, TeamType.WhitePhantom)
    DisableAI(character)
    DisableAI(6490)
    DisableAI(6500)
    OR_1.Add(FlagEnabled(11510598))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=6490, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=6500, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    EnableAI(6490)
    EnableAI(6500)


@ContinueOnRest(11510542)
def Event_11510542(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510542"""
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    EnableFlag(8102)


@ContinueOnRest(11510543)
def Event_11510543(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510543"""
    DisableObject(1511750)
    DeleteVFX(1511751, erase_root_only=False)
    DisableObject(1511752)
    DeleteVFX(1511753, erase_root_only=False)
    DisableObject(1511754)
    DeleteVFX(1511755, erase_root_only=False)
    
    MAIN.Await(FlagEnabled(11510700))
    
    EnableObject(1511750)
    CreateVFX(1511751)
    EnableObject(1511752)
    CreateVFX(1511753)
    EnableObject(1511754)
    CreateVFX(1511755)
    DisableFlag(8104)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(1510412)
    DisableCharacter(1510413)
    DisableCharacter(1510500)
    EnableCharacter(character)
    EnableCharacter(6490)
    EnableCharacter(6500)
    if FlagDisabled(8101):
        EnableFlag(8101)
        End()
    EnableFlag(8100)


@ContinueOnRest(11510544)
def Event_11510544(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11510544"""
    if ThisEventFlagEnabled():
        EnableTreasure(obj=1511601)
        End()
    DisableObject(1511601)
    DisableTreasure(obj=1511601)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11510700))
    AND_1.Add(FlagEnabled(8102))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    SkipLinesIfConditionFalse(3, OR_1)
    AwardItemLot(2060, host_only=True)
    AwardItemLot(6300, host_only=True)
    RemoveGoodFromPlayer(item=115)
    EnableObject(1511601)
    EnableTreasure(obj=1511601)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(151)
def Event_151():
    """Event 151"""
    DisableNetworkSync()
    AND_1.Add(ThisEventFlagEnabled())
    AND_1.Add(ActionButton(
        prompt_text=10010182,
        anchor_entity=1511960,
        anchor_type=CoordEntityType.Object,
        max_distance=3.4000000953674316,
        dummy_id=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(
        text=10010184,
        anchor_entity=1511960,
        display_distance=3.4000000953674316,
        button_type=ButtonType.Yes_or_No,
    )
    Restart()


@RestartOnRest(11515090)
def Event_11515090(_, character: int):
    """Event 11515090"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=500))
    
    EzstateAIRequest(character, command_id=1500, command_slot=0)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(character, tae_event_id=500))
    
    Restart()


@RestartOnRest(11515091)
def Event_11515091(_, character: int):
    """Event 11515091"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=1400))
    
    Wait(10.0)
    EzstateAIRequest(character, command_id=1501, command_slot=0)
    Restart()


@RestartOnRest(11515092)
def Event_11515092(_, character: int, obj: int, flag: int, flag_1: int):
    """Event 11515092"""
    if FlagEnabled(flag):
        return
    if FlagEnabled(flag_1):
        return
    DisableCharacterCollision(character)
    DisableGravity(character)
    EnableObjectInvulnerability(obj)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    WaitFrames(frames=1)
    DestroyObject(obj)
    PlaySoundEffect(obj, 596500000, sound_type=SoundType.o_Object)


@ContinueOnRest(11515030)
def Event_11515030():
    """Event 11515030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6543, authority_level=UpdateAuthority.Forced)
    if ThisEventFlagEnabled():
        DisableCharacter(6003)
    SkipLinesIfFlagEnabled(3, 11515034)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11515031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6543)
    if FlagEnabled(12):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(FlagEnabled(1004))
    OR_1.Add(FlagEnabled(1005))
    OR_1.Add(FlagEnabled(1006))
    OR_1.Add(FlagEnabled(1010))
    OR_1.Add(FlagEnabled(1011))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterBackreadEnabled(6543))
    AND_1.Add(EntityWithinDistance(entity=6543, other_entity=PLAYER, radius=30.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6543,
        region=1512001,
        summon_flag=11515031,
        dismissal_flag=11515034,
    )
    DisableCharacter(6003)
    
    MAIN.Await(FlagEnabled(11515031))
    
    SetNest(6543, region=1512002)


@ContinueOnRest(11515032)
def Event_11515032():
    """Event 11515032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11515031))
    AND_1.Add(FlagEnabled(11515393))
    
    MAIN.Await(AND_1)
    
    AICommand(6543, command_id=10, command_slot=0)
    ReplanAI(6543)
    
    MAIN.Await(CharacterInsideRegion(6543, region=1512998))
    
    RotateToFaceEntity(6543, target_entity=1512997)
    ForceAnimation(6543, 7410)
    AICommand(6543, command_id=-1, command_slot=0)
    ReplanAI(6543)


@ContinueOnRest(11515033)
def Event_11515033():
    """Event 11515033"""
    AND_1.Add(FlagEnabled(11515031))
    AND_1.Add(FlagDisabled(11515390))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1512801))
    
    MAIN.Await(AND_1)
    
    AICommand(6543, command_id=8, command_slot=0)
    ReplanAI(6543)
    
    MAIN.Await(AllPlayersOutsideRegion(region=1512801))
    
    AICommand(6543, command_id=-1, command_slot=0)
    ReplanAI(6543)
    Restart()
