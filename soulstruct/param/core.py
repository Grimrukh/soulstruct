# TODO: GameParam BND indices of param tables are different in PTD/DSR. I'm guessing it may not actually matter, and
#   that all the param tables are loaded and accessed by their names (e.g. 'OBJ_ACT_PARAM_ST').

# TODO: Intelligent tools that change multiple relevant params at once.

from collections import OrderedDict
from io import BytesIO
import struct
from typing import Dict
from soulstruct.core import BinaryStruct, read_chars_from_bytes
from soulstruct.param.paramdef import ParamDefBND

_PARAMDEF_PTD = None
_PARAMDEF_DSR = None


def PARAMDEF_BND(game_version):
    global _PARAMDEF_PTD, _PARAMDEF_DSR
    if game_version.lower() == 'ptd':
        if _PARAMDEF_PTD is None:
            _PARAMDEF_PTD = ParamDefBND('ptd')
        return _PARAMDEF_PTD
    elif game_version.lower() == 'dsr':
        if _PARAMDEF_DSR is None:
            _PARAMDEF_DSR = ParamDefBND('dsr')
        return _PARAMDEF_DSR
    raise ValueError(f"Could not find bundled ParamDef for game version {repr(game_version)}.")


PARAM_TYPE_INFO = {
    # (struct_type, python_type, min_value, max_value)
    'u32': ('<I', int, 0, 2**32 - 1),
    's32': ('<i', int, -2**31, 2**31 - 1),
    'f32': ('<f', float, -float('inf'), float('inf')),
    'u16': ('<H', int, 0, 2**16 - 1),
    's16': ('<h', int, -2**15, 2**15 - 1),
    'u8': ('<B', int, 0, 2**8 - 1),
    's8': ('<b', int, -2**7, 2**7 - 1),

    # Enums  # TODO: which are <B and which are <I?
    'EQUIP_MODEL_CATEGORY': (),
    'EQUIP_MODEL_GENDER': (),
    'WEAPON_CATEGORY': (),
    'WEPMOTION_CATEGORY': (),
    'GUARDMOTION_CATEGORY': (),
    'WEP_MATERIAL_ATK': (),
    'WEP_MATERIAL_DEF': (),
    'WEP_MATERIAL_DEF_SFX': (),
    'WEP_CORRECT_TYPE': (),
    'ATKPARAM_SPATTR_TYPE': (),
    'DURABILITY_DIVERGENCE_CATEGORY': (),
    'EQUIP_BOOL': (),
    'WEP_BASE_CHANGE_CATEGORY': (),
    # 'dummy8': (),
    'PROTECTOR_CATEGORY': (),
    'ATK_PARAM_PARTSDMGTYPE': (),
    'ACCESSORY_CATEGORY': (),
    'BEHAVIOR_REF_TYPE': (),
    'BEHAVIOR_CATEGORY': (),
    'GOODS_TYPE': (),
    'GOODS_CATEGORY': (),
    'GOODS_USE_ANIM': (),
    'GOODS_OPEN_MENU': (),
    'SP_EFFECT_USELIMIT_CATEGORY': (),
    'REPLACE_CATEGORY': (),
    'SHOP_LINEUP_SHOPTYPE': (),
    'SHOP_LINEUP_EQUIPTYPE': (),
    'ON_OFF': (),
    'ACTION_PATTERN': (),
    'THROW_PAD_TYPE': (),
    'THROW_ENABLE_STATE': (),
    'THROW_TYPE': (),
    'THROW_DMY_CHR_DIR_TYPE': (),
    'ENEMY_BEHAVIOR_ID': (),
    'ChrType': (),
    'NPC_ITEMDROP_TYPE': (),
    'NPC_DRAW_TYPE': (),
    'NPC_TYPE': (),
    'NPC_TEMA_TYPE': (),  # (sic)
    'NPC_MOVE_TYPE': (),
    'NPC_BURN_TYPE': (),
    'NPC_SFX_SIZE': (),
    'NPC_HITSTOP_TYPE': (),
    'NPC_BOOL': (),
    'ATK_PARAM_HIT_TYPE': (),
    'ATK_PARAM_MAP_HIT': (),
    'ATKPARAM_ATKATTR_TYPE': (),
    'BEHAVIOR_ATK_TYPE': (),
    'BEHAVIOR_ATK_SIZE': (),
    'ATK_PARAM_HIT_SOURCE': (),
    'ATK_PATAM_THROWFLAG_TYPE': (),
    'ATK_PARAM_BOOL': (),
    'NPC_THINK_GOAL_ACTION': (),
    'NPC_THINK_REPLY_BEHAVIOR_TYPE': (),
    'MAGIC_CATEGORY': (),
    'MAGIC_MOTION_TYPE': (),
    'SP_EFFECT_TYPE': (),
    'MAGIC_BOOL': (),
    'ATK_TYPE': (),
    'ATK_SIZE': (),
    'BULLET_LAUNCH_CONDITION_TYPE': (),
    'BULLET_FOLLOW_TYPE': (),
    'BULLET_EMITTE_POS_TYPE': (),
    'BULLET_ATTACH_EFFECT_TYPE': (),
    'SP_EFFECT_SPCATEGORY': (),
    'SP_EFFECT_SAVE_CATEGORY': (),
    'ATKPARAM_REP_DMGTYPE': (),
    'SP_EFE_WEP_CHANGE_PARAM': (),
    'SP_EFFECT_MOVE_TYPE': (),
    'SP_EFFECT_THROW_CONDITION_TYPE': (),
    'SP_EFFECT_BOOL': (),
    'SP_EFFECT_VFX_EFFECT_TYPE': (),
    'SP_EFFECT_VFX_SOUL_PARAM_TYPE': (),
    'SP_EFFECT_VFX_PLAYCATEGORY': (),
    'ITEMLOT_ITEMCATEGORY': (),
    'ITEMLOT_ENABLE_LUCK': (),
    'ITEMLOT_CUMULATE_RESET': (),
    'CHARACTER_INIT_SEX': (),
    'CHRINIT_VOW_TYPE': (),
    'FACE_PARAM_HAIRSTYLE_TYPE': (),
    'FACE_PARAM_HAIRCOLOR_TYPE': (),
    'RAGDOLL_PARAM_BOOL': (),
    'SKELETON_PARAM_KNEE_AXIS_DIR': (),
    'OBJACT_SP_QUALIFIED_TYPE': (),
    'OBJACT_CHR_SORB_TYPE': (),
    'OBJACT_EVENT_KICK_TIMING': (),
    'HMP_FOOT_EFFECT_HEIGHT_TYPE': (),
    'HMP_FOOT_EFFECT_DIR_TYPE': (),
    'HMP_FLOOR_HEIGHT_TYPE': (),
}


