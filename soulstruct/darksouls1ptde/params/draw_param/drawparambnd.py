from __future__ import annotations

__all__ = ["DrawParamBND"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry, BinderVersion
from soulstruct.darksouls1ptde.game_types.param_types import *
from soulstruct.games import DARK_SOULS_PTDE
from soulstruct.utilities.files import read_json, write_json
from soulstruct.utilities.misc import BiDict

from soulstruct.base.params.paramdef import ParamDefBND

from .core import DrawParam
from ..paramdef import GET_BUNDLED_PARAMDEFBND

try:
    Self = tp.Self
except AttributeError:
    Self = "DrawParamBND"

_LOGGER = logging.getLogger(__name__)

_DRAW_PARAM_FILE_NAME_RE = re.compile(r"([ms]\d\d|default)(_\d)?(_\w+)\.param")  # e.g. 'm12_1_LensFlare.param'


def draw_param_property(draw_param_stem: str):
    return property(lambda self: self.draw_params[draw_param_stem])


@dataclass(slots=True)
class DrawParamBND(Binder):
    """Structure that manages double-slots and DrawParam nicknames for one `DrawParamBND` file (i.e. one map "area")."""

    EXT: tp.ClassVar[str] = ".parambnd"
    DRAW_PARAM_CLASS: tp.ClassVar[tp.Type[DrawParam]] = DrawParam
    GET_BUNDLED_PARAMDEFBND: tp.ClassVar[tp.Callable] = staticmethod(GET_BUNDLED_PARAMDEFBND)
    PARAM_NICKNAMES: tp.ClassVar[BiDict[str, str]] = BiDict(
        ("DofBank", "DepthOfField"),
        ("EnvLightTexBank", "EnvLightTex"),  # unused
        ("FogBank", "Fog"),
        ("LensFlareBank", "LensFlares"),
        ("LensFlareExBank", "LensFlareSources"),
        ("LightBank", "BakedLight"),
        ("ScatteredLightBank", "ScatteredLight"),
        ("PointLightBank", "PointLights"),
        ("ShadowBank", "Shadows"),
        ("ToneCorrectBank", "ToneCorrection"),
        ("ToneMapBank", "ToneMapping"),
        ("s_LightBank", "s_BakedLight"),  # unused (debug)
    )
    PARAM_TYPES: tp.ClassVar[dict[str, BaseGameParam]] = {
        "DofBank": DepthOfFieldParam,
        "EnvLightTexBank": None,  # unused
        "FogBank": FogParam,
        "LensFlareBank": LensFlareParam,
        "LensFlareExBank": LensFlareSourceParam,
        "LightBank": BakedLightParam,
        "ScatteredLightBank": ScatteredLightParam,
        "PointLightBank": PointLightParam,
        "ShadowBank": ShadowParam,
        "ToneCorrectBank": ToneCorrectionParam,
        "ToneMapBank": ToneMappingParam,
        "s_LightBank": BakedLightParam,
    }

    # NOTE: Not using this anymore, but here for documentation.
    KNOWN_UNDECODABLE_ROW_NAMES: tp.ClassVar[dict[str, bytes]] = {
        "LightBank": (b"\x80\x1e", b"\xfe\x1e"),  # invalid single-character used in both versions of DS1
        "s_LightBank": (b"\x80\x1e", b"\xfe\x1e"),  # invalid single-character used in both versions of DS1
    }

    dcx_type = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    # Map area whose lighting is defined by this `DrawParamBND` (e.g. `m15` for Sen's Fortress and Anor Londo). Used to
    # generate correct file names when writing; will raise a `ValueError` if it is still empty at that time. Note that
    # the `DrawParamBND` file stems use `aXX` instead of the `mXX` stored here (as used in the `DrawParam` names). `sXX`
    # prefixed `DrawParam` names are handled automatically.
    map_area: str = ""
    # Maps DrawParam game stems, e.g. 'LightBank', to a pair of two `DrawParam`s for the two slots. These `DrawParam`s
    # (usually the second) may be `None` if that slot is not used.
    draw_params: dict[str, list[DrawParam | None, DrawParam | None]] = field(default_factory=dict)

    DepthOfField = draw_param_property("DofBank")  # type: list[DrawParam]
    # EnvLightTex = draw_param_property("EnvLightTexBank")  # type: list[DrawParam]
    Fog = draw_param_property("FogBank")  # type: list[DrawParam]
    LensFlares = draw_param_property("LensFlareBank")  # type: list[DrawParam]
    LensFlareSources = draw_param_property("LensFlareExBank")  # type: list[DrawParam]
    BakedLight = draw_param_property("LightBank")  # type: list[DrawParam]
    ScatteredLight = draw_param_property("ScatteredLightBank")  # type: list[DrawParam]
    PointLights = draw_param_property("PointLightBank")  # type: list[DrawParam]
    Shadows = draw_param_property("ShadowBank")  # type: list[DrawParam]
    ToneCorrection = draw_param_property("ToneCorrectBank")  # type: list[DrawParam]
    ToneMapping = draw_param_property("ToneMapBank")  # type: list[DrawParam]
    # DebugBakedLight = draw_param_property("s_LightBank")  # type: list[DrawParam]

    def __post_init__(self):
        if not self.draw_params and self.entries:
            return

        # Load from binary Binder source.
        for entry in self.entries:
            if not (match := _DRAW_PARAM_FILE_NAME_RE.match(entry.name)):
                _LOGGER.warning(f"Ignoring malformed `DrawParamBND` entry name: '{entry.name}'")
                continue

            map_area = match.group(1)
            if map_area.startswith("s"):
                map_area = f"m{map_area[1:]}"
            if not self.map_area:
                self.map_area = map_area
            elif map_area != self.map_area:
                raise ValueError(
                    f"Found conflicting map area prefixes in `DrawParamBND` entry names: "
                    f"'{self.map_area}' vs. '{map_area}'"
                )
            slot = int(match.group(2)[1]) if match.group(2) else 0
            if slot not in {0, 1}:
                raise ValueError(
                    "Only slot 0 (`mXX_ParamName.param`) and slot 1 (`mXX_1_ParamName.param`) are valid in "
                    "DrawParam file name."
                )
            param_stem = match.group(3).strip("_")
            if match.group(1).startswith("s"):
                param_stem = "s_" + param_stem

            self.draw_params.setdefault(param_stem, [None, None])

            try:
                self.draw_params[param_stem][slot] = entry.to_game_file(self.DRAW_PARAM_CLASS)  # rows not unpacked yet
            except Exception as ex:
                _LOGGER.error(f"Could not load `DrawParam` from `DrawParamBND` entry '{entry.name}'. Error: {ex}")
                raise

    def unpack_all_param_rows(self, paramdefbnd: ParamDefBND = None):
        """Unpack all row data of all `Param` entries with `paramdefbnd` (defaults to bundled file)."""
        if paramdefbnd is None:
            paramdefbnd = self.DRAW_PARAM_CLASS.GET_BUNDLED_PARAMDEFBND()
        for draw_param_0, draw_param_1 in self.draw_params.values():
            if draw_param_0:
                draw_param_0.unpack_rows(paramdefbnd)
            if draw_param_1:
                draw_param_1.unpack_rows(paramdefbnd)

    def get_draw_param_slot(self, draw_param_stem: str, slot: int) -> DrawParam | None:
        """Get `DrawParam` of given name and slot. Name can be internal or Soulstruct nickname.

        Could return `None` for absent slots."""
        draw_param_stem = draw_param_stem.removesuffix(".param")
        if draw_param_stem in self.PARAM_NICKNAMES.keys():
            return self.draw_params[draw_param_stem][slot]
        if draw_param_stem in self.PARAM_NICKNAMES.values():
            return self.draw_params[self.PARAM_NICKNAMES[draw_param_stem]][slot]
        raise KeyError(f"Invalid `DrawParam` name or nickname: {draw_param_stem}")

    def get_draw_param_entry_path(self, draw_param_stem: str, slot: int) -> str:
        """Use slot and map area to create full entry name, then pass to game's `Param` path generator."""
        if not self.map_area:
            raise ValueError("Cannot generated `DrawParamBND` binder entries without `map_area` set (e.g. 'm12').")
        if draw_param_stem.startswith("s_"):
            map_area = f"s{self.map_area[1:]}"
            draw_param_stem = draw_param_stem[2:]
        else:
            map_area = self.map_area
        if slot == 0:
            entry_name = f"{map_area}_{draw_param_stem}.param"
        elif slot == 1:
            entry_name = f"{map_area}_1_{draw_param_stem}.param"
        else:
            raise ValueError(f"Invalid `DrawParamBND` slot: {slot}. Must be 0 or 1.")
        return self.get_default_entry_path(entry_name)

    def regenerate_entries(self):
        """Regenerate Binder entries from `draw_params` dictionary."""

        # Any existing Binder entries not regenerated here will be removed below.
        regenerated_entry_paths = set()

        for draw_param_stem, draw_param_slots in self.draw_params.items():
            for slot, draw_param in enumerate(draw_param_slots):
                entry_path = self.get_draw_param_entry_path(draw_param_stem, slot)
                regenerated_entry_paths.add(entry_path)
                if entry_path in self.entries_by_path:
                    # Just update data.
                    self.entries_by_path[entry_path].set_from_game_file(draw_param)
                else:
                    # Add new entry.
                    new_id = self.get_first_new_entry_id_in_range(0, 1000000)
                    new_entry = BinderEntry(data=bytes(draw_param), entry_id=new_id, path=entry_path)
                    self.add_entry(new_entry)
                    _LOGGER.debug(f"New `Param` entry added to `DrawParamBND` (ID {new_id}): {new_entry.name}")

        # Remove other entries.
        for entry in list(self.entries):
            if entry.path not in regenerated_entry_paths:
                self.remove_entry(entry)

        self._alphabetize_entry_names()

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
    ):
        if bdt_file_path is not None:
            raise TypeError(
                f"Cannot write `DrawParamBND` to a split `BXF` file. (Invalid `bdt_file_path`: {bdt_file_path})"
            )
        self.regenerate_entries()
        super().write(file_path, make_dirs=make_dirs, check_hash=check_hash)

    @classmethod
    def from_json_directory(cls, directory: Path | str) -> Self:
        """Load individual DrawParam JSON files from an unpacked Binder folder (e.g. from `write_json_directory()`).

        The stems of the DrawParam JSON files to be loaded from the folder are recorded in the `entries` key of the
        `DrawParamBND_manifest.json` file. DrawParams for slot 1 have a '_1' suffix to their JSON stems.
        """
        directory = Path(directory)
        manifest_path = directory / "DrawParamBND_manifest.json"
        if not manifest_path.is_file():
            raise FileNotFoundError(f"Could not find DrawParamBND manifest file '{manifest_path}'.")

        manifest = read_json(manifest_path)
        if "map_area" not in manifest:
            raise ValueError(f"`map_area` key not in `DrawParamBND` JSON manifest: {manifest_path}")
        if "entries" not in manifest:
            raise ValueError(f"`entries` key not in `DrawParamBND` JSON manifest: {manifest_path}")

        manifest["draw_params"] = {}
        for json_stem in manifest.pop("entries"):
            param_stem = cls.PARAM_NICKNAMES[json_stem]
            slot = 1 if param_stem.endswith("_1") else 0
            manifest["draw_params"].setdefault(param_stem, [None, None])
            manifest["draw_params"][param_stem][slot] = cls.DRAW_PARAM_CLASS.from_json(f"{json_stem}.json")

        drawparambnd = cls.from_dict(manifest)
        drawparambnd.path = directory  # TODO: auto-detect better default path, e.g. for binary?
        return drawparambnd

    def write_json_directory(self, directory: Path | str, ignore_pads=True, ignore_defaults=True):
        """Write a folder containing a `DrawParamBND_manifest.json` file with standard `Binder` header information and
        a list of DrawParam JSON file stems to load from the same folder.

        The resulting folder can be loaded with `load_json_directory(directory)`.
        """
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        manifest = self.get_manifest_header()
        manifest.pop("use_id_prefix")
        manifest["entries"] = []

        for draw_param_stem, draw_param_slots in self.draw_params.items():
            for slot, draw_param in enumerate(draw_param_slots):
                json_stem = self.PARAM_NICKNAMES.get(
                    draw_param_stem, draw_param_stem if draw_param.nickname is None else draw_param.nickname
                )
                if slot == 1:
                    json_stem += "_1"
                elif slot != 0:
                    raise ValueError(f"Invalid `DrawParam` slot: {slot}")
                draw_param.write_json(
                    directory / f"{json_stem}.json", ignore_pads=ignore_pads, ignore_defaults=ignore_defaults
                )
                manifest["entries"].append(json_stem)

        write_json(directory / "DrawParamBND_manifest.json", manifest)

    def _alphabetize_entry_names(self):
        """Sort Binder entries (assumed to be just regenerated) by entry name, alphabetically.

        This is how they are sorted in-game. Unlikely to matter, but good to match game behavior.
        """
        new_entries = []
        entries_by_name = self.entries_by_name
        for i, entry_name in enumerate(sorted(entries_by_name.keys())):
            entry = entries_by_name[entry_name]
            entry.entry_id = i
            new_entries.append(entry)
        self.entries = new_entries

    def copy_slot_0_to_slot_1(self, override_existing_slot_1=False):
        """Copy `DrawParam` instances in slot 0 to slot 1.

        If `override_existing_slot_1=False` (default), skips any `DrawParam`s that already have slot 1 data, or have no
        slot 0 data (unusual).
        """
        for draw_param_stem, draw_param_slots in self.draw_params.items():
            if not override_existing_slot_1 and draw_param_slots[1] is not None:
                continue  # skip
            if draw_param_slots[0] is None:
                _LOGGER.warning(f"No slot 0 data for `{draw_param_stem}`. Ignoring.")
                continue
            draw_param_slots[1] = draw_param_slots[0].copy()
