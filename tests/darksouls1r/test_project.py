import shutil
import unittest

from soulstruct import DSR_PATH
from soulstruct.darksouls1r.project import GameDirectoryProject, ProjectWindow


DSR_VANILLA_PATH = DSR_PATH + "/../DARK SOULS REMASTERED (Vanilla Backup)"


class ProjectTest(unittest.TestCase):

    # def setUp(self):
    #     try:
    #         shutil.rmtree("_test_project")
    #     except FileNotFoundError:
    #         pass

    def test_project_window(self):
        ProjectWindow(project_path="_test_project", game_root=DSR_VANILLA_PATH).wait_window()

    def test_project_console(self):
        GameDirectoryProject(project_path="_test_project", game_root=DSR_VANILLA_PATH)


if __name__ == '__main__':
    unittest.main()
