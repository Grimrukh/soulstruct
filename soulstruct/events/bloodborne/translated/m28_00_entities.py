from soulstruct.game_types import *


class Flags(Flag):
    OneRebornDead = 12801800
    OneRebornFirstTimeDone = 12801802
    OneRebornFogEntered = 12804800
    OneRebornBattleStarted = 12804802
    OneRebornStunned = 12804808
    OneRebornPhaseTwo = 12804871


class Characters(Character):
    OneRebornMaiden1 = 2800520
    OneRebornMaiden2 = 2800522
    OneRebornMaiden3 = 2800524
    OneRebornMaiden4 = 2800525
    OneRebornMaiden5 = 2800527
    OneRebornMaiden6 = 2800529
    OneRebornMain = 2800800
    OneRebornHumanPart = 2800801
    OneRebornBulletCreator = 2800802
    OneRebornHealthPool = 2800803


class Objects(Object):
    OneRebornFog1 = 2801800
    OneRebornFog2 = 2801801


class FX(FXEvent):
    OneRebornFog1 = 2803800
    OneRebornFog2 = 2803801


class Cutscenes(IntEnum):
    OneRebornAppears = 28000000


class Effects(SpecialEffectParam):
    OneRebornStunned = 489
