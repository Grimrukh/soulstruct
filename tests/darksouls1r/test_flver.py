import os
import unittest

from soulstruct.base.models.flver import FLVER


class FLVERTest(unittest.TestCase):

    def test_map_piece_read(self):
        FLVER("resources/m2200B0A10.flver.dcx")  # Depths sewers

    def test_chr_read(self):
        FLVER("resources/c5370.flver")  # Gwyn


if __name__ == '__main__':
    unittest.main()
