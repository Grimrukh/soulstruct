"""Test reading of encrypted `regulation.bin` (GameParamBND) in Elden Ring."""
import unittest

from soulstruct.logging_utils import setup
from soulstruct.eldenring.params import GameParamBND
from soulstruct.utilities.inspection import Timer


class ParamTest(unittest.TestCase):

    def setUp(self):
        setup(console_level="DEBUG")

    def test_regulation_read(self):
        with Timer("Regulation Read"):
            regulation = GameParamBND.from_encrypted_path("resources/regulation.bin")
            print(regulation.NpcParam[47300000])  # Starscourge Radahn


if __name__ == '__main__':
    unittest.main()
