"""Script that generates modules and classes in Soulstruct for a game's `ParamDef`s."""
import logging
import textwrap

from soulstruct.base.params.paramdef.paramdefbnd import ParamDefBND
from soulstruct.games import get_game
from soulstruct.utilities.files import SOULSTRUCT_PATH, read_json, write_json

_LOGGER = logging.getLogger(__name__)

# ParamDef field names with miserable weird characters that I've redirected.
# Remapping the entire names, rather than just the weird characters, to keep a better record.
BAD_NAMES = {
    "ｇradFactor": "gradFactor",
}


# Maps ParamDef type names to matching `constrata` type names (alias with bit size).
MAP_PARAM_TYPES = {
    "dummy8": "uint8",  # pad field
    "u8": "uint8",
    "u16": "uint16",
    "u32": "uint32",
    "s8": "int8",
    "s16": "int16",
    "s32": "int32",
    "f32": "float32",
    "f64": "float64",
    "fixstr": "str",  # decoded
    "fixstrW": "str",  # decoded
}


def get_default_nickname(field_name: str):
    nickname = field_name.split(":")[0].split("[")[0].replace("_", "")
    nickname = nickname[0].upper() + nickname[1:]  # capitalize first letter
    return nickname


# `darksouls1r` module imports all `ParamRow` classes from `darksouls1ptde`, except for these.
DSR_PARAMDEFS = (
    # NEW
    "COOL_TIME_PARAM_ST",
    "LEVELSYNC_PARAM_ST",
    "WHITE_COOL_TIME_PARAM_ST",
    # UPDATED
    "EQUIP_PARAM_GOODS_ST",
    "EQUIP_PARAM_WEAPON_ST",
    "REINFORCE_PARAM_WEAPON_ST",
    "TONE_CORRECT_BANK",
    "TONE_MAP_BANK",
)


def update_paramdef_info(paramdefbnd: ParamDefBND, game_submodule: str, template_info: dict = None):
    """Add nicknames and tooltips to 'paramdef_info.json' for given game.

    Any fields that are missing from the corresponding ParamDef in `paramdefbnd` will be removed, and any that are
    missing in the JSON will be added, optionally using `template_info[paramdef_stem][field_name]` as a starting point.
    """
    paramdef_dir = SOULSTRUCT_PATH(f"{game_submodule}/params/paramdef")
    json_path = paramdef_dir / "paramdef_info.json"
    if json_path.exists():
        json_dict = read_json(json_path)
    else:
        json_dict = {}  # completely fresh

    if template_info is None:
        template_info = {}

    for paramdef_stem, paramdef in paramdefbnd.paramdefs.items():
        paramdef_dict = json_dict.setdefault(paramdef_stem, {})
        existing_field_names = list(paramdef_dict)

        for field_name in paramdef.fields.keys():

            if field_name in BAD_NAMES:
                field_name = BAD_NAMES[field_name]

            if field_name not in existing_field_names:
                # New field must be added to JSON.
                try:
                    template_field = template_info[paramdef_stem][field_name]
                except KeyError:
                    template_field = {}
                nickname = template_field.get("nickname", get_default_nickname(field_name))
                tooltip = template_field.get("tooltip", "TOOLTIP-TODO")
                paramdef_dict[field_name] = {"nickname": nickname, "tooltip": tooltip}
                if template_field:
                    for optional_key in ("default", "game_type", "dynamic_callback"):
                        try:
                            paramdef_dict[field_name][optional_key] = template_field[optional_key]
                        except KeyError:
                            pass  # these keys are optional
            else:
                existing_field_names.remove(field_name)

        # Delete any outdated keys that are not in the given (presumably newer) `paramdefbnd`.
        for old_field_name in existing_field_names:
            paramdef_dict.pop(old_field_name)

    # Alphabetize ParamDef keys.
    json_dict = {k: json_dict[k] for k in sorted(json_dict)}

    write_json(json_path, json_dict)


