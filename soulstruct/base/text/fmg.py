from __future__ import annotations

__all__ = ["FMG", "BaseFMG", "FMG0", "FMG1", "FMG2"]

import abc
import logging
from textwrap import wrap

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

_LOGGER = logging.getLogger(__name__)


def FMG(fmg_source, dcx_type=None, remove_empty_entries=True) -> BaseFMG:
    if fmg_source is None:
        raise ValueError(f"Cannot auto-detect FMG class from source `None`.")
    if isinstance(fmg_source, dict):
        try:
            version = fmg_source["version"]
        except KeyError:
            raise ValueError(f"No `version` key in FMG dictionary to read.")
    elif isinstance(fmg_source, GameFile.Types):
        version = BinaryReader(fmg_source).unpack_value("b", offset=6, relative_offset=True)
    else:
        raise ValueError(f"Cannot auto-detect FMG class from source type {type(fmg_source)}.")

    if version == 0:
        return FMG0(fmg_source, dcx_type=dcx_type, remove_empty_entries=remove_empty_entries)
    elif version == 1:
        return FMG1(fmg_source, dcx_type=dcx_type, remove_empty_entries=remove_empty_entries)
    elif version == 2:
        return FMG2(fmg_source, dcx_type=dcx_type, remove_empty_entries=remove_empty_entries)
    else:
        raise ValueError(f"Unrecognized FMG version: {version}")


