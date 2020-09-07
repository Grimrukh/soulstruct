from __future__ import annotations

__all__ = ["ParamDefBND", "ParamDefField", "ParamDef", "PARAMDEF_BASE_NAMES"]

import io
import logging
import typing as tp
from pathlib import Path

from soulstruct.bnd import BND3, BNDEntry
from soulstruct.params.display_info import get_param_info, get_param_info_field
from soulstruct.utilities.core import BinaryStruct, read_chars_from_bytes, PACKAGE_PATH

if tp.TYPE_CHECKING:
    from soulstruct.params.core import ParamEntry
    from soulstruct.params.display_info.base import FieldDisplayInfo

_LOGGER = logging.getLogger(__name__)


class ParamDefBND(BND3):
    def __init__(self, paramdef_bnd_source=None):

        if paramdef_bnd_source is None:
            _LOGGER.warning(
                "No ParamDef source was given, so Soulstruct will assume that you want the Dark Souls Remastered "
                "version. (Use `paramdef_bnd_source='ptde'` to get the PTDE version.)"
            )
            paramdef_bnd_source = "dsr"

        if paramdef_bnd_source.lower() in {"ptde", "dsr"}:
            # Use bundled (recommended).
            dcx = ".dcx" if paramdef_bnd_source.lower() == "dsr" else ""
            paramdef_bnd_source = PACKAGE_PATH("params/resources/paramdef.paramdefbnd" + dcx)
            if not paramdef_bnd_source.is_file():
                raise FileNotFoundError(
                    f"Could not find bundled ParamDef files in {paramdef_bnd_source}.\n"
                    "Reinstall Soulstruct or copy the ParamDef files in yourself."
                )

        super().__init__(paramdef_bnd_source)
        self.paramdefs = {}

        # Simple check for Remastered.
        if "INTERROOT_x64" in self._entries[0].path:
            self.remastered = True
        elif "INTERROOT_win32" in self._entries[0].path:
            self.remastered = False
        else:
            raise ValueError("Malformed BND path: could not detect DS version (PTD/DSR).")

        for param_name, param_base_name in PARAMDEF_BASE_NAMES.items():
            if not self.remastered and param_name in {
                "LEVELSYNC_PARAM_ST",
                "COOL_TIME_PARAM_ST",
                "WHITE_COOL_TIME_PARAM_ST",
            }:
                continue
            self.paramdefs[param_name] = ParamDef(self.entries_by_basename[param_base_name + ".paramdef"])

    def __getitem__(self, param_name) -> ParamDef:
        try:
            return self.paramdefs[param_name]
        except KeyError:

            raise KeyError(
                f"There is no ParamDef with name '{param_name}'. The available names are:\n"
                f"    {list(PARAMDEF_BASE_NAMES.keys())}"
            )


