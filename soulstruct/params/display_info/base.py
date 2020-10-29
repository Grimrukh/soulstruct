import abc


class FieldDisplayInfo:
    def __init__(self, name, nickname, is_enabled, field_type, description="TODO", default_value=None, dsr_only=False):
        self.name = name
        self.nickname = nickname
        self.is_enabled = is_enabled
        self.field_type = field_type
        self.description = description
        self.default_value = default_value
        self.dsr_only = dsr_only

    def __call__(self, entry):
        """No harm done if you treat this as a `DynamicFieldInfo`."""
        return self


class DynamicFieldDisplayInfo(abc.ABC):
    """Called with a `ParamEntry` instance, in which `type_field_name` is checked before returning `FieldInfo`."""

    POSSIBLE_TYPES = set()

    def __init__(self, name, type_field_name):
        self.name = name
        self.type_field_name = type_field_name

    @abc.abstractmethod
    def __call__(self, entry) -> FieldDisplayInfo:
        ...


def pad_field(n):
    return f"<Pad:{n}>"
