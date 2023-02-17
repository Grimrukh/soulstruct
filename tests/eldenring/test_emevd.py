import unittest

from soulstruct.eldenring.events.emevd import EMEVD
from soulstruct.utilities.inspection import Timer


class EMEVDTest(unittest.TestCase):

    # def setUp(self):
    #     for test_file in Path(".").glob("_test*"):
    #         if test_file.is_file():
    #             os.remove(str(test_file))

    def test_emevd(self):

        with Timer("EMEVD Binary Reader"):
            emevd = EMEVD.from_path("resources/m10_00_00_00.emevd.dcx")

        with Timer("EMEVD EVS Write"):
            emevd.write_evs("_test_emevd.evs.py")

        with Timer("EMEVD EVS Read"):
            evs = EMEVD.from_evs_path("_test_emevd.evs.py")

        # with Timer("EMEVD EVS Re-Write"):
        #     evs.write_evs(
        #         "_test_emevd_rewrite.evs.py",
        #         entity_star_module_paths=("resources/m10_00_00_00_entities.py",),
        #         entity_module_prefix="resources.",
        #     )

        # print(evs.events[0].instructions[0])
        # print(evs.events[0].instructions[1])
        # print(evs.events[0].instructions[2])


if __name__ == '__main__':
    unittest.main()
