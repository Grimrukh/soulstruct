import os
import unittest
from pathlib import Path

from soulstruct.flver import FLVER
from soulstruct.utilities.inspection import profile_function, Timer


class FLVERTest(unittest.TestCase):

    def test_map_piece_read(self):
        with Timer("Reading map piece FLVER (DCX)"):
            map_piece = FLVER.from_path("resources/m2200B0A10.flver.dcx")  # Depths sewers
        with Timer("Writing map piece FLVER (DCX)"):
            map_piece.write("_test_m2200B0A10.flver.dcx")
        with Timer("Re-reading map piece FLVER (DCX)"):
            FLVER.from_path("_test_m2200B0A10.flver.dcx")

    def test_chr_read(self):
        with Timer("Reading chr FLVER"):
            gwyn = FLVER.from_path("resources/c5370.flver")
        with Timer("Writing chr FLVER"):
            gwyn.write("_test_c5370.flver")
        with Timer("Re-reading chr FLVER"):
            FLVER.from_path("_test_c5370.flver")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
