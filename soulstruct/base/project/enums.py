__all__ = ["ProjectDataType"]

from soulstruct.utilities.future import StrEnum


class ProjectDataType(StrEnum):
    AI = "ai"
    Lighting = "lighting"
    Enums = "enums"
    Events = "events"
    Params = "params"
    Maps = "maps"
    Text = "text"
    Talk = "talk"
