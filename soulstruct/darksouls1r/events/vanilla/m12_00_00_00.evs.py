"""
Darkroot Garden / Basin

linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@ContinueOnRest(0)
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
    DeleteVFX(1201995, erase_root_only=False)
    DisableObject(1201996)
    DeleteVFX(1201997, erase_root_only=False)
    DisableObject(1201998)
    DeleteVFX(1201999, erase_root_only=False)
    DisableObject(1201988)
    DeleteVFX(1201989, erase_root_only=False)
    DisableObject(1201986)
    DeleteVFX(1201987, erase_root_only=False)
    Event_11200090(0, obj=1201700, vfx_id=1201701, destination=1202600, destination_1=1202601)
    Event_11205080()
    Event_11205081()
    Event_11205082()
    Event_11200100(0, flag=11200110, obj=1201000, model_point=120020, anchor_entity=1202500, left=0, flag_1=61200500)
    Event_11200110(0, flag=11200100, line_intersects=1201000, anchor_entity=1202500, left=0)
    Event_11200100(1, flag=11200111, obj=1201010, model_point=120021, anchor_entity=1202501, left=1, flag_1=61200501)
    Event_11200110(1, flag=11200101, line_intersects=1201010, anchor_entity=1202501, left=1)
    Event_11200120()
    Event_11205000()
    Event_11200800()
    Event_11200200()
    Event_11200690()
    Event_11200600(0, obj=1201650, obj_act_id=11200600)
    Event_11200600(1, obj=1201651, obj_act_id=11200601)
    DisableSoundEvent(sound_id=1203800)
    if FlagEnabled(5):
        Event_11205392()
        DisableObject(1201990)
        DeleteVFX(1201991, erase_root_only=False)
    else:
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
    if FlagEnabled(11200900):
        Event_11205382()
        DisableObject(1201890)
        DeleteVFX(1201891, erase_root_only=False)
        DisableObject(1201892)
        DeleteVFX(1201893, erase_root_only=False)
    else:
        Event_11205380()
        Event_11205381()
        Event_11205383()
        Event_11205382()
        Event_11200900()
        Event_11205384()
        Event_11205385()
        Event_11205120(0, region=1202220, destination=1202180)
        Event_11205120(1, region=1202221, destination=1202181)
        Event_11205120(2, region=1202222, destination=1202182)
        Event_11205120(3, region=1202223, destination=1202183)
        Event_11205120(4, region=1202224, destination=1202184)
        Event_11205120(5, region=1202225, destination=1202185)
        Event_11205120(6, region=1202226, destination=1202186)
        Event_11205120(7, region=1202227, destination=1202187)
        Event_11205120(8, region=1202228, destination=1202188)
        Event_11205120(9, region=1202229, destination=1202189)
    Event_11200801()
    Event_11205300(
        0,
        part_index=1,
        npc_part_id=3530,
        npc_part_id_1=3530,
        character=1200011,
        model_point=91,
        bit_index=0,
        bit_index_1=1,
        special_effect_id=5430,
    )
    Event_11205300(
        1,
        part_index=2,
        npc_part_id=3531,
        npc_part_id_1=3531,
        character=1200012,
        model_point=92,
        bit_index=1,
        bit_index_1=2,
        special_effect_id=5431,
    )
    Event_11205300(
        2,
        part_index=3,
        npc_part_id=3532,
        npc_part_id_1=3532,
        character=1200013,
        model_point=93,
        bit_index=2,
        bit_index_1=3,
        special_effect_id=5432,
    )
    Event_11205300(
        3,
        part_index=4,
        npc_part_id=3533,
        npc_part_id_1=3533,
        character=1200014,
        model_point=94,
        bit_index=3,
        bit_index_1=4,
        special_effect_id=5433,
    )
    Event_11205300(
        4,
        part_index=5,
        npc_part_id=3534,
        npc_part_id_1=3534,
        character=1200015,
        model_point=95,
        bit_index=4,
        bit_index_1=5,
        special_effect_id=5434,
    )
    Event_11205300(
        5,
        part_index=6,
        npc_part_id=3535,
        npc_part_id_1=3535,
        character=1200016,
        model_point=96,
        bit_index=5,
        bit_index_1=6,
        special_effect_id=5435,
    )
    Event_11205300(
        6,
        part_index=8,
        npc_part_id=3536,
        npc_part_id_1=3536,
        character=1200017,
        model_point=97,
        bit_index=6,
        bit_index_1=7,
        special_effect_id=5436,
    )
    Event_11205250(0, character=1200100, region=1202110)
    Event_11205290(0, character=1200101, flag=51200170, seconds=0.0, right=1)
    Event_11205290(1, character=1200102, flag=51200170, seconds=0.20000000298023224, right=1)
    Event_11205290(2, character=1200103, flag=51200170, seconds=0.800000011920929, right=1)
    Event_11205250(1, character=1200104, region=1202111)
    Event_11205290(3, character=1200105, flag=11205263, seconds=0.0, right=0)
    Event_11205290(4, character=1200106, flag=11205263, seconds=0.6000000238418579, right=0)
    Event_11205290(5, character=1200107, flag=11205264, seconds=0.0, right=0)
    Event_11205290(6, character=1200108, flag=11205264, seconds=0.8999999761581421, right=0)
    Event_11205200(0, character=1200109, radius=8.0)
    Event_11205200(1, character=1200110, radius=8.0)
    Event_11205200(2, character=1200111, radius=5.0)
    Event_11205200(3, character=1200112, radius=5.0)
    Event_11205200(4, character=1200113, radius=5.0)
    Event_11205230(0, character=1200600, radius=3.0)
    Event_11205230(2, character=1200602, radius=3.0)
    Event_11205240(0, character=1200600, region=1202710)
    Event_11205240(2, character=1200602, region=1202712)
    Event_11205280(0, character=1200650, radius=6.0, region=1202112)
    Event_11205280(1, character=1200651, radius=2.0, region=1202112)
    Event_11205260(0, character=1200652, radius=6.0)
    Event_11205260(1, character=1200653, radius=10.0)
    Event_11205260(2, character=1200654, radius=8.0)
    Event_11205260(3, character=1200655, radius=4.0)
    Event_11205260(4, character=1200656, radius=4.0)
    Event_11205190(0, character=1200250, region=1202113, seconds=0.0)
    Event_11205190(1, character=1200251, region=1202113, seconds=0.5)
    Event_11205190(2, character=1200252, region=1202113, seconds=1.2000000476837158)
    Event_11205190(3, character=1200253, region=1202113, seconds=0.699999988079071)
    Event_11205150(0, character=1200705)
    Event_11205150(1, character=1200706)
    Event_11205150(2, character=1200707)
    Event_11205150(3, character=1200708)
    Event_11205150(4, character=1200709)
    Event_11205150(5, character=1200710)
    Event_11205150(6, character=1200711)
    Event_11205150(7, character=1200712)
    Event_11205180(0, character=1200350, left=1)
    Event_11205180(1, character=1200351, left=0)
    Event_11205180(2, character=1200352, left=0)
    Event_11200810(0, character=1200000, left=0, item_lot_param_id=0)
    Event_11200810(1, character=1200001, left=0, item_lot_param_id=0)
    Event_11200810(2, character=1200400, left=0, item_lot_param_id=33004000)
    Event_11200810(3, character=1200350, left=0, item_lot_param_id=0)
    Event_11200810(4, character=1200351, left=0, item_lot_param_id=0)
    Event_11200810(5, character=1200352, left=0, item_lot_param_id=0)
    Event_11200810(6, character=1200750, left=0, item_lot_param_id=27901000)
    Event_11200810(7, character=1200301, left=0, item_lot_param_id=0)
    Event_11200810(8, character=1200304, left=1, item_lot_param_id=0)
    Event_11200810(9, character=1200306, left=0, item_lot_param_id=0)
    Event_11205843(0, flag=11200900, line_intersects=1201890, anchor_entity=1202898, target_entity=1202894)
    Event_11205846(0, flag=11200900, obj=1201890, vfx_id=1201891)
    Event_11205843(1, flag=5, line_intersects=1201990, anchor_entity=1202998, target_entity=1202997)
    Event_11205846(1, 5, 1201990, 1201991)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    HumanityRegistration(6521, event_flag=8932)
    Event_11205030()
    Event_11205035()
    Event_11205032()
    Event_11200300()
    Event_11205990(0, flag=11205031, summoned_character=6521)
    SkipLinesIfClient(2)
    DisableFlagRange((11200210, 11200213))
    DisableFlag(11200215)
    HumanityRegistration(6050, event_flag=8350)
    HumanityRegistration(6051, event_flag=8350)
    SkipLinesIfClient(6)
    if FlagEnabled(1123):
        DisableFlagRange((1120, 1139))
        EnableFlag(1122)
    if FlagEnabled(1130):
        DisableFlagRange((1120, 1139))
        EnableFlag(1129)
    if FlagDisabled(1121):
        DisableCharacter(6050)
    if FlagDisabled(1123):
        DisableCharacter(6051)
    if FlagDisabled(1130):
        DisableCharacter(6051)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    Event_11200520(0, character=6050, first_flag=1120, last_flag=1139, flag=1125)
    Event_11200520(1, character=6051, first_flag=1120, last_flag=1139, flag=1125)
    Event_11200530(0, character=6050, first_flag=1120, last_flag=1139, flag=1121)
    Event_11200531(0, character=6050, first_flag=1120, last_flag=1139, flag=1122)
    Event_11200534(0, character=6050, first_flag=1120, last_flag=1139, flag=1123)
    Event_11200532(0, character=6050, first_flag=1120, last_flag=1139, flag=1126)
    Event_11200533()
    Event_11205040(0, flag=11200210, destination=1202000, vfx_id=1203100)
    Event_11205040(1, flag=11200211, destination=1202001, vfx_id=1203101)
    Event_11205040(2, flag=11200212, destination=1202002, vfx_id=1203102)
    Event_11205040(3, flag=11200213, destination=1202003, vfx_id=1203103)
    Event_11200529(0, first_flag=1120, last_flag=1139, flag=1127)
    Event_11200527(0, character=6050, first_flag=1120, last_flag=1139, flag=1129)
    Event_11200525(0, character=6050, first_flag=1120, last_flag=1139, flag=1130)
    Event_11205070(0, flag=11200210, destination=1202000, vfx_id=1203100)
    Event_11205070(1, flag=11200211, destination=1202001, vfx_id=1203101)
    Event_11205070(2, flag=11200212, destination=1202002, vfx_id=1203102)
    Event_11205070(3, flag=11200213, destination=1202003, vfx_id=1203103)
    DeleteVFX(1202009, erase_root_only=False)
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
    Event_11200538(0, character=6380, first_flag=1710, last_flag=1712, flag=1711)
    Event_11200539(0, character=6380, first_flag=1710, last_flag=1712, flag=1712)
    Event_11200540(0, character=6380, first_flag=1710, last_flag=1712, flag=1711)
    Event_11205058()
    Event_11205054()
    Event_11205056()
    Event_11205057()
    Event_11205060(0, character=6310)
    Event_11205060(1, character=6420)
    Event_11205060(2, character=1200300)
    Event_11205060(3, character=1200301)
    Event_11205060(4, character=1200302)
    Event_11205060(5, character=1200303)
    Event_11205060(6, character=1200304)
    Event_11205060(7, character=1200305)
    Event_11205060(8, character=1200306)
    HumanityRegistration(6310, event_flag=8470)
    HumanityRegistration(6420, event_flag=8900)
    DisableCharacter(6310)
    DisableCharacter(6420)
    Event_11200520(2, character=6310, first_flag=1600, last_flag=1619, flag=1604)
    Event_11200520(3, character=6420, first_flag=1760, last_flag=1769, flag=1764)
    Event_11200501(0, character=6310, flag=1603)
    Event_11200535(0, 6310)


@ContinueOnRest(11200090)
def Event_11200090(_, obj: int, vfx_id: int, destination: int, destination_1: int):
    """Event 11200090"""
    if ThisEventSlotFlagEnabled():
        DisableObject(obj)
        DeleteVFX(vfx_id, erase_root_only=False)
        End()
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    AND_2.Add(ActionButton(
        prompt_text=10010407,
        anchor_entity=destination_1,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        line_intersects=obj,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    SkipLines(1)
    Move(PLAYER, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(PLAYER, 7410)
    DisableObject(obj)
    DeleteVFX(vfx_id)


@RestartOnRest(11205080)
def Event_11205080():
    """Event 11205080"""
    if ThisEventFlagEnabled():
        return
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
    
    MAIN.Await(FlagEnabled(11200050))
    
    if FlagEnabled(735):
        return
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
    OR_1.Add(FlagEnabled(11205085))
    OR_1.Add(FlagEnabled(735))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(735):
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
    if Client():
        return
    AND_1.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_1.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(11200050))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    AND_2.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_2.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(11200050))
    if not OR_2:
        return RESTART
    WaitFrames(frames=1)
    AND_3.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_3.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(11200050))
    if not OR_3:
        return RESTART
    WaitFrames(frames=1)
    AND_4.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_4.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_4.Add(AND_4)
    OR_4.Add(FlagEnabled(11200050))
    if not OR_4:
        return RESTART
    WaitFrames(frames=1)
    AND_5.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_5.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_5.Add(AND_5)
    OR_5.Add(FlagEnabled(11200050))
    if not OR_5:
        return RESTART
    WaitFrames(frames=1)
    AND_6.Add(BlackWorldTendencyComparison(ComparisonType.GreaterThan, value=50))
    AND_6.Add(InsideMap(game_map=DARKROOT_GARDEN))
    OR_6.Add(AND_6)
    OR_6.Add(FlagEnabled(11200050))
    if not OR_6:
        return RESTART
    EnableFlag(11200050)
    Wait(600.0)
    AND_7.Add(BlackWorldTendencyComparison(ComparisonType.LessThanOrEqual, value=50))
    AND_7.Add(InsideMap(game_map=DARKROOT_GARDEN))
    if not AND_7:
        return RESTART
    DisableFlag(11200050)
    EnableFlag(11205085)


@RestartOnRest(11200000)
def Event_11200000():
    """Event 11200000"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(11200002):
        return
    DisableCharacter(1200800)
    DisableObject(1201990)
    DeleteVFX(1201991, erase_root_only=False)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(11210021))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120000, cutscene_flags=0, player_id=10000, move_to_region=1202801, game_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120000,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1202801,
        game_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1201200)
    Move(1200800, destination=1202800, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateVFX(1201991)
    EnableFlag(11200002)


@ContinueOnRest(11200002)
def Event_11200002():
    """Event 11200002"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(11200000):
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(11210021))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202999))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)
    EnableFlag(11205390)
    EnableFlag(11205391)
    EnableFlag(11205393)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionFalse(1, AND_2)
    
    MAIN.Await(FlagEnabled(703))
    
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120003, cutscene_flags=0, player_id=10000, move_to_region=1202802, game_map=DARKROOT_GARDEN)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        120003,
        cutscene_flags=CutsceneFlags.Unskippable,
        player_id=10000,
        move_to_region=1202802,
        game_map=DARKROOT_GARDEN,
    )
    SkipLines(1)
    PlayCutscene(120003, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(1201200)
    EnableCharacter(1200800)
    EnableObject(1201990)
    CreateVFX(1201991)
    EnableFlag(11200000)


@ContinueOnRest(11205390)
def Event_11205390():
    """Event 11205390"""
    AND_1.Add(FlagDisabled(5))
    AND_1.Add(FlagEnabled(11200000))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205391)
def Event_11205391():
    """Event 11205391"""
    AND_1.Add(FlagDisabled(5))
    AND_1.Add(FlagEnabled(11205393))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202998,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201990,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202997)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205393)
def Event_11205393():
    """Event 11205393"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagEnabled(11200000))
        AND_1.Add(FlagDisabled(5))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1202996))
        AND_2.Add(ThisEventFlagEnabled())
        OR_1.Add(AND_1)
        OR_1.Add(AND_2)
    
        MAIN.Await(OR_1)
    
        EndIfFinishedConditionTrue(input_condition=AND_2)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1200800)