class ParamDefField:
    """Information about a single field in a ParamTable."""

    FIELD_STRUCT = BinaryStruct(
        ("debug_name", "64j"),
        ("debug_type", "8j"),
        ("debug_format", "8j"),  # %i, %u, %d, etc.
        ("default", "f"),
        ("minimum", "f"),
        ("maximum", "f"),
        ("increment", "f"),
        ("debug_display", "i"),
        ("size", "i"),
        ("description_offset", "i"),  # offset of null-terminated string (unlimited length)
        ("internal_type", "32j"),  # could be an enum name (see params.enums)
        ("name", "32j"),
        ("id", "i"),  # TODO: what is this?
    )

    def __init__(self, field_struct: dict, index: int, description: str, field_info: FieldDisplayInfo = None):
        self.field_index = index
        self.name = field_struct["name"]
        self.description = description
        self.size = field_struct["size"]
        self.internal_type = field_struct["internal_type"]
        self._display_info = field_info

        self.debug_name = field_struct["debug_name"]
        self.debug_type = field_struct["debug_type"]
        self.debug_format = field_struct["debug_format"]

        self.default = field_struct["default"]
        self.minimum = field_struct["minimum"]
        self.maximum = field_struct["maximum"]
        self.increment = field_struct["increment"]

        self.debug_display = field_struct["debug_display"]
        self.field_id = field_struct["id"]

        self.bit_size = self.get_bit_size(self.name, self.internal_type, self.size)

    def get_display_info(self, entry: ParamEntry):
        if not self._display_info:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return self._display_info(entry)

    @classmethod
    def unpack_fields(cls, param_name: str, paramdef_buffer: io.BytesIO, field_count: int):
        """Buffer should be at the start of the packed fields (which are followed by the packed descriptions)."""
        fields = []
        field_structs = cls.FIELD_STRUCT.unpack_count(paramdef_buffer, count=field_count)
        description_table_offset = paramdef_buffer.tell()
        packed_desc_data = paramdef_buffer.read()
        for field_index, field_struct in enumerate(field_structs):
            if field_struct["description_offset"] != 0:
                field_description = read_chars_from_bytes(
                    packed_desc_data,
                    offset=field_struct["description_offset"] - description_table_offset,
                    encoding="shift_jis_2004",
                )
            else:
                field_description = ""
            try:
                field_info = get_param_info_field(param_name, field_struct["name"])
            except KeyError:
                # No information given for this field.
                field_info = None
            fields.append(cls(field_struct, field_index, field_description, field_info))
        return fields

    @staticmethod
    def get_bit_size(name, internal_type, size):
        is_bits = name.find(": ")
        if is_bits == -1:
            is_bits = name.find(":")
        if is_bits != -1:
            try:
                return int(name[is_bits + 1])
            except ValueError:
                return int(name[is_bits + 2])
        elif internal_type == "dummy8":
            is_pad = name.find("[")
            if is_pad != -1:
                return int(name[is_pad + 1]) * 8
            else:
                return 8
        else:
            return size * 8


class ParamDef:
    # No pack/write methods; these are essentially hard-coded structures, and therefore read-only.

    HEADER_STRUCT = BinaryStruct(
        ("size", "i"),
        ("field_table_offset", "H", 48),
        ("unk1", "H"),
        ("field_count", "H"),
        ("field_size", "H", 176),
        ("param_name", "32j"),
        ("unk2", "h"),
        ("relative_field_description_offset", "h", 104),
    )

    def __init__(self, paramdef_source, param_name=None):

        self.param_name = None
        self.paramdef_path = None
        self.fields = []
        self.param_info = {}

        if isinstance(paramdef_source, list):
            if param_name is None:
                raise ValueError("`param_name` must be given to `ParamDef` constructor if a list of fields is passed.")
            self.param_name = param_name
            self.fields = paramdef_source

        elif isinstance(paramdef_source, bytes):
            self.unpack(io.BytesIO(paramdef_source))

        elif isinstance(paramdef_source, str):
            if paramdef_source in PARAMDEF_BASE_NAMES:
                paramdef_source = PARAMDEF_BASE_NAMES[paramdef_source] + ".paramdef"
            self.paramdef_path = Path(paramdef_source)
            with self.paramdef_path.open("rb") as file:
                self.unpack(file)

        elif isinstance(paramdef_source, BNDEntry):
            self.unpack(io.BytesIO(paramdef_source.data))

        else:
            raise TypeError(f"Invalid `paramdef_source` type: {type(paramdef_source)}")

        try:
            self.param_info = get_param_info(self.param_name)
        except KeyError:
            # This param has no extra information.
            self.param_info = None

    def unpack(self, paramdef_buffer):
        """Convert a paramdef file to a dictionary, indexed by ID."""
        header = self.HEADER_STRUCT.unpack(paramdef_buffer)
        self.param_name = header["param_name"]
        self.fields = ParamDefField.unpack_fields(self.param_name, paramdef_buffer, header["field_count"])

    def __getitem__(self, field_name) -> ParamDefField:
        hits = [field for field in self.fields if field.name == field_name]
        if len(hits) >= 2:
            raise AttributeError(
                f"Field {field_name} appears more than once in ParamDef.\n"
                "This should NOT happen unless you've edited the ParamDef for some ungodly reason."
            )
        elif not hits:
            raise AttributeError(f"Field {field_name} does not exist in ParamDef.")
        return hits[0]

    def __repr__(self):
        return f"ParamDef {self.param_name}:\n  " + "\n  ".join(
            [f"{field.index} | {field.debug_name} | {field.description}" for field in self.fields]
        )


