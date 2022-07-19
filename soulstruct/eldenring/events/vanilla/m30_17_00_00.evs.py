"""
Giant-Conquering Hero's Grave

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
from .entities.m30_17_00_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=301700, asset=Assets.AEG099_060_9000)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9000, vfx_id=100, model_point=800, right=0)
    CommonFunc_90005525(0, flag=30170570, asset=Assets.AEG027_157_0500)
    CommonFunc_90005620(
        0,
        flag=30170560,
        asset=Assets.AEG027_079_9000,
        asset_1=Assets.AEG027_216_9000,
        asset_2=0,
        left_flag=30172560,
        cancel_flag__right_flag=30172561,
        right=30172562,
    )
    CommonFunc_90005621(0, flag=30170560, asset=Assets.AEG099_272_9000)
    CommonFunc_90005620(
        0,
        flag=30170565,
        asset=Assets.AEG027_079_9001,
        asset_1=Assets.AEG027_216_9001,
        asset_2=0,
        left_flag=30172565,
        cancel_flag__right_flag=30172566,
        right=30172567,
    )
    CommonFunc_90005621(0, flag=30170565, asset=Assets.AEG099_272_9001)
    Event_30172400(0, character=Characters.Imp0)
    Event_30172400(1, character=Characters.Imp1)
    Event_30172400(2, character=30170202)
    CommonFunc_90005261(0, character=30170223, region=30172223, radius=15.0, seconds=0.0, animation_id=0)
    CommonFunc_90005200(
        0,
        character=Characters.Imp0,
        animation_id=30002,
        animation_id_1=20002,
        region=30172450,
        seconds=0.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Imp1,
        animation_id=30002,
        animation_id_1=20002,
        region=30172450,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005261(2, character=30170202, region=30172450, radius=7.0, seconds=0.0, animation_id=0)
    Event_30172400(3, character=Characters.Imp2)
    Event_30172400(4, character=Characters.Imp3)
    Event_30172400(5, character=30170206)
    CommonFunc_90005200(
        0,
        character=Characters.Imp2,
        animation_id=30000,
        animation_id_1=20000,
        region=30172204,
        seconds=4.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Imp3,
        animation_id=30000,
        animation_id_1=20000,
        region=30172204,
        seconds=3.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        2,
        character=30170206,
        animation_id=30000,
        animation_id_1=20000,
        region=30172204,
        seconds=4.199999809265137,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30172400(6, character=Characters.Imp5)
    Event_30172400(7, character=Characters.Imp6)
    Event_30172400(8, character=Characters.Imp4)
    CommonFunc_90005250(0, character=Characters.Imp4, region=30172315, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Imp4, region=30172217, seconds=0.0, animation_id=3005)
    CommonFunc_90005200(
        0,
        character=Characters.Imp5,
        animation_id=30002,
        animation_id_1=20002,
        region=30172210,
        seconds=5.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        1,
        character=Characters.Imp6,
        animation_id=30002,
        animation_id_1=20002,
        region=30172210,
        seconds=5.5,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30172400(9, character=30170215)
    Event_30172402(0, character=30170216, region=30172202)
    Event_30172400(10, character=30170316)
    CommonFunc_90005250(0, character=30170215, region=30172221, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170216, region=30172201, seconds=0.0, animation_id=-1)
    Event_30172311()
    CommonFunc_90005250(0, character=30170317, region=30172318, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170316, region=30172318, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170215, region=30172214, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170300, region=30172300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(1, character=30170301, region=30172300, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170305, region=30172305, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170306, region=30172306, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170309, region=30172309, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.FireMonk1, region=30172350, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.FireMonk0, region=30172310, seconds=0.0, animation_id=3015)
    CommonFunc_90005261(0, character=30170314, region=30172315, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005261(1, character=30170315, region=30172315, radius=5.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.FireMonk2, region=30172315, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Imp1, region=30172223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.Imp0, region=30172223, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(1, character=30170311, region=30172353, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(2, character=30170312, region=30172353, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.FireMonk0,
        animation_id=30000,
        animation_id_1=20000,
        region=30172353,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30172400(12, character=Characters.ErdtreeBurialWatchdog0)
    Event_30172400(13, character=Characters.ErdtreeBurialWatchdog1)
    Event_30172400(14, character=Characters.ErdtreeBurialWatchdog2)
    CommonFunc_90005250(1, character=Characters.ErdtreeBurialWatchdog0, region=30172451, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(1, character=Characters.ErdtreeBurialWatchdog1, region=30172216, seconds=0.0, animation_id=3025)
    CommonFunc_90005250(1, character=Characters.ErdtreeBurialWatchdog2, region=30172450, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170351, region=30172351, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=30170351, region=30172352, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=Characters.FireMonk2,
        animation_id=30001,
        animation_id_1=20001,
        region=30172315,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.FirePrelate, region=30172353, seconds=0.0, animation_id=-1)
    CommonFunc_90005200(
        0,
        character=30170450,
        animation_id=30000,
        animation_id_1=20000,
        region=30172451,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Troll,
        animation_id=30000,
        animation_id_1=20000,
        region=30172410,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30172400(11, character=Characters.Troll)
    CommonFunc_90005300(0, flag=30170400, character=Characters.Troll, item_lot_param_id=0, seconds=0.0, left=0)
    CommonFunc_90005652(0, flag=30170540, asset=Assets.AEG027_041_0500, flag_1=30170400)
    CommonFunc_90005651(0, flag=30170540, anchor_entity=Assets.AEG027_041_0500)
    Event_30172600()
    CommonFunc_90005501(
        0,
        flag=30170530,
        flag_1=30170531,
        left=4,
        asset=Assets.AEG027_038_0500,
        asset_1=Assets.AEG027_002_0502,
        asset_2=Assets.AEG027_002_0503,
        flag_2=30170532,
    )
    CommonFunc_90005501(
        0,
        flag=30170510,
        flag_1=30171510,
        left=1,
        asset=30171510,
        asset_1=30171511,
        asset_2=30171512,
        flag_2=30170511,
    )
    CommonFunc_90005501(
        0,
        flag=30170515,
        flag_1=30170516,
        left=0,
        asset=Assets.AEG027_065_0500,
        asset_1=Assets.AEG027_002_0500,
        asset_2=Assets.AEG027_002_0501,
        flag_2=30170517,
    )
    Event_30172510()
    CommonFunc_90005513(
        0,
        flag=30170542,
        asset=Assets.AEG027_056_0500,
        asset_1=Assets.AEG027_002_0504,
        obj_act_id=30173543,
        obj_act_id_1=27115,
        animation_id=0,
        animation_id_1=0,
    )
    Event_30172520()
    CommonFunc_90005680(
        0,
        flag=30170500,
        flag_1=30170501,
        flag_2=30170502,
        flag_3=30170503,
        asset=Assets.AEG027_051_0500,
    )
    CommonFunc_90005680(
        0,
        flag=30170500,
        flag_1=30170501,
        flag_2=30170502,
        flag_3=30170503,
        asset=Assets.AEG027_051_0500,
    )
    CommonFunc_90005681(
        0,
        flag=30170500,
        flag_1=30170501,
        flag_2=30170502,
        flag_3=30170503,
        attacked_entity=Assets.AEG027_051_0500,
    )
    Event_30172500()
    Event_30172525()
    Event_30172580()
    Event_30172800()
    Event_30172810()
    Event_30172849()
    Event_30122811()
    CommonFunc_90005646(
        0,
        flag=30170800,
        left_flag=30172840,
        cancel_flag__right_flag=30172841,
        asset=Assets.AEG099_065_9000,
        player_start=30172840,
        area_id=30,
        block_id=17,
        cc_id=0,
        dd_id=0,
    )
    CommonFunc_91005600(0, flag=30172800, asset=30171695, model_point=5)
    Event_16002520(0, flag=30170620, asset=30171620)
    Event_30170050()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_30170519()


@NeverRestart(30170050)
def Event_30170050():
    """Event 30170050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30170500)


