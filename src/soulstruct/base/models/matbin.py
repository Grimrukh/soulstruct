from __future__ import annotations

__all__ = ["MATBIN", "MATBINBND", "MATBIN_PARAM_TYPING"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.games import Game, get_game
from soulstruct.containers import Binder, EntryNotFoundError
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector2

_LOGGER = logging.getLogger(__name__)


MATBIN_PARAM_TYPING = tp.Union[
    bool,
    int,
    tuple[int, int],
    float,
    tuple[float, float],
    tuple[float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float, float],  # new type not supported in MTD
]

class MATBIN(GameFile):
    """Material definition file used from Elden Ring onwards, completely replacing `MTD` format.

    Note that Elden Ring still has an `mtd` folder with MTD Binders inside it, and FLVER textures may reference '.mtd'
    material definitions, but the files are unused and the FLVER texture suffixes are ignored. FLVER texture suffix in
    MATBIN games is typically '.matxml' (which this file presumably converts to, internally) but again, the suffix is
    ignored.
    """
    
    class HeaderStruct(BinaryStruct):
        _magic: bytes = binary_string(4, asserted=b"MAB\0", init=False)
        _two: int = binary(asserted=2, init=False)
        _shader_path_offset: ulong
        _source_path_offset: ulong
        key: uint
        _param_count: int
        _sampler_count: int
        _pad: bytes = binary_pad(0x14, init=False)

    shader_path: str = ""  # '.spx'
    source_path: str = ""  # '.matxml' or '.mtd'
    key: int = 0
    params: list[MATBINParam] = field(default_factory=list)
    samplers: list[MATBINSampler] = field(default_factory=list)
    
    @classmethod
    def from_reader(cls, reader: BinaryReader):
        header = cls.HeaderStruct.from_bytes(reader)
        params = [MATBINParam.from_matbin_reader(reader) for _ in range(header.pop("_param_count"))]
        samplers = [MATBINSampler.from_matbin_reader(reader) for _ in range(header.pop("_sampler_count"))]
        shader_path = reader.unpack_string(offset=header.pop("_shader_path_offset"), encoding="utf-16-le")
        source_path = reader.unpack_string(offset=header.pop("_source_path_offset"), encoding="utf-16-le")
        return header.to_object(
            cls,
            shader_path=shader_path,
            source_path=source_path,
            params=params,
            samplers=samplers,
        )

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
        self.HeaderStruct.object_to_writer(
            self,
            writer,
            _shader_path_offset=RESERVED,
            _source_path_offset=RESERVED,
            _param_count=len(self.params),
            _sampler_count=len(self.samplers),
        )
        
        for i, param in enumerate(self.params):
            param.to_matbin_writer(writer)
        for i, sampler in enumerate(self.samplers):
            sampler.to_matbin_writer(writer)
        for i, param in enumerate(self.params):
            param.fill_matbin_data(writer)
        for i, sampler in enumerate(self.samplers):
            sampler.fill_matbin_data(writer)
        
        writer.fill_with_position("_shader_path_offset", self)
        writer.append(self.shader_path.encode("utf-16-le"))
        writer.fill_with_position("_source_path_offset", self)
        writer.append(self.source_path.encode("utf-16-le"))
        
        return writer

    def has_param(self, matbin_param_name: str) -> bool:
        for param in self.params:
            if param.name == matbin_param_name:
                return True
        return False

    # Overloads of `get_param` that detect return type from `default` argument.

    @tp.overload
    def get_param(self, matbin_param_name: str, default: bool) -> bool:
        ...

    @tp.overload
    def get_param(self, matbin_param_name: str, default: int) -> int:
        ...

    @tp.overload
    def get_param(self, matbin_param_name: str, default: tuple[int, int]) -> tuple[int, int]:
        ...

    @tp.overload
    def get_param(self, matbin_param_name: str, default: float) -> float:
        ...

    @tp.overload
    def get_param(self, matbin_param_name: str, default: tuple[float, float]) -> tuple[float, float]:
        ...

    @tp.overload
    def get_param(
        self, matbin_param_name: str, default: tuple[float, float, float]
    ) -> tuple[float, float, float]:
        ...

    @tp.overload
    def get_param(
        self, matbin_param_name: str, default: tuple[float, float, float, float]
    ) -> tuple[float, float, float, float]:
        ...

    @tp.overload
    def get_param(
        self, matbin_param_name: str, default: tuple[float, float, float, float, float]
    ) -> tuple[float, float, float, float, float]:
        ...

    def get_param(self, matbin_param_name: str, default=None) -> MATBIN_PARAM_TYPING:
        """Get param value by name, or a default value. If `default is None`, raises KeyError if param not found."""
        for param in self.params:
            if param.name == matbin_param_name:
                return param.value
        if default is not None:
            return default
        raise KeyError(
            f"MATBIN param '{matbin_param_name}' not found in MATBIN from path '{self.path}' and no default given."
        )

    def has_sampler_type(self, matbin_sampler_type: str) -> bool:
        for sampler in self.samplers:
            if sampler.sampler_type == matbin_sampler_type:
                return True
        return False

    def get_all_sampler_paths(self) -> dict[str, Path | None]:
        return {sampler.sampler_type: Path(sampler.path) if sampler.path else None for sampler in self.samplers}

    def get_all_sampler_names(self) -> dict[str, str]:
        return {sampler.sampler_type: Path(sampler.path).name if sampler.path else "" for sampler in self.samplers}

    def get_all_sampler_stems(self, lower=False) -> dict[str, str]:
        stems = {}
        for sampler in self.samplers:
            if not sampler.path:
                stems[sampler.sampler_type] = ""
            elif lower:
                stems[sampler.sampler_type] = Path(sampler.path).stem.lower()
            else:
                stems[sampler.sampler_type] = Path(sampler.path).stem
        return stems

    def get_sampler_path(self, matbin_sampler_type: str) -> str:
        for sampler in self.samplers:
            if sampler.sampler_type == matbin_sampler_type:
                return sampler.path
        raise KeyError(
            f"MATBIN sampler type '{matbin_sampler_type}' not found in MATBIN from path '{self.path}'."
        )

    def get_sampler_stem(self, matbin_sampler_type: str) -> str:
        for sampler in self.samplers:
            if sampler.sampler_type == matbin_sampler_type:
                return Path(sampler.path).stem  # drops '.tif' extension
        raise KeyError(
            f"MATBIN sampler type '{matbin_sampler_type}' not found in MATBIN from path '{self.path}'."
        )

    @property
    def shader_name(self):
        return Path(self.shader_path).name

    @property
    def shader_stem(self):
        return Path(self.shader_path).stem

    @property
    def source_name(self):
        return Path(self.source_path).name

    @property
    def source_stem(self):
        return Path(self.source_path).stem

    def __repr__(self):
        params = "\n".join(f"    {param.name} = {param.value}" for param in self.params)
        samplers = "\n".join(f"    {sampler.sampler_type} = \"{sampler.path}\"," for sampler in self.samplers)
        return (
            f"MATBIN(\n"
            f"  shader_path=\"{self.shader_path}\",\n"
            f"  source_path=\"{self.source_path}\",\n"
            f"  params={{\n{params},\n  }},\n"
            f"  samplers={{\n{samplers}\n  }},\n"
            f")"
        )


class MATBINParamType(IntEnum):
    Bool = 0
    Int = 4
    Int2 = 5
    Float = 8
    Float2 = 9
    Float3 = 10  # NOTE: Five floats actually stored in file, but as per `SoulsFormats`, the last two are discarded.
    Float4 = 11
    Float5 = 12


@dataclass(slots=True, init=False)
class MATBINParam:
    """Generic parameter used in a MATBIN."""

    class ParamStruct(BinaryStruct):
        _name_offset: long
        _value_offset: long
        key: uint
        param_type: MATBINParamType = binary(int)
        _pad: bytes = binary_pad(16, init=False)

    name: str = ""
    param_type: MATBINParamType = MATBINParamType.Int
    _value: MATBIN_PARAM_TYPING = 0
    key: int = 0

    def __init__(self, name: str, param_type: MATBINParamType, value: MATBIN_PARAM_TYPING = None, key=0):
        self.name = name
        self.param_type = param_type
        self._value = self.get_default_value(param_type) if value is None else self.validate_value_type(param_type, value)
        self.key = key

    @classmethod
    def from_matbin_reader(cls, reader: BinaryReader):
        """"""
        param_struct = cls.ParamStruct.from_bytes(reader)
        name = reader.unpack_string(offset=param_struct.pop("_name_offset"), encoding="utf-16-le")

        with reader.temp_offset(param_struct.pop("_value_offset")):
            match param_struct.param_type:
                case MATBINParamType.Bool:
                    value = reader["?"]
                case MATBINParamType.Int:
                    value = reader["i"]
                case MATBINParamType.Int2:
                    value = reader.unpack("2i")
                case MATBINParamType.Float:
                    value = reader["f"]
                case MATBINParamType.Float2:
                    value = reader.unpack("2f")
                case MATBINParamType.Float3:
                    value = reader.unpack("3f")  # NOTE: Two extra (useless) floats ignored
                case MATBINParamType.Float4:
                    value = reader.unpack("4f")
                case MATBINParamType.Float5:
                    value = reader.unpack("5f")
                case _:
                    raise ValueError(f"Unknown MATBIN parameter type: {param_struct.param_type}")

        return cls(name, param_struct.param_type, value, param_struct.key)

    def to_matbin_writer(self, writer: BinaryWriter):
        """Write header information. Name and value are written afterward (below)."""
        self.ParamStruct.object_to_writer(
            self,
            writer,
            _name_offset=RESERVED,
            _value_offset=RESERVED,
        )

    # noinspection PyArgumentList
    def fill_matbin_data(self, writer: BinaryWriter):
        """Fill name and data.

        Type of `self.value` is ensured by `value.setter` property.
        """
        writer.fill_with_position("_name_offset", self)
        writer.append(self.name.encode("utf-16-le"))

        writer.fill_with_position("_value_offset", self)
        match self.param_type:
            case MATBINParamType.Bool:
                writer.pack("?", self.value)
            case MATBINParamType.Int:
                writer.pack("i", self.value)
            case MATBINParamType.Int2:
                writer.pack("2i", *self.value)
            case MATBINParamType.Float:
                writer.pack("f", self.value)
            case MATBINParamType.Float2:
                writer.pack("2f", *self.value)
            case MATBINParamType.Float3:
                writer.pack("5f", *self.value, 1.0, 1.0)  # two extra 1s written
            case MATBINParamType.Float4:
                writer.pack("4f", *self.value)
            case MATBINParamType.Float5:
                writer.pack("5f", *self.value)
            case _:
                raise ValueError(f"Unknown MATBIN parameter type: {self.param_type}")

    @property
    def value(self) -> MATBIN_PARAM_TYPING:
        return self._value

    @value.setter
    def value(self, value: MATBIN_PARAM_TYPING) -> None:
        self._value = self.validate_value_type(self.param_type, value)

    def __repr__(self):
        """`key` isn't needed and `param_type` is already clear from the value type."""
        return f"MATBINParam({self.name}={self.value})"

    @staticmethod
    def get_default_value(param_type: MATBINParamType) -> MATBIN_PARAM_TYPING:
        match param_type:
            case MATBINParamType.Bool:
                return False
            case MATBINParamType.Int:
                return 0
            case MATBINParamType.Int2:
                return 0, 0
            case MATBINParamType.Float:
                return 0.0
            case MATBINParamType.Float2:
                return 0.0, 0.0
            case MATBINParamType.Float3:
                return 0.0, 0.0, 0.0
            case MATBINParamType.Float4:
                return 0.0, 0.0, 0.0, 0.0
            case MATBINParamType.Float5:
                return 0.0, 0.0, 0.0, 0.0, 0.0
            case _:
                raise TypeError(f"Invalid `param_type` for MATBINParam: {param_type}")

    @staticmethod
    def validate_value_type(param_type: MATBINParamType, value: MATBIN_PARAM_TYPING) -> MATBIN_PARAM_TYPING:
        match param_type:
            case MATBINParamType.Bool:
                if not isinstance(value, bool):
                    raise ValueError(f"Expected bool, got {type(value)}")
            case MATBINParamType.Int:
                if not isinstance(value, int):
                    raise ValueError(f"Expected int, got {type(value)}")
            case MATBINParamType.Int2:
                if (
                    not isinstance(value, tuple)
                    or len(value) != 2
                    or not all(isinstance(v, int) for v in value)
                ):
                    raise ValueError(f"Expected (int, int), got {value}")
            case MATBINParamType.Float:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"Expected float (or int), got {type(value)}")
            case MATBINParamType.Float2:
                if (
                    not isinstance(value, tuple)
                    or len(value) != 2
                    or not all(isinstance(v, (int, float)) for v in value)
                ):
                    raise ValueError(f"Expected (int | float, int | float), got {value}")
            case MATBINParamType.Float3:
                if (
                    not isinstance(value, tuple)
                    or len(value) != 3
                    or not all(isinstance(v, (int, float)) for v in value)
                ):
                    raise ValueError(f"Expected (int | float, int | float, int | float), got {value}")
            case MATBINParamType.Float4:
                if (
                    not isinstance(value, tuple)
                    or len(value) != 4
                    or not all(isinstance(v, (int, float)) for v in value)
                ):
                    raise ValueError(f"Expected (int | float, int | float, int | float, int | float), got {value}")
            case MATBINParamType.Float5:
                if (
                    not isinstance(value, tuple)
                    or len(value) != 5
                    or not all(isinstance(v, (int, float)) for v in value)
                ):
                    raise ValueError(
                        f"Expected (int | float, int | float, int | float, int | float, int | float), got {value}"
                    )
            case _:
                raise ValueError(f"Unknown MATBIN parameter type: {param_type}")

        return value