# Maps internal header names of ParamTables to their BND entry path base names. DO NOT EDIT THESE!
PARAMDEF_BASE_NAMES = {
    # DrawParam
    "FOG_BANK": "FogBank",
    "LIGHT_BANK": "LightBank",
    "LIGHT_SCATTERING_BANK": "LightScatteringBank",
    "POINT_LIGHT_BANK": "PointLightBank",
    "LENS_FLARE_BANK": "LensFlareBank",
    "LENS_FLARE_EX_BANK": "LensFlareExBank",
    "DOF_BANK": "DofBank",
    "TONE_MAP_BANK": "ToneMapBank",
    "TONE_CORRECT_BANK": "ToneCorrectBank",
    "SHADOW_BANK": "ShadowBank",
    "LENS_FLAG_EX_BANK": "LensFlareExBank",
    "ENV_LIGHT_TEX_BANK": "EnvLightTexBank",
    "LOD_BANK": "LodBank",
    # GameParam
    "ATK_PARAM_ST": "AtkParam",
    "BEHAVIOR_PARAM_ST": "BehaviorParam",
    "BULLET_PARAM_ST": "BulletParam",
    "CHARACTER_INIT_PARAM": "CharaInitParam",
    "EQUIP_MTRL_SET_PARAM_ST": "EquipMtrlSetParam",
    "EQUIP_PARAM_ACCESSORY_ST": "EquipParamAccessory",
    "EQUIP_PARAM_GOODS_ST": "EquipParamGoods",
    "EQUIP_PARAM_PROTECTOR_ST": "EquipParamProtector",
    "EQUIP_PARAM_WEAPON_ST": "EquipParamWeapon",
    "FACE_PARAM_ST": "FaceGenParam",
    "GAME_AREA_PARAM_ST": "GameAreaParam",
    "HIT_MTRL_PARAM_ST": "HitMtrlParam",
    "ITEMLOT_PARAM_ST": "ItemLotParam",
    "KNOCKBACK_PARAM_ST": "KnockBackParam",
    "LOCK_CAM_PARAM_ST": "LockCamParam",
    "MAGIC_PARAM_ST": "MagicParam",
    "MENU_PARAM_COLOR_TABLE_ST": "MenuParamColorTable",
    "MOVE_PARAM_ST": "MoveParam",
    "NPC_PARAM_ST": "NpcParam",
    "NPC_THINK_PARAM_ST": "NpcThinkParam",
    "OBJ_ACT_PARAM_ST": "ObjActParam",
    "OBJECT_PARAM_ST": "ObjectParam",
    "REINFORCE_PARAM_PROTECTOR_ST": "ReinforceParamProtector",
    "REINFORCE_PARAM_WEAPON_ST": "ReinforceParamWeapon",
    "SHOP_LINEUP_PARAM": "ShopLineupParam",
    "SKELETON_PARAM_ST": "SkeletonParam",
    "SP_EFFECT_PARAM_ST": "SpEffect",
    "SP_EFFECT_VFX_PARAM_ST": "SpEffectVfx",
    "TALK_PARAM_ST": "TalkParam",
    "THROW_INFO_BANK": "ThrowParam",
    # DSR-only multiplayer params.
    "LEVELSYNC_PARAM_ST": "LevelSyncParam",
    "COOL_TIME_PARAM_ST": "CoolTimeParam",
    "WHITE_COOL_TIME_PARAM_ST": "WhiteCoolTimeParam",
    # Junk resources that only contain Demon's Souls remnants.
    "AI_STANDARD_INFO_BANK": "AiStandardInfo",
    "CACL_CORRECT_GRAPH_ST": "CalcCorrectGraph",  # note type in internal name
    "ENEMY_STANDARD_INFO_BANK": "EnemyStandardInfo",
    "RAGDOLL_PARAM_ST": "RagdollParam",
    "QWC_CHANGE_PARAM_ST": "QwcChangeParam",
    "QWC_JUDGE_PARAM_ST": "QwcJudgeParam",
}