@RestartOnRest(11205392)
def Event_11205392():
    """Event 11205392"""
    if FlagEnabled(5):
        DisableCharacter(1200800)
        Kill(1200800)
        End()
    DisableAI(1200800)
    AND_1.Add(FlagEnabled(11200000))
    AND_1.Add(FlagEnabled(11205393))
    
    MAIN.Await(AND_1)
    
    EnableAI(1200800)
    EnableBossHealthBar(1200800, name=5210)


@ContinueOnRest(11200001)
def Event_11200001():
    """Event 11200001"""
    MAIN.Await(CharacterDead(1200800))
    
    EnableFlag(5)
    KillBoss(game_area_param_id=1200800)
    DisableObject(1201990)
    DeleteVFX(1201991)


@ContinueOnRest(11205394)
def Event_11205394():
    """Event 11205394"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(5))
    AND_1.Add(FlagEnabled(11205392))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11205391))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202990))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1203800)


@ContinueOnRest(11205395)
def Event_11205395():
    """Event 11205395"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(5))
    AND_1.Add(FlagEnabled(11205394))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1203800)


@RestartOnRest(11205396)
def Event_11205396():
    """Event 11205396"""
    if ThisEventFlagDisabled():
        MAIN.Await(HealthRatio(1200800) <= 0.10000000149011612)
    AddSpecialEffect(1200800, 5401)


