"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11310000()
    Event_11315100()
    Event_11312500()
    Event_11315396()
    Event_11315397()
    Event_11315398()
    Event_11315380(
        0,
        character=1310000,
        flag=11315366,
        first_flag=11315330,
        flag_1=11315331,
        flag_2=11315332,
        flag_3=11315333,
        flag_4=11315334,
        last_flag=11315335
    )
    Event_11315383(0, character=1310000, flag=11315366, flag_1=11315336)
    Event_11315386(0, character=1310000)
    Event_11315380(
        1,
        character=1310001,
        flag=11315367,
        first_flag=11315340,
        flag_1=11315341,
        flag_2=11315342,
        flag_3=11315343,
        flag_4=11315344,
        last_flag=11315345
    )
    Event_11315383(1, character=1310001, flag=11315367, flag_1=11315346)
    Event_11315386(1, character=1310001)
    Event_11315380(
        2,
        character=1310002,
        flag=11315368,
        first_flag=11315350,
        flag_1=11315351,
        flag_2=11315352,
        flag_3=11315353,
        flag_4=11315354,
        last_flag=11315355
    )
    Event_11315383(2, character=1310002, flag=11315368, flag_1=11315356)
    Event_11315386(2, character=1310002)
    Event_11315390(0, 1310000, 11315330, 11315335, 11315366, 11315336, 0, 15.0, 11315393, 0.800000011920929)
    Event_11315390(1, 1310001, 11315340, 11315345, 11315367, 11315346, 1, 15.0, 11315394, 0.6499999761581421)
    Event_11315390(2, 1310002, 11315350, 11315355, 11315368, 11315356, 2, 15.0, 11315395, 0.4000000059604645)
    Event_11312510(
        0,
        flag=11312520,
        flag_1=11312500,
        obj=1311020,
        character=1310017,
        item_lot_param_id=15040,
        item_lot_param_id_1=16040
    )
    Event_11315510(0, 1311020, 11312500, 11312520, 22680, 1.2000000476837158)
    Event_11312000()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11310000)
def Event_11310000():
    """Event 11310000"""
    RegisterBonfire(bonfire_flag=11310992, obj=1311960)
    RegisterLadder(start_climbing_flag=11310010, stop_climbing_flag=11310011, obj=1311000)
    RegisterLadder(start_climbing_flag=11310012, stop_climbing_flag=11310013, obj=1311001)
    RegisterLadder(start_climbing_flag=11310014, stop_climbing_flag=11310015, obj=1311002)
    RegisterLadder(start_climbing_flag=11310016, stop_climbing_flag=11310017, obj=1311003)
    RegisterLadder(start_climbing_flag=11310018, stop_climbing_flag=11310019, obj=1311004)
    RegisterLadder(start_climbing_flag=11310020, stop_climbing_flag=11310021, obj=1311005)
    RegisterLadder(start_climbing_flag=11310022, stop_climbing_flag=11310023, obj=1311006)
    RegisterLadder(start_climbing_flag=11310026, stop_climbing_flag=11310027, obj=1311007)
    DisableObject(1311008)
    DisableObjectActivation(1311008, obj_act_id=-1)
    Event_11310100()


