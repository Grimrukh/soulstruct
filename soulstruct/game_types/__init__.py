from .animation_types import *
from .basic_types import *
from .misc_types import *
from .msb_types import *
from .param_types import *
from .sound_types import *
from .text_types import *


# Game type names that can appear as EMEVD instruction arguments.
EMEVD_GAME_TYPES = {
    "Character",
    "Region",
    "Object",
    "PlayerStart",
    "Flag",
    "ItemLotParam",
    "ItemParam",
    "WeaponParam",
    "ArmorParam",
    "RingParam",
    "GoodParam",
    "Collision",
    "Text",  # TODO: are text types other than EventText and NPCName actually ever used?
    "EventText",
    "NPCName",
}
