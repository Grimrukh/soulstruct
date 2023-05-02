from __future__ import annotations

__all__ = ["DrawParamDirectory"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file_directory import GameFileDirectory
from .drawparambnd import DrawParamBND

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "DrawParamDirectory"

_LOGGER = logging.getLogger(__name__)


def drawparambnd_property(area_name: str):
    return property(lambda self: self.files[f"{area_name}_DrawParam"])


@dataclass(slots=True)
class DrawParamDirectory(GameFileDirectory[DrawParamBND], abc.ABC):

    FILE_NAME_PATTERN: tp.ClassVar[str] = r"(a\d\d|default)_DrawParam\.parambnd"
    FILE_CLASS: tp.ClassVar[tp.Type[DrawParamBND]] = DrawParamBND
    FILE_EXTENSION: tp.ClassVar[str] = ".parambnd"

    # Display descriptions of map areas. Prepended to '_DrawParam' suffix to get BND file stem.
    DRAW_PARAM_AREAS: tp.ClassVar[dict[str, str]] = {
        "a10": "Depths (00), Undead Burg/Parish (01), Firelink Shrine (02)",
        "a11": "Painted World (00)",
        "a12": "Darkroot Garden / Darkroot Basin (00), Royal Wood / Oolacile / Chasm of the Abyss (01)",
        "a13": "Catacombs (00), Tomb of the Giants (01), Great Hollow / Ash Lake (02)",
        "a14": "Blighttown / Quelaag's Domain (00), Demon Ruins / Lost Izalith (01)",
        "a15": "Sen's Fortress (00), Anor Londo (01)",
        "a16": "New Londo Ruins / Valley of Drakes (00)",
        "a17": "Duke's Archives (00)",
        "a18": "Kiln of the First Flame (00), Undead Asylum (01)",
        "a99": "Test Map",
        "default": "Menus",
    }

    # Type override.
    files: dict[str, DrawParamBND] = field(default_factory=dict)

    a10 = drawparambnd_property("a10")  # type: DrawParamBND
    a11 = drawparambnd_property("a11")  # type: DrawParamBND
    a12 = drawparambnd_property("a12")  # type: DrawParamBND
    a13 = drawparambnd_property("a13")  # type: DrawParamBND
    a14 = drawparambnd_property("a14")  # type: DrawParamBND
    a15 = drawparambnd_property("a15")  # type: DrawParamBND
    a16 = drawparambnd_property("a16")  # type: DrawParamBND
    a17 = drawparambnd_property("a17")  # type: DrawParamBND
    a18 = drawparambnd_property("a18")  # type: DrawParamBND
    a99 = drawparambnd_property("a99")  # type: DrawParamBND
    default = drawparambnd_property("default")  # type: DrawParamBND

    def get_drawparambnd(self, draw_param_stem: str) -> DrawParamBND:
        """Get `DrawParamBND` by 'mXX' name, 'aXX' name, or 'default', with or without '_DrawParam' suffix."""
        draw_param_stem = draw_param_stem.split(".")[0]
        if draw_param_stem == "default":
            return self.files["default_DrawParam"]
        if draw_param_stem.startswith("m"):
            draw_param_stem = "a" + draw_param_stem[1:]
        if draw_param_stem in self.DRAW_PARAM_AREAS:
            return self.files[f"{draw_param_stem}_DrawParam"]
        raise KeyError(f"Invalid `DrawParamBND` in this `DrawParamDirectory`: {draw_param_stem}")

    @classmethod
    def from_path(cls, directory_path: Path | str):
        # NOTE: Pattern is still used in combination with `Map` stems.
        if cls.FILE_NAME_PATTERN is None or cls.FILE_CLASS is None:
            raise TypeError(
                f"`GameFileDirectory` subclass `{cls.__name__}` must define `FILE_NAME_PATTERN` and `FILE_CLASS` class "
                f"variables, or override `from_path()` with its own different logic."
            )

        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")

        all_bnd_stems = cls.get_all_file_stems()

        files = {}
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?$")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_bnd_stems:
                    files[file_stem] = cls.FILE_CLASS.from_path(file_path)
                    all_bnd_stems.remove(file_stem)
                else:
                    _LOGGER.warning(
                        f"Ignoring file with unrecognized area stem in `{cls.__name__}` directory: {file_path.name}"
                    )
                    continue
            else:
                _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")
                continue

        if all_bnd_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_bnd_stems)}")

        return cls(directory=directory_path, files=files)

    def write(self, directory_path: Path | str | None = None, check_file_hashes: bool = False):
        """Same as `GameFileDirectory`, but reports unknown files and if any maps are missing."""
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)
        directory_path.mkdir(parents=True, exist_ok=True)

        all_bnd_stems = self.get_all_file_stems()

        for file_stem, draw_param_bnd in self.files.items():
            if file_stem in all_bnd_stems:
                all_bnd_stems.remove(file_stem)
            else:
                _LOGGER.warning(f"Writing unknown area file found in `{self.__class__.__name__}`: {file_stem}")
            draw_param_bnd.write(directory_path / f"{file_stem}{self.FILE_EXTENSION}", check_hash=check_file_hashes)
        if all_bnd_stems:
            _LOGGER.warning(
                f"Could not find some files while writing `{self.__class__.__name__}` directory: "
                f"{', '.join(all_bnd_stems)}"
            )
        _LOGGER.info(
            f"`{self.__class__.__name__}` written to `{directory_path}` successfully ({len(self.files)} files)."
        )

    @classmethod
    def from_json_directory(cls, directory: Path | str) -> Self:
        directory = Path(directory)
        files = {}

        all_bnd_stems = cls.get_all_file_stems()

        for bnd_stem in tuple(all_bnd_stems):
            if (bnd_json_directory := directory / bnd_stem).is_dir():
                drawparambnd = cls.FILE_CLASS.from_json_directory(bnd_json_directory)
            elif (bnd_json := directory / f"{bnd_stem}.json").is_file():
                # TODO: Not actually supported properly by `DrawParamBND` yet.
                drawparambnd = cls.FILE_CLASS.from_json(bnd_json)
            else:
                continue  # can't find file
            all_bnd_stems.remove(bnd_stem)
            files[bnd_stem] = drawparambnd

        if all_bnd_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_bnd_stems)}")

        return cls(directory=directory, files=files)

    def write_json_directory(self, directory: Path | str = None, ignore_pads=True, ignore_defaults=True):
        """Write all `DrawParamBND` files into their own nested directories of `DrawParam` JSONs."""
        if directory is None:
            directory = self.directory
        else:
            directory = Path(directory)

        all_bnd_stems = self.get_all_file_stems()

        for file_stem, drawparambnd in self.files.items():
            if file_stem in all_bnd_stems:
                all_bnd_stems.remove(file_stem)
            else:
                _LOGGER.warning(
                    f"Writing JSON for unknown `DrawParamBND` file found in `{self.__class__.__name__}`: {file_stem}"
                )
            drawparambnd.write_json_directory(directory / file_stem, ignore_pads, ignore_defaults)

    def __getitem__(self, area_name: str) -> DrawParamBND:
        if not area_name.endswith("_DrawParam"):
            area_name += "_DrawParam"
        return self.files[area_name]

    @classmethod
    def get_all_file_stems(cls) -> list[str]:
        return [f"{area_name}_DrawParam" for area_name in cls.DRAW_PARAM_AREAS]
