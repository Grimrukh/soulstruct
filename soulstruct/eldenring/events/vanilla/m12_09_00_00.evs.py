"""
Regal Ancestor Arena

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
from .entities.m12_09_00_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    Event_12092849()
    Event_12092800()
    Event_12092810()
    Event_12092848()
    Event_12092200(0, character=Characters.Deer0, flag=12092858)
    Event_12092200(1, character=Characters.Deer1, flag=12092858)
    Event_12092200(2, character=Characters.Deer2, flag=12092858)
    Event_12092200(3, character=Characters.Deer3, flag=12092858)
    Event_12092200(4, character=Characters.Deer4, flag=12092858)
    Event_12092200(5, character=Characters.Deer5, flag=12092858)
    Event_12092200(6, character=Characters.Deer6, flag=12092858)
    Event_12092200(7, character=Characters.Boar0, flag=12092858)
    Event_12092200(8, character=Characters.Boar1, flag=12092858)
    Event_12092200(9, character=Characters.Boar2, flag=12092858)
    Event_12092200(10, character=Characters.Boar3, flag=12092858)
    Event_12092200(11, character=Characters.Boar4, flag=12092858)
    Event_12092200(12, character=Characters.Boar5, flag=12092858)
    Event_12092200(13, character=Characters.Boar6, flag=12092858)
    Event_12092200(14, character=Characters.WildMouflon0, flag=12092858)
    Event_12092200(15, character=Characters.WildMouflon1, flag=12092859)
    Event_12092200(16, character=Characters.WildMouflon2, flag=12092858)
    Event_12092200(17, character=Characters.WildMouflon3, flag=12092858)
    Event_12092200(18, character=Characters.WildMouflon4, flag=12092858)
    Event_12092200(19, character=Characters.WildMouflon5, flag=12092858)
    Event_12092200(20, character=Characters.WildMouflon6, flag=12092858)
    Event_12092200(21, character=Characters.Springhare0, flag=12092858)
    Event_12092200(22, character=Characters.Springhare1, flag=12092859)
    Event_12092200(23, character=Characters.Springhare2, flag=12092858)
    Event_12092200(24, character=Characters.Springhare3, flag=12092858)
    Event_12092200(25, character=Characters.Springhare4, flag=12092858)
    Event_12092200(26, character=Characters.Springhare5, flag=12092858)
    Event_12092200(27, character=Characters.Springhare6, flag=12092858)
    Event_12092230(0, flag=12092870, character=Characters.Deer0)
    Event_12092230(1, flag=12092871, character=Characters.Deer1)
    Event_12092230(2, flag=12092872, character=Characters.Deer2)
    Event_12092230(3, flag=12092873, character=Characters.Deer3)
    Event_12092230(4, flag=12092874, character=Characters.Deer4)
    Event_12092230(5, flag=12092875, character=Characters.Deer5)
    Event_12092230(6, flag=12092876, character=Characters.Deer6)
    Event_12092230(7, flag=12092877, character=Characters.Boar0)
    Event_12092230(8, flag=12092878, character=Characters.Boar1)
    Event_12092230(9, flag=12092879, character=Characters.Boar2)
    Event_12092230(10, flag=12092880, character=Characters.Boar3)
    Event_12092230(11, flag=12092881, character=Characters.Boar4)
    Event_12092230(12, flag=12092882, character=Characters.Boar5)
    Event_12092230(13, flag=12092883, character=Characters.Boar6)
    Event_12092230(14, flag=12092884, character=Characters.WildMouflon0)
    Event_12092230(15, flag=12092885, character=Characters.WildMouflon1)
    Event_12092230(16, flag=12092886, character=Characters.WildMouflon2)
    Event_12092230(17, flag=12092887, character=Characters.WildMouflon3)
    Event_12092230(18, flag=12092888, character=Characters.WildMouflon4)
    Event_12092230(19, flag=12092889, character=Characters.WildMouflon5)
    Event_12092230(20, flag=12092890, character=Characters.WildMouflon6)
    Event_12092230(21, flag=12092891, character=Characters.Springhare0)
    Event_12092230(22, flag=12092892, character=Characters.Springhare1)
    Event_12092230(23, flag=12092893, character=Characters.Springhare2)
    Event_12092230(24, flag=12092894, character=Characters.Springhare3)
    Event_12092230(25, flag=12092895, character=Characters.Springhare4)
    Event_12092230(26, flag=12092896, character=Characters.Springhare5)
    Event_12092230(27, flag=12092897, character=Characters.Springhare6)
    Event_12092260(0, flag=12092870, character=Characters.Deer0, character_1=Characters.AncestorSpirit)
    Event_12092260(1, flag=12092871, character=Characters.Deer1, character_1=Characters.AncestorSpirit)
    Event_12092260(2, flag=12092872, character=Characters.Deer2, character_1=Characters.AncestorSpirit)
    Event_12092260(3, flag=12092873, character=Characters.Deer3, character_1=Characters.AncestorSpirit)
    Event_12092260(4, flag=12092874, character=Characters.Deer4, character_1=Characters.AncestorSpirit)
    Event_12092260(5, flag=12092875, character=Characters.Deer5, character_1=Characters.AncestorSpirit)
    Event_12092260(6, flag=12092876, character=Characters.Deer6, character_1=Characters.AncestorSpirit)
    Event_12092260(7, flag=12092877, character=Characters.Boar0, character_1=Characters.AncestorSpirit)
    Event_12092260(8, flag=12092878, character=Characters.Boar1, character_1=Characters.AncestorSpirit)
    Event_12092260(9, flag=12092879, character=Characters.Boar2, character_1=Characters.AncestorSpirit)
    Event_12092260(10, flag=12092880, character=Characters.Boar3, character_1=Characters.AncestorSpirit)
    Event_12092260(11, flag=12092881, character=Characters.Boar4, character_1=Characters.AncestorSpirit)
    Event_12092260(12, flag=12092882, character=Characters.Boar5, character_1=Characters.AncestorSpirit)
    Event_12092260(13, flag=12092883, character=Characters.Boar6, character_1=Characters.AncestorSpirit)
    Event_12092260(14, flag=12092884, character=Characters.WildMouflon0, character_1=Characters.AncestorSpirit)
    Event_12092260(15, flag=12092885, character=Characters.WildMouflon1, character_1=Characters.AncestorSpirit)
    Event_12092260(16, flag=12092886, character=Characters.WildMouflon2, character_1=Characters.AncestorSpirit)
    Event_12092260(17, flag=12092887, character=Characters.WildMouflon3, character_1=Characters.AncestorSpirit)
    Event_12092260(18, flag=12092888, character=Characters.WildMouflon4, character_1=Characters.AncestorSpirit)
    Event_12092260(19, flag=12092889, character=Characters.WildMouflon5, character_1=Characters.AncestorSpirit)
    Event_12092260(20, flag=12092890, character=Characters.WildMouflon6, character_1=Characters.AncestorSpirit)
    Event_12092260(21, flag=12092891, character=Characters.Springhare0, character_1=Characters.AncestorSpirit)
    Event_12092260(22, flag=12092892, character=Characters.Springhare1, character_1=Characters.AncestorSpirit)
    Event_12092260(23, flag=12092893, character=Characters.Springhare2, character_1=Characters.AncestorSpirit)
    Event_12092260(24, flag=12092894, character=Characters.Springhare3, character_1=Characters.AncestorSpirit)
    Event_12092260(25, flag=12092895, character=Characters.Springhare4, character_1=Characters.AncestorSpirit)
    Event_12092260(26, flag=12092896, character=Characters.Springhare5, character_1=Characters.AncestorSpirit)
    Event_12092260(27, flag=12092897, character=Characters.Springhare6, character_1=Characters.AncestorSpirit)
    Event_12092290()
    Event_12092295(0, character=12095200)
    Event_12092854(
        0,
        flag=12092850,
        flag_1=12092851,
        flag_2=12092852,
        flag_3=12092853,
        character=Characters.AncestorSpirit,
        character_1=12095200,
    )
    Event_12092859(
        0,
        flag=12092850,
        flag_1=12092851,
        flag_2=12092852,
        flag_3=12092853,
        first_flag=12092855,
        flag_4=12092856,
        last_flag=12092857,
        character=Characters.AncestorSpirit,
        character_1=12095200,
        character_2=12095201,
        character_3=12095202,
        character_4=12095203,
        character_5=12095204,
        character_6=Characters.Deer0,
        character_7=Characters.Deer1,
        character_8=Characters.Deer2,
        character_9=Characters.Deer3,
        character_10=Characters.Deer4,
        character_11=Characters.Deer5,
        character_12=Characters.Deer6,
        character_13=Characters.Boar0,
        character_14=Characters.Boar1,
        character_15=Characters.Boar2,
        character_16=Characters.Boar3,
        character_17=Characters.Boar4,
        character_18=Characters.Boar5,
        character_19=Characters.Boar6,
        character_20=Characters.WildMouflon0,
        character_21=Characters.WildMouflon1,
        character_22=Characters.WildMouflon2,
        character_23=Characters.WildMouflon3,
        character_24=Characters.WildMouflon4,
        character_25=Characters.WildMouflon5,
        character_26=Characters.WildMouflon6,
        character_27=Characters.Springhare0,
        character_28=Characters.Springhare1,
        character_29=Characters.Springhare2,
        character_30=Characters.Springhare3,
        character_31=Characters.Springhare4,
        character_32=Characters.Springhare5,
        character_33=Characters.Springhare6,
        character_34=12093200,
        character_35=12093201,
        character_36=12093202,
        character_37=12093203,
        character_38=12093204,
        character_39=12093205,
        character_40=12093206,
        character_41=12093220,
        character_42=12093221,
        character_43=12093222,
        character_44=12093223,
        character_45=12093224,
        character_46=12093225,
        character_47=12093226,
        character_48=12093240,
        character_49=12093241,
        character_50=12093242,
        character_51=12093243,
        character_52=12093244,
        character_53=12093245,
        character_54=12093246,
        character_55=12093260,
        character_56=12093261,
        character_57=12093262,
        character_58=12093263,
        character_59=12093264,
        character_60=12093265,
        character_61=12093266,
        flag_5=12092858,
    )
    Event_12092860(
        0,
        flag=12092858,
        character=Characters.AncestorSpirit,
        character_1=12095201,
        character_2=12095202,
        character_3=12095203,
        character_4=12095204,
        character_5=12095200,
    )
    Event_12092861(0, character=Characters.AncestorSpirit)
    Event_12092862(0, character=Characters.AncestorSpirit, character_1=12095200)
    Event_12092863(0, character=Characters.AncestorSpirit, character_1=12095200, flag=12092862)
    Event_12092864(0, character=Characters.AncestorSpirit, character_1=12095200, flag=12092862, flag_1=12092863)
    Event_12092910(0, entity=Characters.Dummy)
    Event_12092865(0, character=Characters.AncestorSpirit)
    Event_12092920(0, left=12092907, owner_entity=Characters.Dummy, source_entity=12092300)
    Event_12092920(1, left=12092907, owner_entity=Characters.Dummy, source_entity=12092301)
    Event_12092920(2, left=12092907, owner_entity=Characters.Dummy, source_entity=12092302)
    Event_12092920(3, left=12092907, owner_entity=Characters.Dummy, source_entity=12092303)
    Event_12092920(4, left=12092907, owner_entity=Characters.Dummy, source_entity=12092304)
    Event_12092920(5, left=12092907, owner_entity=Characters.Dummy, source_entity=12092305)
    Event_12092920(6, left=12092907, owner_entity=Characters.Dummy, source_entity=12092306)
    Event_12092920(7, left=12092907, owner_entity=Characters.Dummy, source_entity=12092307)
    Event_12092920(8, left=12092907, owner_entity=Characters.Dummy, source_entity=12092308)
    Event_12092920(9, left=12092907, owner_entity=Characters.Dummy, source_entity=12092309)
    Event_12092920(10, left=12092907, owner_entity=Characters.Dummy, source_entity=12092310)
    Event_12092920(11, left=12092908, owner_entity=Characters.Dummy, source_entity=12092311)
    Event_12092920(12, left=12092908, owner_entity=Characters.Dummy, source_entity=12092312)
    Event_12092920(13, left=12092908, owner_entity=Characters.Dummy, source_entity=12092313)
    Event_12092920(14, left=12092908, owner_entity=Characters.Dummy, source_entity=12092314)
    Event_12092920(15, left=12092908, owner_entity=Characters.Dummy, source_entity=12092315)
    Event_12092920(16, left=12092908, owner_entity=Characters.Dummy, source_entity=12092316)
    Event_12092920(17, left=12092908, owner_entity=Characters.Dummy, source_entity=12092317)
    Event_12092920(18, left=12092908, owner_entity=Characters.Dummy, source_entity=12092318)
    Event_12092920(19, left=12092908, owner_entity=Characters.Dummy, source_entity=12092319)
    Event_12092920(20, left=12092908, owner_entity=Characters.Dummy, source_entity=12092320)
    Event_12092920(21, left=12092908, owner_entity=Characters.Dummy, source_entity=12092321)
    Event_12092920(22, left=12092908, owner_entity=Characters.Dummy, source_entity=12092322)
    Event_12092920(23, left=12092908, owner_entity=Characters.Dummy, source_entity=12092323)
    Event_12092920(24, left=12092908, owner_entity=Characters.Dummy, source_entity=12092324)
    Event_12092920(25, left=12092908, owner_entity=Characters.Dummy, source_entity=12092325)
    Event_12092920(26, left=12092908, owner_entity=Characters.Dummy, source_entity=12092326)
    Event_12092920(27, left=12092908, owner_entity=Characters.Dummy, source_entity=12092327)
    Event_12092920(28, left=12092908, owner_entity=Characters.Dummy, source_entity=12092328)
    Event_12092920(29, left=12092908, owner_entity=Characters.Dummy, source_entity=12092329)
    Event_12092920(30, left=12092908, owner_entity=Characters.Dummy, source_entity=12092330)
    Event_12092920(31, left=12092909, owner_entity=Characters.Dummy, source_entity=12092331)
    Event_12092920(32, left=12092909, owner_entity=Characters.Dummy, source_entity=12092332)
    Event_12092920(33, left=12092909, owner_entity=Characters.Dummy, source_entity=12092333)
    Event_12092920(34, left=12092909, owner_entity=Characters.Dummy, source_entity=12092334)
    Event_12092920(35, left=12092909, owner_entity=Characters.Dummy, source_entity=12092335)
    Event_12092920(36, left=12092909, owner_entity=Characters.Dummy, source_entity=12092336)
    Event_12092920(37, left=12092909, owner_entity=Characters.Dummy, source_entity=12092337)
    Event_12092920(38, left=12092909, owner_entity=Characters.Dummy, source_entity=12092338)
    Event_12092920(39, left=12092909, owner_entity=Characters.Dummy, source_entity=12092339)
    Event_12092920(40, left=12092909, owner_entity=Characters.Dummy, source_entity=12092340)
    Event_12092920(41, left=12092909, owner_entity=Characters.Dummy, source_entity=12092341)
    Event_12092920(42, left=12092909, owner_entity=Characters.Dummy, source_entity=12092342)
    Event_12092920(43, left=12092909, owner_entity=Characters.Dummy, source_entity=12092343)
    Event_12092920(44, left=12092909, owner_entity=Characters.Dummy, source_entity=12092344)
    Event_12092920(45, left=12092909, owner_entity=Characters.Dummy, source_entity=12092345)
    Event_12092920(46, left=12092909, owner_entity=Characters.Dummy, source_entity=12092346)
    Event_12092920(47, left=12092909, owner_entity=Characters.Dummy, source_entity=12092347)
    Event_12092920(48, left=12092909, owner_entity=Characters.Dummy, source_entity=12092348)
    Event_12092920(49, left=12092909, owner_entity=Characters.Dummy, source_entity=12092349)
    Event_12092920(50, 12092909, 12090290, 12092350)


@ContinueOnRest(12092848)
def Event_12092848():
    """Event 12092848"""
    GotoIfFlagEnabled(Label.L0, flag=12090800)
    DeleteAssetVFX(Assets.AEG099_065_9000, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(12090800))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteAssetVFX(Assets.AEG099_065_9000)
    CreateAssetVFX(Assets.AEG099_065_9000, vfx_id=190, model_point=1300)
    OR_2.Add(MultiplayerPending())
    OR_2.Add(Multiplayer())
    AND_2.Add(not OR_2)
    AND_2.Add(ActionButtonParamActivated(action_button_id=9526, entity=Assets.AEG099_065_9000))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 60460)
    Wait(2.5)
    SetRespawnPoint(respawn_point=12022201)
    SaveRequest()
    WarpToMap(game_map=SIOFRA_RIVER, player_start=12022201)


@ContinueOnRest(12092800)
def Event_12092800():
    """Event 12092800"""
    if FlagEnabled(12090800):
        return
    
    MAIN.Await(HealthRatio(Characters.AncestorSpirit) <= 0.0)
    
    DisableFlag(12092907)
    DisableFlag(12092908)
    DisableFlag(12092909)
    Kill(12095200)
    Wait(2.0)
    PlaySoundEffect(Characters.AncestorSpirit, 77777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.AncestorSpirit))
    
    KillBossAndDisplayBanner(character=Characters.AncestorSpirit, banner_type=BannerType.LegendFelled)
    EnableFlag(12090800)
    EnableFlag(9133)
    if PlayerInOwnWorld():
        EnableFlag(91133)
    AwardItemLot(48000000, host_only=True)


@RestartOnRest(12092810)
def Event_12092810():
    """Event 12092810"""
    GotoIfFlagDisabled(Label.L0, flag=12090800)
    DisableCharacter(Characters.AncestorSpirit)
    DisableAnimations(Characters.AncestorSpirit)
    Kill(Characters.AncestorSpirit)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.AncestorSpirit)
    AND_2.Add(FlagEnabled(12092805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=12092800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.AncestorSpirit)
    SetNetworkUpdateRate(Characters.AncestorSpirit, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.AncestorSpirit, name=904670001)


@ContinueOnRest(12092849)
def Event_12092849():
    """Event 12092849"""
    CommonFunc_9005822(
        0,
        flag=12090800,
        bgm_boss_conv_param_id=467000,
        flag_1=12090805,
        flag_2=12090806,
        right=0,
        flag_3=12092802,
        left=0,
        left_1=0,
    )
    CommonFunc_9005800(
        0,
        flag=12090800,
        entity=Assets.AEG099_002_9000,
        region=12092800,
        flag_1=12092805,
        character=12095800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=12090800,
        entity=Assets.AEG099_002_9000,
        region=12092800,
        flag_1=12092805,
        flag_2=12092806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=12090800, asset=Assets.AEG099_002_9000, model_point=8, right=0)
    CommonFunc_9005822(0, 12090800, 467000, 12092805, 12092806, 0, 12092802, 0, 0)


@RestartOnRest(12092200)
def Event_12092200(_, character: uint, flag: uint):
    """Event 12092200"""
    AND_1.Add(CharacterHasSpecialEffect(character, 13605))
    AND_1.Add(HealthRatio(character) == 0.0)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 13605)
    EnableFlag(flag)
    Restart()


@RestartOnRest(12092230)
def Event_12092230(_, flag: uint, character: uint):
    """Event 12092230"""
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 13605)
    EnableInvincibility(character)
    DisableAnimations(character)
    DisableGravity(character)
    DisableAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(character, 20000, wait_for_completion=True)
    ForceAnimation(character, 20001, loop=True)
    Wait(15.0)
    Restart()


@RestartOnRest(12092260)
def Event_12092260(_, flag: uint, character: uint, character_1: uint):
    """Event 12092260"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(character_1, 13610))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableAnimations(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=260,
        short_move=True,
    )
    AND_15.Add(EntityWithinDistance(entity=20000, other_entity=character, radius=40.0))
    AND_15.Add(EntityBeyondDistance(entity=20000, other_entity=character, radius=7.0))
    SkipLinesIfConditionTrue(2, AND_15)
    ForceAnimation(character_1, 3014)
    SkipLines(1)
    ForceAnimation(character_1, 3037)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_1, special_effect=13601)
    AddSpecialEffect(character_1, 13613)
    AddSpecialEffect(character_1, 13618)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_1, special_effect=13602)
    AddSpecialEffect(character_1, 13614)
    AddSpecialEffect(character_1, 13619)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=3, character=character_1, special_effect=13603)
    AddSpecialEffect(character_1, 13615)
    AddSpecialEffect(character_1, 13620)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character_1, special_effect=13604)
    AddSpecialEffect(character_1, 13616)
    AddSpecialEffect(character_1, 13621)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 20002, wait_for_completion=True)
    DisableAI(character)
    EnableGravity(character)
    DisableCharacter(character)
    DisableInvincibility(character)
    Kill(character)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    EnableAnimations(character_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(12092290)
def Event_12092290():
    """Event 12092290"""
    AND_1.Add(FlagEnabled(12092901))
    AND_1.Add(CharacterHasSpecialEffect(Characters.AncestorSpirit, 13610))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12092901)
    DisableAnimations(Characters.AncestorSpirit)
    Move(
        Characters.AncestorSpirit,
        destination=12092308,
        destination_type=CoordEntityType.Region,
        model_point=0,
        short_move=True,
    )
    ForceAnimation(Characters.AncestorSpirit, 3014)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.AncestorSpirit,
        special_effect=13601,
    )
    AddSpecialEffect(Characters.AncestorSpirit, 13613)
    AddSpecialEffect(Characters.AncestorSpirit, 13618)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.AncestorSpirit,
        special_effect=13602,
    )
    AddSpecialEffect(Characters.AncestorSpirit, 13614)
    AddSpecialEffect(Characters.AncestorSpirit, 13619)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=3,
        character=Characters.AncestorSpirit,
        special_effect=13603,
    )
    AddSpecialEffect(Characters.AncestorSpirit, 13615)
    AddSpecialEffect(Characters.AncestorSpirit, 13620)
    Goto(Label.L0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(
        line_count=2,
        character=Characters.AncestorSpirit,
        special_effect=13604,
    )
    AddSpecialEffect(Characters.AncestorSpirit, 13616)
    AddSpecialEffect(Characters.AncestorSpirit, 13621)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableAnimations(Characters.AncestorSpirit)
    DisableFlag(12092901)
    Restart()


@RestartOnRest(12092295)
def Event_12092295(_, character: uint):
    """Event 12092295"""
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableAnimations(character)


@RestartOnRest(12092854)
def Event_12092854(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, character: uint, character_1: uint):
    """Event 12092854"""
    MAIN.Await(CharacterHasSpecialEffect(character, 13642))
    
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    AND_15.Add(CharacterHasSpecialEffect(character_1, 13605, target_comparison_type=ComparisonType.LessThan, target_count=5.0))
    SkipLinesIfConditionFalse(2, AND_15)
    EnableFlag(flag_2)
    Goto(Label.L0)
    AND_14.Add(CharacterHasSpecialEffect(character_1, 13605, target_comparison_type=ComparisonType.LessThan, target_count=10.0))
    SkipLinesIfConditionFalse(2, AND_14)
    EnableFlag(flag_1)
    Goto(Label.L0)
    AND_13.Add(CharacterHasSpecialEffect(
        character_1,
        13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    SkipLinesIfConditionFalse(2, AND_13)
    EnableFlag(flag)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(character_1, 13643)
    DisableFlag(flag_3)
    Wait(2.0)
    EnableFlag(flag_3)
    Restart()


@RestartOnRest(12092859)
def Event_12092859(
    _,
    flag: uint,
    flag_1: uint,
    flag_2: uint,
    flag_3: uint,
    first_flag: uint,
    flag_4: uint,
    last_flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
    character_6: uint,
    character_7: uint,
    character_8: uint,
    character_9: uint,
    character_10: uint,
    character_11: uint,
    character_12: uint,
    character_13: uint,
    character_14: uint,
    character_15: uint,
    character_16: uint,
    character_17: uint,
    character_18: uint,
    character_19: uint,
    character_20: uint,
    character_21: uint,
    character_22: uint,
    character_23: uint,
    character_24: uint,
    character_25: uint,
    character_26: uint,
    character_27: uint,
    character_28: uint,
    character_29: uint,
    character_30: uint,
    character_31: uint,
    character_32: uint,
    character_33: uint,
    character_34: uint,
    character_35: uint,
    character_36: uint,
    character_37: uint,
    character_38: uint,
    character_39: uint,
    character_40: uint,
    character_41: uint,
    character_42: uint,
    character_43: uint,
    character_44: uint,
    character_45: uint,
    character_46: uint,
    character_47: uint,
    character_48: uint,
    character_49: uint,
    character_50: uint,
    character_51: uint,
    character_52: uint,
    character_53: uint,
    character_54: uint,
    character_55: uint,
    character_56: uint,
    character_57: uint,
    character_58: uint,
    character_59: uint,
    character_60: uint,
    character_61: uint,
    flag_5: uint,
):
    """Event 12092859"""
    if ThisEventSlotFlagDisabled():
        EnableFlag(flag_3)
        Restart()
    
    MAIN.Await(FlagDisabled(flag_3))
    
    DisableFlag(first_flag)
    DisableFlag(flag_4)
    DisableFlag(last_flag)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=13645)
    GotoIfCharacterHasSpecialEffect(
        Label.L0,
        character=character_2,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_8)
    EnableAI(character_8)
    ForceSpawnerToSpawn(spawner=character_36)
    WaitFrames(frames=1)
    AddSpecialEffect(character_8, 13643)
    AddSpecialEffect(character_8, 13605)
    DisableAnimations(character_8)
    Goto(Label.L20)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L1, character=character, special_effect=13646)
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=8,
        character=character_3,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_13)
    EnableAI(character_13)
    ForceSpawnerToSpawn(spawner=character_41)
    WaitFrames(frames=1)
    AddSpecialEffect(character_13, 13643)
    AddSpecialEffect(character_13, 13605)
    DisableAnimations(character_13)
    Goto(Label.L20)
    GotoIfCharacterHasSpecialEffect(
        Label.L1,
        character=character_5,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_27)
    EnableAI(character_27)
    ForceSpawnerToSpawn(spawner=character_55)
    WaitFrames(frames=1)
    AddSpecialEffect(character_27, 13643)
    AddSpecialEffect(character_27, 13605)
    DisableAnimations(character_27)
    Goto(Label.L20)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L2, character=character, special_effect=13647)
    GotoIfCharacterHasSpecialEffect(
        Label.L2,
        character=character_4,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    EnableCharacter(character_20)
    EnableAI(character_20)
    ForceSpawnerToSpawn(spawner=character_48)
    WaitFrames(frames=1)
    AddSpecialEffect(character_20, 13643)
    AddSpecialEffect(character_20, 13605)
    DisableAnimations(character_20)
    Goto(Label.L20)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagDisabled(first_flag):
        GotoIfFlagEnabled(Label.L3, flag=flag_4)
        GotoIfFlagEnabled(Label.L4, flag=last_flag)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_6, special_effect=13605)
    EnableCharacter(character_6)
    EnableAI(character_6)
    ForceSpawnerToSpawn(spawner=character_34)
    WaitFrames(frames=1)
    AddSpecialEffect(character_6, 13643)
    AddSpecialEffect(character_6, 13605)
    DisableAnimations(character_6)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_13, special_effect=13605)
    EnableCharacter(character_13)
    EnableAI(character_13)
    ForceSpawnerToSpawn(spawner=character_41)
    WaitFrames(frames=1)
    AddSpecialEffect(character_13, 13643)
    AddSpecialEffect(character_13, 13605)
    DisableAnimations(character_13)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_20, special_effect=13605)
    EnableCharacter(character_20)
    EnableAI(character_20)
    ForceSpawnerToSpawn(spawner=character_48)
    WaitFrames(frames=1)
    AddSpecialEffect(character_20, 13643)
    AddSpecialEffect(character_20, 13605)
    DisableAnimations(character_20)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_27, special_effect=13605)
    EnableCharacter(character_27)
    EnableAI(character_27)
    ForceSpawnerToSpawn(spawner=character_55)
    WaitFrames(frames=1)
    AddSpecialEffect(character_27, 13643)
    AddSpecialEffect(character_27, 13605)
    DisableAnimations(character_27)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_7, special_effect=13605)
    EnableCharacter(character_7)
    EnableAI(character_7)
    ForceSpawnerToSpawn(spawner=character_35)
    WaitFrames(frames=1)
    AddSpecialEffect(character_7, 13643)
    AddSpecialEffect(character_7, 13605)
    DisableAnimations(character_7)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_14, special_effect=13605)
    EnableCharacter(character_14)
    EnableAI(character_14)
    ForceSpawnerToSpawn(spawner=character_42)
    WaitFrames(frames=1)
    AddSpecialEffect(character_14, 13643)
    AddSpecialEffect(character_14, 13605)
    DisableAnimations(character_14)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_21, special_effect=13605)
    EnableCharacter(character_21)
    EnableAI(character_21)
    ForceSpawnerToSpawn(spawner=character_49)
    WaitFrames(frames=1)
    AddSpecialEffect(character_21, 13643)
    AddSpecialEffect(character_21, 13605)
    DisableAnimations(character_21)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_28, special_effect=13605)
    EnableCharacter(character_28)
    EnableAI(character_28)
    ForceSpawnerToSpawn(spawner=character_56)
    WaitFrames(frames=1)
    AddSpecialEffect(character_28, 13643)
    AddSpecialEffect(character_28, 13605)
    DisableAnimations(character_28)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_8, special_effect=13605)
    EnableCharacter(character_8)
    EnableAI(character_8)
    ForceSpawnerToSpawn(spawner=character_36)
    WaitFrames(frames=1)
    AddSpecialEffect(character_8, 13643)
    AddSpecialEffect(character_8, 13605)
    DisableAnimations(character_8)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_15, special_effect=13605)
    EnableCharacter(character_15)
    EnableAI(character_15)
    ForceSpawnerToSpawn(spawner=character_43)
    WaitFrames(frames=1)
    AddSpecialEffect(character_15, 13643)
    AddSpecialEffect(character_15, 13605)
    DisableAnimations(character_15)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_22, special_effect=13605)
    EnableCharacter(character_22)
    EnableAI(character_22)
    ForceSpawnerToSpawn(spawner=character_50)
    WaitFrames(frames=1)
    AddSpecialEffect(character_22, 13643)
    AddSpecialEffect(character_22, 13605)
    DisableAnimations(character_22)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_29, special_effect=13605)
    EnableCharacter(character_29)
    EnableAI(character_29)
    ForceSpawnerToSpawn(spawner=character_57)
    WaitFrames(frames=1)
    AddSpecialEffect(character_29, 13643)
    AddSpecialEffect(character_29, 13605)
    DisableAnimations(character_29)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_23, special_effect=13605)
    EnableCharacter(character_23)
    EnableAI(character_23)
    ForceSpawnerToSpawn(spawner=character_51)
    WaitFrames(frames=1)
    AddSpecialEffect(character_23, 13643)
    AddSpecialEffect(character_23, 13605)
    DisableAnimations(character_23)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_9, special_effect=13605)
    EnableCharacter(character_9)
    EnableAI(character_9)
    ForceSpawnerToSpawn(spawner=character_37)
    WaitFrames(frames=1)
    AddSpecialEffect(character_9, 13643)
    AddSpecialEffect(character_9, 13605)
    DisableAnimations(character_9)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_30, special_effect=13605)
    EnableCharacter(character_30)
    EnableAI(character_30)
    ForceSpawnerToSpawn(spawner=character_58)
    WaitFrames(frames=1)
    AddSpecialEffect(character_30, 13643)
    AddSpecialEffect(character_30, 13605)
    DisableAnimations(character_30)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_16, special_effect=13605)
    EnableCharacter(character_16)
    EnableAI(character_16)
    ForceSpawnerToSpawn(spawner=character_44)
    WaitFrames(frames=1)
    AddSpecialEffect(character_16, 13643)
    AddSpecialEffect(character_16, 13605)
    DisableAnimations(character_16)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_24, special_effect=13605)
    EnableCharacter(character_24)
    EnableAI(character_24)
    ForceSpawnerToSpawn(spawner=character_52)
    WaitFrames(frames=1)
    AddSpecialEffect(character_24, 13643)
    AddSpecialEffect(character_24, 13605)
    DisableAnimations(character_24)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_10, special_effect=13605)
    EnableCharacter(character_10)
    EnableAI(character_10)
    ForceSpawnerToSpawn(spawner=character_38)
    WaitFrames(frames=1)
    AddSpecialEffect(character_10, 13643)
    AddSpecialEffect(character_10, 13605)
    DisableAnimations(character_10)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_31, special_effect=13605)
    EnableCharacter(character_31)
    EnableAI(character_31)
    ForceSpawnerToSpawn(spawner=character_59)
    WaitFrames(frames=1)
    AddSpecialEffect(character_31, 13643)
    AddSpecialEffect(character_31, 13605)
    DisableAnimations(character_31)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_17, special_effect=13605)
    EnableCharacter(character_17)
    EnableAI(character_17)
    ForceSpawnerToSpawn(spawner=character_45)
    WaitFrames(frames=1)
    AddSpecialEffect(character_17, 13643)
    AddSpecialEffect(character_17, 13605)
    DisableAnimations(character_17)
    Goto(Label.L20)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_32, special_effect=13605)
    EnableCharacter(character_32)
    EnableAI(character_32)
    ForceSpawnerToSpawn(spawner=character_60)
    WaitFrames(frames=1)
    AddSpecialEffect(character_32, 13643)
    AddSpecialEffect(character_32, 13605)
    DisableAnimations(character_32)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_25, special_effect=13605)
    EnableCharacter(character_25)
    EnableAI(character_25)
    ForceSpawnerToSpawn(spawner=character_53)
    WaitFrames(frames=1)
    AddSpecialEffect(character_25, 13643)
    AddSpecialEffect(character_25, 13605)
    DisableAnimations(character_25)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_18, special_effect=13605)
    EnableCharacter(character_18)
    EnableAI(character_18)
    ForceSpawnerToSpawn(spawner=character_46)
    WaitFrames(frames=1)
    AddSpecialEffect(character_18, 13643)
    AddSpecialEffect(character_18, 13605)
    DisableAnimations(character_18)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_11, special_effect=13605)
    EnableCharacter(character_11)
    EnableAI(character_11)
    ForceSpawnerToSpawn(spawner=character_39)
    WaitFrames(frames=1)
    AddSpecialEffect(character_11, 13643)
    AddSpecialEffect(character_11, 13605)
    DisableAnimations(character_11)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_33, special_effect=13605)
    EnableCharacter(character_33)
    EnableAI(character_33)
    ForceSpawnerToSpawn(spawner=character_61)
    WaitFrames(frames=1)
    AddSpecialEffect(character_33, 13643)
    AddSpecialEffect(character_33, 13605)
    DisableAnimations(character_33)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_26, special_effect=13605)
    EnableCharacter(character_26)
    EnableAI(character_26)
    ForceSpawnerToSpawn(spawner=character_54)
    WaitFrames(frames=1)
    AddSpecialEffect(character_26, 13643)
    AddSpecialEffect(character_26, 13605)
    DisableAnimations(character_26)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_19, special_effect=13605)
    EnableCharacter(character_19)
    EnableAI(character_19)
    ForceSpawnerToSpawn(spawner=character_47)
    WaitFrames(frames=1)
    AddSpecialEffect(character_19, 13643)
    AddSpecialEffect(character_19, 13605)
    DisableAnimations(character_19)
    Goto(Label.L20)
    SkipLinesIfCharacterHasSpecialEffect(line_count=8, character=character_12, special_effect=13605)
    EnableCharacter(character_12)
    EnableAI(character_12)
    ForceSpawnerToSpawn(spawner=character_40)
    WaitFrames(frames=1)
    AddSpecialEffect(character_12, 13643)
    AddSpecialEffect(character_12, 13605)
    DisableAnimations(character_12)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(flag_5)
    AND_10.Add(FlagEnabled(flag))
    AND_10.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=6.0,
    ))
    AND_11.Add(FlagEnabled(flag_1))
    AND_11.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=8.0,
    ))
    AND_12.Add(FlagEnabled(flag_2))
    AND_12.Add(CharacterHasSpecialEffect(
        character_1,
        13643,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=10.0,
    ))
    OR_10.Add(AND_10)
    OR_10.Add(AND_11)
    OR_10.Add(AND_12)
    SkipLinesIfConditionFalse(2, OR_10)
    EnableFlag(flag_3)
    RemoveSpecialEffect(character_1, 13643)
    Restart()


