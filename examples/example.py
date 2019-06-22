""" EVS example.

See 'example_with_comments.py' in the same folder for an identical version of the script that has been extensively
documented throughout by me.
"""

from soulstruct.emevd.ds1 import *
from .example_constants import *


def CONSTRUCTOR():
    """ 0: Constructor run on map load. """
    PullOutMeltedIronKey()
    DespawnChanneler(0, CHARACTERS.DepthsChanneler)
    SlimeAmbush(0, 1002100, 1002110, 1000100, 0.0)
    SlimeAmbush(1, 1002101, 1002112, 1000101, 0.5)
    SlimeAmbush(2, 1002102, 1002113, 1000102, 0.4)
    SlimeAmbush(3, 1002102, 1002113, 1000103, 0.2)


def PullOutMeltedIronKey():
    """ MeltedIronKeyReceived 11000112: Inspect door to Depths from Blighttown and pull out Melted Iron Key. """
    if THIS_FLAG:
        return
    DisableObjectActivation(OBJECTS.DepthsDoor, -1)
    await DialogPromptActivated(TEXT.Open, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                                model_point=100, max_distance=1.5)
    DisplayDialog(TEXT.SomethingInDoor, anchor_entity=OBJECTS.DepthsDoor)
    Wait(1.0)
    await DialogPromptActivated(TEXT.RemoveItemFromDoor, anchor_entity=OBJECTS.DepthsDoor, facing_angle=60.0,
                                model_point=100, max_distance=1.5)
    AwardItemLot(ITEMLOT.InDepthsDoor)
    Wait(2.0)
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
            await (trigger_region_1 or IsAttacked(slime, PLAYER))
        else:
            await (trigger_region_1 or trigger_region_2 or IsAttacked(slime, PLAYER))
        Wait(delay)
    EnableGravity(slime)
    EnableCollision(slime)
    ResetStandbyAnimationSettings(slime)
