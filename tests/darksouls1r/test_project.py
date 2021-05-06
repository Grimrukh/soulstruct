import shutil
import unittest

from soulstruct.darksouls1r.events import EMEVD, compare_events
from soulstruct.darksouls1r.project import GameDirectoryProject, ProjectWindow


class ProjectTest(unittest.TestCase):

    def setUp(self):
        try:
            shutil.rmtree("_test_project")
        except FileNotFoundError:
            pass

    def test_project_console(self):
        GameDirectoryProject(project_path="_test_project", game_root="G:/Steam/steamapps/common/DARK SOULS REMASTERED")


if __name__ == '__main__':
    unittest.main()
