from __future__ import annotations

__all__ = [
    "traverse_path_tree",
    "BiDict",
    "get_startupinfo",
    "partialmethod",
    "Timer",
    "Flags8",
]

import abc
import functools
import logging
import subprocess
import time

_LOGGER = logging.getLogger(__name__)


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


class partialmethod(functools.partialmethod):
    """Wrapper for `partialmethod` that adds a `__call__` attribute to stop PyCharm from complaining."""

    __call__ = None


class Timer:

    def __init__(self, name: str):
        self._name = name

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *exc):
        if any(exc):
            _LOGGER.error(f"{self._name} FAILED after {time.time() - self._start} s.")
        else:
            _LOGGER.info(f"{self._name} COMPLETED in {time.time() - self._start} s.")


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