@dataclass(slots=True)
class MATBINSampler:
    """Texture samplers used in a MATBIN."""

    class SamplerStruct(BinaryStruct):
        _sampler_type_offset: long
        _path_offset: long
        key: uint
        unk_x14: Vector2
        _pad: bytes = binary_pad(0x14, init=False)

    sampler_type: str = ""
    path: str = ""
    key: int = 0
    unk_x14: Vector2 = field(default_factory=lambda: Vector2.zero)

    @classmethod
    def from_matbin_reader(cls, reader: BinaryReader):
        """"""
        sampler_struct = cls.SamplerStruct.from_bytes(reader)
        sampler_type = reader.unpack_string(offset=sampler_struct.pop("_sampler_type_offset"), encoding="utf-16-le")
        path = reader.unpack_string(offset=sampler_struct.pop("_path_offset"), encoding="utf-16-le")
        return sampler_struct.to_object(cls, sampler_type=sampler_type, path=path)

    def to_matbin_writer(self, writer: BinaryWriter):
        """Write header information. Name and value are written afterward (below)."""
        self.SamplerStruct.object_to_writer(
            self,
            writer,
            _sampler_type_offset=RESERVED,
            _path_offset=RESERVED,
        )

    def fill_matbin_data(self, writer: BinaryWriter):
        """Fill sampler type and path."""
        writer.fill_with_position("_sampler_type_offset", self)
        writer.append(self.sampler_type.encode("utf-16-le"))

        writer.fill_with_position("_path_offset", self)
        writer.append(self.path.encode("utf-16-le"))


