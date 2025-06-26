import unittest

from soulstruct.flver import FLVER
from soulstruct.utilities.inspection import Timer


class EMEVDTest(unittest.TestCase):

    # def setUp(self):
    #     for test_file in Path(".").glob("_test*"):
    #         if test_file.is_file():
    #             os.remove(str(test_file))

    def test_flver(self):

        with Timer("FLVER Binary Read"):
            flver = FLVER.from_path("resources/m10_00_00_00.emevd.dcx")

        # print(evs.events[0].instructions[0])
        # print(evs.events[0].instructions[1])
        # print(evs.events[0].instructions[2])


if __name__ == '__main__':
    unittest.main()
