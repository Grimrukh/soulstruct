"""
Southwest Mountaintops (NW) (SE)

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
from .entities.m60_49_54_00_entities import *
from .entities.m12_03_00_00_entities import Assets as m12_03_Assets


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1049540000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005100(
        0,
        flag=76652,
        flag_1=76650,
        asset=Assets.AEG099_090_9000,
        source_flag=77520,
        value=0,
        flag_2=78520,
        flag_3=78521,
        flag_4=78522,
        flag_5=78523,
        flag_6=78524,
        flag_7=78525,
        flag_8=78526,
        flag_9=78527,
        flag_10=78528,
        flag_11=78529,
    )
    CommonFunc_90005300(
        0,
        flag=1049540200,
        character=Characters.Scarab,
        item_lot_param_id=1049540700,
        seconds=0.0,
        left=0,
    )
    CommonFunc_90005501(
        0,
        flag=1049540510,
        flag_1=1049541511,
        left=10,
        asset=m12_03_Assets.AEG239_010_0500,
        asset_1=12031511,
        asset_2=m12_03_Assets.AEG239_021_0502,
        flag_2=1049540512,
    )
    Event_1049542510()
    CommonFunc_90005640(0, flag=1049540540, asset=1049541540)
    Event_1049542210()
    Event_1049542216(0, character=Characters.WanderingNoble3)
    CommonFunc_90005261(0, character=Characters.Wolf, region=1049542260, radius=10.0, seconds=0.0, animation_id=20010)
    CommonFunc_90005261(0, character=1049540373, region=1049542260, radius=10.0, seconds=0.0, animation_id=20002)
    Event_1049542350(0, character__region=1049540350, character=Characters.BigWolf)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    Event_1049543700(0, character=Characters.TalkDummy1, region=1049542700, distance=155.0)
    CommonFunc_90005706(0, 1049540710, 930023, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.TalkDummy1)
    DisableBackread(Characters.WanderingNoble4)


@RestartOnRest(1049542210)
def Event_1049542210():
    """Event 1049542210"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(Characters.WanderingNoble0)
    DisableAI(Characters.WanderingNoble1)
    DisableAI(Characters.WanderingNoble2)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.WanderingNoble0, attacker=0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.WanderingNoble1, attacker=0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.WanderingNoble2, attacker=0))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble0, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble0, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble0, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble0, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble0, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble1, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble1, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble1, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble1, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble1, state_info=260))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble2, state_info=436))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble2, state_info=2))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble2, state_info=5))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble2, state_info=6))
    OR_1.Add(CharacterHasStateInfo(character=Characters.WanderingNoble2, state_info=260))
    AND_1.Add(CharacterHasSpecialEffect(Characters.WanderingNoble0, 481))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90100))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90110))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90160))
    AND_2.Add(CharacterHasSpecialEffect(Characters.WanderingNoble0, 482))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90100))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90120))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90160))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90162))
    AND_3.Add(CharacterHasSpecialEffect(Characters.WanderingNoble0, 483))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90100))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90140))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90160))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90161))
    AND_4.Add(CharacterHasSpecialEffect(Characters.WanderingNoble0, 484))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90130))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90161))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90162))
    AND_5.Add(CharacterHasSpecialEffect(Characters.WanderingNoble0, 487))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90150))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble0, 90160))
    AND_6.Add(CharacterHasSpecialEffect(Characters.WanderingNoble1, 481))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90110))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90160))
    AND_7.Add(CharacterHasSpecialEffect(Characters.WanderingNoble1, 482))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90120))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90160))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.WanderingNoble1, 483))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90140))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90160))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90161))
    AND_9.Add(CharacterHasSpecialEffect(Characters.WanderingNoble1, 484))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90100))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90130))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90161))
    AND_9.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90162))
    AND_10.Add(CharacterHasSpecialEffect(Characters.WanderingNoble1, 487))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90100))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90150))
    AND_10.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble1, 90160))
    AND_11.Add(CharacterHasSpecialEffect(Characters.WanderingNoble2, 481))
    AND_11.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90100))
    AND_11.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90110))
    AND_11.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90160))
    AND_12.Add(CharacterHasSpecialEffect(Characters.WanderingNoble2, 482))
    AND_12.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90100))
    AND_12.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90120))
    AND_12.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90160))
    AND_12.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90162))
    AND_13.Add(CharacterHasSpecialEffect(Characters.WanderingNoble2, 483))
    AND_13.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90100))
    AND_13.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90140))
    AND_13.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90160))
    AND_13.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90161))
    AND_14.Add(CharacterHasSpecialEffect(Characters.WanderingNoble2, 484))
    AND_14.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90100))
    AND_14.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90130))
    AND_14.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90161))
    AND_14.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90162))
    AND_15.Add(CharacterHasSpecialEffect(Characters.WanderingNoble2, 487))
    AND_15.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90100))
    AND_15.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90150))
    AND_15.Add(CharacterDoesNotHaveSpecialEffect(Characters.WanderingNoble2, 90160))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_10)
    OR_1.Add(AND_11)
    OR_1.Add(AND_12)
    OR_1.Add(AND_13)
    OR_1.Add(AND_14)
    OR_1.Add(AND_15)
    
    MAIN.Await(OR_1)
    
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    EnableAI(Characters.WanderingNoble0)
    EnableAI(Characters.WanderingNoble1)
    EnableAI(Characters.WanderingNoble2)


