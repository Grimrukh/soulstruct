"""Test reading of encrypted `regulation.bin` (GameParamBND) in Elden Ring."""
import unittest

from soulstruct.eldenring.params import GameParamBND
from soulstruct.utilities.inspection import Timer
from constrata.metadata import BinaryMetadata


class ParamTest(unittest.TestCase):

    def test_atk_param_paramdef(self):
        from soulstruct.eldenring.params.paramdef import ParamDef
        from soulstruct.utilities.files import SOULSTRUCT_PATH

        paramdef = ParamDef.from_paramdex_xml(SOULSTRUCT_PATH("eldenring/params/paramdef/Paramdex/AtkParam.xml"))
        print(paramdef)
        print(sum([p.size for _, p in paramdef.fields.items()]))

    def test_regulation_read(self):
        with Timer("Regulation Read"):
            regulation = GameParamBND.from_encrypted_path("resources/regulation.bin")


if __name__ == '__main__':
    unittest.main()
