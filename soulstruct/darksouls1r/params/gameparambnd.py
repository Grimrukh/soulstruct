from __future__ import annotations

__all__ = ["GameParamBND"]

import typing as tp
from dataclasses import dataclass

from soulstruct.games import DARK_SOULS_DSR
from soulstruct.darksouls1r.game_types import *
from soulstruct.containers import BinderVersion
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.base.params.param import Param
from soulstruct.utilities.misc import BiDict
from soulstruct.darksouls1ptde.constants import PLAYER_WEAPON_BEHAVIOR_VARIATIONS, BEHAVIOR_SUB_ID

from . import paramdef
from .paramdef import *

if tp.TYPE_CHECKING:
    from ..text.msg_directory import MSGDirectory


@dataclass(slots=True)
class GameParamBND(_BaseGameParamBND):

    PARAMDEF_MODULE: tp.ClassVar = paramdef

    PARAM_NICKNAMES: tp.ClassVar = BiDict(
        ("AtkParam_Npc", "NonPlayerAttacks"),
        ("AtkParam_Pc", "PlayerAttacks"),
        ("BehaviorParam", "NonPlayerBehaviors"),
        ("BehaviorParam_PC", "PlayerBehaviors"),
        ("Bullet", "Bullets"),
        ("CalcCorrectGraph", "GrowthCurves"),
        ("CharaInitParam", "Players"),
        ("CoolTimeParam", "CoolTime"),
        ("default_AIStandardInfoBank", "DefaultAIStandardInfo"),
        ("default_EnemyBehaviorBank", "DefaultEnemyBehaviors"),
        ("EquipParamProtector", "Armor"),
        ("EquipMtrlSetParam", "UpgradeMaterials"),
        ("EquipParamAccessory", "Rings"),
        ("EquipParamGoods", "Goods"),
        ("EquipParamWeapon", "Weapons"),
        ("FaceGenParam", "FaceGenerators"),
        ("GameAreaParam", "Bosses"),
        ("HitMtrlParam", "Terrains"),
        ("ItemLotParam", "ItemLots"),
        ("KnockBackParam", "Knockbacks"),
        ("LevelSyncParam", "LevelSync"),
        ("LockCamParam", "Cameras"),
        ("Magic", "Spells"),
        ("MenuColorTableParam", "MenuColors"),
        ("MoveParam", "Movement"),
        ("NpcParam", "Characters"),
        ("NpcThinkParam", "AI"),
        ("ObjActParam", "ObjectActivations"),
        ("ObjectParam", "Objects"),
        ("QwcChange", "WorldTendencyChange"),
        ("QwcJudge", "WorldTendencyJudgement"),
        ("RagdollParam", "Ragdolls"),
        ("ReinforceParamProtector", "ArmorUpgrades"),
        ("ReinforceParamWeapon", "WeaponUpgrades"),
        ("ShopLineupParam", "Shops"),
        ("SkeletonParam", "Skeletons"),
        ("SpEffectParam", "SpecialEffects"),
        ("SpEffectVfxParam", "SpecialEffectVisuals"),
        ("TalkParam", "Dialogue"),
        ("ThrowParam", "Throws"),
        ("WhiteCoolTimeParam", "WhiteCoolTime"),
    )

    dcx_type = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    AI = param_property("NpcThinkParam")  # type: Param[NPC_THINK_PARAM_ST]
    Armor = param_property("EquipParamProtector")  # type: Param[EQUIP_PARAM_PROTECTOR_ST]
    ArmorUpgrades = param_property("ReinforceParamProtector")  # type: Param[REINFORCE_PARAM_PROTECTOR_ST]
    Bosses = param_property("GameAreaParam")  # type: Param[GAME_AREA_PARAM_ST]
    Bullets = param_property("Bullet")  # type: Param[BULLET_PARAM_ST]
    Cameras = param_property("LockCamParam")  # type: Param[LOCK_CAM_PARAM_ST]
    Characters = param_property("NpcParam")  # type: Param[NPC_PARAM_ST]
    CoolTime = param_property("CoolTimeParam")  # type: Param[COOL_TIME_PARAM_ST]
    DefaultAIStandardInfo = param_property("default_AIStandardInfoBank")  # type: Param[AI_STANDARD_INFO_BANK]
    DefaultEnemyBehaviors = param_property("default_EnemyBehaviorBank")  # type: Param[ENEMY_STANDARD_INFO_BANK]
    Dialogue = param_property("TalkParam")  # type: Param[TALK_PARAM_ST]
    FaceGenerators = param_property("FaceGenParam")  # type: Param[FACE_PARAM_ST]
    Goods = param_property("EquipParamGoods")  # type: Param[EQUIP_PARAM_GOODS_ST]
    GrowthCurves = param_property("CalcCorrectGraph")  # type: Param[CACL_CORRECT_GRAPH_ST]
    ItemLots = param_property("ItemLotParam")  # type: Param[ITEMLOT_PARAM_ST]
    Knockbacks = param_property("KnockBackParam")  # type: Param[KNOCKBACK_PARAM_ST]
    LevelSync = param_property("LevelSyncParam")  # type: Param[LEVELSYNC_PARAM_ST]
    NonPlayerAttacks = param_property("AtkParam_Npc")  # type: Param[ATK_PARAM_ST]
    NonPlayerBehaviors = param_property("BehaviorParam")  # type: Param[BEHAVIOR_PARAM_ST]
    MenuColors = param_property("MenuColorTableParam")  # type: Param[MENU_PARAM_COLOR_TABLE_ST]
    Movement = param_property("MoveParam")  # type: Param[MOVE_PARAM_ST]
    Objects = param_property("ObjectParam")  # type: Param[OBJECT_PARAM_ST]
    ObjectActivations = param_property("ObjActParam")  # type: Param[OBJ_ACT_PARAM_ST]
    Players = param_property("CharaInitParam")  # type: Param[CHARACTER_INIT_PARAM]
    PlayerAttacks = param_property("AtkParam_Pc")  # type: Param[ATK_PARAM_ST]
    PlayerBehaviors = param_property("BehaviorParam_PC")  # type: Param[BEHAVIOR_PARAM_ST]
    Ragdolls = param_property("RagdollParam")  # type: Param[RAGDOLL_PARAM_ST]
    Rings = param_property("EquipParamAccessory")  # type: Param[EQUIP_PARAM_ACCESSORY_ST]
    Shops = param_property("ShopLineupParam")  # type: Param[SHOP_LINEUP_PARAM]
    Skeletons = param_property("SkeletonParam")  # type: Param[SKELETON_PARAM_ST]
    SpecialEffects = param_property("SpEffectParam")  # type: Param[SP_EFFECT_PARAM_ST]
    SpecialEffectVisuals = param_property("SpEffectVfxParam")  # type: Param[SP_EFFECT_VFX_PARAM_ST]
    Spells = param_property("Magic")  # type: Param[MAGIC_PARAM_ST]
    Terrains = param_property("HitMtrlParam")  # type: Param[HIT_MTRL_PARAM_ST]
    Throws = param_property("ThrowParam")  # type: Param[THROW_INFO_BANK]
    UpgradeMaterials = param_property("EquipMtrlSetParam")  # type: Param[EQUIP_MTRL_SET_PARAM_ST]
    Weapons = param_property("EquipParamWeapon")  # type: Param[EQUIP_PARAM_WEAPON_ST]
    WeaponUpgrades = param_property("ReinforceParamWeapon")  # type: Param[REINFORCE_PARAM_WEAPON_ST]
    WhiteCoolTime = param_property("WhiteCoolTimeParam")  # type: Param[WHITE_COOL_TIME_PARAM_ST]
    WorldTendencyChange = param_property("QwcChange")  # type: Param[QWC_CHANGE_PARAM_ST]
    WorldTendencyJudgement = param_property("QwcJudge")  # type: Param[QWC_JUDGE_PARAM_ST]

    # Also defines display order/presence.
    GAME_TYPES: tp.ClassVar = {
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
        "FaceGenerators": FaceGenParam,
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,
    }

    GET_BUNDLED_PARAMDEFBND: tp.ClassVar[tp.Callable] = GET_BUNDLED_PARAMDEFBND

    @classmethod
    def get_default_entry_path(cls, entry_name: str) -> str:
        return f"N:\\FRPG\\data\\INTERROOT_x64\\param\\GameParam\\{entry_name}"

    def rename_entries_from_text(self, text: MSGDirectory, param_nickname: str = None):
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
                    f"Invalid `param_nickname`: {param_nickname}. Must be 'Weapons', 'Armor', 'Rings', "
                    f"'Goods', or 'Spells'."
                )
        for item_type_check, param, text_fmg in zip(
            ("weapon", "armor", "ring", "good", "spell"),
            (self.Weapons, self.Armor, self.Rings, self.Goods, self.Spells),
            (text.WeaponNames, text.ArmorNames, text.RingNames, text.GoodNames, text.SpellNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                print(f"Renaming {item_type_check} entries...")
                for param_id, param_row in param.items():
                    if param_id in text_fmg.entries:
                        param_row.Name = text_fmg.entries[param_id]

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
