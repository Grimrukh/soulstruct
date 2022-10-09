import os
import unittest
from pathlib import Path

from soulstruct.darksouls1r.events.emevd import EMEVD


class EMEVDTest(unittest.TestCase):

    def test_emevd(self):
        emevd = EMEVD("resources/m10_00_00_00.emevd.dcx")
        emevd.write_evs(
            "_test_emevd.evs.py",
            entity_star_module_paths=(Path("resources/m10_00_00_00_entities.py"),),
            warn_missing_enums=False,
            entity_module_prefix="resources.",
        )

        evs = EMEVD("_test_emevd.evs.py")
        print(evs.events[0].instructions[0])
        print(evs.events[0].instructions[1])
        print(evs.events[0].instructions[2])

    # def tearDown(self):
    #     for test_file in Path(".").glob("_test*"):
    #         if test_file.is_file():
    #             os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
