from __future__ import annotations

__all__ = ["Param", "GameParamBND"]

from pathlib import Path

from soulstruct.containers.bnd import BND4
from soulstruct.containers.dcx import decompress
from soulstruct.games import ELDEN_RING
from soulstruct.game_types import *
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND
from soulstruct.base.params.param import Param as _BaseParam
from soulstruct.utilities.binary import BinaryReader, BinaryWriter

from .paramdef import ParamDefBND, GET_BUNDLED_PARAMDEFBND

# if tp.TYPE_CHECKING:
#     from ..text.msg_directory import MSGDirectory


class Param(_BaseParam):
    GET_BUNDLED_PARAMDEFBND = staticmethod(GET_BUNDLED_PARAMDEFBND)


class GameParamBND(_BaseGameParamBND, BND4):
    Param = Param
    ParamDefBND = ParamDefBND

    PARAM_NICKNAMES = {
        "AtkParam_Npc": "NonPlayerAttacks",
        "AtkParam_Pc": "PlayerAttacks",
        "BehaviorParam": "NonPlayerBehaviors",
        "BehaviorParam_PC": "PlayerBehaviors",

        # TODO: Placing all undocumented new tables here for now.
        # TODO: Add new Elden Ring tables and remove unused Bloodborne ones.
        "ActionButtonParam": "ActionButtons",
        "AiSoundParam": "AISounds",
        "CharMakeMenuListItemParam": "CharacterCreationMenuItems",
        "CharMakeMenuTopParam": "CharacterCreationMenuTop",
        "DecalParam": "Decals",
        "DungeonFeatureParam": "DungeonFeatures",
        "DungeonSubFeatLotParam": "DungeonSubFeatureLots",
        "FaceGenParam": "FaceGenerators",
        "FaceParam": "Faces",
        "FaceRangeParam": "FaceRanges",
        "GameMapParam": "GameMaps",
        "GemCategoryParam": "GemCategories",
        "GemDropDopingParam": "GemDropDoping",
        "GemDropModifyParam": "GemDropModifications",
        "GemeffectParam": "GemEffects",
        "GemGenParam": "GemsAndRunes",
        "HolygrailExParam": "RitualChalices",
        "ItemLotLvdepParam": "ItemLotsWithScaling",
        "MenuPropertyLayoutParam": "MenuPropertyLayouts",
        "MenuPropertySpecParam": "MenuPropertySpecs",
        "MenuValueTableSpecParam": "MenuValueTableSpecs",
        "ProtectorGenParam": "ArmorGenerators",
        "ResidentVFXParam": "ResidentVFX",
        "ReturnPointParam": "ReturnPoints",
        "RitualRequiredMatParam": "RitualMaterials",
        "WeaponGenParam": "WeaponGenerators",
        "WindParam": "Wind",
    }

    # Maps attribute names to game types. Also defines display order.
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
        "Faces": FaceParam,  # TODO: different for BB? FaceGenerators?
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,

        # TODO: Create param types for these new BB params. Some are currently disabled.
        "ActionButtons": None,
        "AISounds": None,
        # "CharacterCreationMenuItems": None,
        # "CharacterCreationMenuTop": None,
        "Decals": None,
        "DungeonFeatures": None,
        # "DungeonSubFeatureLots": None,
        "FaceGenerators": None,
        "FaceRanges": None,
        "GameMaps": None,
        "GemCategories": None,
        "GemDropDoping": None,
        "GemDropModifications": None,
        "GemEffects": None,
        "GemsAndRunes": None,
        "RitualChalices": None,
        # "ItemLotsWithScaling": None,
        # "MenuPropertyLayouts": None,
        # "MenuPropertySpecs": None,
        # "MenuValueTableSpecs": None,
        # "ArmorGenerators": None,
        "ResidentVFX": None,
        "ReturnPoints": None,
        "RitualMaterials": None,
        "WeaponGenerators": None,
        "Wind": None,
    }

    # TODO: Some of these may be Dark Souls junk (like Rings).
    ActionButtons: Param
    AI: Param
    AISounds: Param
    Armor: Param
    ArmorGenerators: Param
    ArmorUpgrades: Param
    Bosses: Param
    Bullets: Param
    Cameras: Param
    Characters: Param
    CharacterCreationMenuItems: Param
    CharacterCreationMenuTop: Param
    Decals: Param
    Dialogue: Param
    DungeonFeatures: Param
    DungeonSubFeatureLots: Param
    FaceGenerators: Param
    FaceRanges: Param
    Faces: Param
    GameMaps: Param
    GemCategories: Param
    GemDropDoping: Param
    GemDropModifications: Param
    GemEffects: Param
    GemsAndRunes: Param
    Goods: Param
    GrowthCurves: Param
    ItemLots: Param
    ItemLotsWithScaling: Param
    NonPlayerAttacks: Param
    NonPlayerBehaviors: Param
    MenuColors: Param
    MenuPropertyLayouts: Param
    MenuPropertySpecs: Param
    MenuValueTableSpecs: Param
    Movement: Param
    Objects: Param
    ObjectActivations: Param
    Players: Param
    PlayerAttacks: Param
    PlayerBehaviors: Param
    ResidentVFX: Param  # TODO: possibly `PlayerVFX`
    ReturnPoints: Param  # TODO: ?
    # Rings: Param
    RitualChalices: Param
    RitualMaterials: Param
    Shops: Param
    SpecialEffects: Param
    SpecialEffectVisuals: Param
    Spells: Param
    Terrains: Param
    Throws: Param
    UpgradeMaterials: Param
    Weapons: Param
    WeaponGenerators: Param
    WeaponUpgrades: Param
    Wind: Param

    REGULATION_KEY = (  # 128-bit key
        b"\x99\xBF\xFC\x36\x6A\x6B\xC8\xC6\xF5\x82\x7D\x09\x36\x02\xD6\x76"
        b"\xC4\x28\x92\xA0\x1C\x20\x7F\xB0\x24\xD3\xAF\x4E\x49\x3F\xEF\x99"
    )

    def __init__(self, gameparambnd_source=None, paramdef_bnd=None):
        # TODO: Detect and decrypt `regulation.bin`.
        if isinstance(gameparambnd_source, (str, Path)):
            if Path(gameparambnd_source).name == "regulation.bin":
                gameparambnd_source = self.decrypt_regulation_bin(Path(gameparambnd_source).read_bytes())
        elif isinstance(gameparambnd_source, bytes) and gameparambnd_source[:4] != b"BND4":
            # Assume source is `regulation.bin` bytes.
            gameparambnd_source = self.decrypt_regulation_bin(gameparambnd_source)

        super().__init__(gameparambnd_source, paramdef_bnd=ELDEN_RING if paramdef_bnd is None else paramdef_bnd)

    def decrypt_regulation_bin(self, data: bytes) -> bytes:
        try:
            # noinspection PyPackageRequirements
            from aespython import key_expander, aes_cipher, cbc_mode
        except ImportError:
            raise ModuleNotFoundError(f"Cannot decrypt `regulation.bin` for Elden Ring without `aespython` package.")

        iv = data[:16]
        encrypted = BinaryReader(data)

        key_expander_256 = key_expander.KeyExpander(256)
        expanded_key = key_expander_256.expand(bytearray(self.REGULATION_KEY))
        aes_cipher_256 = aes_cipher.AESCipher(expanded_key)
        aes_cbc_256 = cbc_mode.CBCMode(aes_cipher_256, 16)
        aes_cbc_256.set_iv(iv)

        decrypted = b""

        while True:
            chunk = encrypted.read(16)
            if len(chunk) == 0:  # end of file
                break
            decrypted_chunk = bytearray(aes_cbc_256.decrypt_block(list(bytearray(chunk))))
            decrypted += decrypted_chunk
            # print(f"{len(decrypted)}")

        with open("regulation.bin.decrypted", "wb") as f:
            f.write(decrypted)
        with open("regulation.bin.decryptednodcx", "wb") as f:
            f.write(decompress(decrypted[16:])[0])

        return decrypted

    def rename_entries_from_text(self, text: MSGDirectory, param_nickname=None):
        """Rename item param entries according to their (presumably more desirable) names in Bloodborne text data.

        Many Bloodborne names (mainly for cut stuff) use a single asterisk as a placeholder. Such names are ignored by
        this method.

        TODO: 'GemsAndRunes' uses some kind of text ID offset param field.

        Args:
            text (MSGDirectory): text data structure to pull names from.
            param_nickname (str or None): specific ParamTable name to rename, or None to rename all (default).
                Valid names are "Weapons", "Armor", "Goods", and "GemsAndRunes" (or None to do all).
        """
        if param_nickname:
            param_nickname = param_nickname.lower().rstrip("s")
            if param_nickname not in {"weapon", "armor", "good", "gemsandrune"}:
                raise ValueError(
                    f"Invalid item type: {param_nickname}. Must be 'Weapons', 'Armor', 'Goods', or 'GemsAndRunes'."
                )
        for item_type_check, param_table, text_dict in zip(
            ("weapon", "armor", "good", "gemsandrune"),
            (self.Weapons, self.Armor, self.Goods, self.GemsAndRunes),
            (text.WeaponNames, text.ArmorNames, text.GoodNames, text.BloodGemNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                for param_id, param_entry in param_table.items():
                    if param_id in text_dict and text_dict[param_id].strip(" *"):
                        param_entry.name = text_dict[param_id]
