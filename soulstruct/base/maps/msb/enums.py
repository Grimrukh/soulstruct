__all__ = [
    "BaseMSBSubtype",
    "BaseMSBModelSubtype",
    "BaseMSBEventSubtype",
    "BaseMSBRegionSubtype",
    "BaseMSBPartSubtype",
]

from enum import IntEnum


class BaseMSBSubtype(IntEnum):
    @property
    def pluralized_name(self):
        if self.name in ("Box", "Navmesh"):
            return self.name + "es"
        elif self.name in ("VFX", "Wind", "Treasure", "Navigation", "NPCInvasion", "WindVFX", "Other"):
            return self.name
        return self.name + "s"

    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError


class BaseMSBModelSubtype(BaseMSBSubtype):

    @property
    def sib_path_stem(self) -> str:
        raise NotImplementedError

    @classmethod
    def get_pluralized_type_name(cls) -> str:
        raise NotImplementedError

    def get_default_sib_path(self, name: str, map_id=()) -> str:
        raise NotImplementedError


class BaseMSBEventSubtype(BaseMSBSubtype):
    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError


class BaseMSBRegionSubtype(BaseMSBSubtype):
    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError


class BaseMSBPartSubtype(BaseMSBSubtype):
    @classmethod
    def get_pluralized_type_name(cls):
        raise NotImplementedError
