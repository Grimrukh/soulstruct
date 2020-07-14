import typing as tp
from io import BufferedReader, BytesIO

from soulstruct.core import SoulstructError
from soulstruct.maps.base import MSBEntryList, MSBEntry
from soulstruct.maps.core import MSB_MODEL_TYPE

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSBModel(MSBEntry):

    MODEL_STRUCT = BinaryStruct(
        ('__name_offset', 'i'),
        ('__model_type', 'i'),
        ('_model_type_index', 'i'),
        ('__sib_path_offset', 'i'),
        ('_instance_count', 'i'),
        '12x',
    )

    FIELD_INFO = {
        'sib_path': (
            'Placeholder Path', True, str,
            "Internal path to model placeholder SIB file. The path's base name should match the model name."),
    }

    def __init__(self, msb_model_source=None, name=None, description=None, model_type=None, sib_path=None):
        """Create an instance of an MSB model entry using packed data (`msb_model_source`) or keyword arguments.

        If `msb_model_source` is not given, then at least `name` and `entry_type` must be, with `description` optional
        (defaults to `None`) and `sib_path` auto-generated using `name` and `entry_type`. For MapPiece, Collision, and
        Navmesh models, `sib_path` must be a full string or a sequence of map ID parts (e.g. (10, 2) or (10, 2, 0, 0)
        for map `m10_02_00_00.msb`), as the models for these MSB parts are map-specific.
        """
        super().__init__()
        self.ENTRY_TYPE = None
        self._model_type_index = None  # not sure if this matters.
        self.sib_path = ""
        self._instance_count = None

        if isinstance(msb_model_source, bytes):
            msb_model_source = BytesIO(msb_model_source)
        if isinstance(msb_model_source, BufferedReader):
            self.unpack(msb_model_source)
        elif msb_model_source is None and name is not None and model_type is not None:
            self.name = name
            self.ENTRY_TYPE = MSBModelList.resolve_entry_type(model_type)
            if not isinstance(self.ENTRY_TYPE, MSB_MODEL_TYPE):
                raise TypeError(f"`model_type` must be a MSB_MODEL_TYPE (or a name/value inside it), not {model_type}")
            if description is None or isinstance(description, str):
                self.description = description
            else:
                raise TypeError("`description` must be a string (or None).")
            if isinstance(sib_path, str):
                self.sib_path = sib_path
            else:
                self.sib_path = self.auto_sib_path(name=self.name, entry_type=self.ENTRY_TYPE, sib_path=sib_path)
        else:
            raise TypeError(f"`msb_model_source` must be a buffer, `bytes`, or `None` (with `name` and `entry_type` "
                            f"given), not {type(msb_model_source)}")

    def unpack(self, msb_buffer):
        model_offset = msb_buffer.tell()
        model_data = self.MODEL_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data["__name_offset"], encoding='shift-jis')
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data["__sib_path_offset"], encoding='shift-jis')
        self.ENTRY_TYPE = MSB_MODEL_TYPE(model_data["__model_type"])
        self.set(**model_data)

    def pack(self):
        name_offset = self.MODEL_STRUCT.size
        packed_name = self.get_name_to_pack().encode('shift-jis') + b'\0'
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode('shift-jis') + b'\0' if self.sib_path else b'\0' * 6
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b'\0'
        packed_model_data = self.MODEL_STRUCT.pack(
            __name_offset=name_offset,
            __model_type=MSB_MODEL_TYPE(self.ENTRY_TYPE).value,
            _model_type_index=self._model_type_index,
            __sib_path_offset=sib_path_offset,
            _instance_count=self._instance_count,
        )
        return packed_model_data + packed_name + packed_sib_path

    def set_indices(self, model_type_index, instance_count):
        self._model_type_index = model_type_index
        self._instance_count = instance_count

    def set_sib_path_from_map_id(self, map_id):
        """Use given map ID sequence, e.g. (10, 2, 0, 0), to auto-set SIB path."""
        self.sib_path = self.auto_sib_path(name=self.name, entry_type=self.ENTRY_TYPE, sib_path=map_id)

    @staticmethod
    def auto_sib_path(name, entry_type, sib_path):
        stem = f"N:\\FRPG\\data\\Model\\"
        if entry_type in (MSB_MODEL_TYPE.MapPiece, MSB_MODEL_TYPE.Collision, MSB_MODEL_TYPE.Navmesh):
            if not isinstance(sib_path, (list, tuple)) or len(sib_path) not in {2, 4}:
                raise TypeError(f"`sib_path` for Map Pieces, Collisions, and Navmeshes must be a full string or a "
                                f"sequence of map ID parts, e.g. (10, 2), not: {repr(sib_path)}")
            if len(sib_path) == 2:
                sib_path = (sib_path[0], sib_path[1], 0, 0)
            sib_path = f"m{sib_path[0]:02d}_{sib_path[1]:02d}_{sib_path[2]:02d}_{sib_path[3]:02d}"
            stem += f"map\\{sib_path}\\"
            if entry_type == MSB_MODEL_TYPE.MapPiece:
                if not name.startswith("m"):
                    raise ValueError(f"MapPiece model name did not start with 'm': {name}")
                return stem + f"sib\\{name}.sib"
            elif entry_type == MSB_MODEL_TYPE.Collision:
                if not name.startswith("h"):
                    raise ValueError(f"Collision model name did not start with 'h': {name}")
                return stem + f"hkxwin\\{name}.hkxwin"
            elif entry_type == MSB_MODEL_TYPE.Navmesh:
                if not name.startswith("n"):
                    raise ValueError(f"Navmesh model name did not start with 'n': {name}")
                return stem + f"navimesh\\{name}.SIB"
        elif entry_type in (MSB_MODEL_TYPE.Character, MSB_MODEL_TYPE.Player):
            if not name.startswith("c"):
                raise ValueError(f"Character/Player model name did not start with 'c': {name}")
            return stem + f"chr\\{name}\\sib\\{name}.sib"
        elif entry_type == MSB_MODEL_TYPE.Object:
            if not name.startswith("o"):
                raise ValueError(f"Object model name did not start with 'o': {name}")
            return stem + f"obj\\{name}\\sib\\{name}.sib"
        elif entry_type == MSB_MODEL_TYPE.Unknown:
            raise ValueError("Cannot automatically determine model SIB path for 'Unknown' model type. (If you know "
                             "what this type is, please tell Grimrukh!)")
        raise ValueError(f"Invalid MSB model type: {entry_type}. Cannot determine SIB path.")


