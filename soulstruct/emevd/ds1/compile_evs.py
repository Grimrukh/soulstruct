import os
from soulstruct.emevd.ds1 import EMEVD
from soulstruct.emevd.ds1.constants import ALL_MAPS


def unpack_all_emevd_to_numeric(emevd_dir, numeric_dir):
    """ Build numeric files from all DCX-compressed EMEVD files in a directory.

    I have not included the DS1 EMEVD in the package, but you can build them yourself from the packaged EVS files
    and compare to the originals if you have them.
    """
    for game_map in ALL_MAPS:
        map_name = game_map.file_name
        print('Building EMEVD -> numeric', map_name)
        e = EMEVD(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'))
        e.write_numeric(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))


def pack_all_numeric_to_emevd(numeric_dir, emevd_dir):
    for game_map in ALL_MAPS:
        map_name = game_map.file_name
        print('Building numeric -> EMEVD:', map_name)
        e = EMEVD(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        e.write_packed(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'), dcx=True)


def decompile_all_numeric(numeric_dir, evs_dir):
    for game_map in ALL_MAPS:
        map_name = game_map.file_name
        print('File:', map_name)
        print('  Loading from numeric...')
        e = EMEVD(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        print('  Writing numeric to EVS...')
        e.write_evs(os.path.join(evs_dir, f'{map_name}.evs'))
        print('  Numeric decompiled successfully.')


def compile_all_evs(evs_dir='evs', numeric_dir='numeric_from_evs', emevd_dir='emevd_from_evs', maps=()):
    """ Quickly build all scripts. You can replace 'ALL_MAPS' with whatever subset of maps you want to build.

    Note that the files built from EVS will not be quite identical to the original numeric files:
        - The order of event argument replacements (the indented lines starting with '^') may change.
        - The scanned argument types in RunEvent calls (2000[00]) will be correct in the EVS-built version, rather than
          assuming they are all integers.
        - Instructions with string arguments (in the 2013 class) may have non-zero dummy values, which are offsets to
          an empty string. These dummy values don't matter, and preserving them would be pointless effort, as these
          'PlayLog' instructions aren't even particularly useful.
        - Some other dummy values may not be quite correct. FromSoft couldn't decide whether to use 0 or -1 for many
          integer arguments, for example. I've fixed as many of these as I can just for presentation, but again, it
          doesn't even matter, as these dummy values will be overridden.

    If you notice any changes *other* than those described above, it's likely a bug. Let me know!
    """
    if not maps:
        maps = ALL_MAPS  # Includes common events and shared Chalice Dungeons events (m29).

    for game_map in maps:
        map_name = game_map.file_name
        print('File:', map_name)
        print('  Loading from EVS...')
        e = EMEVD(os.path.join(evs_dir, f'{map_name}.evs'))
        print('  Writing EVS to numeric...')
        e.write_numeric(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        print('  Writing EVS to EMEVD (DCX)... ')
        e.write_packed(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'), dcx=True)
        print('  EVS compiled successfully.')


if __name__ == '__main__':
    # unpack_all_emevd_to_numeric('game_data', 'numeric_from_vanilla')
    # pack_all_numeric_to_emevd('numeric_from_vanilla', 'emevd_from_numeric')
    # decompile_all_numeric('numeric_from_vanilla', 'evs')
    # compile_all_evs()
    # asylum = EMEVD('packed/m18_01_00_00.emevd')
    # asylum.write_packed('packed/m18_01_00_00.emevd')
    o_asylum = EMEVD(r'C:\Dark Souls\Dark Souls DATA\event\m18_01_00_00.emevd')
    o_asylum.write_evs('asylum.py')
    evs_asylum = EMEVD('asylum.py')
    evs_asylum.write_packed('repacked.emevd')
    unre = EMEVD('repacked.emevd')
    unre.write_evs('unre.evs')