@ContinueOnRest(11205380)
def Event_11205380():
    """Event 11205380"""
    AND_1.Add(FlagDisabled(11200900))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=1201890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205381)
def Event_11205381():
    """Event 11205381"""
    AND_1.Add(FlagDisabled(11200900))
    AND_1.Add(FlagEnabled(11205383))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=1202898,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=1201890,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


@ContinueOnRest(11205383)
def Event_11205383():
    """Event 11205383"""
    if ThisEventFlagDisabled():
        AND_1.Add(FlagDisabled(11200900))
        AND_1.Add(CharacterInsideRegion(PLAYER, region=1202896))
    
        MAIN.Await(AND_1)
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
    if FlagEnabled(11200900):
        DisableCharacter(1200801)
        Kill(1200801)
        End()
    DisableHealthBar(1200801)
    DisableAI(1200801)
    SetStandbyAnimationSettings(1200801, standby_animation=7000)
    
    MAIN.Await(FlagEnabled(11205383))
    
    SetStandbyAnimationSettings(1200801, cancel_animation=7001)
    EnableAI(1200801)
    EnableBossHealthBar(1200801, name=3230)


@ContinueOnRest(11200900)
def Event_11200900():
    """Event 11200900"""
    MAIN.Await(CharacterDead(1200801))
    
    RemoveSpecialEffect(PLAYER, 5500)
    EnableFlag(11200900)
    KillBoss(game_area_param_id=1200801)
    DisableObject(1201890)
    DeleteVFX(1201891)
    DisableObject(1201892)
    DeleteVFX(1201893)


