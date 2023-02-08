from __future__ import annotations

__all__ = ["MSGDirectory"]

import abc
import csv
import logging
import re
import typing as tp
from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry
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
    DEFAULT_ENTRY_NAMES: tp.ClassVar[dict[(str, int), str]]

    # Maps any non-patch ('base') FMG entry sources/IDs to patch FMG entry sources/IDs.
    # When `merge_base_and_patch()` is called, all base and patch FMGs will be merged (with 'patch' taking precedence in
    # case of conflicts) and the results written to BOTH base and patch.
    BASE_PATCH_FMGS: tp.ClassVar[dict[(str, int), (str, int)]] = {}

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
        file_name_re = re.compile(r"(item|menu)\.msgbnd(\.dcx)?")
        for file_path in directory_path.glob("*"):
            if match := file_name_re.match(file_path.name):
                if match.group(1) == "item":
                    files["item"] = cls.FILE_CLASS.from_path(file_path)
                elif match.group(2) == "menu":
                    files["menu"] = cls.FILE_CLASS.from_path(file_path)

        if not files["item"]:
            raise FileNotFoundError("Could not find `item.msgbnd[.dcx]` in directory.")
        if not files["menu"]:
            raise FileNotFoundError("Could not find `menu.msgbnd[.dcx]` in directory.")

        # Open FMGs.
        fmgs = cls.get_fmgs(files["item"], files["menu"])

        return cls(directory_path, files, fmgs)

    @classmethod
    def from_json_directory(cls, directory_path: Path | str):
        directory_path = Path(directory_path)
        self.load_json_dir(msg_directory, clear_old_data=False)
        return

    @classmethod
    def from_item_menu_binders(cls, item_msgbnd: Binder, menu_msgbnd: Binder) -> Self:

        files = {"item": item_msgbnd, "menu": menu_msgbnd}
        fmgs = cls.get_fmgs(item_msgbnd, menu_msgbnd)
        return cls(directory=Path(), files=files, fmgs=fmgs)

    @classmethod
    def get_fmgs(cls, item_msgbnd: Binder, menu_msgbnd: Binder) -> dict[(str, int), FMG]:
        """Loads FMGs from given `msgbnd` into `categories` dictionary."""
        fmgs = {}
        for entry in item_msgbnd.entries:
            try:
                fmgs["item", entry.entry_id] = entry.to_game_file(FMG)
            except Exception as ex:
                _LOGGER.error(f"Error encountered while loading FMG '{entry.name}' in `item`: {ex}")
                raise
        for entry in menu_msgbnd.entries:
            try:
                fmgs["menu", entry.entry_id] = entry.to_game_file(FMG)
            except Exception as ex:
                _LOGGER.error(f"Error encountered while loading FMG '{entry.name}' in `menu`: {ex}")
                raise
        return fmgs

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
            if (msgbnd_name, entry_id) not in self.DEFAULT_ENTRY_NAMES:
                raise KeyError(
                    f"Class `{self.__class__.__name__}` does not have a default entry name for ID {entry_id} "
                    f"in '{msgbnd_name}' MSGBND."
                )
            msgbnd.add_or_replace_entry_id(entry_id, fmg, self.DEFAULT_ENTRY_NAMES[entry_id])

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

    def get_matching_fmgs(self, category_name_regex: re.Pattern | str) -> dict[str, FMG]:
        if isinstance(category_name_regex, str):
            category_name_regex = re.compile(category_name_regex)
        fmgs = {}
        for attr_name in dir(self.__class__):
            if isinstance(getattr(self.__class__, attr_name), property) and re.match(category_name_regex, attr_name):
                fmgs[attr_name] = getattr(self, attr_name)
        return fmgs

    def remove_empty_strings(self, category_name_regex: str):
        """Iterate over all `MSGDirectory` property names (e.g. "WeaponDescriptions") and remove empty strings from all
        FMGs in properties that match `category_name_regex` pattern (e.g. r".*Descriptions").

        Use match-all regex like `r".*"` to affect all FMGs.
        """
        for fmg in self.get_matching_fmgs(category_name_regex).values():
            fmg.remove_empty_strings()

    def apply_line_limits(self, category_name_regex: str, max_chars_per_line: int = None, max_lines: int = None):
        """Iterate over all `MSGDirectory` property names (e.g. "WeaponDescriptions") and apply given word wrap and line
        count limits to all FMGs in properties that match `category_name_regex` pattern (e.g. r".*Descriptions").

        Use match-all regex like `r".*"` to affect all FMGs.
        """
        for fmg in self.get_matching_fmgs(category_name_regex).values():
            fmg.apply_line_limits(max_chars_per_line, max_lines)

    def replace_substring_in_all(self, category_name_regex: str, old_substring: str, new_substring: str) -> FMG:
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
        self.files["item"].write(directory_path / f"item.{self.FILE_EXTENSION}", check_hash=check_file_hashes)
        self.files["menu"].write(directory_path / f"item.{self.FILE_EXTENSION}", check_hash=check_file_hashes)
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

    def find(self, search_string: str, replace_with=None, text_category=None, exclude_conversations=True):
        """Search for the given text in the entire game.

        Args:
            search_string: Text to find. The text can appear anywhere inside an entry to return a result.
            replace_with: String to replace the given text with in any results. (Default: None)
            text_category: Name of text category (FMG) to search. If no category is given, all categories will be
                searched (except perhaps Subtitles; see below). (Default: None)
            exclude_conversations: If True, the Subtitles text category will not be searched when all categories are
                searched. (This category contains a lot of text, and you are unlikely to want to modify it, given how it
                lines up with the audio.) (Default: True)
        """
        if text_category is None:
            dicts_to_search = (
                [(fmg_name, fmg_dict) for fmg_name, fmg_dict in self.categories.items() if fmg_name != "Subtitles"]
                if exclude_conversations
                else self.categories.items()
            )
        else:
            dicts_to_search = ((text_category, self[text_category]),)

        found_something = False
        for fmg_name, fmg_dict in dicts_to_search:
            for index, text in fmg_dict.items():
                if search_string in text:
                    found_something = True
                    print(f"\n~~~ {fmg_name}[{index}]:\n{text}")
                    if replace_with is not None:
                        fmg_dict[index] = text.replace(search_string, replace_with)
                        print(f"-> {fmg_dict[index]}")
        if not found_something:
            print(f"Could not find any occurrences of string {repr(search_string)}.")

    def __iter__(self):
        return iter(self.fmgs.keys())

    def __getitem__(self, text_category):
        try:
            return self.categories[text_category]
        except KeyError:
            raise AttributeError(f"Non-existent text category (FMG): '{text_category}'")

    def get_range(self, category, start, end):
        """Get a list of (id, text) pairs from a certain range inside the ID-sorted text dictionary."""
        return [
            (text_id, self.categories[category][text_id])
            for text_id in sorted(self.categories[category])[start:end]
        ]

    def update_from_csv(
        self,
        csv_path: Path,
        category_column: int,
        id_column: int,
        text_column: int,
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
        with Path(csv_path).open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
            for i, row in enumerate(reader):
                if i == 0 and skip_first_row:
                    continue
                category, text_id, text_value = row[category_column], row[id_column], row[text_column]
                if parse_newlines:
                    text_value = text_value.replace("\\n", "\n")
                self[category][int(text_id)] = text_value

    def load_json_dir(self, directory: tp.Union[Path, str], clear_old_data=True):
        """Load individual text (FMG) JSON files from an unpacked Binder folder (produced by `write_json_dir()`).

        The names of the JSON files to be loaded from the folder are recorded in the "categories" key of the
        `item_manifest.json` and `menu_manifest.json` files, along with header information for each BND.

        Note that this will immediately modify the underlying MSGBNDs held in this `MSGDirectory` instance.
        """
        directory = Path(directory)
        item_manifest_path = directory / "item_manifest.json"
        if not item_manifest_path.is_file():
            raise FileNotFoundError(f"Could not find `MSGDirectory` manifest file '{item_manifest_path}'.")
        item_manifest = read_json(item_manifest_path)
        menu_manifest_path = directory / "menu_manifest.json"
        if not menu_manifest_path.is_file():
            raise FileNotFoundError(f"Could not find `MSGDirectory` manifest file '{menu_manifest_path}'.")
        menu_manifest = read_json(menu_manifest_path)

        if clear_old_data:
            self._original_names = {}
            self._is_menu = {}

        # Update MSGBND binder information.
        for bnd_name, bnd, manifest in zip(
            ("item", "menu"),
            (self.item_msgbnd, self.menu_msgbnd),
            (item_manifest, menu_manifest),
        ):
            entry_ids = set()
            if bnd is None:
                bnd = self.MSGBND_CLASS(manifest)
                bnd.path = Path(f"{bnd_name}.msgbnd.dcx" if self.IS_DCX else f"{bnd_name}.msgbnd")
                setattr(self, f"{bnd_name}_msgbnd", bnd)
            else:
                for field, value in bnd.process_manifest_header(manifest).items():
                    if not clear_old_data:
                        if (old_value := getattr(bnd, field)) != value:
                            raise ValueError(
                                f"New `{field}` value {repr(value)} does not match old value {repr(old_value)}."
                            )
                    else:
                        setattr(bnd, field, value)
                if clear_old_data:
                    bnd.clear_entries()
                else:
                    entry_ids = set(bnd.entries_by_id)

            for json_name in manifest["entries"]:
                try:
                    fmg_dict = read_json(directory / json_name)
                except FileNotFoundError:
                    raise FileNotFoundError(f"Could not find text (FMG) JSON file '{directory / json_name}'.")
                for field in ("entry_id", "path", "flags", "data"):
                    if field not in fmg_dict:
                        raise KeyError(f"Required field `{field}` not specified in '{json_name}'.")
                fmg = self.FMG_CLASS({"entries": {int(k): v for k, v in fmg_dict["data"].items()}})

                if json_name.endswith("Patch.json"):
                    # "Patch" JSONs are also written into non-Patch Binder entries.
                    non_patch_entry_id = self._MSGBND_INDEX_NAMES[json_name.removesuffix("Patch.json")]
                    non_patch_entry = bnd.BinderEntry(
                        fmg.pack(),
                        non_patch_entry_id,
                        fmg_dict["path"],  # TODO: Patch and non-Patch paths are identical in DSR, but not others.
                        fmg_dict["flags"],
                    )
                    if non_patch_entry_id in entry_ids:
                        _LOGGER.warning(
                            f"Binder entry ID {non_patch_entry_id} appears more than once in `MSGDirectory` "
                            f"'{bnd_name}' MSGBND. Fix this ASAP."
                        )
                    bnd.add_entry(non_patch_entry)

                entry = bnd.BinderEntry(fmg.pack(), fmg_dict["entry_id"], fmg_dict["path"], fmg_dict["flags"])
                if entry.entry_id in entry_ids:
                    _LOGGER.warning(
                        f"Binder entry ID {entry.entry_id} appears more than once in `MSGDirectory` '{bnd_name}' MSGBND. "
                        f"Fix this ASAP."
                    )
                bnd.add_entry(entry)

        # Refresh `MSGDirectory` instance data from new MSGBNDs.
        self.load_fmg_entries_from_bnd(self.item_msgbnd, is_menu=False)
        self.load_fmg_entries_from_bnd(self.menu_msgbnd, is_menu=True)

        for key, fmg_dict in self.categories.items():
            setattr(self, key, fmg_dict)

    def write_json_dir(self, directory: tp.Union[Path, str], remove_empty_entries=True):
        """Write a folder containing 'item_manifest.json' and 'menu_manifest.json' files with `Binder` header
        information for those MSGBNDs and a list of text category (FMG) JSON files to load from the same folder.

        The resulting folder can be loaded with `load_json_dir(directory)`.

        The JSON file names will always be the more readable Soulstruct names, but the Binder "path" key inside each
        JSON will be the original BND entry paths at the time this method is called, so these will still be the original
        internal game names unless modified elsewhere. Other `pack()` arguments (description word wrap, pipe to newline)
        are not offered, as these JSONs are intended to preserve the exact state of this class rather then preparing
        data for ingame use.
        """
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        item_manifest = self.item_msgbnd.get_manifest_header()
        menu_manifest = self.menu_msgbnd.get_manifest_header()
        item_manifest.pop("use_id_prefix")
        item_manifest["entries"] = []
        menu_manifest.pop("use_id_prefix")
        menu_manifest["entries"] = []

        new_item_msgbnd = deepcopy(self.item_msgbnd)  # type: BaseBND
        new_menu_msgbnd = deepcopy(self.menu_msgbnd)  # type: BaseBND

        for fmg_name, fmg_entries in self.categories.items():
            if remove_empty_entries:
                fmg_entries = {k: fmg_entries[k] for k in sorted(fmg_entries) if fmg_entries[k] != ""}
            else:
                fmg_entries = {k: fmg_entries[k] for k in sorted(fmg_entries)}
            if fmg_name + "Patch" in self._is_menu:
                # Updates patch only, if available.
                fmg_name = fmg_name + "Patch"
            fmg_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            manifest = menu_manifest if self._is_menu[fmg_name] else item_manifest
            try:
                bnd_entry_id = self._MSGBND_INDEX_NAMES[fmg_name]
            except IndexError:
                raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
            bnd_entry = fmg_msgbnd.entries_by_id[bnd_entry_id]  # type: BinderEntry
            # Don't need to actually update BND data. We just want the entry information.
            fmg_dict = {
                "entry_id": bnd_entry.entry_id,
                "path": bnd_entry.path,  # will still be original unless already modified
                "flags": bnd_entry.flags,
                "data": fmg_entries,
            }
            json_name = fmg_name + ".json"
            write_json(directory / json_name, fmg_dict, encoding="utf-8")
            manifest["entries"].append(json_name)

        write_json(directory / "item_manifest.json", item_manifest)
        write_json(directory / "menu_manifest.json", menu_manifest)

    @staticmethod
    def resolve_item_type(item_type) -> str:
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


_CAN_MERGE_PATCH = {
    "WeaponNamesPatch",
    "WeaponSummariesPatch",
    "WeaponDescriptionsPatch",
    "ArmorNamesPatch",
    "ArmorSummariesPatch",
    "ArmorDescriptionsPatch",
    "AccessoryNamesPatch",
    "AccessorySummariesPatch",
    "AccessoryDescriptionsPatch",
    "GoodNamesPatch",
    "GoodSummariesPatch",
    "GoodDescriptionsPatch",
    "SpellNamesPatch",
    "SpellDescriptionsPatch",
    "NPCNamesPatch",
    "PlaceNamesPatch",
}
_CANNOT_MERGE_PATCH = {
    "EventText",
    "MenuDialogs",
    "SoapstoneMessages",
    "MenuHelpSnippets",
    "KeyGuide",
    "MenuText_Other",
    "MenuText_Common",
}
