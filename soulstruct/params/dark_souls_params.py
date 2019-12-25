import pickle
from pathlib import Path
from typing import Dict, List, Optional

from soulstruct.bnd.core import BND, BaseBND
from soulstruct.params import ParamTable, DrawParamTable, PARAMDEF_BND
from soulstruct.params.fields import PARAM_NICKNAMES


class DarkSoulsGameParameters(object):

    AI: ParamTable
    Armor: ParamTable
    ArmorUpgrades: ParamTable
    Bosses: ParamTable
    Bullets: ParamTable
    Cameras: ParamTable
    Dialogue: ParamTable
    Faces: ParamTable
    Goods: ParamTable
    Players: ParamTable
    PlayerAttacks: ParamTable
    PlayerBehaviors: ParamTable
    ItemLots: ParamTable
    NonPlayers: ParamTable
    NonPlayerAttacks: ParamTable
    NonPlayerBehaviors: ParamTable
    MenuColors: ParamTable
    Movement: ParamTable
    Objects: ParamTable
    ObjectActivations: ParamTable
    Rings: ParamTable
    Shops: ParamTable
    SpecialEffects: ParamTable
    Spells: ParamTable
    Terrains: ParamTable
    Throws: ParamTable
    UpgradeMaterials: ParamTable
    Weapons: ParamTable
    WeaponUpgrades: ParamTable
    SpecialEffectVisuals: ParamTable

    param_names = [
        'Players', 'PlayerBehaviors', 'PlayerAttacks',
        'NonPlayers', 'NonPlayerBehaviors', 'NonPlayerAttacks',
        'Bullets', 'Throws', 'SpecialEffects',
        'Weapons', 'Armor', 'Rings', 'Goods',
        'WeaponUpgrades', 'ArmorUpgrades', 'UpgradeMaterials',
        'ItemLots', 'Bosses', 'Shops', 'Spells', 'Objects', 'ObjectActivations',
        'Movement', 'Cameras', 'Terrains', 'Faces', 'Dialogue',
        'MenuColors', 'SpecialEffectVisuals',
    ]

    def __init__(self, game_param_bnd_source=None):
        """Unpack DS1 GameParams into a single modifiable structure.

        Args:
            game_param_bnd_source: any valid source for GameParam.parambnd[.dcx] (its file path, the directory
                containing it, the unpacked BND directory, or an existing BND instance). It will default to the
                DEFAULT_GAME package. The appropriate bundled ParamDef will be loaded automatically, detected based on
                the DCX compression of the BND.
        """
        self._reload_warning = True
        self._data = {}

        if game_param_bnd_source is None:
            self._game_param_bnd = None
            self.paramdef_bnd = None
            return

        if isinstance(game_param_bnd_source, BaseBND):
            self._game_param_bnd = game_param_bnd_source
        else:
            if isinstance(game_param_bnd_source, (str, Path)):
                game_param_bnd_source = Path(game_param_bnd_source)
                if game_param_bnd_source.is_dir():
                    if (game_param_bnd_source / 'GameParam.parambnd').is_file():
                        game_param_bnd_source = game_param_bnd_source / 'GameParam.parambnd'
                    elif (game_param_bnd_source / 'GameParam.parambnd.dcx').is_file():
                        game_param_bnd_source = game_param_bnd_source / 'GameParam.parambnd.dcx'
            try:
                self._game_param_bnd = BND(game_param_bnd_source)
            except TypeError:
                raise TypeError("Could not load DarkSoulsGameParameters from given source.")
        self.paramdef_bnd = PARAMDEF_BND('dsr' if self._game_param_bnd.dcx else 'ptd')

        for entry in self._game_param_bnd:
            p = self._data[entry.path] = ParamTable(entry.data, self.paramdef_bnd)
            try:
                # Nickname assigned here (ParamTable isn't aware of its own basename).
                param_nickname = PARAM_NICKNAMES[entry.name[:-len('.param')]]
            except KeyError:
                # ParamTables without nicknames (i.e. useless params) are excluded from this structure.
                pass
            else:
                setattr(self, param_nickname, p)  # NOTE: Reference to dictionary in self._data[entry.path].
                p.nickname = param_nickname

    def update_bnd(self):
        """Update the internal BND by packing the current ParamTables. Called automatically by `save()`."""
        for param_table_entry_path, param_table in self._data.items():
            self._game_param_bnd.entries_by_path[param_table_entry_path].data = param_table.pack()

    def save(self, game_param_bnd_path=None, auto_pickle=False):
        """Save the DarkSoulsGameParameters. If no path is given, it will attempt to save to the same BND file."""
        self.update_bnd()
        if auto_pickle:
            self.pickle()
        self._game_param_bnd.write(game_param_bnd_path)
        print('# INFO: --------> Dark Souls game parameters (GameParam) saved successfully.')
        if not self._reload_warning:
            print('# INFO: --------> Remember to reload your game to see changes.')
            self._reload_warning = True

    def pickle(self, game_param_pickle_path=None):
        """Save the entire DarkSoulsGameParameters to a pickled file, which will be faster to load in future."""
        if game_param_pickle_path is None:
            game_param_pickle_path = self._game_param_bnd.bnd_path
            if game_param_pickle_path is None:
                raise ValueError("Could not automatically determine path to pickle DarkSoulsGameParameters.")
            while game_param_pickle_path.suffix in {'.dcx', '.parambnd'}:
                game_param_pickle_path = game_param_pickle_path.parent / game_param_pickle_path.stem
            if not game_param_pickle_path.suffix != '.pickle':
                game_param_pickle_path = game_param_pickle_path.with_suffix(game_param_pickle_path.suffix + '.pickle')
        with open(game_param_pickle_path, 'wb') as f:
            pickle.dump(self, f)

    def __getitem__(self, category) -> ParamTable:
        return getattr(self, category)

    def get_range(self, category, start, count):
        """Get a list of (id, entry) pairs from a certain range inside ID-sorted param dictionary."""
        return self[category].get_range(start, count)


