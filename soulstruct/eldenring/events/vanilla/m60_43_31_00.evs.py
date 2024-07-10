"""
South Weeping Peninsula (NE) (NE)

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
from .enums.m60_43_31_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1043310000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76161,
        flag_1=76158,
        asset=Assets.AEG099_090_9001,
        source_flag=77110,
        value=3,
        flag_2=78110,
        flag_3=78111,
        flag_4=78112,
        flag_5=78113,
        flag_6=78114,
        flag_7=78115,
        flag_8=78116,
        flag_9=78117,
        flag_10=78118,
        flag_11=78119,
    )
    RegisterGrace(grace_flag=1043310001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=1043310002, asset=Assets.AEG099_060_9002)
    Event_1043312580()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9002, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005250(0, character=Characters.Misbegotten2, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten3, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten4, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten5, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten6, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310212, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310213, region=1043312200, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten0, region=1043312201, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten1, region=1043312201, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten8, region=1043312201, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten0, region=1043312201, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten2, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten3, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten4, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten5, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten6, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310212, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310213, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten0, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten1, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten8, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten0, region=1043312280, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310214, region=1043312218, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten9, region=1043312213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten10, region=1043312213, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten12, region=1043312218, seconds=0.0, animation_id=-1)
    Event_1043312443(0, character=Characters.Misbegotten9, region=1043312213)
    Event_1043312443(1, character=Characters.Misbegotten10, region=1043312213)
    Event_1043312443(2, character=Characters.Misbegotten12, region=1043312213)
    CommonFunc_90005250(0, character=Characters.Misbegotten11, region=1043312213, seconds=5.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten13, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310221, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten14, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten15, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten16, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten17, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310226, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten18, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten19, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.Misbegotten24, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=1043310246, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=1043310267, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=1043310268, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten1, region=1043312250, seconds=0.0, animation_id=-1)
    Event_1043312443(3, character=Characters.ScalyMisbegotten1, region=1043312250)
    CommonFunc_90005271(0, character=Characters.Misbegotten25, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(1, character=Characters.Misbegotten30, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(2, character=Characters.Misbegotten31, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Misbegotten26, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten27, region=1043312256, seconds=0.0, animation_id=3023)
    CommonFunc_90005250(0, character=1043310262, region=1043312262, seconds=1.0, animation_id=3031)
    Event_1043312443(4, character=1043310262, region=1043312262)
    CommonFunc_90005271(0, character=Characters.Misbegotten28, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.ScalyMisbegotten2, region=1043312285, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Misbegotten29, region=1043312285, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310270, region=1043312285, seconds=0.0, animation_id=-1)
    Event_1043312242(0, attacker__character=1043315240, region=1043312242)
    Event_1043312223(0, attacker__character=1043315223, region=1043312223)
    CommonFunc_90005250(0, character=1043310304, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310305, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310306, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310307, region=1043312220, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310311, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GodrickFootSoldier0, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GodrickFootSoldier1, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310314, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310315, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310316, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005271(0, character=Characters.GodrickSoldier0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GodrickSoldier1, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.GodrickSoldier2, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310357, region=1043312223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog0, region=1043312400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog1, region=1043312400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog2, region=1043312400, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog3, region=1043312403, seconds=0.0, animation_id=-1)
    CommonFunc_90005260(
        0,
        character=Characters.SmallerDog4,
        region=1043312403,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005201(
        0,
        character=Characters.MadPumpkinHead,
        animation_id=30005,
        animation_id_1=20005,
        radius=3.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.LivingMass,
        animation_id=30000,
        animation_id_1=20000,
        region=1043312430,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=1043310434, region=1043312430, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310440, region=1043312442, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1043310441, region=1043312442, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=1043310442, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005501(
        0,
        flag=1043310510,
        flag_1=1043310511,
        left=3,
        asset=Assets.AEG030_858_2000,
        asset_1=Assets.AEG099_026_2001,
        asset_2=Assets.AEG099_026_2000,
        flag_2=1043310512,
    )
    Event_1043312510()
    if FlagEnabled(57):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG030_924_2000,
            asset=Assets.AEG030_924_2000,
            dummy_id_start=200,
            dummy_id_end=0,
            behavior_param_id__behaviour_id=802001200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930023, left=0)
    CommonFunc_90005704(0, attacked_entity=Characters.Edgar, flag=3401, flag_1=3400, flag_2=1043309201, right=3)
    CommonFunc_90005703(
        0,
        character=Characters.Edgar,
        flag=3401,
        flag_1=3402,
        flag_2=1043309201,
        flag_3=3401,
        first_flag=3400,
        last_flag=3403,
        right=-1,
    )
    CommonFunc_90005702(0, character=Characters.Edgar, flag=3403, first_flag=3400, last_flag=3403)
    Event_1043310705(0, character=Characters.Edgar, asset=Assets.AEG003_061_2019)
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9000,
        action_button_id=4110,
        item_lot=110620,
        first_flag=400061,
        last_flag=400061,
        flag=1043319208,
        vfx_id=0,
    )
    Event_1043310706()
    Event_1043310707(0, other_entity=Characters.Edgar)
    Event_1043310708()
    Event_1043312709(0, character=Characters.Edgar, asset=Assets.AEG003_061_2019)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)
    DisableBackread(Characters.Edgar)
    Event_1043310519()


@RestartOnRest(1043312443)
def Event_1043312443(_, character: Character | int, region: Region | int):
    """Event 1043312443"""
    AND_1.Add(PlayerInOwnWorld())
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AddSpecialEffect(character, 8080)
    Wait(0.4000000059604645)
    Restart()


@RestartOnRest(1043312242)
def Event_1043312242(_, attacker__character: uint, region: Region | int):
    """Event 1043312242"""
    RemoveSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1043312240):
        return
    AddSpecialEffect(attacker__character, 4800)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1043312240)
    RemoveSpecialEffect(attacker__character, 4800)


@RestartOnRest(1043312223)
def Event_1043312223(_, attacker__character: uint, region: Region | int):
    """Event 1043312223"""
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5655)
    AddSpecialEffect(attacker__character, 4802)
    if FlagEnabled(1043312223):
        return
    AddSpecialEffect(attacker__character, 4800)
    AddSpecialEffect(attacker__character, 5655)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=PLAYER))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacker__character, attacker=ALL_SPIRIT_SUMMONS))
    OR_2.Add(AttackedWithDamageType(attacked_entity=ALL_SPIRIT_SUMMONS, attacker=attacker__character))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=attacker__character, radius=10.0))
    OR_2.Add(EntityWithinDistance(entity=ALL_SPIRIT_SUMMONS, other_entity=attacker__character, radius=10.0))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(character=ALL_SPIRIT_SUMMONS, region=region))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(1043312223)
    RemoveSpecialEffect(attacker__character, 4800)
    RemoveSpecialEffect(attacker__character, 5655)


@ContinueOnRest(1043312510)
def Event_1043312510():
    """Event 1043312510"""
    CommonFunc_90005500(
        0,
        flag=1043310510,
        flag_1=1043310511,
        left=3,
        asset=Assets.AEG030_858_2000,
        asset_1=Assets.AEG099_026_2001,
        obj_act_id=1043313511,
        asset_2=Assets.AEG099_026_2000,
        obj_act_id_1=1043313512,
        region=1043312511,
        region_1=1043312512,
        flag_2=1043310512,
        flag_3=1043310513,
        left_1=0,
    )


@ContinueOnRest(1043310519)
def Event_1043310519():
    """Event 1043310519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1043310510)


