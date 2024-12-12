"""Generates Python enum files for MSB entities for use as EMEVD arguments."""
from __future__ import annotations

__all__ = [
    "EnumModuleGenerator",
]

import logging
import re
from pathlib import Path

from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.games import Game
from soulstruct.utilities.text import PY_NAME_RE
from soulstruct.utilities.misc import IDList

from .msb import MSB, MSBEntry, MSBEntryList
from .msb.region_shapes import RegionShapeType

_LOGGER = logging.getLogger("soulstruct")

MAP_NAME_RE = re.compile(r"m(\d{2})_(\d{2})_(\d{2})_(\d{2})")
TRAILING_DIGIT_RE = re.compile(r"(.*?)(\d+)")


class EnumModuleGenerator:

    msb: MSB
    path: Path
    map_stem: str
    game: Game

    def __init__(self, msb: MSB, map_stem: str = None):
        self.msb = msb
        self.path = msb.path
        self.map_stem = map_stem or self.path.name.split(".")[0]
        self.game = self.msb.get_game()

    def write_enums_module(
        self,
        output_module_path: str | Path = None,
        append_to_module: str = "",
        separate_region_points_volumes: bool = False,
        sort_by_id=False,
    ):
        """Generates a '{mXX_YY}_enums.py' file with entity IDs for import into EVS scripts.

        If `append_to_module` text is given, all map enums will be appended to it.

        If `separate_region_points_volumes` is True, separate enums called `RegionPoints` and `RegionVolumes` (both
        inheriting from `Region`) will be created for `Region` entities based on their shape. This is useful for clearer
        arguments for EMEVD instructions like `IsInsideRegion`, so you're less likely to use shapeless Points.
        """
        if not (match := MAP_NAME_RE.match(self.map_stem)):
            _LOGGER.warning(
                f"Unusual map stem detected in `EnumModuleGenerator`: {self.map_stem}. Enum ID ranges will not be "
                f"applied to enum classes."
            )
            auto_map_base_id = None
        else:
            aa_id, bb_id, cc_id, dd_id = map(int, match.group(1, 2, 3, 4))
            if aa_id in {60, 61}:
                if dd_id not in {0, 1, 2}:
                    _LOGGER.warning(
                        f"Elden Ring overworld map tile size is invalid: {self.map_stem}. "
                        f"Enum ID ranges will not be applied to enum classes."
                    )
                    auto_map_base_id = None
                elif dd_id != 0:
                    # Silently disable map ID ranges, since the true base entity ID for this map depends on the small
                    # tile that each entity is actually in.
                    auto_map_base_id = None
                else:
                    # Elden Ring ten-digit overworld map format (small tiles).
                    # Note that these match flags in Elden Ring.
                    auto_map_base_id = int(f"10{bb_id:02d}{cc_id:02d}0000")
            elif self.game.variable_name == "ELDEN_RING":
                # Standard eight-digit format.
                auto_map_base_id = int(f"{aa_id:02d}{bb_id:02d}0000")
            else:
                # Older seven-digit format (single block digit).
                auto_map_base_id = int(f"{aa_id:02d}{bb_id:01d}{cc_id:02d}00")

        if output_module_path is None:
            if self.path is None:
                raise ValueError("Cannot auto-detect MSB entities `module_path` (MSB path not known).")
            output_module_path = self.path.parent / f"{self.path.name.split('.')[0]}_enums.py"
        else:
            output_module_path = Path(output_module_path)

        output_module_path.parent.mkdir(parents=True, exist_ok=True)

        game_types_import = f"from soulstruct.{self.game.submodule_name}.game_types import *"
        if append_to_module:
            if game_types_import not in append_to_module:
                # Add game type start import to module. (Very rare that it wouldn't already be there.)
                first_class_def_index = append_to_module.find("\nclass")
                if first_class_def_index != -1:
                    append_to_module = append_to_module.replace("\nclass", game_types_import + "\n\nclass", 1)
                else:
                    append_to_module += game_types_import
            module_text = append_to_module.rstrip("\n") + "\n"
        else:
            module_text = game_types_import

        for subtype_name, subtype_game_type in self.msb.ENTITY_GAME_TYPES.items():

            if separate_region_points_volumes and subtype_name == "regions":
                # Two subtypes: `RegionPoints` and `RegionVolumes`.

                volume_shape_types = RegionShapeType.get_volume_types()
                other_shape_types = RegionShapeType.get_2d_types()

                for class_name, region_predicate in (
                    ("RegionPoints", lambda r: r.shape.SHAPE_TYPE == RegionShapeType.Point),
                    ("RegionVolumes", lambda r: r.shape.SHAPE_TYPE in volume_shape_types),
                    ("Region2D", lambda r: r.shape.SHAPE_TYPE in other_shape_types),  # shouldn't exist but won't ignore
                ):
                    filtered_regions = IDList([region for region in self.msb.get_regions() if region_predicate(region)])

                    if filtered_regions:
                        class_contents = self._get_enum_class_contents(filtered_regions, sort_by_id)
                        if class_contents:
                            class_def = self._get_enum_class_def(class_name, subtype_game_type, auto_map_base_id)
                            module_text += "\n" + class_def + class_contents

            else:
                # Standard: just one enum per subtype.
                class_name = subtype_game_type.get_msb_entry_supertype_subtype(pluralized_subtype=True)[1]
                subtype_list = getattr(self.msb, subtype_name)  # type: MSBEntryList
                if subtype_list:
                    class_contents = self._get_enum_class_contents(subtype_list, sort_by_id)
                    # If no entries in the list have entity IDs, `class_contents` will be empty.
                    if class_contents:
                        class_def = self._get_enum_class_def(class_name, subtype_game_type, auto_map_base_id)
                        module_text += "\n" + class_def + class_contents

        module_text += "\n"  # trailing newline

        with output_module_path.open("w", encoding="utf-8") as f:
            f.write(module_text)

    def _get_enum_class_contents(self, entry_list: IDList[MSBEntry], sort_by_id: bool) -> str:
        """Iterate over all MSB entries in the given list and return a string of definitions for an enum class.

        `entry_list` does not have to be a real `MSBEntryList`; just an `IDList[MSBEntry]`.
        """
        entity_id_dict = self._get_entity_id_dict(entry_list, sort_by_entity_id=sort_by_id)
        sorted_entity_id_dict = {
            k: v for k, v in sorted(entity_id_dict.items(), key=self._sort_key)
        }

        class_lines = []
        last_is_non_ascii = False
        for entity_id, entry in sorted_entity_id_dict.items():
            # name = entry.name.replace(" ", "_")
            try:
                name = entry.name.encode("utf-8").decode("ascii")
            except UnicodeDecodeError:
                if not last_is_non_ascii:
                    class_lines.append("# TODO: Non-ASCII name characters.")
                    last_is_non_ascii = True
                class_lines.append(f"# {entry.name} = {entity_id}")  # invalid name commented out
            else:
                last_is_non_ascii = False
                if not PY_NAME_RE.match(name):
                    class_lines.append(f"# TODO: Invalid Python variable name.")
                    class_lines.append(f"# {entry.name} = {entity_id}")  # invalid name commented out
                else:
                    class_lines.append(f"{name} = {entity_id}")
            if entry.description:
                class_lines[-1] += f"  # {entry.description}"

        if not class_lines:
            return ""

        return "    " + "\n    ".join(class_lines)

    def _get_enum_class_def(
        self, class_name: str, subtype_game_type: type[MapEntity], auto_map_base_id: int | None
    ) -> str:
        """Create class definition and docstring string."""
        game_type_name = subtype_game_type.__name__
        if auto_map_base_id is not None and subtype_game_type in self.msb.ID_RANGES:
            range_kwargs = self.msb.ID_RANGES[subtype_game_type](auto_map_base_id)
            try:
                first_value = range_kwargs["first_value"]
                last_value = range_kwargs["last_value"]
            except KeyError:
                _LOGGER.warning(
                    f"`ID_RANGES` callback for {game_type_name} did not return `first_value` and `last_value`."
                )
                class_def = f"\n\nclass {class_name}({game_type_name}):\n"
            else:
                class_def = f"\n\nclass {class_name}({game_type_name}, {first_value=}, {last_value=}):\n"
        else:
            class_def = f"\n\nclass {class_name}({game_type_name}):\n"
        class_def += f"    \"\"\"`{game_type_name}` entity IDs for MSB and EVS use.\"\"\"\n\n"
        return class_def

    def _get_entity_id_dict(self, entries: IDList[MSBEntry], sort_by_entity_id=False) -> dict[int, MSBEntry]:
        """Get a dictionary mapping entity IDs to `MSBEntry` instances for this subtype list.

        If multiple `MSBEntry` instances are found for a given ID, a warning is logged, and only the *first* one found
        is used (which matches game engine behavior).

        Raises a `TypeError` if `entity_id` is not defined on this subtype.
        """
        entries_by_id = {}
        for entry in entries:
            entity_id = entry.get_entity_id()
            if entity_id is None:
                raise TypeError(f"`entity_id` is not a valid field for MSB entry `{entry.name}`.")
            if entity_id <= 0:
                continue  # ignore null ID
            if entity_id in entries_by_id:
                _LOGGER.warning(
                    f"{self.map_stem}: Found multiple entries for entity ID {entity_id}. Using first only (in MSB "
                    f"entry order), which is what the game engine will do with this ID."
                )
            else:
                entries_by_id[entity_id] = entry
        if sort_by_entity_id:
            entries_by_id = {k: entries_by_id[k] for k in sorted(entries_by_id.keys())}
        return entries_by_id

    @staticmethod
    def _sort_key(key_value) -> tuple[str, int]:
        """Sort trailing digits properly."""
        _, value_ = key_value
        if match := TRAILING_DIGIT_RE.match(value_.name):
            return match.group(1), int(match.group(2))
        return value_.name, 0
