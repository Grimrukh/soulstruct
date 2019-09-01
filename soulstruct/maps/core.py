import re

_DUPLICATE_TAG_MATCH = re.compile(r' <(\d+)>$')


class MSBEntry(object):

    def __init__(self):
        self.name = None

    def get_name_to_pack(self):
        """Remove duplicate tags '<i>' from end of name."""
        return _DUPLICATE_TAG_MATCH.sub('', self.name)
