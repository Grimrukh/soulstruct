import os
import unittest
from pathlib import Path

from soulstruct.base.models.flver import FLVER
from soulstruct.utilities.inspection import Timer


class FLVERTest(unittest.TestCase):

    def test_map_piece_read(self):
        with Timer("Reading map piece FLVER"):
            map_piece = FLVER.from_path("resources/m0000.flv")

            # for mesh in map_piece.meshes:
            #     print(mesh.material)
            #     print(mesh.layout)
            #     print(mesh.vertices[:5])

        with Timer("Writing map piece FLVER"):
            map_piece.write("_test_m0000.flv")
        with Timer("Re-reading map piece FLVER"):
            FLVER.from_path("_test_m0000.flv")

    def test_chr_read(self):
        with Timer("Reading chr FLVER"):
            character = FLVER.from_path("resources/c3090.flv")

            for mesh in character.meshes:
                print(mesh.material)
                print(mesh.layout)
                print(mesh.vertices[:5])

        with Timer("Writing chr FLVER"):
            character.write("_test_c3090.flv")
        with Timer("Re-reading chr FLVER"):
            character.from_path("_test_c3090.flv")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
