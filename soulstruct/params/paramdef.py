from io import BytesIO
import os
from soulstruct.utilities.core import BinaryStruct, read_chars_from_bytes, PACKAGE_PATH
from soulstruct.bnd import BND3

# TODO: Pickle bundled ParamDef files.


class ParamDefBND(BND3):

    def __init__(self, paramdef_bnd_source=None):

        if paramdef_bnd_source is None:
            print("# WARNING: No ParamDef source was given, so Soulstruct will assume that you want the\n"
                  "# Dark Souls Remastered version. (Use paramdef_bnd_source='ptd' to get the PTD version.)")
            paramdef_bnd_source = 'dsr'

        if paramdef_bnd_source.lower() in {'ptd', 'dsr'}:
            # Use bundled (recommended).
            dcx = '.dcx' if paramdef_bnd_source.lower() == 'dsr' else ''
            paramdef_bnd_source = PACKAGE_PATH('params/resources/paramdef.paramdefbnd' + dcx)
            if not paramdef_bnd_source.is_file():
                raise FileNotFoundError(f"Could not find bundled ParamDef files in {paramdef_bnd_source}.\n"
                                        "Reinstall Soulstruct or copy the ParamDef files in yourself.")

        super().__init__(paramdef_bnd_source)
        self.paramdefs = {}

        # Simple check for remastered.
        if 'INTERROOT_x64' in self._entries[0].path:
            self.remastered = True
        elif 'INTERROOT_win32' in self._entries[0].path:
            self.remastered = False
        else:
            raise ValueError("Malformed BND path: could not detect DS version (PTD/DSR).")

        for param_name, param_base_name in PARAMDEF_BASE_NAMES.items():
            if not self.remastered and param_name in {
                    'LEVELSYNC_PARAM_ST', 'COOL_TIME_PARAM_ST', 'WHITE_COOL_TIME_PARAM_ST'}:
                continue
            self.paramdefs[param_name] = ParamDef(self.entries_by_basename[param_base_name + '.paramdef'])

    def __getitem__(self, param_name):
        try:
            return self.paramdefs[param_name]
        except KeyError:

            raise KeyError(f"There is no ParamDef with name '{param_name}'. The available names are:\n"
                           f"    {list(PARAMDEF_BASE_NAMES.keys())}")


class ParamDef(object):
    # No pack/write methods; these are essentially hard-coded structures, and therefore read-only.

    HEADER_STRUCT = BinaryStruct(
        ('size', 'i'),
        ('field_table_offset', 'H', 48),
        ('unk1', 'H'),
        ('field_count', 'H'),
        ('field_size', 'H', 176),
        ('param_name', '32j'),
        ('unk2', 'h'),
        ('relative_field_description_offset', 'h', 104),
    )

    FIELD_STRUCT = BinaryStruct(
        ('debug_name', '64j'),
        ('debug_type', '8j'),
        ('debug_format', '8j'),  # %i, %u, %d, etc.
        ('default', 'f'),
        ('minimum', 'f'),
        ('maximum', 'f'),
        ('increment', 'f'),
        ('debug_display', 'i'),
        ('size', 'i'),
        ('description_offset', 'i'),  # offset of null-terminated string (unlimited length)
        ('internal_type', '32j'),  # could be an enum name (see params.enums)
        ('name', '32j'),
        ('id', 'i'),  # TODO: what is this?
    )

    def __init__(self, paramdef_source, param_name=None):

        self.param_name = None
        self.fields = []
        self.fields_by_name = {}

        if isinstance(paramdef_source, list):
            if param_name is None:
                raise ValueError("`param_name` must be given to ParamDef if a list of fields is passed.")
            self.param_name = param_name
            self.fields = paramdef_source

        elif isinstance(paramdef_source, bytes):
            self.unpack(BytesIO(paramdef_source))

        elif isinstance(paramdef_source, str):
            if paramdef_source in PARAMDEF_BASE_NAMES:
                paramdef_source = PARAMDEF_BASE_NAMES[paramdef_source] + '.paramdef'
            self.paramdef_path = paramdef_source
            with open(paramdef_source, 'rb') as file:
                self.unpack(file)

        elif hasattr(paramdef_source, 'data'):
            # Try reading .data attribute (e.g. BNDEntry).
            self.unpack(BytesIO(paramdef_source.data))

    def unpack(self, paramdef_buffer):
        """Convert a paramdef file to a dictionary, indexed by ID."""
        header = self.HEADER_STRUCT.unpack(paramdef_buffer)
        self.param_name = header.param_name
        fields = self.FIELD_STRUCT.unpack(paramdef_buffer, count=header.field_count)
        description_table_offset = paramdef_buffer.tell()
        packed_desc_data = paramdef_buffer.read()

        for field_index, field in enumerate(fields):
            if field.description_offset != 0:
                fdo = field.description_offset - description_table_offset
                field.description = read_chars_from_bytes(packed_desc_data, offset=fdo, encoding='shift_jis_2004')
            else:
                field.description = ''

            # print(f"{self.param_name} {field_index} | {field.internal_type} | {field.debug_type} | {field.name} | "
            #       f"{field.debug_name} | {field.description}")

            is_bits = field.name.find(': ')
            if is_bits == -1:
                is_bits = field.name.find(':')
            if is_bits != -1:
                try:
                    bit_size = int(field.name[is_bits + 1])
                except ValueError:
                    bit_size = int(field.name[is_bits + 2])
            elif field.internal_type == 'dummy8':
                is_pad = field.name.find('[')
                if is_pad != -1:
                    bit_size = int(field.name[is_pad + 1]) * 8
                else:
                    bit_size = 8
            else:
                bit_size = field.size * 8

            field.index = field_index
            field.bit_size = bit_size

            self.fields.append(field)
            if self.fields_by_name is not None:
                if field.name in self.fields_by_name:
                    print(f"# WARNING: ParamDef field with name '{field.name}' was unpacked more than once,\n"
                          f"so you will not be able to access fields by name. (Should NOT happen in any known files!)")
                else:
                    self.fields_by_name[field.name] = field

    def __getitem__(self, field_name):
        if self.fields_by_name is None:
            return AttributeError("Cannot access ParamDef fields by name due to one or more repeated field name.\n"
                                  "This should NOT happen unless you've edited the ParamDef for some ungodly reason.")
        return self.fields_by_name[field_name]

    def __repr__(self):
        return f"ParamDef {self.param_name}:\n  " + "\n  ".join(
            [f"{field.index} | {field.debug_name} | {field.description}" for field in self.fields])


