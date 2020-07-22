from soulstruct.events.darksouls1 import *
from soulstruct.game_types import *
from .example_constants import *

DOOR_INACTIVE_DELAY = 2.0

def CONSTRUCTOR():
    """ 0: Constructor run on map load. """
    PullOutMeltedIronKey()
    DespawnChanneler(0, CHARACTERS.DepthsChanneler)
    SlimeAmbush(0, 1002100, 1002110, 1000100, 0.0)
    SlimeAmbush(1, 1002101, 1002112, 1000101, 0.5)
    for slot, trigger_region_1, trigger_region_2, slime, fall_delay in zip(
            (2, 3, 4),  # slot
            (2, 2, 2),  # trigger_region_1
            (3, 3, 3),  # trigger_region_2
            (2, 3, 4),  # slime
            (0.4, 0.2, 0.2)  # fall_delay
    ):
        SlimeAmbush(slot, 1002100 + trigger_region_1, 1002110 + trigger_region_2, 1000100 + slime, fall_delay)


def PullOutMeltedIronKey():
    """ MeltedIronKeyReceived 11000112: Inspect door to Depths from Blighttown and pull out Melted Iron Key. """
    if THIS_FLAG:
        return
    DisableObjectActivation(OBJECTS.DepthsDoor, -1)
    Await(ActionButton(TEXT.Open, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                       model_point=100, max_distance=1.5))
    DisplayDialog(TEXT.SomethingInDoor, anchor_entity=OBJECTS.DepthsDoor)
    Wait(1.0)
    await ActionButton(TEXT.RemoveItemFromDoor, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                       model_point=100, max_distance=1.5)
    AwardItemLot(ITEMLOT.InDepthsDoor)
    Wait(DOOR_INACTIVE_DELAY)
    EnableObjectActivation(OBJECTS.DepthsDoor, -1)


@RestartOnRest
def DespawnChanneler(channeler: int):
    """ 11000860: Channeler appears until you have been to the Painted World. """
    if not FLAGS.PaintedWorldVisited:
        return
    Await(InsideMap(DEPTHS))
    DisableCharacter(channeler)
    Kill(channeler)


@RestartOnRest
def SlimeAmbush(trigger_region_1: Region, trigger_region_2: Region, slime: Character, delay: float):
    """ 11005100: Slime ambushes. Now takes two region triggers rather than one. """
    if not THIS_SLOT_FLAG:
        DisableGravity(slime)
        DisableCollision(slime)
        if trigger_region_2 == 0:
            Await(trigger_region_1 or IsAttacked(slime, PLAYER))
        else:
            Await(trigger_region_1 or trigger_region_2 or IsAttacked(slime, PLAYER))
        Wait(delay)

    EnableGravity(slime)
    EnableCollision(slime)
    ResetStandbyAnimationSettings(slime)
