"""Test reading of encrypted `regulation.bin` (GameParamBND) in Elden Ring."""
import logging
import unittest

from soulstruct.logging_utils import setup
from soulstruct.eldenring.params import GameParamBND
from soulstruct.utilities.inspection import Timer
from constrata.metadata import BinaryMetadata


# class ParamTest(unittest.TestCase):
#
#     def test_atk_param_paramdef(self):
#         from soulstruct.eldenring.params.paramdef import ParamDef
#         from soulstruct.utilities.files import SOULSTRUCT_PATH
#
#         paramdef = ParamDef.from_paramdex_xml(SOULSTRUCT_PATH("eldenring/params/paramdef/Paramdex/AssetGeometryParam.xml"))
#         print(f"{paramdef.path_name} total size:", paramdef.get_total_size())
#
#     def test_regulation_read(self):
#         with Timer("Regulation Read"):
#             regulation = GameParamBND.from_encrypted_path("resources/regulation.bin")


from soulstruct.utilities.inspection import profile_function


@profile_function(20)
def test_regulation_read():
    # with Timer("Regulation Read"):
    regulation = GameParamBND.from_encrypted_path("resources/regulation.bin")


if __name__ == '__main__':
    # unittest.main()
    setup(console_level="DEBUG")
    test_regulation_read()
