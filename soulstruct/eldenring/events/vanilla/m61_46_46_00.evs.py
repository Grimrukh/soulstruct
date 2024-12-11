"""
Land of Shadow 11-11 NE SW

linked:
0
82

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: 
168: 
170: 
172: 
174: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from soulstruct.eldenring.game_types import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005870(0, character=2046460800, name=905210600, npc_threat_level=23)
    CommonFunc_90005860(0, flag=2046460800, left=0, character=2046460800, left_1=0, item_lot=30940, seconds=0.0)
    CommonFunc_90005872(0, character=2046460800, npc_threat_level=23, right=2046462802)
    Event_2046462814()
    Event_2046462811()
    Event_2046462815()
    Event_2046462816()
    Event_2046462830()
    Event_2046462817(0, character=2046460800)
    Event_2046462820(1, flag=2046462851, entity=2046463801)
    Event_2046462820(2, flag=2046462852, entity=2046463802)
    Event_2046462820(3, flag=2046462853, entity=2046463803)
    Event_2046462820(4, flag=2046462854, entity=2046463804)
    Event_2046462820(5, flag=2046462855, entity=2046463805)
    Event_2046462820(6, flag=2046462856, entity=2046463806)
    Event_2046462820(7, flag=2046462857, entity=2046463807)
    Event_2046462820(8, flag=2046462858, entity=2046463808)
    Event_2046462820(9, flag=2046462859, entity=2046463809)
    CommonFunc_90005301(0, flag=2046460290, character=2046460290, item_lot__unk1=2046460000, seconds=3.0, unk1=0)
    CommonFunc_90005557(0, entity=2046461680)
    CommonFunc_90005557(0, entity=2046461681)
    CommonFunc_90005557(0, entity=2046461682)
    CommonFunc_90005557(0, entity=2046461683)
    CommonFunc_90005557(0, entity=2046461684)
    CommonFunc_90005557(0, entity=2046461685)
    CommonFunc_90005557(0, entity=2046461686)
    CommonFunc_90005556(0, asset=2046461687, flag=2046467800)
    CommonFunc_90005638(0, flag=2046460500, asset=2046461500, asset_1=2046461501)


@RestartOnRest(2046462811)
def Event_2046462811():
    """Event 2046462811"""
    if FlagEnabled(20000800):
        return
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 20011220))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501000))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501001))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501002))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501003))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501004))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501005))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501006))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501007))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501008))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501009))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501010))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501011))
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 501012))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 20011246)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501000):
        AddSpecialEffect(2046460800, 20011221)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501001):
        AddSpecialEffect(2046460800, 20011222)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501002):
        AddSpecialEffect(2046460800, 20011223)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501003):
        AddSpecialEffect(2046460800, 20011224)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501004):
        AddSpecialEffect(2046460800, 20011225)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501005):
        AddSpecialEffect(2046460800, 20011226)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501006):
        AddSpecialEffect(2046460800, 20011227)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501007):
        AddSpecialEffect(2046460800, 20011228)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501008):
        AddSpecialEffect(2046460800, 20011229)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501009):
        AddSpecialEffect(2046460800, 20011230)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501010):
        AddSpecialEffect(2046460800, 20011231)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501011):
        AddSpecialEffect(2046460800, 20011232)
        Goto(Label.L0)
    if CharacterHasSpecialEffect(character=PLAYER, special_effect=501012):
        AddSpecialEffect(2046460800, 20011233)
        Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(5.0)
    Restart()


@RestartOnRest(2046462814)
def Event_2046462814():
    """Event 2046462814"""
    GotoIfFlagDisabled(Label.L0, flag=2046460800)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    RemoveSpecialEffect(PLAYER, 20004220)
    RemoveSpecialEffect(PLAYER, 20004221)
    RemoveSpecialEffect(PLAYER, 20004222)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    OR_1.Add(CharacterHasSpecialEffect(2046460800, 20011210))
    OR_1.Add(CharacterHasSpecialEffect(2046460800, 20011211))
    OR_1.Add(CharacterHasSpecialEffect(2046460800, 20011212))
    OR_1.Add(CharacterHasSpecialEffect(2046460800, 20011215))
    OR_1.Add(CharacterHasSpecialEffect(2046460800, 20011218))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2046462800))
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(PLAYER, 20004220)
    RemoveSpecialEffect(PLAYER, 20004221)
    RemoveSpecialEffect(PLAYER, 20004222)
    if CharacterHasSpecialEffect(character=2046460800, special_effect=20011210):
        SetWeather(weather=Weather.ScatteredRain, duration=1440.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004220)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=2046460800, special_effect=20011211):
        SetWeather(weather=Weather.HeavySnow, duration=1440.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004221)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=2046460800, special_effect=20011212):
        SetWeather(weather=Weather.PuffyClouds, duration=1440.0, immediate_change=False)
        AddSpecialEffect(PLAYER, 20004222)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=2046460800, special_effect=20011215):
        SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
        Goto(Label.L1)
    if CharacterHasSpecialEffect(character=2046460800, special_effect=20011218):
        SetWeather(weather=Weather.Fog, duration=1440.0, immediate_change=False)
        Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(3.0)
    Restart()


@RestartOnRest(2046462815)
def Event_2046462815():
    """Event 2046462815"""
    if FlagEnabled(2046460800):
        return
    
    MAIN.Await(HealthValue(2046460800) == 0)
    
    Kill(2046460811)
    Kill(2046460812)
    Kill(2046460813)
    Kill(2046460814)
    Kill(2046460815)
    Kill(2046460816)
    Kill(2046460817)
    Kill(2046460818)
    SetWeather(weather=Weather.Null, duration=-1.0, immediate_change=False)
    RemoveSpecialEffect(PLAYER, 20004220)
    RemoveSpecialEffect(PLAYER, 20004221)
    RemoveSpecialEffect(PLAYER, 20004222)
    End()


@ContinueOnRest(2046462816)
def Event_2046462816():
    """Event 2046462816"""
    if FlagEnabled(2046460800):
        return
    if FlagEnabled(2046462802):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2046460800, 20011239))
    
    EnableNetworkFlag(2046462802)
    End()


@RestartOnRest(2046462817)
def Event_2046462817(_, character: Character | int):
    """Event 2046462817"""
    GotoIfFlagDisabled(Label.L0, flag=2046460800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(2046462851)
    DisableFlag(2046462852)
    DisableFlag(2046462853)
    DisableFlag(2046462854)
    DisableFlag(2046462855)
    DisableFlag(2046462856)
    DisableFlag(2046462857)
    DisableFlag(2046462858)
    DisableFlag(2046462859)
    AND_1.Add(CharacterHasSpecialEffect(character, 20011217))
    AND_2.Add(CharacterInsideRegion(character=character, region=2046462800))
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)
    
    WaitRealFrames(frames=1)
    GotoIfCharacterOutsideRegion(Label.L1, character=character, region=2046462810)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462811, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462812, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462813, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462814, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462851)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfCharacterOutsideRegion(Label.L2, character=character, region=2046462820)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462821, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462822, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462823, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462824, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462852)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfCharacterOutsideRegion(Label.L3, character=character, region=2046462830)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462831, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462832, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462833, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462834, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462853)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfCharacterOutsideRegion(Label.L4, character=character, region=2046462840)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462841, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462842, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462843, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462844, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462854)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfCharacterOutsideRegion(Label.L5, character=character, region=2046462850)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462851, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462852, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462853, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462854, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462855)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfCharacterOutsideRegion(Label.L6, character=character, region=2046462860)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462861, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462862, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462863, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462864, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462856)
    Goto(Label.L10)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfCharacterOutsideRegion(Label.L7, character=character, region=2046462870)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462871, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462872, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462873, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462874, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462857)
    Goto(Label.L10)

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfCharacterOutsideRegion(Label.L8, character=character, region=2046462880)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462881, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462882, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462883, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462884, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462858)
    Goto(Label.L10)

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagDisabled(Label.L11, flag=2046462830)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462891, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462892, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462893, anchor_type=CoordEntityType.Region)
    CreateTemporaryVFX(vfx_id=653505, anchor_entity=2046462894, anchor_type=CoordEntityType.Region)
    EnableFlag(2046462859)

    # --- Label 11 --- #
    DefineLabel(11)
    Wait(1.0)
    Restart()


@RestartOnRest(2046462820)
def Event_2046462820(_, flag: Flag | int, entity: uint):
    """Event 2046462820"""
    GotoIfFlagDisabled(Label.L0, flag=2046460800)
    DisableSpawner(entity=entity)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableSpawner(entity=entity)
    
    MAIN.Await(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    EnableSpawner(entity=entity)
    Wait(5.0)
    DisableSpawner(entity=entity)
    Restart()


@RestartOnRest(2046462830)
def Event_2046462830():
    """Event 2046462830"""
    if FlagEnabled(2046460800):
        return
    DisableFlag(2046462830)
    AND_1.Add(CharacterHasSpecialEffect(2046460800, 20011217))
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=2046462890))
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(2046462830)
    Wait(3.0)
    Restart()


@RestartOnRest(2046462500)
def Event_2046462500():
    """Event 2046462500"""
    GotoIfFlagDisabled(Label.L0, flag=2046460500)
    DisableAsset(2046461500)
    DisableAsset(2046461501)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAssetInvulnerability(2046461501)
    
    MAIN.Await(AssetDestroyed(2046461500))
    
    DisableAssetInvulnerability(2046461501)
    WaitRealFrames(frames=1)
    DestroyAsset(2046461501, request_slot=0)
    EnableFlag(2046460500)