@ContinueOnRest(11205384)
def Event_11205384():
    """Event 11205384"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(11200900))
    AND_1.Add(FlagEnabled(11205382))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(11205381))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=1202890))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=1203801)


@ContinueOnRest(11205385)
def Event_11205385():
    """Event 11205385"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(11200900))
    AND_1.Add(FlagEnabled(11205384))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=1203801)


@ContinueOnRest(11205120)
def Event_11205120(_, region: int, destination: int):
    """Event 11205120"""
    AND_1.Add(CharacterInsideRegion(1200801, region=region))
    AND_1.Add(CharacterHasTAEEvent(1200801, tae_event_id=10))
    
    MAIN.Await(AND_1)
    
    Move(1200801, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    
    MAIN.Await(CharacterDoesNotHaveTAEEvent(1200801, tae_event_id=10))
    
    Restart()


@ContinueOnRest(11200100)
def Event_11200100(_, flag: int, obj: int, model_point: int, anchor_entity: int, left: int, flag_1: int):
    """Event 11200100"""
    SkipLinesIfFlagEnabled(1, flag_1)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EndOfAnimation(obj=obj, animation_id=1)
    End()
    CreateObjectVFX(obj, vfx_id=200, model_point=model_point)
    if ValueNotEqual(left=left, right=1):
        AND_1.Add(PlayerHasGood(2002))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=obj,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfValueEqual(1, left=left, right=1)
    SkipLinesIfClient(1)
    if ValueNotEqual(left=left, right=1):
        DisplayDialog(text=10010861, anchor_entity=obj, button_type=ButtonType.Yes_or_No)
    ForceAnimation(obj, 1)
    DeleteObjectVFX(obj)


@ContinueOnRest(11200110)
def Event_11200110(_, flag: int, line_intersects: int, anchor_entity: int, left: int):
    """Event 11200110"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(flag))
    if ValueNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(703))
    if ValueNotEqual(left=left, right=1):
        AND_1.Add(PlayerDoesNotHaveGood(2002))
    AND_1.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=line_intersects,
    ))
    AND_2.Add(Client())
    AND_2.Add(ActionButton(
        prompt_text=10010400,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=line_intersects,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=10010160, anchor_entity=line_intersects, button_type=ButtonType.Yes_or_No)
    Restart()


@ContinueOnRest(11200120)
def Event_11200120():
    """Event 11200120"""
    if ThisEventFlagEnabled():
        DisableObject(1201300)
        End()
    
    MAIN.Await(ObjectDestroyed(1201300))
    
    EnableFlag(11200120)


@RestartOnRest(11205150)
def Event_11205150(_, character: int):
    """Event 11205150"""
    AND_1.Add(HealthRatio(character) <= 0.800000011920929)
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(11205180)
def Event_11205180(_, character: int, left: int):
    """Event 11205180"""
    if ValueNotEqual(left=left, right=0):
        MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
        SetNest(character, region=1202732)
        End()
    if ThisEventSlotFlagDisabled():
        SetStandbyAnimationSettings(character, standby_animation=9000)
        DisableAI(character)
    
        MAIN.Await(HealthRatio(1200350) <= 0.4000000059604645)
    
        WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
        SetStandbyAnimationSettings(character, cancel_animation=9060)
        EnableAI(character)
    SetNest(character, region=1202732)


@RestartOnRest(11205190)
def Event_11205190(_, character: int, region: int, seconds: float):
    """Event 11205190"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacter(character)
    DisableAI(character)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    Wait(seconds)
    EnableGravity(character)
    EnableCharacter(character)
    ForceAnimation(character, 7000, wait_for_completion=True)
    EnableAI(character)


@RestartOnRest(11205200)
def Event_11205200(_, character: int, radius: float):
    """Event 11205200"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=6521))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205250)
def Event_11205250(_, character: int, region: int):
    """Event 11205250"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=6521))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(6521, region=region))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205290)
def Event_11205290(_, character: int, flag: int, seconds: float, right: int):
    """Event 11205290"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableAI(character)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(Attacked(attacked_entity=character, attacker=6521))
    SkipLinesIfValueEqual(1, left=0, right=right)
    SkipLinesIfClient(1)
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    EnableAI(character)
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205230)
def Event_11205230(_, character: int, radius: float):
    """Event 11205230"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    DisableCharacterCollision(character)
    DisableGravity(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=6521, radius=radius))
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(Attacked(attacked_entity=character, attacker=6521))
    AND_1.Add(OR_1)
    AND_2.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableCharacterCollision(character)
    EnableGravity(character)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    SetStandbyAnimationSettings(character, cancel_animation=9063)


