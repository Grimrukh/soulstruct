from __future__ import annotations

import abc
import csv
import logging
import typing as tp
from copy import deepcopy
from pathlib import Path

from soulstruct.containers import Binder
from soulstruct.utilities.files import read_json, write_json
from .fmg import BaseFMG

if tp.TYPE_CHECKING:
    from soulstruct.base.binder_entry import BinderEntry
    from soulstruct.containers.bnd import BaseBND
    from soulstruct.utilities.misc import BiDict

__all__ = ["MSGDirectory"]
_LOGGER = logging.getLogger(__name__)


class MSGDirectory(abc.ABC):

    IS_DCX: bool = None

    # These are text categories you are likely to want to change in mod projects.
    MAIN_CATEGORIES = ()

    # These are text categories you are unlikely to change, whether it's for pragmatic
    # reasons or because they contain low-level menu/system text. Generally, new IDs
    # cannot be added to these categories without modifying the game engine.
    INTERNAL_CATEGORIES = ()

    ALL_CATEGORIES = ALL_FMG_NAMES = MAIN_CATEGORIES + INTERNAL_CATEGORIES

    _MSGBND_INDEX_NAMES = None  # type: BiDict[int, str]
    _ORIGINAL_PATCH_SUFFIX = ""

    FMG_CLASS = None  # type: tp.Type[BaseFMG]
    MSGBND_CLASS = None  # type: tp.Type[BaseBND]

    def __init__(self, msg_directory=None, use_json=False):
        """Unpack all text data in given folder (from both 'item' and 'menu' MSGBND files) into one unified structure.

        You can access and modify the `entries` attributes of each loaded `FMG` instance using the names of the FMGs,
        which I have translated into a standard list (see game-specific attribute hints). The source (item/menu) of the
        FMG and its type (standard/Patch) are handled internally.
        , though the latter does not matter in either version of DS1
        (and neither do the names of the FMG files in the MSGBND archives)

        Args:
            msg_directory: Directory containing 'item.msgbnd[.dcx]' and 'menu.msgbnd[.dcx]', in any of the language
                folders (such as 'ENGLISH' or 'engus') within the 'msg' directory in your game installation.
            use_json: if `True`, will assume the source is a path to a folder containing `item_manifest.json`,
                `menu_manifest.json`, and JSON file for each text category in those manifests' `entries`.
        """
        self.directory = None
        self._is_menu = {}  # Records whether each FMG belongs in 'item' or 'menu' MSGBND.
        self._original_names = {}  # Records original names of FMG files in BNDs.
        self.categories = {}  # type: dict[str, dict[int, str]]

        if msg_directory is None:
            self.item_msgbnd = None
            self.menu_msgbnd = None
            return

        self.directory = Path(msg_directory)

        if use_json:
            # BNDs will be generated from information in manifests.
            self.item_msgbnd = None
            self.menu_msgbnd = None
            self.load_json_dir(msg_directory, clear_old_data=False)
            return

        ext = "msgbnd.dcx" if self.IS_DCX else "msgbnd"
        self.item_msgbnd = Binder(self.directory / f"item.{ext}")
        self.menu_msgbnd = Binder(self.directory / f"menu.{ext}")

        self.load_fmg_entries_from_bnd(self.item_msgbnd, is_menu=False)
        self.load_fmg_entries_from_bnd(self.menu_msgbnd, is_menu=True)

        for key, fmg_dict in self.categories.items():
            setattr(self, key, fmg_dict)

    @classmethod
    def from_bnds(cls, item_msgbnd: BaseBND, menu_msgbnd: BaseBND):
        instance = cls()
        instance.item_msgbnd = item_msgbnd
        instance.menu_msgbnd = menu_msgbnd
        instance.load_fmg_entries_from_bnd(instance.item_msgbnd, is_menu=False)
        instance.load_fmg_entries_from_bnd(instance.menu_msgbnd, is_menu=True)
        for key, fmg_dict in instance.categories.items():
            setattr(instance, key, fmg_dict)
        return instance

    def load_fmg_entries_from_bnd(self, msgbnd: BaseBND, is_menu: bool):
        """Loads FMGs from given `msgbnd` into `categories` dictionary."""
        for entry in msgbnd:
            try:
                attr_name = self._MSGBND_INDEX_NAMES[entry.id]
            except KeyError:
                raise ValueError(f"MSGBND entry '{entry.path}' has unexpected index {entry.id} in its msgbnd.")
            self._original_names[attr_name] = entry.name
            self._is_menu[attr_name] = is_menu
            try:
                fmg = self.FMG_CLASS(entry.get_uncompressed_data())
            except Exception as ex:
                _LOGGER.error(f"Error encountered while loading FMG '{entry.name}': {ex}")
                raise
            if attr_name.endswith("Patch"):
                # Patch FMGs are used to update the base FMGs here.
                # Original source (patch or no) is not tracked; all entries will be written to patch FMG by `pack()`.
                attr_name = attr_name[:-5]
            self.categories.setdefault(attr_name, {}).update(fmg.entries)

    def update_msgbnd_entry(
        self, msgbnd, fmg_name, fmg_entries: dict, word_wrap_limit=None, pipe_to_newline=False, use_original_names=True
    ):
        fmg_data = self.FMG_CLASS({"entries": fmg_entries}).pack(
            word_wrap_limit=word_wrap_limit, pipe_to_newline=pipe_to_newline
        )
        try:
            bnd_entry_id = self._MSGBND_INDEX_NAMES[fmg_name]
        except IndexError:
            raise ValueError(f"Could not recover BND entry ID for FMG named {fmg_name}.")
        try:
            bnd_entry = msgbnd.entries_by_id[bnd_entry_id]  # type: BinderEntry
        except KeyError:
            # BND entry does not exist. If it's "Patch", we can try to create it by duplicating the path (and flags)
            # from the non-Patch version.
            if fmg_name.endswith("Patch"):
                bnd_entry = self.create_patch_msgbnd_entry(msgbnd, fmg_name, fmg_data)
            else:
                raise KeyError(
                    f"Text (FMG) category '{fmg_name}' does not exist in this `MSGDirectory` instance, and it is not a "
                    f"'Patch' FMG that could be created automatically."
                )
        else:
            bnd_entry.set_uncompressed_data(fmg_data)
        if not use_original_names:
            bnd_entry.path = bnd_entry.path.replace(self._original_names[fmg_name], fmg_name + ".fmg")

    def create_patch_msgbnd_entry(self, msgbnd: BaseBND, patch_fmg_name: str, data: bytes):
        non_patch_fmg_name = patch_fmg_name.removesuffix("Patch")
        if non_patch_fmg_name not in self._MSGBND_INDEX_NAMES:
            raise KeyError(f"Patch text (FMG) category '{patch_fmg_name}' is not a known Patch category for this game.")
        non_patch_entry_id = self._MSGBND_INDEX_NAMES[non_patch_fmg_name]
        non_patch_bnd_entry = msgbnd.entries_by_id[non_patch_entry_id]
        non_patch_entry_stem = Path(non_patch_bnd_entry.path).stem
        patch_entry_path = non_patch_bnd_entry.path.replace(
            non_patch_entry_stem, non_patch_entry_stem + self._ORIGINAL_PATCH_SUFFIX
        )
        bnd_entry = msgbnd.BinderEntry(
            data=data,
            entry_id=self._MSGBND_INDEX_NAMES[patch_fmg_name],
            path=patch_entry_path,
            flags=non_patch_bnd_entry.flags,
        )
        msgbnd.add_entry(bnd_entry)
        return bnd_entry

    def pack(
        self,
        description_word_wrap_limit=None,
        use_original_names=True,
        pipe_to_newline=True,
    ) -> tuple[BaseBND, BaseBND]:
        """Pack up and return new "item" and "menu" MSGBNDs. Does not modify any instance state."""
        new_item_msgbnd = deepcopy(self.item_msgbnd)  # type: BaseBND
        new_menu_msgbnd = deepcopy(self.menu_msgbnd)  # type: BaseBND

        for fmg_name, fmg_entries in self.categories.items():
            word_wrap = description_word_wrap_limit if "Descriptions" in fmg_name else None

            fmg_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            self.update_msgbnd_entry(
                fmg_msgbnd,
                fmg_name,
                fmg_entries,
                word_wrap_limit=word_wrap,
                pipe_to_newline=pipe_to_newline,
                use_original_names=use_original_names,
            )

            if fmg_name + "Patch" in self._MSGBND_INDEX_NAMES.values():
                # Updates patch version as well (with identical content), if it exists for this game and category.
                self.update_msgbnd_entry(
                    fmg_msgbnd,
                    fmg_name + "Patch",
                    fmg_entries,
                    word_wrap_limit=word_wrap,
                    pipe_to_newline=pipe_to_newline,
                    use_original_names=use_original_names,
                )

        return new_item_msgbnd, new_menu_msgbnd

    def write(
        self,
        msg_directory=None,
        description_word_wrap_limit=None,
        use_original_names=True,
        pipe_to_newline=True,
        update_instance=True,
    ):
        """Pack up and write new "item" and "menu" MSGBNDs. See `pack()` for more."""
        msg_directory = self.directory if msg_directory is None else Path(msg_directory)

        new_item_msgbnd, new_menu_msgbnd = self.pack(
            description_word_wrap_limit=description_word_wrap_limit,
            use_original_names=use_original_names,
            pipe_to_newline=pipe_to_newline,
        )

        # Write BNDs (to original directory by default).
        ext = "msgbnd.dcx" if self.IS_DCX else "msgbnd"
        new_item_msgbnd.write(msg_directory / f"item.{ext}")
        new_menu_msgbnd.write(msg_directory / f"menu.{ext}")

        _LOGGER.info("MSGDirectory files (`item` and `menu` MSGBND files) written successfully.")

        if update_instance:
            # Update BNDs only after successful write.
            self.item_msgbnd = new_item_msgbnd
            self.menu_msgbnd = new_menu_msgbnd

    def get_all_item_text(self, index, item_type="good"):
        """Get name, summary, and description of goods, weapons, armor, or rings."""
        item_fmg = self.resolve_item_type(item_type)
        if index not in self.categories[item_fmg + "Names"]:
            return None
        return {
            "name": self.categories[item_fmg + "Names"][index],
            "summary": self.categories[item_fmg + "Summaries"][index],
            "description": self.categories[item_fmg + "Descriptions"][index],
        }

    def add_item_text(self, index, item_type, name, summary, description):
        item_fmg = self.resolve_item_type(item_type)
        if index in self.categories[item_fmg + "Names"]:
            raise ValueError(
                f"Item with index {index} already exists in {item_fmg}Names: "
                f"{self.categories[item_fmg + 'Names'][index]}"
            )
        self.categories[item_fmg + "Names"][index] = name
        self.categories[item_fmg + "Summaries"][index] = summary
        self.categories[item_fmg + "Descriptions"][index] = description

    def delete_item_text(self, index, item_fmg="good"):
        """Remove entries for item name, summary, and description."""
        item_fmg = self.resolve_item_type(item_fmg)
        if index not in self.categories[item_fmg + "Names"]:
            raise ValueError(f"There is no {item_fmg} with index {index} to delete.")
        self.categories[item_fmg + "Names"][index] = ""
        self.categories[item_fmg + "Summaries"][index] = ""
        self.categories[item_fmg + "Descriptions"][index] = ""

    def change_item_text(self, text_dict, index=None, item_type=None, patch=False):
        if index is None:
            index = text_dict["index"]
        if not isinstance(index, (list, tuple)):
            index = (index,)
        if item_type is None:
            item_type = text_dict["item_type"]
        item_fmg = self.resolve_item_type(item_type)
        patch = "Patch" if patch else ""
        for i in index:
            if i not in self[item_fmg + "Names"]:
                _LOGGER.info(
                    f"NEW ENTRY: {item_fmg} with index {i} has been added ({text_dict.get('name', 'unknown name')})"
                )
            if "name" in text_dict:
                self[item_fmg + "Names" + patch][i] = text_dict["name"]
            if "summary" in text_dict:
                self[item_fmg + "Summaries" + patch][i] = text_dict["summary"]
            if "description" in text_dict:
                self[item_fmg + "Descriptions" + patch][i] = text_dict["description"]

    def find(self, search_string, replace_with=None, text_category=None, exclude_conversations=True):
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
        return iter(self.categories.items())

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
                for field, value in bnd.get_manifest_header(manifest).items():
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
                if entry.id in entry_ids:
                    _LOGGER.warning(
                        f"Binder entry ID {entry.id} appears more than once in `MSGDirectory` '{bnd_name}' MSGBND. "
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
        item_manifest = self.item_msgbnd.get_json_header()
        menu_manifest = self.menu_msgbnd.get_json_header()
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
                "entry_id": bnd_entry.id,
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
