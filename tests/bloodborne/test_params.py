import os
import unittest
from pathlib import Path

from soulstruct.bloodborne.params import GameParamBND
from soulstruct.bloodborne.params.paramdef import GET_BUNDLED_PARAMDEFBND
from soulstruct.utilities.misc import Timer


class ParamsTest(unittest.TestCase):

    def test(self):
        with Timer("ParamDef read"):
            paramdef_bnd = GET_BUNDLED_PARAMDEFBND()
        with Timer("GameParamBND read"):
            game_param = GameParamBND("gameparam.parambnd.dcx", paramdef_bnd=paramdef_bnd)
        with Timer("GameParamBND write"):
            game_param.write("_test_gameparam.parambnd.dcx")
        with Timer("GameParamBND re-read"):
            game_param_re = GameParamBND("_test_gameparam.parambnd.dcx")
        with Timer("GameParamBND comparison"):
            for initial, reload in zip(game_param.params.values(), game_param_re.params.values()):
                for i, reload_row in reload.items():
                    self.assertEqual(
                        initial[i],
                        reload_row,
                        msg=f"Param {initial.param_type}, row {i}\n{initial[i].compare(reload_row)}",
                    )

        with Timer("GameParamBND JSON write"):
            game_param.write_json("_test_gameparam.parambnd.json")
        with Timer("GameParamBND JSON re-read"):
            game_param_from_json = GameParamBND("_test_gameparam.parambnd.json")
        with Timer("GameParamBND JSON re-write"):
            game_param_from_json.write_json("_test_json_re_gameparam.parambnd.json")
        with Timer("GameParamBND re-read JSON write"):
            game_param_re.write_json("_test_re_gameparam.parambnd.json")

        # Check that JSON file does not change when reloaded and rewritten.
        with open("_test_gameparam.parambnd.json") as f:
            json_initial = f.readlines()
        with open("_test_json_re_gameparam.parambnd.json") as f:
            json_from_json_read = f.readlines()
        with open("_test_re_gameparam.parambnd.json") as f:
            json_from_binary_read = f.readlines()
        for i, (line_initial, line_json_read) in enumerate(zip(json_initial, json_from_json_read)):
            self.assertEqual(line_initial, line_json_read, msg=f"Line {i + 1}")
        for i, (line_initial, line_json_read) in enumerate(zip(json_initial, json_from_binary_read)):
            self.assertEqual(line_initial, line_json_read, msg=f"Line {i + 1}")

    def tearDown(self):
        for test_file in Path(".").glob("_test*"):
            if test_file.is_file():
                os.remove(str(test_file))


if __name__ == '__main__':
    unittest.main()
