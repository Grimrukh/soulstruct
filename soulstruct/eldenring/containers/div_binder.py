"""Multi-BND binder whose separate 'div' source Binder files are marked by `.blf` files in the main Binder."""
from __future__ import annotations

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers.core import Binder, BinderEntry
from soulstruct.utilities.binary import BinaryReader, BinaryWriter

_LOGGER = logging.getLogger("soulstruct")


class DivBinder(Binder):
    """Binder that optionally supports division into multiple sub-Binders when written, based on `.blf` Binder entries.

    Identical to `Binder` if `write_blf_division` is `False`.

    NOTE: These Binders can sometimes have clashing entry IDs across the different sub-Binders (that end up being unique
    when those sub-Binders are written). Example: the HKX compendium files in Elden Ring's divided ANIBNDs (7000000).
    """
    PATH_ROOT: tp.ClassVar[str] = "N:\\GR\\data"  # BLF regex is relative to this path (but includes leading backslash)

    # Override default. `True` not supported if `write_blf_division` is True.
    is_split_bxf: bool = False

    write_blf_division: bool = True

    @classmethod
    def from_path(cls, path: str | Path, bdt_path: str | Path | None = None) -> tp.Self:
        """`path` should be the path to the core Binder containing BLF files.

        Does NOT support `bdt_path` of base class currently, as no split div Binders have been encountered.
        """
        if bdt_path is not None:
            raise ValueError("DivBinder does not support `bdt_path` (i.e. does not support split Binder).")
        path = Path(path)

        # Read base Binder (as `DivBinder` instance).
        # noinspection PyTypeChecker
        core_binder = super(DivBinder, cls).from_path(path, bdt_path)  # type: tp.Self

        # We only need the stems of BLF entries to find those files next to `path`. No need to read BLFs.
        blf_stems = [entry.minimal_stem for entry in core_binder.entries if entry.name.endswith(".blf")]
        if not blf_stems:
            core_binder.write_blf_division = False
            return core_binder

        # Currently not handling split Binders one way or the other. I doubt they ever can or should occur with BLF.
        if core_binder.is_split_bxf:
            raise ValueError(f"Cannot load BLF divided Binders that are also BXF split Binders: {path}")

        path_full_suffix = "".join(path.suffixes)
        core_entries_by_id = core_binder.get_entries_by_id()
        all_div_entries_by_id = {}
        for blf_stem in blf_stems:
            div_name = f"{blf_stem}{path_full_suffix}"
            div_path = Path(path).with_name(div_name)
            if not div_path.is_file():
                raise FileNotFoundError(f"Could not find div Binder file specified by BLF: {div_path}")
            div_binder = Binder.from_path(div_path)
            found_div_data = False
            for div_entry in div_binder.entries:
                if not found_div_data and div_entry.name == "div_data.txt":
                    found_div_data = True

                if div_entry.entry_id in core_entries_by_id:
                    # Check path matches, and ignore if so.
                    core_entry = core_entries_by_id[div_entry.entry_id]
                    if core_entry.path == div_entry.path:
                        continue
                    # Clash between core and div Binders is not permitted (only clashes between different div Binders).
                    raise ValueError(
                        f"Entry ID {div_entry.entry_id} in BLF Binder {div_path} has different path to core Binder."
                    )
                if div_entry.entry_id in all_div_entries_by_id:
                    # Check path matches, and ignore if so.
                    existing_div_entry = all_div_entries_by_id[div_entry.entry_id]
                    if existing_div_entry.path == div_entry.path:
                        continue
                    # Clash between div Binders is permitted.
                    # TODO: Could enforce stem matches div Binder?
                    # TODO: Could enforce identical data?
                    if div_entry.minimal_stem == blf_stem:
                        _LOGGER.info(
                            f"Entry ID {div_entry.entry_id} in BLF Binder {div_path} repeats, but has expected "
                            f"div-specific name: {div_entry.path}"
                        )
                    else:
                        _LOGGER.warning(
                            f"Entry ID {div_entry.entry_id} in BLF Binder {div_path} has different path to another div "
                            f"Binder, and name does not match div Binder: "
                            f"{div_entry.path} vs. {existing_div_entry.path}."
                        )

                all_div_entries_by_id[div_entry.entry_id] = div_entry
                core_binder.entries.append(div_entry)

            if not found_div_data:
                _LOGGER.warning(f"No 'div_data.txt' found in div Binder {div_path}. This empty text file should exist.")

        return core_binder

    def get_div_bytes(self) -> tuple[bytes, list[bytes]]:
        """Return the bytes of the core Binder and the bytes of the div Binders."""
        raise NotImplementedError("`DivBinder` does not support writing yet.")

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
    ) -> list[Path]:
        """If enabled, write the core Binder and all div Binders to the given `file_path` and div paths from BLF
        entries.

        TODO: Raise error if split and BLF division are both enabled.
        TODO: Warn if BLF division is disabled but BLF entries present.
        TODO: Warn if BLF division is enabled but no BLF entries present. (Error if any IDs repeat?)
        """
        if not self.write_blf_division:
            return super().write(file_path, bdt_file_path, make_dirs, check_hash)

        raise NotImplementedError("`DivBinder` does not support BLF division writing yet. (Need BLF parsing!)")

    # TODO: Method that parses BLF text file and uses regex to create split DIV Binders!


