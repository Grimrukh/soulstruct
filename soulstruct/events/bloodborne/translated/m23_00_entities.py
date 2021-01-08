from soulstruct.game_types import *


class Flags(Flag):
    DarkbeastPaarlDead = 12301700
    DarkbeastPaarlFirstTimeDone = 12301702
    DarkbeastPaarlFogEntered = 12304700
    DarkbeastPaarlBattleStartedForSummon = 12304701
    DarkbeastPaarlBattleStarted = 123047

    BloodStarvedBeastDead = 12301800
    BloodStarvedBeastFirstTimeDone = 12301802
    BloodStarvedBeastFogEntered = 12304800
    BloodStarvedBeastBattleStartedForSummon = 12304801
    BloodStarvedBeastBattleStarted = 12304802


class Characters(Character):
    BloodStarvedBeast = 2300800
    DarkbeastPaarl = 2300810


class Objects(Object):
    BossFog = 2301800
    OldYharnamLantern = 2301950
    BloodStarvedBeastLantern = 2301951
    DarkbeastPaarlLantern = 2301952


class Regions(Region):
    BloodStarvedBeastFirstTimeTrigger = 2302805


class VFX(VFXEvent):
    BossFog = 2303800
