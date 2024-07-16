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


IDListElementType = tp.TypeVar("IDListElementType")


class IDList(list[IDListElementType]):
    """List that checks for membership by object ID instead of equality."""
    def __contains__(self, item: IDListElementType):
        for i in self:
            if id(i) == id(item):
                return True
        return False

    def index(self, item: IDListElementType, start=None, stop=None) -> int:
        """Index exact instance `entry`. Returns -1 if absent rather than raising an error."""
        for i, e in enumerate(self):
            if start is not None and i < start:
                continue
            if stop is not None and i >= stop:
                break
            if e is item:
                return i
        return -1

    def remove(self, item: IDListElementType):
        """Remove entry from this list, by ID, not `__eq__`."""
        for i, e in enumerate(self):
            if e is item:
                del self[i]
                return
        raise ValueError(f"Item `{item}` is not in list.")

    def count(self, item: IDListElementType):
        """Counts the number of times the exact instance `item` appears in this list."""
        return sum(1 for i in self if id(i) == id(item))

    def __eq__(self, other):
        return all(id(a) == id(b) for a, b in zip(self, other))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        """Hash by ID, not `__eq__`."""
        return hash(tuple(id(i) for i in self))