@dataclass(slots=True)
class BLFCommmand:
    first_entry_id: int
    path_regex_str: str
    unk_int_0: int = 16
    unk_int_1: int = 2
    unk_int_2: int = 1
    entry_type: str = "_TXT"
    regex_replace: str = ""

    ENTRY_ID_RE: tp.ClassVar[re.Pattern] = re.compile(r"^\$(\d+)$")
    ARGS_RE: tp.ClassVar[re.Pattern] = re.compile(
        r"^\s*\"(?P<path_regex_str>.*)\"\s*,"
        r"\s*(?P<unk_int_0>\d+)\s*,\s*(?P<unk_int_1>\d+)\s*,\s*(?P<unk_int_2>\d+)\s*,"
        r"\s*(?P<entry_type>\w{4})\s*,\s*\"(?P<regex_replace>.*)\"$"
    )

    @classmethod
    def from_blf_lines(cls, entry_id_line: str, args_line: str) -> BLFCommmand:
        """Parse and remove next two lines of BLF file."""
        entry_id_match = cls.ENTRY_ID_RE.match(entry_id_line)
        args_match = cls.ARGS_RE.match(args_line)
        if entry_id_match is None:
            raise ValueError(f"First line of BLF command does not match expected format: {repr(entry_id_line)}")
        if args_match is None:
            raise ValueError(f"Second line of BLF command does not match expected format: {repr(args_line)}")
        return cls(
            first_entry_id=int(entry_id_match.group(1)),
            path_regex_str=args_match.group("path_regex_str"),
            unk_int_0=int(args_match.group("unk_int_0")),
            unk_int_1=int(args_match.group("unk_int_1")),
            unk_int_2=int(args_match.group("unk_int_2")),
            entry_type=args_match.group("entry_type"),
            regex_replace=args_match.group("regex_replace"),
        )

    def to_blf_lines(self) -> tuple[str, str]:
        entry_id_line = f"${self.first_entry_id}"
        args_line = (
            f"\t\"{self.path_regex_str}\",\t{self.unk_int_0},\t{self.unk_int_1},\t{self.unk_int_2},\t"
            f"{self.entry_type},\t\"{self.regex_replace}\""
        )
        return entry_id_line, args_line

    def get_path_regex(self) -> re.Pattern:
        return re.compile(self.path_regex_str)

    def get_matching_entries(self, entry_root: str, entries: list[BinderEntry]) -> list[BinderEntry]:
        """TODO: Doesn't work, because HKX files are in 'hkx_divXX_compendium' subfolder, not just 'hkx'."""
        path_regex = self.get_path_regex()
        matching_entries = []
        for entry in entries:
            entry_relative_path = entry.path.removeprefix(entry_root)
            print(entry_relative_path)
            if path_regex.match(entry_relative_path):
                matching_entries.append(entry)
                print("   MATCH")
        return matching_entries


class BLF(GameFile):
    """Binder List File. Contains a list of Binder files that should be used to split a DivBinder."""

    ENCODING: tp.ClassVar[str] = "shift-jis"
    FILE_VERSION_RE: tp.ClassVar[re.Pattern] = re.compile(r"^#FILE_VERSION = (\d+)$")

    file_version: int = 301
    comments: list[str] = field(default_factory=lambda: ["-" * 80, "   ファイルリスト", "-" * 80])
    commands: list[BLFCommmand] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> BLF:
        blf_text = reader.read().decode(cls.ENCODING)
        blf_lines = blf_text.split("\r\n")
        bli3 = blf_lines.pop(0)
        if bli3 != "BLI3":
            raise ValueError(f"BLF text file does not start with expected 'BLI3' header: {repr(bli3)}")
        file_version_line = blf_lines.pop(0)
        file_version_match = cls.FILE_VERSION_RE.match(file_version_line)
        if file_version_match is None:
            raise ValueError(
                f"Second line of BLF file does not match expected '#FILE_VERSION' format: {file_version_line}"
            )
        try:
            file_version = int(file_version_match.group(1))
        except ValueError:
            raise ValueError(f"Could not parse file version number from BLF file: {file_version_line}")

        i = 0
        comments = []
        commands = []
        while i < len(blf_lines):
            line = blf_lines[i].strip()
            if not line:
                i += 1
                continue
            if line.startswith("//"):
                comments.append(line.lstrip("/ "))
                i += 1
                continue
            if line.startswith("$"):
                entry_id_line = line
                args_line = blf_lines[i + 1]
                command = BLFCommmand.from_blf_lines(entry_id_line, args_line)
                commands.append(command)
                i += 2
                continue
            else:
                raise ValueError(f"Unexpected line in BLF file: {line}")
        return cls(file_version=file_version, commands=commands)

    def to_writer(self) -> BinaryWriter:
        blf_lines = ["BLI3", f"#FILE_VERSION = {self.file_version}", ""]
        for comment in self.comments:
            blf_lines.append(f"// {comment}")
        blf_lines.append("")

        for command in self.commands:
            entry_id_line, args_line = command.to_blf_lines()
            blf_lines.append(entry_id_line)
            blf_lines.append(args_line)

        blf_bytes = "\r\n".join(blf_lines).encode(self.ENCODING)
        writer = BinaryWriter()
        writer.append(blf_bytes)
        return writer


def test():
    path = r"C:\Steam\steamapps\common\ELDEN RING (Modding 1.10)\Game\chr\c2140.anibnd.dcx"
    div_binder = DivBinder.from_path(path)
    print(div_binder)
    blf_entries = [entry for entry in div_binder.entries if entry.name.endswith(".blf")]
    for entry in blf_entries:
        print(entry.name)
        blf = BLF.from_binder_entry(entry)
        print(blf.base_repr())
        div_entries = blf.commands[0].get_matching_entries(div_binder.PATH_ROOT, div_binder.entries)
        print(div_entries)
        return


if __name__ == '__main__':
    test()
