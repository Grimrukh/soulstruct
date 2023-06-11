from __future__ import annotations

__all__ = ["MSGDirectory", "fmg_property"]

import abc
import csv
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry, DCXType
from soulstruct.base.game_file_directory import GameFileDirectory
from soulstruct.utilities.files import read_json, write_json

from .fmg import FMG
from .msgbnd import MSGBND

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGDirectory"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MSGDirectory(GameFileDirectory, abc.ABC):
    """Loads `item.msgbnd` and `menu.msgbnd` simultaneously and manages their text categories (FMGs).

    Used in lieu of a `MSGBND` class, which would just be half of this class and make it difficult to manage 'patch'
    entries.
    """
    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*\.msgbnd"
    FILE_CLASS: tp.ClassVar[tp.Type[MSGBND]] = MSGBND
    FILE_EXTENSION: tp.ClassVar[str] = ".msgbnd"

    # These are text categories you are likely to want to change in mod projects (in display order).
    MAIN_CATEGORIES: tp.ClassVar[tuple[str, ...]]

    # These are text categories you are unlikely to change, whether it's for pragmatic reasons or because they contain
    # low-level menu/system text. Generally, new IDs cannot be added to these categories in a functional way.
    INTERNAL_CATEGORIES: tp.ClassVar[tuple[str, ...]]

    # Maps "item/menu" string and entry IDs to default entry names (without paths) to use when generating new FMG binder
    # entries from scratch.
    DEFAULT_ENTRY_STEMS: tp.ClassVar[dict[(str, int), str]]

    # Maps any non-patch ('base') FMG entry sources/IDs to patch FMG entry sources/IDs.
    # When `merge_base_and_patch()` is called, all base and patch FMGs will be merged (with 'patch' taking precedence in
    # case of conflicts) and the results written to BOTH base and patch.
    BASE_PATCH_FMGS: tp.ClassVar[dict[(str, int), (str, int)]] = {}

    # DCX compression type to use for `FMG` entries (as `FMG` does not have game-specific subclasses). Typically Null.
    FMG_DCX_TYPE: tp.ClassVar[DCXType] = DCXType.Null

    # Override file type.
    files: dict[str, Binder] = field(default_factory=dict)  # maps 'true stems' to `FILE_CLASS` instances

    # Maps "item/menu" string and entry IDs to FMGs (unusual for IDs to matter, but they do in MSGBNDs).
    fmgs: dict[(str, int), FMG] = field(default_factory=dict)

    @classmethod
    def GET_ALL_CATEGORIES(cls):
        return cls.MAIN_CATEGORIES + cls.INTERNAL_CATEGORIES

    @classmethod
    def from_path(cls, directory_path: Path | str):
        """Specifically loads `item` and `menu` MSGBND files only, and all their FMGs."""
        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")
        files = {}
        file_name_re = re.compile(r"^(item|menu)\.msgbnd(\.dcx)?$")
        for file_path in directory_path.glob("*"):
            if match := file_name_re.match(file_path.name):
                if match.group(1) == "item":
                    files["item"] = cls.FILE_CLASS.from_path(file_path)
                elif match.group(1) == "menu":
                    files["menu"] = cls.FILE_CLASS.from_path(file_path)

        if "item" not in files:
            raise FileNotFoundError(f"Could not find `item.msgbnd[.dcx]` in directory: {directory_path}.")
        if "menu" not in files:
            raise FileNotFoundError(f"Could not find `menu.msgbnd[.dcx]` in directory: {directory_path}.")

        # Open FMGs.
        fmgs = cls.create_fmgs(files["item"], files["menu"])

        return cls(directory=directory_path, files=files, fmgs=fmgs)

    @classmethod
    def from_item_menu_binders(cls, item_msgbnd: Binder, menu_msgbnd: Binder) -> Self:

        files = {"item": item_msgbnd, "menu": menu_msgbnd}
        fmgs = cls.create_fmgs(item_msgbnd, menu_msgbnd)
        return cls(directory=None, files=files, fmgs=fmgs)

    @classmethod
    def from_json_directory(cls, directory: Path | str) -> Self:
        """Load individual text (FMG) JSON files from an unpacked Binder folder (e.g. from `write_json_directory()`).

        The names of the JSON files to be loaded from the folder are recorded in the "entries" key of the
        `item_msgbnd_manifest.json` and `menu_msgbnd_manifest.json` files, along with header information for each BND.

        NOTE: This does not use the `Binder` base manifest system at all.
        """
        directory = Path(directory)
        item_manifest_path = directory / "item_msgbnd_manifest.json"
        if not item_manifest_path.is_file():
            raise FileNotFoundError(f"Could not find `MSGDirectory` manifest file '{item_manifest_path}'.")
        item_manifest = read_json(item_manifest_path)
        menu_manifest_path = directory / "menu_msgbnd_manifest.json"
        if not menu_manifest_path.is_file():
            raise FileNotFoundError(f"Could not find `MSGDirectory` manifest file '{menu_manifest_path}'.")
        menu_manifest = read_json(menu_manifest_path)

        files = {}
        fmgs = {}

        item_kwargs = cls.FILE_CLASS.process_manifest_header(item_manifest)
        menu_kwargs = cls.FILE_CLASS.process_manifest_header(menu_manifest)

        missing_ids = list(cls.DEFAULT_ENTRY_STEMS)
        for msgbnd_name, kwargs in zip(("item", "menu"), (item_kwargs, menu_kwargs)):
            entries = []
            entry_json_dict = kwargs.pop("entries", {})
            for entry_id, json_stem in entry_json_dict.items():
                entry_id = int(entry_id)
                json_name = f"{json_stem}.json"
                if (msgbnd_name, entry_id) not in cls.DEFAULT_ENTRY_STEMS:
                    _LOGGER.warning(f"Ignoring unrecognized MSGBND JSON file with entry ID {entry_id}: {json_name}")
                    continue
                try:
                    fmg = FMG.from_json(directory / json_name)
                except FileNotFoundError:
                    raise FileNotFoundError(f"Could not find text (FMG) JSON file: {directory / json_name}")
                fmg.dcx_type = cls.FMG_DCX_TYPE
                fmg_stem = cls.DEFAULT_ENTRY_STEMS[(msgbnd_name, entry_id)]
                entry_path = cls.FILE_CLASS.get_default_entry_path(fmg_stem + ".fmg")
                entry = BinderEntry(bytes(fmg), entry_id, entry_path, cls.FILE_CLASS.DEFAULT_ENTRY_FLAGS)
                entries.append(entry)
                fmgs[(msgbnd_name, entry_id)] = fmg
                missing_ids.remove((msgbnd_name, entry_id))
            kwargs["entries"] = entries
            kwargs.pop("use_id_prefix", None)  # if present
            files[msgbnd_name] = cls.FILE_CLASS.from_dict(kwargs)

        if missing_ids:
            missing = f"\n  ".join(f"{entry_id}: {cls.DEFAULT_ENTRY_STEMS[entry_id]}" for entry_id in missing_ids)
            _LOGGER.warning(f"Could not find these MSGBND entry IDs in JSON directory:\n  {missing}")

        return cls(directory=directory, files=files, fmgs=fmgs)

    @classmethod
    def create_fmgs(cls, item_msgbnd: Binder, menu_msgbnd: Binder) -> dict[(str, int), FMG]:
        """Loads FMGs from given `msgbnd` into `categories` dictionary."""
        fmgs = {}
        for entry in item_msgbnd.entries:
            try:
                fmgs["item", entry.entry_id] = entry.to_binary_file(FMG)
            except Exception as ex:
                _LOGGER.error(f"Error encountered while loading FMG '{entry.name}' in `item`: {ex}")
                raise
        for entry in menu_msgbnd.entries:
            try:
                fmgs["menu", entry.entry_id] = entry.to_binary_file(FMG)
            except Exception as ex:
                _LOGGER.error(f"Error encountered while loading FMG '{entry.name}' in `menu`: {ex}")
                raise
        return fmgs

    def write_json_directory(self, directory: tp.Union[Path, str]):
        """Write a folder containing custom MSGBND manifests linking to FMG JSON entry files.

        The resulting folder can be loaded with `from_json_directory(directory)`.

        The JSON file names will always be the more readable Soulstruct 'category' names, e.g. 'WeaponDescriptions', but
        the entry names written to the Binders by `write()` will always use the game-specific internal names from
        `DEFAULT_ENTRY_NAMES`.
        """
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        manifests = {
            "item": self.files["item"].get_manifest_header() | {"entries": {}},
            "menu": self.files["menu"].get_manifest_header() | {"entries": {}},
        }

        # `use_id_prefix` not required for JSON manifest, even in DSR, where internal paths repeat.
        manifests["item"].pop("use_id_prefix", None)
        manifests["menu"].pop("use_id_prefix", None)

        category_fmgs = self.get_matching_fmgs()

        for (msgbnd_name, entry_id), fmg in self.fmgs.items():
            # TODO: Clunky way to get Soulstruct category name...
            category_name = [key for key, _fmg in category_fmgs.items() if _fmg is fmg][0]
            manifests[msgbnd_name]["entries"][entry_id] = category_name
            fmg.write_json(directory / f"{category_name}.json", encoding="utf-8")

        write_json(directory / "item_msgbnd_manifest.json", manifests["item"])
        write_json(directory / "menu_msgbnd_manifest.json", manifests["menu"])

    def regenerate_binders(self):
        """Regenerate `item` and `menu` MSGBNDs from all FMGs."""

        # First, remove any binder entries that are not present in `fmgs`.
        fmg_keys = self.fmgs.keys()
        for msgbnd_name in ("item", "menu"):
            msgbnd = self.files[msgbnd_name]
            for entry in msgbnd.entries:
                if (msgbnd_name, entry.entry_id) not in fmg_keys:
                    msgbnd.remove_entry(entry)

        # Add or update entries from new packed FMGs.
        for (msgbnd_name, entry_id), fmg in self.fmgs.items():
            msgbnd = self.files[msgbnd_name]
            if (msgbnd_name, entry_id) not in self.DEFAULT_ENTRY_STEMS:
                raise KeyError(
                    f"Class `{self.__class__.__name__}` does not have a default entry name for ID {entry_id} "
                    f"in '{msgbnd_name}' MSGBND."
                )
            msgbnd.add_or_replace_entry_id(entry_id, fmg, self.DEFAULT_ENTRY_STEMS[msgbnd_name, entry_id] + ".fmg")

    def merge_base_and_patch(self, use_patch_if_conflict=True):
        """Merge all base and patch FMGs together (as per class `BASE_PATCH_FMGS`) and write merged FMG to both.

        The way that base and patch (e.g. DLC) entries interact can be confusing, so my shotgun-like solution is to just
        merge them and write identical data to each, to guarantee desired results. The FMG files are so small that this
        has little downside.

        Does nothing (and logs nothing) if `BASE_PATCH_FMGS` is empty.

        If string IDs conflict, `use_patch_if_conflict` determines whether patch (True) or base (False) string is used.
        """
        for base_fmg_key, patch_fmg_key in self.BASE_PATCH_FMGS.items():
            base_fmg = self.fmgs[base_fmg_key]
            patch_fmg = self.fmgs[patch_fmg_key]
            if use_patch_if_conflict:
                base_fmg.update(patch_fmg)  # override base with patch
                self.fmgs[patch_fmg_key] = base_fmg.copy()  # copy merged to patch
            else:
                patch_fmg.update(base_fmg)  # override patch with base
                self.fmgs[base_fmg_key] = patch_fmg.copy()  # copy merged to base

    def get_matching_fmgs(self, category_name_regex: re.Pattern | str = "") -> dict[str, FMG]:
        if isinstance(category_name_regex, str) and category_name_regex:
            category_name_regex = re.compile(category_name_regex)
        fmgs = {}
        for attr_name in dir(self.__class__):
            if (
                isinstance(getattr(self.__class__, attr_name), property)
                and (not category_name_regex or re.match(category_name_regex, attr_name))
            ):
                fmgs[attr_name] = getattr(self, attr_name)
        return fmgs

    def remove_empty_strings(self, category_name_regex: str = ""):
        """Iterate over all `MSGDirectory` property names (e.g. "WeaponDescriptions") and remove empty strings from all
        FMGs in properties that match `category_name_regex` pattern (e.g. r".*Descriptions").

        Modifies FMGs in-place, unlike the `FMG.remove_empty_strings()` method.

        Default `category_name_regex` will match all FMG names.
        """
        matching_fmgs = list(self.get_matching_fmgs(category_name_regex).values())
        for fmg in matching_fmgs:
            fmg.entries = {string_id: string for string_id, string in fmg.entries.items() if string}

    def apply_line_limits(self, category_name_regex: str = "", max_chars_per_line: int = None, max_lines: int = None):
        """Iterate over all `MSGDirectory` property names (e.g. "WeaponDescriptions") and apply given word wrap and line
        count limits to all FMGs in properties that match `category_name_regex` pattern (e.g. r".*Descriptions").

        Default `category_name_regex` will match all FMG names.
        """
        matching_fmgs = list(self.get_matching_fmgs(category_name_regex).values())
        for fmg_key, fmg in self.fmgs.items():
            if fmg in matching_fmgs:
                self.fmgs[fmg_key] = fmg.apply_line_limits(max_chars_per_line, max_lines)

    def replace_substring_in_all(self, category_name_regex: str, old_substring: str, new_substring: str):
        """Iterate over all `MSGDirectory` property names (e.g. "WeaponDescriptions") and replace the given substring
        with the given new substring in all FMGs in properties that match `category_name_regex` pattern.

        Use match-all regex like `r".*"` to affect all FMGs.
        """
        for fmg in self.get_matching_fmgs(category_name_regex).values():
            fmg.entries = {
                string_id: string.replace(old_substring, new_substring)
                for string_id, string in fmg.entries
            }

    def write(self, directory_path: Path | str | None = None, check_file_hashes: bool = False):
        """Regenerate and write `item` and `menu` MSGBNDs."""
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)
        directory_path.mkdir(parents=True, exist_ok=True)

        self.regenerate_binders()
        self.files["item"].write(directory_path / f"item{self.FILE_EXTENSION}", check_hash=check_file_hashes)
        self.files["menu"].write(directory_path / f"menu{self.FILE_EXTENSION}", check_hash=check_file_hashes)
        _LOGGER.info(
            f"`{self.__class__.__name__}` written to `{directory_path}` successfully ({len(self.files)} files)."
        )

    # region Utility Methods: Items

    def get_item_fmgs(self, item_type: str) -> dict[str, FMG]:
        """Return a dictionary with keys 'Names', 'Summaries', and 'Descriptions' mapping to the FMGs of `item_type`
        and that key text type (e.g. 'WeaponDescriptions').

        Will raise a `KeyError` if any of the three text categories are missing.
        """
        item_type = self.resolve_item_type(item_type)
        item_fmgs = self.get_matching_fmgs(re.compile(rf"{item_type}(Names|Summaries|Descriptions)"))
        if len(item_fmgs) != 3:
            raise KeyError(
                f"Could not find all of '{item_type}Names', '{item_type}Summaries', and '{item_type}Descriptions' "
                f"in `MSGDirectory`."
            )
        return {
            "Names": item_fmgs[f"{item_type}Names"],
            "Summaries": item_fmgs[f"{item_type}Summaries"],
            "Descriptions": item_fmgs[f"{item_type}Descriptions"],
        }

    def get_all_item_text(self, item_id: int, item_type: str) -> dict[str, str]:
        """Get name, summary, and description of the given item ID with given type.

        Returns empty dictionary if ID is not present in '*Names' category. Other strings (Summaries/Descriptions) may
        be `None` in returned dictionary if absent.
        """
        item_fmgs = self.get_item_fmgs(item_type)
        if item_id not in item_fmgs["Names"]:
            return {}  # ID absent
        return {
            "name": item_fmgs["Names"][item_id],
            "summary": item_fmgs["Summaries"].get(item_id, None),
            "description": item_fmgs["Descriptions"].get(item_id, None),
        }

    def set_item_text(
        self, item_id: int, item_type: str, name: str, summary: str, description: str, allow_override=True
    ):
        """Set `name`, `summary`, and `description` text to `item_id` of `item_type`.

        Will create the IDs if they don't exist or happily replace any that exist if `allow_override=True` (default).
        Otherwise, existing keys will raise a `ValueError`.
        """
        item_fmgs = self.get_item_fmgs(item_type)
        for (fmg_name, fmg), string in zip(item_fmgs.items(), (name, summary, description)):
            if not allow_override and item_id in fmg.entries:
                raise ValueError(f"Item with index {item_id} already exists in `{item_type}{fmg_name}`: {fmg[item_id]}")
            fmg[item_id] = string

    def delete_item_text(self, item_id: int, item_type="good"):
        """Remove entries for item name, summary, and description.

        Will remove whichever entries are present and not complain if any are missing.
        """
        item_fmgs = self.get_item_fmgs(item_type)
        for fmg in item_fmgs.values():
            fmg.pop(item_id, default=None)

    def find_and_print(self, search_string: str, category_name_regex: str = r".*", exclude_subtitles=True):
        """Search for the given text across categories and print the categories, IDs, and strings of hits.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            category_name_regex: Name of text category (FMG) to search. If no category is given, all categories will be
                searched (except perhaps Subtitles; see below). (Default: None)
            exclude_subtitles: the 'Subtitles' text category is so large that it deserves its own bool to exclude it
                from the text search separate.
        """
        fmgs = self.get_matching_fmgs(category_name_regex)
        if exclude_subtitles:
            fmgs.pop("Subtitles", None)

        found_something = False
        for fmg_name, fmg in fmgs.items():
            for string_id, string in fmg.items():
                if search_string in string:
                    found_something = True
                    print(f"\n~~~ {fmg_name}[{string_id}]:\n{string}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def __iter__(self):
        return iter(self.fmgs.keys())

    def __getitem__(self, category_name: str):
        try:
            return self.get_matching_fmgs()[category_name]
        except KeyError:
            raise AttributeError(f"Non-existent text category (FMG): '{category_name}'")

    def get_range(self, category_name: str, first_index: int, last_index: int):
        """Get a list of (id, text) pairs from a certain index range inside the ID-sorted text dictionary.

        NOTE: The range indices are NOT string IDs in the FMG. They are the ordered indices of all the strings.
        """
        fmg = self[category_name]
        return [(string_id, fmg[string_id]) for string_id in sorted(fmg.keys())[first_index:last_index]]

    def update_from_csv(
        self,
        csv_path: Path,
        category_column_index: int,
        string_id_column_index: int,
        string_column_index: int,
        skip_first_row=True,
        delimiter=",",
        quotechar="\"",
        parse_newlines=True,
    ):
        """Update this `MSGDirectory` instance from the given CSV.

        Arguments specify which columns the category names (e.g. 'AccessoryNames'), text IDs, and text entries are in.
        Use `skip_first_row` to indicate if a header row is present (defaults to True).

        If `parse_newlines=True` (default), doubly-escaped newlines in the CSV will be replaced by actual newlines
        (i.e., '\\n' -> '\n').
        """
        fmgs = self.get_matching_fmgs()
        with Path(csv_path).open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
            for i, row in enumerate(reader):
                if i == 0 and skip_first_row:
                    continue
                category_name = row[category_column_index]
                string_id = int(row[string_id_column_index])
                string = row[string_column_index]
                if parse_newlines:
                    string = string.replace("\\n", "\n")
                fmgs[category_name][string_id] = string

    @staticmethod
    def resolve_item_type(item_type: str) -> str:
        """TODO: Subclass override with Runes, etc."""
        if item_type.lower() in {"good", "consumable"}:
            return "Good"
        elif item_type.lower() in {"ring", "accessory"}:
            return "Ring"
        elif item_type.lower() in {"weapon", "shield"}:
            return "Weapon"
        elif item_type.lower() in {"armour", "armor", "protector"}:
            return "Armor"
        elif item_type.lower() == "equipment":
            raise ValueError("'equipment' is ambiguous. Did you mean 'weapon', 'armor', 'ring', or 'good'?")
        elif item_type.lower() == "item":
            raise ValueError(
                "'item' is ambiguous; it's the term used to describe everything in your inventory.\n"
                "Did you mean 'weapon', 'armor', 'ring', or 'good'?"
            )
        else:
            raise ValueError(f"Unrecognized item type: '{item_type}'")


def fmg_property(msgbnd_name: str, bnd_index: int):
    """Assists in assigning properties to FMG nicknames, e.g. `ArmorDescriptions = fmg_property("item", 26)`.

    No setter is available. Contents of an FMG can be replaced completely by setting its `entries` attribute.
    """
    return property(lambda self: self.fmgs[msgbnd_name, bnd_index])
