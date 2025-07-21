from __future__ import annotations

__all__ = ["FMG"]

import logging
import typing as tp
from dataclasses import field
from enum import IntEnum
from pathlib import Path
from textwrap import wrap

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import read_json

_LOGGER = logging.getLogger(__name__)


class FMGVersion(IntEnum):
    V0 = 0  # Demon's Souls
    V1 = 1  # Dark Souls, Dark Souls 2
    V2 = 2  # Bloodborne, Dark Souls 3, Sekiro, Elden Ring


GAME_MAX_LINES = {
    "darksouls1ptde": 11,
    "darksouls1r": 11,
}


class FMGHeaderV0(BinaryStruct):
    _pad1: bytes = binary_pad(1)
    big_endian: bool
    version: FMGVersion = binary(byte)
    _pad2: bytes = binary_pad(1)
    file_size: int
    _one: byte = binary(asserted=1)
    _minus_one: byte = binary(asserted=-1)
    _pad3: bytes = binary_pad(2)
    range_count: int
    string_count: int
    # unknown2: int = binary(asserted=255)
    string_offsets_offset: int
    _pad4: bytes = binary_pad(4)
    # _pad5: bytes = binary_pad(4)


class FMGHeaderV1(BinaryStruct):
    _pad1: bytes = binary_pad(1)
    big_endian: bool
    version: FMGVersion = binary(byte)
    _pad2: bytes = binary_pad(1)
    file_size: int
    _one: byte = binary(asserted=1)
    _zero: byte = binary(asserted=0)
    _pad3: bytes = binary_pad(2)
    range_count: int
    string_count: int
    # unknown2: int = binary(asserted=255)
    string_offsets_offset: int
    _pad4: bytes = binary_pad(4)
    # _pad5: bytes = binary_pad(4)


class FMGHeaderV2(BinaryStruct):
    _pad1: bytes = binary_pad(1)
    big_endian: bool
    version: FMGVersion = binary(byte)
    _pad2: bytes = binary_pad(1)
    file_size: int
    _one: byte = binary(asserted=1)
    _zero: byte = binary(asserted=0)
    _pad3: bytes = binary_pad(2)
    range_count: int
    string_count: int
    unknown2: int = binary(asserted=255)
    string_offsets_offset: long
    _pad4: bytes = binary_pad(4)
    _pad5: bytes = binary_pad(4)