@RestartOnRest(30172250)
def Event_30172250(_, flag: uint, asset: uint, flag_1: uint):
    """Event 30172250"""
    if FlagEnabled(flag):
        return
    DisableAssetActivation(asset, obj_act_id=-1)
    GotoIfFlagDisabled(Label.L0, flag=flag_1)
    EnableAssetActivation(asset, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableAssetActivation(asset, obj_act_id=-1)


@RestartOnRest(30172200)
def Event_30172200(_, character: uint):
    """Event 30172200"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 17153)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30172200))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 17153)
    AddSpecialEffect(character, 17152)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30172311)
def Event_30172311():
    """Event 30172311"""
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=30172316))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=30170316, attacker=0))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    ForceAnimation(30170316, 3004, wait_for_completion=True)
    SetNetworkFlagState(FlagType.RelativeToThisEventSlot, 0, state=FlagSetting.On)


@RestartOnRest(30172400)
def Event_30172400(_, character: uint):
    """Event 30172400"""
    OR_2.Add(CharacterDead(character))
    OR_2.Add(ThisEventSlotFlagEnabled())
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4320)
    DisableAnimations(character)
    OR_1.Add(CharacterInsideRegion(character=character, region=30172405))
    AND_1.Add(CharacterInsideRegion(character=character, region=30172406))
    AND_1.Add(FlagEnabled(30170526))
    OR_1.Add(AND_1)
    AND_2.Add(CharacterInsideRegion(character=character, region=30172407))
    AND_2.Add(FlagEnabled(30170521))
    OR_1.Add(AND_2)
    AND_3.Add(CharacterInsideRegion(character=character, region=30172408))
    AND_3.Add(FlagEnabled(30170522))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisableThisSlotFlag()
    AddSpecialEffect(character, 5881)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character, 5882)
    RemoveSpecialEffect(character, 5880)
    AddSpecialEffect(character, 4321)
    EnableAnimations(character)
    End()


@RestartOnRest(30172401)
def Event_30172401(_, character: uint):
    """Event 30172401"""
    OR_2.Add(CharacterDead(character))
    OR_2.Add(ThisEventSlotFlagEnabled())
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AddSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4320)
    EnableInvincibility(character)
    DisableAnimations(character)
    OR_1.Add(CharacterInsideRegion(character=character, region=30172405))
    AND_1.Add(CharacterInsideRegion(character=character, region=30172406))
    AND_1.Add(FlagEnabled(30170526))
    OR_1.Add(AND_1)
    AND_2.Add(CharacterInsideRegion(character=character, region=30172407))
    AND_2.Add(FlagEnabled(30170521))
    OR_1.Add(AND_2)
    AND_3.Add(CharacterInsideRegion(character=character, region=30172408))
    AND_3.Add(FlagEnabled(30170522))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4321)
    DisableInvincibility(character)
    EnableAnimations(character)
    End()


@RestartOnRest(30172402)
def Event_30172402(_, character: uint, region: uint):
    """Event 30172402"""
    OR_2.Add(CharacterDead(character))
    OR_2.Add(ThisEventSlotFlagEnabled())
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=0))
    EnableSpawner(entity=30173216)
    Wait(4.0)
    AddSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4320)
    EnableInvincibility(character)
    DisableAnimations(character)
    OR_1.Add(CharacterInsideRegion(character=character, region=30172405))
    AND_1.Add(CharacterInsideRegion(character=character, region=30172406))
    AND_1.Add(FlagEnabled(30170526))
    OR_1.Add(AND_1)
    AND_2.Add(CharacterInsideRegion(character=character, region=30172407))
    AND_2.Add(FlagEnabled(30170521))
    OR_1.Add(AND_2)
    AND_3.Add(CharacterInsideRegion(character=character, region=30172408))
    AND_3.Add(FlagEnabled(30170522))
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    RemoveSpecialEffect(character, 10120)
    AddSpecialEffect(character, 4321)
    DisableInvincibility(character)
    EnableAnimations(character)
    End()


@NeverRestart(30172500)
def Event_30172500():
    """Event 30172500"""
    CommonFunc_90005681(
        0,
        flag=30170500,
        flag_1=30170501,
        flag_2=30170502,
        flag_3=30170503,
        attacked_entity=Assets.AEG027_051_0500,
    )
    if FlagEnabled(57):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105070,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(56):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105060,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(55):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105050,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(54):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105040,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(53):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105030,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(52):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105020,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(51):
        CommonFunc_90005682(
            0,
            flag=30170502,
            source_entity=Assets.AEG027_051_0500,
            region=30172500,
            owner_entity=Characters.TalkDummy0,
            behavior_id=801105010,
            behavior_id_1=801105005,
            model_point=101,
            model_point_1=104,
            model_point_2=100,
            model_point_3=0,
        )
    if FlagEnabled(50):
        CommonFunc_90005682(0, 30170502, 30171500, 30172500, 30170500, 801105000, 801105005, 101, 104, 100, 0)


@NeverRestart(30172501)
def Event_30172501(_, flag: uint, flag_1: uint, flag_2: uint, flag_3: uint, attacked_entity: uint):
    """Event 30172501"""
    if FlagDisabled(30170504):
        GotoIfFlagDisabled(Label.L20, flag=30170504)
    AND_13.Add(FlagEnabled(flag))
    AND_13.Add(FlagEnabled(flag_1))
    OR_15.Add(AND_13)
    AND_14.Add(FlagDisabled(flag))
    AND_14.Add(FlagDisabled(flag_1))
    OR_15.Add(AND_14)
    AND_15.Add(OR_15)
    AND_15.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L9, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    OR_1.Add(FlagDisabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_2.Add(AND_2)
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    
    MAIN.Await(OR_4)
    
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    ForceAnimation(attacked_entity, 21, wait_for_completion=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_5.Add(FlagEnabled(flag))
    AND_6.Add(FlagDisabled(flag_1))
    AND_6.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=20000))
    OR_6.Add(AND_6)
    OR_8.Add(OR_5)
    OR_8.Add(OR_6)
    
    MAIN.Await(OR_8)

    # --- Label 20 --- #
    DefineLabel(20)
    EnableFlag(30170504)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=2,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    EnableNetworkFlag(flag)
    EnableNetworkFlag(flag_3)
    EnableFlag(flag_1)
    ForceAnimation(attacked_entity, 12, wait_for_completion=True)
    SkipLinesIfMapDoesNotHaveUpdatePermission(
        line_count=1,
        unk_state=False,
        game_map=(0, 0, 0, 0),
    )
    DisableNetworkFlag(flag_3)
    EnableFlag(flag_2)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    
    MAIN.Await(FlagDisabled(flag_3))
    
    Restart()


@NeverRestart(30172502)
def Event_30172502(
    _,
    flag: uint,
    source_entity: uint,
    region: uint,
    owner_entity: uint,
    behavior_id: int,
    behavior_id_1: int,
    model_point: int,
    model_point_1: int,
    model_point_2: int,
    model_point_3: int,
):
    """Event 30172502"""
    AND_1.Add(FlagEnabled(flag))
    if UnsignedNotEqual(left=region, right=0):
        AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    CreateProjectileOwner(entity=owner_entity)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=model_point, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=801105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point,
            behavior_id=801105005,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=model_point_1, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=801105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_1,
            behavior_id=801105005,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=model_point_2, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=801105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_2,
            behavior_id=801105005,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfValueComparison(Label.L4, comparison_type=ComparisonType.Equal, left=model_point_3, right=0)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=801105000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if ValueNotEqual(left=behavior_id_1, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=behavior_id_1,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    else:
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            model_point=model_point_3,
            behavior_id=801105005,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 4 --- #
    DefineLabel(4)
    Wait(7.199999809265137)
    Restart()


@NeverRestart(30172510)
def Event_30172510():
    """Event 30172510"""
    CommonFunc_90005500(
        0,
        flag=30170510,
        flag_1=30171510,
        left=1,
        asset=30171510,
        asset_1=30171511,
        obj_act_id=30173511,
        asset_2=30171512,
        obj_act_id_1=30173512,
        region=30172511,
        region_1=30172512,
        flag_2=30170511,
        flag_3=30172512,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        flag=30170515,
        flag_1=30171516,
        left=0,
        asset=Assets.AEG027_065_0500,
        asset_1=Assets.AEG027_002_0500,
        obj_act_id=30173516,
        asset_2=Assets.AEG027_002_0501,
        obj_act_id_1=30173517,
        region=30172516,
        region_1=30172517,
        flag_2=30170517,
        flag_3=30172517,
        left_1=0,
    )
    CommonFunc_90005500(
        0,
        30170530,
        30170531,
        4,
        30171530,
        30171531,
        30173531,
        30171532,
        30173532,
        30172531,
        30172532,
        30170532,
        30172532,
        0,
    )


@NeverRestart(30170519)
def Event_30170519():
    """Event 30170519"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30170530)
    EnableFlag(30170510)
    EnableFlag(30170515)


@RestartOnRest(30172520)
def Event_30172520():
    """Event 30172520"""
    GotoIfFlagDisabled(Label.L0, flag=30170515)
    
    MAIN.Await(FlagEnabled(30170515))
    
    Wait(4.0)
    DeleteVFX(30172403)
    DisableFlag(30170522)
    Wait(6.0)
    CreateVFX(30172402)
    EnableFlag(30170521)
    
    MAIN.Await(FlagDisabled(30170515))

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(3.0)
    DeleteVFX(30172402)
    DisableFlag(30170521)
    Wait(9.0)
    CreateVFX(30172403)
    EnableFlag(30170522)
    
    MAIN.Await(FlagEnabled(30170515))
    
    Restart()


@RestartOnRest(30172525)
def Event_30172525():
    """Event 30172525"""
    MAIN.Await(FlagEnabled(30170500))
    
    Wait(3.0)
    CreateVFX(30172401)
    EnableFlag(30170526)
    
    MAIN.Await(FlagDisabled(30170500))
    
    Wait(0.30000001192092896)
    DeleteVFX(30172401)
    DisableFlag(30170526)
    Restart()


@NeverRestart(30172580)
def Event_30172580():
    """Event 30172580"""
    RegisterLadder(start_climbing_flag=30170580, stop_climbing_flag=30170581, asset=Assets.AEG027_009_0500)
    RegisterLadder(start_climbing_flag=30170582, stop_climbing_flag=30170583, asset=Assets.AEG027_064_0500)


@RestartOnRest(30172600)
def Event_30172600():
    """Event 30172600"""
    if FlagEnabled(30170400):
        return
    
    MAIN.Await(CharacterDead(Characters.Troll))
    
    EnableFlag(30170400)
    End()


@RestartOnRest(30172800)
def Event_30172800():
    """Event 30172800"""
    if FlagEnabled(30170800):
        return
    
    MAIN.Await(HealthValue(Characters.AncientHeroofZamor) <= 0)
    
    Wait(4.0)
    PlaySoundEffect(Characters.AncientHeroofZamor, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.AncientHeroofZamor))
    
    KillBossAndDisplayBanner(character=Characters.AncientHeroofZamor, banner_type=BannerType.EnemyFelled)
    EnableFlag(30170800)
    EnableFlag(9217)
    if PlayerInOwnWorld():
        EnableFlag(61217)