def create_game_classes(
    paramdefbnd: ParamDefBND,
    game_submodule: str,
    no_info: bool = False,
    no_enums: bool = True,
    only_paramdefs: set[str] = (),
):
    """Use given `paramdefbnd` to generate `ParamRow` (`BinaryStruct`) subclasses, e.g. `ATK_PARAM_ST`.

    Unless disabled, `paramdef_
    """
    paramdef_dir = SOULSTRUCT_PATH(f"{game_submodule}/params/paramdef")

    if no_info:
        paramdefbnd_info = {}
    else:
        paramdef_info_path = paramdef_dir / "paramdef_info.json"
        try:
            # Named to distinguish it from the per-ParamDef sub-dictionaries used below.
            paramdefbnd_info = read_json(paramdef_info_path)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Could not find ParamDef info JSON: {paramdef_info_path}. Create it first with "
                f"`create_paramdef_info()` or ignore it with `no_info=True` argument."
            )

    # TODO: Collect all *USED* values of all enums by iterating over actual GameParam.
    all_enums = {}  # maps display type names to internal_type

    for paramdef_stem, paramdef in paramdefbnd.paramdefs.items():

        if only_paramdefs and paramdef_stem not in only_paramdefs:
            continue

        print(f"Creating `{game_submodule}` class for: {paramdef_stem}")

        bitpad_count = 0
        pad_count = 0

        import_lines = [
            "from __future__ import annotations",
            "",
            f"__all__ = [\"{paramdef_stem}\"]",
            "",
            "from soulstruct.base.params.param_row import *",
            "from soulstruct.utilities.binary import *",
        ]

        dynamic_imports = []

        lines = [
            f"class {paramdef_stem}(ParamRow):",  # dataclass built in to `BinaryStruct`
        ]

        game_types_used = False
        param_enums_used = False

        try:
            paramdef_info = paramdefbnd_info[paramdef_stem]
        except KeyError:
            paramdef_info = {
                field_name: {"nickname": get_default_nickname(field_name), "tooltip": "TOOLTIP-TODO"}
                for field_name in paramdef.fields
            }

        for field_name, paramdef_field in paramdef.fields.items():
            if field_name in BAD_NAMES:
                field_name = BAD_NAMES[field_name]

            display_type_name = paramdef_field.display_type.__name__
            enum_name = paramdef_field.internal_type_name
            if not enum_name:
                if game_submodule == "darksouls1r" and field_name == "sfxMultiplier":  # known bug in DSR ParamDef
                    enum_name = display_type_name

            try:
                info = paramdef_info[field_name]
            except KeyError:
                raise KeyError(f"No info for field `{field_name}` in paramdef {paramdef_stem}.")

            fmt = MAP_PARAM_TYPES[display_type_name]
            field_args = [fmt, f"\"{field_name}\""]

            ind = " " * 8

            if display_type_name == "dummy8":  # pad
                if paramdef_field.bit_count != -1:  # bit pad
                    lines.append(
                        f"    _BitPad{bitpad_count}: int = ParamBitPad({fmt}, \"{field_name}\", "
                        f"bit_count={paramdef_field.bit_count})"
                    )
                    bitpad_count += 1
                else:  # array pad
                    lines.append(
                        f"    _Pad{pad_count}: bytes = ParamPad({paramdef_field.size}, \"{field_name}\")"
                    )
                    pad_count += 1
                continue

            # Get display type enum (if given).
            if enum_name != display_type_name:
                field_args.append(enum_name)  # no keyword
                param_enums_used = True
                if enum_name not in all_enums:
                    all_enums[enum_name] = display_type_name
                elif all_enums[enum_name] != display_type_name:
                    old_display_type_name = all_enums[enum_name]
                    if (
                        old_display_type_name[0] in "su" and display_type_name[0] in "su"
                        and old_display_type_name[1:] == display_type_name[1:]
                    ):
                        # Just a signed/unsigned difference. Use unsigned.
                        all_enums[enum_name] = "u" + old_display_type_name[1:]
                    else:
                        raise ValueError(
                            f"Enum type `{enum_name}` had display type {all_enums[enum_name]} but now has type "
                            f"'{display_type_name}' from field '{field_name}' in '{paramdef_stem}."
                        )

            if "game_type" in info:
                field_args.append(f"game_type={info['game_type']}")
                game_types_used = True

            # Get field type annotation.
            if display_type_name in {"fixstr", "fixstrW"}:
                if display_type_name == "fixstrW":
                    field_args.append(f"encoding=\"utf-16\"")  # no baked endianness
                else:
                    field_args.append(f"encoding=\"shift_jis_2004\"")
                field_args.append(f"length={paramdef_field.size}")
                field_type_name = "str"
            elif paramdef_field.bit_count == 1:
                field_type_name = "bool"
            elif issubclass(paramdef_field.display_type, int):
                field_type_name = "int"
            elif display_type_name in {"f32", "f64"}:
                field_type_name = "float"
            else:
                raise TypeError(display_type_name)

            if paramdef_field.bit_count != -1:
                field_args.append(f"bit_count={paramdef_field.bit_count}")

            if "default" in info:
                default = info["default"]
            else:
                default = paramdef_field.default
                if field_type_name == "int":
                    default = int(default)  # always stored in ParamDef as float
                elif field_type_name == "bool":
                    default = bool(default)
            field_args.append(f"default={repr(default)}")

            if "dynamic_callback" in info:
                dynamic_imports.append(info["dynamic_callback"].split("(")[0])
                field_args.append(f"dynamic_callback={info['dynamic_callback']}")

            nickname = info["nickname"]
            args = ", ".join(field_args)
            tooltip = info["tooltip"]
            if len(tooltip) < 100:
                tooltip_lines = [tooltip]
            else:
                tooltip_lines = textwrap.wrap(tooltip, 100)
            args += f",\n{ind}tooltip=\"{tooltip_lines[0]}"  # no closing quote
            for line in tooltip_lines[1:]:
                args += f" \"\n{ind}{ind}\"{line}"
            args += "\""
            line = f"    {nickname}: {field_type_name} = ParamField(\n{ind}{args},\n    )"

            lines.append(line)

        cls_string = "\n".join(lines)

        if param_enums_used:
            # Import param enums.
            import_lines.insert(5, f"from soulstruct.{game_submodule}.params.enums import *")
        if game_types_used:
            # Import game types.
            import_lines.insert(5, f"from soulstruct.{game_submodule}.game_types import *")

        if dynamic_imports:
            dynamic_imports_sorted = sorted(set(dynamic_imports))
            import_lines.extend(["", f"from .dynamics import {', '.join(dynamic_imports_sorted)}"])

        module_text = "\n".join(import_lines) + "\n\n\n" + cls_string + "\n"

        if game_submodule == "darksouls1r" and paramdef_stem not in DSR_PARAMDEFS:
            # This ParamDef is identical to PTDE, which we import and use for DS1R.
            # (We still created the module above to validate it.)
            continue

        (paramdef_dir / f"{paramdef_stem}.py").write_text(module_text)

    # We don't rewrite partial enums!
    if not only_paramdefs and not no_enums:

        # Write enums.
        enum_module_text = "from soulstruct.base.params.paramdef.field_types import *"
        for display_name, internal_name in all_enums.items():
            enum_module_text += f"\n\n\nclass {display_name}({internal_name}):\n    pass"
        enum_module_text += "\n"

        # Enums are written to the `params` parent directory.
        (paramdef_dir / "../enums.py").write_text(enum_module_text)


