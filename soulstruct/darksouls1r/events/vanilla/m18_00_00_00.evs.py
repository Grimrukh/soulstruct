"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11806100(0, 1800004, 1800010, 40.0, 200)
    Event_11806100(1, 1800005, 1800011, 35.0, 0)
    Event_11806100(2, 1800006, 1800012, 40.0, 0)
    Event_11806100(3, 1800007, 1800013, 50.0, 200)
    Event_11806100(4, 1800008, 1800014, 60.0, 0)
    Event_11806100(5, 1800009, 1800015, 50.0, 200)
    Event_11813101()
    Event_11813102()
    Event_11813103()
    Event_11802003()
    Event_11802004()
    Event_11802005()
    Event_11802006()
    Event_11813104()
    Event_11802009()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@RestartOnRest(11806100)
def Event_11806100(_, character: int, character_1: int, radius: float, animation_id: int):
    """Event 11806100"""
    DisableAI(character)
    DisableCharacter(character)
    DisableCharacter(character_1)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    EnableCharacter(character)
    FadeInCharacter(character=character, duration=2.0)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=20.0))
    
    ForceAnimation(character, animation_id, loop=True)
    Wait(2.0)
    FadeOutCharacter(character=character, duration=1.0)
    EnableCharacter(character_1)
    FadeInCharacter(character=character_1, duration=2.0)
    Wait(1.0)
    DisableCharacter(character)