# Maps internal header names of ParamTables to their BND entry path base names. DO NOT EDIT THESE!
PARAMDEF_BASE_NAMES = {
    # DrawParam
    'FOG_BANK': 'FogBank',
    'LIGHT_BANK': 'LightBank',
    'LIGHT_SCATTERING_BANK': 'LightScatteringBank',
    'POINT_LIGHT_BANK': 'PointLightBank',
    'LENS_FLARE_BANK': 'LensFlareBank',
    'LENS_FLARE_EX_BANK': 'LensFlareExBank',
    'DOF_BANK': 'DofBank',
    'TONE_MAP_BANK': 'ToneMapBank',
    'TONE_CORRECT_BANK': 'ToneCorrectBank',
    'SHADOW_BANK': 'ShadowBank',
    'LENS_FLAG_EX_BANK': 'LensFlareExBank',
    'ENV_LIGHT_TEX_BANK': 'EnvLightTexBank',
    'LOD_BANK': 'LodBank',

    # GameParam
    'ATK_PARAM_ST': 'AtkParam',
    'BEHAVIOR_PARAM_ST': 'BehaviorParam',
    'BULLET_PARAM_ST': 'BulletParam',
    'CHARACTER_INIT_PARAM': 'CharaInitParam',
    'EQUIP_MTRL_SET_PARAM_ST': 'EquipMtrlSetParam',
    'EQUIP_PARAM_ACCESSORY_ST': 'EquipParamAccessory',
    'EQUIP_PARAM_GOODS_ST': 'EquipParamGoods',
    'EQUIP_PARAM_PROTECTOR_ST': 'EquipParamProtector',
    'EQUIP_PARAM_WEAPON_ST': 'EquipParamWeapon',
    'FACE_PARAM_ST': 'FaceGenParam',
    'GAME_AREA_PARAM_ST': 'GameAreaParam',
    'HIT_MTRL_PARAM_ST': 'HitMtrlParam',
    'ITEMLOT_PARAM_ST': 'ItemLotParam',
    'KNOCKBACK_PARAM_ST': 'KnockBackParam',
    'LOCK_CAM_PARAM_ST': 'LockCamParam',
    'MAGIC_PARAM_ST': 'MagicParam',
    'MENU_PARAM_COLOR_TABLE_ST': 'MenuParamColorTable',
    'MOVE_PARAM_ST': 'MoveParam',
    'NPC_PARAM_ST': 'NpcParam',
    'NPC_THINK_PARAM_ST': 'NpcThinkParam',
    'OBJ_ACT_PARAM_ST': 'ObjActParam',
    'OBJECT_PARAM_ST': 'ObjectParam',
    'REINFORCE_PARAM_PROTECTOR_ST': 'ReinforceParamProtector',
    'REINFORCE_PARAM_WEAPON_ST': 'ReinforceParamWeapon',
    'SHOP_LINEUP_PARAM': 'ShopLineupParam',
    'SKELETON_PARAM_ST': 'SkeletonParam',
    'SP_EFFECT_PARAM_ST': 'SpEffect',
    'SP_EFFECT_VFX_PARAM_ST': 'SpEffectVfx',
    'TALK_PARAM_ST': 'TalkParam',
    'THROW_INFO_BANK': 'ThrowParam',

    # DSR-only multiplayer params.
    'LEVELSYNC_PARAM_ST': 'LevelSyncParam',
    'COOL_TIME_PARAM_ST': 'CoolTimeParam',
    'WHITE_COOL_TIME_PARAM_ST': 'WhiteCoolTimeParam',

    # Junk resources that only contain Demon's Souls remnants.
    'AI_STANDARD_INFO_BANK': 'AiStandardInfo',
    'CACL_CORRECT_GRAPH_ST': 'CalcCorrectGraph',  # (sic)
    'ENEMY_STANDARD_INFO_BANK': 'EnemyStandardInfo',
    'RAGDOLL_PARAM_ST': 'RagdollParam',
    'QWC_CHANGE_PARAM_ST': 'QwcChangeParam',
    'QWC_JUDGE_PARAM_ST': 'QwcJudgeParam',
}
