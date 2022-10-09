from __future__ import annotations

__all__ = ["BaseMSBModel", "BaseMSBGeometryModel", "BaseMSBModelList"]

import abc
import typing as tp

from soulstruct.utilities.binary import BinaryStruct, BinaryReader

from .enums import BaseMSBModelSubtype
from .msb_entry import MSBEntry
from .msb_entry_list import BaseMSBEntryList
from .utils import MapFieldInfo


class BaseMSBModel(MSBEntry, abc.ABC):
    """Class used by all MSB models."""

    ENTRY_SUBTYPE: BaseMSBModelSubtype
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

    def __init__(self, source=None, map_id=(), **kwargs):
        """Create an instance of an MSB model entry using packed data (`source`) or keyword arguments.

        If `source` is not given, then at least `sib_path` or both `name` (in kwargs) and `map_id` must be.
        """
        self._model_type_index = None  # not sure if this matters
        self._instance_count = None
        if source is None:
            if "sib_path" not in kwargs:
                if "name" not in kwargs:
                    raise ValueError(f"`name` must be given to `{self.__class__.__name__}` if `sib_path` is not given.")
                kwargs["sib_path"] = self.ENTRY_SUBTYPE.get_default_sib_path(kwargs["name"], map_id)

        super().__init__(source=source, **kwargs)

    def unpack(self, msb_reader: BinaryReader):
        model_offset = msb_reader.position
        header = msb_reader.unpack_struct(self.MODEL_STRUCT)
        self.name = msb_reader.unpack_string(
            offset=model_offset + header["__name_offset"], encoding=self.NAME_ENCODING
        )
        self.sib_path = msb_reader.unpack_string(
            offset=model_offset + header["__sib_path_offset"], encoding=self.NAME_ENCODING,
        )
        if header["__model_type"] != self.ENTRY_SUBTYPE.value:
            raise ValueError(
                f"Unexpected MSB model type value {header['__model_type']} for {self.__class__.__name__}. "
                f"Expected {self.ENTRY_SUBTYPE.value}."
            )
        self.set(**header)

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

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        # TODO: Do some models use generic sib paths?
        return {"name": self.name, "sib_path": self.sib_path}

    def __repr__(self):
        data = self.to_dict(ignore_defaults=True)
        if data:
            fields = "\n    ".join(f"{k}={repr(v)}," for k, v in data.items())
            return (
                f"{self.__class__.__name__}(\n"
                f"    name={repr(self.name)},\n"
                f"    {fields}\n"
                f")"
            )
        return f"{self.__class__.__name__}(name={repr(self.name)})"


class BaseMSBGeometryModel(BaseMSBModel):

    def __init__(self, source=None, **kwargs):
        """Additionally Requires `map_id` if `source` is None."""
        if source is None and "sib_path" not in kwargs and ("map_id" not in kwargs or "name" not in kwargs):
            raise ValueError(
                f"`name` and `map_id` must be given to `{self.__class__.__name__}` if `sib_path` is not given."
            )
        super().__init__(source, **kwargs)


class BaseMSBModelList(BaseMSBEntryList, abc.ABC):

    @abc.abstractmethod
    def set_indices(self, part_instance_counts):
        pass
