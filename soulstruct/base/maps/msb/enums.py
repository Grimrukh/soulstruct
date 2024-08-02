from __future__ import annotations

__all__ = [
    "MSBSupertype",
    "BaseMSBSubtype",
    "BaseMSBModelSubtype",
    "BaseMSBEventSubtype",
    "BaseMSBRegionSubtype",
    "BaseMSBPartSubtype",
]

from enum import IntEnum, StrEnum


class MSBSupertype(StrEnum):
    """Same for most games."""
    MODELS = "MODEL_PARAM_ST"
    EVENTS = "EVENT_PARAM_ST"
    REGIONS = "POINT_PARAM_ST"
    PARTS = "PARTS_PARAM_ST"

    @classmethod
    def resolve(cls, supertype: str) -> MSBSupertype:
        """Resolve various forms of the supertype name into this enum."""
        if supertype.upper().startswith("MODEL"):
            return cls.MODELS
        if supertype.upper().startswith("EVENT"):
            return cls.EVENTS
        if supertype.upper().startswith("REGION") or supertype.upper().startswith("POINT"):
            return cls.REGIONS
        if supertype.upper().startswith("PARTS"):
            return cls.PARTS
        raise ValueError(f"Cannot resolve unknown MSB supertype name: {supertype}")

    @classmethod
    def entity_id_supertypes(cls) -> tuple[MSBSupertype, ...]:
        """Returns all supertypes whose entries use entity IDs."""
        return cls.EVENTS, cls.REGIONS, cls.PARTS


class BaseMSBSubtype(IntEnum):
    @property
    def pluralized_name(self):
        """Handles library-wide special cases here out of laziness."""
        if self.name in ("Box", "Navmesh"):
            return self.name + "es"
        elif self.name in ("VFX", "Wind", "Treasure", "Navigation", "NPCInvasion", "WindVFX", "Other"):
            return self.name
        return self.name + "s"

    @classmethod
    def get_plural_supertype_name(cls):
        raise NotImplementedError


class BaseMSBModelSubtype(BaseMSBSubtype):

    @classmethod
    def get_sib_path_stem(cls) -> str:
        raise NotImplementedError

    @classmethod
    def get_plural_supertype_name(cls) -> str:
        raise NotImplementedError


class BaseMSBEventSubtype(BaseMSBSubtype):
    @classmethod
    def get_plural_supertype_name(cls):
        raise NotImplementedError


class BaseMSBRegionSubtype(BaseMSBSubtype):
    @classmethod
    def get_plural_supertype_name(cls):
        raise NotImplementedError


class BaseMSBPartSubtype(BaseMSBSubtype):
    @classmethod
    def get_plural_supertype_name(cls):
        raise NotImplementedError
