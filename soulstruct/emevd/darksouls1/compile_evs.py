import os
from soulstruct.emevd.darksouls1 import EMEVD
from soulstruct.emevd.darksouls1.constants import *


def unpack_all_emevd_to_numeric(emevd_dir, numeric_dir, maps=()):
    """ Build numeric resources from all DCX-compressed EMEVD resources in a directory.

    I have not included the DS1 EMEVD in the package, but you can build them yourself from the packaged EVS resources
    and compare to the originals if you have them.
    """
    if not maps:
        maps = ALL_MAPS
    for game_map in maps:
        map_name = game_map.file_name
        print('Building EMEVD -> numeric', map_name)
        e = EMEVD(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'))
        e.write_numeric(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))


def pack_all_numeric_to_emevd(numeric_dir, emevd_dir):
    for game_map in ALL_MAPS:
        map_name = game_map.file_name
        print('Building numeric -> EMEVD:', map_name)
        e = EMEVD(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        e.write_emevd(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'), dcx=True)


def decompile_all_numeric(numeric_dir, evs_dir, maps=()):
    if not maps:
        maps = ALL_MAPS
    for game_map in maps:
        map_name = game_map.file_name
        print('File:', map_name)
        print('  Loading from numeric...')
        e = EMEVD(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        print('  Writing numeric to EVS...')
        e.write_evs(os.path.join(evs_dir, f'{map_name}.py'))
        print('  Numeric decompiled successfully.')


def compile_all_evs(evs_dir='evs', numeric_dir='numeric_from_evs', emevd_dir='emevd_from_evs', maps=()):
    """ Quickly build all scripts. You can replace 'ALL_MAPS' with whatever subset of maps you want to build.

    Note that the resources built from EVS will not be quite identical to the original numeric resources:
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
        maps = ALL_MAPS  # Includes common events.

    for game_map in maps:
        map_name = game_map.file_name
        print('File:', map_name)
        print('  Loading from EVS...')
        e = EMEVD(os.path.join(evs_dir, f'{map_name}.py'))
        print('  Writing EVS to numeric...')
        e.write_numeric(os.path.join(numeric_dir, f'{map_name}.numeric.txt'))
        print('  Writing EVS to EMEVD (DCX)... ')
        e.write_emevd(os.path.join(emevd_dir, f'{map_name}.emevd.dcx'), dcx=True)
        print('  EVS compiled successfully.')


if __name__ == '__main__':
    # pack_all_numeric_to_emevd('numeric_from_vanilla', 'emevd_from_numeric')
    # decompile_all_numeric('numeric_from_vanilla', 'evs')
    compile_all_evs()
    unpack_all_emevd_to_numeric('emevd_from_evs', 'numeric_from_repack')
    decompile_all_numeric('numeric_from_repack', 'evs_from_repack')