@RestartOnRest(11315100)
def Event_11315100():
    """Event 11315100"""
    Event_11315091()
    Event_11315092()
    Event_11315150(0, flag=11315100, vfx_id=1313200, flag_1=11315101)
    Event_11315150(1, flag=11315101, vfx_id=1313201, flag_1=11315102)
    Event_11315150(2, flag=11315102, vfx_id=1313202, flag_1=11315103)
    Event_11315150(3, flag=11315103, vfx_id=1313203, flag_1=11315104)
    Event_11315150(4, flag=11315104, vfx_id=1313204, flag_1=11315105)
    Event_11315150(5, flag=11315105, vfx_id=1313205, flag_1=11315106)
    Event_11315150(6, flag=11315106, vfx_id=1313206, flag_1=11315107)
    Event_11315150(7, flag=11315107, vfx_id=1313207, flag_1=11315108)
    Event_11315150(8, flag=11315108, vfx_id=1313208, flag_1=11315109)
    Event_11315150(9, flag=11315109, vfx_id=1313209, flag_1=11315110)
    Event_11315150(10, flag=11315110, vfx_id=1313210, flag_1=11315111)
    Event_11315150(11, flag=11315111, vfx_id=1313211, flag_1=11315112)
    Event_11315150(12, flag=11315112, vfx_id=1313212, flag_1=11315113)
    Event_11315150(13, flag=11315113, vfx_id=1313213, flag_1=11315114)
    Event_11315150(14, flag=11315114, vfx_id=1313214, flag_1=11315115)
    Event_11315150(15, flag=11315115, vfx_id=1313215, flag_1=11315116)
    Event_11315150(16, flag=11315116, vfx_id=1313216, flag_1=11315117)
    Event_11315150(17, flag=11315117, vfx_id=1313217, flag_1=11315118)
    Event_11315150(18, flag=11315118, vfx_id=1313218, flag_1=11315119)
    Event_11315150(19, flag=11315119, vfx_id=1313219, flag_1=11315120)
    Event_11315150(20, flag=11315120, vfx_id=1313220, flag_1=11315121)
    Event_11315150(21, flag=11315121, vfx_id=1313221, flag_1=11315122)
    Event_11315150(22, flag=11315122, vfx_id=1313222, flag_1=11315123)
    Event_11315150(23, flag=11315123, vfx_id=1313223, flag_1=11315124)
    Event_11315150(24, flag=11315124, vfx_id=1313224, flag_1=11315125)
    Event_11315150(25, flag=11315125, vfx_id=1313225, flag_1=11315126)
    Event_11315150(26, flag=11315126, vfx_id=1313226, flag_1=11315127)
    Event_11315150(27, flag=11315127, vfx_id=1313227, flag_1=11315128)
    Event_11315150(28, flag=11315128, vfx_id=1313228, flag_1=11315129)
    Event_11315150(29, flag=11315129, vfx_id=1313229, flag_1=11315130)
    Event_11315150(30, flag=11315130, vfx_id=1313230, flag_1=11315131)
    Event_11315150(31, flag=11315131, vfx_id=1313231, flag_1=11315132)
    Event_11315150(32, flag=11315132, vfx_id=1313232, flag_1=11315133)
    Event_11315150(33, flag=11315133, vfx_id=1313233, flag_1=11315134)
    Event_11315150(34, flag=11315134, vfx_id=1313234, flag_1=11315135)
    Event_11315150(35, flag=11315135, vfx_id=1313235, flag_1=11315136)
    Event_11315150(36, flag=11315136, vfx_id=1313236, flag_1=11315137)
    Event_11315150(37, flag=11315137, vfx_id=1313237, flag_1=11315138)
    Event_11315150(38, flag=11315138, vfx_id=1313238, flag_1=11315139)
    Event_11315150(39, flag=11315139, vfx_id=1313239, flag_1=11315140)
    Event_11315150(40, flag=11315140, vfx_id=1313240, flag_1=11315141)
    Event_11315150(41, flag=11315141, vfx_id=1313241, flag_1=11315142)
    Event_11315150(42, flag=11315142, vfx_id=1313242, flag_1=11315143)
    Event_11315150(43, flag=11315143, vfx_id=1313243, flag_1=11315144)
    Event_11315150(44, flag=11315144, vfx_id=1313244, flag_1=11315145)
    Event_11315150(45, flag=11315145, vfx_id=1313245, flag_1=11315146)
    Event_11315150(46, flag=11315146, vfx_id=1313246, flag_1=11315147)
    Event_11315150(47, flag=11315147, vfx_id=1313247, flag_1=11315148)
    Event_11315150(48, 11315148, 1313248, 11315149)


