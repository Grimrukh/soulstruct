"""
Ainsel River

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
from .entities.m12_01_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=71211, asset=Assets.AEG099_060_9001)
    RegisterGrace(grace_flag=71212, asset=Assets.AEG099_060_9002)
    RegisterGrace(grace_flag=71213, asset=Assets.AEG099_060_9003)
    RegisterGrace(grace_flag=71214, asset=Assets.AEG099_060_9004)
    RegisterGrace(grace_flag=71215, asset=Assets.AEG099_060_9005)
    RegisterGrace(grace_flag=71216, asset=Assets.AEG099_060_9006)
    RegisterGrace(grace_flag=71217, asset=12011957)
    RegisterGrace(grace_flag=71218, asset=Assets.AEG099_060_9008)
    RegisterGrace(grace_flag=71219, asset=Assets.AEG099_060_9009)
    CommonFunc_9005810(
        0,
        flag=12010800,
        grace_flag=71210,
        character=Characters.TalkDummy0,
        asset=Assets.AEG099_060_9000,
        enemy_block_distance=5.0,
    )
    CommonFunc_90005620(
        0,
        flag=12010570,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=12012570,
        cancel_flag__right_flag=12012571,
        right=12012572,
    )
    Event_12012569(0, flag=12010570, asset=Assets.AEG099_271_9000)
    Event_12012569(1, flag=12010570, asset=Assets.AEG099_271_9001)
    CommonFunc_90005251(0, character=Characters.GiantAnt0, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantAnt1, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantAnt2, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=12010207, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.GiantAnt5, radius=40.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.GiantAnt4,
        animation_id=30001,
        animation_id_1=20001,
        radius=14.0,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.GiantAnt6,
        animation_id=30001,
        animation_id_1=20001,
        radius=10.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.GiantAnt3, region=12012200, seconds=0.5, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.GiantAnt8,
        animation_id=30009,
        animation_id_1=20022,
        region=12012211,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.GiantAnt9,
        animation_id=30009,
        animation_id_1=20022,
        region=12012211,
        seconds=10.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.GiantAnt7, radius=3.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005201(
        0,
        character=Characters.GiantAnt18,
        animation_id=30001,
        animation_id_1=20001,
        radius=8.0,
        seconds=0.0,
        left=1,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(
        0,
        flag=12010240,
        character=Characters.GiantAnt10,
        item_lot=12010105,
        seconds=3.5,
        left=0,
    )
    Event_12012220(0, character=Characters.GiantAnt11)
    Event_12012220(1, character=Characters.GiantAnt12)
    Event_12012220(2, character=Characters.GiantAnt13)
    Event_12012220(3, character=Characters.GiantAnt14)
    Event_12012220(4, character=Characters.GiantAnt15)
    Event_12012220(5, character=Characters.GiantAnt16)
    Event_12012220(6, character=Characters.GiantAnt17)
    Event_12012220(7, character=Characters.GiantAnt10)
    Event_12012231(0, character=Characters.GiantAnt11, seconds=0.0)
    Event_12012231(1, character=Characters.GiantAnt12, seconds=3.0)
    Event_12012231(2, character=Characters.GiantAnt13, seconds=6.0)
    Event_12012231(3, character=Characters.GiantAnt14, seconds=9.0)
    Event_12012231(4, character=Characters.GiantAnt15, seconds=12.0)
    Event_12012231(5, character=Characters.GiantAnt16, seconds=12.0)
    Event_12012231(6, character=Characters.GiantAnt17, seconds=16.0)
    CommonFunc_90005261(0, character=Characters.GiantBall0, region=12012245, radius=30.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=12010246, region=12012246, seconds=1.0, animation_id=-1)
    Event_12012239()
    Event_12012249()
    Event_12012240()
    Event_12012256()
    Event_12012257()
    Event_12012288(0, character=Characters.SilverTear5, character_1=Characters.SilverTear0, region=12022298)
    Event_12012288(1, character=Characters.SilverTear6, character_1=Characters.SilverTear1, region=12022299)
    CommonFunc_90005261(0, character=Characters.NoxFighter1, region=12012251, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=12010260, region=12012260, seconds=0.5, animation_id=3006)
    CommonFunc_90005250(0, character=Characters.NoxFighter2, region=12012260, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.NoxFighter3, region=12012260, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.NoxFighter0, radius=25.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(0, character=12015280, region=12012280, radius=10.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear2,
        animation_id=30000,
        animation_id_1=20000,
        region=12012288,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear3,
        animation_id=30000,
        animation_id_1=20000,
        region=12012289,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear7,
        animation_id=30000,
        animation_id_1=20000,
        region=12012290,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear8,
        animation_id=30000,
        animation_id_1=20000,
        region=12012290,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.SilverTear9,
        animation_id=30000,
        animation_id_1=20000,
        region=12012290,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_12012301()
    CommonFunc_90005251(0, character=Characters.Clayman0, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=12010320,
        animation_id=30001,
        animation_id_1=20001,
        region=12012320,
        seconds=6.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower0,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower1,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower2,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower3,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower4,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=1.2000000476837158,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.MirandaFlower5,
        animation_id=30000,
        animation_id_1=20000,
        region=12012330,
        seconds=1.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005860(
        0,
        flag=12010850,
        left=0,
        character=Characters.DragonkinSoldier3,
        left_1=1,
        item_lot=30600,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.DragonkinSoldier3, name=904650601, npc_threat_level=25)
    CommonFunc_90005201(
        0,
        character=Characters.DragonkinSoldier3,
        animation_id=30000,
        animation_id_1=20000,
        radius=20.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005251(0, character=Characters.DragonkinSoldier3, radius=20.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=12010373, radius=12.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.Basilisk0, radius=18.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Basilisk1, region=12012377, seconds=0.0, animation_id=3000)
    CommonFunc_90005250(0, character=Characters.Basilisk2, region=12012377, seconds=2.0, animation_id=3001)
    CommonFunc_90005250(0, character=Characters.Basilisk3, region=12012377, seconds=2.0, animation_id=3001)
    CommonFunc_90005211(
        0,
        character=Characters.MalformedStar0,
        animation_id=30005,
        animation_id_1=20005,
        region=12012400,
        radius=30.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005300(0, flag=12010400, character=Characters.MalformedStar0, item_lot=0, seconds=3.5, left=0)
    CommonFunc_90005300(
        0,
        flag=12010401,
        character=Characters.MalformedStar1,
        item_lot=12015995,
        seconds=3.5,
        left=0,
    )
    CommonFunc_90005300(0, flag=12010403, character=Characters.Scarab0, item_lot=40600, seconds=1.5, left=0)
    CommonFunc_90005300(0, flag=12010404, character=Characters.Scarab1, item_lot=40602, seconds=1.5, left=0)
    CommonFunc_90005300(
        0,
        flag=12010420,
        character=Characters.UlceratedTreeSpirit,
        item_lot=12015997,
        seconds=3.5,
        left=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.UlceratedTreeSpirit,
        animation_id=30002,
        animation_id_1=20002,
        radius=15.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_12012421()
    CommonFunc_90005300(0, flag=12010421, character=Characters.OnyxLord, item_lot=0, seconds=1.5, left=0)
    CommonFunc_90005200(
        0,
        character=Characters.Snail0,
        animation_id=30005,
        animation_id_1=20005,
        region=12012410,
        seconds=1.2999999523162842,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=12010416,
        animation_id=30005,
        animation_id_1=20005,
        region=12012410,
        seconds=0.800000011920929,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Snail1,
        animation_id=30005,
        animation_id_1=20005,
        region=12012410,
        seconds=1.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Snail2,
        animation_id=30005,
        animation_id_1=20005,
        region=12012410,
        seconds=0.6000000238418579,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Snail3,
        animation_id=30005,
        animation_id_1=20005,
        region=12012410,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_12012800()
    Event_12012810()
    Event_12012849()
    Event_12012820()
    Event_12012830()
    Event_12012811()
    Event_12012812()
    CommonFunc_90005501(
        0,
        flag=12010510,
        flag_1=12010511,
        left=2,
        asset=Assets.AEG239_010_0500,
        asset_1=Assets.AEG239_020_0504,
        asset_2=Assets.AEG239_020_0505,
        flag_2=12010512,
    )
    CommonFunc_90005501(
        0,
        flag=12010515,
        flag_1=12010516,
        left=3,
        asset=Assets.AEG239_010_0501,
        asset_1=Assets.AEG239_020_0502,
        asset_2=Assets.AEG239_020_0503,
        flag_2=12010517,
    )
    CommonFunc_90005501(
        0,
        flag=12010520,
        flag_1=12010521,
        left=6,
        asset=Assets.AEG239_010_0502,
        asset_1=Assets.AEG239_020_0500,
        asset_2=Assets.AEG239_020_0501,
        flag_2=12010522,
    )
    CommonFunc_90005501(
        0,
        flag=12010525,
        flag_1=12010526,
        left=9,
        asset=Assets.AEG239_010_0503,
        asset_1=Assets.AEG239_020_0506,
        asset_2=Assets.AEG239_020_0507,
        flag_2=12010527,
    )
    Event_12010509()
    Event_12012506()
    Event_12012507()
    Event_12012530()
    Event_12012590()
    Event_12012591()
    Event_12012593()
    Event_12012594()
    Event_12012595()
    Event_12012580(
        0,
        flag=12010590,
        vibration_id=105,
        anchor_entity=12012580,
        decay_start_distance=20.0,
        decay_end_distance=100.0,
    )
    Event_12012581(
        1,
        flag=12010591,
        vibration_id=105,
        anchor_entity=12012581,
        decay_start_distance=100.0,
        decay_end_distance=400.0,
    )
    Event_12012582(
        2,
        flag=12010593,
        vibration_id=105,
        anchor_entity=12012583,
        decay_start_distance=100.0,
        decay_end_distance=400.0,
    )
    Event_12012583(
        3,
        flag=12010594,
        vibration_id=105,
        anchor_entity=12012584,
        decay_start_distance=100.0,
        decay_end_distance=400.0,
    )
    Event_12012584(
        4,
        flag=12010595,
        vibration_id=105,
        anchor_entity=12012585,
        decay_start_distance=35.0,
        decay_end_distance=150.0,
    )
    Event_12010700()
    Event_12010701()
    Event_12010702()
    Event_12010705()
    Event_12010706()
    Event_12010707()
    Event_12010708()
    CommonFunc_90005750(
        0,
        asset=Assets.AEG099_990_9001,
        action_button_id=4350,
        item_lot=103940,
        first_flag=400394,
        last_flag=400394,
        flag=1034509430,
        model_point=0,
    )
    CommonFunc_90005726(
        0,
        flag=4805,
        flag_1=4806,
        flag_2=4808,
        flag_3=1035469205,
        character=Characters.Merchant,
        asset=12016700,
    )
    CommonFunc_90005703(
        0,
        character=Characters.Merchant,
        flag=4806,
        flag_1=4807,
        flag_2=12019006,
        flag_3=4806,
        first_flag=4805,
        last_flag=4809,
        right=0,
    )
    CommonFunc_90005704(0, attacked_entity=Characters.Merchant, flag=4806, flag_1=4805, flag_2=12019006, right=3)
    CommonFunc_90005702(0, 12010705, 4808, 4805, 4809)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_12010519()
    Event_12012050()
    DisableBackread(Characters.Blaidd)
    DisableBackread(12010720)


@RestartOnRest(12010700)
def Event_12010700():
    """Event 12010700"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy16, radius=3.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy17, radius=3.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12012710)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy16, radius=3.0))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy17, radius=3.0))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12012710)
    Restart()