class MATBINBND(Binder):

    IS_SPLIT_BXF: tp.ClassVar[bool] = False

    _BUNDLED: tp.ClassVar[dict[Game, MATBINBND]] = {}

    matbins: dict[str, MATBIN] = field(default_factory=dict)

    def get_matbin(self, matbin_name: str) -> MATBIN:
        """Look up MATBIN name in Binder. Changes '.mtd' or '.matxml' suffix to '.matbin' if necessary."""
        if matbin_name.endswith(".matxml"):
            matbin_name = matbin_name.removesuffix(".matxml")
        elif matbin_name.endswith(".mtd"):
            matbin_name = matbin_name.removesuffix(".mtd")
        if not matbin_name.endswith(".matbin"):
            matbin_name += ".matbin"
        try:
            return self.matbins[matbin_name]
        except KeyError:
            try:
                # Need to ignore case.
                matbin_entry = self.find_entry_matching_name(re.escape(matbin_name), re.IGNORECASE)
            except EntryNotFoundError:
                raise KeyError(f"MATBIN '{matbin_name}' not found in {self.__class__.__name__}.")
            matbin = matbin_entry.to_binary_file(MATBIN)
            self.matbins[matbin_name] = matbin
            return matbin

    def load_all_matbins(self):
        """Load all MATBINs in the Binder into memory."""
        for entry in self.entries:
            if entry.name.lower().endswith(".matbin"):
                matbin = entry.to_binary_file(MATBIN)
                self.matbins[entry.name] = matbin

    @classmethod
    def from_bundled(cls, game_or_name: Game | str) -> MATBINBND:
        game = get_game(game_or_name)
        if game in cls._BUNDLED:
            return cls._BUNDLED[game]
        matbinbnd = None  # type: MATBINBND | None
        for resource_key, resource_path in game.bundled_resource_paths.items():
            if resource_key.endswith("MATBINBND"):
                if matbinbnd is None:
                    matbinbnd = cls.from_path(resource_path)
                else:
                    matbinbnd |= cls.from_path(resource_path)
        if not matbinbnd:
            raise FileNotFoundError(f"No bundled MATBINBND found for {game.name}.")
        cls._BUNDLED[game] = matbinbnd
        return matbinbnd

    @classmethod
    def from_path_or_bundled(cls, game_or_name: Game | str, matbinbnd_path: Path | None):
        if matbinbnd_path and matbinbnd_path.is_file():
            return cls.from_path(matbinbnd_path)
        return cls.from_bundled(game_or_name)

    @classmethod
    def combine_matbinbnds(cls, *matbinbnds: MATBINBND):
        """Combine multiple MATBINBND Binders into one.

        Combines both raw BND entries and pre-loaded MATBINs.
        """
        combined = cls()
        for matbinbnd in matbinbnds:
            for matbin_name, matbin in matbinbnd.matbins.items():
                if matbin_name in combined.matbins:
                    _LOGGER.warning(f"MATBIN '{matbin_name}' already exists in combined MATBINBND. Replacing...")
                combined.matbins[matbin_name] = matbin
            entries_by_name = combined.get_entries_by_name()
            for entry in matbinbnd.entries:
                if entry.name in entries_by_name:
                    _LOGGER.warning(f"Entry '{entry.name}' already exists in combined MATBINBND. Replacing...")
                    combined.remove_entry_name(entry.name)
                combined.entries.append(entry)
                entries_by_name[entry.name] = entry
        return combined
