"""
Volcano Cave

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
from .enums.m31_09_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=31090000, asset=Assets.AEG099_060_9000)
    Event_31092800()
    Event_31092810()
    Event_31092849()
    Event_31092811()
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, dummy_id=100, vfx_id=800, right=0)
    CommonFunc_90005261(0, character=Characters.DemiHuman0, region=31092200, radius=1.0, seconds=0.0, animation_id=0)
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman1,
        animation_id=30001,
        animation_id_1=20001,
        region=31092201,
        radius=1.0,
        seconds=1.399999976158142,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman2,
        animation_id=30002,
        animation_id_1=20002,
        region=31092201,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman3,
        animation_id=30000,
        animation_id_1=20000,
        region=31092201,
        radius=1.0,
        seconds=1.600000023841858,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman4,
        animation_id=30000,
        animation_id_1=20000,
        region=31092201,
        radius=1.0,
        seconds=1.7999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman5,
        animation_id=30002,
        animation_id_1=20002,
        region=31092214,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman6,
        animation_id=30002,
        animation_id_1=20002,
        region=31092214,
        radius=1.0,
        seconds=0.30000001192092896,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHuman7,
        animation_id=30001,
        animation_id_1=20001,
        region=31092214,
        radius=1.0,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.LargeDemiHuman2,
        animation_id=30002,
        animation_id_1=20002,
        region=31092214,
        radius=1.0,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanShaman0,
        region=31092254,
        radius=1.0,
        seconds=0.0,
        animation_id=0,
    )
    CommonFunc_90005211(
        0,
        character=Characters.DemiHumanShaman1,
        animation_id=30002,
        animation_id_1=20002,
        region=31092256,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_31092301(0, character=Characters.DemiHuman8, seconds=1.0)
    Event_31092301(1, character=Characters.DemiHumanShaman2, seconds=0.5)
    Event_31092301(2, character=Characters.LargeDemiHuman1, seconds=1.0)
    CommonFunc_90005261(
        0,
        character=Characters.DemiHumanBeastman,
        region=31092350,
        radius=2.0,
        seconds=0.0,
        animation_id=0,
    )
    Event_31092350()
    Event_31092351()
    Event_31092300()
    CommonFunc_90005646(
        0,
        flag=31090800,
        left_flag=31092840,
        cancel_flag__right_flag=31092841,
        asset=Assets.AEG099_065_9000,
        player_start=31092840,
        area_id=31,
        block_id=9,
        cc_id=0,
        dd_id=0,
    )


@RestartOnRest(31092300)
def Event_31092300():
    """Event 31092300"""
    OR_15.Add(CharacterDead(Characters.LargeDemiHuman0))
    if OR_15:
        return
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.LargeDemiHuman0)
    DisableAI(Characters.LargeDemiHuman0)
    ForceAnimation(Characters.LargeDemiHuman0, 30002)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHuman8))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHumanShaman2))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LargeDemiHuman0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LargeDemiHuman1))
    OR_1.Add(EntityWithinDistance(entity=Characters.LargeDemiHuman0, other_entity=PLAYER, radius=3.0))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=31092301))
    AND_4.Add(CharacterHasSpecialEffect(Characters.LargeDemiHuman0, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.LargeDemiHuman0, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.LargeDemiHuman0, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.LargeDemiHuman0, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.LargeDemiHuman0, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.LargeDemiHuman0, 90160))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    Wait(0.5)
    EnableAI(Characters.LargeDemiHuman0)
    ForceAnimation(Characters.LargeDemiHuman0, 20002, skip_transition=True)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=Characters.LargeDemiHuman0, state=True)


@RestartOnRest(31092301)
def Event_31092301(_, character: uint, seconds: float):
    """Event 31092301"""
    OR_15.Add(CharacterDead(character))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    DisableAI(character)
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHuman8))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.DemiHumanShaman2))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LargeDemiHuman0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=Characters.LargeDemiHuman1))
    OR_1.Add(AssetDestroyed(31091550))
    OR_1.Add(AssetDestroyed(31091551))
    OR_1.Add(AssetDestroyed(31091552))
    OR_1.Add(AssetDestroyed(31091553))
    OR_1.Add(AssetDestroyed(31091554))
    OR_1.Add(AssetDestroyed(31091555))
    OR_1.Add(AssetDestroyed(31091556))
    OR_1.Add(AssetDestroyed(31091557))
    OR_1.Add(AssetDestroyed(31091558))
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
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=31092301))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    EnableAI(character)
    EnableThisNetworkSlotFlag()


@RestartOnRest(31092350)
def Event_31092350():
    """Event 31092350"""
    AND_15.Add(CharacterDead(Characters.DemiHumanBeastman))
    if AND_15:
        return
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.DemiHumanBeastman, 8081))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=31092351))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(Characters.DemiHumanBeastman, 8081)
    Restart()


@RestartOnRest(31092351)
def Event_31092351():
    """Event 31092351"""
    AND_15.Add(CharacterDead(Characters.DemiHumanBeastman))
    if AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.DemiHumanBeastman, 8081))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=31092351))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(Characters.DemiHumanBeastman, 8081)
    Restart()


@RestartOnRest(31092800)
def Event_31092800():
    """Event 31092800"""
    if FlagEnabled(31090800):
        return
    
    MAIN.Await(HealthValue(Characters.DemiHumanQueen) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.DemiHumanQueen, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.DemiHumanQueen))
    
    KillBossAndDisplayBanner(character=Characters.DemiHumanQueen, banner_type=BannerType.EnemyFelled)
    EnableFlag(31090800)
    EnableFlag(9240)
    if PlayerInOwnWorld():
        EnableFlag(61240)


@RestartOnRest(31092810)
def Event_31092810():
    """Event 31092810"""
    GotoIfFlagDisabled(Label.L0, flag=31090800)
    DisableCharacter(Characters.DemiHumanQueen)
    DisableAnimations(Characters.DemiHumanQueen)
    Kill(Characters.DemiHumanQueen)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.DemiHumanQueen)
    AddSpecialEffect(Characters.DemiHumanQueen, 8092)
    AND_2.Add(FlagEnabled(31092805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=31092800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.DemiHumanQueen)
    SetNetworkUpdateRate(Characters.DemiHumanQueen, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DemiHumanQueen, name=904130310)


@RestartOnRest(31092811)
def Event_31092811():
    """Event 31092811"""
    if FlagEnabled(31090800):
        return
    AND_1.Add(HealthRatio(Characters.DemiHumanQueen) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(31092802)


@RestartOnRest(31092849)
def Event_31092849():
    """Event 31092849"""
    CommonFunc_9005800(
        0,
        flag=31090800,
        entity=Assets.AEG099_001_9001,
        region=31092800,
        flag_1=31092805,
        character=31095800,
        action_button_id=10010,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=31090800,
        entity=Assets.AEG099_001_9001,
        region=31092800,
        flag_1=31092805,
        flag_2=31092806,
        action_button_id=10010,
    )
    CommonFunc_9005811(0, flag=31090800, asset=Assets.AEG099_001_9001, vfx_id=5, right=0)
    CommonFunc_9005822(
        0,
        flag=31090800,
        bgm_boss_conv_param_id=931000,
        flag_1=31092805,
        flag_2=31092806,
        right=0,
        flag_3=31092802,
        left=0,
        left_1=0,
    )
