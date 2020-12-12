import typing as tp
from io import BufferedReader, BytesIO

from soulstruct.core import SoulstructError
from soulstruct.maps.base.msb_entry import MSBEntryList, MSBEntry
from soulstruct.maps.enums import MSBModelSubtype

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSBModel(MSBEntry):

    # ENTRY_SUBTYPE is spoofed as an instance variable, since all Models have identical binary formats.

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("__model_type", "I"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "i"),
        ("_instance_count", "i"),
        "12x",
    )

    ENCODING = "shift-jis"
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0" * 6

    FIELD_INFO = {
        "sib_path": (
            "Placeholder Path",
            str,
            "Internal path to model placeholder SIB file. The path's base name should match the model name.",
        ),
    }

    def __init__(self, msb_model_source=None, name=None, description=None, model_subtype=None, sib_path=None):
        """Create an instance of an MSB model entry using packed data (`msb_model_source`) or keyword arguments.

        If `msb_model_source` is not given, then at least `name` and `entry_type` must be, with `description` optional
        (defaults to `None`) and `sib_path` auto-generated using `name` and `entry_type`. For MapPiece, Collision, and
        Navmesh models, `sib_path` must be a full string or a sequence of map ID parts (e.g. (10, 2) or (10, 2, 0, 0)
        for map `m10_02_00_00.msb`), as the models for these MSB parts are map-specific.
        """
        super().__init__()
        self.ENTRY_SUBTYPE = None  # type: tp.Optional[MSBModelSubtype]
        self._model_type_index = None  # not sure if this matters.
        self.sib_path = ""
        self._instance_count = None

        if isinstance(msb_model_source, bytes):
            msb_model_source = BytesIO(msb_model_source)
        if isinstance(msb_model_source, BufferedReader):
            self.unpack(msb_model_source)
        elif msb_model_source is None and name is not None and model_subtype is not None:
            self.name = name
            self.ENTRY_SUBTYPE = MSBModelList.resolve_entry_subtype(model_subtype)
            if description is None or isinstance(description, str):
                self.description = description
            else:
                raise TypeError("`description` must be a string (or None).")
            if isinstance(sib_path, str):
                self.sib_path = sib_path
            else:
                self.sib_path = self.auto_sib_path(name=self.name, entry_type=self.ENTRY_SUBTYPE, sib_path=sib_path)
        else:
            raise TypeError(
                f"`msb_model_source` must be a buffer, `bytes`, or `None` (with `name` and `model_subtype` "
                f"given), not {type(msb_model_source)}."
            )

    def unpack(self, msb_buffer):
        model_offset = msb_buffer.tell()
        model_data = self.MODEL_STRUCT.unpack(msb_buffer)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data["__name_offset"], encoding=self.ENCODING,
        )
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=model_offset + model_data["__sib_path_offset"], encoding=self.ENCODING,
        )
        try:
            self.ENTRY_SUBTYPE = MSBModelSubtype(model_data["__model_type"])
        except TypeError:
            raise ValueError(f"Unrecognized MSB model type: {model_data['__model_type']}")
        self.set(**model_data)

    def pack(self):
        name_offset = self.MODEL_STRUCT.size
        packed_name = self.get_name_to_pack().encode(self.ENCODING) + self.NULL
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode(self.ENCODING) + self.NULL if self.sib_path else self.EMPTY_SIB_PATH
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        packed_model_data = self.MODEL_STRUCT.pack(
            __name_offset=name_offset,
            __model_type=self.ENTRY_SUBTYPE.value,
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
        self.sib_path = self.auto_sib_path(name=self.name, entry_type=self.ENTRY_SUBTYPE, sib_path=map_id)

    @staticmethod
    def auto_sib_path(name, entry_type, sib_path):
        stem = f"N:\\FRPG\\data\\Model\\"
        if entry_type in (MSBModelSubtype.MapPiece, MSBModelSubtype.Collision, MSBModelSubtype.Navmesh):
            if not isinstance(sib_path, (list, tuple)) or len(sib_path) not in {2, 4}:
                raise TypeError(
                    f"`sib_path` for Map Pieces, Collisions, and Navmeshes must be a full string or a "
                    f"sequence of map ID parts, e.g. (10, 2), not: {repr(sib_path)}"
                )
            if len(sib_path) == 2:
                sib_path = (sib_path[0], sib_path[1], 0, 0)
            sib_path = f"m{sib_path[0]:02d}_{sib_path[1]:02d}_{sib_path[2]:02d}_{sib_path[3]:02d}"
            stem += f"map\\{sib_path}\\"
            if entry_type == MSBModelSubtype.MapPiece:
                if not name.startswith("m"):
                    raise ValueError(f"MapPiece model name did not start with 'm': {name}")
                return stem + f"sib\\{name}.sib"
            elif entry_type == MSBModelSubtype.Collision:
                if not name.startswith("h"):
                    raise ValueError(f"Collision model name did not start with 'h': {name}")
                return stem + f"hkxwin\\{name}.hkxwin"
            elif entry_type == MSBModelSubtype.Navmesh:
                if not name.startswith("n"):
                    raise ValueError(f"Navmesh model name did not start with 'n': {name}")
                return stem + f"navimesh\\{name}.SIB"
        elif entry_type in (MSBModelSubtype.Character, MSBModelSubtype.Player):
            if not name.startswith("c"):
                raise ValueError(f"Character/Player model name did not start with 'c': {name}")
            return stem + f"chr\\{name}\\sib\\{name}.sib"
        elif entry_type == MSBModelSubtype.Object:
            if not name.startswith("o"):
                raise ValueError(f"Object model name did not start with 'o': {name}")
            return stem + f"obj\\{name}\\sib\\{name}.sib"
        raise ValueError(f"Invalid MSB model type: {repr(entry_type)}. Cannot determine SIB path.")


class MSBModelList(MSBEntryList[MSBModel]):

    PLURALIZED_NAME = "Models"
    ENTRY_SUBTYPE_ENUM = MSBModelSubtype
    ENTRY_CLASS = staticmethod(MSBModel)

    _entries: tp.List[MSBModel]

    MapPieces: tp.List[MSBModel]
    Objects: tp.List[MSBModel]
    Characters: tp.List[MSBModel]
    Items: tp.List[MSBModel]
    Players: tp.List[MSBModel]
    Collisions: tp.List[MSBModel]
    Navmeshes: tp.List[MSBModel]

    def add_model(self, model_subtype, model_name, sib_path=None, description=None) -> MSBModel:
        """Add a new `MSBModel` instance of the given entry subtype and SIB path (or map sequence)."""
        model = MSBModel(
            name=model_name,
            description=description,
            model_subtype=model_subtype,
            sib_path=sib_path,
        )
        self.add_entry(model, append_to_entry_subtype=model_subtype)
        return model

    def set_indices(self, part_instance_counts):
        """Local type-specific index only. (Note that global entry index is still used by Parts.)"""
        type_indices = {}
        for entry in self._entries:
            try:
                entry.set_indices(
                    model_type_index=type_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    instance_count=part_instance_counts.get(entry.name, 0),
                )
            except KeyError as e:
                raise SoulstructError(
                    f"Invalid map component name for {entry.ENTRY_SUBTYPE.name} model {entry.name}: {e}"
                )
            else:
                type_indices[entry.ENTRY_SUBTYPE] += 1

    def get_subtype_instance(self, entry_subtype, **kwargs):
        return MSBModel(msb_model_source=None, **kwargs)


for _entry_subtype in MSBModelList.ENTRY_SUBTYPE_ENUM:
    setattr(
        MSBModelList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
