import os
import unittest
from pathlib import Path

from soulstruct.darksouls1r.events.emevd import EMEVD


class EMEVDTest(unittest.TestCase):

    def test_emevd(self):
        emevd = EMEVD("resources/m10_00_00_00.emevd.dcx")
        emevd.write_numeric("_test_emevd_numeric.txt")

        numeric = EMEVD("_test_emevd_numeric.txt")
        numeric.write("_test_numeric.emevd.dcx")

        emevd.write_evs("_test_emevd.evs.py")
        evs = EMEVD("_test_emevd.evs.py")
        evs.write_numeric("_test_evs_numeric.txt")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
