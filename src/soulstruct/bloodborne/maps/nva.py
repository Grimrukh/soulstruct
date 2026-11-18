"""Read Bloodborne's v4 NVA navmesh placement section."""

from __future__ import annotations

__all__ = ["NVA", "NVANavmeshPlacement"]

from dataclasses import dataclass
from pathlib import Path
from struct import Struct

from soulstruct.dcx import decompress

_HEADER = Struct("<4s7I")
_PLACEMENT = Struct("<3f4x3f4x3f4x2i8x2i2xh68x")


@dataclass(frozen=True, slots=True)
class NVANavmeshPlacement:
    """One instance of a model in a map's NVMHKTBND, in the NVA coordinate frame."""

    translate: tuple[float, float, float]
    rotate: tuple[float, float, float]  # Euler angles in radians.
    scale: tuple[float, float, float]
    name_id: int
    model_id: int
    vertex_count: int
    reference_count: int
    node_count: int

    @property
    def is_placeholder(self) -> bool:
        return self.name_id == -1 and self.vertex_count == self.reference_count == 0


@dataclass(frozen=True, slots=True)
class NVA:
    """Read-only view of Bloodborne's first NVA section.

    Entries retain their file order, including empty placeholders. Apply the map's MSB MapOffset when placing
    the tiles in the MSB frame. Trailing sections, such as cross-tile connections, are outside this reader.
    """

    navmesh_placements: tuple[NVANavmeshPlacement, ...]

    @classmethod
    def from_path(cls, path: str | Path) -> NVA:
        return cls.from_bytes(Path(path).read_bytes())

    @classmethod
    def from_bytes(cls, data: bytes) -> NVA:
        if data.startswith(b"DCX\0"):
            data, _ = decompress(data)
        if len(data) < _HEADER.size:
            raise ValueError("Truncated NVA header.")

        magic, version, size, _, section, revision, length, count = _HEADER.unpack_from(data)
        if (magic, version, section, revision) != (b"NVMA", 4, 0, 3):
            raise ValueError("Expected a Bloodborne v4 NVA with a v3 navmesh placement section.")
        if size != len(data) or length != count * _PLACEMENT.size or _HEADER.size + length > size:
            raise ValueError("Invalid NVA placement section size.")

        entries = (
            NVANavmeshPlacement(entry[:3], entry[3:6], entry[6:9], *entry[9:])
            for entry in _PLACEMENT.iter_unpack(memoryview(data)[_HEADER.size:_HEADER.size + length])
        )
        return cls(tuple(entries))
