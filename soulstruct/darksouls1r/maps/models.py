__all__ = ["MSBModel", "MSBModelList"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.config import DSR_PATH
from soulstruct.darksouls1ptde.maps.models import (
    MSBModel,
    MSBModelList as _BaseMSBModelList,
)
from .constants import get_map
from .utilities import import_map_piece_flver

_LOGGER = logging.getLogger(__name__)


class MSBModelList(_BaseMSBModelList):

    def import_map_piece_model(
        self,
        source_map,
        source_model_id: tp.Union[int, str],
        dest_map,
        dest_model_id: tp.Union[int, str] = None,
        map_directory: tp.Union[None, str, Path] = None,
        overwrite=False,
    ):
        """Import a Map Piece model from `source_map` to `dest_map` (should be this map)."""
        source_map = get_map(source_map)
        dest_map = get_map(dest_map)

        map_directory = Path(map_directory) if map_directory is not None else Path(DSR_PATH) / "map"

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

        if dest_model_name in self.get_entry_names("MapPiece"):
            raise ValueError(f"There is already a Map Piece model with name 'm{dest_model_id}' in this MSB.")

        dest_flver_path = map_directory / f"{dest_map.msb_file_stem}/{dest_model_name}A{dest_map.area_id:02d}.flver.dcx"

        import_map_piece_flver(source_flver_path, dest_flver_path, overwrite=overwrite)

        self.new_map_piece_model(model_subtype="MapPiece", name=f"m{dest_model_id}")