@RestartOnRest(30172810)
def Event_30172810():
    """Event 30172810"""
    GotoIfFlagDisabled(Label.L0, flag=30170800)
    DisableCharacter(Characters.AncientHeroofZamor)
    DisableAnimations(Characters.AncientHeroofZamor)
    Kill(Characters.AncientHeroofZamor)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.AncientHeroofZamor)
    AND_2.Add(FlagEnabled(30172805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30172800))
    
    MAIN.Await(AND_2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(Characters.AncientHeroofZamor)
    SetNetworkUpdateRate(Characters.AncientHeroofZamor, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.AncientHeroofZamor, name=907100301)


@RestartOnRest(30122811)
def Event_30122811():
    """Event 30122811"""
    if FlagEnabled(30170800):
        return
    AND_1.Add(HealthRatio(Characters.AncientHeroofZamor) <= 0.6000000238418579)
    
    MAIN.Await(AND_1)
    
    EnableFlag(30172802)


@RestartOnRest(30172849)
def Event_30172849():
    """Event 30172849"""
    CommonFunc_9005800(
        0,
        flag=30170800,
        entity=Assets.AEG099_001_9000,
        region=30172800,
        flag_1=30172805,
        character=30175800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30170800,
        entity=Assets.AEG099_001_9000,
        region=30172800,
        flag_1=30172805,
        flag_2=30172806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30170800, asset=Assets.AEG099_001_9000, model_point=3, right=0)
    CommonFunc_9005822(0, 30170800, 920200, 30172805, 30172806, 0, 30172802, 0, 0)


@RestartOnRest(16002520)
def Event_16002520(_, flag: uint, asset: uint):
    """Event 16002520"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(AttackedWithDamageType(attacked_entity=asset, attacker=20000))
    
    MAIN.Await(AND_1)
    
    EnableNetworkFlag(flag)
    ForceAnimation(asset, 1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAsset(asset)
