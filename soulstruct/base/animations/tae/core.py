"""'Time Act Editor' (TAE) file format.

TAE files contain various events (function callbacks with parameters) that occur on specific frames of corresponding
model animations (HKX files), such as sounds, FFX spawning, hitboxes, parry windows, and so on. Essentially, they are
responsible for everything that happens during an animation other than the actual FLVER bone/mesh deformation.

I currently have no plans to support any GUI editing of TAE events, as Meowmaritus's DS Anim Studio already does this
in an unbeatably good way. However, as such a critical game format, I do want it here for completion (and to permit
scripted changes).

Currently only made for Dark Souls Remastered. (PTDE is identical, but with 32-bit offsets, I believe.)
"""
import typing as tp
from dataclasses import dataclass

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryReader, BinaryWriter


@dataclass(slots=True)
class TAE(GameFile):
    """TODO"""

    def to_writer(self) -> BinaryWriter:
        pass

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        pass

    def unpack(self, reader: BinaryReader, **kwargs):
        pass

    def pack(self, **kwargs) -> bytes:
        pass
