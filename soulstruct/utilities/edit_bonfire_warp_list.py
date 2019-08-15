"""Script that edits the bonfire warp list, which is an array that is hard-coded into the game executable."""
import struct

# These offsets may be wrong if you do not have the latest version of the game.
# They are unlikely to change in future game updates, so hard-coding them is fairly safe.
PTD_WARP_LIST_OFFSET = 15585416  # normal version of EXE
PTD_DEBUG_WARP_LIST_OFFSET = 15599240
DSR_WARP_LIST_OFFSET = 28100512

# (required_flag, bonfire_entity, location_name_text)
# The order that these are listed is the order they will appear
# in the warp menu. The first number is the flag that must be
# enabled for the bonfire to appear; these flags are enabled by
# the engine when you sit at the corresponding bonfire. The second
# number is the entity ID of the bonfire object in the MSB. The
# third number is the index of the displayed location name in the
# PlaceNames FMG text table (in 'menu.msgbnd').
VANILLA_EXE_DATA = [
    (200, 1021960, 2000),
    (205, 1011961, 2001),
    (203, 1511960, 2002),
    (207, 1511950, 2003),
    (208, 1511962, 2004),
    (204, 1601950, 2005),
    (202, 1401960, 2006),
    (206, 1311950, 2007),
    (201, 1321960, 2008),
    (209, 1211963, 2009),
    (210, 1211961, 2010),
    (211, 1211962, 2011),
    (212, 1211950, 2012),
    (213, 1211964, 2013),
    (214, 1001960, 2014),
    (215, 1011964, 2015),
    (216, 1101960, 2016),
    (217, 1311961, 2017),
    (218, 1701960, 2018),
    (219, 1701950, 2019),
]

# I've left the Daughters of Ash list here for you to inspect.
# Note that many of the required flags have changed, as the original
# flags (in the 200-220 range) are difficult to manipulate. I've
# added new flags that are manually enabled in the corresponding map's
# event scripts when it detects that you have sat at that bonfire.
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


def edit_executable(executable_path, debug=False, restore=False):
    """Detects PTD vs. DSR automatically based on file name, but you must specify 'debug=True' for PTD debug."""
    new_warp_list_bytes = b''.join(
        [struct.pack('3i', *bonfire) for bonfire in (VANILLA_EXE_DATA if restore else MODDED_EXE_DATA)])
    dsr = True if executable_path.endswith('DarkSoulsRemastered.exe') else False
    with open(executable_path, 'r+b') as f:
        if dsr:
            if debug:
                raise ValueError("'debug' cannot both be true for 'DarkSoulsRemastered.exe' executable.")
            f.seek(DSR_WARP_LIST_OFFSET)
        elif debug:
            f.seek(PTD_DEBUG_WARP_LIST_OFFSET)
        else:
            f.seek(PTD_WARP_LIST_OFFSET)
        f.write(new_warp_list_bytes)
    print(f"# Executable at {repr(executable_path)} {'restored' if restore else 'modded'} successfully.")


if __name__ == '__main__':
    EXE_PATH = 'G:/Steam/steamapps/common/DARK SOULS REMASTERED/DarkSoulsRemastered.exe'
    edit_executable(EXE_PATH, debug=False, restore=False)
