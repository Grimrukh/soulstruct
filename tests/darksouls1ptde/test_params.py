import os
import unittest

from soulstruct.params.darksouls1ptde import GameParamBND, GET_BUNDLED_PARAMDEF
from soulstruct.utilities import Timer


class ParamsTest(unittest.TestCase):

    def test(self):
        with Timer("ParamDef read"):
            paramdef_bnd = GET_BUNDLED_PARAMDEF()
        with Timer("GameParamBND read"):
            game_param = GameParamBND("gameparam.parambnd", paramdef_bnd=paramdef_bnd)
        with Timer("GameParamBND write"):
            game_param.write("_test_gameparam.parambnd")
        with Timer("GameParamBND re-read"):
            GameParamBND("_test_gameparam.parambnd")
        with Timer("GameParamBND JSON write"):
            game_param.write_json("_test_gameparam.parambnd.json")
        with Timer("GameParamBND JSON re-read"):
            GameParamBND("_test_gameparam.parambnd.json")

    def tearDown(self) -> None:
        for test_file in ("_test_gameparam.parambnd", "_test_gameparam.parambnd.json"):
            try:
                os.remove(test_file)
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    unittest.main()
