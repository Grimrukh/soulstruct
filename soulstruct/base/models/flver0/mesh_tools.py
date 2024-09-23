from __future__ import annotations

__all__ = [
    "SplitSubmeshDef",
    "MergedMesh",
]

import logging
import multiprocessing
import typing as tp
from dataclasses import dataclass

from soulstruct.base.models.base.mesh_tools import SplitSubmeshDef, BaseMergedMesh
from .material import Material
from .vertex_array import VertexArray
from .submesh import Submesh

if tp.TYPE_CHECKING:
    from .core import FLVER0

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MergedMesh(BaseMergedMesh):

    MATERIAL: tp.ClassVar[type[Material]] = Material
    VERTEX_ARRAY: tp.ClassVar[type[VertexArray]] = VertexArray
    SUBMESH: tp.ClassVar[type[Submesh]] = Submesh

    @classmethod
    def from_flver_batch(
        cls,
        flvers: list[FLVER0],
        merged_mesh_args: list[tuple[tuple[int, ...], tuple[tuple[str, ...], ...], bool]],
        processes: int = None,
    ) -> list[tp.Self | None]:
        """Use multiprocessing to create `MergedMesh` instances from given `FLVER` instances and args in parallel.

        Failed conversions will put `None` into list rather than `MergedMesh`.
        """
        mp_args = [
            (flver, *args) for flver, args in zip(flvers, merged_mesh_args, strict=True)
        ]

        with multiprocessing.Pool(processes=processes) as pool:
            merged_meshes = pool.starmap(_from_flver_mp, mp_args)  # blocks here until all done

        return merged_meshes


def _from_flver_mp(
    flver: FLVER0,
    submesh_material_indices: list[int],
    material_uv_layer_names: list[list[str]],
    merge_vertices: bool,
) -> MergedMesh | None:
    if not flver.submeshes:
        _LOGGER.info(f"FLVER0 '{flver.path_name}' has no submeshes. No MergedMesh created.")
        return None
    try:
        return MergedMesh.from_flver(flver, submesh_material_indices, material_uv_layer_names, merge_vertices)
    except Exception as ex:
        _LOGGER.error(f"Failed to load FLVER0 '{flver.path_name}' as MergedMesh: {ex}")
        return None