@RestartOnRest(11205240)
def Event_11205240(_, character: int, region: int):
    """Event 11205240"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5110))
    
    SetNest(character, region=region)


@RestartOnRest(11205260)
def Event_11205260(_, character: int, radius: float):
    """Event 11205260"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=6521, radius=radius))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205280)
def Event_11205280(_, character: int, radius: float, region: int):
    """Event 11205280"""
    if ThisEventSlotFlagEnabled():
        SetStandbyAnimationSettings(character)
        End()
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=6521, radius=radius))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(6521, region=region))
    
    MAIN.Await(OR_1)
    
    SetStandbyAnimationSettings(character, cancel_animation=9060)


@RestartOnRest(11205000)
def Event_11205000():
    """Event 11205000"""
    DisableGravity(1200000)
    DisableCharacterCollision(1200000)
    if ThisEventFlagDisabled():
        MAIN.Await(CharacterInsideRegion(PLAYER, region=1202100))
    EnableGravity(1200000)
    EnableCharacterCollision(1200000)
    SetNest(1200000, region=1202101)


@RestartOnRest(11200800)
def Event_11200800():
    """Event 11200800"""
    DisableCharacter(1200200)
    if ThisEventFlagEnabled():
        return
    if FlagDisabled(11200801):
        MAIN.Await(FlagEnabled(703))
    EnableCharacter(1200200)
    
    MAIN.Await(CharacterBackreadEnabled(1200200))
    
    SetDisplayMask(1200200, bit_index=0, switch_type=OnOffChange.Off)
    
    MAIN.Await(CharacterDead(1200200))
    
    EnableFlag(11200800)


@RestartOnRest(11200801)
def Event_11200801():
    """Event 11200801"""
    if ThisEventFlagEnabled():
        DisableCharacter(1200010)
        End()
    OR_1.Add(CharacterDead(1200010))
    AND_1.Add(CharacterDead(1200011))
    AND_1.Add(CharacterDead(1200012))
    AND_1.Add(CharacterDead(1200013))
    AND_1.Add(CharacterDead(1200014))
    AND_1.Add(CharacterDead(1200015))
    AND_1.Add(CharacterDead(1200016))
    AND_1.Add(CharacterDead(1200017))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    Kill(1200010, award_souls=True)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(35300100, host_only=True)


