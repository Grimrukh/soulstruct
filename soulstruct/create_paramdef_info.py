import inspect
import re

from soulstruct.bloodborne.params import paramdef as paramdef_module, ParamDefBND
from soulstruct.base.params.utils import *
from soulstruct.utilities.files import read_json, write_json


# def make_nickname_json():
#
#     game_dict = {}
#     paramdefbnd = ParamDefBND.from_bundled()
#
#     for attr_name, attr in vars(paramdef_module).items():
#         if inspect.isclass(attr) and issubclass(attr, ParamRow):
#
#             paramdef = paramdefbnd[attr_name]
#             paramdef_dict = game_dict.setdefault(attr_name, {})
#
#             print(attr_name)
#             # if attr_name == "TONE_MAP_BANK":
#             #     my_field_names = attr.get_binary_field_names()
#             #     paramdef_field_names = list(paramdef.fields)
#             #     diff = len(paramdef_field_names) - len(my_field_names)
#             #     my_field_names += ("<NONE>",) * diff
#             #     for field, paramdef_field in zip(my_field_names, paramdef_field_names, strict=True):
#             #         print(field, paramdef_field)
#             #     print(paramdef["inverseToneMapMul"])
#
#             for field, paramdef_field in zip(attr.get_binary_fields(), paramdef.fields.values(), strict=True):
#                 binary = field.metadata["binary"]
#                 metadata = field.metadata["param"]  # type: ParamFieldMetadata
#                 # paramdef_field = paramdef[metadata.internal_name]
#                 paramdef_dict[metadata.internal_name] = {
#                     "nickname": field.name, "tooltip": metadata.tooltip,
#                 }
#                 if not binary.asserted and field.default is not None and field.default != paramdef_field.default:
#                     if isinstance(field.default, bytes):
#                         if field.default:
#                             raise ValueError(f"Non-empty default bytes {field.default} for {field.name}")
#                         default = field.default.decode()
#                     else:
#                         default = field.default
#                     paramdef_dict[metadata.internal_name]["default"] = default
#
#     write_json("bloodborne/params/paramdef/paramdef_info.json", game_dict)


import colorama
colorama.init()
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW
RESET = colorama.Fore.RESET


def add_game_types():

    patterns = {
        "BulletParam": re.compile(r"hitbulletid"),
        "BehaviorParam": re.compile(r"behaviorid"),
        "SpecialEffectParam": re.compile(r"speffectid"),
        "UpgradeMaterialParam": re.compile(r"materialsetid"),
        "DecalParam": re.compile(r"decalid"),
        "AISoundParam": re.compile(r"aisoundid"),
        "Flag": re.compile(r"flagid"),
        "ItemLotParam": re.compile(r"itemlotparamid|itemlotid"),
        "SpellParam": re.compile(r"magicid"),
        "KnockbackParam": re.compile(r"knockbackparamid"),
        "ArmorParam": re.compile(r"protectorid|proparamid"),
        "WeaponParam": re.compile(r"weaponid|wepparamid"),
        "ModelDummy": re.compile(r"dmyid|dmypolyid|dummyid"),
        "Animation": re.compile(r"animid"),
        "ActionButtonParam": re.compile(r"actionbuttonparamid"),
        "Icon": re.compile(r"iconid"),
        "EquipmentModel": re.compile(r"equipmodelid|modelid|partsid"),  # TODO: Not sure if model ID and parts ID same
        "AIParam": re.compile(r"thinkid"),
        "FaceGenParam": re.compile(r"npcplayerfacegenid"),
        "AttackParam": re.compile(r"atkid"),
        "VisualEffect": re.compile(r"sfxid"),
        "GoodParam": re.compile(r"materialitemid|materialid0|mtrlitemid"),  # not just `materialid`
        "BattleAIScript": re.compile(r"battlegoalid"),
        "LogicAIScript": re.compile(r"logicid"),
    }

    ignore = {
        "sortid",
    }

    json_dict = read_json("darksouls1r/params/paramdef/paramdef_info.json")
    for paramdef_stem, paramdef in json_dict.items():
        for field_name, field_info in paramdef.items():
            if "dynamic_callback" in field_info:
                continue
            if field_name.lower() in ignore:
                continue
            if field_name.lower().endswith("offset"):
                continue

            if paramdef_stem == "EQUIP_PARAM_WEAPON_ST" and field_name == "reinforceTypeId":
                print(f"{YELLOW}{paramdef_stem}[{field_name}] = WeaponUpgradeParam{RESET}")
                field_info["game_type"] = "WeaponUpgradeParam"
                continue
            elif paramdef_stem == "EQUIP_PARAM_PROTECTOR_ST" and field_name == "reinforceTypeId":
                print(f"{YELLOW}{paramdef_stem}[{field_name}] = ArmorUpgradeParam{RESET}")
                field_info["game_type"] = "ArmorUpgradeParam"
                continue

            for game_type_name, pattern in patterns.items():
                if pattern.search(field_name.lower()):
                    print(f"{YELLOW}{paramdef_stem}[{field_name}] = {game_type_name}{RESET}")
                    field_info["game_type"] = game_type_name
                    break
            else:
                if "Id" in field_name or "ID" in field_name:
                    print(f"{RED}{paramdef_stem}[{field_name}] = ???{RESET}")

    write_json("darksouls1r/params/paramdef/paramdef_info.json", json_dict)


# if __name__ == '__main__':
#     add_game_types()
