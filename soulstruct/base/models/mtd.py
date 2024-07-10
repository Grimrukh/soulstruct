from __future__ import annotations

__all__ = [
    "MTD",
    "MTDParam",
    "MTDBND",
]

import logging
import typing as tp
from pathlib import Path

from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.base.game_file import GameFile
from soulstruct.games import Game, get_game
from soulstruct.containers import Binder
from soulstruct.utilities.binary import *
from soulstruct.utilities.future import StrEnum

try:
    Self = tp.Self
except AttributeError:
    Self = "MTDBND"

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MTD(GameFile):
    """Material definition file used in older games. Replaced by similar but more powerful `MATBIN` in newer games
    (from Elden Ring). Note that these newer games' FLVERs may still reference '.mtd' files, but the suffix is wrong."""

    shader_path: str
    description: str
    params: list[MTDParam] = field(default_factory=list)
    samplers: list[MTDSampler] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> MTD:
        reader.default_byte_order = ByteOrder.LittleEndian

        assert_block(reader, 0, 3, 0x01)  # file
        assert_block(reader, 1, 2, 0xB0)  # header

        magic = read_marked_string(reader, 0x34)
        if magic != "MTD ":
            raise ValueError(f"Expected 'MTD ' string in header, not: {magic}")
        if (m := reader["i"]) != 1000:
            raise ValueError(f"Expected 1000 after 'MTD ' string, not: {m}")
        assert_marker(reader, 0x01)

        assert_block(reader, 2, 4, 0xA3)  # data
        shader_path = read_marked_string(reader, 0xA3)
        description = read_marked_string(reader, 0x03)
        if (m := reader["i"]) != 1:
            raise ValueError(f"Expected 1 in MTD data, not {m}.")

        assert_block(reader, 3, 4, 0xA3)  # lists
        reader.assert_pad(4)
        assert_marker(reader, 0x03)

        param_count = reader["i"]
        mtd_params = [MTDParam.from_mtd_reader(reader) for _ in range(param_count)]
        assert_marker(reader, 0x03)

        sampler_count = reader["i"]
        mtd_samplers = [MTDSampler.from_mtd_reader(reader) for _ in range(sampler_count)]

        assert_marker(reader, 0x04)
        reader.assert_pad(4)  # end of lists

        assert_marker(reader, 0x04)
        reader.assert_pad(4)  # end of data

        assert_marker(reader, 0x04)
        reader.assert_pad(4)  # end of file

        return cls(
            shader_path,
            description,
            mtd_params,
            mtd_samplers,
        )

    def to_writer(self) -> BinaryWriter:
        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)

        file_block, file_block_offset = write_block(writer, 0, 3, 0x01)
        header_block, header_block_offset = write_block(writer, 1, 2, 0xB0)

        write_marked_string(writer, 0x34, "MTD ")
        writer.pack("i", 1000)
        header_block.fill(writer, "length", writer.position - header_block_offset)
        write_marker(writer, 0x01)

        data_block, data_block_offset = write_block(writer, 2, 4, 0xA3)
        write_marked_string(writer, 0xA3, self.shader_path)
        write_marked_string(writer, 0x03, self.description)
        writer.pack("i", 1)

        lists_block, lists_block_offset = write_block(writer, 3, 4, 0xA3)
        writer.pad(4)
        write_marker(writer, 0x03)
        writer.pack("i", len(self.params))
        for param in self.params:
            param.to_mtd_writer(writer)
        write_marker(writer, 0x03)
        writer.pack("i", len(self.samplers))
        for sampler in self.samplers:
            sampler.to_mtd_writer(writer)
        write_marker(writer, 0x04)
        writer.pad(4)

        lists_block.fill(writer, "length", writer.position - lists_block_offset)
        write_marker(writer, 0x04)
        writer.pad(4)

        data_block.fill(writer, "length", writer.position - data_block_offset)
        write_marker(writer, 0x04)
        writer.pad(4)

        file_block.fill(writer, "length", writer.position - file_block_offset)

        return writer

    def has_param(self, mtd_param_name: str) -> bool:
        for param in self.params:
            if param.name == mtd_param_name:
                return True
        return False

    def get_param(self, mtd_param_name: str, default=None) -> bool | int | list[int] | float | list[float]:
        for param in self.params:
            if param.name == mtd_param_name:
                return param.value
        if default is not None:
            return default
        raise KeyError(f"MTD param '{mtd_param_name}' not found in MTD from path '{self.path}' and no default given.")

    def has_sampler_type(self, sampler_type: str) -> bool:
        for sampler in self.samplers:
            if sampler.sampler_type == sampler_type:
                return True
        return False

    def get_sampler_type_uv_index(self, sampler_type: str) -> int:
        for sampler in self.samplers:
            if sampler.sampler_type == sampler_type:
                return sampler.uv_index
        raise KeyError(f"`MTDSampler` type '{sampler_type}' not found in MTD from path '{self.path}'.")

    @property
    def shader_name(self):
        return Path(self.shader_path).name

    @property
    def shader_stem(self):
        return Path(self.shader_path).stem

    def __repr__(self):
        params = "\n        ".join(str(p) for p in self.params)
        if params:
            params = f"[\n        {params}\n    ]"
        else:
            params = "[]"

        samplers = "\n        ".join(str(p) for p in self.samplers)
        if samplers:
            samplers = f"[\n        {samplers}\n    ]"
        else:
            samplers = "[]"

        return (
            f"MTD(\n"
            f"    dcx_type={self.dcx_type},\n"
            f"    path={self.path},\n"
            f"    shader_path={self.shader_path},\n"
            f"    description={self.description},\n"
            f"    params = {params},\n"
            f"    samplers = {samplers},\n"
            f")"
        )


