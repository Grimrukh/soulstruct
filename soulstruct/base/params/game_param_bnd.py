from __future__ import annotations

import abc
import logging
import typing as tp
from pathlib import Path

from soulstruct.containers.bnd import BaseBND
from soulstruct.utilities.files import read_json, write_json

from .paramdef import ParamDefBND

if tp.TYPE_CHECKING:
    from soulstruct.game_types import BaseGameParam
    from .param import Param


_LOGGER = logging.getLogger(__name__)


class GameParamBND(BaseBND, abc.ABC):

    EXT = ".parambnd"
    Param: tp.Type[Param] = None
    ParamDefBND: tp.Type[ParamDefBND] = None

    PARAM_NICKNAMES: dict[str, str] = {}
    PARAM_TYPES: dict[str, BaseGameParam] = {}

    def __init__(self, game_param_bnd_source=None, dcx_type=None, paramdef_bnd=None, use_json=False):
        """Unpack a `GameParam.gameparambnd[.dcx]` file binder into a single modifiable structure.

        Args:
            game_param_bnd_source: any valid source for GameParam.parambnd[.dcx] (its file path, the directory
                containing it, the unpacked BND directory, or an existing BND instance).
            dcx_type: optional DCX type.
            paramdef_bnd: previously loaded `ParamDefBND` instance, or source to create it. Can also be automatically
                detected from subclass.
            use_json: if `True`, will assume the source is a path to a folder containing `GameParamBND_manifest.json`
                and a `*Param.json` file for each Param to be loaded.
        """

        self._reload_warning_given = True
        self.params = {}  # type: dict[str, Param]
        if paramdef_bnd is None:
            self.paramdef_bnd = self.ParamDefBND()
        self.paramdef_bnd = paramdef_bnd if isinstance(paramdef_bnd, ParamDefBND) else self.ParamDefBND(paramdef_bnd)

        if use_json:  # source is a folder with individual `*Param.json` files and a manifest
            super().__init__(None, dcx_type=dcx_type)
            self.load_json_dir(game_param_bnd_source, clear_old_data=True)
        else:  # must be a standard `BaseBND` source
            super().__init__(game_param_bnd_source, dcx_type=dcx_type)

        if self.params:
            return  # already generated

        for entry in self.entries:
            p = self.params[entry.path] = self.Param(entry.get_uncompressed_data(), paramdef_bnd=self.paramdef_bnd)
            # Preferential nickname source order:
            #     `self.PARAM_NICKNAMES[BinderEntry.stem]`, `p.nickname`, `BinderEntry.stem`
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if p.nickname is None else p.nickname)
            setattr(self, nickname, p)

    def update_bnd_entries(self):
        """Update the `GameParamBND` by packing the current `Param` instances. Called automatically by `write()`."""
        for param_table_entry_path, param_table in self.params.items():
            self.entries_by_path[param_table_entry_path].set_uncompressed_data(param_table.pack())

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, check_hash=False, **pack_kwargs):
        """Write the `GameParamBND` file after updating the binary BND entries from the loadewd `Param` instances.

        See `GameFile.write()` for more.
        """
        self.update_bnd_entries()
        super().write(file_path, make_dirs=make_dirs, check_hash=check_hash, **pack_kwargs)
        _LOGGER.info("GameParamBND written successfully.")
        if not self._reload_warning_given:
            _LOGGER.info("Remember to reload your game to see changes.")
            self._reload_warning_given = True

    def load_dict(self, data: dict, clear_old_data=True):
        if "params" not in data:
            raise KeyError("Field `params` not specified in `GameParamBND` dict.")
        for field, value in self.get_manifest_header(data).items():
            if not clear_old_data:
                if (old_value := getattr(self, field)) != value:
                    raise ValueError(f"New `{field}` value {repr(value)} does not match old value {repr(old_value)}.")
            else:
                setattr(self, field, value)
        if clear_old_data:
            self._entries.clear()
            entry_ids = set()
        else:
            entry_ids = set(self.entries_by_id.keys())
        for i, param_dict in enumerate(data["params"]):
            for field in ("entry_id", "path", "flags", "data"):
                if field not in param_dict:
                    raise KeyError(f"Field `{field}` not specified in 'params[{i}]' in `GameParamBND` dict.")
            param = self.Param(param_dict["data"], paramdef_bnd=self.paramdef_bnd)
            entry = self.BinderEntry(param.pack(), param_dict["entry_id"], param_dict["path"], param_dict["flags"])
            if entry.id in entry_ids:
                _LOGGER.warning(
                    f"Binder entry ID {entry.id} appears more than once in this `GameParamBND`. Fix this ASAP."
                )
            self._entries.append(entry)
            entry_ids.add(entry.id)
            p = self.params[entry.path] = param
            # Preferential nickname source order:
            #     `self.PARAM_NICKNAMES[BinderEntry.stem]`, `p.nickname`, `BinderEntry.stem`
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if p.nickname is None else p.nickname)
            setattr(self, nickname, p)

    def to_dict(self, ignore_pads=True, ignore_defaults=True) -> dict[str, tp.Any]:
        """Convert entire `GameParamBND` to a single dictionary with both the `Binder` header and all Param data."""
        data = self.get_json_header()
        data.pop("use_id_prefix")
        data["params"] = []
        for path, param in self.params.items():
            entry = self.entries_by_path[path]
            param_dict = param.to_dict(ignore_pads=ignore_pads, ignore_defaults=ignore_defaults)
            data["params"].append({
                "entry_id": entry.id,
                "path": path,
                "flags": entry.flags,
                "data": param_dict,
            })
        return data

    def load_json_dir(self, directory: tp.Union[Path, str], clear_old_data=True):
        """Load individual Param JSON files from an unpacked Binder folder (produced by `write_json_dir()`).

        The names of the Param JSON files to be loaded from the folder are recorded in the "entries" key of the
        `GameParamBND_manifest.json` file.

        Functionally very similar to `load_dict()`, but avoids the need for one gigantic JSON file for all Params.
        """
        directory = Path(directory)
        manifest_path = directory / "GameParamBND_manifest.json"
        if not manifest_path.is_file():
            raise FileNotFoundError(f"Could not find GameParamBND manifest file '{manifest_path}'.")
        manifest = read_json(manifest_path)
        for field, value in self.get_manifest_header(manifest).items():
            if not clear_old_data:
                if (old_value := getattr(self, field)) != value:
                    raise ValueError(f"New `{field}` value {repr(value)} does not match old value {repr(old_value)}.")
            else:
                setattr(self, field, value)

        if clear_old_data:
            self._entries.clear()
            entry_ids = set()
        else:
            entry_ids = set(self.entries_by_id.keys())
        for json_name in manifest["entries"]:
            try:
                param_dict = read_json(directory / json_name, encoding="utf-8")
            except FileNotFoundError:
                raise FileNotFoundError(f"Could not find Param JSON file '{directory / json_name}'.")
            for field in ("entry_id", "path", "flags", "data"):
                if field not in param_dict:
                    raise KeyError(
                        f"Field `{field}` not specified in '{json_name}' in `GameParamBND` folder."
                    )
            param = self.Param(param_dict["data"], paramdef_bnd=self.paramdef_bnd)
            entry = self.BinderEntry(param.pack(), param_dict["entry_id"], param_dict["path"], param_dict["flags"])
            if entry.id in entry_ids:
                _LOGGER.warning(
                    f"Binder entry ID {entry.id} appears more than once in this `GameParamBND`. Fix this ASAP."
                )
            self._entries.append(entry)
            p = self.params[entry.path] = param
            # Preferential nickname source order:
            #     `self.PARAM_NICKNAMES[BinderEntry.stem]`, `p.nickname`, `BinderEntry.stem`
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if p.nickname is None else p.nickname)
            setattr(self, nickname, p)

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

        for path, param in self.params.items():
            entry = self.entries_by_path[path]
            param_dict = {
                "entry_id": entry.id,
                "path": path,
                "flags": entry.flags,
                "data": param.to_dict(ignore_pads=ignore_pads, ignore_defaults=ignore_defaults),
            }
            nickname = self.PARAM_NICKNAMES.get(entry.stem, entry.stem if param.nickname is None else param.nickname)
            json_name = nickname + ".json"
            write_json(directory / json_name, param_dict, encoding="utf-8", ensure_ascii=False)
            manifest["entries"].append(json_name)

        write_json(directory / "GameParamBND_manifest.json", manifest)

    def get_param(self, param_nickname) -> Param:
        if param_nickname not in self.PARAM_TYPES:
            raise ValueError(f"Invalid param nickname: {param_nickname}")
        return getattr(self, param_nickname)

    # TODO: Inherit from some abstract `ProjectData` class that provides this interface.
    def get_range(self, param_nickname, start, count):
        """Get a list of (id, entry) pairs from a certain range inside ID-sorted param dictionary."""
        return getattr(self, param_nickname).get_range(start, count)
