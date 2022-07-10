"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    Event_11400000()
    Event_11402000()
    Event_11405500(0, 1400000, 3.0, 9060)
    Event_11405500(1, 1400001, 3.0, 9060)
    Event_11405500(2, 1400002, 3.0, 9060)
    Event_11405500(3, 1400003, 3.0, 9060)
    Event_11405500(4, 1400006, 3.0, 3000)
    Event_11405500(5, 1400007, 3.0, 3000)
    Event_11405500(6, 1400008, 5.0, 9060)
    Event_11405500(7, 1400009, 3.0, 9060)
    Event_11405500(8, 1400014, 3.0, 3001)
    Event_11405500(9, 1400016, 3.0, 9060)
    Event_11405500(10, 1400019, 3.0, 9060)
    Event_11405500(11, 1400020, 3.0, 9060)
    Event_11405500(12, 1400021, 3.0, 9060)
    Event_11405500(13, 1400022, 3.0, 9060)
    Event_11405500(14, 1400024, 3.0, 9060)
    Event_11405500(15, 1400025, 3.0, 200)
    Event_11405500(16, 1400026, 8.0, 200)
    Event_11405500(17, 1400027, 4.0, 9060)
    Event_11405500(18, 1400028, 3.0, 9060)
    Event_11405500(19, 1400030, 2.0, 3002)
    Event_11405500(20, 1400031, 3.0, 3006)
    Event_11405500(21, 1400033, 3.0, 3005)
    Event_11405500(22, 1400034, 3.0, 9060)
    Event_11405500(23, 1400035, 3.0, 3000)
    Event_11405500(24, 1400036, 3.0, 9060)
    Event_11405500(25, 1400037, 3.0, 9060)
    Event_11405500(26, 1400038, 3.0, 9060)
    Event_11405500(27, 1400041, 3.0, 3006)
    Event_11405500(28, 1400042, 3.0, 3002)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Wait(0.10000000149011612)


@NeverRestart(11400000)
def Event_11400000():
    """Event 11400000"""
    RegisterBonfire(bonfire_flag=11400992, obj=1401960)
    RegisterBonfire(bonfire_flag=11400984, obj=1401961)
    RegisterBonfire(bonfire_flag=11400976, obj=1401962)
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=1401140)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=1401141)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=1401142)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=1401143)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=1401144)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=1401145)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=1401146)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=1401147)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=1401148)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=1401149)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=1401150)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=1401151)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=1401152)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=1401153)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=1401154)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=1401155)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=1401156)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=1401157)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=1401158)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=1401159)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=1401160)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=1401161)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=1401162)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=1401163)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=1401164)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=1401165)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=1401166)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=1401167)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=1401168)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=1401169)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=1401170)
    Event_11405100(0, entity=1401000, region=1402000, region_1=1402001, region_2=1402002)
    Event_11405110(0, 1401002, 1402006, 1402007, 1402008, 1402009, 1402010)


@NeverRestart(11405100)
def Event_11405100(_, entity: int, region: int, region_1: int, region_2: int):
    """Event 11405100"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@NeverRestart(11405110)
def Event_11405110(_, entity: int, region: int, region_1: int, region_2: int, region_3: int, region_4: int):
    """Event 11405110"""
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_3))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableNetworkSync()
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_1))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_2))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_3))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=region_4))
    
    MAIN.Await(AND_1)
    
    EnableNetworkSync()
    Restart()


@NeverRestart(11402000)
def Event_11402000():
    """Event 11402000"""
    Wait(3.0)
    
    MAIN.Await(ActionButton(
        prompt_text=10012010,
        anchor_entity=1402011,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.Human | TriggerAttribute.Hollow,
    ))
    
    RotateToFaceEntity(PLAYER, target_entity=1402500)
    ForceAnimation(PLAYER, 7522)
    Wait(1.0)
    EnableFlag(11813007)
    WarpToMap(game_map=PAINTED_WORLD, player_start=1100987)


@NeverRestart(11405500)
def Event_11405500(_, character: int, radius: float, cancel_animation: int):
    """Event 11405500"""
    DisableAI(character)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_2)
    SetStandbyAnimationSettings(character, cancel_animation=cancel_animation)
    SkipLines(1)
    ResetStandbyAnimationSettings(character)
    EnableAI(character)
