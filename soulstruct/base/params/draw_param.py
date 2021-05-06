from __future__ import annotations

__all__ = ["DrawParamBND", "DrawParamDirectory", "DRAW_PARAMS"]

import abc
import logging
import pickle
import re
import typing as tp
from pathlib import Path

from soulstruct.containers.bnd import BND3
from soulstruct.games import GameSpecificType

from .paramdef import ParamDefBND

if tp.TYPE_CHECKING:
    from .param import Param

_LOGGER = logging.getLogger(__name__)

_DRAW_PARAM_FILE_NAME_RE = re.compile(r"([ms]\d\d|default)(_\d)?(_[\w]+\.param)")
_DRAW_PARAM_BND_FILE_NAME_RE = re.compile(r"(a\d\d|default)(_[\w]+\.DrawParam\.parambnd)(\.dcx)?")


DRAW_PARAMS = (
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


class DrawParamBND(GameSpecificType, BND3, abc.ABC):

    EXT = ".parambnd"
    DRAW_PARAM_CLASS: tp.Type[Param] = None
    GET_BUNDLED_PARAMDEF: tp.Callable = None
    UNDECODABLE_ROW_NAMES = {
        "LIGHT_BANK": (b"\x80\x1e", b"\xfe\x1e"),  # invalid single-character used in both versions of DS1
    }

    def __init__(self, draw_param_bnd_source, dcx_magic=(), paramdef_bnd=None):
        """Structure that manages double-slots and table nicknames for one `DrawParamBND` file (i.e. one map "area")."""
        self.params = {}  # type: dict[str, list[tp.Optional[Param], tp.Optional[Param]]]
        self._slot_entry_paths = {}  # type: dict[tuple[str, int], str]

        if paramdef_bnd is None:
            self.paramdef_bnd = self.GET_BUNDLED_PARAMDEF()
        elif isinstance(paramdef_bnd, ParamDefBND):
            self.paramdef_bnd = paramdef_bnd
        else:
            raise TypeError(f"`paramdef_bnd` must be None or an existing `ParamDefBND`, not {type(paramdef_bnd)}.")

        super().__init__(draw_param_bnd_source, dcx_magic=dcx_magic)

        for entry in self.entries:
            if not (match := _DRAW_PARAM_FILE_NAME_RE.match(entry.name)):
                raise ValueError(f"Malformed `DrawParam` BND entry name: '{entry.name}'")
            slot = int(match.group(2)[1]) if match.group(2) else 0
            if slot not in {0, 1}:
                raise ValueError(
                    "Only slot 0 (`mXX_ParamName.param`) and slot 1 (`mXX_1_ParamName.param`) are valid in file name."
                )
            param_name = match.group(3)
            if match.group(1).startswith("s"):
                param_name = "s_" + param_name

            undecodable_row_names = self.UNDECODABLE_ROW_NAMES.get(param_name, ())
            p = self.DRAW_PARAM_CLASS(
                entry.get_uncompressed_data(),
                paramdef_bnd=self.paramdef_bnd,
                undecodable_row_names=undecodable_row_names,
            )
            self.params.setdefault(param_name, [None, None])[slot] = p
            self._slot_entry_paths[param_name, slot] = entry.path
            if not match.group(1).startswith("s") and p.param_info is not None:
                # sXX_LightBank does not have attribute access.
                setattr(self, p.nickname, self.params[param_name])

    def keys(self):
        return self.params.keys()

    def values(self):
        return self.params.values()

    def items(self):
        return self.params.items()

    def get_param(self, param_nickname) -> Param:
        return getattr(self, param_nickname)

    def copy_slot_0_to_slot_1(self):
        """Also creates BND entries if needed, which involves shifting up the IDs of all the slot 0 entries.

        Note that any new slot 1 BND entries are copied from the existing slot 0 entries, while the slot 1 `ParamTable`
        attributes are copied from the slot 0 `ParamTable` attributes. If the `ParamTable` structures and BND entries
        are out of sync (i.e. changes have been made to a table since the last `save()` or `update_bnd()` call), they
        will be equally out of sync for slot 1.
        """
        if len(self.entries) == 12:
            # Create new paths and move up slot 0 IDs.
            for table_name, slots in self.params.items():
                slot_0_path = self._slot_entry_paths[table_name, 0]
                self._slot_entry_paths[table_name, 1] = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", slot_0_path)
            s_ambient = self.entries[11]
            self.remove_entry(11)
            for i in range(11):
                slot_0 = self.entries[i].copy()
                slot_0.id += 11
                new_path = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", self.entries[i].path)
                self.entries[i].path = new_path
                self.add_entry(slot_0)
            s_ambient_0 = s_ambient.copy()
            s_ambient_0.id = 23
            s_ambient.path = _DRAW_PARAM_FILE_NAME_RE.sub(r"\1_1\2", s_ambient.path)
            s_ambient.id = 22
            self.add_entry(s_ambient)
            self.add_entry(s_ambient_0)
        for table_name, slots in self.params.items():
            slots[1] = slots[0].copy()

    def update_entries(self):
        """Update `BND` entries by packing the current `DrawParam` instances. Called automatically by `write()`."""
        for param_name, param_table_slots in self.params.items():
            for slot, param_table in enumerate(param_table_slots):
                try:
                    param_table_entry_path = self._slot_entry_paths[param_name, slot]
                except KeyError:
                    continue  # Slot does not exist.
                if param_table is None:
                    self.remove_entry(param_table_entry_path)  # Slot deleted.
                else:
                    self.entries_by_path[param_table_entry_path].set_uncompressed_data(param_table.pack())

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, **pack_kwargs):
        """Write to `DrawParamBND` file after updating entries."""
        self.update_entries()
        super().write(file_path, make_dirs, **pack_kwargs)


