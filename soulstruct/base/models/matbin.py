from __future__ import annotations

__all__ = ["MATBIN", "MATBINBND"]

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

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MATBIN(GameFile):
    """Material definition file used from Elden Ring onwards, completely replacing `MTD` format.

    Note that Elden Ring still has an `mtd` folder with MTD Binders inside it, and FLVER textures may reference '.mtd'
    material definitions, but the files are unused and the FLVER texture suffixes are ignored. FLVER texture suffix in
    MATBIN games is typically '.matxml' (which this file presumably converts to, internally) but again, the suffix is
    ignored.
    """
    
    @dataclass(slots=True)
    class HeaderStruct(BinaryStruct):
        _magic: bytes = field(init=False, **BinaryString(4, asserted=b"MAB\0"))
        _two: int = field(init=False, **Binary(asserted=2))
        _shader_path_offset: ulong
        _source_path_offset: ulong
        key: uint
        _param_count: int
        _sampler_count: int
        _pad: bytes = field(init=False, **BinaryPad(0x14))        

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

    def get_param(self, matbin_param_name: str, default=None) -> bool | int | list[int] | float | list[float]:
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

    def get_all_sampler_stems(self) -> dict[str, str]:
        return {sampler.sampler_type: Path(sampler.path).stem if sampler.path else "" for sampler in self.samplers}

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


@dataclass(slots=True)
class MATBINParam:
    """Generic parameter used in a MATBIN."""

    @dataclass(slots=True)
    class ParamStruct(BinaryStruct):
        _name_offset: long
        _value_offset: long
        key: uint
        param_type: MATBINParamType = field(**Binary("i"))
        _pad: bytes = field(init=False, **BinaryPad(16))

    name: str = ""
    value: bool | int | list[int] | float | list[float] = 0
    key: int = 0
    param_type: MATBINParamType = MATBINParamType.Int

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
                    value = list(reader.unpack("2i"))
                case MATBINParamType.Float:
                    value = reader["f"]
                case MATBINParamType.Float2:
                    value = list(reader.unpack("2f"))
                case MATBINParamType.Float3:
                    value = list(reader.unpack("3f"))  # NOTE: Two extra (useless) floats ignored.
                case MATBINParamType.Float4:
                    value = list(reader.unpack("4f"))
                case MATBINParamType.Float5:
                    value = list(reader.unpack("5f"))
                case _:
                    raise ValueError(f"Unknown MATBIN parameter type: {param_struct.param_type}")

        return param_struct.to_object(cls, name=name, value=value)

    def to_matbin_writer(self, writer: BinaryWriter):
        """Write header information. Name and value are written afterward (below)."""
        self.ParamStruct.object_to_writer(
            self,
            writer,
            _name_offset=RESERVED,
            _value_offset=RESERVED,
        )

    def fill_matbin_data(self, writer: BinaryWriter):
        """Fill name and data."""
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

    def __repr__(self):
        """`key` isn't needed and `param_type` is already clear from the value type."""
        return f"MATBINParam({self.name}={self.value})"


@dataclass(slots=True)
class MATBINSampler:
    """Texture samplers used in a MATBIN."""

    @dataclass(slots=True)
    class SamplerStruct(BinaryStruct):
        _sampler_type_offset: long
        _path_offset: long
        key: uint
        unk_x14: Vector2
        _pad: bytes = field(init=False, **BinaryPad(0x14))

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


@dataclass(slots=True)
class MATBINBND(Binder):

    _BUNDLED: tp.ClassVar[dict[Game, MATBINBND]] = {}

    use_lazy_load: bool = True  # if True, entries will only be loaded into `MATBIN` instances when requested
    matbins: dict[str, MATBIN] = field(default_factory=dict)

    def __post_init__(self):
        """Loads FIRST instance of each entry name as an MATBIN."""
        super(MATBINBND, self).__post_init__()

        if self.matbins or self.use_lazy_load:
            return  # already passed in, or lazy loading enabled

        self.matbins = {}
        for entry in self.entries:
            if entry.name in self.matbins:
                continue  # ignore repeated names silently
            self.matbins[entry.name] = entry.to_binary_file(MATBIN)

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