@RestartOnRest(12010701)
def Event_12010701():
    """Event 12010701"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy17, radius=3.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12012711)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy17, radius=3.0))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12012711)
    Restart()


@RestartOnRest(12010702)
def Event_12010702():
    """Event 12010702"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12012712)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=Characters.TalkDummy18, radius=3.0))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12012712)
    Restart()


@RestartOnRest(12010705)
def Event_12010705():
    """Event 12010705"""
    DisableBackread(Characters.Blaidd)
    GotoIfFlagEnabled(Label.L0, flag=12012715)
    if FlagEnabled(12019280):
        Kill(Characters.Blaidd)
        End()
    AND_1.Add(FlagEnabled(12019257))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=Characters.Blaidd, radius=53.0))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        EnableFlag(12012715)
    EnableBackread(Characters.Blaidd)
    EnableCharacter(Characters.Blaidd)
    WaitFrames(frames=1)
    ForceAnimation(Characters.Blaidd, 20039)
    End()


@RestartOnRest(12010706)
def Event_12010706():
    """Event 12010706"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(12019280):
        return
    OR_1.Add(CharacterDead(Characters.Blaidd))
    OR_1.Add(HealthValue(Characters.Blaidd) <= 0)
    
    MAIN.Await(OR_1)
    
    EnableFlag(12019280)
    EnableFlag(12012716)
    End()


@RestartOnRest(12010707)
def Event_12010707():
    """Event 12010707"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(12019280):
        return
    if FlagEnabled(12019271):
        return
    DisableFlag(12019270)
    AND_1.Add(FlagEnabled(12012715))
    AND_1.Add(EntityWithinDistance(entity=20000, other_entity=Characters.Blaidd, radius=25.0))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=Characters.TalkDummy19, distance=100.0)
    EnableFlag(12019270)
    OR_1.Add(TimeElapsed(seconds=30.0))
    OR_1.Add(FlagEnabled(12019280))
    
    MAIN.Await(OR_1)
    
    if FlagDisabled(12019280):
        SetCharacterTalkRange(character=Characters.TalkDummy19, distance=17.0)
    End()


