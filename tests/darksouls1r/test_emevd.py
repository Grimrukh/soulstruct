import os
import unittest

from soulstruct.darksouls1r.events.emevd import EMEVD


class NavmeshTest(unittest.TestCase):

    def test_emevd(self):
        emevd = EMEVD("resources/m10_00_00_00.emevd.dcx")


if __name__ == '__main__':
    unittest.main()
