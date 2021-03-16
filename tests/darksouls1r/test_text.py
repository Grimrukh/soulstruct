import shutil
import unittest

from soulstruct.config import DSR_PATH
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.utilities import Timer


class TextTest(unittest.TestCase):
    
    def test_text(self):
        with Timer("Read MSG Directory"):
            dsr_text = MSGDirectory(DSR_PATH + "/msg/ENGLISH")
        with Timer("Write MSG Directory"):
            dsr_text.write("_test_dsr_text")
        with Timer("Re-read MSG Directory"):
            MSGDirectory("_test_dsr_text")

    def tearDown(self):
        shutil.rmtree("_test_dsr_text")