@RestartOnRest(12010708)
def Event_12010708():
    """Event 12010708"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(12019280):
        return
    if FlagEnabled(12019273):
        return
    DisableFlag(12019272)
    
    MAIN.Await(FlagEnabled(12019280))
    
    Move(
        Characters.TalkDummy19,
        destination=20000,
        destination_type=CoordEntityType.Character,
        model_point=11,
        copy_draw_parent=20000,
    )
    SetCharacterTalkRange(character=Characters.TalkDummy19, distance=100.0)
    EnableFlag(12019272)
    
    MAIN.Await(TimeElapsed(seconds=30.0))
    
    SetCharacterTalkRange(character=Characters.TalkDummy19, distance=17.0)
    End()


@RestartOnRest(12012050)
def Event_12012050():
    """Event 12012050"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(12010340, 90010)
    AddSpecialEffect(Characters.DragonkinSoldier3, 90010)
    AddSpecialEffect(Characters.UlceratedTreeSpirit, 90010)
    AddSpecialEffect(Characters.GiantBall0, 5490)
    
    MAIN.Await(InsideMap(game_map=AINSEL_RIVER))
    
    DisableAsset(12015650)


@ContinueOnRest(12012569)
def Event_12012569(_, flag: uint, asset: uint):
    """Event 12012569"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAsset(asset)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateAssetVFX(asset, vfx_id=101, model_point=806043)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DeleteAssetVFX(asset)
    PlaySoundEffect(asset, 90011, sound_type=SoundType.s_SFX)
    Wait(0.5)
    DisableAsset(asset)


@RestartOnRest(12012580)
def Event_12012580(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012580"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.699999988079071)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=106,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.8999999761581421)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012581)
def Event_12012581(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012581"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.6000000238418579)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012582)
def Event_12012582(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012582"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=106,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012583)
def Event_12012583(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012583"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.0)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2000000476837158)
    SetCameraVibration(
        vibration_id=103,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012584)
def Event_12012584(
    _,
    flag: uint,
    vibration_id: int,
    anchor_entity: uint,
    decay_start_distance: float,
    decay_end_distance: float,
):
    """Event 12012584"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.5)
    SetCameraVibration(
        vibration_id=102,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(0.800000011920929)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=vibration_id,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.0)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )
    Wait(1.2999999523162842)
    SetCameraVibration(
        vibration_id=105,
        anchor_entity=anchor_entity,
        decay_start_distance=decay_start_distance,
        decay_end_distance=decay_end_distance,
        anchor_type=CoordEntityType.Region,
    )