@RestartOnRest(11205300)
def Event_11205300(
    _,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    character: int,
    model_point: int,
    bit_index: uchar,
    bit_index_1: uchar,
    special_effect_id: int,
):
    """Event 11205300"""
    DisableCharacter(character)
    if ThisEventSlotFlagEnabled():
        SetDisplayMask(1200010, bit_index=bit_index, switch_type=OnOffChange.On)
        SetCollisionMask(1200010, bit_index=bit_index_1, switch_type=OnOffChange.Off)
        AddSpecialEffect(1200010, special_effect_id)
        End()
    
    MAIN.Await(CharacterBackreadEnabled(1200010))
    
    CreateNPCPart(1200010, npc_part_id=npc_part_id, part_index=part_index, part_health=176)
    AND_1.Add(CharacterPartHealth(1200010, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(1200010) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ResetAnimation(1200010)
    Move(
        character,
        destination=1200010,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=1200010,
    )
    EnableCharacter(character)
    ForceAnimation(character, 8100)
    ForceAnimation(1200010, 8000)
    SetDisplayMask(1200010, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(1200010, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    AddSpecialEffect(1200010, special_effect_id)


@ContinueOnRest(11200200)
def Event_11200200():
    """Event 11200200"""
    DisableNetworkSync()
    if Client():
        return
    AND_1.Add(Host())
    AND_2.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(not AND_2)
    OR_1.Add(PlayerStandingOnCollision(1203500))
    OR_1.Add(PlayerStandingOnCollision(1203501))
    OR_1.Add(PlayerStandingOnCollision(1203502))
    OR_1.Add(PlayerStandingOnCollision(1203503))
    OR_1.Add(PlayerStandingOnCollision(1203504))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 4500)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(11200810)
def Event_11200810(_, character: int, left: int, item_lot_param_id: int):
    """Event 11200810"""
    SkipLinesIfThisEventSlotFlagDisabled(6)
    SkipLinesIfValueEqual(3, left=left, right=1)
    DisableCharacter(character)
    Kill(character)
    End()
    DropMandatoryTreasure(character)
    End()
    
    MAIN.Await(CharacterDead(character))
    
    if ValueEqual(left=item_lot_param_id, right=0):
        return
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    if not OR_7:
        return
    AwardItemLot(item_lot_param_id, host_only=True)


@ContinueOnRest(11200600)
def Event_11200600(_, obj: int, obj_act_id: int):
    """Event 11200600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    DisableTreasure(obj=obj)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(11200690)
def Event_11200690():
    """Event 11200690"""
    if ThisEventFlagDisabled():
        DisableTreasure(obj=1201600)
        DisableObject(1201600)
        OR_1.Add(FlagEnabled(1123))
        OR_1.Add(FlagEnabled(1130))
    
        MAIN.Await(OR_1)
    
        EnableObject(1201600)
    EnableTreasure(obj=1201600)


@ContinueOnRest(11200510)
def Event_11200510(_, character: int, flag: int):
    """Event 11200510"""
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
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_3)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(703))
    
    EnableFlag(flag)
    SetTeamTypeAndExitStandbyAnimation(character, team_type=TeamType.HostileAlly)
    SaveRequest()


@ContinueOnRest(11200520)
def Event_11200520(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200520"""
    if ThisEventSlotFlagEnabled():
        DropMandatoryTreasure(character)
        End()
    
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200501)
def Event_11200501(_, character: int, flag: int):
    """Event 11200501"""
    AND_1.Add(FlagDisabled(1603))
    AND_1.Add(FlagEnabled(1600))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(ThisEventFlagDisabled())
    AND_2.Add(FlagDisabled(1763))
    AND_2.Add(FlagEnabled(1760))
    AND_2.Add(HealthRatio(6420) <= 0.8999999761581421)
    AND_2.Add(HealthRatio(6420) > 0.0)
    AND_2.Add(Attacked(attacked_entity=6420, attacker=PLAYER))
    AND_2.Add(ThisEventFlagDisabled())
    AND_3.Add(FlagEnabled(746))
    AND_3.Add(ThisEventFlagDisabled())
    OR_2.Add(FlagEnabled(flag))
    OR_2.Add(FlagEnabled(1763))
    AND_4.Add(OR_2)
    AND_4.Add(ThisEventFlagEnabled())
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_4)
    if FlagDisabled(1604):
        EnableFlag(flag)
    if FlagDisabled(1764):
        EnableFlag(1763)
    if FlagDisabled(1604):
        EnableCharacter(character)
    if FlagDisabled(1764):
        EnableCharacter(6420)
    SetTeamType(character, TeamType.Enemy)
    SetTeamType(6420, TeamType.Enemy)
    SaveRequest()
    EnableFlag(1766)


@ContinueOnRest(11200530)
def Event_11200530(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200530"""
    AND_1.Add(FlagEnabled(1120))
    AND_1.Add(FlagEnabled(11200800))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    Move(
        character,
        destination=1200200,
        destination_type=CoordEntityType.Character,
        model_point=101,
        copy_draw_parent=1200200,
    )
    EnableCharacter(character)
    Wait(0.5)
    SetStandbyAnimationSettings(character, standby_animation=7875)
    ForceAnimation(character, 7876)


@ContinueOnRest(11200531)
def Event_11200531(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200531"""
    AND_1.Add(FlagEnabled(1121))
    AND_1.Add(FlagEnabled(11200590))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7877, wait_for_completion=True)
    ForceAnimation(character, 8289, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200532)
def Event_11200532(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200532"""
    AND_1.Add(FlagEnabled(1121))
    AND_1.Add(FlagEnabled(11200591))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7877, wait_for_completion=True)
    ForceAnimation(character, 8289, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200533)
def Event_11200533():
    """Event 11200533"""
    DeleteVFX(1203100, erase_root_only=False)
    DeleteVFX(1203101, erase_root_only=False)
    DeleteVFX(1203102, erase_root_only=False)
    DeleteVFX(1203103, erase_root_only=False)
    if Client():
        return
    AND_1.Add(PlayerDoesNotHaveGood(2520))
    AND_1.Add(FlagEnabled(1122))
    AND_2.Add(FlagEnabled(1129))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableRandomFlagInRange(flag_range=(11200210, 11200213))
    if FlagEnabled(11200210):
        CreateVFX(1203100)
    if FlagEnabled(11200211):
        CreateVFX(1203101)
    if FlagEnabled(11200212):
        CreateVFX(1203102)
    if FlagEnabled(11200213):
        CreateVFX(1203103)


@ContinueOnRest(11205040)
def Event_11205040(_, flag: int, destination: int, vfx_id: int):
    """Event 11205040"""
    if FlagEnabled(11200215):
        EnableCharacter(6051)
        End()
    AND_1.Add(FlagEnabled(1122))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=50000000,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11200215)
    DeleteVFX(vfx_id)
    Move(6051, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205310)


@ContinueOnRest(11200534)
def Event_11200534(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200534"""
    AND_1.Add(FlagEnabled(1122))
    AND_1.Add(FlagEnabled(11205310))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200529)
def Event_11200529(_, first_flag: int, last_flag: int, flag: int):
    """Event 11200529"""
    if FlagEnabled(17):
        return
    OR_1.Add(FlagEnabled(1122))
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfFlagEnabled(2, 1125)
    SkipLinesIfFlagEnabled(1, 1126)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200527)
