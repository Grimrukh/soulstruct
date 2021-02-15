from __future__ import annotations

import abc
import logging
import typing as tp
from copy import deepcopy
from pathlib import Path

from soulstruct.containers.bnd import BND
from .fmg import BaseFMG

if tp.TYPE_CHECKING:
    from soulstruct.containers.bnd import BaseBND
    from soulstruct.utilities import BiDict

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

    _MSGBND_INDEX_NAMES = None  # type: BiDict[str, str]

    FMG_CLASS = None  # type: tp.Type[BaseFMG]

    def __init__(self, msg_directory=None):
        """Unpack all text data in given folder (from both 'item' and 'menu' MSGBND files) into one unified structure.

        You can access and modify the `entries` attributes of each loaded `FMG` instance using the names of the FMGs,
        which I have translated into a standard list (see game-specific attribute hints). The source (item/menu) of the
        FMG and its type (standard/Patch) are handled internally.
        , though the latter does not matter in either version of DS1
        (and neither do the names of the FMG files in the MSGBND archives)

        Args:
            msg_directory: Directory containing 'item.msgbnd[.dcx]' and 'menu.msgbnd[.dcx]', in any of the language
                folders (such as 'ENGLISH' or 'engus') within the 'msg' directory in your game installation.
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

        ext = "msgbnd.dcx" if self.IS_DCX else "msgbnd"
        self.item_msgbnd = BND(self.directory / f"item.{ext}")
        self.menu_msgbnd = BND(self.directory / f"menu.{ext}")

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
            fmg = self.FMG_CLASS(entry.data)
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
        bnd_entry = msgbnd.entries_by_id[bnd_entry_id]
        bnd_entry.data = fmg_data
        if not use_original_names:
            bnd_entry.path = bnd_entry.path.replace(self._original_names[fmg_name], fmg_name + ".fmg")

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

            if fmg_name + "Patch" in self._is_menu:
                # Updates patch only, if available.
                fmg_name = fmg_name + "Patch"

            fmg_msgbnd = new_menu_msgbnd if self._is_menu[fmg_name] else new_item_msgbnd
            self.update_msgbnd_entry(
                fmg_msgbnd,
                fmg_name,
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
        new_item_msgbnd.write(msg_directory / new_item_msgbnd.path.name)
        new_menu_msgbnd.write(msg_directory / new_menu_msgbnd.path.name)

        _LOGGER.info("MSGDirectory files (`item` and `menu` MSGBND files) written successfully.")

        if update_instance:
            # Update BNDs only after successful write.
            self.item_msgbnd = new_item_msgbnd
            self.menu_msgbnd = new_menu_msgbnd

    def get_all_item_text(self, index, item_type="good"):
        """ Get name, summary, and description of goods, weapons, armor, or rings. """
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
        """ Remove entries for item name, summary, and description. """
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
    "RingNamesPatch",
    "RingSummariesPatch",
    "RingDescriptionsPatch",
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
