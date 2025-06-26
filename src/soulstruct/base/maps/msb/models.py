from __future__ import annotations

__all__ = ["BaseMSBModel"]

import abc
import typing as tp
from dataclasses import dataclass
from string import Formatter

from soulstruct.utilities.binary import *

from .enums import BaseMSBModelSubtype, MSBSupertype
from .msb_entry import *

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBModel(MSBEntry, abc.ABC):
    """Base class used by all MSB models. (They used to not even subclass this per subtype, but now do.)"""

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.MODELS
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBModelSubtype]
    NAME_ENCODING: tp.ClassVar[str] = ""
    STRUCTS: tp.ClassVar[dict[str, MSBBinaryStruct]] = {}  # no data, just name and SIB path

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""

    sib_path: str = ""

    def to_msb_writer(
        self,
        writer: BinaryWriter,
        supertype_index: int,
        subtype_index: int,
        entry_lists: dict[str, IDList[MSBEntry]],
        instance_count=0,
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        self.HEADER_STRUCT.kwargs_to_msb_writer(
            self,
            writer,
            entry_offset,
            entry_lists,
            supertype_index=supertype_index,
            subtype_index=subtype_index,
            instance_count=instance_count,
        )

        for struct_name, struct_type in self.STRUCTS.items():
            if struct_type is None:
                continue  # not reserved in header
            struct_offset = writer.position - entry_offset
            writer.fill(f"{struct_name}_offset", struct_offset, obj=self)
            struct_type.kwargs_to_msb_writer(self, writer, entry_offset, entry_lists)

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        """TODO: Do some models use generic sib paths?"""
        return {"name": self.name, "sib_path": self.sib_path}

    def set_auto_sib_path(self, **format_kwargs):
        """Some `MSBModel` subclasses can auto-generate SIB path from `SIB_PATH_TEMPLATE` and `format_kwargs`.

        Tries to format `SIB_PATH_TEMPLATE` with just `self.name` by default. Typically, if more kwargs are required,
        this method is overridden, but it should still work if I forget (and extra `kwargs` are harmless).
        """
        if not self.SIB_PATH_TEMPLATE:
            raise TypeError(f"Cannot set `sib_path` automatically for type `{self.cls_name}`.")
        # Otherwise, try to format with just model `name`.
        try:
            self.sib_path = self.SIB_PATH_TEMPLATE.format(name=self.name, **format_kwargs)
        except KeyError:
            keys = [i[1] for i in Formatter().parse(self.SIB_PATH_TEMPLATE) if i[1] is not None and i[1] != "name"]
            raise TypeError(f"Setting `sib_path` automatically for type `{self.cls_name}` requires more kwargs: {keys}")

    def get_model_file_stem(self, map_stem: str):
        """Allows subclasses to depend on `map_stem` when generating model file stem. Default is just name."""
        return self.name

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        """Allows subclasses to convert a model file stem to a model name. Default is just stem."""
        return model_stem

    def set_name_from_model_file_stem(self, model_stem: str):
        """Set name immediately using class method above."""
        self.name = self.model_file_stem_to_model_name(model_stem)
