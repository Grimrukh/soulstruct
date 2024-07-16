import os
import unittest
from pathlib import Path

from soulstruct.darksouls1r.params import GameParamBND, ParamDefBND
from soulstruct.utilities.inspection import Timer


class ParamsTest(unittest.TestCase):

    def test(self):
        with Timer("ParamDef read"):
            paramdef_bnd = ParamDefBND.from_bundled("DARK_SOULS_DSR")
        with Timer("GameParamBND read"):
            game_param = GameParamBND("resources/GameParam.parambnd.dcx", paramdef_bnd=paramdef_bnd)

        # dagger = game_param.Weapons[100000]
        # packed = dagger.pack()
        # from soulstruct.params.base.param import ParamRow
        # dagger2 = ParamRow(packed, game_param.Weapons.paramdef, name=dagger.name)
        # for field in dagger.fields:
        #     print(field, dagger[field], dagger2[field])
        # exit()

        with Timer("GameParamBND write"):
            game_param.write("_test_gameparam.parambnd.dcx")
        with Timer("GameParamBND re-read"):
            game_param_re = GameParamBND("_test_gameparam.parambnd.dcx")

        with Timer("GameParamBND JSON write"):
            game_param.write_json("_test_gameparam.parambnd.json")
        with Timer("GameParamBND JSON re-read"):
            game_param_from_json = GameParamBND("_test_gameparam.parambnd.json")
        with Timer("GameParamBND JSON re-write"):
            game_param_from_json.write_json("_test_json_re_gameparam.parambnd.json")
        with Timer("GameParamBND re-read JSON write"):
            game_param_re.write_json("_test_re_gameparam.parambnd.json")

        # Check that JSON does not change when reloaded and rewritten.
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
