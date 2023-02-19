import os
import unittest
from pathlib import Path

from soulstruct.darksouls1r.ezstate import TalkESD, TalkESDBND, TalkDirectory
from soulstruct.utilities.inspection import Timer


class TestTalk(unittest.TestCase):

    def test_talk_dir(self):

        from soulstruct import DSR_PATH
        td = TalkDirectory.from_path(DSR_PATH + "/script/talk")
        td.write_esp_directory("_test_talk_directory")
        tdd = TalkDirectory.from_path("_test_talk_directory")
        print(tdd.Depths[100010])

    def test_esd(self):
        talk = TalkESD.from_path("resources/t100613.esd")
        talk.write("_test_t100613.esd")
        retalk = TalkESD.from_path("_test_t100613.esd")

    def test_talkesdbnd(self):
        with Timer("Read TalkESDBND"):
            talkesdbnd = TalkESDBND.from_path("resources/m10_00_00_00.talkesdbnd.dcx")

        with Timer("Write TalkESDBND"):
            talkesdbnd.write("_test.talkesdbnd.dcx")

        with Timer("Re-Read TalkESDBND"):
            TalkESDBND.from_path("_test.talkesdbnd.dcx")

        with Timer("Write TalkESDBND Unpacked"):
            talkesdbnd.write_esp_directory("_test_talkesdbnd")
        with Timer("Read TalkESDBND Unpacked"):
            TalkESDBND.from_esp_directory("_test_talkesdbnd")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))
