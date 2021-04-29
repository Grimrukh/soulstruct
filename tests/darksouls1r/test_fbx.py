import os
import unittest
from pathlib import Path

from soulstruct.base.models.fbx import FBX
from soulstruct.utilities.misc import Timer


class FBXTest(unittest.TestCase):

    def test_chr_read(self):
        with Timer("Reading chr FLVER"):
            gwyn = FBX("resources/c5370_noesis.fbx")
        print(gwyn.to_string())

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