class DrawParamDirectory(GameSpecificType, abc.ABC):

    # Lod (default only), EnvLightTex (useless) and DebugAmbientLight (useless) are left out.
    PARAM_NAMES = (
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
    )

    DRAW_PARAM_BND_CLASS: tp.Type[DrawParamBND] = None
    DRAW_PARAM_MAPS: dict[str, str] = {}

    def __init__(self, draw_param_directory=None, paramdef_bnd=None):
        """Unpack `DrawParamBND`s into a single modifiable structure.

        Opens all DrawParam BNDs simultaneously for editing and repacking. The appropriate bundled ParamDef file will be
        loaded automatically if not given.

        Args:
            draw_param_directory: Directory where all the 'aXX_DrawParam.parambnd[.dcx]' files are. This will be inside
                'params/DrawParam' in your game directory..
        """

        self._reload_warning_given = True
        self.bnds = {}

        if draw_param_directory is None:
            return

        self._draw_param_directory = Path(draw_param_directory)

        for map_name in self.DRAW_PARAM_MAPS:
            map_prefix = map_name if map_name == "default" else f"a{map_name[1:]}"
            file_map_name = self.GAME.dcxify(f"{map_prefix}_DrawParam.parambnd")
            draw_param_bnd_path = self._draw_param_directory / file_map_name
            self.bnds[file_map_name] = self.DRAW_PARAM_BND_CLASS(draw_param_bnd_path, paramdef_bnd)
            setattr(self, map_name, self.bnds[file_map_name])

    def __getitem__(self, bnd_file_name):
        if bnd_file_name not in self.bnds:
            raise KeyError(f"Invalid `DrawParamBND` file name: '{bnd_file_name}'")
        return self.bnds[bnd_file_name]

    def __iter__(self):
        return iter(self.bnds.items())

    def get_draw_param_bnd(self, map_name: str) -> DrawParamBND:
        return getattr(self, map_name)

    def pickle(self, pickle_path):
        """Save the entire `DarkSoulsLightingParameters` instance to a pickled file, which will be faster to load."""
        with Path(pickle_path).open("wb") as f:
            pickle.dump(self, f)

    def write(self, draw_param_directory=None):
        if not draw_param_directory:
            draw_param_directory = self._draw_param_directory
        draw_param_directory = Path(draw_param_directory)
        for bnd_file_name, map_draw_param in self.bnds.items():
            map_draw_param.write(draw_param_directory / bnd_file_name)
        _LOGGER.info("DrawParamDirectory written successfully.")
        if not self._reload_warning_given:
            _LOGGER.info("Remember to reload your game to see changes.")
            self._reload_warning_given = True
