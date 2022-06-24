from soulstruct.darksouls1r.events import *
from soulstruct.darksouls1r.events.instructions import *
from soulstruct.darksouls1r.game_types import *

from example_constants import *

DOOR_INACTIVE_DELAY = 2.0


def Constructor():
    """ 0: Constructor run on map load. """
    PullOutMeltedIronKey()
    DespawnChanneler(0, Characters.DepthsChanneler)
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
    """ 11000112: Inspect door to Depths from Blighttown and pull out Melted Iron Key. """
    if THIS_FLAG:
        return
    DisableObjectActivation(Objects.DepthsDoor, -1)
    Await(
        ActionButton(
            EventTexts.Open, anchor_entity=Objects.DepthsDoor, facing_angle=60.0, model_point=100, max_distance=1.5
        )
    )
    DisplayDialog(EventTexts.SomethingInDoor, anchor_entity=Objects.DepthsDoor)
    Wait(1.0)
    await ActionButton(
        EventTexts.RemoveItemFromDoor, anchor_entity=Objects.DepthsDoor, facing_angle=60.0, model_point=100, max_distance=1.5
    )
    AwardItemLot(ItemLots.InDepthsDoor)
    Wait(DOOR_INACTIVE_DELAY)
    EnableObjectActivation(Objects.DepthsDoor, -1)


@RestartOnRest
def DespawnChanneler(channeler: int):
    """ 11000860: Channeler appears until you have been to the Painted World. """
    if not Flags.PaintedWorldVisited:
        return
    Await(InsideMap(DEPTHS))
    DisableCharacter(channeler)
    Kill(channeler)


@RestartOnRest
def SlimeAmbush(trigger_region_1: Region, trigger_region_2: Region, slime: Character, delay: float):
    """ 11005100: Slime ambushes. Now takes two region triggers rather than one. """
    if not THIS_SLOT_FLAG:
        DisableGravity(slime)
        DisableMapCollision(slime)
        if trigger_region_2 == 0:
            Await(trigger_region_1 or IsAttacked(slime, PLAYER))
        else:
            Await(trigger_region_1 or trigger_region_2 or IsAttacked(slime, PLAYER))
        Wait(delay)

    EnableGravity(slime)
    EnableMapCollision(slime)
    ResetStandbyAnimationSettings(slime)