@ContinueOnRest(1043312580)
def Event_1043312580():
    """Event 1043312580"""
    RegisterLadder(start_climbing_flag=1043310580, stop_climbing_flag=1043310851, asset=Assets.AEG030_893_2000)
    RegisterLadder(start_climbing_flag=1043310582, stop_climbing_flag=1043310853, asset=Assets.AEG030_863_2000)
    RegisterLadder(start_climbing_flag=1043310584, stop_climbing_flag=1043310855, asset=Assets.AEG030_888_2001)
    RegisterLadder(start_climbing_flag=1043310586, stop_climbing_flag=1043310857, asset=Assets.AEG030_860_2001)
    RegisterLadder(start_climbing_flag=1043310588, stop_climbing_flag=1043310859, asset=Assets.AEG030_844_2003)
    RegisterLadder(start_climbing_flag=1043310590, stop_climbing_flag=1043310861, asset=Assets.AEG030_860_2000)
    RegisterLadder(start_climbing_flag=1043310592, stop_climbing_flag=1043310863, asset=Assets.AEG030_888_2002)
    End()


@RestartOnRest(1043313700)
def Event_1043313700(_, character: uint):
    """Event 1043313700"""
    EnableBackread(character)
    EnableCharacter(character)
    ForceAnimation(character, 30023)
    End()