@RestartOnRest(12012590)
def Event_12012590():
    """Event 12012590"""
    GotoIfFlagDisabled(Label.L0, flag=12010590)
    EndOfAnimation(asset=Assets.AEG237_065_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG237_081_0500, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=Assets.AEG237_065_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG237_081_0500, animation_id=0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12010590))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012590))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12010590)
    ForceAnimation(Assets.AEG237_081_0500, 1, wait_for_completion=True)
    Wait(1.0)
    ForceAnimation(Assets.AEG237_065_0500, 0)
    End()


@RestartOnRest(12012591)
def Event_12012591():
    """Event 12012591"""
    GotoIfFlagDisabled(Label.L0, flag=12010591)
    EndOfAnimation(asset=Assets.AEG237_066_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG237_069_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG237_081_0501, animation_id=2)
    EnableMapCollision(collision=12014594)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=Assets.AEG237_066_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG237_069_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG237_081_0501, animation_id=0)
    DisableMapCollision(collision=12014594)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12010591))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012591))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12010591)
    SetCameraVibration(
        vibration_id=107,
        anchor_entity=12012581,
        decay_start_distance=50.0,
        decay_end_distance=100.0,
        anchor_type=CoordEntityType.Region,
    )
    ForceAnimation(Assets.AEG237_081_0501, 1, wait_for_completion=True)
    Wait(1.0)
    ForceAnimation(Assets.AEG237_066_0500, 0)
    ForceAnimation(Assets.AEG237_069_0500, 0)
    EnableMapCollision(collision=12014594)
    End()


@RestartOnRest(12012593)
def Event_12012593():
    """Event 12012593"""
    GotoIfFlagDisabled(Label.L0, flag=12010593)
    EndOfAnimation(asset=Assets.AEG237_067_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG237_081_0502, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=Assets.AEG237_067_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG237_081_0502, animation_id=0)
    DisableAsset(Assets.AEG099_600_9000)
    DisableTreasure(asset=Assets.AEG099_600_9000)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12010593))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012593))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12010593)
    ForceAnimation(Assets.AEG237_081_0502, 1, wait_for_completion=True)
    Wait(1.0)
    ForceAnimation(Assets.AEG237_067_0500, 0, wait_for_completion=True)
    EnableAsset(Assets.AEG099_600_9000)
    EnableTreasure(asset=Assets.AEG099_600_9000)
    End()


@RestartOnRest(12012594)
def Event_12012594():
    """Event 12012594"""
    GotoIfFlagDisabled(Label.L0, flag=12010594)
    EndOfAnimation(asset=Assets.AEG237_068_0500, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=Assets.AEG237_068_0500, animation_id=1)
    DisableMapCollision(collision=12014591)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12010594))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012594))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12010594)
    ForceAnimation(Assets.AEG237_068_0500, 0)
    EnableMapCollision(collision=12014591)
    End()


