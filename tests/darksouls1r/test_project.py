import shutil
import unittest

from soulstruct import DSR_PATH
from soulstruct.darksouls1r.project import GameDirectoryProject, ProjectWindow


class ProjectTest(unittest.TestCase):

    def setUp(self):
        try:
            shutil.rmtree("_test_project")
        except FileNotFoundError:
            pass

    def test_project_window(self):
        ProjectWindow(project_path="_test_project").wait_window()

    def test_project_console(self):
        GameDirectoryProject(project_path="_test_project", game_root=DSR_PATH)


if __name__ == '__main__':
    unittest.main()
