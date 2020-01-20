"""Script that gets and sets the bonfire warp list, which is an array that is hard-coded into the game executable."""
import logging
import struct

from .core import get_ds1_executable_and_version

_LOGGER = logging.getLogger(__name__)


# These offsets may be wrong if you do not have the latest version of the game.
# They are unlikely to change in future game updates, so hard-coding them is fairly safe.
PTDE_WARP_LIST_OFFSET = 15585416  # normal version of EXE
PTDE_DEBUG_WARP_LIST_OFFSET = 15599240
DSR_WARP_LIST_OFFSET = 28100512
# no debug version of DSR

# The order that these are listed is the order they will appear
# in the warp menu. The first number is the flag that must be
# enabled for the bonfire to appear; these flags are enabled by
# the engine when you sit at the corresponding bonfire. The second
# number is the entity ID of the bonfire object in the MSB. The
# third number is the index of the displayed location name in the
# PlaceNames FMG text table (in 'menu.msgbnd').
PTDE_VANILLA_EXE_DATA = [
    # (required_flag, bonfire_entity, location_name_text),
    (200, 1021960, 2000),  # Firelink Shrine
    (205, 1011961, 2001),  # Sunlight Altar
    (203, 1511960, 2002),  # Anor Londo
    (207, 1511950, 2003),  # Chamber of the Princess
    (208, 1511962, 2004),  # Darkmoon Tomb
    (204, 1601950, 2005),  # The Abyss
    (202, 1401960, 2006),  # Daughter of Chaos
    (206, 1311950, 2007),  # Altar of the Gravelord
    (201, 1321960, 2008),  # Stone Dragon
    (209, 1211963, 2009),  # Sanctuary Garden
    (210, 1211961, 2010),  # Oolacile Sanctuary
    (211, 1211962, 2011),  # Oolacile Township
    (212, 1211950, 2012),  # Chasm of the Abyss
    (213, 1211964, 2013),  # Oolacile Township Dungeon
    (214, 1001960, 2014),  # Depths
    (215, 1011964, 2015),  # Undead Parish
    (216, 1101960, 2016),  # Painted World of Ariamis
    (217, 1311961, 2017),  # Tomb of the Giants
    (218, 1701960, 2018),  # The Duke's Archives
    (219, 1701950, 2019),  # Crystal Cave
]

DSR_VANILLA_EXE_DATA = PTDE_VANILLA_EXE_DATA + [
    (220, 1301962, 2020),  # Catacombs (Vamos)
]

# I've left the Daughters of Ash list here for you to inspect.
# Note that many of the required flags have changed, as the original
# flags (in the 200-220 range) are difficult to manipulate. I've
# added new flags that are manually enabled in the corresponding map's
# event script when it detects that you have sat at that bonfire.
MODDED_EXE_DATA = [
    # (required_flag, bonfire_entity, location_name_text)
    (200, 1021960, 2000),       # Firelink Shrine
    (11012045, 1011961, 2001),  # Parish Turret
    (215, 1011964, 2002),       # Abandoned Church
    (11302045, 1301961, 2003),  # Bone Chimney
    (11202045, 1201961, 2004),  # Moonlight Grove
    (11402045, 1401961, 2005),  # Fetid Slagmire
    (11002045, 1001960, 2006),  # The Sluiceworks
    (203, 1511960, 2007),       # Anor Londo
    (11512045, 1511950, 2008),  # Sun Chamber
    (11512046, 1511962, 2009),  # Gwyn's Altar
    (11312045, 1311960, 2010),  # The Undercrypt
    (202, 1401960, 2011),       # The Nursery
    (11412085, 1411964, 2012),  # Sanctum of Chaos
    (11602045, 1601950, 2013),  # The Abyss
    (11702045, 1701960, 2014),  # The Duke's Archives
    (11102045, 1101960, 2015),  # Cloister of Exiles
    (201, 1321960, 2016),       # Ash Lake
    (11212085, 1211962, 2017),  # Royal Hippodrome
    (213, 1211964, 2018),       # Chasm Cell
    (11812045, 1811960, 2019),  # Undead Asylum
]


def restore_bonfire_warp_data(executable_path, dsr=None, debug=False):
    executable_path, dsr, debug = get_ds1_executable_and_version(executable_path, dsr, debug)
    bonfire_warp_data = DSR_VANILLA_EXE_DATA if dsr else PTDE_VANILLA_EXE_DATA
    return edit_executable_bonfire_warp_data(executable_path, bonfire_warp_data, dsr=dsr, debug=debug)


def get_executable_bonfire_warp_data(executable_path, dsr=None, debug=False):
    executable_path, dsr, debug = get_ds1_executable_and_version(executable_path, dsr, debug)
    with executable_path.open('r+b') as f:
        if dsr:
            f.seek(DSR_WARP_LIST_OFFSET)
            bonfire_count = len(DSR_VANILLA_EXE_DATA)
        else:
            if debug:
                f.seek(PTDE_DEBUG_WARP_LIST_OFFSET)
            else:
                f.seek(PTDE_WARP_LIST_OFFSET)
            bonfire_count = len(PTDE_VANILLA_EXE_DATA)
        bonfire_warp_data = []
        for _ in range(bonfire_count):
            bonfire_warp_data.append(struct.unpack('3i', f.read(12)))
    return bonfire_warp_data


def edit_executable_bonfire_warp_data(executable_path, bonfire_warp_data, dsr=None, debug=False):
    """Detects PTDE vs. DSR automatically based on file name, but you must specify 'debug=True' for PTDE debug."""
    executable_path, dsr, debug = get_ds1_executable_and_version(executable_path, dsr, debug)

    if not all([isinstance(data, (list, tuple)) and len(data) == 3 for data in bonfire_warp_data]):
        raise ValueError("Bonfire data must be a sequence of (flag, entity, text) tuple/list triplets.")
    if dsr and len(bonfire_warp_data) != 21:
        raise ValueError("A list of 21 bonfire (flag, entity, text) triplets must be given for DSR.")
    elif not dsr and len(bonfire_warp_data) != 20:
        raise ValueError("A list of 20 bonfire (flag, entity, text) triplets must be given for PTDE.")

    new_warp_list_bytes = b''.join([struct.pack('3i', *bonfire) for bonfire in bonfire_warp_data])

    with executable_path.open('r+b') as f:
        if dsr:
            f.seek(DSR_WARP_LIST_OFFSET)
        else:
            if debug:
                f.seek(PTDE_DEBUG_WARP_LIST_OFFSET)
            else:
                f.seek(PTDE_WARP_LIST_OFFSET)
        f.write(new_warp_list_bytes)
    _LOGGER.info(f"Bonfire warp list in DS1 executable {str(executable_path)} modified successfully.")


if __name__ == '__main__':
    from soulstruct import PTDE_PATH
    bd = get_executable_bonfire_warp_data(PTDE_PATH)
    print(bd)