@RestartOnRest(11813101)
def Event_11813101():
    """Event 11813101"""
    DisableCharacter(1800003)
    EnableInvincibility(1800000)
    if ThisEventFlagEnabled():
        DropMandatoryTreasure(1800002)
        DisableCharacter(1800000)
        End()
    DisableAI(1800002)
    DisableAI(1800000)
    DisableHealthBar(1800002)
    DisableHealthBar(1800000)
    DisableObject(1801002)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802001))
    
    SetRespawnPoint(respawn_point=1803900)
    EnableFlag(11813101)
    SaveRequest()
    ForceAnimation(1800002, 3000)
    Wait(0.4000000059604645)
    ForceAnimation(1800000, 235100)
    ForceAnimation(1800002, 3500)
    Wait(1.5)
    Move(1800002, destination=1802500, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(1800000, 203201)
    ForceAnimation(1800002, 2510)
    Wait(4.5)
    Event_11802001()
    ForceAnimation(1800002, 2520)
    Wait(7.5)
    DropMandatoryTreasure(1800002)
    CreateTemporaryVFX(vfx_id=90014, anchor_entity=1801002, anchor_type=CoordEntityType.Object)
    Wait(2.0)
    EnableObject(1801002)


@NeverRestart(11813102)
def Event_11813102():
    """Event 11813102"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerHasGood(150))
    AND_1.Add(ActionButton(
        prompt_text=10010001,
        anchor_entity=1801002,
        anchor_type=CoordEntityType.Object,
        model_point=-1,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 7522)


@NeverRestart(11813103)
def Event_11813103():
    """Event 11813103"""
    if ThisEventFlagEnabled():
        DisableObject(1801003)
        DeleteVFX(1803400, erase_root_only=False)
        End()
    
    MAIN.Await(FlagEnabled(11813102))
    
    EnableCharacter(1800003)
    DisableHealthBar(1800003)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=1800003, radius=0.5))
    OR_1.Add(Attacked(attacked_entity=1800003, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    Kill(1800003)
    Wait(0.30000001192092896)
    ForceAnimation(PLAYER, 7517, wait_for_completion=True)
    RemoveGoodFromPlayer(item=117)
    AwardItemLot(1000, host_only=True)
    DisableObject(1801003)
    DeleteVFX(1803400)


@NeverRestart(11802001)
def Event_11802001():
    """Event 11802001"""
    DisableObject(1801003)
    DeleteVFX(1803400)
    Wait(0.5)
    RotateToFaceEntity(1800000, target_entity=1802501)
    ForceAnimation(1800000, 500, loop=True)
    Wait(5.5)
    EnableObject(1801003)
    CreateVFX(1803400)
    Wait(3.0)
    RotateToFaceEntity(1800000, target_entity=1802502)
    ForceAnimation(1800000, 500, loop=True)
    Wait(5.0)
    DisableCharacter(1800000)


@NeverRestart(11802003)
def Event_11802003():
    """Event 11802003"""
    if FlagEnabled(11813104):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802003))
    
    PlaySoundEffect(PLAYER, 844001700, sound_type=SoundType.v_Voice)


@NeverRestart(11802004)
def Event_11802004():
    """Event 11802004"""
    if FlagEnabled(11813104):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802004))
    
    PlaySoundEffect(PLAYER, 844001701, sound_type=SoundType.v_Voice)


@NeverRestart(11802005)
def Event_11802005():
    """Event 11802005"""
    if FlagEnabled(11813104):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802005))
    
    PlaySoundEffect(PLAYER, 844001702, sound_type=SoundType.v_Voice)
    Wait(3.9000000953674316)
    PlaySoundEffect(PLAYER, 844001703, sound_type=SoundType.v_Voice)
    Wait(4.699999809265137)
    PlaySoundEffect(PLAYER, 844001704, sound_type=SoundType.v_Voice)


@RestartOnRest(11802006)
def Event_11802006():
    """Event 11802006"""
    DisableCharacter(1800016)
    DisableCharacter(1800017)
    DisableCharacter(1800018)
    DisableCharacter(1800019)
    DisableCharacter(1800020)
    DisableCharacter(1800021)
    DisableCharacter(1800022)
    DisableCharacter(1800023)
    DisableCharacter(1800024)
    DisableCharacter(1800025)
    if FlagEnabled(11813104):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802005))
    
    EnableCharacter(1800016)
    DisableGravity(1800016)
    EnableInvincibility(1800016)
    EnableCharacter(1800017)
    DisableGravity(1800017)
    EnableInvincibility(1800017)
    EnableCharacter(1800018)
    DisableGravity(1800018)
    EnableInvincibility(1800018)
    EnableCharacter(1800019)
    DisableGravity(1800019)
    EnableInvincibility(1800019)
    EnableCharacter(1800020)
    DisableGravity(1800020)
    EnableInvincibility(1800020)
    EnableCharacter(1800021)
    DisableGravity(1800021)
    EnableInvincibility(1800021)
    EnableCharacter(1800022)
    DisableGravity(1800022)
    EnableInvincibility(1800022)
    EnableCharacter(1800023)
    DisableGravity(1800023)
    EnableInvincibility(1800023)
    EnableCharacter(1800024)
    DisableGravity(1800024)
    EnableInvincibility(1800024)
    EnableCharacter(1800025)
    DisableGravity(1800025)
    EnableInvincibility(1800025)
    MoveToEntity(1800000, destination=1802503, destination_type=CoordEntityType.Region)
    EnableCharacter(1800000)
    ForceAnimation(1800000, 200, loop=True)
    Event_11802007()
    Wait(3.0)
    ForceAnimation(1800016, 7005)
    Wait(0.10000000149011612)
    ForceAnimation(1800021, 7005)
    Wait(0.25)
    ForceAnimation(1800017, 7005)
    Wait(0.10000000149011612)
    ForceAnimation(1800022, 7005)
    Wait(0.25)
    ForceAnimation(1800018, 7005)
    Wait(0.05000000074505806)
    ForceAnimation(1800023, 7005)
    Wait(0.15000000596046448)
    ForceAnimation(1800024, 7005)
    Wait(0.10000000149011612)
    ForceAnimation(1800019, 7005)
    Wait(0.20000000298023224)
    ForceAnimation(1800020, 7005)
    Wait(0.10000000149011612)
    ForceAnimation(1800025, 7005)
    Wait(1.0)
    DisableCharacter(1800016)
    DisableCharacter(1800017)
    DisableCharacter(1800018)
    DisableCharacter(1800019)
    DisableCharacter(1800020)
    DisableCharacter(1800021)
    DisableCharacter(1800022)
    DisableCharacter(1800023)
    DisableCharacter(1800024)
    DisableCharacter(1800025)


@NeverRestart(11802007)
def Event_11802007():
    """Event 11802007"""
    Wait(4.0)
    FadeOutCharacter(character=1800000, duration=3.0)
    Wait(3.0)
    DisableCharacter(1800000)


@RestartOnRest(11813104)
def Event_11813104():
    """Event 11813104"""
    DisableSoundEvent(sound_id=1803800)
    DisableGravity(1800026)
    DisableCharacterCollision(1800026)
    DisableCharacter(1800026)
    DisableGravity(1800027)
    DisableCharacterCollision(1800027)
    DisableCharacter(1800027)
    DisableGravity(1800028)
    DisableCharacterCollision(1800028)
    DisableCharacter(1800028)
    DisableGravity(1800029)
    DisableCharacterCollision(1800029)
    DisableCharacter(1800029)
    DisableGravity(1800030)
    DisableCharacterCollision(1800030)
    DisableCharacter(1800030)
    DisableGravity(1800031)
    DisableCharacterCollision(1800031)
    DisableCharacter(1800031)
    DisableGravity(1800032)
    DisableCharacterCollision(1800032)
    DisableCharacter(1800032)
    DisableGravity(1800033)
    DisableCharacterCollision(1800033)
    DisableCharacter(1800033)
    DisableGravity(1800034)
    DisableCharacterCollision(1800034)
    DisableCharacter(1800034)
    DisableGravity(1800035)
    DisableCharacterCollision(1800035)
    DisableCharacter(1800035)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=1802000))
    
    ForceAnimation(1801000, 3)
    EnableSoundEvent(sound_id=1803800)
    DisableMapPiece(map_piece_id=1803000)
    DisableMapCollision(collision=1803200)
    SetCameraVibration(vibration_id=101, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    Wait(0.5)
    Event_11802010(1, 1800027, 800, 3.5, 4.0)
    Event_11802010(2, 1800028, 801, 3.5, 4.0)
    Event_11802010(3, 1800029, 800, 3.5, 9.0)
    Event_11802010(4, 1800030, 801, 3.5, 4.0)
    Event_11802010(5, 1800031, 803, 1.0, 4.0)
    Event_11802010(6, 1800032, 800, 1.0, 4.0)
    Event_11802010(7, 1800033, 801, 1.0, 4.0)
    Event_11802010(8, 1800034, 802, 1.0, 4.0)
    Event_11802010(9, 1800035, 801, 1.0, 4.0)
    Wait(3.0)
    SetCameraVibration(vibration_id=101, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    Wait(2.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    Wait(2.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    SetCameraVibration(vibration_id=200, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=15398, anchor_entity=1800029, model_point=1, anchor_type=CoordEntityType.Character)
    Wait(3.0)
    SetCameraVibration(vibration_id=101, anchor_entity=1802000, anchor_type=CoordEntityType.Region)
    ForceAnimation(PLAYER, 7050, wait_for_completion=True)
    RemoveGoodFromPlayer(item=150)
    AwardItemLot(1010, host_only=True)
    DisplayStatus(900100)
    ForceAnimation(PLAYER, 7052)
    Wait(2.0)
    DropMandatoryTreasure(1800001)
    
    MAIN.Await(FlagEnabled(50000020))
    
    ForceAnimation(1801000, 1)


@NeverRestart(11802009)
def Event_11802009():
    """Event 11802009"""
    if FlagDisabled(11813104):
        EndOfAnimation(obj=1801000, animation_id=1)
        End()
    DisableMapPiece(map_piece_id=1803000)
    DisableMapCollision(collision=1803200)
    EndOfAnimation(obj=1801000, animation_id=2)
    
    MAIN.Await(PlayerStandingOnCollision(1803201))
    
    Wait(2.0)
    ForceAnimation(1801000, 1)


@NeverRestart(11802010)
def Event_11802010(_, character: int, special_effect_id: int, seconds: float, seconds_1: float):
    """Event 11802010"""
    Wait(seconds)
    WaitRandomSeconds(min_seconds=0.20000000298023224, max_seconds=1.0)
    EnableCharacter(character)
    AddSpecialEffect(character, special_effect_id)
    Wait(seconds_1)
    WaitRandomSeconds(min_seconds=0.20000000298023224, max_seconds=1.0)
    Kill(character)