@UnknownRestart(11315150)
def Event_11315150(_, flag: int, vfx_id: int, flag_1: int):
    """Event 11315150"""
    if FlagDisabled(11315090):
        DeleteVFX(vfx_id, erase_root_only=False)
        AND_1.Add(FlagEnabled(11315090))
        AND_1.Add(FlagEnabled(flag))
    
        MAIN.Await(AND_1)
    CreateVFX(vfx_id)
    EnableFlag(flag_1)
    
    MAIN.Await(FlagDisabled(11315090))
    
    DeleteVFX(vfx_id)
    DisableFlag(flag_1)
    Restart()


@UnknownRestart(11315091)
def Event_11315091():
    """Event 11315091"""
    AND_1.Add(SkullLanternActive())
    AND_1.Add(TimeElapsed(seconds=2.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11315090)
    RestartEvent(event_id=11315092)
    Restart()


@UnknownRestart(11315092)
def Event_11315092():
    """Event 11315092"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(11315090))
    
    Wait(3.0)
    DisableFlag(11315090)
    Restart()


@NeverRestart(11310100)
def Event_11310100():
    """Event 11310100"""
    if ThisEventFlagEnabled():
        DisableObject(1311009)
        End()
    
    MAIN.Await(ObjectDestroyed(1311009))
    
    End()


@NeverRestart(11312000)
def Event_11312000():
    """Event 11312000"""
    AND_1.Add(InsideMap(game_map=UNDEAD_BURG))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=1312009))
    
    MAIN.Await(AND_1)
    
    DisableMapCollision(collision=1313203)
    DisableMapCollision(collision=1313204)
    DisableMapCollision(collision=1313205)
    DisableMapCollision(collision=1313206)
    DisableMapCollision(collision=1313207)
    OR_1.Add(InsideMap(game_map=TOMB_OF_THE_GIANTS))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=1312009))
    
    MAIN.Await(OR_1)
    
    EnableMapCollision(collision=1313203)
    EnableMapCollision(collision=1313204)
    EnableMapCollision(collision=1313205)
    EnableMapCollision(collision=1313206)
    EnableMapCollision(collision=1313207)
    Restart()


@RestartOnRest(11312500)
def Event_11312500():
    """Event 11312500"""
    DisableSoundEvent(sound_id=1313800)
    DisableGravity(1310017)
    DisableCharacterCollision(1310017)
    DisableCharacter(1310017)
    if ThisEventFlagEnabled():
        Kill(1310017)
        DisableCharacter(1310000)
        Kill(1310000)
        DisableCharacter(1310001)
        Kill(1310001)
        DisableCharacter(1310002)
        Kill(1310002)
        DisableCharacter(1310003)
        Kill(1310003)
        DisableCharacter(1310004)
        Kill(1310004)
        DisableCharacter(1310005)
        Kill(1310005)
        DisableCharacter(1310006)
        Kill(1310006)
        DisableCharacter(1310007)
        Kill(1310007)
        DisableCharacter(1310008)
        Kill(1310008)
        DisableCharacter(1310009)
        Kill(1310009)
        DisableCharacter(1310010)
        Kill(1310010)
        End()
    DisableGravity(1310003)
    DisableCharacterCollision(1310003)
    EnableInvincibility(1310003)
    DisableGravity(1310004)
    DisableCharacterCollision(1310004)
    EnableInvincibility(1310004)
    DisableGravity(1310005)
    DisableCharacterCollision(1310005)
    EnableInvincibility(1310005)
    DisableGravity(1310006)
    DisableCharacterCollision(1310006)
    EnableInvincibility(1310006)
    DisableGravity(1310007)
    DisableCharacterCollision(1310007)
    EnableInvincibility(1310007)
    DisableGravity(1310008)
    DisableCharacterCollision(1310008)
    EnableInvincibility(1310008)
    DisableGravity(1310009)
    DisableCharacterCollision(1310009)
    EnableInvincibility(1310009)
    DisableGravity(1310010)
    DisableCharacterCollision(1310010)
    EnableInvincibility(1310010)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1312010))
    
    ForceAnimation(1310000, 3008)
    WaitRandomSeconds(min_seconds=0.019999999552965164, max_seconds=0.07999999821186066)
    ForceAnimation(1310001, 3008)
    WaitRandomSeconds(min_seconds=0.019999999552965164, max_seconds=0.07999999821186066)
    ForceAnimation(1310002, 3008)
    Wait(3.799999952316284)
    DisableCharacter(1310000)
    DisableCharacter(1310001)
    DisableCharacter(1310002)
    ForceAnimation(1310003, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310004, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310005, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310006, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310007, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310008, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310009, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    ForceAnimation(1310010, 9061)
    WaitRandomSeconds(min_seconds=0.05000000074505806, max_seconds=0.10000000149011612)
    Wait(1.100000023841858)
    FadeOutCharacter(character=1310003, duration=1.0)
    FadeOutCharacter(character=1310004, duration=1.0)
    FadeOutCharacter(character=1310005, duration=1.0)
    FadeOutCharacter(character=1310006, duration=1.0)
    FadeOutCharacter(character=1310007, duration=1.0)
    FadeOutCharacter(character=1310008, duration=1.0)
    FadeOutCharacter(character=1310009, duration=1.0)
    FadeOutCharacter(character=1310010, duration=1.0)
    EnableCharacter(1310017)
    ForceAnimation(1310017, 1750)
    FadeInCharacter(character=1310017, duration=1.0)
    Wait(0.8999999761581421)
    DisableCharacter(1310003)
    DisableCharacter(1310004)
    DisableCharacter(1310005)
    DisableCharacter(1310006)
    DisableCharacter(1310007)
    DisableCharacter(1310008)
    DisableCharacter(1310009)
    DisableCharacter(1310010)
    EnableBossHealthBar(1310017, name=5220)
    EnableSoundEvent(sound_id=1313800)
    EnableCharacterCollision(1310017)
    EnableGravity(1310017)
    EnableFlag(11315400)
    EnableFlag(11315366)
    EnableFlag(11315367)
    EnableFlag(11315368)
    
    MAIN.Await(CharacterDead(1310017))
    
    DisableBossHealthBar(1310017)
    DisableSoundEvent(sound_id=1313800)
    PlaySoundEffect(PLAYER, 777777777, sound_type=SoundType.s_SFX)


@NeverRestart(11315390)
def Event_11315390(
    _,
    character: int,
    first_flag: int,
    last_flag: int,
    flag: int,
    flag_1: int,
    event_slot: int,
    seconds: float,
    flag_2: int,
    value: float,
):
    """Event 11315390"""
    if FlagEnabled(11312500):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(1310017, value=value))
    
    Wait(seconds)
    OR_7.Add(CharacterDead(character))
    SkipLinesIfConditionFalse(1, OR_7)
    End()
    AND_1.Add(FlagDisabled(11315393))
    AND_1.Add(FlagDisabled(11315394))
    AND_1.Add(FlagDisabled(11315395))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag_2)
    if FlagEnabled(flag_1):
        AICommand(character, command_id=1, command_slot=0)
    
        MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=600))
    
        AICommand(character, command_id=0, command_slot=0)
    DisableCharacter(character)
    WaitFrames(frames=2)
    MoveToEntity(character, destination=1310017, model_point=230, destination_type=CoordEntityType.Character)
    WaitFrames(frames=2)
    EnableCharacter(character)
    ForceAnimation(character, 7000, wait_for_completion=True)
    ForceAnimation(character, 3008, wait_for_completion=True)
    DisableCharacter(character)
    DisableFlagRange((first_flag, last_flag))
    WaitFrames(frames=2)
    EnableFlag(flag)
    RestartEvent(event_id=11315383, event_slot=event_slot)
    AddSpecialEffect(1310017, 3001)
    Wait(4.0)
    DisableFlag(flag_2)
    Restart()


@RestartOnRest(11315396)
def Event_11315396():
    """Event 11315396"""
    DisableObject(1311011)
    DisableObject(1311012)
    DisableObject(1311013)
    DisableCharacter(1310011)
    DisableCharacter(1310012)
    DisableCharacter(1310013)
    DisableCharacter(1310014)
    DisableCharacter(1310015)
    DisableCharacter(1310016)
    if FlagEnabled(11312500):
        Kill(1310011)
        Kill(1310012)
        Kill(1310013)
        Kill(1310014)
        Kill(1310015)
        Kill(1310016)
        End()
    Event_11315320(0, character=1310011, obj=1311014)
    Event_11315320(1, character=1310012, obj=1311015)
    Event_11315320(2, character=1310013, obj=1311016)
    Event_11315320(3, character=1310014, obj=1311017)
    Event_11315320(4, character=1310015, obj=1311018)
    Event_11315320(5, character=1310016, obj=1311019)
    Event_11315370(0, 11315373, 0.800000011920929, 1311011, 1310011, 1310012, 8000)
    Event_11315370(1, 11315374, 0.6499999761581421, 1311012, 1310013, 1310014, 8010)
    Event_11315370(2, 11315375, 0.5, 1311013, 1310015, 1310016, 8020)
    Event_11315376(0, 11315373, 0.800000011920929, 1310011, 1310012)
    Event_11315376(1, 11315374, 0.6499999761581421, 1310013, 1310014)
    Event_11315376(2, 11315375, 0.5, 1310015, 1310016)
    
    MAIN.Await(CharacterBackreadEnabled(1310017))
    
    SetDisplayMask(1310017, bit_index=0, switch_type=OnOffChange.On)


@UnknownRestart(11315370)
def Event_11315370(_, left: int, value: float, obj: int, character: int, character_1: int, animation_id: int):
    """Event 11315370"""
    MAIN.Await(FlagDisabled(left))
    
    AND_1.Add(HealthRatioGreaterThan(1310017, value=0.0))
    AND_1.Add(HealthRatioLessThan(1310017, value=value))
    AND_2.Add(HealthRatioLessThanOrEqual(1310017, value=0.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    SkipLinesIfValueNotEqual(5, left=left, right=11315373)
    SetCollisionMask(1310017, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=4, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=7, switch_type=OnOffChange.On)
    SkipLines(11)
    SkipLinesIfValueNotEqual(5, left=left, right=11315374)
    SetCollisionMask(1310017, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=5, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=8, switch_type=OnOffChange.On)
    SkipLines(5)
    if ValueEqual(left=left, right=11315375):
        SetCollisionMask(1310017, bit_index=3, switch_type=OnOffChange.Off)
        SetDisplayMask(1310017, bit_index=3, switch_type=OnOffChange.On)
        SetDisplayMask(1310017, bit_index=6, switch_type=OnOffChange.On)
        SetDisplayMask(1310017, bit_index=9, switch_type=OnOffChange.On)
    EnableObject(obj)
    RestoreObject(obj)
    MoveObjectToCharacter(obj, character=1310017, model_point=50)
    DestroyObject(obj)
    EnableCharacter(character)
    FadeInCharacter(character=character, duration=0.10000000149011612)
    Move(
        character,
        destination=1310017,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=1310017,
    )
    ForceAnimation(character, 7000)
    EnableCharacter(character_1)
    FadeInCharacter(character=character_1, duration=0.10000000149011612)
    Move(
        character_1,
        destination=1310017,
        destination_type=CoordEntityType.Character,
        model_point=51,
        copy_draw_parent=1310017,
    )
    ForceAnimation(character_1, 7000)
    ForceAnimation(1310017, animation_id, wait_for_completion=True)
    Wait(3.0)
    EnableFlag(left)
    Restart()


@UnknownRestart(11315376)
def Event_11315376(_, left: int, value: float, character: int, character_1: int):
    """Event 11315376"""
    MAIN.Await(FlagEnabled(left))
    
    AND_1.Add(HealthRatioGreaterThan(1310017, value=value))
    AND_2.Add(HealthRatioLessThanOrEqual(1310017, value=0.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    EnableCharacter(character)
    ResetAnimation(character, disable_interpolation=True)
    EnableCharacter(character_1)
    ResetAnimation(character_1, disable_interpolation=True)
    MoveToEntity(character, destination=1310017, model_point=230, destination_type=CoordEntityType.Character)
    MoveToEntity(character_1, destination=1310017, model_point=230, destination_type=CoordEntityType.Character)
    ForceAnimation(character, 9061)
    ForceAnimation(character_1, 9061)
    FadeOutCharacter(character=character, duration=1.5)
    FadeOutCharacter(character=character_1, duration=1.5)
    Wait(1.5)
    DisableCharacter(character)
    DisableCharacter(character_1)
    SkipLinesIfValueNotEqual(5, left=left, right=11315373)
    SetCollisionMask(1310017, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=1, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=4, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=7, switch_type=OnOffChange.Off)
    SkipLines(11)
    SkipLinesIfValueNotEqual(5, left=left, right=11315374)
    SetCollisionMask(1310017, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(1310017, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=5, switch_type=OnOffChange.Off)
    SetDisplayMask(1310017, bit_index=8, switch_type=OnOffChange.Off)
    SkipLines(5)
    if ValueEqual(left=left, right=11315375):
        SetCollisionMask(1310017, bit_index=3, switch_type=OnOffChange.On)
        SetDisplayMask(1310017, bit_index=3, switch_type=OnOffChange.Off)
        SetDisplayMask(1310017, bit_index=6, switch_type=OnOffChange.Off)
        SetDisplayMask(1310017, bit_index=9, switch_type=OnOffChange.Off)
    DisableFlag(left)
    Restart()


@NeverRestart(11315320)
def Event_11315320(_, character: int, obj: int):
    """Event 11315320"""
    if FlagEnabled(11312500):
        return
    EnableImmortality(character)
    
    MAIN.Await(HealthRatioLessThanOrEqual(character, value=0.10000000149011612))
    
    AddSpecialEffect(character, 3000)
    WaitFrames(frames=1)
    EnableObject(obj)
    RestoreObject(obj)
    MoveObjectToCharacter(obj, character=character, model_point=6)
    DestroyObject(obj)
    WaitFrames(frames=1)
    DisableCharacter(character)
    Restart()


@NeverRestart(11315380)
def Event_11315380(
    _,
    character: int,
    flag: int,
    first_flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    last_flag: int,
):
    """Event 11315380"""
    if FlagEnabled(11312500):
        return
    
    MAIN.Await(FlagEnabled(11315400))
    
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(11315369))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11315369)
    DisableFlagRange((11315360, 11315365))
    EnableRandomFlagInRange(flag_range=(11315360, 11315365))
    SkipLinesIfFlagDisabled(8, 11315360)
    SkipLinesIfFlagEnabled(7, 11315330)
    SkipLinesIfFlagEnabled(6, 11315340)
    SkipLinesIfFlagEnabled(5, 11315350)
    MoveToEntity(character, destination=1312003, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312003)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(first_flag)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(8, 11315361)
    SkipLinesIfFlagEnabled(7, 11315331)
    SkipLinesIfFlagEnabled(6, 11315341)
    SkipLinesIfFlagEnabled(5, 11315351)
    MoveToEntity(character, destination=1312004, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312004)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(8, 11315362)
    SkipLinesIfFlagEnabled(7, 11315332)
    SkipLinesIfFlagEnabled(6, 11315342)
    SkipLinesIfFlagEnabled(5, 11315352)
    MoveToEntity(character, destination=1312005, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312005)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_2)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(8, 11315363)
    SkipLinesIfFlagEnabled(7, 11315333)
    SkipLinesIfFlagEnabled(6, 11315343)
    SkipLinesIfFlagEnabled(5, 11315353)
    MoveToEntity(character, destination=1312006, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312006)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_3)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(8, 11315364)
    SkipLinesIfFlagEnabled(7, 11315334)
    SkipLinesIfFlagEnabled(6, 11315344)
    SkipLinesIfFlagEnabled(5, 11315354)
    MoveToEntity(character, destination=1312007, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312007)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_4)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(8, 11315365)
    SkipLinesIfFlagEnabled(7, 11315335)
    SkipLinesIfFlagEnabled(6, 11315345)
    SkipLinesIfFlagEnabled(5, 11315355)
    MoveToEntity(character, destination=1312008, destination_type=CoordEntityType.Region)
    SetNest(character, region=1312008)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(last_flag)
    DisableFlag(flag)
    DisableFlag(11315369)
    Restart()


@NeverRestart(11315383)
def Event_11315383(_, character: int, flag: int, flag_1: int):
    """Event 11315383"""
    if FlagEnabled(11312500):
        return
    DisableFlag(flag_1)
    
    MAIN.Await(FlagEnabled(11315400))
    
    Wait(5.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    EnableCharacter(character)
    EnableFlag(flag_1)
    ForceAnimation(character, 7000)
    
    MAIN.Await(Attacked(attacked_entity=character, attacker=PLAYER))
    
    AICommand(character, command_id=1, command_slot=0)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=600))
    
    DisableCharacter(character)
    AICommand(character, command_id=0, command_slot=0)
    WaitFrames(frames=2)
    EnableFlag(flag)
    Restart()


@NeverRestart(11315386)
def Event_11315386(_, character: int):
    """Event 11315386"""
    if FlagEnabled(11312500):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(character, value=0.0))
    
    End()


@RestartOnRest(11315397)
def Event_11315397():
    """Event 11315397"""
    AND_1.Add(FlagEnabled(11315400))
    AND_1.Add(CharacterTargeting(targeting_character=1310017, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(1310017, tae_event_id=700))
    
    MAIN.Await(AND_1)
    
    EnableFlag(11313398)
    
    MAIN.Await(CharacterHasTAEEvent(1310017, tae_event_id=710))
    
    EnableFlag(11313399)
    Restart()


@RestartOnRest(11315398)
def Event_11315398():
    """Event 11315398"""
    MAIN.Await(FlagEnabled(11313398))
    
    MoveObjectToCharacter(1311010, character=PLAYER)
    DisableFlag(11313398)
    
    MAIN.Await(FlagEnabled(11313399))
    
    CreateHazard(
        obj_flag=11315399,
        obj=1311010,
        model_point=1,
        behavior_param_id=11300,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.30000001192092896,
        repetition_time=0.0,
    )
    CreateTemporaryVFX(vfx_id=15224, anchor_entity=1311010, anchor_type=CoordEntityType.Object)
    DisableFlag(11313399)
    Restart()


@NeverRestart(11312510)
def Event_11312510(
    _,
    flag: int,
    flag_1: int,
    obj: int,
    character: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
):
    """Event 11312510"""
    DisableObject(obj)
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    EnableObject(obj)
    MoveObjectToCharacter(obj, character=character)
    AND_1.Add(PlayerHasGood(1500))
    AND_1.Add(ActionButton(
        prompt_text=10050000,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_2.Add(PlayerHasGood(1600))
    AND_2.Add(ActionButton(
        prompt_text=10050001,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    AND_3.Add(PlayerDoesNotHaveGood(1500))
    AND_3.Add(PlayerDoesNotHaveGood(1600))
    AND_3.Add(ActionButton(
        prompt_text=10050002,
        anchor_entity=obj,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7522)
    Wait(0.6000000238418579)
    AwardItemLot(item_lot_param_id, host_only=True)
    RemoveGoodFromPlayer(item=1500)
    SkipLines(9)
    SkipLinesIfFinishedConditionFalse(6, input_condition=AND_2)
    RotateToFaceEntity(PLAYER, target_entity=obj)
    ForceAnimation(PLAYER, 7522)
    Wait(0.6000000238418579)
    AwardItemLot(item_lot_param_id_1, host_only=True)
    RemoveGoodFromPlayer(item=1600)
    SkipLines(2)
    DisplayDialog(text=10050003)
    Restart()
    DeleteObjectVFX(obj)
    DisableObject(obj)
    EnableFlag(flag)
    End()


@NeverRestart(11315510)
def Event_11315510(_, obj: int, flag: int, flag_1: int, vfx_id: int, seconds: float):
    """Event 11315510"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    CreateObjectVFX(obj, vfx_id=vfx_id, model_point=1)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=99010, model_point=1)
    Wait(seconds)
    Restart()
