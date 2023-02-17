import os
import shutil
import unittest

from soulstruct.darksouls1ptde.params import GameParamBND
from soulstruct.darksouls1ptde.params.paramdef import GET_BUNDLED_PARAMDEFBND
from soulstruct.utilities.misc import Timer


class ParamsTest(unittest.TestCase):

    def setUp(self) -> None:
        for test_file in ("_test_gameparam.parambnd", "_test_gameparam.parambnd.json"):
            try:
                os.remove(test_file)
            except FileNotFoundError:
                pass
        try:
            shutil.rmtree("_test_gameparam_json")
        except FileNotFoundError:
            pass

    def test(self):
        with Timer("ParamDef read"):
            paramdef_bnd = GET_BUNDLED_PARAMDEFBND()
        with Timer("GameParamBND read"):
            game_param = GameParamBND.from_path("resources/GameParam.parambnd")
            print(game_param.entries[0].path)
        with Timer("GameParamBND write"):
            game_param.write("_test_gameparam.parambnd")
        with Timer("GameParamBND re-read"):
            GameParamBND.from_path("_test_gameparam.parambnd")
        with Timer("GameParamBND JSON write"):
            game_param.write_json_directory("_test_gameparam_json")
        with Timer("GameParamBND JSON re-read"):
            GameParamBND.from_json_directory("_test_gameparam_json")


if __name__ == '__main__':
    unittest.main()