class MTDParamType(StrEnum):
    """Referenced by NAME in MTDParam."""
    Bool = "bool"  # one-byte bool
    Int = "int"  # one four-byte integer
    Int2 = "int2"  # two four-byte integers
    Float = "float"  # one four-byte single float
    Float2 = "float2"  # two four-byte single floats
    Float3 = "float3"  # three four-byte single floats
    Float4 = "float4"  # four four-byte single floats

    def get_value_count(self) -> int:
        if self in {self.Bool, self.Int, self.Float}:
            return 1
        return int(self.value[-1])

    def get_block_type_marker(self) -> tuple[int, int]:
        if self == self.Bool:
            return 0x1000, 0xC0
        if self.value.startswith("int"):
            return 0x1001, 0xC5
        if self.value.startswith("float"):
            return 0x1002, 0xCa
        raise TypeError(f"Cannot get MTD block data type and marker of MTD param type: {self}")


@dataclass(slots=True)
class MTDParam:

    name: str
    param_type: MTDParamType
    value: bool | int | list[int] | float | list[float]

    def __init__(self, name: str, param_type: MTDParamType, value: bool | int | list[int] | float | list[float] = None):
        self.name = name
        self.param_type = param_type
        self.value = self.get_default_value(param_type) if value is None else self.validate_type(param_type, value)

    @staticmethod
    def get_default_value(param_type: MTDParamType):
        match param_type:
            case MTDParamType.Bool:
                return False
            case MTDParamType.Int:
                return 0
            case MTDParamType.Int2:
                return [0, 0]
            case MTDParamType.Float:
                return 0.0
            case MTDParamType.Float2:
                return [0.0, 0.0]
            case MTDParamType.Float3:
                return [0.0, 0.0, 0.0]
            case MTDParamType.Float4:
                return [0.0, 0.0, 0.0, 0.0]
            case _:
                raise TypeError(f"Invalid `param_type` for MTDParam: {param_type}")

    @staticmethod
    def validate_type(param_type: MTDParamType, value):
        """Check given `value` is appropriate for `param_type`."""
        match param_type:
            case MTDParamType.Bool:
                if not isinstance(value, bool):
                    raise TypeError(f"Value for Bool MTDParam must be a `bool`, not: {value}")
            case MTDParamType.Int:
                if not isinstance(value, int):
                    raise TypeError(f"Value for Int MTDParam must be an `int`, not: {value}")
            case MTDParamType.Int2:
                if not isinstance(value, (list, tuple)) or not len(value) == 2 or not all(
                    isinstance(x, int) for x in value
                ):
                    raise TypeError(f"Value for Int2 MTDParam must be a list of `int`, not: {value}")
                value = list(value)
            case MTDParamType.Float:
                if not isinstance(value, float):
                    raise TypeError(f"Value for Float MTDParam must be a `float`, not: {value}")
            case MTDParamType.Float2:
                if not isinstance(value, (list, tuple)) or not len(value) == 2 or not all(
                    isinstance(x, float) for x in value
                ):
                    raise TypeError(f"Value for Float2 MTDParam must be a list of `float`, not: {value}")
                value = list(value)
            case MTDParamType.Float3:
                if not isinstance(value, (list, tuple)) or not len(value) == 3 or not all(
                    isinstance(x, float) for x in value
                ):
                    raise TypeError(f"Value for Float3 MTDParam must be a list of `float`, not: {value}")
                value = list(value)
            case MTDParamType.Float4:
                if not isinstance(value, (list, tuple)) or not len(value) == 4 or not all(
                    isinstance(x, float) for x in value
                ):
                    raise TypeError(f"Value for Float4 MTDParam must be a list of `float`, not: {value}")
                value = list(value)
            case _:
                raise TypeError(f"Invalid `param_type` for MTDParam: {param_type}")
        return value

    @classmethod
    def from_mtd_reader(cls, reader: BinaryReader):

        assert_block(reader, 4, 4, 0xA3)  # param
        name = read_marked_string(reader, 0xA3)
        param_type = MTDParamType(read_marked_string(reader, 0x04))
        if (m := reader["i"]) != 1:
            raise ValueError(f"Expected 1 in MTDParam, not {m}.")

        assert_block(reader, version=1)
        reader.unpack("i")  # redundant with known type lengths

        match param_type:
            case MTDParamType.Bool:
                value = reader["?"]
            case MTDParamType.Int:
                value = reader["i"]
            case MTDParamType.Int2:
                value = list(reader.unpack("2i"))
            case MTDParamType.Float:
                value = reader["f"]
            case MTDParamType.Float2:
                value = list(reader.unpack("2f"))
            case MTDParamType.Float3:
                value = list(reader.unpack("3f"))
            case MTDParamType.Float4:
                value = list(reader.unpack("4f"))
            case _:
                raise ValueError(f"Cannot parse MTD param type: {param_type}")
        assert_marker(reader, 0x04)
        reader.assert_pad(4)
        return cls(name, param_type, value)

    def to_mtd_writer(self, mtd_writer: BinaryWriter):

        param_block, param_block_offset = write_block(mtd_writer, 4, 4, 0xA3)
        write_marked_string(mtd_writer, 0xA3, self.name)
        write_marked_string(mtd_writer, 0x04, self.param_type.value)  # lower case
        mtd_writer.pack("i", 1)

        data_type, marker = self.param_type.get_block_type_marker()
        value_block, value_block_offset = write_block(mtd_writer, data_type, 1, marker)

        value_count = self.param_type.get_value_count()
        mtd_writer.pack("i", value_count)

        match self.param_type:
            case MTDParamType.Bool:
                mtd_writer.pack("?", self.value)
            case MTDParamType.Int:
                mtd_writer.pack("i", self.value)
            case MTDParamType.Int2:
                mtd_writer.pack("2i", *self.value)
            case MTDParamType.Float:
                mtd_writer.pack("f", self.value)
            case MTDParamType.Float2:
                mtd_writer.pack("2f", *self.value)
            case MTDParamType.Float3:
                mtd_writer.pack("3f", *self.value)
            case MTDParamType.Float4:
                mtd_writer.pack("4f", *self.value)
            case _:
                raise ValueError(f"Cannot pack value for MTD param type: {self.param_type}")

        value_block.fill(mtd_writer, "length", mtd_writer.position - value_block_offset)
        write_marker(mtd_writer, 0x04)
        mtd_writer.pad(4)

        param_block.fill(mtd_writer, "length", mtd_writer.position - param_block_offset)

    def __repr__(self):
        return f"MTDParam(\"{self.name}\", {self.param_type.name}, value={self.value})"