DRAW_PARAM_TABLES = ('Dof', 'EnvLightTex', 'Fog', 'LensFlare', 'LensFlareEx', 'AmbientLight', 'ScatteredLight',
                     'PointLight', 'Shadow', 'ToneCorrect', 'ToneMap', 's_AmbientLight')


class MapDrawParam(object):

    DepthOfField: List[Optional[DrawParamTable]]
    # EnvLightTex: List[Optional[DrawParamTable]]
    Fog: List[Optional[DrawParamTable]]
    LensFlares: List[Optional[DrawParamTable]]
    LensFlareSources: List[Optional[DrawParamTable]]
    AmbientLight: List[Optional[DrawParamTable]]
    ScatteredLight: List[Optional[DrawParamTable]]
    PlayerLights: List[Optional[DrawParamTable]]
    Shadows: List[Optional[DrawParamTable]]
    ToneCorrection: List[Optional[DrawParamTable]]
    ToneMapping: List[Optional[DrawParamTable]]
    # DebugAmbientLight: List[Optional[DrawParamTable]]

    def __init__(self, draw_param_bnd):
        """Structure that manages double-slots and table nicknames for one DrawParam BND file (i.e. one map area)."""
        self._data = {}  # type: Dict[str, List[Optional[DrawParamTable], Optional[DrawParamTable]]]
        self._bnd_entry_paths = {}
        paramdef_bnd = PARAMDEF_BND('dsr' if bool(draw_param_bnd.dcx) else 'ptd')

        if not isinstance(draw_param_bnd, BaseBND):
            draw_param_bnd = BND(draw_param_bnd)

        self._draw_param_bnd = draw_param_bnd

        for entry in draw_param_bnd:
            parts = entry.name[:-len('.param')].split('_')
            if len(parts) == 2:
                slot = 0
                param_name = parts[1]
            elif len(parts) == 3:
                if parts[1] != '1':
                    raise ValueError("Only slot 0 (no slot number in path) and slot 1 ('_1_' in path) are valid in "
                                     "DrawParam.")
                slot = 1
                param_name = parts[2]
            else:
                raise ValueError(f"Malformed ParamTable name: '{entry.name}'")
            if parts[0].startswith('s'):
                param_name = 's_' + param_name

            self._data.setdefault(param_name, [None, None])[slot] = DrawParamTable(entry.data, paramdef_bnd)
            self._bnd_entry_paths[param_name, slot] = entry.path
            try:
                param_nickname = PARAM_NICKNAMES[param_name]
            except KeyError:
                raise KeyError(f"Could not find nickname for DrawParam table: {param_name}")
            else:
                setattr(self, param_nickname, self._data[param_name])

    def __getitem__(self, category):
        if not category.startswith('_'):
            try:
                return getattr(self, category)
            except AttributeError:
                pass
        raise KeyError(f"{category} is not a valid Lighting param category.")

    def __iter__(self):
        return iter(self._data.keys())

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    # TODO: Method that adds slot 1 (duplicating slot 0). Will need to add entry path as well.

    def update_bnd(self):
        """Update the internal BND by packing the current ParamTables. Called automatically by `save()`."""
        for param_name, param_table_slots in self._data.items():
            for slot, param_table in enumerate(param_table_slots):
                try:
                    param_table_entry_path = self._bnd_entry_paths[param_name, slot]
                except KeyError:
                    continue  # Slot does not exist.
                if param_table is None:
                    self._draw_param_bnd.remove_entry(param_table_entry_path)  # Slot deleted.
                else:
                    self._draw_param_bnd.entries_by_path[param_table_entry_path].data = param_table.pack()

    def save(self, draw_param_bnd_path=None):
        """Save the DarkSoulsGameParameters. If no path is given, it will attempt to save to the same BND file."""
        self.update_bnd()
        self._draw_param_bnd.write(draw_param_bnd_path)