class FMG(GameFile):
    """Simple text dictionary.

    Since Demon's Souls, only the `version` field differs between games, with slight header structure changes.
    """

    EXT: tp.ClassVar[str] = ".fmg"
    HEADER_VERSIONS: tp.ClassVar[dict[FMGVersion, type[FMGHeaderV0] | type[FMGHeaderV1] | type[FMGHeaderV2]]] = {
        FMGVersion.V0: FMGHeaderV0,
        FMGVersion.V1: FMGHeaderV1,
        FMGVersion.V2: FMGHeaderV2,
    }

    entries: dict[int, str] = field(default_factory=dict)
    version: int = 2  # default to newest version (Bloodborne onwards)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:

        version = FMGVersion(reader["b", 2])
        reader.byte_order = ByteOrder.big_endian_bool(version == FMGVersion.V0)
        reader.long_varints = version >= 2
        header = cls.HEADER_VERSIONS[version].from_bytes(reader)  # type: FMGHeaderV0 | FMGHeaderV1 | FMGHeaderV2

        # Groups of contiguous text string IDs are defined by ranges (first ID, last ID) to save space.
        ranges = []
        for _ in range(header.range_count):
            first_index, first_id, last_id = reader.unpack("3i")
            if version == 2:
                reader.assert_pad(4)
            ranges.append((first_index, first_id, last_id))

        if reader.position != header.string_offsets_offset:
            _LOGGER.warning("Range data did not end at string data offset given in unpacked FMG header.")

        string_offsets = reader.unpack(f"{header.string_count}v")  # type: tuple[int, ...]

        # Text pointer table corresponds to all the IDs (joined together) of the above ranges, in order.
        entries = {}
        for first_index, first_id, last_id in ranges:
            for string_id in range(first_id, last_id + 1):
                if string_id in entries:
                    raise ValueError(f"Malformed FMG: Text entry ID {string_id} appeared more than once.")
                string_offset = string_offsets[first_index]
                if string_offset == 0:
                    entries[string_id] = ""  # empty string (will trigger in-game error placeholder text)
                else:
                    entries[string_id] = reader.unpack_string(
                        offset=string_offset,
                        encoding=reader.get_utf_16_encoding(),
                    )
                first_index += 1

        return cls(entries=entries, version=version)

    @classmethod
    def from_json(cls, json_path: str | Path) -> tp.Self:
        """`entries` dictionary keys need to be converted to `int`."""
        json_dict = read_json(json_path)
        json_dict["entries"] = {int(k): v for k, v in json_dict["entries"].items()}
        return cls.from_dict(json_dict)

    def sort(self):
        """Sort strings by ID in-place."""
        self.entries = {string_id: self.entries[string_id] for string_id in sorted(self.entries.keys())}

    def remove_empty_strings(self) -> FMG:
        """Remove all empty strings from entry dictionary and returns a copy.

        This will remove many entries from vanilla files, which (in older games at least) prefer defining entire ranges
        of strings even if only a few of them are used (which leads to smaller file sizes but makes dictionary versions
        of the data awkward).

        Returns a copy, e.g. if you only want to do it before packing.
        """
        new_entries = {string_id: string for string_id, string in self.entries.items() if string}
        return FMG(entries=new_entries, version=self.version)

    def apply_line_limits(self, max_chars_per_line: int = None, max_lines: int = None) -> FMG:
        """Reformat strings to apply a word wrap limit and log a warning if line count exceeds `max_lines`. Returns a
        modified copy of the FMG.

        `max_lines` will be auto-detected by game by default. Set it to something stupidly high to disable it.
        """
        if max_lines is None:
            game = self.get_game()
            max_lines = GAME_MAX_LINES.get(game.submodule_name, None)

        new_entries = {}
        for string_id, string in self.entries.items():
            lines = string.split("\n\n")
            if lines in ["", " "]:
                new_entries[string_id] = string
                continue  # empty string or one-space string
            # Wrap lines, and re-add manual newlines.
            wrapped_lines = []
            for line in lines:
                if max_chars_per_line is None or "\n" in line:
                    # Don't touch lines with newlines already in them.
                    wrapped_lines.append(line)
                else:
                    wrapped_lines.append("\n".join(wrap(line, max_chars_per_line)))
            wrapped_string = "\n\n".join(wrapped_lines).rstrip("\n")
            line_count = wrapped_string.count("\n") + 1
            if max_lines is not None and line_count > max_lines - 1:
                _LOGGER.warning(
                    f"FMG string ID {string_id} has {line_count} lines (max is {max_lines}):\n"
                    f"{wrapped_string}"
                )
            new_entries[string_id] = wrapped_string
        return FMG(entries=new_entries, version=self.version)

    def to_writer(self, sort=True) -> BinaryWriter:
        """Pack text dictionary to binary FMG file."""
        if sort:
            self.sort()

        writer = BinaryWriter(
            byte_order=ByteOrder.BigEndian if self.version == 0 else ByteOrder.LittleEndian,
            long_varints=self.version >= 2,
        )

        header_cls = self.HEADER_VERSIONS[FMGVersion(self.version)]

        header_cls.object_to_writer(
            self,
            writer,
            big_endian=self.version == 0,
            file_size=RESERVED,
            unknown1=-1 if self.version == 0 else 0,
            range_count=RESERVED,
            string_count=len(self.entries),
            string_offsets_offset=RESERVED,
        )

        # Construct ranges. A single missing ID will interrupt a range. (If empty strings from vanilla files have not
        # been removed, and no other IDs added/removed, these ranges should be identical to the vanilla ones.)

        range_count = 0
        range_start_index = first_id = last_id = None
        for string_index, string_id in enumerate(self.entries.keys()):
            if range_start_index is None:
                # Start new range at this string.
                range_start_index = string_index
                first_id = last_id = string_id
            elif string_id == last_id + 1:
                # Expand current range to include this string.
                last_id += 1
            else:
                # Terminate last range...
                writer.pack("3i", range_start_index, first_id, last_id)
                if self.version == 2:
                    writer.pad(4)
                range_count += 1
                # ... then start new one at this string.
                range_start_index = string_index
                first_id = last_id = string_id

        if first_id is not None:
            # Terminate final range.
            writer.pack("3i", range_start_index, first_id, last_id)
            if self.version == 2:
                writer.pad(4)
            range_count += 1
        writer.fill("range_count", range_count, obj=self)

        writer.fill_with_position("string_offsets_offset", obj=self)
        packed_strings = b""  # saving ourselves an additional iteration
        packed_strings_offset = writer.position + (8 if writer.long_varints else 4) * len(self.entries)
        for string_id, string in self.entries.items():
            if string == "":
                writer.pack("v", 0)  # no offset
            else:
                writer.pack("v", packed_strings_offset + len(packed_strings))
            packed_strings += string.encode(writer.get_utf_16_encoding()) + b"\0\0"

        writer.append(packed_strings)

        writer.fill_with_position("file_size", obj=self)

        return writer

    def to_dict(self, sort=True) -> dict[str, tp.Any]:
        """Optionally (and by default) sorts text entries before converting to dictionary."""
        if sort:
            self.sort()
        return super(GameFile, self).to_dict()

    def __getitem__(self, index: int):
        return self.entries[index]

    def get(self, string_id: int, default: str = None):
        """Return `string_id` value or `default` if missing."""
        return self.entries.get(string_id, default)

    def __setitem__(self, index: int, text: str):
        self.entries[index] = text

    def setdefault(self, string_id: int, default: str):
        """Return `string_id` value or set it to `default` and return that."""
        return self.entries.setdefault(string_id, default)

    def pop(self, string_id: int, default: str = None):
        """Remove `string_id` value and return it, or return `default`.

        Will never raise a `KeyError`. Use `FMG.entries.pop()` if you want to assert the key exists.
        """
        return self.entries.pop(string_id, default)

    def update(self, fmg_or_entries: FMG | dict):
        """Update this FMG in place with `FMG` or `entries` dict."""
        if isinstance(fmg_or_entries, dict):
            return self.entries.update(fmg_or_entries)
        elif isinstance(fmg_or_entries, FMG):
            return self.entries.update(fmg_or_entries.entries)
        raise TypeError(f"Can only call `FMG.update()` with a dictionary or another `FMG`, not {type(fmg_or_entries)}.")

    def find(self, search_string: str, replace_with=None):
        """Search for the given text in this FMG.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            replace_with: String to replace the given text with in any results. (Default: None)
        """
        found_something = False
        for index, text in self.entries.items():
            if search_string in text:
                if not found_something:
                    print(f"\n~~~ FMG: {str(self.path) if self.path is not None else '<None>'}")
                    found_something = True
                print(f"\n  [{index}]:\n{text}")
                if replace_with is not None:
                    self.entries[index] = text.replace(search_string, replace_with)
                    print(f"  -> {self.entries[index]}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def replace_substring_in_all(self, old_substring: str, new_substring: str) -> FMG:
        """Returns a copy off the FMG with all given substring replacements done.

        NOTE: Just a quieter, simpler version of calling `find` with `replace_with`.
        """
        new_entries = {
            string_id: string.replace(old_substring, new_substring)
            for string_id, string in self.entries
        }
        return FMG(entries=new_entries, version=self.version)

    def keys(self):
        return self.entries.keys()

    def values(self):
        return self.entries.values()

    def items(self):
        return self.entries.items()

    def __iter__(self):
        return iter(self.entries.keys())

    def __repr__(self):
        s = f"FMG Path: {str(self.path) if self.path is not None else '<None>'}"
        for index, text in self.entries.items():
            s += f"\n    {index}: {text}"
        return s
