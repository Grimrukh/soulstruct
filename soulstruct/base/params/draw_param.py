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
from soulstruct.utilities.files import read_json, write_json

from .paramdef import ParamDefBND

if tp.TYPE_CHECKING:
    from .param import Param

_LOGGER = logging.getLogger(__name__)

_DRAW_PARAM_FILE_NAME_RE = re.compile(r"([ms]\d\d|default)(_\d)?(_[\w]+\.param)")  # e.g. 'm12_1_LensFlare.param'
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

    def __init__(self, draw_param_bnd_source=None, dcx_magic=(), paramdef_bnd=None, use_json=False):
        """Structure that manages double-slots and table nicknames for one `DrawParamBND` file (i.e. one map "area")."""
        self.params = {}  # type: dict[str, list[tp.Optional[Param], tp.Optional[Param]]]
        self._slot_entry_paths = {}  # type: dict[tuple[str, int], str]

        if paramdef_bnd is None:
            self.paramdef_bnd = self.GET_BUNDLED_PARAMDEF()
        elif isinstance(paramdef_bnd, ParamDefBND):
            self.paramdef_bnd = paramdef_bnd
        else:
            raise TypeError(f"`paramdef_bnd` must be None or an existing `ParamDefBND`, not {type(paramdef_bnd)}.")

        if use_json:  # source is a folder with individual `*Param.json` files and a manifest
            super().__init__(None, dcx_magic=dcx_magic)
            self.load_json_dir(draw_param_bnd_source, clear_old_data=True)
        else:  # must be a standard `BaseBND` source
            super().__init__(draw_param_bnd_source, dcx_magic=dcx_magic)

        if self.params:
            return  # already generated

        for entry in self.entries:
            if not (match := _DRAW_PARAM_FILE_NAME_RE.match(entry.name)):
                raise ValueError(f"Malformed `DrawParam` BND entry name: '{entry.name}'")
            slot = int(match.group(2)[1]) if match.group(2) else 0
            if slot not in {0, 1}:
                raise ValueError(
                    "Only slot 0 (`mXX_ParamName.param`) and slot 1 (`mXX_1_ParamName.param`) are valid in file name."
                )
            param_name = match.group(3).strip("_")
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

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, check_hash=False, **pack_kwargs):
        """Write to `DrawParamBND` file after updating entries."""
        self.update_entries()
        super().write(file_path, make_dirs, check_hash=check_hash, **pack_kwargs)

    def load_json_dir(self, directory: tp.Union[Path, str], clear_old_data=True):
        """Load individual Param JSON files from an unpacked Binder folder (produced by `write_json_dir()`).

        The names of the Param JSON files to be loaded from the folder are recorded in the "entries" key of the
        `GameParamBND_manifest.json` file.

        Functionally very similar to `load_dict()`, but avoids the need for one gigantic JSON file for all Params.
        """
        directory = Path(directory)
        manifest_path = directory / "DrawParamBND_manifest.json"
        if not manifest_path.is_file():
            raise FileNotFoundError(f"Could not find `DrawParamBND` manifest file '{manifest_path}'.")
        manifest = read_json(manifest_path)
        for field, value in self.get_manifest_header(manifest).items():
            if not clear_old_data:
                if (old_value := getattr(self, field)) != value:
                    raise ValueError(f"New `{field}` value {repr(value)} does not match old value {repr(old_value)}.")
            else:
                setattr(self, field, value)

        if clear_old_data:
            self._entries.clear()
            self.params = {}  # type: dict[str, list[tp.Optional[Param], tp.Optional[Param]]]
            entry_ids = set()
        else:
            entry_ids = set(self.entries_by_id.keys())
        for json_name in manifest["entries"]:
            # The rest of the JSON file name doesn't actually matter; we use the BND "path" within to identify it.
            try:
                param_dict = read_json(directory / json_name, encoding="shift_jis")
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find DrawParam JSON file '{directory / json_name}'.")
            for field in ("entry_id", "path", "flags", "data"):
                if field not in param_dict:
                    raise KeyError(
                        f"Field `{field}` not specified in '{json_name}' in `DrawParamBND` folder."
                    )
            path_name = Path(param_dict["path"]).name
            if not (match := _DRAW_PARAM_FILE_NAME_RE.match(path_name)):
                raise ValueError(f"Invalid `DrawParam` path name in '{json_name}': '{path_name}'")
            slot = int(match.group(2)[1]) if match.group(2) else 0
            if slot not in {0, 1}:
                raise ValueError(
                    "Only slot 0 (`mXX_ParamName.param`) and slot 1 (`mXX_1_ParamName.param`) are valid in file name."
                )
            param_name = match.group(3).strip("_")
            if match.group(1).startswith("s"):
                param_name = "s_" + param_name

            undecodable_row_names = self.UNDECODABLE_ROW_NAMES.get(param_name, ())
            p = self.DRAW_PARAM_CLASS(
                param_dict["data"],
                paramdef_bnd=self.paramdef_bnd,
                undecodable_row_names=undecodable_row_names,
            )
            entry = self.BinderEntry(p.pack(), param_dict["entry_id"], param_dict["path"], param_dict["flags"])
            if entry.id in entry_ids:
                _LOGGER.warning(
                    f"Binder entry ID {entry.id} appears more than once in this `DrawParamBND`. Fix this ASAP."
                )
            self._entries.append(entry)

            self.params.setdefault(param_name, [None, None])[slot] = p
            self._slot_entry_paths[param_name, slot] = param_dict["path"]
            if not match.group(1).startswith("s") and p.param_info is not None:
                # sXX_LightBank does not have attribute access.
                setattr(self, p.nickname, self.params[param_name])

    def write_json_dir(self, directory: tp.Union[Path, str], ignore_pads=True, ignore_defaults=True):
        """Write a folder containing a `GameParamBND_manifest.json` file with standard `Binder` header information and
        a list of Param JSON files to load from the same folder.

        The resulting folder can be loaded with `load_json_dir(directory)`.
        """
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        manifest = self.get_json_header()
        manifest.pop("use_id_prefix")
        manifest["entries"] = []

        for param_name, param_slots in self.params.items():
            for slot, p in enumerate(param_slots):
                if p is None:
                    continue
                entry = self.entries_by_path[self._slot_entry_paths[param_name, slot]]
                param_dict = {
                    "entry_id": entry.id,
                    "path": entry.path,
                    "flags": entry.flags,
                    "data": p.to_dict(ignore_pads=ignore_pads, ignore_defaults=ignore_defaults),
                }
                nickname = param_name.split(".")[0] if p.nickname is None else p.nickname
                json_name = f"{nickname}_{slot}.json"
                if param_name.startswith("s_"):
                    json_name = "s_" + json_name
                write_json(directory / json_name, param_dict, encoding="shift-jis")
                manifest["entries"].append(json_name)

        write_json(directory / "DrawParamBND_manifest.json", manifest)


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

    def __init__(self, draw_param_directory=None, paramdef_bnd=None, use_json=False):
        """Unpack `DrawParamBND`s into a single modifiable structure.

        Opens all DrawParam BNDs simultaneously for editing and repacking. The appropriate bundled ParamDef file will be
        loaded automatically if not given.

        Args:
            draw_param_directory: Directory where all the 'aXX_DrawParam.parambnd[.dcx]' files are. This will be inside
                'params/DrawParam' in your game directory.
        """

        self._reload_warning_given = True
        self.bnds = {}

        if draw_param_directory is None:
            return

        self._draw_param_directory = Path(draw_param_directory)

        if use_json:
            self.load_json_dir(draw_param_directory, clear_old_data=False)
            return

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

    def load_json_dir(self, directory: tp.Union[Path, str], clear_old_data=True):
        directory = Path(directory)
        for map_name in self.DRAW_PARAM_MAPS:
            try:
                draw_param_bnd = getattr(self, map_name)
            except AttributeError:
                map_prefix = map_name if map_name == "default" else f"a{map_name[1:]}"
                file_map_name = self.GAME.dcxify(f"{map_prefix}_DrawParam.parambnd")
                self.bnds[file_map_name] = self.DRAW_PARAM_BND_CLASS(directory / map_name, use_json=True)
                setattr(self, map_name, self.bnds[file_map_name])
            else:
                # Modify existing `DrawParamBND`.
                draw_param_bnd.load_json_dir(directory / map_name, clear_old_data=clear_old_data)

    def write_json_dir(self, directory: tp.Union[Path, str], ignore_pads=True, ignore_defaults=True):
        directory = Path(directory)
        for map_name in self.DRAW_PARAM_MAPS:
            getattr(self, map_name).write_json_dir(
                directory / map_name, ignore_pads=ignore_pads, ignore_defaults=ignore_defaults
            )
