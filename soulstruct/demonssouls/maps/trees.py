from __future__ import annotations

__all__ = [
    "MSBTree",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.msb_entry import MSBEntry
from soulstruct.demonssouls.maps.enums import MSBSupertype, MSBTreeSubtype
from soulstruct.utilities.binary import BinaryReader, BinaryWriter, BinaryStruct
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import IDList


@dataclass(slots=True)
class TreeHeaderStruct(BinaryStruct):
    """Header struct for a 'tree' in a Demon's Souls MSB file."""
    point_0: Vector3
    unk_x0c: int
    point_1: Vector3
    unk_x1c: int
    point_2: Vector3
    unk_x2c: int
    unk_x30: float
    _short_count: int
    # Array of shorts here.


@dataclass(slots=True, eq=False, repr=False)
class MSBTree(MSBEntry):
    """Weird unknown 'tree' in Demon's Souls MSBs that does not resemble other MSB entries at all."""

    NAME_ENCODING = ""  # unused
    SUPERTYPE_ENUM = MSBSupertype.TREES
    SUBTYPE_ENUM = MSBTreeSubtype.Tree
    HEADER_STRUCT = TreeHeaderStruct
    STRUCTS = {}

    point_0: Vector3 = field(default_factory=Vector3.zero)  # seems to be the lowest
    unk_x0c: int = 0  # typically 0 or 64
    point_1: Vector3 = field(default_factory=Vector3.zero)  # seems to be the highest
    unk_x1c: int = 0  # have only seen 0 thus far
    point_2: Vector3 = field(default_factory=Vector3.zero)  # seems to be the midpoint
    unk_x2c: int = 0  # a few different values (multiples of 64?)
    unk_x30: float = 1.0  # possibly scale
    unk_shorts_x38: list[int] = field(default_factory=list)  # eclectic; NOT tree indices or offsets AFAICT

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader):

        header = TreeHeaderStruct.from_bytes(reader)
        shorts = [reader.unpack_value('h') for _ in range(header.pop("_short_count"))]
        # Dummy name 'Tree' is used for compulsory field, but it is not used in the actual MSB.
        cls.SETATTR_CHECKS_DISABLED = True
        tree = header.to_object(cls, name="Tree", unk_shorts_x38=shorts)
        cls.SETATTR_CHECKS_DISABLED = False
        return tree

    @classmethod
    def reader_to_entry_kwargs(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        raise TypeError("MSBTree entries are not stored in an ID list, so this method is not used.")

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, IDList[MSBEntry]]
    ):
        """Default `name` based on index added, but not used. Note 16-byte alignment AFTER each tree."""
        TreeHeaderStruct.object_to_writer(self, writer, _short_count=len(self.unk_shorts_x38))
        writer.pack(f"{len(self.unk_shorts_x38)}h", *self.unk_shorts_x38)
        writer.pad_align(0x10)
