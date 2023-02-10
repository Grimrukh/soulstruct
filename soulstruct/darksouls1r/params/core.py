from __future__ import annotations

__all__ = ["Param", "GameParamBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.games import DARK_SOULS_DSR
from soulstruct.bloodborne.game_types import *
from soulstruct.containers import BinderVersion
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.base.params.param import Param as _BaseParam
from soulstruct.utilities.misc import BiDict
from soulstruct.darksouls1ptde.constants import PLAYER_WEAPON_BEHAVIOR_VARIATIONS, BEHAVIOR_SUB_ID

from .paramdef import GET_BUNDLED_PARAMDEFBND

if tp.TYPE_CHECKING:
    from ..text.msg_directory import MSGDirectory


@dataclass(slots=True)
class Param(_BaseParam):
    GET_BUNDLED_PARAMDEFBND = staticmethod(GET_BUNDLED_PARAMDEFBND)


@dataclass(slots=True)
class GameParamBND(_BaseGameParamBND):
    Param: tp.ClassVar = Param

    PARAM_NICKNAMES: tp.ClassVar = BiDict(
        ("AtkParam_Npc", "NonPlayerAttacks"),
        ("AtkParam_Pc", "PlayerAttacks"),
        ("BehaviorParam", "NonPlayerBehaviors"),
        ("BehaviorParam_PC", "PlayerBehaviors"),
    )

    dcx_type = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    AI = param_property("AI")  # type: Param
    Armor = param_property("Armor")  # type: Param
    ArmorUpgrades = param_property("ArmorUpgrades")  # type: Param
    Bosses = param_property("Bosses")  # type: Param
    Bullets = param_property("Bullets")  # type: Param
    Cameras = param_property("Cameras")  # type: Param
    Characters = param_property("Characters")  # type: Param
    Dialogue = param_property("Dialogue")  # type: Param
    Faces = param_property("Faces")  # type: Param
    Goods = param_property("Goods")  # type: Param
    GrowthCurves = param_property("GrowthCurves")  # type: Param
    ItemLots = param_property("ItemLots")  # type: Param
    NonPlayerAttacks = param_property("NonPlayerAttacks")  # type: Param
    NonPlayerBehaviors = param_property("NonPlayerBehaviors")  # type: Param
    MenuColors = param_property("MenuColors")  # type: Param
    Movement = param_property("Movement")  # type: Param
    Objects = param_property("Objects")  # type: Param
    ObjectActivations = param_property("ObjectActivations")  # type: Param
    Players = param_property("Players")  # type: Param
    PlayerAttacks = param_property("PlayerAttacks")  # type: Param
    PlayerBehaviors = param_property("PlayerBehaviors")  # type: Param
    Rings = param_property("Rings")  # type: Param
    Shops = param_property("Shops")  # type: Param
    SpecialEffects = param_property("SpecialEffects")  # type: Param
    SpecialEffectVisuals = param_property("SpecialEffectVisuals")  # type: Param
    Spells = param_property("Spells")  # type: Param
    Terrains = param_property("Terrains")  # type: Param
    Throws = param_property("Throws")  # type: Param
    UpgradeMaterials = param_property("UpgradeMaterials")  # type: Param
    Weapons = param_property("Weapons")  # type: Param
    WeaponUpgrades = param_property("WeaponUpgrades")  # type: Param

    # Also defines display order.
    PARAM_TYPES: tp.ClassVar = {
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
        "Rings": AccessoryParam,
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

    def better_debug_player(self):
        """Set the default debug player param (9000) to something better."""
        debug_player = self.Players[9000]
        debug_player.update(
            equip_Wep_Right=500010,  # Uchigatana +10
            equip_Subwep_Right=1201010,  # Longbow +10
            equip_Wep_Left=1457000,  # Dragon Crest Shield
            equip_Subwep_Left=1300000,  # Sorcerer's Catalyst
            equip_Helm=300000,  # Thief Set
            equip_Armer=301000,
            equip_Gaunt=302000,
            equip_Leg=303000,
            equip_Arrow=2002000,  # Feather Arrow
            equip_Bolt=-1,
            equip_SubArrow=-1,
            equip_SubBolt=-1,
            equip_Accessory01=100,  # Havel's Ring
            equip_Accessory02=138,  # Covenant of Artorias
            equip_Accessory03=-1,
            equip_Accessory04=-1,
            equip_Accessory05=-1,
            equip_Spell_01=3010,  # Great Soul Arrow
            equip_Spell_02=3070,  # Crystal Soul Spear
            equip_Spell_03=3210,  # Crystal Magic Weapon
            equip_Spell_04=3500,  # Cast Light
            equip_Spell_05=3550,  # Chameleon
            equip_Spell_06=-1,
            equip_Spell_07=-1,
            item_01=201,  # Estus Flask
            item_02=500,  # Humanity
            item_03=240,  # Divine Blessing
            item_04=-1,
            item_05=-1,
            item_06=-1,
            item_07=-1,
            item_08=-1,
            item_09=-1,
            item_10=-1,
            arrowNum=999,
            boltNum=0,
            subArrowNum=0,
            subBoltNum=0,
            itemNum_01=5,
            itemNum_02=99,
            itemNum_03=99,
            itemNum_04=0,
            itemNum_05=0,
            itemNum_06=0,
            itemNum_07=0,
            itemNum_08=0,
            itemNum_09=0,
            itemNum_10=0,
            npcPlayerSex=0,  # Female
        )