@dataclass(slots=True)
class MTDSampler:

    sampler_type: str  # e.g. 'g_Diffuse' or 'g_Specular'
    extended: bool = False  # Sekiro only
    uv_index: int = 0  # FLVER vertex UV index used by shader
    shader_data_index: int = 0
    sampler_path: str = ""  # Sekiro only
    unk_floats: list[float] = field(default_factory=list)  # Sekiro only

    @classmethod
    def from_mtd_reader(cls, reader: BinaryReader):

        sampler_block = assert_block(reader, data_type=0x2000, marker=0xA3)
        if sampler_block.version == 3:
            extended = False
        elif sampler_block.version == 5:
            extended = True
        else:
            raise ValueError(f"`MTDSampler` block version should be 3 or 5, not {sampler_block.version}.")

        sampler_type = read_marked_string(reader, 0x35)
        uv_index = reader["i"]
        assert_marker(reader, 0x35)
        shader_data_index = reader["i"]

        if extended:
            if (m := reader["i"]) != 0xA3:
                raise ValueError(f"Expected integer 0xA3 in `MTDSampler` extended data, not {m}.")
            sampler_path = read_marked_string(reader, 0xBA)
            float_count = reader["i"]
            unk_floats = list(reader.unpack(f"{float_count}f"))
        else:
            sampler_path = ""
            unk_floats = []

        return cls(
            sampler_type,
            extended,
            uv_index,
            shader_data_index,
            sampler_path,
            unk_floats,
        )

    def to_mtd_writer(self, mtd_writer: BinaryWriter):
        sampler_block, sampler_block_offset = write_block(mtd_writer, 0x2000, 5 if self.extended else 3, 0xA3)

        write_marked_string(mtd_writer, 0x35, self.sampler_type)
        mtd_writer.pack("i", self.uv_index)
        write_marker(mtd_writer, 0x35)
        mtd_writer.pack("i", self.shader_data_index)

        if self.extended:
            mtd_writer.pack("i", 0xA3)
            write_marked_string(mtd_writer, 0xBA, self.sampler_path)
            float_count = len(self.unk_floats)
            mtd_writer.pack("i", float_count)
            mtd_writer.pack(f"{float_count}f", *self.unk_floats)
        # Otherwise, no more to write.

        sampler_block.fill(mtd_writer, "length", mtd_writer.position - sampler_block_offset)

    def __repr__(self):
        if self.extended:
            return (
                f"MTDSampler(\"{self.sampler_type}\", "
                f"uv_index={self.uv_index}, "
                f"shader_data_index={self.shader_data_index}, "
                f"sampler_path=\"{self.sampler_path}\", "
                f"unk_floats={self.unk_floats})"
            )
        return (
            f"MTDSampler(\"{self.sampler_type}\", "
            f"uv_index={self.uv_index}, "
            f"shader_data_index={self.shader_data_index})"
        )