class MSBModelList(MSBEntryList[MSBModel]):

    ENTRY_LIST_NAME = "Models"
    ENTRY_CLASS = staticmethod(MSBModel)
    ENTRY_TYPE_ENUM = MSB_MODEL_TYPE

    _entries: tp.List[MSBModel]

    MapPieces: tp.List[MSBModel]
    Objects: tp.List[MSBModel]
    Characters: tp.List[MSBModel]
    Players: tp.List[MSBModel]
    Collisions: tp.List[MSBModel]
    Navmeshes: tp.List[MSBModel]

    def add_model(self, model_type, model_name, sib_path, description=None):
        """Add a new `MSBModel` instance of the given entry type and SIB path (or map sequence)."""
        self.add_entry(
            MSBModel(name=model_name, description=description, model_type=model_type, sib_path=sib_path),
            append_to_entry_type=model_type,
        )

    def set_indices(self, part_instance_counts):
        """Local type-specific index only. (Note that global entry index is still used by Parts.)"""
        type_indices = {}
        for entry in self._entries:
            try:
                entry.set_indices(
                    model_type_index=type_indices.setdefault(entry.ENTRY_TYPE, 0),
                    instance_count=part_instance_counts.get(entry.name, 0),
                )
            except KeyError as e:
                raise SoulstructError(f"Invalid map component name for {entry.ENTRY_TYPE.name} model {entry.name}: {e}")
            else:
                type_indices[entry.ENTRY_TYPE] += 1
