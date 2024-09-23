from __future__ import annotations

__all__ = ["FaceSetFlags", "FaceSet", "Submesh"]

import logging
import random
from dataclasses import dataclass, field

import numpy as np

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.text import indent_lines
from soulstruct.base.models.base.face_set import FaceSet, FaceSetFlags
from soulstruct.base.models.base.submesh import BaseSubmesh

from .material import Material
from .vertex_array import VertexArray
from .vertex_array import VertexArrayLayout

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class Submesh(BaseSubmesh[Material, VertexArrayLayout, VertexArray]):
    """A single FLVER submesh that uses a single material.

    FLVER files are exported 3D model files optimized for rendering, not editing. Model faces with different materials
    are thus already split up into multiple submeshes, and may even be split further to handle large bone counts (older
    games like DS1 cannot support more than 38 bones per submesh).

    Soulstruct assigns FLVER `Material` instances directly to submeshes. When packing the `FLVER`, identical materials
    used by multiple submeshes will be merged.
    """

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        is_bind_pose: bool
        _pad1: bytes = field(init=False, **BinaryPad(3))
        _material_index: int
        _pad2: bytes = field(init=False, **BinaryPad(8))
        default_bone_index: int
        _bone_count: int
        _bounding_box_offset: int
        _bone_offset: int
        _face_set_count: int
        _face_set_offset: int
        _vertex_array_count: int = field(**Binary(asserted=[1, 2, 3]))
        _vertex_array_offset: int

    material: Material  # override

    is_bind_pose: bool = False  # determines weighted bone behavior; typically `False` only for Map Pieces
    uses_bounding_box: bool = True  # TODO: perfect candidate for a game-specific subclass ClassVar
    # TODO: These are clearly NOT min/max in later games that use the third vector below.
    #  'min' seems to be roughly half the extent of the bounding box, but it's quite rough.
    #   - center in 'local box coordinates'?
    #  'max' is quite smaller and sometimes even negative. Not quite contained to [-1, 1] range though.
    #   - center in 'FLVER bounding box normalized coordinates'?
    bounding_box_min: Vector3 = field(default_factory=Vector3.single_max)
    bounding_box_max: Vector3 = field(default_factory=Vector3.single_min)
    # TODO: Seems to be VERY close to the center of the mesh bounding box in FLVER space.
    bounding_box_unknown: Vector3 | None = None  # only used in Sekiro onward  # TODO: see above

    # Held temporarily while unpacking.
    _face_set_indices: list[int] | None = field(default=None, init=False)
    _vertex_array_indices: list[int] | None = field(default=None, init=False)

    @classmethod
    def from_flver_reader(
        cls,
        reader: BinaryReader,
        materials: list[Material],
        bounding_box_has_unknown: bool,
        index: int,
    ):
        mesh_struct = cls.STRUCT.from_bytes(reader)

        _material_index = mesh_struct.pop("_material_index")
        _bone_count = mesh_struct.pop("_bone_count")
        _bounding_box_offset = mesh_struct.pop("_bounding_box_offset")
        _bone_offset = mesh_struct.pop("_bone_offset")
        _face_set_count = mesh_struct.pop("_face_set_count")
        _face_set_offset = mesh_struct.pop("_face_set_offset")
        _vertex_array_count = mesh_struct.pop("_vertex_array_count")
        _vertex_array_offset = mesh_struct.pop("_vertex_array_offset")

        bone_indices = np.array(reader.unpack(f"{_bone_count}i", offset=_bone_offset)) if _bone_count > 0 else None

        _face_set_indices = list(reader.unpack(f"{_face_set_count}i", offset=_face_set_offset))
        _vertex_array_indices = list(reader.unpack(f"{_vertex_array_count}i", offset=_vertex_array_offset))

        kwargs = {}
        if _bounding_box_offset != 0:
            with reader.temp_offset(_bounding_box_offset):
                kwargs["bounding_box_min"] = Vector3(reader.unpack("3f"))
                kwargs["bounding_box_max"] = Vector3(reader.unpack("3f"))
                kwargs["bounding_box_unknown"] = Vector3(reader.unpack("3f")) if bounding_box_has_unknown else None
        else:
            kwargs["uses_bounding_box"] = False

        submesh = mesh_struct.to_object(
            cls,
            material=materials[_material_index],
            bone_indices=bone_indices,
            index=index,
            vertex_arrays=[],
            face_sets=[],
            **kwargs,
        )
        submesh._face_set_indices = _face_set_indices
        submesh._vertex_array_indices = _vertex_array_indices
        return submesh

    def dereference_face_sets(self, face_sets: dict[int, FaceSet]):
        self.face_sets = []
        for i in self._face_set_indices:
            if i not in face_sets:
                raise KeyError(
                    f"Tried to assign `FaceSet` with index {i} to `Submesh`, but the `FaceSet` has "
                    "already been assigned to another `Submesh` (or does not exist)."
                )
            self.face_sets.append(face_sets.pop(i))
        self._face_set_indices = None

    def dereference_vertex_arrays(self, vertex_arrays: dict[int, VertexArray]):
        self.vertex_arrays = []
        for i in self._vertex_array_indices:
            if i not in vertex_arrays:
                raise KeyError(
                    f"Tried to assign `VertexBuffer` with index {i} to `Submesh`, but the `VertexBuffer` has "
                    "already been assigned to another `Submesh` (or does not exist)."
                )
            self.vertex_arrays.append(vertex_arrays.pop(i))
        self._vertex_array_indices = None

        # Check that all vertex arrays for this submesh have the same length.
        if self.vertex_arrays:
            if len({len(vertex_array.array) for vertex_array in self.vertex_arrays}) != 1:
                raise ValueError("Vertex arrays for submesh do not all have the same size.")
        else:
            _LOGGER.warning("Submesh has no vertex arrays.")

        if any(vertex_array.array.size == 0 for vertex_array in self.vertex_arrays):
            mat_def_name = self.material.mat_def_name if self.material else '<unknown>'
            _LOGGER.warning(
                f"Submesh in FLVER (mat def '{mat_def_name}') has an incorrect layout that could not be fixed. Submesh "
                f"marked with `invalid_layout = True`; handle this as needed."
            )
            self.invalid_layout = True

        # TODO: SoulsFormats does an extra check here for edge-compressed vertex arrays, which are not supported here.

    def to_flver_writer(self, writer: BinaryWriter, material_index: int):
        """Material index is the index into shared FLVER materials, so multiple submeshes can point to the same one."""
        self.STRUCT.object_to_writer(
            self,
            writer,
            _material_index=material_index,
            _bone_count=len(self.bone_indices) if self.bone_indices is not None else 0,
            _face_set_count=len(self.face_sets),
            _vertex_array_count=len(self.vertex_arrays),
        )

    def pack_bounding_box(self, writer: BinaryWriter):
        if not self.uses_bounding_box:
            writer.fill("_bounding_box_offset", 0, obj=self)
        else:
            writer.fill_with_position("_bounding_box_offset", obj=self)
            writer.pack("3f", *self.bounding_box_min)
            writer.pack("3f", *self.bounding_box_max)
            if self.bounding_box_unknown is not None:
                writer.pack("3f", *self.bounding_box_unknown)

    def pack_bone_indices(self, writer: BinaryWriter, bone_indices_start: int):
        if self.bone_indices is None:
            # Weird case for byte-perfect writing.
            writer.fill("_bone_offset", bone_indices_start, obj=self)
        else:
            writer.fill_with_position("_bone_offset", obj=self)
            writer.pack(f"{len(self.bone_indices)}i", *self.bone_indices)

    def pack_face_set_indices(self, writer: BinaryWriter, first_face_set_index: int):
        face_set_indices = [first_face_set_index + i for i in range(len(self.face_sets))]
        writer.fill_with_position("_face_set_offset", obj=self)
        writer.pack(f"{len(face_set_indices)}i", *face_set_indices)

    def pack_vertex_array_indices(self, writer: BinaryWriter, first_vertex_array_index: int):
        vertex_array_indices = [first_vertex_array_index + i for i in range(len(self.vertex_arrays))]
        writer.fill_with_position("_vertex_array_offset", obj=self)
        writer.pack(f"{len(vertex_array_indices)}i", *vertex_array_indices)

    def refresh_bounding_box(self):
        if not self.uses_bounding_box:
            return  # nothing to refresh
        if not self.vertex_arrays:
            _LOGGER.warning("Submesh has no vertex arrays. Cannot refresh bounding box.")
            return
        self.bounding_box_min = Vector3.single_max()
        self.bounding_box_max = Vector3.single_min()
        for vertex_array in self.vertex_arrays:
            self.bounding_box_min = np.minimum(self.bounding_box_min, vertex_array.array["position"].min(axis=0))
            self.bounding_box_max = np.maximum(self.bounding_box_max, vertex_array.array["position"].max(axis=0))
        if self.bounding_box_unknown is not None:
            _LOGGER.warning("Cannot refresh `bounding_box_unknown` for Submesh (unknown values).")

    def vertex_count_exceeds_ushort(self, vertex_array=0):
        return len(self.vertex_arrays[vertex_array]) < 0xFFFF

    def draw(
        self,
        vertex_color="red",
        show_normals=True,
        show_face_sets=(),
        show_origin=False,
        auto_show=False,
        axes=None,
        random_face_colors=False,
        **kwargs,
    ):
        import matplotlib.pyplot as plt
        if axes is None:
            axes = plt.figure().add_subplot(111, projection="3d")
        array = self.vertex_arrays[0]
        positions = array["position"]
        axes.scatter(*zip(*positions), c=vertex_color, s=1, alpha=0.1)  # note y/z swapped
        if show_normals:
            normals = array["normal"]
            for position, normal in zip(positions, normals):
                axes.plot(*zip(position, position + normal), c="black", alpha=0.1)
        if show_origin:
            axes.scatter(0, 0, 0, c="black", marker="x", s=5)
        if show_face_sets == "all":
            show_face_sets = tuple(range(len(self.face_sets)))
        if show_face_sets:
            from mpl_toolkits.mplot3d import art3d
            faces = []
            for i, face_set in enumerate(self.face_sets):
                if i in show_face_sets:
                    faces += [tri for tri in face_set.triangulate(False)]
            faces = np.array(faces)
            face_colors = list(range(len(faces)))
            if random_face_colors:
                random.shuffle(face_colors)
            colors = np.array(face_colors)
            norm = plt.Normalize(colors.min(initial=0), colors.max(initial=1))
            # noinspection PyUnresolvedReferences
            colors = plt.cm.rainbow(norm(colors))
            pc = art3d.Poly3DCollection(positions[faces], facecolors=colors, edgecolor="black", linewidth=0.1)
            axes.add_collection(pc)
        axes.set(**kwargs)
        if auto_show:
            plt.show()

    def __repr__(self):
        face_sets = ",\n".join(["    " + indent_lines(repr(f)) for f in self.face_sets])
        material = indent_lines(repr(self.material))
        lines = [
            "Submesh(",
            f"  material = {material}",
            f"  default_bone_index = {self.default_bone_index}",
            f"  bone_indices = {self.bone_indices}",
            f"  vertices = <{len(self.vertices)} vertices>",
        ]
        if not self.is_bind_pose:
            lines.append("  is_bind_pose = False")
        if self.uses_bounding_box:
            lines.append(f"  bounding_box_min = {self.bounding_box_min}")
            lines.append(f"  bounding_box_max = {self.bounding_box_max}")
            if self.bounding_box_unknown is not None:
                lines.append(f"  bounding_box_unknown = {self.bounding_box_unknown}")
        lines.append(f"  face_sets = [\n{face_sets}\n  ]")
        lines.append(")")

        return "\n".join(lines)
