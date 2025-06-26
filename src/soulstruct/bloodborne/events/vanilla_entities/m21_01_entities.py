from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    12110100: ("InspectDoll", ""),
    12110200: ("OpenChest", ""),
    12110300: ("GetItemFromStorage", ""),
    12110301: ("GetItemFromMemoryAltar", ""),
    12110302: ("GetItemFromOldHunterHeadstone", ""),
    12110400: ("InitializeMoonPhase", ""),
    12110990: ("AwardAbandonedOldWorkshopAchievement", ""),
}


class Characters(Character):
    InanimateDoll = 2110700


class Collisions(Collision):
    CollisionForAchievement = 2113500
