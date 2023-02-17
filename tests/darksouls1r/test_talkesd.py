import os
import unittest
from pathlib import Path

from soulstruct.darksouls1r.ezstate import TalkESDBND
from soulstruct.utilities.inspection import Timer


class TextTest(unittest.TestCase):
    
    def test_text(self):
        with Timer("Read TalkESDBND"):
            dsr_text = TalkESDBND("resources/m10_00_00_00.talkesdbnd.dcx")
        with Timer("Write TalkESDBND Directory"):
            dsr_text.write("_test.talkesdbnd.dcx")
        with Timer("Re-read MSG Directory"):
            TalkESDBND("_test.talkesdbnd.dcx")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))
