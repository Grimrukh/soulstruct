"""Test reading of encrypted `regulation.bin` (GameParamBND) in Elden Ring."""
import unittest

from soulstruct.eldenring.params import GameParamBND
from soulstruct.utilities.inspection import Timer
from constrata.metadata import BinaryMetadata


class ParamTest(unittest.TestCase):

    def test_regulation_read(self):
        with Timer("Regulation Read"):
            regulation = GameParamBND.from_encrypted_path("resources/regulation.bin")


if __name__ == '__main__':
    unittest.main()
