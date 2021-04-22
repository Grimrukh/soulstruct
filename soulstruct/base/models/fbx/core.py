__all__ = ["FBX"]

import io
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .node import FBXNode


class FBX(GameFile):
    """Not actually a "game" file, but interchangeable with `FLVER` game files."""

    MAX_VERSION = 7400

    HEADER_STRUCT = BinaryStruct(
        ("magic", "23s", b"Kaydara FBX Binary  \x00\x1a\x00"),
        ("version", "I"),
    )

    # Constant 176 byte footer at the end of every FBX file.
    FOOTER = (
        b"\xfa\xbc\xab\x09\xd0\xc8\xd4\x66\xb1\x76\xfb\x83\x1c\xf7\x26\x7e" + b"\0" * 20
        + b"\xe8\x1c" + b"\0" * 122
        + b"\xf8\x5a\x8c\x6a\xde\xf5\xd9\x7e\xec\xe9\x0c\xe3\x75\x8f\x29\x0b"
    )

    def __init__(
        self,
        file_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase, BinaryReader] = None,
        dcx_magic: tuple[int, int] = (),
        **kwargs,
    ):
        self.root_nodes = []  # type: list[FBXNode]

        super().__init__(file_source, dcx_magic, **kwargs)

    def unpack(self, reader: BinaryReader, **kwargs):
        header = reader.unpack_struct(self.HEADER_STRUCT)
        if header["version"] > self.MAX_VERSION:
            raise NotImplementedError(
                f"Cannot unpack FBX version {header['version']}. Last supported version is {self.MAX_VERSION}."
            )

        start_offset = self.HEADER_STRUCT.size
        self.root_nodes = []
        while 1:
            node = FBXNode(reader, start_offset=start_offset)
            start_offset += node.size
            if node.is_empty:
                break  # empty node is not kept
            self.root_nodes.append(node)

        # Constant FBX footer is ignored.

    def pack(self):
        raise NotImplementedError("FBX cannot be packed yet.")

    def to_string(self) -> str:
        return "\n".join(node.to_string() for node in self.root_nodes)