@RestartOnRest(12012595)
def Event_12012595():
    """Event 12012595"""
    GotoIfFlagDisabled(Label.L0, flag=12010595)
    EndOfAnimation(asset=Assets.AEG237_072_0500, animation_id=2)
    EndOfAnimation(asset=Assets.AEG237_081_0503, animation_id=2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(asset=Assets.AEG237_072_0500, animation_id=1)
    EndOfAnimation(asset=Assets.AEG237_081_0503, animation_id=0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12010595))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012595))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12010595)
    ForceAnimation(Assets.AEG237_081_0503, 1)
    Wait(1.0)
    ForceAnimation(Assets.AEG237_072_0500, 0)
    End()


@RestartOnRest(12012421)
def Event_12012421():
    """Event 12012421"""
    EndIffSpecialStandbyEndedFlagEnabled(character=Characters.OnyxLord)
    DisableCharacter(Characters.OnyxLord)
    DisableMapCollision(collision=12014421)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012421))
    AND_1.Add(FlagEnabled(12010591))
    AND_1.Add(FlagEnabled(12010593))
    AND_1.Add(FlagEnabled(12010594))
    AND_4.Add(CharacterHasSpecialEffect(Characters.OnyxLord, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90160))
    AND_5.Add(CharacterHasSpecialEffect(Characters.OnyxLord, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90162))
    AND_6.Add(CharacterHasSpecialEffect(Characters.OnyxLord, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90161))
    AND_7.Add(CharacterHasSpecialEffect(Characters.OnyxLord, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90162))
    AND_8.Add(CharacterHasSpecialEffect(Characters.OnyxLord, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(Characters.OnyxLord, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.OnyxLord, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.OnyxLord, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.OnyxLord, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.OnyxLord, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.OnyxLord, state_info=260))
    OR_2.Add(CharacterHasStateInfo(character=Characters.OnyxLord, state_info=436))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=Characters.OnyxLord, state=True)
    EnableCharacter(Characters.OnyxLord)
    End()


@RestartOnRest(12012220)
def Event_12012220(_, character: uint):
    """Event 12012220"""
    if ThisEventSlotFlagEnabled():
        return
    DisableThisSlotFlag()
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
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    EnableFlag(12012230)