class MTDBlendMode(IntEnum):
    Normal = 0
    TexEdge = 1
    Blend = 2
    Water = 3
    Add = 4
    Sub = 5
    Mul = 6
    AddMul = 7
    SubMul = 8
    WaterWave = 9
    LSNormal = 32
    LSTexEdge = 33
    LSBlend = 34
    LSWater = 35
    LSAdd = 36
    LSSub = 37
    LSMul = 38
    LSAddMul = 39
    LSSubMul = 40
    LSWaterWave = 41


class MTDLightingType(IntEnum):
    Null = 0
    HemDirDifSpcx3 = 1
    HemEnvDifSpc = 3


@dataclass(slots=True)
class MTDBlock(BinaryStruct):
    _pad0: bytes = field(init=False, **BinaryPad(4))
    length: uint
    data_type: int  # may extend beyond listed `MTDParamType` values
    version: int
    marker: byte
    # Always align to four afterward and ignore bytes.


def assert_block(reader: BinaryReader, data_type: int = None, version: int = None, marker: int = None):
    kwargs = {}
    if data_type is not None:
        kwargs["data_type"] = data_type
    if version is not None:
        kwargs["version"] = version
    if marker is not None:
        kwargs["marker"] = marker
    block = MTDBlock.from_bytes(reader)
    block.assert_field_values(**kwargs)
    reader.align(4)
    return block  # so non-asserted fields can be inspected