class BaseFMG(GameFile, abc.ABC):
    """Simple text dictionary.

    Since Demon's Souls, only the `version` field differs between games, with slight header structure changes.
    """

    EXT = ".fmg"
    HEADER_STRUCT: BinaryStruct = None
    RANGE_STRUCT: BinaryStruct = None
    STRING_OFFSET_STRUCT: BinaryStruct = None
    BIG_ENDIAN = False
    VERSION = None  # type: int

    MAX_LINES = None  # type: int

    entries: dict[int, str]

    def __init__(self, fmg_source, dcx_type=None, remove_empty_entries=True):
        self.entries = {}
        if isinstance(fmg_source, dict) and "version" not in fmg_source:
            fmg_source["version"] = self.VERSION
        super().__init__(fmg_source, dcx_type)
        if remove_empty_entries:
            self.entries = {i: entry for i, entry in self.entries.items() if entry}

    def load_dict(self, data: dict, clear_old_data=True):
        if data["version"] != self.VERSION:
            raise ValueError(f"FMG dictionary has version {data['version']}, but requires version {self.VERSION}.")
        if clear_old_data:
            self.entries = data["entries"]
        else:
            self.entries.update(data["entries"])

    def unpack(self, reader: BinaryReader, remove_empty_entries=True):
        header = reader.unpack_struct(self.HEADER_STRUCT)

        # Groups of contiguous text string IDs are defined by ranges (first ID, last ID) to save space.
        ranges = reader.unpack_structs(self.RANGE_STRUCT, count=header["range_count"])
        if reader.position != header["string_offsets_offset"]:
            _LOGGER.warning("Range data did not end at string data offset given in FMG header.")
        string_offsets = reader.unpack_structs(self.STRING_OFFSET_STRUCT, count=header["string_count"])

        # Text pointer table corresponds to all the IDs (joined together) of the above ranges, in order.
        for string_range in ranges:
            i = string_range["first_index"]
            for string_id in range(string_range["first_id"], string_range["last_id"] + 1):
                if string_id in self.entries:
                    raise ValueError(f"Malformed FMG: Entry index {string_id} appeared more than once.")
                string_offset = string_offsets[i]["offset"]
                if string_offset == 0:
                    if not remove_empty_entries:
                        # Empty text string. These will trigger in-game error messages, like ?PlaceName?.
                        # Distinct from ' ', which is intentionally blank text data (e.g. the unused area subtitles).
                        self.entries[string_id] = ""
                else:
                    string = reader.unpack_string(offset=string_offset, encoding="utf-16le")
                    if string or not remove_empty_entries:
                        self.entries[string_id] = string
                i += 1

    def to_dict(self):
        return {
            "dcx_type": self.dcx_type.value,
            "version": self.VERSION,
            "entries": self.entries.copy(),
        }

    def pack(self, remove_empty_entries=True, pipe_to_newline=True, word_wrap_limit=None, max_lines=None):
        """Pack text dictionary to binary FMG file.

        Args:
            remove_empty_entries: Ignore empty entries ('') when writing. This will remove many entries from the vanilla
                FMG files, and likely make some of them larger (as the ranges used to define them will be more broken
                up), but will make the dictionary much easier to read through. (Default: True)
            pipe_to_newline: Convert pipes ('|') to newlines ('\n'), which allows for nicer strings. Newline characters
                will still be treated normally. (Default: True)
            word_wrap_limit: Specify a horizontal character limit for automatic word wrapping. If None, no wrapping will
                be applied. (Default: None)
            max_lines: Maximum number of lines that should appear in each text entry. An error will be raised if any
                text exceeds this (and no file will be written). This is most useful for item descriptions when auto
                wrapping is used. It defaults to a class value, `.MAX_LINES`.

        Note that none of these arguments will modify the entries in this FMG instance, only the packed output.
        """
        if max_lines is None:
            max_lines = self.MAX_LINES

        # Convert to sorted list (sorted by ID).
        if remove_empty_entries:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items() if v != ""], key=lambda x: x[0])
        else:
            fmg_entries = sorted([(k, v) for k, v in self.entries.items()], key=lambda x: x[0])

        for i in range(len(fmg_entries)):
            # Optional: convert double spaces to double new lines.
            index, string = fmg_entries[i]
            if pipe_to_newline:
                string = string.replace("|", "\n")
                fmg_entries[i] = (index, string)
            # Optional: insert new lines to wrap automatically.
            if word_wrap_limit is not None:
                lines = string.split("\n\n")
                if lines != [" "]:
                    # Wrap lines, and re-add manual newlines.
                    wrapped_lines = []
                    for line in lines:
                        if "\n" in line:
                            # Don't touch lines with newlines already in them.
                            wrapped_lines.append(line)
                        else:
                            wrapped_lines.append("\n".join(wrap(line, word_wrap_limit)))
                    wrapped_string = "\n\n".join(wrapped_lines).rstrip("\n")
                    line_count = wrapped_string.count("\n") + 1
                    if max_lines is not None and line_count > max_lines - 1:
                        _LOGGER.warning(
                            f"FMG index {index} has {line_count} lines (max is {max_lines}):\n" f"{wrapped_string}"
                        )
                    fmg_entries[i] = (index, wrapped_string)

        # Encode all text entries and pack them, and record the offsets (will be globally offset later).
        relative_string_offset = 0
        packed_strings = b""
        string_offset_list = []

        for string_id, string in fmg_entries:
            if string == "":
                string_offset_list.append(-1)  # changed to zero when offsets become absolute
            null_terminated_text = string.encode("utf-16le") + b"\0\0"
            packed_strings += null_terminated_text
            string_offset_list.append(relative_string_offset)
            relative_string_offset += len(null_terminated_text)

        # Next, the ranges. We just make these as efficient as possible, but unlike FROM, we value the lack of clutter
        # from empty entries more highly than defining a handful less ranges.
        ranges = []
        range_start_index = None
        range_start = None
        range_stop = None
        for string_index, (string_id, _) in enumerate(fmg_entries):
            if range_start_index is None:
                range_start_index = string_index
                range_start = range_stop = string_id
            elif string_id == range_stop + 1:
                # Expand current range to include this string.
                range_stop += 1
            else:
                # Terminate last range...
                ranges.append(
                    self.RANGE_STRUCT.pack(first_index=range_start_index, first_id=range_start, last_id=range_stop)
                )
                # ... then start new one at this string.
                range_start_index = string_index
                range_start = range_stop = string_id

        if range_start is not None:
            # Terminate last range.
            ranges.append(
                self.RANGE_STRUCT.pack(first_index=range_start_index, first_id=range_start, last_id=range_stop)
            )

        packed_ranges = b"".join(ranges)

        # Compute table offsets.
        ranges_offset = self.HEADER_STRUCT.size
        string_offsets_offset = ranges_offset + len(packed_ranges)
        packed_strings_offset = string_offsets_offset + self.STRING_OFFSET_STRUCT.size * len(string_offset_list)
        file_size = packed_strings_offset + len(packed_strings)
        packed_string_offsets = b""
        for string_offset in string_offset_list:
            if string_offset == -1:
                packed_string_offsets += self.STRING_OFFSET_STRUCT.pack(offset=0)
            else:
                packed_string_offsets += self.STRING_OFFSET_STRUCT.pack(offset=packed_strings_offset + string_offset)

        packed_header = self.HEADER_STRUCT.pack(
            file_size=file_size,
            range_count=len(ranges),
            string_count=len(fmg_entries),
            string_offsets_offset=string_offsets_offset,
        )

        return packed_header + packed_ranges + packed_string_offsets + packed_strings

    def write(
        self,
        file_path=None,
        make_dirs=True,
        check_hash=False,
        remove_empty_entries=True,
        pipe_to_newline=True,
        word_wrap_limit=None,
        max_lines=None,
    ):
        """Write binary FMG to given path. See `pack` for descriptions of the other arguments."""
        super().write(
            file_path=file_path,
            make_dirs=make_dirs,
            check_hash=check_hash,
            remove_empty_entries=remove_empty_entries,
            pipe_to_newline=pipe_to_newline,
            word_wrap_limit=word_wrap_limit,
            max_lines=max_lines,
        )

    def __getitem__(self, index: int):
        return self.entries[index]

    def __setitem__(self, index: int, text: str):
        self.entries[index] = text

    def update(self, entries):
        if isinstance(entries, dict):
            return self.entries.update(entries)
        elif isinstance(entries, BaseFMG):
            return self.entries.update(entries.entries)
        raise TypeError(f"Can only call `FMG.update()` with a dictionary or another FMG, not {type(entries)}.")

    def find(self, search_string, replace_with=None):
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

    def __iter__(self):
        return iter(self.entries.items())

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.entries == other
        elif isinstance(other, BaseFMG):
            return self.entries == other.entries
        raise TypeError("Can only test FMG equality with a dictionary or other `BaseFMG`.")

    def __repr__(self):
        s = f"FMG Path: {str(self.path) if self.path is not None else '<None>'}"
        for index, text in self.entries.items():
            s += f"\n    {index}: {text}"
        return s