@RestartOnRest(12012231)
def Event_12012231(_, character: uint, seconds: float):
    """Event 12012231"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    DisableGravity(character)
    AddSpecialEffect(character, 2900)
    ForceAnimation(character, 30001, loop=True)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(FlagEnabled(12012230))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    EnableGravity(character)
    ForceAnimation(character, 20001, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    End()


@RestartOnRest(12012249)
def Event_12012249():
    """Event 12012249"""
    OR_10.Add(FlagEnabled(12012247))
    OR_10.Add(FlagEnabled(12012249))
    GotoIfConditionFalse(Label.L0, input_condition=OR_10)
    ForceAnimation(Characters.GiantBall2, 20003)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.GiantBall2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.GiantBall2, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantBall2, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantBall2, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantBall2, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantBall2, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.GiantBall2, state_info=260))
    AND_2.Add(OR_2)
    AND_2.Add(FlagDisabled(12012247))
    
    MAIN.Await(AND_2)
    
    EnableNetworkFlag(12012249)
    EnableAI(Characters.GiantBall2)


@RestartOnRest(12012239)
def Event_12012239():
    """Event 12012239"""
    MAIN.Await(CharacterInsideRegion(character=Characters.GiantBall0, region=12012239))
    
    AddSpecialEffect(Characters.GiantBall0, 16318)
    Wait(1.0)
    
    MAIN.Await(CharacterOutsideRegion(character=Characters.GiantBall0, region=12012239))
    
    AddSpecialEffect(Characters.GiantBall0, 16319)
    Wait(1.0)
    Restart()


@RestartOnRest(12012240)
def Event_12012240():
    """Event 12012240"""
    if FlagEnabled(12012249):
        return
    if FlagEnabled(12012247):
        return
    AND_15.Add(CharacterInsideRegion(character=PLAYER, region=12012247))
    AND_15.Add(FlagDisabled(12012249))
    
    MAIN.Await(AND_15)
    
    Wait(1.0)
    GotoIfFlagEnabled(Label.L0, flag=12012240)
    ForceSpawnerToSpawn(spawner=12013240)
    EnableNetworkFlag(12012240)
    Wait(3.0)
    DisableSpawner(entity=12013240)
    Goto(Label.L10)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=12012241)
    ForceSpawnerToSpawn(spawner=12013241)
    EnableNetworkFlag(12012241)
    Wait(8.0)
    DisableSpawner(entity=12013241)
    Goto(Label.L10)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=12012242)
    ForceSpawnerToSpawn(spawner=12013242)
    EnableNetworkFlag(12012242)
    Wait(5.0)
    DisableSpawner(entity=12013242)
    Goto(Label.L10)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L3, flag=12012243)
    ForceSpawnerToSpawn(spawner=12013243)
    EnableNetworkFlag(12012243)
    Wait(5.0)
    DisableSpawner(entity=12013243)
    Goto(Label.L10)

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagEnabled(Label.L4, flag=12012244)
    ForceSpawnerToSpawn(spawner=12013244)
    EnableNetworkFlag(12012244)
    Wait(8.0)
    DisableSpawner(entity=12013244)
    Goto(Label.L10)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L5, flag=12012245)
    ForceSpawnerToSpawn(spawner=12013245)
    EnableNetworkFlag(12012245)
    Wait(8.0)
    DisableSpawner(entity=12013245)
    Goto(Label.L10)

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L6, flag=12012246)
    ForceSpawnerToSpawn(spawner=12013246)
    EnableNetworkFlag(12012246)
    Wait(3.0)
    DisableSpawner(entity=12013246)
    Goto(Label.L10)

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagEnabled(Label.L1, flag=12012247)
    ForceSpawnerToSpawn(spawner=12013247)
    EnableAI(Characters.GiantBall2)
    ForceAnimation(Characters.GiantBall2, 20003)
    EnableNetworkFlag(12012247)
    DisableSpawner(entity=12013247)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    Restart()


@RestartOnRest(12012256)
def Event_12012256():
    """Event 12012256"""
    AND_15.Add(FlagEnabled(12012256))
    AND_15.Add(FlagDisabled(12012257))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    EndOfAnimation(asset=Assets.AEG237_070_0500, animation_id=0)
    ForceAnimation(Characters.GiantBall1, 20003)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_14.Add(FlagEnabled(12012256))
    AND_14.Add(FlagEnabled(12012257))
    GotoIfConditionFalse(Label.L1, input_condition=AND_14)
    EndOfAnimation(asset=Assets.AEG237_070_0500, animation_id=2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(asset=Assets.AEG237_070_0500, animation_id=2)
    DisableAI(Characters.GiantBall1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012256))
    AND_1.Add(CharacterAlive(Characters.GiantBall1))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12012256)
    ForceAnimation(Assets.AEG237_070_0500, 3)
    ForceAnimation(Characters.GiantBall1, 20003)
    EnableAI(Characters.GiantBall1)


@RestartOnRest(12012257)
def Event_12012257():
    """Event 12012257"""
    OR_15.Add(FlagEnabled(12012257))
    if OR_15:
        return
    AND_1.Add(FlagEnabled(12012256))
    OR_1.Add(CharacterDead(Characters.GiantBall1))
    OR_1.Add(CharacterOutsideRegion(character=PLAYER, region=12012257))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(12012257)
    ForceAnimation(Assets.AEG237_070_0500, 1)


@RestartOnRest(12012288)
def Event_12012288(_, character: uint, character_1: uint, region: uint):
    """Event 12012288"""
    AND_15.Add(CharacterAlive(character_1))
    SkipLinesIfConditionTrue(1, AND_15)
    DisableCharacter(character)
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(PlayerNotInOwnWorld())
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if PlayerInOwnWorld():
        DisableThisSlotFlag()
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16307))
    
    EnableCharacter(character_1)
    EnableAnimations(character_1)
    SetNest(character_1, region=region)
    DisableAnimations(character)
    WaitFrames(frames=5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=900,
        copy_draw_parent=character,
    )
    ForceAnimation(character_1, 63010, skip_transition=True)
    AddSpecialEffect(character_1, 16316)
    Wait(4.5)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    EnableAI(character_1)


@RestartOnRest(12012301)
def Event_12012301():
    """Event 12012301"""
    GotoIfFlagDisabled(Label.L0, flag=12012301)
    RemoveSpecialEffect(12015301, 8081)
    RemoveSpecialEffect(12015301, 8082)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(12015301, 8081)
    AddSpecialEffect(12015301, 8082)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=12012301, min_target_count=0))
    
    RemoveSpecialEffect(12015301, 8081)
    RemoveSpecialEffect(12015301, 8082)
    EnableNetworkFlag(12012301)


@ContinueOnRest(12012506)
def Event_12012506():
    """Event 12012506"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(12040800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9711, entity=Assets.AEG237_018_2000))
    
    MAIN.Await(AND_1)
    
    BanishInvaders(unknown=0)
    EnableFlag(9021)
    if PlayerInOwnWorld():
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=12010000,
            cutscene_flags=0,
            move_to_region=12042506,
            map_id=12040000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
        PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    else:
        PlayCutsceneToPlayerAndWarp(
            cutscene_id=12010000,
            cutscene_flags=0,
            move_to_region=12042508,
            map_id=12040000,
            player_id=10000,
            unk_20_24=0,
            unk_24_25=False,
        )
        PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    WaitFramesAfterCutscene(frames=1)
    End()


