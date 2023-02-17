import shutil
import unittest

from soulstruct.config import DSR_PATH
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.utilities.misc import Timer


class TextTest(unittest.TestCase):

    def setUp(self) -> None:
        try:
            shutil.rmtree("_test_dsr_text")
        except FileNotFoundError:
            pass

    def test_text(self):

        with Timer("Read MSG Directory"):
            dsr_text = MSGDirectory.from_path(DSR_PATH + "/msg/ENGLISH")

        with Timer("Write MSG Directory"):
            dsr_text.write("_test_dsr_text")

        with Timer("Re-read MSG Directory"):
            MSGDirectory.from_path("_test_dsr_text")