class ParamEntry(object):

    def __init__(self, entry_source, paramdef, name=None):
        self.fields = OrderedDict()
        self.paramdef = paramdef

        if isinstance(entry_source, OrderedDict):
            if name is None:
                if 'name' not in entry_source:
                    raise ValueError("Name must be specified in arguments or source dictionary.")
                self.name = entry_source['name']
            elif isinstance(name, str):
                # TODO: Name needs to be converted to shift-jis...
                if 'name' not in entry_source:
                    print(f"# WARNING: Name in source dictionary of ParamEntry '{entry_source['name']}' will\n"
                          f"be overridden with argument value ('{name}').")
                self.name = entry_source['name'] = name
            else:
                raise ValueError("Name must be a string.")
        elif isinstance(entry_source, dict):
            raise TypeError("You must use an OrderedDict to create a ParamEntry. Try copying an existing entry first.")
        elif isinstance(entry_source, bytes):
            if name is None:
                raise ValueError("`name` argument must be given explictly alongside raw entry data.")
            self.unpack(entry_source, name)
            self.name = name

    def __iter__(self):
        return iter(self.fields.items())

    def __getitem__(self, field):
        if isinstance(field, int):
            try:
                field = list(self.fields.keys())[field]
            except IndexError:
                raise KeyError(f"No field with index {field}.")
        if isinstance(field, str):
            try:
                return self.fields[field]
            except KeyError:
                raise KeyError(f"No field with name '{field}' in entry {self.fields['name']}.")

    def __setitem__(self, field, value):
        if isinstance(field, int):
            try:
                field = list(self.fields.keys())[field]
            except IndexError:
                raise KeyError(f"No field with index {field}. (You cannot create new fields.)")
        if field not in self.fields:
            raise KeyError(f"Field '{field}' does not exist in param.")
        # TODO: Check value type is valid (or that it can be cast).
        self.fields[field] = value

    @property
    def field_names(self):
        return list(self.fields.keys())

    def __repr__(self):
        return f"\nName: {self.name}" + ''.join(
            [f"\n    {key} = {value}" for key, value in self.fields.items()])

    def unpack(self, entry_buffer, name: str):
        bit_field = None
        bit_field_offset = 0
        if isinstance(entry_buffer, bytes):
            entry_buffer = BytesIO(entry_buffer)

        for field in self.paramdef.fields:

            # Determine field format.
            if field['bit_size'] < 8:
                field_format = 'bit'
            elif field['internal_type'] == 'dummy8':
                field_format = field['size']
            elif not field['internal_type'] or not PARAM_TYPE_INFO[field['internal_type']]:
                # Internal type missing or has no information; use debug type.
                try:
                    field_format = PARAM_TYPE_INFO[field['debug_type']][0]
                except IndexError:
                    # It's an enum whose size I haven't written yet (so guess based on size).
                    raise KeyError(f"Field {field['name']} has unknown debug type {field['debug_type']}.")
            else:
                field_format = PARAM_TYPE_INFO[field['internal_type']][0]

            if field_format == 'bit':
                if bit_field is None:
                    # Consume (and reverse) new one-byte bit field.
                    bit_field = format(struct.unpack('<B', entry_buffer.read(1))[0], '08b')[::-1]

                field_value = int(bit_field[bit_field_offset:bit_field_offset + field['bit_size']][::-1], 2)
                bit_field_offset += field['bit_size']
                if bit_field_offset >= 8:
                    bit_field = None
                    bit_field_offset = bit_field_offset % 8

            else:
                if bit_field is not None:
                    # Terminate unfinished bit field.
                    bit_field = None
                    bit_field_offset = 0
                if isinstance(field_format, int):
                    # Padding.
                    field_value = entry_buffer.read(field['size'])
                    if not field_value == b'\0' * field['size']:
                        print(field, "Value:", field_value, "Format:", field_format)
                        raise ValueError("Pad value is not null.")
                else:
                    data = entry_buffer.read(struct.calcsize(field_format))
                    try:
                        field_value, = struct.unpack(field_format, data)
                    except struct.error:
                        if field['debug_name'] in {'inverseToneMapMul', 'sfxMultiplier'}:
                            # These fields are screwed up in m99 and default ToneMapBank.
                            field_value = 1.0
                        else:
                            raise ValueError(f"Could not read any data for field: {field}")

            self.fields[field['name']] = field_value

        self.name = name