def modify_paramdef_info(game_submodule: str):
    """Transient functions to edit JSON."""
    paramdef_dir = SOULSTRUCT_PATH(f"{game_submodule}/params/paramdef")
    json_path = paramdef_dir / "paramdef_info.json"
    paramdef_info = read_json(json_path)

    # Set some dynamic game types.
    chara_init_param_info = paramdef_info["CHARACTER_INIT_PARAM"]
    armor_suffixes = {"Helm", "Armer", "Gaunt", "Leg"}
    ammo_suffixes = {"Arrow", "Bolt", "SubArrow", "SubBolt"}
    for key, info in chara_init_param_info.items():
        if "_Wep_" in key or "_Subwep_" in key:
            info["game_type"] = "WeaponParam"
        elif key.split("_")[-1] in armor_suffixes:
            info["game_type"] = "ArmorParam"
        elif key.split("_")[-1] in ammo_suffixes:
            info["game_type"] = "WeaponParam"
        elif "_Accessory" in key:
            info["game_type"] = "AccessoryParam"
        elif "_Spell_" in key:
            info["game_type"] = "SpellParam"
        elif key.startswith("item_"):
            info["game_type"] = "GoodParam"

    write_json(json_path, paramdef_info, indent=4)


def create_for_game(game_module_name: str):
    game = get_game(game_module_name)
    paramdef_module = game.import_game_submodule("params", "paramdef")
    _paramdefbnd = paramdef_module.ParamDefBND.from_bundled(game_module_name)
    update_paramdef_info(_paramdefbnd, game_module_name)
    modify_paramdef_info(game_module_name)
    create_game_classes(_paramdefbnd, game_module_name)


def create_for_elden_ring():
    """Uses Elden Ring's"""
    from soulstruct.eldenring.params.paramdef import ParamDefBND
    _paramdefbnd = ParamDefBND.from_bundled("eldenring")
    update_paramdef_info(_paramdefbnd, "eldenring")
    modify_paramdef_info("eldenring")
    create_game_classes(_paramdefbnd, "eldenring")


if __name__ == '__main__':
    create_for_game("bloodborne")
