from __future__ import annotations

__all__ = [
    "MISSING_REF",
    "traverse_path_tree",
    "setdefault_lambda",
    "BiDict",
    "get_startupinfo",
    "Flags8",
    "IDList",
]

import abc
import logging
import subprocess
import typing as tp

_LOGGER = logging.getLogger("soulstruct")


class MissingReference:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MissingReference, cls).__new__(cls)
        return cls._instance

    def __eq__(self, other):
        raise TypeError("Cannot test MissingReference for equality.")

    def __repr__(self):
        return "<Missing Reference>"


# Singleton instance of MissingReference, for use as a default value when a reference is missing.
MISSING_REF = MissingReference()


def traverse_path_tree(tree, cur=()):
    if isinstance(tree, dict):
        for node, leaf in tree.items():
            for path in traverse_path_tree(leaf, cur + (node,)):
                yield path
    elif isinstance(tree, (list, tuple)):
        for item in tree:
            if isinstance(item, str):
                yield cur + (item,)
            else:  # dict
                for path in traverse_path_tree(item, cur):
                    yield path
    else:
        raise ValueError(f"Invalid type encountered in path tree: {type(tree)}")


def setdefault_lambda(dictionary: dict, key, default: tp.Callable[[], tp.Any]):
    """Avoids a 'gotcha' with `dict.setdefault`.

    If the default is expensive to compute, we only want to do that when it's actually needed!
    """
    if key not in dictionary:
        dictionary[key] = default()
    return dictionary[key]


class BiDict(dict):
    def __init__(self, *args):
        """Initialized with pairs of values to be connected."""
        super().__init__()
        self.__keys = []
        self.__values = []
        for arg in args:
            if not isinstance(arg, tuple) or len(arg) != 2:
                raise ValueError("BiDict can only be initialized with (value_1, value_2) tuple pair args.")
            self.__setitem__(*arg)

    def __setitem__(self, value_1, value_2):
        """Removes any pre-existing connections using either value.

        Order of values determines whether they will appear in `keys()` or `values()`.
        """
        if value_1 in self:
            del self[value_1]
            try:
                self.__keys.remove(value_1)
            except ValueError:
                pass
            try:
                self.__values.remove(value_1)
            except ValueError:
                pass
        if value_2 in self:
            del self[value_2]
            try:
                self.__keys.remove(value_2)
            except ValueError:
                pass
            try:
                self.__values.remove(value_2)
            except ValueError:
                pass
        super().__setitem__(value_1, value_2)
        super().__setitem__(value_2, value_1)
        self.__keys.append(value_1)
        self.__values.append(value_2)

    def __delitem__(self, key):
        super().__delitem__(key)
        super().__delitem__(self[key])

    def __len__(self):
        return super().__len__() // 2

    def __iter__(self):
        return iter(self.__keys)

    def keys(self):
        """Returns first elements of all set pairs."""
        return self.__keys

    def values(self):
        """Returns second elements of all set pairs."""
        return self.__values

    def items(self):
        """Returns all set pairs in order."""
        return zip(self.__keys, self.__values)


def get_startupinfo():
    """Disables command window for PyInstaller `--noconsole` option.

    See `https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess`
    """
    if hasattr(subprocess, "STARTUPINFO"):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
        si = None
    return si


class Flags8(abc.ABC):
    def __init__(self, byte: int):
        if isinstance(byte, Flags8):
            self.flags = byte.flags
        else:
            self.flags = [bool(2 ** i & byte) for i in range(8)]

    def __getitem__(self, i):
        return self.flags[i]

    def pack(self) -> int:
        return sum(2 ** i if enabled else 0 for i, enabled in enumerate(self.flags))

    __int__ = pack

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(str(int(f)) for f in self.flags)})"

    @classmethod
    def default(cls):
        return cls(0)


ElementType = tp.TypeVar("ElementType")


class IDList(tp.Generic[ElementType]):
    
    _list: list[ElementType]  # list of objects
    _index_dict: dict[int, int]  # maps object ID to list index (NOT ordered)
    _size: int  # number of objects in list
    
    def __init__(self, seq=()):
        self._list = []
        self._index_dict = {}
        self._size = 0
        for item in seq:
            # Need to watch for duplicates in `seq`.
            self.append(item)

    def append(self, item: ElementType) -> None:
        item_id = id(item)
        if item_id not in self._index_dict:
            self._index_dict[item_id] = self._size
            self._list.append(item)
            self._size += 1
        else:
            raise ValueError(f"Item `{item}` is already in `IDList`.")

    def extend(self, items: tp.Iterable[ElementType]) -> None:
        for item in items:
            self.append(item)

    def insert(self, index: int, item: ElementType) -> None:
        item_id = id(item)
        if item_id in self._index_dict:
            raise ValueError(f"Item `{item}` is already in `IDList`.")
        self._list.insert(index, item)
        self._index_dict[item_id] = index
        # Increment all later or equal indices in dict.
        for id_key, list_index in self._index_dict.items():
            if list_index >= index:
                self._index_dict[id_key] = list_index + 1
        self._size += 1

    def pop(self, index: int = -1) -> ElementType:
        item = self._list.pop(index)
        self._index_dict.pop(id(item))
        self._size -= 1
        return item

    def remove(self, item: ElementType) -> None:
        item_id = id(item)
        if item_id in self._index_dict:
            index = self._index_dict.pop(item_id)
            self._list.pop(index)
            self._size -= 1
        else:
            raise ValueError(f"Item `{item}` is not in `IDList`.")

    def clear(self) -> None:
        self._list.clear()
        self._index_dict.clear()
        self._size = 0

    def index(self, item: ElementType) -> int:
        item_id = id(item)
        if item_id in self._index_dict:
            return self._index_dict[item_id]
        print("ITEMS:")
        for o in self._list:
            print("   ", o.name, id(o), id(o) in self._index_dict)
        raise ValueError(f"Item `{item.name}` (ID {item_id}) is not in `IDList`.")

    def copy(self) -> IDList[ElementType]:
        new_list = IDList()
        new_list._list = self._list.copy()
        new_list._index_dict = self._index_dict.copy()
        new_list._size = self._size
        return new_list

    def sort(self, key=None, reverse=False):
        self._list.sort(key=key, reverse=reverse)
        # Regenerate dictionary completely.
        self._index_dict = {id(item): i for i, item in enumerate(self._list)}

    def __getitem__(self, index: int) -> ElementType:
        return self._list[index]

    def __setitem__(self, index: int, item: ElementType) -> None:
        item_id = id(item)
        if item_id in self._index_dict:
            raise ValueError(f"Item `{item}` is already in `IDList`.")
        old_item = self._list[index]
        self._list[index] = item
        self._index_dict.pop(id(old_item))
        self._index_dict[item_id] = index

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0

    def __iter__(self) -> tp.Iterator[ElementType]:
        return iter(self._list)

    def __contains__(self, item: ElementType) -> bool:
        return id(item) in self._index_dict

    def __eq__(self, other: IDList) -> bool:
        """Equal if dictionaries are exactly equal, ignoring dictionary order."""
        return self._index_dict == other._index_dict

    def __ne__(self, other: IDList) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """Hash by ID keys, not `__eq__`."""
        return hash(tuple(self._index_dict))

    def __setstate__(self, state):
        """We need to reconstruct the index dictionary from the list."""
        self._list = state["_list"]
        self._index_dict = state["_index_dict"]
        self._size = state["_size"]
        # Refresh indices in dict.
        self._index_dict = {id(item): i for i, item in enumerate(self._list)}

    def __repr__(self) -> str:
        return f"IDList({self._list})"
