__all__ = ["AI", "Animation", "Flag", "Model", "Texture", "VisualEffect", "Params", "Sound", "Text"]

# Overrides for certain basic enums.
ATK_PARAM_HIT_SOURCE = int
SP_EFFECT_SPCATEGORY = int


class AI:
    Logic = "<AI:Logic>"
    Battle = "<AI:Battle>"


class Params:
    AI = "<Params:AI>"
    Armor = "<Params:Armor>"
    ArmorUpgrades = "<Params:ArmorUpgrades>"
    Attacks = "<Params:Attacks>"  # links to both Human and Non Human Attacks are provided
    Behaviors = "<Params:Behaviors>"  # links to both Human and Non Human Behaviors are provided
    Bosses = "<Params:Bosses>"
    Bullets = "<Params:Bullets>"
    Cameras = "<Params:Cameras>"
    Conversations = "<Params:Conversations>"
    Faces = "<Params:Faces>"
    Goods = "<Params:Goods>"
    ItemLots = "<Params:ItemLots>"
    Knockback = "<Params:Knockback>"
    LevelSyncCorrect = "<Params:LevelSyncCorrect>"
    Movement = "<Params:Movement>"
    Rings = "<Params:Rings>"
    SpecialEffects = "<Params:SpecialEffects>"
    Spells = "<Params:Spells>"
    Terrains = "<Params:Terrains>"
    SpecialEffectVisuals = "<Params:SpecialEffectVisuals>"
    UpgradeMaterials = "<Params:UpgradeMaterials>"
    Weapons = "<Params:Weapons>"
    WeaponUpgrades = "<Params:WeaponUpgrades>"


class Sound:
    SFX = "<Sound:SFX>"
    Voice = "<Sound:Voice>"


class Text:
    Conversations = "<Text:Conversations>"
    EventText = "<Text:EventText>"
    NPCNames = "<Text:NPCNames>"


Animation = "<Animation>"
Flag = "<Flag>"
Model = "<Model>"
Texture = "<Texture>"
VisualEffect = "<VisualEffect>"
