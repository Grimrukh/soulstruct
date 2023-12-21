import shutil
import unittest

from soulstruct import DSR_PATH
from soulstruct.darksouls1r.project import GameDirectoryProject, ProjectWindow
from soulstruct.utilities.inspection import profile_function


RESET_PROJECT = False
# DSR_VANILLA_PATH = DSR_PATH + "/../DARK SOULS REMASTERED (Vanilla Backup)"
DSR_VANILLA_PATH = DSR_PATH


class ProjectTest(unittest.TestCase):

    def setUp(self):
        if not RESET_PROJECT:
            return
        try:
            shutil.rmtree("_test_project")
        except FileNotFoundError:
            pass

    def test_project_window(self):
        ProjectWindow(project_path="_test_project", game_root=DSR_VANILLA_PATH).wait_window()

    # def test_event_directory_enums(self):
    #     from soulstruct.darksouls1r.events import EventDirectory
    #     from pathlib import Path
    #     event_directory = EventDirectory.from_path(
    #         DSR_VANILLA_PATH + "/event",
    #     )
    #     event_directory.write_evs(
    #         Path("_test_project/events"),
    #         enums_directory=Path("_test_project/enums"),
    #         warn_missing_enums=True,  # TODO: project setting
    #         enums_module_prefix="..enums.",
    #     )

    # def test_project_console(self):
    #     GameDirectoryProject(project_path="_test_project", game_root=DSR_VANILLA_PATH)


if __name__ == '__main__':
    unittest.main()
