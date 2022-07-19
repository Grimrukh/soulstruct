"""
East Weeping Peninsula (SW) (NW)

linked:
0
82
166

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: N:\\GR\\data\\Param\\event\\common_macro.emevd
166: N:\\GR\\data\\Param\\event\\m60.emevd
232: 
234: 
236: 
238: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_44_33_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1044330000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1044330001, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=1044330002, asset=Assets.AEG099_060_9002)
    CommonFunc_90005100(
        0,
        flag=76161,
        flag_1=76151,
        asset=Assets.AEG099_090_9001,
        source_flag=77110,
        value=2,
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
    CommonFunc_90005300(0, flag=1044330290, character=Characters.Scarab, item_lot_param_id=40140, seconds=0.0, left=0)
    CommonFunc_90005550(0, flag=1044330500, asset=1044331500, obj_act_id=44333500)
    CommonFunc_90005510(
        0,
        flag=1044330540,
        asset=1044331540,
        obj_act_id=1044333540,
        obj_act_id_1=-1,
        text=10010851,
        left=0,
    )
    CommonFunc_90005461(0, character=Characters.Commoner0)
    CommonFunc_90005462(1, character=Characters.Commoner0)
    CommonFunc_90005460(0, character=Characters.Commoner0)
    Event_1044332230(0, character=1044330970)
    Event_1044332230(1, character=1044330240)
    Event_1044332230(2, character=1044330241)
    Event_1044332230(3, character=1044330242)
    Event_1044332230(4, character=1044330243)
    Event_1044332230(5, character=1044330244)
    Event_1044332230(6, character=1044330245)
    Event_1044332230(7, character=1044330246)
    Event_1044332230(18, character=1044330247)
    Event_1044332230(19, character=1044330248)
    Event_1044332230(20, character=1044330249)
    Event_1044332230(8, character=1044330304)
    Event_1044332230(9, character=1044330305)
    Event_1044332230(10, character=1044330306)
    Event_1044332230(11, character=1044330307)
    Event_1044332230(12, character=1044330308)
    Event_1044332230(13, character=1044330309)
    Event_1044332230(14, character=1044330310)
    Event_1044332230(15, character=1044330311)
    Event_1044332230(16, character=1044330312)
    Event_1044332230(17, character=1044330313)
    Event_1044332230(21, character=1044330300)
    Event_1044332230(22, character=1044330301)
    Event_1044332230(15, character=Characters.Misbegotten4)
    Event_1044332230(16, character=1044330251)
    Event_1044332230(17, character=1044330252)
    Event_1044332230(18, character=1044330253)
    Event_1044332230(19, character=1044330254)
    Event_1044332230(20, character=1044330255)
    Event_1044332230(21, character=1044330256)
    Event_1044332280(0, character=Characters.DemiHuman0, asset=Assets.AEG801_480_9000, region=1044332280)
    Event_1044332280(1, character=Characters.DemiHuman1, asset=Assets.AEG801_480_9001, region=1044332280)
    CommonFunc_90005400(0, character=Characters.Misbegotten4, special_effect_id=0, seconds=0.0, seconds_1=0.0, left=0)
    CommonFunc_90005401(0, flag=98103, character=Characters.Misbegotten4)
    if FlagEnabled(57):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001270,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(56):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001260,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(55):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001250,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(54):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001240,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(53):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001230,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(52):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001220,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(51):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001210,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    if FlagEnabled(50):
        CommonFunc_90005695(
            0,
            asset__asset_flag=Assets.AEG007_450_1000,
            asset=Assets.AEG007_450_1000,
            model_point_start=200,
            model_point_end=0,
            behavior_param_id__behaviour_id=802001200,
            radius=1.0,
            life=0.0,
            repetition_time=1.0,
        )
    Event_1044333700(0, character=1044330700)
    CommonFunc_90005725(
        0,
        flag=4735,
        flag_1=4736,
        flag_2=4738,
        flag_3=1044339205,
        character=Characters.Merchant,
        character_1=Characters.NomadMule,
        asset=1044336700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4736,
        flag_1=4737,
        flag_2=1044339206,
        flag_3=4736,
        first_flag=4735,
        last_flag=4739,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4736, flag_1=4735, flag_2=1044339206, right=3)
    CommonFunc_90005702(0, character=Characters.Merchant, flag=4738, first_flag=4735, last_flag=4739)
    CommonFunc_90005703(
        0,
        character=Characters.NomadMule,
        flag=4736,
        flag_1=4737,
        flag_2=1044339207,
        flag_3=4736,
        first_flag=4735,
        last_flag=4739,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.NomadMule, flag=4736, flag_1=4735, flag_2=1044339207, right=3)
    CommonFunc_90005728(0, attacked_entity=Characters.NomadMule, flag=1044332706, flag_1=1044332707)
    CommonFunc_90005727(0, 4736, 1044330705, 1044330706, 4735, 4738)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1044330700)
    DisableBackread(Characters.Merchant)
    DisableBackread(Characters.NomadMule)
    CommonFunc_90005251(0, character=Characters.GodrickSoldier0, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GodrickSoldier1, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog0, region=1044332233, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=1044330271, region=1044332233, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog1, region=1044332231, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog2, region=1044332231, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.SmallerDog3, region=1044332231, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Troll, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten0,
        region=1044332260,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten1,
        region=1044332260,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten2,
        region=1044332260,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005261(
        0,
        character=Characters.Misbegotten3,
        region=1044332260,
        radius=5.0,
        seconds=0.0,
        animation_id=-1,
    )
    CommonFunc_90005251(0, character=Characters.Commoner0, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commoner1, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commoner2, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commoner3, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Commoner4, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(2, character=Characters.Commoner5, radius=4.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.Commoner0,
        animation_id=30006,
        animation_id_1=20006,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Commoner1,
        animation_id=30004,
        animation_id_1=20004,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Commoner2,
        animation_id=30004,
        animation_id_1=20004,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Commoner3,
        animation_id=30006,
        animation_id_1=20006,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Commoner4,
        animation_id=30004,
        animation_id_1=20004,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Commoner5,
        animation_id=30004,
        animation_id_1=20004,
        radius=4.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(0, character=Characters.Rat0, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Rat1, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=1044330216, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Rat2, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Rat3, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.GiantRat, region=1044332220, radius=15.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=Characters.Commoner0, region=1044332200, radius=1.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, 1044330201, 1044332200, 1.0, 0.0, -1)


@NeverRestart(200)
def Event_200():
    """Event 200"""
    Event_1044332240()


@RestartOnRest(1044332230)
def Event_1044332230(_, character: uint):
    """Event 1044332230"""
    Kill(character)
    End()


@RestartOnRest(1044332240)
def Event_1044332240():
    """Event 1044332240"""
    EndOfAnimation(asset=Assets.AEG100_101_1000, animation_id=2)


@RestartOnRest(1044332280)
def Event_1044332280(_, character: uint, asset: uint, region: uint):
    """Event 1044332280"""
    DisableCharacter(character)
    DisableAsset(asset)
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    AND_10.Add(CharacterDead(character))
    if AND_10:
        return
    EnableAsset(asset)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    OR_2.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    OR_3.Add(AND_5)
    OR_3.Add(AND_6)
    OR_3.Add(AND_7)
    OR_3.Add(AND_8)
    
    MAIN.Await(OR_3)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    CreateTemporaryVFX(vfx_id=641012, anchor_entity=character, model_point=900, anchor_type=CoordEntityType.Character)
    Wait(0.5)
    DisableAsset(asset)
    Wait(0.30000001192092896)
    EnableCharacter(character)


@RestartOnRest(1044332300)
def Event_1044332300():
    """Event 1044332300"""
    AddSpecialEffect(Characters.GiantRat, 8810)
    DisableCharacter(1044330210)
    DisableAnimations(1044330210)
    DisableCharacter(1044335240)
    DisableAnimations(1044335240)
    ForceAnimation(1044330210, 30005, loop=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1044332351))
    AND_1.Add(FlagDisabled(1044330321))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(1044330210)
    EnableAnimations(1044330210)
    ForceAnimation(1044330210, 30005, loop=True)
    EnableFlag(1044330300)
    EnableFlag(1044332320)


@RestartOnRest(1044332301)
def Event_1044332301():
    """Event 1044332301"""
    GotoIfFlagEnabled(Label.L0, flag=1044330321)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1044332332))
    
    MAIN.Await(AND_1)
    
    ChangePatrolBehavior(1044330210, patrol_information_id=1044333351)
    Wait(10.0)
    DisableFlag(1044332320)
    EnableFlag(1044330321)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(1044330210)
    DisableAnimations(1044330210)
    DisableCharacter(1044335240)
    DisableAnimations(1044335240)


@RestartOnRest(1044332302)
def Event_1044332302():
    """Event 1044332302"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1044332320))
    AND_1.Add(FlagDisabled(1044330321))
    AND_1.Add(FlagDisabled(1044332322))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=1044332350))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(1044335240)
    EnableAnimations(1044335240)
    AddSpecialEffect(1044335240, 10270)
    RemoveSpecialEffect(1044335240, 8552)
    EnableFlag(1044332322)
    ForceAnimation(1044330210, 20021, wait_for_completion=True)
    ChangePatrolBehavior(1044330210, patrol_information_id=1044333350)
    AddSpecialEffect(1044330210, 5000)
    EnableFlag(1044332330)


@RestartOnRest(1044332303)
def Event_1044332303():
    """Event 1044332303"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1044332320))
    AND_1.Add(CharacterDead(1044330225))
    AND_1.Add(CharacterDead(1044330226))
    AND_1.Add(CharacterDead(1044330227))
    AND_1.Add(CharacterDead(1044330228))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1044332331)
    RemoveSpecialEffect(1044330210, 5000)


@RestartOnRest(1044332304)
def Event_1044332304():
    """Event 1044332304"""
    DisableFlag(1044332330)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1044330390))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1044332330)


@RestartOnRest(1044333700)
def Event_1044333700(_, character: uint):
    """Event 1044333700"""
    WaitFrames(frames=1)
    if PlayerNotInOwnWorld():
        return
    EnableImmortality(character)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    ForceAnimation(character, 20022)
    Wait(10.0)
    DisableCharacter(character)
    DisableBackread(character)
    End()