def Event_11200527(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200527"""
    MAIN.Await(FlagEnabled(1128))
    
    SkipLinesIfFlagEnabled(5, 1125)
    SkipLinesIfFlagEnabled(8, 1126)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    DisableCharacter(character)
    End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1125)
    DisableCharacter(character)
    End()
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(1126)
    DisableCharacter(character)


@ContinueOnRest(11205070)
def Event_11205070(_, flag: int, destination: int, vfx_id: int):
    """Event 11205070"""
    if FlagEnabled(11200215):
        EnableCharacter(6051)
        End()
    AND_1.Add(FlagEnabled(1129))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=50000000,
        anchor_entity=destination,
        anchor_type=CoordEntityType.Region,
        model_point=0,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11200215)
    DeleteVFX(vfx_id)
    Move(6051, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=1203150)
    Wait(5.0)
    EnableCharacter(6051)
    CreateTemporaryVFX(vfx_id=120, anchor_entity=destination, anchor_type=CoordEntityType.Region)
    SetStandbyAnimationSettings(6051, standby_animation=7875)
    ForceAnimation(6051, 6951, wait_for_completion=True)
    ForceAnimation(6051, 7876)
    EnableFlag(11205311)


@ContinueOnRest(11200525)
def Event_11200525(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200525"""
    AND_1.Add(FlagEnabled(1129))
    AND_1.Add(FlagEnabled(11205311))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200535)
def Event_11200535(_, character: int):
    """Event 11200535"""
    SkipLinesIfClient(1)
    DisableFlag(11205021)
    SkipLinesIfHost(1)
    if FlagDisabled(11205021):
        AND_1.Add(FlagDisabled(1603))
        AND_1.Add(FlagDisabled(1601))
        AND_1.Add(Host())
        AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    
        MAIN.Await(AND_1)
    if FlagDisabled(1604):
        EnableCharacter(character)
    if FlagDisabled(1764):
        EnableCharacter(6420)
        EnableFlag(1766)
    EnableFlag(11205021)


@ContinueOnRest(11200538)
def Event_11200538(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200538"""
    MAIN.Await(Attacked(attacked_entity=character, attacker=PLAYER))
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 9030, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11200539)
def Event_11200539(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200539"""
    AND_1.Add(FlagEnabled(1710))
    AND_1.Add(FlagEnabled(746))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)


@ContinueOnRest(11200540)
def Event_11200540(_, character: int, first_flag: int, last_flag: int, flag: int):
    """Event 11200540"""
    AND_1.Add(FlagEnabled(1712))
    AND_1.Add(FlagEnabled(11200596))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    ForceAnimation(character, 7003, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(11205054)
def Event_11205054():
    """Event 11205054"""
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(FlagDisabled(11205055))
    AND_1.Add(FlagEnabled(11205053))
    AND_1.Add(OR_7)
    AND_1.Add(not AND_7)
    AND_1.Add(FlagDisabled(11205050))
    AND_2.Add(FlagDisabled(11205055))
    AND_2.Add(FlagEnabled(11205053))
    AND_2.Add(OR_7)
    AND_2.Add(AND_7)
    OR_6.Add(Attacked(attacked_entity=6380, attacker=PLAYER))
    OR_6.Add(FlagEnabled(11205060))
    OR_6.Add(FlagEnabled(11205061))
    OR_6.Add(FlagEnabled(11205062))
    OR_6.Add(FlagEnabled(11205063))
    OR_6.Add(FlagEnabled(11205064))
    OR_6.Add(FlagEnabled(11205065))
    OR_6.Add(FlagEnabled(11205066))
    OR_6.Add(FlagEnabled(11205067))
    OR_6.Add(FlagEnabled(11205068))
    OR_6.Add(FlagEnabled(745))
    AND_2.Add(OR_6)
    AND_3.Add(FlagDisabled(11205055))
    AND_3.Add(FlagDisabled(11205053))
    AND_3.Add(OR_7)
    AND_3.Add(not AND_7)
    AND_3.Add(FlagEnabled(11205050))
    AND_4.Add(FlagDisabled(11205055))
    AND_4.Add(FlagDisabled(11205053))
    AND_4.Add(OR_7)
    AND_4.Add(AND_7)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    EnableFlag(11205055)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_2)
    EnableFlag(11205051)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_3)
    EnableFlag(11205052)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_4)
    EnableFlag(11205052)
    Restart()


@RestartOnRest(11205056)
def Event_11205056():
    """Event 11205056"""
    AND_7.Add(PlayerCovenant(Covenant.ForestHunter))
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(FlagEnabled(11205051))
    AND_1.Add(OR_7)
    AND_1.Add(AND_7)
    AND_2.Add(FlagEnabled(11205051))
    AND_2.Add(OR_7)
    AND_2.Add(not AND_7)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisableFlag(11205051)
    DisableFlag(11205053)
    SkipLinesIfFinishedConditionTrue(9, input_condition=AND_2)
    OR_6.Add(CharacterHuman(PLAYER))
    OR_6.Add(CharacterHollow(PLAYER))
    SkipLinesIfConditionFalse(3, OR_6)
    BetrayCurrentCovenant()
    if FlagDisabled(9001):
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
    MAIN.Await(FlagEnabled(11205052))
    
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


