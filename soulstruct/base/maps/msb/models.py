import typing as tp

from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.misc import partialmethod
from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .enums import MSBModelSubtype
from .msb_entry import MSBEntryList, MSBEntry
from .utils import MapFieldInfo


class MSBModel(MSBEntry):
    """`ENTRY_SUBTYPE` is spoofed as an instance variable, since all Models have identical binary formats."""

    MODEL_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0"
    SIB_PATH_STEM = ""

    FIELD_INFO = {
        "sib_path": MapFieldInfo(
            "Placeholder Path",
            str,
            None,
            "Internal path to model placeholder SIB file. The path's base name should match the model name.",
        ),
    }

    sib_path: str

    def __init__(self, source=None, model_subtype=None, **kwargs):
        """Create an instance of an MSB model entry using packed data (`source`) or keyword arguments.

        If `source` is not given, then at least `name`, `sib_path`, and `model_subtype` must be, with optional
        (defaults to `None`) and `sib_path` auto-generated using `name` and `entry_type`. For MapPiece, Collision, and
        Navmesh models, `sib_path` must be a full string or a sequence of map ID parts (e.g. (10, 2) or (10, 2, 0, 0)
        for map `m10_02_00_00.msb`), as the models for these MSB parts are map-specific.
        """
        self.ENTRY_SUBTYPE = None  # type: tp.Optional[MSBModelSubtype]
        self._model_type_index = None  # not sure if this matters
        self._instance_count = None

        if source is None:
            if model_subtype is None:
                raise ValueError("`model_subtype` must be passed to `MSBModel` if binary `source` is not given.")
            self.ENTRY_SUBTYPE = MSBModelList.resolve_entry_subtype(model_subtype)
            try:
                name = kwargs["name"]
            except KeyError:
                raise ValueError(
                    "`name` and (for some model subtypes) `sib_path` must be given to `MSBModel` "
                    "if no binary `source` is given."
                )
            kwargs["sib_path"] = self.auto_sib_path(
                name=name, entry_type=self.ENTRY_SUBTYPE, sib_path=kwargs.get("sib_path", None),
            )

        super().__init__(source=source, **kwargs)

    def unpack(self, msb_reader: BinaryReader):
        model_offset = msb_reader.position
        model_data = msb_reader.unpack_struct(self.MODEL_STRUCT)
        self.name = msb_reader.unpack_string(
            offset=model_offset + model_data["__name_offset"], encoding=self.NAME_ENCODING
        )
        self.sib_path = msb_reader.unpack_string(
            offset=model_offset + model_data["__sib_path_offset"], encoding=self.NAME_ENCODING,
        )
        try:
            self.ENTRY_SUBTYPE = MSBModelSubtype(model_data["__model_type"])
        except TypeError:
            raise ValueError(f"Unrecognized MSB model type: {model_data['__model_type']}")
        self.set(**model_data)

    def pack(self):
        name_offset = self.MODEL_STRUCT.size
        packed_name = self.get_name_to_pack().encode(self.NAME_ENCODING) + self.NULL
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode(self.NAME_ENCODING) + self.NULL if self.sib_path else self.EMPTY_SIB_PATH
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

    @classmethod
    def auto_sib_path(cls, name, entry_type, sib_path):
        if isinstance(sib_path, str):
            return sib_path

        if entry_type in (MSBModelSubtype.MapPiece, MSBModelSubtype.Collision, MSBModelSubtype.Navmesh):
            if not isinstance(sib_path, (list, tuple)) or len(sib_path) not in {2, 4}:
                raise TypeError(
                    f"`sib_path` for Map Pieces, Collisions, and Navmeshes must be a full string or a "
                    f"sequence of map ID parts, e.g. (10, 2), not: {repr(sib_path)}"
                )
            if len(sib_path) == 2:
                sib_path = (sib_path[0], sib_path[1], 0, 0)
            sib_path = f"m{sib_path[0]:02d}_{sib_path[1]:02d}_{sib_path[2]:02d}_{sib_path[3]:02d}"
            stem = cls.SIB_PATH_STEM + f"map\\{sib_path}\\"
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
            return cls.SIB_PATH_STEM + f"chr\\{name}\\sib\\{name}.sib"
        elif entry_type == MSBModelSubtype.Object:
            if not name.startswith("o"):
                raise ValueError(f"Object model name did not start with 'o': {name}")
            return cls.SIB_PATH_STEM + f"obj\\{name}\\sib\\{name}.sib"
        raise ValueError(f"Invalid MSB model type: {repr(entry_type)}. Cannot determine SIB path.")

    def __repr__(self):
        kwargs = {}
        default = self.__class__(name="__DEFAULT__", model_subtype=self.ENTRY_SUBTYPE)
        for name in self.field_names:
            value = getattr(self, name)
            default_value = getattr(default, name)
            if value == default_value:
                continue  # ignore default values
            kwargs[name] = value
        if kwargs:
            fields = "\n    ".join(f"{k}={repr(v)}," for k, v in kwargs.items())
            return (
                f"{self.__class__.__name__}(\n"
                f"    model_subtype={repr(self.ENTRY_SUBTYPE.name)},\n"
                f"    name={repr(self.name)},\n"
                f"    {fields}\n"
                f")"
            )
        return f"{self.__class__.__name__}(model_subtype={repr(self.ENTRY_SUBTYPE.name)}, name={repr(self.name)})"


class MSBModelList(MSBEntryList[MSBModel]):

    PLURALIZED_NAME = "Models"
    ENTRY_SUBTYPE_ENUM = MSBModelSubtype
    SUBTYPE_CLASSES = {}  # type: dict[MSBModelSubtype, tp.Callable]
    ENTRY_CLASS: tp.Type[MSBModel] = None

    _entries: list[MSBModel]

    MapPieces: list[MSBModel]
    Objects: list[MSBModel]
    Characters: list[MSBModel]
    Items: list[MSBModel]
    Players: list[MSBModel]
    Collisions: list[MSBModel]
    Navmeshes: list[MSBModel]

    new_map_piece_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.MapPiece)
    new_object_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Object)
    new_character_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Character)
    new_item_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Item)
    new_player_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Player)
    new_collision_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Collision)
    new_navmesh_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Navmesh)

    def pack_entry(self, index: int, entry: MSBModel):
        return entry.pack()

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


for _entry_subtype in MSBModelSubtype:
    setattr(
        MSBModelList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