@ContinueOnRest(12012507)
def Event_12012507():
    """Event 12012507"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(12040800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9711, entity=Assets.AEG237_018_2000))
    
    MAIN.Await(AND_1)
    
    BanishPhantoms(unknown=0)
    Wait(1.0)
    EnableFlag(9021)
    PlayCutsceneToPlayerAndWarp(
        cutscene_id=12010000,
        cutscene_flags=0,
        move_to_region=12042506,
        map_id=12040000,
        player_id=10000,
        unk_20_24=0,
        unk_24_25=False,
    )
    PlayCutscene(12010001, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.Unknown16, player_id=10000)
    End()


@ContinueOnRest(12010509)
def Event_12010509():
    """Event 12010509"""
    CommonFunc_90005500(
        0,
        flag=12010510,
        flag_1=12010511,
        left=2,
        asset=Assets.AEG239_010_0500,
        asset_1=Assets.AEG239_020_0504,
        obj_act_id=12013511,
        asset_2=Assets.AEG239_020_0505,
        obj_act_id_1=12013512,
        region=12012511,
        region_1=12012512,
        flag_2=12010512,
        flag_3=12010513,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=12010515,
        flag_1=12010516,
        left=3,
        asset=Assets.AEG239_010_0501,
        asset_1=Assets.AEG239_020_0502,
        obj_act_id=12013516,
        asset_2=Assets.AEG239_020_0503,
        obj_act_id_1=12013517,
        region=12012516,
        region_1=12012517,
        flag_2=12010517,
        flag_3=12010518,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=12010520,
        flag_1=12010521,
        left=6,
        asset=Assets.AEG239_010_0502,
        asset_1=Assets.AEG239_020_0500,
        obj_act_id=12013521,
        asset_2=Assets.AEG239_020_0501,
        obj_act_id_1=12013522,
        region=12012521,
        region_1=12012522,
        flag_2=12010522,
        flag_3=12010523,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        12010525,
        12010526,
        9,
        12011525,
        12011526,
        12013526,
        12011527,
        12013527,
        12012526,
        12012527,
        12010527,
        12010528,
        0,
    )


@ContinueOnRest(12010519)
def Event_12010519():
    """Event 12010519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(12010510)
    EnableFlag(12010515)
    EnableFlag(12010520)
    EnableFlag(12010525)


@RestartOnRest(12012530)
def Event_12012530():
    """Event 12012530"""
    RegisterLadder(start_climbing_flag=12010530, stop_climbing_flag=12010531, asset=Assets.AEG239_040_0500)
    RegisterLadder(start_climbing_flag=12010532, stop_climbing_flag=12010533, asset=Assets.AEG027_210_2000)


@RestartOnRest(12012800)
def Event_12012800():
    """Event 12012800"""
    if FlagEnabled(12010800):
        return
    
    MAIN.Await(HealthValue(Characters.DragonkinSoldier0) <= 0)
    
    Kill(Characters.DragonkinSoldier1)
    Kill(Characters.DragonkinSoldier2)
    Wait(4.0)
    PlaySoundEffect(Characters.DragonkinSoldier0, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.DragonkinSoldier0))
    
    KillBossAndDisplayBanner(character=Characters.DragonkinSoldier0, banner_type=BannerType.GreatEnemyFelled)
    EnableFlag(12010800)
    EnableFlag(9109)
    if PlayerInOwnWorld():
        EnableFlag(61109)