@RestartOnRest(1043310705)
def Event_1043310705(_, character: uint, asset: Asset | int):
    """Event 1043310705"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    if FlagEnabled(3400):
        DisableFlag(1043319202)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L5, flag=3405)
    GotoIfFlagEnabled(Label.L7, flag=3407)
    DisableCharacter(character)
    DisableBackread(character)
    OR_1.Add(FlagEnabled(3405))
    OR_1.Add(FlagEnabled(3407))
    
    MAIN.Await(OR_1)
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)

    # --- Label 7 --- #
    DefineLabel(7)
    GotoIfFlagEnabled(Label.L0, flag=3400)
    GotoIfFlagEnabled(Label.L1, flag=3401)
    GotoIfFlagEnabled(Label.L3, flag=3403)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 90100)
    Move(character, destination=1043312700, destination_type=CoordEntityType.Region, short_move=True)
    RestoreAsset(asset)
    EnableAssetInvulnerability(asset)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(character)
    EnableBackread(character)
    SetTeamType(character, TeamType.HostileNPC)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    if PlayerInOwnWorld():
        EnableFlag(1043319208)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    AND_1.Add(FlagDisabled(3405))
    AND_1.Add(FlagDisabled(3407))
    
    MAIN.Await(AND_1)
    
    Restart()


@ContinueOnRest(1043310706)
def Event_1043310706():
    """Event 1043310706"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1043319206))
    OR_1.Add(FlagEnabled(3403))
    AND_1.Add(FlagEnabled(3405))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(3398)
    AND_2.Add(FlagEnabled(1043319206))
    AND_2.Add(FlagEnabled(1043300800))
    if not AND_2:
        return
    EnableFlag(3418)


@ContinueOnRest(1043310707)
def Event_1043310707(_, other_entity: uint):
    """Event 1043310707"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(3406, 3417))
    AND_1.Add(FlagEnabled(1043319206))
    AND_1.Add(FlagEnabled(3405))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=100.0))
    
    MAIN.Await(AND_1)
    
    EnableFlag(3418)


@ContinueOnRest(1043310708)
def Event_1043310708():
    """Event 1043310708"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(1043300800):
        return
    AND_1.Add(FlagEnabled(1043300800))
    AND_1.Add(FlagEnabled(3406))
    
    MAIN.Await(AND_1)
    
    EnableFlag(3418)


@RestartOnRest(1043312709)
def Event_1043312709(_, character: Character | int, asset: Asset | int):
    """Event 1043312709"""
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    OR_1.Add(FlagEnabled(3405))
    OR_1.Add(FlagEnabled(3407))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 9624))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(FlagEnabled(3401))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableAssetInvulnerability(asset)
    DestroyAsset(asset, request_slot=0)
