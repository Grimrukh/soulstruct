import re

_DUPLICATE_TAG_MATCH = re.compile(r' <(\d+)>$')


class MSBEntry(object):

    ENTRY_TYPE = None
    FIELD_INFO = {}

    def __init__(self):
        self.name = None

    def get_name_to_pack(self):
        """Remove duplicate tags '<i>' from end of name."""
        return _DUPLICATE_TAG_MATCH.sub('', self.name)

    def __getitem__(self, field_name):
        if field_name in self.FIELD_INFO:
            return getattr(self, field_name)
        raise KeyError(f"Field {field_name} does not exist in MSB entry type {self.__class__.__name__}.")

    def __setitem__(self, field_name, value):
        if field_name in self.FIELD_INFO:
            setattr(self, field_name, value)
            return
        raise KeyError(f"Field {field_name} does not exist in MSB entry type {self.__class__.__name__}.")
