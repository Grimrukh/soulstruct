from __future__ import annotations

__all__ = [
    "MTD",
    "MTDParam",
    "MTDInfo",
]

import re
import typing as tp
from pathlib import Path

from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *
from soulstruct.utilities.future import StrEnum

try:
    Self = tp.Self
except AttributeError:
    Self = "MTD"


@dataclass(slots=True)
class MTD(GameFile):

    shader_path: str
    description: str
    params: list[MTDParam] = field(default_factory=list)
    textures: list[MTDTexture] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
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

        texture_count = reader["i"]
        mtd_textures = [MTDTexture.from_mtd_reader(reader) for _ in range(texture_count)]

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
            mtd_textures,
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
        writer.pack("i", len(self.textures))
        for texture in self.textures:
            texture.to_mtd_writer(writer)
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

    def has_texture_type(self, mtd_texture_type: str) -> bool:
        for texture in self.textures:
            if texture.texture_type == mtd_texture_type:
                return True
        return False

    def get_texture_type_uv_index(self, mtd_texture_type: str) -> int:
        for texture in self.textures:
            if texture.texture_type == mtd_texture_type:
                return texture.uv_index
        raise KeyError(f"MTD texture type '{mtd_texture_type}' not found in MTD from path '{self.path}'.")

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

        textures = "\n        ".join(str(p) for p in self.textures)
        if textures:
            textures = f"[\n        {textures}\n    ]"
        else:
            textures = "[]"

        return (
            f"MTD(\n"
            f"    dcx_type={self.dcx_type},\n"
            f"    path={self.path},\n"
            f"    shader_path={self.shader_path},\n"
            f"    description={self.description},\n"
            f"    params = {params},\n"
            f"    textures = {textures},\n"
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
class MTDTexture:

    texture_type: str  # e.g. 'g_Diffuse' or 'g_Specular'
    extended: bool = False  # Sekiro only
    uv_index: int = 0  # FLVER vertex UV index used by shader
    shader_data_index: int = 0
    texture_path: str = ""  # Sekiro only
    unk_floats: list[float] = field(default_factory=list)  # Sekiro only

    @classmethod
    def from_mtd_reader(cls, reader: BinaryReader):

        texture_block = assert_block(reader, data_type=0x2000, marker=0xA3)
        if texture_block.version == 3:
            extended = False
        elif texture_block.version == 5:
            extended = True
        else:
            raise ValueError(f"MTD Texture block version should be 3 or 5, not {texture_block.version}.")

        texture_type = read_marked_string(reader, 0x35)
        uv_index = reader["i"]
        assert_marker(reader, 0x35)
        shader_data_index = reader["i"]

        if extended:
            if (m := reader["i"]) != 0xA3:
                raise ValueError(f"Expected integer 0xA3 in MTD texture extended data, not {m}.")
            texture_path = read_marked_string(reader, 0xBA)
            float_count = reader["i"]
            unk_floats = list(reader.unpack(f"{float_count}f"))
        else:
            texture_path = ""
            unk_floats = []

        return cls(
            texture_type,
            extended,
            uv_index,
            shader_data_index,
            texture_path,
            unk_floats,
        )

    def to_mtd_writer(self, mtd_writer: BinaryWriter):
        texture_block, texture_block_offset = write_block(mtd_writer, 0x2000, 5 if self.extended else 3, 0xA3)

        write_marked_string(mtd_writer, 0x35, self.texture_type)
        mtd_writer.pack("i", self.uv_index)
        write_marker(mtd_writer, 0x35)
        mtd_writer.pack("i", self.shader_data_index)

        if self.extended:
            mtd_writer.pack("i", 0xA3)
            write_marked_string(mtd_writer, 0xBA, self.texture_path)
            float_count = len(self.unk_floats)
            mtd_writer.pack("i", float_count)
            mtd_writer.pack(f"{float_count}f", *self.unk_floats)
        # Otherwise, no more to write.

        texture_block.fill(mtd_writer, "length", mtd_writer.position - texture_block_offset)

    def __repr__(self):
        if self.extended:
            return (
                f"MTDTexture(\"{self.texture_type}\", "
                f"uv_index={self.uv_index}, "
                f"shader_data_index={self.shader_data_index}, "
                f"texture_path=\"{self.texture_path}\", "
                f"unk_floats={self.unk_floats})"
            )
        return (
            f"MTDTexture(\"{self.texture_type}\", "
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
class MTDInfo:
    """Various booleans that indicate required textures for a specific MTD shader."""

    MTD_DSBH_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(D)?(S)?(B)?(H)?\].*")  # TODO: support 'T' (translucency)
    MTD_M_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(M|ML|LM)\].*")
    MTD_L_RE: tp.ClassVar[re.Pattern] = re.compile(r".*\[(L|ML|LM)\].*")
    # Checked separately: [Dn] (g_Diffuse only), [We] (g_Bumpmap only)

    # TODO: Hardcoding a set of 'foliage' shader prefixes I've encountered in DSR.
    MTD_FOLIAGE_PREFIXES: tp.ClassVar[set[str]] = {
        "M_2Foliage",
        "M_3Ivy",
    }

    # All MTD stems in DSR that use a 'FRPG_Water*' SPX shader but don't have [We] in their name.
    WATER_STEMS: tp.ClassVar[set[str]] = {
        "M_5Water[B]",  # FRPG_Water_Reflect
        "A10_00_Water_drainage",  # FRPG_Water_Reflect
        "A10_01_Water[B]",  # FRPG_Water_Reflect
        "A11_Water[W]",  # FRPG_Water_Reflect
        "A12_Little River",  # FRPG_Water_Reflect
        "A12_River",  # FRPG_Water_Reflect
        "A12_River_No reflect",  # FRPG_Water_Reflect
        "A12_Water",  # FRPG_Water_Reflect
        "A12_Water_lake",  # FRPG_Water_Reflect
        "A14Water[B]",  # FRPG_Water_Reflect
        "S[DB]_Alp_water",  # FRPG_WaterWaveSfx
        "A12_DarkRiver",  # FRPG_Water_Reflect
        "A12_DarkWater",  # FRPG_Water_Reflect
        "A12_NewWater",  # FRPG_Water_Reflect
        "A12_Water_boss",  # FRPG_Water_Reflect
    }

    SNOW_STEMS: tp.ClassVar[set[str]] = {
        "M_8Snow",  # FRPG_Snow
        "A10_slime[D][L]",  # FRPG_Snow_Lit
        "A11_Snow",  # FRPG_Snow
        "A11_Snow[L]",  # FRPG_Snow_Lit
        "A11_Snow_stair",  # FRPG_Snow
        "A11_Snow_stair[L]",  # FRPG_Snow_Lit
        "A14_numa",  # FRPG_Snow (Blighttown swamp)
        "A14_numa2",  # FRPG_Snow (Blighttown swamp)
        "A15_Tar",  # FRPG_Snow
        "A18_ash",  # FRPG_Snow
        "A19_Snow",  # FRPG_Snow
        "A19_Snow[L]",  # FRPG_Snow_Lit
    }

    # Subset of `SNOW_STEMS` that use a 'FRPG_Snow*' SPX shader and also have a 'g_SnowMetalMask' param and an extra
    # 'g_Bumpmap_3' texture type.
    SNOW_METAL_MASK_STEMS: tp.ClassVar[set[str]] = {
        "A10_slime[D][L]",  # FRPG_Snow_Lit
        "A11_Snow",  # FRPG_Snow
        "A11_Snow[L]",  # FRPG_Snow_Lit
        "A11_Snow_stair",  # FRPG_Snow
        "A11_Snow_stair[L]",  # FRPG_Snow_Lit
        "A14_numa",  # FRPG_Snow (Blighttown swamp)
        "A14_numa2",  # FRPG_Snow (Blighttown swamp)
        "A15_Tar",  # FRPG_Snow
        "A19_Snow",  # FRPG_Snow
        "A19_Snow[L]",  # FRPG_Snow_Lit
    }

    NO_TANGENT_STEMS: tp.ClassVar[set[str]] = {
        "M_Tree[D]_Edge",
    }

    HAS_BITANGENT_STEMS: tp.ClassVar[set[str]] = {
        "A10_02_m9000_M[D]",
    }

    # Ordered dict mapping texture type names like 'g_Diffuse' to their FLVER vertex UV index/Blender layer (1-indexed).
    texture_types: dict[str, int] = field(default_factory=dict)
    # TODO: Some shaders simply don't use the always-empty 'g_DetailBumpmap', but I can find no reliable way to detect
    #  this from their MTD names alone. I may have to guess that they do unless the MTD file is provided.

    alpha: bool = False
    edge: bool = False
    spec: bool = False
    detb: bool = False  # I don't think these shaders are used in DS1. Also `g_EnvSpcSlotNo = 2`...
    is_water: bool = False
    is_foliage: bool = False  # has 'g_Wind*' params and two extra UV slots for wind animation control
    is_snow: bool = False  # has 'g_SnowColor', 'g_SnowHeight', and other 'g_Snow*' params
    has_snow_roughness: bool = False  # has 'g_Bumpmap_3' texture and 'g_Snow[Roughness/MetalMask/DiffuseF0]' params
    has_tangent: bool = True  # False for unshaded FLVERs like skybox textures and some trees
    has_bitangent: bool | None = None  # if `None`, bitangents

    @classmethod
    def from_mtd(cls, mtd: MTD):
        mtd_info = cls()

        for texture in mtd.textures:
            # NOTE: Each MTD may not use certain UV indices -- e.g. 'g_Lightmap' always uses 3, even if there is no
            # second texture slot to use UV index 2. This is obviously desirable to keep the same UV layouts together
            # and we do the same in Blender.
            mtd_info.texture_types[texture.texture_type] = texture.uv_index  # 1-indexed!

        blend_mode = mtd.get_param("g_BlendMode", default=0)
        if blend_mode == 1:
            mtd_info.edge = True
        elif blend_mode == 2:
            mtd_info.alpha = True

        env_spc_slot_no = mtd.get_param("g_EnvSpcSlotNo", default=0)
        if env_spc_slot_no == 1:
            mtd_info.spec = True

        detail_bump_power = mtd.get_param("g_DetailBump_BumpPower", default=0.0)
        if detail_bump_power > 0.0:
            mtd_info.detb = True

        lighting_type = mtd.get_param("g_LightingType", default=1)
        if lighting_type == 0:  # e.g. unshaded skybox
            mtd_info.has_tangent = False
            mtd_info.has_bitangent = False

        mtd_info.is_water = mtd.shader_stem.startswith("FRPG_Water")
        mtd_info.is_foliage = mtd.has_param("g_IsFoliage")
        mtd_info.is_snow = mtd.shader_stem.startswith("FRPG_Snow")
        mtd_info.has_snow_roughness = mtd.has_param("g_SnowRoughness")  # only present in some Snow shaders

        return mtd_info

    @classmethod
    def from_mtd_name(cls, mtd_name):
        """Guess as much information about the shader as possible purely from its name.

        Obviously, getting the texture names right is the most important part, but we can also guess whether the shader
        uses a lightmap (L), two texture slots (M), or has extra features like alpha (Alp/Edge).
        """
        mtd_info = cls()
        mtd_stem = Path(mtd_name).stem

        if dsbh_match := cls.MTD_DSBH_RE.match(mtd_stem):
            if dsbh_match.group(1):
                mtd_info.texture_types["g_Diffuse"] = 1
            if dsbh_match.group(2):
                mtd_info.texture_types["g_Specular"] = 1
            if dsbh_match.group(3):
                mtd_info.texture_types["g_Bumpmap"] = 1
            if dsbh_match.group(4):
                mtd_info.texture_types["g_Height"] = 1
        elif "[Dn]" in mtd_stem:  # e.g. unshaded skybox
            mtd_info.texture_types["g_Diffuse"] = 1
            mtd_info.has_tangent = False
            mtd_info.has_bitangent = False
        elif "[We]" in mtd_stem or mtd_stem in cls.WATER_STEMS:
            mtd_info.texture_types["g_Bumpmap"] = 1
            mtd_info.is_water = True
        else:
            print(f"# ERROR: Shader name '{mtd_name}' could not be parsed for its textures.")

        # TODO: A few [D] shaders also don't use tangents...
        if mtd_stem in cls.NO_TANGENT_STEMS:
            mtd_info.has_tangent = False
            mtd_info.has_bitangent = False

        if cls.MTD_M_RE.match(mtd_stem):
            for texture_type, _ in mtd_info.texture_types:
                mtd_info.texture_types[texture_type + "_2"] = 2

        if cls.MTD_L_RE.match(mtd_stem):
            mtd_info.texture_types["g_Lightmap"] = 3  # even if there is no second texture slot

        # Has two extra UV slots.
        mtd_info.is_foliage = any(mtd_name.startswith(prefix) for prefix in cls.MTD_FOLIAGE_PREFIXES)
        mtd_info.is_snow = mtd_stem in cls.SNOW_STEMS
        # Has an extra 'g_Bumpmap_3' texture type.
        mtd_info.has_snow_roughness = mtd_stem in cls.SNOW_METAL_MASK_STEMS

        mtd_info.alpha = "_Alp" in mtd_name
        mtd_info.edge = "_Edge" in mtd_name
        mtd_info.spec = "_Spec" in mtd_name
        mtd_info.detb = "_DetB" in mtd_name

        if "g_Bumpmap" in mtd_info.texture_types:
            # Add useless 'g_DetailBumpmap' for completion.
            # TODO: Some shaders, even with 'g_Bumpmap', do not have this. I have no way to detect from the name.
            #  Currently assuming that it doesn't matter at all if FLVERs have an (empty) texture definition for it.
            mtd_info.texture_types["g_DetailBumpmap"] = 1  # always

        return mtd_info

    def get_uv_layer_names(self) -> list[str]:
        """Determine Blender UV layer names, which should correspond with the length of each vertex UV list."""
        uv_layer_names = []
        sorted_texture_types = sorted(self.texture_types.items(), key=lambda x: x[1])  # sort by UV index (value)
        for texture_type, uv_index in sorted_texture_types:
            name = f"UVMap{uv_index}"
            if name not in uv_layer_names:
                uv_layer_names.append(name)
        if self.is_foliage:
            uv_layer_names.extend(["UVMapWindA", "UVMapWindB"])
        return uv_layer_names

    @property
    def has_two_slots(self):
        return any(texture_type.endswith("_2") for texture_type in self.texture_types)

    @property
    def has_bumpmap_3(self):
        """Snow shaders with roughness have this (and no other shaders in DSR at least)."""
        return "g_Bumpmap_3" in self.texture_types

    @property
    def has_lightmap(self):
        return "g_Lightmap" in self.texture_types

    @property
    def has_detail_bumpmap(self):
        return "g_DetailBumpmap" in self.texture_types
