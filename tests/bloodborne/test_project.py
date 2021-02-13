import unittest

from soulstruct.bloodborne.project import ProjectWindow


class ProjectTest(unittest.TestCase):

    def test_project(self):
        pw = ProjectWindow(project_path="_test_project")
        pw.wait_window()


if __name__ == '__main__':
    unittest.main()