class FMG0(BaseFMG):
    """Used only in Demon's Souls. Big-endian."""

    HEADER_STRUCT = BinaryStruct(
        "x",
        ("big_endian", "?", True),
        ("version", "b", 0),
        "x",
        ("file_size", "i"),
        ("one", "b", 1),
        ("unknown1", "b", -1),
        "2x",
        ("range_count", "i"),
        ("string_count", "i"),
        ("string_offsets_offset", "i"),
        ("zero", "i", 0),
        byte_order=">",
    )
    RANGE_STRUCT = BinaryStruct(
        ("first_index", "i"),
        ("first_id", "i"),
        ("last_id", "i"),
        byte_order=">",
    )
    STRING_OFFSET_STRUCT = BinaryStruct(
        ("offset", "i"),
        byte_order=">",
    )
    BIG_ENDIAN = True
    VERSION = 0

    MAX_LINES = None  # TODO: Don't know for Demon's Souls.


class FMG1(BaseFMG):
    """Used in Dark Souls (both versions) and Dark Souls 2."""

    HEADER_STRUCT = BinaryStruct(
        "x",
        ("big_endian", "?", False),
        ("version", "b", 1),
        "x",
        ("file_size", "i"),
        ("one", "b", 1),
        ("unknown1", "b", 0),
        "2x",
        ("range_count", "i"),
        ("string_count", "i"),
        ("string_offsets_offset", "i"),
        ("zero", "i", 0),
    )
    RANGE_STRUCT = BinaryStruct(
        ("first_index", "i"),
        ("first_id", "i"),
        ("last_id", "i"),
    )
    STRING_OFFSET_STRUCT = BinaryStruct(
        ("offset", "i"),
    )
    BIG_ENDIAN = False
    VERSION = 1

    MAX_LINES = 11  # TODO: Correct for DS1, not sure about DS2.


class FMG2(BaseFMG):
    """Used in Bloodborne, Dark Souls 3, and Sekiro."""

    HEADER_STRUCT = BinaryStruct(
        "x",
        ("big_endian", "?", False),
        ("version", "b", 2),
        "x",
        ("file_size", "i"),
        ("one", "b", 1),
        ("unknown1", "b", 0),
        "2x",
        ("range_count", "i"),
        ("string_count", "i"),
        ("unknown2", "i", 255),
        ("string_offsets_offset", "q"),
        ("zero", "q", 0),
    )
    RANGE_STRUCT = BinaryStruct(
        ("first_index", "i"),
        ("first_id", "i"),
        ("last_id", "i"),
        "4x",
    )
    STRING_OFFSET_STRUCT = BinaryStruct(
        ("offset", "q"),
    )
    BIG_ENDIAN = False
    VERSION = 2

    MAX_LINES = None  # TODO: Don't know for Bloodborne or DS3.