@RestartOnRest(1049542216)
def Event_1049542216(_, character: uint):
    """Event 1049542216"""
    EnableImmortality(character)
    DisableAnimations(character)
    ForceAnimation(character, 30005, loop=True)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableHealthBar(character)
    End()


@RestartOnRest(1049542350)
def Event_1049542350(_, character__region: uint, character: uint):
    """Event 1049542350"""
    if ThisEventSlotFlagDisabled():
        SetCharacterEventTarget(character, region=character__region)
    AND_1.Add(CharacterHasSpecialEffect(character, 11893))
    AND_1.Add(CharacterAlive(character__region))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(character__region, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=283,
        set_draw_parent=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(character, 20003)
    AddSpecialEffect(character__region, 11880)
    AddSpecialEffect(character, 11880)
    ReplanAI(character__region)
    Wait(5.0)
    SetNetworkUpdateRate(character__region, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@NeverRestart(1049542510)
def Event_1049542510():
    """Event 1049542510"""
    CommonFunc_90005500(
        0,
        1049540510,
        1049540511,
        10,
        12031510,
        1049541511,
        1049543511,
        12031512,
        12033512,
        1049542511,
        12032512,
        1049540512,
        1049542513,
        0,
    )


@RestartOnRest(1049540519)
def Event_1049540519():
    """Event 1049540519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1049540510)


@RestartOnRest(1049543700)
def Event_1049543700(_, character: uint, region: uint, distance: float):
    """Event 1049543700"""
    WaitFrames(frames=1)
    DisableBackread(character)
    DisableCharacter(character)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(4100):
        return
    if FlagDisabled(4106):
        return
    if FlagEnabled(1049549201):
        return
    if FlagEnabled(1047589205):
        return
    EnableBackread(character)
    EnableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    if FlagDisabled(1049512700):
        DisableFlag(1049549200)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    SetCharacterTalkRange(character=character, distance=distance)
    EnableFlag(1049549200)
    Wait(30.0)
    SetCharacterTalkRange(character=character, distance=17.0)
    End()


@NeverRestart(200)
def Event_200():
    """Event 200"""
    CommonFunc_90005421(0, character=Characters.CaravanDummy, asset=Assets.AEG100_101_9000, flag=1249548301)
    CommonFunc_90005422(0, flag=1249548301, asset=Assets.AEG100_120_9000, obj_act_id=1249543301)
    CommonFunc_90005424(
        0,
        asset=Assets.AEG100_120_9000,
        character=Characters.SnowTroll0,
        character_1=Characters.SnowTroll1,
        character_2=Characters.CaravanDummy,
        asset_1=Assets.AEG100_101_9000,
    )
    CommonFunc_90005423(0, character=Characters.SnowTroll0)
    CommonFunc_90005423(0, character=Characters.SnowTroll1)
    CommonFunc_90005261(
        0,
        character=Characters.CaravanDummy,
        region=1249542300,
        radius=10.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005261(0, character=Characters.Dummy, region=1249542300, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, character=Characters.SnowTroll0, region=1249542300, radius=10.0, seconds=0.0, animation_id=0)
    CommonFunc_90005261(0, 1249540303, 1249542300, 10.0, 0.0, 0)


@NeverRestart(250)
def Event_250():
    """Event 250"""
    CommonFunc_90005420(0, 1249540300, 1249541300, 1249541301, 1249540301, 1249540302, 1249540303, 0.0)