@RestartOnRest(12092860)
def Event_12092860(
    _,
    flag: uint,
    character: uint,
    character_1: uint,
    character_2: uint,
    character_3: uint,
    character_4: uint,
    character_5: uint,
):
    """Event 12092860"""
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterHasSpecialEffect(character_1, 13605, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_1)
    AddSpecialEffect(character, 13606)
    SkipLines(1)
    RemoveSpecialEffect(character, 13606)
    AND_2.Add(CharacterHasSpecialEffect(character_2, 13605, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_2)
    AddSpecialEffect(character, 13607)
    SkipLines(1)
    RemoveSpecialEffect(character, 13607)
    AND_3.Add(CharacterHasSpecialEffect(character_3, 13605, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_3)
    AddSpecialEffect(character, 13608)
    SkipLines(1)
    RemoveSpecialEffect(character, 13608)
    AND_4.Add(CharacterHasSpecialEffect(character_4, 13605, target_count=0.0))
    SkipLinesIfConditionTrue(2, AND_4)
    AddSpecialEffect(character, 13609)
    SkipLines(1)
    RemoveSpecialEffect(character, 13609)
    AND_5.Add(CharacterHasSpecialEffect(
        character_5,
        13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=5.0,
    ))
    SkipLinesIfConditionTrue(2, AND_5)
    AddSpecialEffect(character, 13625)
    SkipLines(1)
    RemoveSpecialEffect(character, 13625)
    DisableFlag(12092907)
    DisableFlag(12092908)
    DisableFlag(12092909)
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=3,
        character=character_5,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=20,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=4,
        character=character_5,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
        target_count=13,
    )
    SkipLinesIfCharacterHasSpecialEffect(
        line_count=5,
        character=character_5,
        special_effect=13605,
        target_comparison_type=ComparisonType.GreaterThanOrEqual,
    )
    SkipLines(5)
    EnableFlag(12092909)
    SkipLines(3)
    EnableFlag(12092908)
    SkipLines(1)
    EnableFlag(12092907)
    Restart()


@RestartOnRest(12092861)
def Event_12092861(_, character: uint):
    """Event 12092861"""
    MAIN.Await(CharacterHasSpecialEffect(character, 13623))
    
    EnableAnimations(character)
    ReplanAI(character)
    Restart()


@RestartOnRest(12092862)
def Event_12092862(_, character: uint, character_1: uint):
    """Event 12092862"""
    MAIN.Await(CharacterHasSpecialEffect(character, 13624))
    
    AddSpecialEffect(character, 13632)
    AddSpecialEffect(character, 13646)
    AddSpecialEffect(character_1, 13617)
    Kill(character_1)
    Wait(1.0)
    DisableThisSlotFlag()
    EnableFlag(12092802)


@RestartOnRest(12092863)
def Event_12092863(_, character: uint, character_1: uint, flag: uint):
    """Event 12092863"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterHasSpecialEffect(character, 13624))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 13633)
    AddSpecialEffect(character, 13647)
    AddSpecialEffect(character_1, 13617)
    Kill(character_1)
    Wait(1.0)
    DisableThisSlotFlag()


@RestartOnRest(12092864)
def Event_12092864(_, character: uint, character_1: uint, flag: uint, flag_1: uint):
    """Event 12092864"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 13624))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 13634)
    AddSpecialEffect(character_1, 13617)
    Kill(character_1)
    Wait(1.0)
    Restart()


@RestartOnRest(12092865)
def Event_12092865(_, character: uint):
    """Event 12092865"""
    MAIN.Await(CharacterHasSpecialEffect(character, 13624))
    
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092300,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092301,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092302,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092303,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092304,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092305,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092306,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092307,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092308,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092309,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092310,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092311,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092312,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092313,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092314,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092315,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092316,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092317,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092318,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092319,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092320,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092321,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092322,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092323,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092324,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092325,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092326,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092327,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092328,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092329,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092330,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092331,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092332,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092333,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092334,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092335,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092336,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092337,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092338,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092339,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092340,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092341,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092342,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092343,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092344,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092345,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092346,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092347,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092348,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092349,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=Characters.Dummy,
        source_entity=12092350,
        model_point=-1,
        behavior_id=246700910,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@RestartOnRest(12092910)
def Event_12092910(_, entity: uint):
    """Event 12092910"""
    CreateProjectileOwner(entity=entity)


@RestartOnRest(12092920)
def Event_12092920(_, left: uint, owner_entity: uint, source_entity: uint):
    """Event 12092920"""
    SkipLinesIfUnsignedEqual(2, left=left, right=12092908)
    SkipLinesIfUnsignedEqual(2, left=left, right=12092909)
    OR_1.Add(FlagEnabled(12092907))
    OR_1.Add(FlagEnabled(12092908))
    OR_1.Add(FlagEnabled(12092909))
    AND_1.Add(CharacterAlive(Characters.AncestorSpirit))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ShootProjectile(
        owner_entity=owner_entity,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=246700900,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLinesIfFlagEnabled(3, 12092908)
    SkipLinesIfFlagEnabled(4, 12092909)
    WaitRandomSeconds(min_seconds=8.0, max_seconds=10.0)
    SkipLines(3)
    WaitRandomSeconds(min_seconds=6.0, max_seconds=8.0)
    SkipLines(1)
    WaitRandomSeconds(min_seconds=4.0, max_seconds=6.0)
    Restart()