@RestartOnRest(12012810)
def Event_12012810():
    """Event 12012810"""
    GotoIfFlagDisabled(Label.L0, flag=12010800)
    DisableCharacter(Characters.DragonkinSoldier0)
    DisableAnimations(Characters.DragonkinSoldier0)
    Kill(Characters.DragonkinSoldier0)
    DisableCharacter(Characters.DragonkinSoldier1)
    DisableAnimations(Characters.DragonkinSoldier1)
    Kill(Characters.DragonkinSoldier1)
    DisableCharacter(Characters.DragonkinSoldier2)
    DisableAnimations(Characters.DragonkinSoldier2)
    Kill(Characters.DragonkinSoldier2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.DragonkinSoldier1)
    DisableAI(Characters.DragonkinSoldier2)
    DisableHealthBar(Characters.DragonkinSoldier1)
    DisableHealthBar(Characters.DragonkinSoldier2)
    ReferDamageToEntity(Characters.DragonkinSoldier1, target_entity=Characters.DragonkinSoldier0)
    ReferDamageToEntity(Characters.DragonkinSoldier2, target_entity=Characters.DragonkinSoldier0)
    EnableImmortality(Characters.DragonkinSoldier1)
    EnableImmortality(Characters.DragonkinSoldier2)
    DisableGravity(Characters.DragonkinSoldier0)
    DisableAnimations(Characters.DragonkinSoldier0)
    DisableCharacter(Characters.DragonkinSoldier2)
    ForceAnimation(Characters.DragonkinSoldier1, 30002, loop=True)
    GotoIfFlagEnabled(Label.L1, flag=12010801)
    DisableCharacter(Characters.DragonkinSoldier0)
    DisableCharacter(Characters.DragonkinSoldier1)
    AND_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012801))
    AND_1.Add(CharacterBackreadEnabled(Characters.DragonkinSoldier1))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=Characters.DragonkinSoldier1, attacker=0))
    OR_2.Add(CharacterHasStateInfo(character=Characters.DragonkinSoldier1, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=Characters.DragonkinSoldier1, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=Characters.DragonkinSoldier1, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=Characters.DragonkinSoldier1, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=Characters.DragonkinSoldier1, state_info=260))
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableCharacter(Characters.DragonkinSoldier0)
    EnableCharacter(Characters.DragonkinSoldier1)
    ForceAnimation(Characters.DragonkinSoldier1, 20002)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_10.Add(FlagEnabled(12012805))
    AND_10.Add(CharacterInsideRegion(character=PLAYER, region=12012800))
    
    MAIN.Await(AND_10)
    
    ForceAnimation(Characters.DragonkinSoldier1, 20002)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    EnableNetworkFlag(12010840)
    Wait(2.0)
    EnableNetworkFlag(12012803)
    Wait(0.10000000149011612)
    EnableNetworkFlag(12010801)
    EnableAI(Characters.DragonkinSoldier1)
    SetNetworkUpdateRate(Characters.DragonkinSoldier1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.DragonkinSoldier0, name=904650000)


@RestartOnRest(12012820)
def Event_12012820():
    """Event 12012820"""
    if FlagEnabled(12010800):
        return
    AND_1.Add(EntityWithinDistance(entity=Characters.DragonkinSoldier2, other_entity=PLAYER, radius=50.0))
    AND_1.Add(CharacterHasSpecialEffect(Characters.DragonkinSoldier2, 13208))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=4651)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12012830)
def Event_12012830():
    """Event 12012830"""
    if FlagEnabled(12010800):
        return
    DisableNetworkSync()
    AND_1.Add(EntityWithinDistance(entity=Characters.DragonkinSoldier2, other_entity=PLAYER, radius=50.0))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(Characters.DragonkinSoldier2, 13208))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=4650)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12012811)
def Event_12012811():
    """Event 12012811"""
    if FlagEnabled(12010800):
        return
    AND_1.Add(CharacterHasSpecialEffect(Characters.DragonkinSoldier1, 13209))
    
    MAIN.Await(AND_1)
    
    EnableFlag(12012811)
    EnableFlag(12012802)
    EnableCharacter(Characters.DragonkinSoldier2)
    DisableAnimations(Characters.DragonkinSoldier2)
    EnableAI(Characters.DragonkinSoldier2)
    SetNetworkUpdateRate(Characters.DragonkinSoldier2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        Characters.DragonkinSoldier2,
        destination=Characters.DragonkinSoldier1,
        destination_type=CoordEntityType.Character,
        model_point=100,
        short_move=True,
    )
    WaitFrames(frames=90)
    DisableCharacter(Characters.DragonkinSoldier1)
    EnableAnimations(Characters.DragonkinSoldier2)


@RestartOnRest(12012812)
def Event_12012812():
    """Event 12012812"""
    if FlagEnabled(12010800):
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=12012812))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(Characters.DragonkinSoldier0, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.DragonkinSoldier1, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(12012849)
def Event_12012849():
    """Event 12012849"""
    CommonFunc_9005811(0, flag=12010800, asset=Assets.AEG099_002_9001, model_point=4, right=12010840)
    CommonFunc_9005822(
        0,
        flag=12010800,
        bgm_boss_conv_param_id=920300,
        flag_1=12012805,
        flag_2=12012806,
        right=12012803,
        flag_3=12012802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=12010800,
        entity=Assets.AEG099_002_9000,
        region=12012800,
        flag_1=12012805,
        character=12015800,
        action_button_id=10000,
        left=12010801,
        region_1=12012801,
    )
    CommonFunc_9005801(
        0,
        flag=12010800,
        entity=Assets.AEG099_002_9000,
        region=12012800,
        flag_1=12012805,
        flag_2=12012806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12010800, asset=Assets.AEG099_002_9000, model_point=5, right=12010801)
    CommonFunc_9005822(0, 12010800, 920300, 12012805, 12012806, 12012803, 12012802, 0, 0)
