from __future__ import annotations

__all__ = ["ParamRow", "Param", "GameParamBND"]

import typing as tp

from soulstruct.bnd import BND3
from soulstruct.games import DARK_SOULS_PTDE
from soulstruct.game_types import *
from soulstruct.models.darksouls1 import BEHAVIOR_SUB_ID, PLAYER_WEAPON_BEHAVIOR_VARIATIONS
from soulstruct.params.base.param import ParamRow as _BaseParamRow, Param as _BaseParam
from soulstruct.params.base.game_param_bnd import GameParamBND as _BaseGameParamBND

from . import enums
from .paramdef import ParamDefBND

if tp.TYPE_CHECKING:
    from soulstruct.text.darksouls1 import MSGDirectory


class ParamRow(_BaseParamRow):
    def get_field_type(self, field_type_name: str):
        """Look for field type in game-specific appropriate `enums` module."""
        return getattr(enums, field_type_name)


class Param(_BaseParam):
    ParamRow = ParamRow


class GameParamBND(_BaseGameParamBND, BND3):
    Param = Param
    GAME = DARK_SOULS_PTDE
    ParamDefBND = ParamDefBND

    PARAM_NICKNAMES = {
        "AtkParam_Npc": "NonPlayerAttacks",
        "AtkParam_Pc": "PlayerAttacks",
        "BehaviorParam": "NonPlayerBehaviors",
        "BehaviorParam_PC": "PlayerBehaviors",
    }

    AI: Param
    Armor: Param
    ArmorUpgrades: Param
    Bosses: Param
    Bullets: Param
    Cameras: Param
    Characters: Param
    Dialogue: Param
    Faces: Param
    Goods: Param
    GrowthCurves: Param
    ItemLots: Param
    NonPlayerAttacks: Param
    NonPlayerBehaviors: Param
    MenuColors: Param
    Movement: Param
    Objects: Param
    ObjectActivations: Param
    Players: Param
    PlayerAttacks: Param
    PlayerBehaviors: Param
    Rings: Param
    Shops: Param
    SpecialEffects: Param
    SpecialEffectVisuals: Param
    Spells: Param
    Terrains: Param
    Throws: Param
    UpgradeMaterials: Param
    Weapons: Param
    WeaponUpgrades: Param

    # Also defines display order.
    PARAM_TYPES = {
        "Players": PlayerParam,
        "Characters": CharacterParam,
        "PlayerBehaviors": BehaviorParam,
        "PlayerAttacks": AttackParam,
        "NonPlayerBehaviors": BehaviorParam,
        "NonPlayerAttacks": AttackParam,
        "AI": AIParam,
        "Bullets": BulletParam,
        "Throws": ThrowParam,
        "SpecialEffects": SpecialEffectParam,
        "Weapons": WeaponParam,
        "Armor": ArmorParam,
        "Rings": RingParam,
        "Goods": GoodParam,
        "WeaponUpgrades": WeaponUpgradeParam,
        "ArmorUpgrades": ArmorUpgradeParam,
        "UpgradeMaterials": UpgradeMaterialParam,
        "ItemLots": ItemLotParam,
        "Bosses": BossParam,
        "Shops": ShopParam,
        "Spells": SpellParam,
        "Objects": ObjectParam,
        "ObjectActivations": ObjActParam,
        "Movement": MovementParam,
        "Cameras": CameraParam,
        "Terrains": TerrainParam,
        "Faces": FaceParam,
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,
    }

    def rename_entries_from_text(self, text: MSGDirectory, param_nickname=None):
        """Rename item param entries according to their (presumably more desirable) names in DS1 Text data.

        Args:
            text (MSGDirectory): text data structure to pull names from.
            param_nickname (str or None): specific ParamTable name to rename, or None to rename all (default).
                Valid names are "Weapons", "Armor", "Rings", "Goods", and "Spells" (or None).
        """
        if param_nickname:
            param_nickname = param_nickname.lower().rstrip("s")
            if param_nickname not in {"weapon", "armor", "ring", "good", "spell"}:
                raise ValueError(
                    f"Invalid item type: {param_nickname}. Must be 'Weapons', 'Armor', 'Rings', "
                    f"'Goods', or 'Spells'."
                )
        for item_type_check, param_table, text_dict in zip(
            ("weapon", "armor", "ring", "good", "spell"),
            (self.Weapons, self.Armor, self.Rings, self.Goods, self.Spells),
            (text.WeaponNames, text.ArmorNames, text.RingNames, text.GoodNames, text.SpellNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                for param_id, param_entry in param_table.items():
                    if param_id in text_dict:
                        param_entry.name = text_dict[param_id]

    def print_hitbox_info(self):
        current_var_id = None
        for b_id, b_entry in self.PlayerBehaviors.items():
            if b_id > 100000:
                if current_var_id != b_entry["variationId"]:
                    current_var_id = b_entry["variationId"]
                    print(f"{PLAYER_WEAPON_BEHAVIOR_VARIATIONS[current_var_id]} ({current_var_id})")
                sub_id = b_entry["behaviorJudgeId"]
                sub_name = BEHAVIOR_SUB_ID.get(sub_id, "UNKNOWN")
                if b_entry["refType"] == 0:
                    attack_id = b_entry["refId"]
                    try:
                        attack_param = self.PlayerAttacks[b_entry["refId"]]
                    except KeyError:
                        print(f"    {sub_id}: {sub_name} -> Attack {attack_id} (DOES NOT EXIST!)")
                        continue
                    print(f"    {sub_id}: {sub_name} -> Attack {attack_id}")
                    for i in range(4):
                        start_point = attack_param[f"hit{i}_DmyPoly1"]
                        if start_point != -1:
                            end_point = attack_param[f"hit{i}_DmyPoly2"]
                            radius = attack_param[f"hit{i}_Radius"]
                            print(f"         {i}. R = {radius:.3f}")
                            print(f"         {i}. Dmy = ({start_point}, {end_point})")
