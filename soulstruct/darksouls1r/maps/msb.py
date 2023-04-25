__all__ = ["MSB"]

import logging
import typing as tp
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from soulstruct.base.maps.utilities import MAP_SOURCE_TYPING
from soulstruct.darksouls1ptde.maps.msb import MSB as _PTDE_MSB, MSBSupertype

from .constants import VANILLA_MSB_TRANSLATIONS, get_map
from .models import MSBModel
from .events import MSBEvent
from .regions import MSBRegion
from .parts import MSBPart
from .utilities import import_map_piece_flver

_LOGGER = logging.getLogger(__name__)


# TODO: Move to base and use in other game MSBs.
ENTRY_T = tp.TypeVar("ENTRY_T", MSBModel, MSBEvent, MSBRegion, MSBPart)


class FindEntry(tp.Protocol[ENTRY_T]):
    def __call__(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> ENTRY_T:
        ...


@dataclass(slots=True, kw_only=True)
class MSB(_PTDE_MSB):
    """Only difference from DS1PTDE is in the methods."""

    find_model_name: tp.ClassVar[FindEntry[MSBModel]]
    find_event_name: tp.ClassVar[FindEntry[MSBEvent]]
    find_region_name: tp.ClassVar[FindEntry[MSBRegion]]
    find_part_name: tp.ClassVar[FindEntry[MSBPart]]

    def translate_entity_id_names(self):
        """Apply my hand-crafted translations of all vanilla Japanese DS1 MSB names (mostly those with entity IDs).

        TODO: Can probably go in PTDE subclass. (Just not sure if there are old PTDE Arena event needing translation.)
        """
        supertypes = {MSBSupertype.EVENTS, MSBSupertype.REGIONS}
        for subtype_name, game_type in self.ENTITY_GAME_TYPES.items():
            translated_entity_ids = set()  # reset per entry type
            entry_list = self[subtype_name]
            if entry_list.supertype not in supertypes:
                continue  # parts and models do not need translation (already English and unique)
            for entry in entry_list:
                if entry.entity_id not in {-1, 0}:
                    if entry.entity_id in translated_entity_ids:
                        _LOGGER.warning(f"Found repeated entity ID while translating: {entry.entity_id}. Ignored.")
                        continue
                    if entry.entity_id not in VANILLA_MSB_TRANSLATIONS:
                        _LOGGER.warning(f"Unexpected entity ID for vanilla DSR: {entry.entity_id}. Not translated.")
                    else:
                        # old_name = entry.name
                        entry.name = VANILLA_MSB_TRANSLATIONS[entry.entity_id]
                        translated_entity_ids.add(entry.entity_id)

    def import_map_piece_model(
        self,
        source_map: MAP_SOURCE_TYPING,
        source_model_id: int | str,
        dest_map: MAP_SOURCE_TYPING,
        dest_model_id: int | str = None,
        map_directory: Path | str = None,
        overwrite=False,
    ):
        """Import a Map Piece model from `source_map` to `dest_map` (should be this `MSB`).

        Moves the `FLVER` file and adds the `MSBMapPieceModel` entry.

        TODO: Can go in PTDE base class with some tweaks (no DCX extension, mainly).
        """
        source_map = get_map(source_map)
        dest_map = get_map(dest_map)

        if map_directory is None:
            from soulstruct import DSR_PATH
            map_directory = Path(DSR_PATH) / "map"
        else:
            map_directory = Path(map_directory)

        if isinstance(source_model_id, int):
            source_model_id = f"{source_model_id:04d}"
        else:
            source_model_id = source_model_id.lstrip("m")
            if len(source_model_id) == 9 and source_model_id[6] == "A":
                source_model_id = source_model_id[:6]  # remove 'AZZ' area suffix
        if len(source_model_id) == 4:
            source_model_id += f"B{source_map.block_id}"
        elif len(source_model_id) != 6:
            raise ValueError(
                f"`source_model_id` of map piece (excluding 'm' prefix) must be four characters (in which case 'BX' "
                f"will be appended) or the full six. Received: {source_model_id}"
            )

        source_model_name = f"m{source_model_id}A{source_map.area_id:02d}.flver.dcx"
        source_flver_path = map_directory / f"{source_map.msb_file_stem}/{source_model_name}"
        if not source_flver_path.is_file():
            raise FileNotFoundError(f"Could not find source FLVER {source_flver_path}.")

        if dest_model_id is None:  # defaults to "YZXXXX", where the source FLVER is "mXXXXBYAZZ"
            dest_model_id = f"{str(source_map.area_id)[-1]}{str(source_map.block_id)[-1]}{source_model_id[:4]}"
        else:
            if isinstance(dest_model_id, int):
                dest_model_id = f"{dest_model_id:04d}"
            else:
                dest_model_id = dest_model_id.lstrip("m")
            if len(dest_model_id) == 4:
                dest_model_id += f"B{source_map.block_id}"
            elif len(dest_model_id) != 6:
                raise ValueError(
                    f"`dest_model_id` of map piece (excluding 'm' prefix) must be four characters (in which case 'BX' "
                    f"will be appended) or the full six. Received: {dest_model_id}"
                )
        dest_model_name = f"m{dest_model_id}"

        if dest_model_name in self.map_piece_models.get_entry_names():
            raise ValueError(f"There is already a Map Piece model with name 'm{dest_model_id}' in this MSB.")

        dest_flver_path = map_directory / f"{dest_map.msb_file_stem}/{dest_model_name}A{dest_map.area_id:02d}.flver.dcx"

        import_map_piece_flver(source_flver_path, dest_flver_path, overwrite=overwrite)

        new_model = self.map_piece_models.new(name=f"m{dest_model_id}")
        new_model.set_auto_sib_path(dest_map.msb_file_stem)