class ParamTable(object):

    # TODO: This is currently for DeS/DS1 only.
    HEADER_STRUCT = BinaryStruct(
        ('name_data_offset', 'I'),
        ('entry_data_offset', 'H'),
        ('magic0', 'H'),  # 0 or 1
        ('magic1', 'H'),  # 1, 2, or 3
        ('entry_count', 'H'),
        ('param_name', '32j'),
        ('big_endian', 'b', 0),  # TODO: check, rather than assert
        ('magic2', 'H'),  # TODO: Actually two format flag bytes.
        ('unknown', 'B', 0),  # TODO: sometimes -1 in later formats.
    )

    ENTRY_POINTER_STRUCT = BinaryStruct(
        # These are packed together, and contain offsets into packed entry data and packed names.
        ('id', 'i'),
        ('data_offset', 'i'),
        ('name_offset', 'i'),
    )

    entries: Dict[int, ParamEntry]

    def __init__(self, param_source, paramdef_bnd):
        # TODO: Need to specify param type somewhere.
        self.param_path = ''
        self.param_name = ''  # internal name (shift-jis) with capitals and underscores
        self.paramdef_bnd = PARAMDEF_BND(paramdef_bnd) if isinstance(paramdef_bnd, str) else paramdef_bnd
        self.entries = {}
        self.__magic = []

        if isinstance(param_source, dict):
            self.entries = param_source

        elif isinstance(param_source, bytes):
            self.unpack(BytesIO(param_source))

        elif isinstance(param_source, str):
            self.param_path = param_source
            with open(param_source, 'rb') as data:
                self.unpack(data)

        elif hasattr(param_source, 'data'):
            # Try reading .data attribute (e.g. BNDEntry).
            try:
                self.unpack(BytesIO(param_source.data))
            except ValueError:
                raise ValueError("ParamTable source has a '.data' attribute, but it could not be interpreted.")

    def __getitem__(self, entry_index):
        if entry_index in self.entries:
            return self.entries[entry_index]
        raise KeyError(f"No entry with ID {entry_index} in {self.param_name}.")

    def __setitem__(self, entry_index, entry):
        if isinstance(entry, dict):
            if 'name' not in entry:
                raise ValueError("New entry must have a 'name' field.")
            entry = ParamEntry(entry, self.paramdef_bnd[self.param_name])
        if isinstance(entry, ParamEntry):
            self.entries[entry_index] = entry
        raise TypeError("New entry must be a ParamEntry or a dictionary that contains all required fields.")

    def __iter__(self):
        return iter(self.entries.items())

    # TODO: __repr__ method returns basic information about ParamTable (but not entire entry list).

    def unpack(self, param_buffer):
        header = self.HEADER_STRUCT.unpack(param_buffer)
        self.param_name = header.param_name
        self.__magic = [header.magic0, header.magic1, header.magic2]
        entry_data_offset = header.entry_data_offset
        name_data_offset = header.name_data_offset  # CANNOT BE TRUSTED IN VANILLA FILES! Off by +12 bytes.

        # Load entry pointer data.
        entry_pointers = self.ENTRY_POINTER_STRUCT.unpack(param_buffer, count=header.entry_count)

        # Entry size is lazily determined.
        if len(entry_pointers) == 0:
            return
        elif len(entry_pointers) == 1:
            # NOTE: No vanilla ParamTables have just one entry, so name_data_offset can be implicitly trusted here.
            entry_size = name_data_offset - entry_data_offset
        else:
            entry_size = entry_pointers[1].data_offset - entry_pointers[0].data_offset

        # Store packed data blocks.
        param_buffer.seek(entry_data_offset)
        packed_entry_data = param_buffer.read(entry_size * header.entry_count)
        name_data_offset = param_buffer.tell()  # Overrides untrustworthy value from header.
        packed_name_data = param_buffer.read()

        # Note that we no longer need to track buffer offset.
        for entry_struct in entry_pointers:
            relative_entry_offset = entry_struct.data_offset - entry_data_offset
            entry_data = packed_entry_data[relative_entry_offset:relative_entry_offset + entry_size]
            if entry_struct.name_offset != 0:
                relative_name_offset = entry_struct.name_offset - name_data_offset
                name = read_chars_from_bytes(packed_name_data, offset=relative_name_offset, encoding='shift_jis_2004')
            else:
                name = ''
            self.entries[entry_struct.id] = ParamEntry(entry_data, self.paramdef_bnd[self.param_name], name=name)

    def pack(self, sort=True):
        sorted_entries = sorted(self.entries.items()) if sort else self.entries.items()

        current_name_offset = 0
        name_offset_list = []
        data_offset = 0
        data_offset_list = []
        packed_names = b''
        packed_data = b''

        warned_enum_names = set()

        for entry_id, entry in sorted_entries:

            # 1. Pack names with relative offsets (to be globally offset later).
            name_z_str = entry.name.encode('shift_jis_2004') + b'\x00'
            packed_names += name_z_str
            name_offset_list.append(current_name_offset)
            current_name_offset += len(name_z_str)

            # 2. Pack data after validating the type for each field.
            packed_entry = b''
            bit_field = ''
            for field_name, field_value in entry.fields.items():  # These are ordered correctly already.

                field = self.paramdef_bnd[field_name]

                if field['bit_size'] < 8:
                    # Add bits.
                    binary_value = bin(field_value)[2:]
                    if len(binary_value) > field['bit_size']:
                        raise ValueError(f"Value {field_value} (binary: {binary_value}) of binary field "
                                         f"{field_name} is too large for field size of {field['bit_size']} bits).")
                    binary_value = '0' * (field['bit_size'] - len(binary_value)) + binary_value  # leading zeroes
                    bit_field += binary_value[::-1]
                    if len(bit_field) >= 8:
                        completed_bit_field = bit_field[:8]
                        byte_to_write = int(completed_bit_field[::-1], 2)  # reversed
                        packed_entry += struct.pack('<B', byte_to_write)
                        # Leftover bytes go into next lot (though this should never happen due to pad fields).
                        bit_field = bit_field[8:] if len(bit_field) > 8 else ''
                else:
                    if bit_field:
                        # Pad out existing non-empty bit field and write it.
                        bit_field += '0' * (8 - len(bit_field))
                        byte_to_write = int(bit_field[::-1], 2)  # note reversal
                        packed_entry += struct.pack('<B', byte_to_write)
                        bit_field = ''

                    if field['internal_type'] == 'dummy8':
                        # Write nulls.
                        packed_entry += b'\x00' * field['size']
                        continue

                    if field['internal_type'] in PARAM_TYPE_INFO and PARAM_TYPE_INFO[field['internal_type']]:
                        try:
                            field_fmt, field_type, field_min, field_max = PARAM_TYPE_INFO[field['internal_type']]
                        except ValueError:
                            raise ValueError(f"Found incomplete enum {field['internal_type']} in PARAM_TYPE_INFO.")
                    else:
                        # It's an enum whose size I haven't written yet. TODO: Get all the enum sizes.
                        if field_name not in warned_enum_names:
                            print(f"# WARNING: Field {field_name} has unknown enum type {field['internal_type']} "
                                  f"(field size: {field['size']}).")
                            warned_enum_names.add(field_name)
                        if field['size'] == 1:
                            field_fmt, field_type, field_min, field_max = '<B', int, 0, 2 ** 8 - 1
                        else:
                            field_fmt, field_type, field_min, field_max = '<I', int, 0, 2 ** 32 - 1

                    if not isinstance(entry[field['name']], field_type):
                        raise ValueError(f"Bad type: field {field['name']} in entry {entry_id} has value "
                                         f"{entry[field['name']]} with type {type(entry[field['name']])},\n"
                                         f"but should have type {field_type}.")
                    if not field_min <= entry[field['name']] <= field_max:
                        raise ValueError(f"Invalid: field {field['name']} in entry {entry_id} has out-of-range value "
                                         f"{entry[field['name']]}")

                    packed_entry += struct.pack(field_fmt, field_value)

            packed_data += packed_entry
            data_offset_list.append(data_offset)
            data_offset += len(packed_entry)

        entry_pointer_table_offset = self.HEADER_STRUCT.size
        entry_data_offset = entry_pointer_table_offset + self.ENTRY_POINTER_STRUCT.size * len(sorted_entries)
        name_data_offset = entry_data_offset + len(packed_data)

        # Entries.
        entry_pointer_data = b''
        for i, (entry_id, _) in enumerate(sorted_entries):
            entry_pointer_data += self.ENTRY_POINTER_STRUCT.pack(dict(
                id=entry_id, data_offset=entry_data_offset + data_offset_list[i],
                name_offset=name_data_offset + name_offset_list[i]))

        # Header.
        header = self.HEADER_STRUCT.pack(dict(
            name_data_offset=name_data_offset,
            entry_data_offset=entry_data_offset,
            magic0=self.__magic[0],
            magic1=self.__magic[1],
            entry_count=len(sorted_entries),
            param_name=self.param_name,
            magic2=self.__magic[2],
        ))

        return header + entry_pointer_data + packed_data + packed_names

    def write_packed(self, param_path=None):
        if param_path is None:
            if self.param_path:
                param_path = self.param_path
            else:
                raise ValueError("Param path could not be determined automatically (must be specified).")
        if not param_path.endswith('.param'):
            param_path += '.param'

        with open(param_path, 'wb') as output:
            output.write(self.pack())


class DrawParamTable(ParamTable):

    def get_active_draw_params(self, polyg=False):
        """ Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if polyg:
            return {index: entry for index, entry in self.entries.items()
                    if entry.name and not entry.name.startswith('0')}
        return {index: entry for index, entry in self.entries.items()
                if entry.name and not entry.name.startswith('0') and not entry.name.lower().startswith('polyg')}