@ContinueOnRest(11205058)
def Event_11205058():
    """Event 11205058"""
    if FlagEnabled(11205053):
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
def Event_11205060(_, character: int):
    """Event 11205060"""
    if FlagEnabled(746):
        SetTeamType(character, TeamType.Enemy)
    OR_7.Add(CharacterHuman(PLAYER))
    OR_7.Add(CharacterHollow(PLAYER))
    AND_1.Add(OR_7)
    AND_1.Add(PlayerCovenant(Covenant.ForestHunter))
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(HealthRatio(character) <= 0.8999999761581421)
    
    MAIN.Await(AND_1)
    
    End()


@ContinueOnRest(11205030)
def Event_11205030():
    """Event 11205030"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6521, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11205033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11205031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6521)
    if FlagEnabled(11200900):
        return
    AND_1.Add(Host())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(6521))
    AND_1.Add(EntityWithinDistance(entity=6521, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6521,
        region=1202010,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


@ContinueOnRest(11205035)
def Event_11205035():
    """Event 11205035"""
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6521, authority_level=UpdateAuthority.Forced)
    SkipLinesIfFlagEnabled(3, 11205033)
    AND_2.Add(Client())
    AND_2.Add(FlagEnabled(11205031))
    SkipLinesIfConditionTrue(1, AND_2)
    DisableCharacter(6521)
    if FlagEnabled(11200900):
        return
    If_Unknown_3_24(AND_1, unk1=4, unk2=3)
    AND_1.Add(Host())
    AND_1.Add(FlagDisabled(11205031))
    AND_1.Add(FlagDisabled(11205033))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterBackreadEnabled(6521))
    AND_1.Add(EntityWithinDistance(entity=6521, other_entity=PLAYER, radius=10.0))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 28))
    
    MAIN.Await(AND_1)
    
    PlaceSummonSign(
        sign_type=SummonSignType.BlueEyeSign,
        character=6521,
        region=1202010,
        summon_flag=11205031,
        dismissal_flag=11205033,
    )


@ContinueOnRest(11205990)
def Event_11205990(_, flag: int, summoned_character: int):
    """Event 11205990"""
    MAIN.Await(FlagEnabled(flag))
    
    EraseNPCSummonSign(summoned_character=summoned_character)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(11205032)
def Event_11205032():
    """Event 11205032"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(11205031))
    AND_1.Add(FlagEnabled(11205383))
    
    MAIN.Await(AND_1)
    
    AICommand(6521, command_id=10, command_slot=0)
    ReplanAI(6521)
    
    MAIN.Await(CharacterInsideRegion(6521, region=1202898))
    
    RotateToFaceEntity(6521, target_entity=1202894)
    ForceAnimation(6521, 7410)
    AICommand(6521, command_id=-1, command_slot=0)
    ReplanAI(6521)


@ContinueOnRest(11200300)
def Event_11200300():
    """Event 11200300"""
    MAIN.Await(FlagEnabled(11205031))
    
    EnableFlag(11200300)


@ContinueOnRest(11200005)
def Event_11200005():
    """Event 11200005"""
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    OR_1.Add(FlagEnabled(1127))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    AND_1.Add(FlagDisabled(17))
    
    MAIN.Await(AND_1)
    
    if Client():
        return
    
    MAIN.Await(Singleplayer())
    
    CreateVFX(1202009)
    
    MAIN.Await(Multiplayer())
    
    DeleteVFX(1202009)
    Restart()


@ContinueOnRest(11200006)
def Event_11200006():
    """Event 11200006"""
    OR_1.Add(FlagEnabled(1125))
    OR_1.Add(FlagEnabled(1126))
    OR_1.Add(FlagEnabled(1127))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerHasGood(2520))
    AND_1.Add(FlagDisabled(17))
    AND_1.Add(Singleplayer())
    AND_1.Add(ActionButton(
        prompt_text=10010100,
        anchor_entity=1202008,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    if Client():
        return
    PlayCutscene(120002, cutscene_flags=0, player_id=10000, move_to_region=1212510, game_map=OOLACILE)
    WaitFrames(frames=1)
    SaveRequest()
    Restart()


@ContinueOnRest(11205843)
def Event_11205843(_, flag: int, line_intersects: int, anchor_entity: int, target_entity: int):
    """Event 11205843"""
    AND_1.Add(Host())
    AND_1.Add(Multiplayer())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(ActionButton(
        prompt_text=10010403,
        anchor_entity=anchor_entity,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
        boss_version=True,
        line_intersects=line_intersects,
    ))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity=target_entity)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Unknown_2003_47()
    Restart()


@ContinueOnRest(11205846)
def Event_11205846(_, flag: int, obj: int, vfx_id: int):
    """Event 11205846"""
    OR_1.Add(Multiplayer())
    OR_1.Add(UnknownPlayerType5())
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableObject(obj)
    CreateVFX(vfx_id)
    AND_3.Add(UnknownPlayerType5())
    AND_2.Add(not AND_3)
    AND_2.Add(Singleplayer())
    
    MAIN.Await(AND_2)
    
    DisableObject(obj)
    DeleteVFX(vfx_id)
    Restart()
