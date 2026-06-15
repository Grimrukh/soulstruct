from __future__ import annotations

__all__ = ["DataclassMeta", "PathDataclassMeta"]

import abc
import typing as tp
from dataclasses import dataclass
from pathlib import Path


@tp.dataclass_transform(kw_only_default=False)
class DataclassMeta(abc.ABCMeta):
    """Base metaclass for Soulstruct dataclasses that automatically applies `slots=True`.

    May be subclassed to hijack certain constructor overloads.
    """

    # Required to ensure we wrap with `dataclass` exactly once.
    __WRAPPED_TYPE_IDS: set[int] = set()

    __PRIMED_BASE_ID: int = 0

    def __new__(mcs, name, bases, namespace, **kwargs):

        cls = super().__new__(mcs, name, bases, namespace)

        if mcs.__PRIMED_BASE_ID > 0:
            # This must be a `dataclass` recursive call.
            mcs.__WRAPPED_TYPE_IDS.add(mcs.__PRIMED_BASE_ID)
            mcs.__PRIMED_BASE_ID = 0
            return cls  # true `dataclass`

        if not hasattr(cls, "__qualname__"):
            raise TypeError(f"Unprimed wrapped dataclass encountered by {mcs.__name__}.")

        mcs.__PRIMED_BASE_ID = id(cls)

        # TRICK: We copy '__classcell__' from `namespace`, if it exists, while we construct the new class. This
        # is necessary because `dataclass` has no choice but to construct a new class that uses `__slots__`, which
        # will break classes that user the zero-argument form of `super()` (they rely on the 'magical context' of
        # the classcell to get the correct class).
        # This trick works because `dataclasses._add_slots()` uses the class `__dict__`

        del_classcell = False
        if "__classcell__" in namespace:
            cls.__classcell__ = namespace["__classcell__"]
            del_classcell = True

        # noinspection PyArgumentList
        datacls = dataclass(cls, slots=True)

        if mcs.__PRIMED_BASE_ID > 0:
            raise ValueError("Dataclass was not wrapped successfully with `dataclass`.")

        if del_classcell:
            del cls.__classcell__

        return datacls


@tp.dataclass_transform(kw_only_default=False)
class PathDataclassMeta(DataclassMeta):
    """Extension of `DataclassMeta` that supports a special single `Path` argument.

    Either a single positional `Path` argument or a `path: Path | str` keyword argument will be intercepted. A
    positional `str` argument cannot be safely intercepted as the first dataclass field could be a `str` (but `Path`
    is extremely unlikely as a first field).
    """

    def __call__[T](cls: type[T], *args, **kwargs) -> T:
        """Intercept instance creation to handle the single-argument path case, which calls `cls.from_path(path)`."""
        if len(args) == 1 and isinstance(args[0], Path) and not kwargs:
            # Call `from_path` if a single `Path` positional argument is provided.
            return cls.from_path(args[0])
        if len(args) == 0 and len(kwargs) == 1 and isinstance(kwargs.get("path"), (Path, str)):
            # Call `from_path` if a single `path: Path` keyword argument is provided.
            return cls.from_path(kwargs["path"])
        # Otherwise, proceed with the normal dataclass constructor.
        return super(PathDataclassMeta, cls).__call__(*args, **kwargs)
