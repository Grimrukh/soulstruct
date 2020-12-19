__all__ = ["DrawParam", "DrawParamBND", "DrawParamDirectory", "DRAW_PARAM_TABLES", "DRAW_PARAM_MAPS"]

import abc
import logging
import pickle
import re
import typing as tp
from pathlib import Path

from soulstruct.bnd import BaseBND, BND3

from .core import Param
from .paramdef import ParamDefBND, GET_BUNDLED

_LOGGER = logging.getLogger(__name__)

_DRAW_PARAM_FILE_NAME_RE = re.compile(r"([ms]\d\d|default)(_\d)?(_[\w]+\.param)")
_DRAW_PARAM_BND_FILE_NAME_RE = re.compile(r"(a\d\d|default)(_[\w]+\.DrawParam\.parambnd)(\.dcx)?")


class DrawParam(Param):
    """`Param` with some extra methods that are specific to DrawParam tables."""

    def get_nonzero_entries(self, ignore_polyg=True):
        """Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if ignore_polyg:
            return {
                index: row for index, row in self.rows.items() if row.name and not row.name.startswith("0")
            }
        return {
            index: row
            for index, row in self.rows.items()
            if row.name and not row.name.startswith("0") and not row.name.lower().startswith("polyg")
        }


DRAW_PARAM_TABLES = (
    "Dof",
    "EnvLightTex",
    "Fog",
    "LensFlare",
    "LensFlareEx",
    "AmbientLight",
    "ScatteredLight",
    "PointLight",
    "Shadow",
    "ToneCorrect",
    "ToneMap",
    "s_AmbientLight",
)


class DrawParamBND:

    DepthOfField: list[DrawParam]
    # EnvLightTex: list[DrawParam]
    Fog: list[DrawParam]
    LensFlares: list[DrawParam]
    LensFlareSources: list[DrawParam]
    AmbientLight: list[DrawParam]
    ScatteredLight: list[DrawParam]
    PointLights: list[DrawParam]
    Shadows: list[DrawParam]
    ToneCorrection: list[DrawParam]
    ToneMapping: list[DrawParam]
    # DebugAmbientLight: list[DrawParam]

    UNDECODABLE_ROW_NAMES = {
        "LIGHT_BANK": (b"\x80\x1e", b"\xfe\x1e"),
    }

    def __init__(self, draw_param_bnd_source, paramdef_bnd=None):
        """Structure that manages double-slots and table nicknames for one DrawParamBND file (i.e. one map "area")."""
        self.params = {}  # type: dict[str, list[tp.Optional[DrawParam], tp.Optional[DrawParam]]]
        self._bnd_entry_paths = {}  # type: dict[tuple[str, int], str]
        if paramdef_bnd is None:
            paramdef_bnd = GET_BUNDLED()
        elif not isinstance(paramdef_bnd, ParamDefBND):
            raise TypeError(
                f"`paramdef_bnd` must be None or an existing `ParamDefBND`, not {type(paramdef_bnd)}."
            )

        if not isinstance(draw_param_bnd_source, BaseBND):
            draw_param_bnd_source = BND3(draw_param_bnd_source)

        self._bnd = draw_param_bnd_source

        for entry in draw_param_bnd_source:

            if not (match := _DRAW_PARAM_FILE_NAME_RE.match(entry.name)):
                raise ValueError(f"Malformed Param name: '{entry.name}'")
            slot = int(match.group(2)[1]) if match.group(2) else 0
            if slot not in {0, 1}:
                raise ValueError(
                    "Only slot 0 (`mXX_ParamName.param`) and slot 1 (`mXX_1_ParamName.param`) are valid in file name."
                )
            param_name = match.group(3)
            if match.group(1).startswith("s"):
                param_name = "s_" + param_name

            undecodable_row_names = self.UNDECODABLE_ROW_NAMES.get(param_name, ())
            p = DrawParam(entry.data, paramdef_bnd, undecodable_row_names=undecodable_row_names)
            self.params.setdefault(param_name, [None, None])[slot] = p
            self._bnd_entry_paths[param_name, slot] = entry.path
            if not match.group(1).startswith("s") and p.param_info is not None:
                # sXX_LightBank does not have attribute access.
                setattr(self, p.nickname, self.params[param_name])

    def __getitem__(self, category):
        if not category.startswith("_"):
            try:
                return getattr(self, category)
            except AttributeError:
                pass
        raise KeyError(f"{category} is not a valid Lighting param category.")

    def __iter__(self):
        return iter(self.params.keys())

    def keys(self):
        return self.params.keys()

    def values(self):
        return self.params.values()

    def items(self):
        return self.params.items()

    # TODO: Move to Dark Souls 1 until indices, etc. are confirmed for other games.
    def copy_slot_0_to_slot_1(self):
        """Also creates BND entries if needed, which involves shifting up the IDs of all the slot 0 entries.

        Note that any new slot 1 BND entries are copied from the existing slot 0 entries, while the slot 1 `ParamTable`
        attributes are copied from the slot 0 `ParamTable` attributes. If the `ParamTable` structures and BND entries
        are out of sync (i.e. changes have been made to a table since the last `save()` or `update_bnd()` call), they
        will be equally out of sync for slot 1.
        """
        if len(self._bnd) == 12:
            # Create new paths and move up slot 0 IDs.
            for table_name, slots in self.params.items():
                slot_0_path = self._bnd_entry_paths[table_name, 0]
                self._bnd_entry_paths[table_name, 1] = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", slot_0_path)
            s_ambient = self._bnd[11]
            self._bnd.remove_entry(11)
            for i in range(11):
                slot_0 = self._bnd[i].copy()
                slot_0.id += 11
                new_path = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", self._bnd[i].path)
                self._bnd[i].path = new_path
                self._bnd.add_entry(slot_0)
            s_ambient_0 = s_ambient.copy()
            s_ambient_0.id = 23
            s_ambient.path = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", s_ambient.path)
            s_ambient.id = 22
            self._bnd.add_entry(s_ambient)
            self._bnd.add_entry(s_ambient_0)
        for table_name, slots in self.params.items():
            slots[1] = slots[0].copy()

    def update_bnd(self):
        """Update the internal BND by packing the current ParamTables. Called automatically by `save()`."""
        for param_name, param_table_slots in self.params.items():
            for slot, param_table in enumerate(param_table_slots):
                try:
                    param_table_entry_path = self._bnd_entry_paths[param_name, slot]
                except KeyError:
                    continue  # Slot does not exist.
                if param_table is None:
                    self._bnd.remove_entry(param_table_entry_path)  # Slot deleted.
                else:
                    self._bnd.entries_by_path[param_table_entry_path].data = param_table.pack()

    def save(self, draw_param_bnd_path=None):
        """Save the DarkSoulsGameParameters. If no path is given, it will attempt to save to the same BND file."""
        self.update_bnd()
        self._bnd.write(draw_param_bnd_path)


class DrawParamDirectory(abc.ABC):

    _MAP_IDS = (10, 11, 12, 13, 14, 15, 16, 17, 18, 99, "default")

    m10: DrawParamBND
    m11: DrawParamBND
    m12: DrawParamBND
    m13: DrawParamBND
    m14: DrawParamBND
    m15: DrawParamBND
    m16: DrawParamBND
    m17: DrawParamBND
    m18: DrawParamBND
    m99: DrawParamBND
    default: DrawParamBND

    # Lod (default only), EnvLightTex (useless) and DebugAmbientLight (useless) are left out.
    PARAM_NAMES = [
        "DepthOfField",
        "Fog",
        "LensFlares",
        "LensFlareSources",
        "AmbientLight",
        "ScatteredLight",
        "PointLights",
        "Shadows",
        "ToneCorrection",
        "ToneMapping",
    ]

    JUNK_ENCODED_BYTES = (b"\x80\x1e", b"\xfe\x1e")  # These appear as `ParamEntry` Shift-JIS names in LIGHT_BANK.

    def __init__(self, draw_param_directory=None, paramdef_bnd=None):
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
                file_map_name = f"a{area_id}"
                map_name = f"m{area_id}"
            else:
                file_map_name = map_name = area_id
            file_map_name += "_DrawParam.parambnd"

            try:
                draw_param_bnd = BND3(self._draw_param_directory / f"{file_map_name}.dcx")
                file_map_name += ".dcx"
            except FileNotFoundError:
                try:
                    draw_param_bnd = BND3(self._draw_param_directory / file_map_name)
                except FileNotFoundError:
                    raise FileNotFoundError(
                        f"Could not find '{file_map_name}[.dcx]' in directory " f"'{self._draw_param_directory}'."
                    )
            self._data[map_name] = DrawParamBND(draw_param_bnd, paramdef_bnd)
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
        with Path(lighting_param_pickle_path).open("wb") as f:
            pickle.dump(self, f)

    def save(self, draw_param_directory=None):
        if not draw_param_directory:
            draw_param_directory = self._draw_param_directory
        draw_param_directory = Path(draw_param_directory)
        for map_name, map_draw_param in self._data.items():
            bnd_file_name = self._bnd_file_names[map_name]
            map_draw_param.save(draw_param_directory / bnd_file_name)
        _LOGGER.info("Dark Souls lighting parameters (DrawParam) written successfully.")
        if not self._reload_warning_given:
            _LOGGER.info("Remember to reload your game to see changes.")
            self._reload_warning_given = True


DRAW_PARAM_MAPS = {
    "m10": "Depths, Undead Burg/Parish, Firelink Shrine",
    "m11": "Painted World",
    "m12": "Darkroot, Oolacile",
    "m13": "Catacombs, Tomb of the Giants, Great Hollow, Ash Lake",
    "m14": "Blighttown, Quelaag's Domain, Demon Ruins, Lost Izalith",
    "m15": "Sen's Fortress, Anor Londo",
    "m16": "New Londo Ruins, Valley of Drakes",
    "m17": "Duke's Archives",
    "m18": "Kiln of the First Flame, Undead Asylum",
    "default": "Menus",
}
