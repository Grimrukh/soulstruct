import unittest
from pathlib import Path

from soulstruct.darksouls1r.events import EMEVD, EventDirectory
from soulstruct.utilities.inspection import Timer


class EMEVDTest(unittest.TestCase):

    # def setUp(self):
    #     for test_file in Path(".").glob("_test*"):
    #         if test_file.is_file():
    #             os.remove(str(test_file))

    def test_event_directory(self):
        from soulstruct.config import DSR_PATH

        with Timer("Event Directory Read"):
            ed = EventDirectory.from_path(DSR_PATH / "event")

        with Timer("Event Directory Write"):
            ed.write("_test_event_directory")

        with Timer("Event Directory EVS Write"):
            ed.write_evs("_test_evs_directory")

        with Timer("Event Directory EVS Read"):
            evs_ed = ed.from_path("_test_evs_directory")

        with Timer("Event Directory Write from EVS"):
            evs_ed.write("_test_event_from_evs_directory")

    def test_emevd(self):

        with Timer("EMEVD Binary Reader"):
            emevd = EMEVD.from_path("resources/m10_00_00_00.emevd.dcx")

        with Timer("EMEVD Binary Write"):
            emevd.write("_test.emevd.dcx")

        with Timer("EMEVD Binary Reader"):
            re_emevd = EMEVD.from_path("_test.emevd.dcx")

        with Timer("EMEVD EVS Write"):
            emevd.write_evs(
                "_test_emevd.evs.py",
                enums_star_module_paths=[Path("resources/m10_00_00_00_enums.py")],
                warn_missing_enums=True,
                enums_module_prefix="resources.",
            )
            # re_emevd.write_evs(
            #     "_test_re_emevd.evs.py",
            #     enums_star_module_paths=(Path("resources/m10_00_00_00_enums.py"),),
            #     warn_missing_enums=True,
            #     enums_module_prefix="resources.",
            # )

        # with Timer("EMEVD EVS Read"):
        #     evs = EMEVD.from_evs_path("_test_emevd.evs.py")

        # with Timer("EMEVD EVS Re-Write"):
        #     evs.write_evs(
        #         "_test_emevd_rewrite.evs.py",
        #         enum_star_module_paths=("resources/m10_00_00_00_enums.py",),
        #         enums_module_prefix="resources.",
        #     )

        # print(evs.events[0].instructions[0])
        # print(evs.events[0].instructions[1])
        # print(evs.events[0].instructions[2])


if __name__ == '__main__':
    unittest.main()
