import glob
import os
from soulstruct.emevd.ds1 import EMEVD
from soulstruct.emevd.ds1.constants import ALL_MAPS


def build_all_vanilla_verbose(directory='vanilla_verbose_ptd'):
    """ Build local vanilla verbose files. Useful after changes have been made to the verbose style. """
    for emevd_name in glob.glob(os.path.join(os.path.dirname(__file__), 'vanilla_numeric_ptd/*.numeric.txt')):
        e = EMEVD(emevd_name)
        e.write_verbose(os.path.join(directory, os.path.basename(emevd_name).replace('numeric', 'verbose')))


def build_all_evs():
    for game_map in ALL_MAPS:
        map_name = game_map.file_name
        print('Building', map_name)
        print('  Loading from numeric...')
        e = EMEVD(f'vanilla_numeric_ptd/{map_name}.numeric.txt')
        print('  Writing numeric to verbose...')
        e.write_verbose(f'vanilla_verbose_ptd/{map_name}.verbose.txt')
        print('  Writing numeric to EVS...')
        e.write_evs(f'vanilla_evs_ptd/{map_name}.evs')
        print('  Loading from EVS...')
        e = EMEVD(f'vanilla_evs_ptd/{map_name}.evs')
        print('  Writing EVS to numeric...')
        e.write_numeric(f'vanilla_numeric_from_evs_ptd/{map_name}.from_evs.numeric.txt')
        print('  Writing EVS to verbose...')
        e.write_verbose(f'vanilla_verbose_from_evs_ptd/{map_name}.from_evs.verbose.txt')
        print('  Writing EVS to EMEVD...')
        e.write_packed(f'vanilla_emevd_from_evs_ptd/{map_name}.from_evs.emevd')
        print('  Success.')


if __name__ == '__main__':
    build_all_evs()
