from soulstruct.utilities import word_wrap


class SoulstructError(Exception):
    def __init__(self, msg=None):
        super().__init__(word_wrap(msg, 60) if msg else msg)