def write_block(writer: BinaryWriter, data_type: int, version: int, marker: int) -> tuple[MTDBlock, int]:
    block_offset = writer.position + 8
    block = MTDBlock(length=RESERVED, data_type=data_type, version=version, marker=marker)
    block.to_writer(writer)
    writer.pad_align(4)
    return block, block_offset


def assert_marker(reader: BinaryReader, marker: int):
    m = reader["B"]
    if m != marker:
        raise ValueError(f"MTD marker {hex(m)} does not match asserted marker {hex(marker)}.")
    reader.align(4)
    # No point returning anything, as everything is asserted.


def write_marker(writer: BinaryWriter, marker: int):
    writer.pack("B", marker)
    writer.pad_align(4)


def read_marked_string(reader: BinaryReader, asserted_marker: int) -> str:
    """String is NOT stripped."""
    length = reader["i"]
    string = reader.unpack_string(length=length, encoding="shift-jis", strip=False)
    assert_marker(reader, asserted_marker)
    return string


def write_marked_string(writer: BinaryWriter, marker: int, string: str):
    encoded = string.encode("shift-jis")
    writer.pack("i", len(encoded))
    writer.append(encoded)
    write_marker(writer, marker)


@dataclass(slots=True)
class MTDBND(Binder):
    """NOTE: This is NOT an abstract class. It can be used for any game (so far), but will lack `from_bundled()`."""

    mtds: dict[str, MTD] = field(default_factory=dict)

    def __post_init__(self):
        """Loads FIRST instance of each entry name as an MTD."""
        super(MTDBND, self).__post_init__()

        if self.mtds:
            return  # already passed in

        self.mtds = {}
        for entry in self.entries:
            if entry.name in self.mtds:
                continue  # ignore repeated names silently
            self.mtds[entry.name] = entry.to_binary_file(MTD)

    @classmethod
    def from_bundled(cls, game_or_name: Game | str) -> MTDBND:
        game = get_game(game_or_name)
        mtdbnd = None  # type: MTDBND | None
        for resource_key, resource_path in game.bundled_resource_paths.items():
            if resource_key.endswith("MTDBND"):
                if mtdbnd is None:
                    mtdbnd = cls.from_path(resource_path)
                else:
                    mtdbnd |= cls.from_path(resource_path)
        if mtdbnd is None:
            raise FileNotFoundError(f"No bundled MTDBND found for {game.name}.")
        return mtdbnd

    @classmethod
    def from_path_or_bundled(cls, game_or_name: Game | str, mtdbnd_path: Path):
        if mtdbnd_path.is_file():
            return cls.from_path(mtdbnd_path)
        return cls.from_bundled(game_or_name)