DRAW_PARAM_MAPS = {
    'm10': 'Depths | Undead Burg/Parish | Firelink Shrine',
    'm11': 'Painted World',
    'm12': 'Darkroot | Oolacile',
    'm13': 'Catacombs | Tomb of the Giants | Great Hollow/Ash Lake',
    'm14': "Blighttown | Quelaag's Domain | Demon Ruins/Lost Izalith",
    'm15': "Sen's Fortress | Anor Londo",
    'm16': 'New Londo Ruins/Valley of Drakes',
    'm17': "Duke's Archives",
    'm18': 'Kiln of the First Flame | Undead Asylum',
    'default': 'Menus',
}


class DarkSoulsLightingParameters(object):

    _MAP_IDS = (10, 11, 12, 13, 14, 15, 16, 17, 18, 99, 'default')

    m10: MapDrawParam
    m11: MapDrawParam
    m12: MapDrawParam
    m13: MapDrawParam
    m14: MapDrawParam
    m15: MapDrawParam
    m16: MapDrawParam
    m17: MapDrawParam
    m18: MapDrawParam
    m99: MapDrawParam
    default: MapDrawParam

    # Lod (default only), EnvLightTex (useless) and DebugAmbientLight (useless) are left out.
    param_names = [
        'DepthOfField', 'Fog', 'LensFlares', 'LensFlareSources',
        'AmbientLight', 'ScatteredLight', 'PlayerLights',
        'Shadows', 'ToneCorrection', 'ToneMapping',
    ]

    def __init__(self, draw_param_directory=None):
        """Unpack DS1 DrawParams into a single modifiable structure.

        Opens all DrawParam BNDs simultaneously for editing and repacking. The appropriate bundled ParamDef file will be
        loaded, with the game version determined by the DrawParam DCX compression.

        Args:
            draw_param_directory: Directory where all the 'aXX_DrawParam.parambnd[.dcx]' files are. This will be inside
                'params/DrawParam' in your game directory..
        """

        self._reload_warning_given = True
        self._data = {}
        self._bnd_file_names = {}

        if draw_param_directory is None:
            return

        self._draw_param_directory = Path(draw_param_directory)

        for area_id in self._MAP_IDS:
            if isinstance(area_id, int):
                file_map_name = f'a{area_id}'
                map_name = f'm{area_id}'
            else:
                file_map_name = map_name = area_id
            file_map_name += '_DrawParam.parambnd'

            try:
                draw_param_bnd = BND(self._draw_param_directory / f'{file_map_name}.dcx', optional_dcx=False)
                file_map_name += '.dcx'
            except FileNotFoundError:
                try:
                    draw_param_bnd = BND(self._draw_param_directory / file_map_name, optional_dcx=False)
                except FileNotFoundError:
                    raise FileNotFoundError(f"Could not find '{file_map_name}[.dcx]' in directory "
                                            f"'{self._draw_param_directory}'.")
            self._data[map_name] = MapDrawParam(draw_param_bnd)
            self._bnd_file_names[map_name] = file_map_name
            setattr(self, map_name, self._data[map_name])

    def __getitem__(self, map_name):
        if map_name not in self._data:
            raise KeyError(f"Invalid DrawParam map name: '{map_name}'")
        return self._data[map_name]

    def __iter__(self):
        return iter(self._data.items())

    def pickle(self, lighting_param_pickle_path):
        """Save the entire `DarkSoulsLightingParameters` instance to a pickled file, which will be faster to load."""
        with open(lighting_param_pickle_path, 'wb') as f:
            pickle.dump(self, f)

    def save(self, draw_param_directory=None):
        if not draw_param_directory:
            draw_param_directory = self._draw_param_directory
        draw_param_directory = Path(draw_param_directory)
        for map_name, map_draw_param in self._data.items():
            bnd_file_name = self._bnd_file_names[map_name]
            map_draw_param.save(draw_param_directory / bnd_file_name)
        print('# INFO: --------> Dark Souls lighting parameters (DrawParam) saved successfully.')
        if not self._reload_warning_given:
            print('# INFO: Remember to reload your game to see changes.')
            self._reload_warning_given = True
