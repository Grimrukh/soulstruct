"""
linked:


strings:
0: ダンジョン_トラップ発動_錆びた宝箱
38: ダンジョン_ギミック起動_魔法壁消失
76: ダンジョン_トラップ発動_錆びた扉
112: ダンジョン_トラップ発動_テレポーター
152: ダンジョン_トラップ発動_落とし穴
188: ダンジョン_トラップ発動_火矢作動
224: ダンジョン_ギミック起動_跳ね橋降下
262: ボス_撃破
274: PC情報_ボス撃破_上層
300: PC情報_ボス撃破_中層
326: PC情報_ボス撃破_下層
352: PC情報_ボス撃破_最下層
380: クリア時間_通し
398: PC情報_ダンジョン到達時
426: ダンジョン_上層_クリア時間_通し
462: ダンジョン_上層_クリア時間_1プレイ
502: ダンジョン_中層_クリア時間_通し
538: ダンジョン_中層_クリア時間_1プレイ
578: ダンジョン_下層_クリア時間_通し
614: ダンジョン_下層_クリア時間_1プレイ
654: ダンジョン_最下層_クリア時間_通し
692: ダンジョン_最下層_クリア時間_1プレイ
734: ダンジョン_トラップ発動_落下敵
768: ダンジョン_ギミック起動_血舐め発生
806: ダンジョン_トラップ発動_悪霊女出現
844: ダンジョン_トラップ発動_ギロチン
880: ダンジョン_トラップ発動_クモ天井待機
920: ダンジョン_トラップ発動_クモ天井待機_領域使用
970: ダンジョン_トラップ発動_飛び出す敵
1008: ダンジョン_トラップ発動_領域で飛び出す敵
1052: ダンジョン_トラップ発動_モンスタールーム
1096: ダンジョン_ギミック起動_強化憑依
1132: ダンジョン_トラップ発動_鐘を鳴らす
1170: ダンジョン_トラップ発動_モンスタールーム_巣に帰る
1224: ダンジョン_トラップ発動_伏兵落下
1260: ボス_戦闘開始
1276: ダンジョン_ボスラッシュ前座_撃破時間
1316: ダンジョン_上層_ボス戦_撃破時間
1352: ダンジョン_中層_ボス戦_撃破時間
1388: ダンジョン_下層_ボス戦_撃破時間
1424: ダンジョン_最下層_ボス戦_撃破時間
1462: ダンジョン_トラップ発動_火薬タル爆発
1502: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    SkipLinesIfClient(1)
    AddSpecialEffect(PLAYER, 9920)
    SkipLinesIfHost(1)
    DisableFlagRange((12906660, 12906725))
    Event_12901685()
    Event_12907000(0, character=2900950, obj=2901950, flag=999, flag_1=12907800)
    Event_12907000(1, character=2900951, obj=2901951, flag=999, flag_1=12907820)
    Event_12907000(2, character=2900952, obj=2901952, flag=12901800, flag_1=12907840)
    Event_12907000(3, character=2900953, obj=2901953, flag=999, flag_1=12907860)
    Event_12907000(4, character=2900954, obj=2901954, flag=12901801, flag_1=12907880)
    Event_12907000(5, character=2900955, obj=2901955, flag=999, flag_1=12907900)
    Event_12907000(6, character=2900956, obj=2901956, flag=12901802, flag_1=12907920)
    Event_12907000(7, character=2900957, obj=2901957, flag=999, flag_1=12907940)
    Event_12907000(8, character=2900958, obj=2901958, flag=12901803, flag_1=12907960)
    Event_12907010(0, flag=72900200, warp_object_id=2901950)
    Event_12907010(1, flag=72900201, warp_object_id=2901951)
    Event_12907010(2, flag=72900202, warp_object_id=2901952)
    Event_12907010(3, flag=72900203, warp_object_id=2901953)
    Event_12907010(4, flag=72900204, warp_object_id=2901954)
    Event_12907010(5, flag=72900205, warp_object_id=2901955)
    Event_12907010(6, flag=72900206, warp_object_id=2901956)
    Event_12907010(7, flag=72900207, warp_object_id=2901957)
    Event_12907010(8, flag=72900208, warp_object_id=2901958)
    Event_12907020(0, flag=72900100, anchor_entity=2901950)
    Event_12907020(1, flag=72900101, anchor_entity=2901951)
    Event_12907020(2, flag=72900102, anchor_entity=2901952)
    Event_12907020(3, flag=72900103, anchor_entity=2901953)
    Event_12907020(4, flag=72900104, anchor_entity=2901954)
    Event_12907020(5, flag=72900105, anchor_entity=2901955)
    Event_12907020(6, flag=72900106, anchor_entity=2901956)
    Event_12907020(7, flag=72900107, anchor_entity=2901957)
    Event_12907020(8, flag=72900108, anchor_entity=2901958)
    Event_12907030(0, flag=72102900, warp_object_id=2901950)
    Event_12907030(1, flag=72102901, warp_object_id=2901951)
    Event_12907030(2, flag=72102902, warp_object_id=2901952)
    Event_12907030(3, flag=72102903, warp_object_id=2901953)
    Event_12907030(4, flag=72102904, warp_object_id=2901954)
    Event_12907030(5, flag=72102905, warp_object_id=2901955)
    Event_12907030(6, flag=72102906, warp_object_id=2901956)
    Event_12907030(7, flag=72102907, warp_object_id=2901957)
    Event_12907030(8, flag=72102908, warp_object_id=2901958)
    Event_12907420(0, special_effect_id=4730, flag=92905370, special_effect_id_1=4735, special_effect_id_2=4736)
    Event_12907420(1, special_effect_id=4731, flag=92905371, special_effect_id_1=4735, special_effect_id_2=4736)
    Event_12907420(2, special_effect_id=4732, flag=92905372, special_effect_id_1=4735, special_effect_id_2=4736)
    DisableFlag(12907230)
    DisableFlag(12907231)
    Event_12907400()


@NeverRestart(12900000)
def Event_12900000(_, obj: int, obj_act_id: int):
    """Event 12900000"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SkipLinesIfObjectDestroyed(1, obj)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=obj_act_id)
    IfObjectDestroyed(-1, obj)
    AwaitConditionTrue(-1)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)
    DisableObjectActivation(obj, obj_act_id=-1)


@NeverRestart(12900060)
def Event_12900060(_, obj: int, obj_1: int):
    """Event 12900060"""
    SkipLinesIfFlagDisabled(4, 92905335)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@NeverRestart(12900067)
def Event_12900067(_, obj: int, obj_act_id: int, flag: int):
    """Event 12900067"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SkipLinesIfObjectDestroyed(1, obj)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=obj_act_id)
    IfObjectDestroyed(2, obj)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=10)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    EndIfFinishedConditionTrue(input_condition=2)
    EnableFlag(flag)


@NeverRestart(12900078)
def Event_12900078(_, source_entity: int, flag: int):
    """Event 12900078"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, flag)
    CreatePlayLog(name=0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=90,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=90,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@NeverRestart(12900089)
def Event_12900089(_, obj: int, obj_act_id: int, obj_act_id_1: int, obj_act_id_2: int):
    """Event 12900089"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    End()


@NeverRestart(12900163)
def Event_12900163(_, obj: int, obj_act_id: int, obj_act_id_1: int, flag: int):
    """Event 12900163"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableFlag(flag)
    End()


@NeverRestart(12900174)
def Event_12900174(_, entity: int, obj_act_id: int, flag: int):
    """Event 12900174"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParamActivated(1, action_button_id=7011, entity=entity)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisplayDialog(text=10010161, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900185)
def Event_12900185(_, obj: int, obj_1: int, obj_act_id: int, flag: int):
    """Event 12900185"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    ForceAnimation(obj, 0, wait_for_completion=True)
    EnableFlag(flag)


@NeverRestart(12900186)
def Event_12900186(_, anchor_entity: int, flag: int):
    """Event 12900186"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=anchor_entity)
    IfActionButtonParamActivated(2, action_button_id=7011, entity=anchor_entity)
    IfFlagEnabled(3, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    DisplayDialog(text=10010160, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900187)
def Event_12900187(_, anchor_entity: int, flag: int):
    """Event 12900187"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=anchor_entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010170, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900188)
def Event_12900188(_, obj: int, obj_act_id: int, flag: int, flag_1: int):
    """Event 12900188"""
    EndIfFlagEnabled(flag_1)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=1)
    EnableObjectActivation(obj, obj_act_id=9921)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(obj, obj_act_id=9921)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    ForceAnimation(obj, 1)
    Wait(2.5)
    EnableObjectActivation(obj, obj_act_id=9921)
    Wait(0.5)
    EnableFlag(flag)


@NeverRestart(12900189)
def Event_12900189(_, obj: int, obj_act_id: int, flag: int):
    """Event 12900189"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=9921)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EnableFlag(flag)
    Wait(0.0)


@NeverRestart(12900190)
def Event_12900190(_, anchor_entity: int, flag: int):
    """Event 12900190"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=anchor_entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010160, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900191)
def Event_12900191(_, anchor_entity: int, flag: int):
    """Event 12900191"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=anchor_entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010170, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900192)
def Event_12900192(_, obj_act_id: int, flag: int, obj: int):
    """Event 12900192"""
    SkipLinesIfFlagDisabled(3, flag)
    DisableObjectActivation(obj, obj_act_id=2902000)
    CreateObjectVFX(obj, vfx_id=703, model_point=929136)
    End()
    CreateObjectVFX(obj, vfx_id=703, model_point=929134)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=56)
    EnableFlag(flag)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=703, model_point=929136)
    DisplayBanner(BannerType.YouWin)
    PlaySoundEffect(PLAYER, 888880000, sound_type=SoundType.v_Voice)
    WaitFrames(frames=44)
    Wait(1.0)
    DisplayBattlefieldMessage(10011260, display_location_index=0)


@NeverRestart(12900197)
def Event_12900197(_, obj: int, obj_act_id: int, flag: int):
    """Event 12900197"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=2900100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    EnableFlag(flag)
    Wait(0.0)


@NeverRestart(12900202)
def Event_12900202(_, anchor_entity: int, flag: int):
    """Event 12900202"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=anchor_entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010167, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900207)
def Event_12900207(_, anchor_entity: int, flag: int):
    """Event 12900207"""
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    Wait(3.0)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=anchor_entity)
    DisplayDialog(text=10010170, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900229)
def Event_12900229(_, obj: int, flag: int, flag_1: int):
    """Event 12900229"""
    WaitFrames(frames=2)
    SkipLinesIfFlagDisabled(2, flag_1)
    CreateObjectVFX(obj, vfx_id=703, model_point=929136)
    End()
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=1)
    CreateObjectVFX(obj, vfx_id=703, model_point=929136)
    EnableObjectActivation(obj, obj_act_id=2900100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(obj, obj_act_id=2900100)
    CreateObjectVFX(obj, vfx_id=703, model_point=929134)
    IfFlagEnabled(0, flag)
    DeleteObjectVFX(obj)
    ForceAnimation(obj, 1)
    Wait(2.5)
    CreateObjectVFX(obj, vfx_id=703, model_point=929136)
    EnableObjectActivation(obj, obj_act_id=2900100)
    Wait(0.5)


@NeverRestart(12900234)
def Event_12900234(_, obj_act_id: int, item: int, text: int, obj: int, obj_act_id_1: int, obj_act_id_2: int):
    """Event 12900234"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    SkipLinesIfClient(2)
    DisplayDialog(text=text, anchor_entity=PLAYER, number_buttons=NumberButtons.OneButton)
    RemoveGoodFromPlayer(item=item)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)


@NeverRestart(12900235)
def Event_12900235(_, obj_act_id: int, text: int, obj: int, obj_act_id_1: int, obj_act_id_2: int):
    """Event 12900235"""
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    SkipLinesIfClient(1)
    DisplayDialog(text=text, anchor_entity=PLAYER, number_buttons=NumberButtons.OneButton)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)


@NeverRestart(12900236)
def Event_12900236(_, obj: int):
    """Event 12900236"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(obj)
    End()
    IfObjectDestroyed(0, obj)
    CreatePlayLog(name=38)


@NeverRestart(12901760)
def Event_12901760(_, obj: int):
    """Event 12901760"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(0, obj)
    CreatePlayLog(name=38)


@NeverRestart(12900238)
def Event_12900238(_, obj: int, obj_act_id: int, obj_act_id_1: int, obj_act_id_2: int, flag: int):
    """Event 12900238"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)
    EnableFlag(flag)


@NeverRestart(12900239)
def Event_12900239(_, source_entity: int, flag: int):
    """Event 12900239"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, flag)
    CreatePlayLog(name=76)
    Wait(1.5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=source_entity,
        model_point=120,
        behavior_id=6020,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@NeverRestart(12900240)
def Event_12900240(_, obj: int, obj_1: int, obj_2: int, flag: int, flag_1: int):
    """Event 12900240"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=10)
    EndOfAnimation(obj=obj_1, animation_id=0)
    EndOfAnimation(obj=obj_2, animation_id=1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=0)
    EndOfAnimation(obj=obj_1, animation_id=1)
    EndOfAnimation(obj=obj_2, animation_id=0)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(flag_1)


@NeverRestart(12900245)
def Event_12900245(
    _,
    entity: int,
    entity_1: int,
    entity_2: int,
    region: int,
    region_1: int,
    region_2: int,
    flag: int,
    flag_1: int,
):
    """Event 12900245"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfCharacterInsideRegion(2, PLAYER, region=region_2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    DisableFlag(flag)
    ForceAnimation(entity_2, 1)
    ForceAnimation(entity, 10, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    DisableFlag(flag_1)
    ForceAnimation(entity_1, 0)
    Restart()


@NeverRestart(12900250)
def Event_12900250(
    _,
    entity: int,
    entity_1: int,
    entity_2: int,
    region: int,
    region_1: int,
    region_2: int,
    flag: int,
    flag_1: int,
):
    """Event 12900250"""
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfCharacterInsideRegion(2, PLAYER, region=region_2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    EnableFlag(flag)
    ForceAnimation(entity_1, 1)
    ForceAnimation(entity, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region)
    DisableFlag(flag_1)
    ForceAnimation(entity_2, 0)
    Restart()


@NeverRestart(12900255)
def Event_12900255(_, entity: int, entity_1: int, flag: int, flag_1: int):
    """Event 12900255"""
    DisableNetworkSync()
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=entity)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=entity_1)
    IfFlagEnabled(3, flag_1)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=entity)
    IfFlagEnabled(4, flag_1)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=entity_1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900260)
def Event_12900260(_, character: int):
    """Event 12900260"""
    IfCharacterHasSpecialEffect(1, PLAYER, 6100)
    IfCharacterDead(1, character)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    EndIfConditionFalse(2)
    AwardItemLot(5530, host_only=True)


@NeverRestart(12900293)
def Event_12900293(_, region: int, flag: int, flag_1: int):
    """Event 12900293"""
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreatePlayLog(name=112)
    EnableFlag(flag_1)
    WaitFrames(frames=6)
    IfCharacterOutsideRegion(1, PLAYER, region=region)
    RestartIfConditionTrue(1)
    ResetAnimation(PLAYER)
    ForceAnimation(PLAYER, 101161)
    WaitFrames(frames=59)
    EnableFlag(flag)
    IfFlagDisabled(0, flag)
    Restart()


@NeverRestart(12900304)
def Event_12900304(_, flag: int, move_to_region: int, flag_1: int):
    """Event 12900304"""
    DisableNetworkSync()
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    PlayCutsceneAndMovePlayer_Dummy(move_to_region=move_to_region, game_map=CHALICE_DUNGEON)
    WaitFrames(frames=2)
    EnableFlag(flag_1)
    ForceAnimation(PLAYER, 101162, wait_for_completion=True)
    DisableFlag(flag)
    Restart()


@NeverRestart(12901732)
def Event_12901732(_, flag: int, obj: int):
    """Event 12901732"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    CreateObjectVFX(obj, vfx_id=700, model_point=929102)
    CreateObjectVFX(obj, vfx_id=702, model_point=929102)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    CreateObjectVFX(obj, vfx_id=700, model_point=929102)
    CreateObjectVFX(obj, vfx_id=702, model_point=929102)

    # --- 1 --- #
    DefineLabel(1)
    CreateTemporaryVFX(vfx_id=929213, anchor_entity=obj, model_point=200, anchor_type=CoordEntityType.Object)
    DisableFlag(flag)
    Restart()


@NeverRestart(12901743)
def Event_12901743(_, flag: int, anchor_entity: int):
    """Event 12901743"""
    IfFlagEnabled(0, flag)
    CreateTemporaryVFX(vfx_id=929215, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Object)
    DisableFlag(flag)
    Restart()


@NeverRestart(12900315)
def Event_12900315(_, flag: int, obj: int, obj_1: int, obj_act_id: int, obj_2: int, flag_1: int):
    """Event 12900315"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=obj, animation_id=12)
    DisableObjectActivation(obj_1, obj_act_id=obj_act_id)
    EnableObjectActivation(obj_2, obj_act_id=obj_act_id)
    SkipLines(3)
    EndOfAnimation(obj=obj, animation_id=132)
    DisableObjectActivation(obj_2, obj_act_id=obj_act_id)
    EnableObjectActivation(obj_1, obj_act_id=obj_act_id)
    DisableFlag(flag_1)


@NeverRestart(12900323)
def Event_12900323(
    _,
    flag: int,
    flag_1: int,
    region: int,
    obj_act_id: int,
    entity: int,
    region_1: int,
    obj: int,
    obj_1: int,
):
    """Event 12900323"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 133, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 35, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 11, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    EnableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900331)
def Event_12900331(
    _,
    flag: int,
    flag_1: int,
    region: int,
    obj_act_id: int,
    entity: int,
    region_1: int,
    obj: int,
    obj_1: int,
):
    """Event 12900331"""
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 16, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 131, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    EnableFlag(flag)
    DisableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    EnableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900339)
def Event_12900339(_, flag: int, entity: int, flag_1: int, entity_1: int):
    """Event 12900339"""
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=entity)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=entity_1)
    IfFlagEnabled(3, flag)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=entity_1)
    IfFlagEnabled(4, flag)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=entity)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12900347)
def Event_12900347(_, obj: int, obj_1: int, obj_2: int, flag: int, flag_1: int, animation_id: int, animation_id_1: int):
    """Event 12900347"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    EnableObjectActivation(obj_2, obj_act_id=9902)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=obj, animation_id=animation_id_1)
    EnableObjectActivation(obj_1, obj_act_id=9902)
    DisableObjectActivation(obj_2, obj_act_id=9902)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(flag_1)


@NeverRestart(12900351)
def Event_12900351(
    _,
    entity: int,
    obj: int,
    obj_1: int,
    region: int,
    region_1: int,
    obj_act_id: int,
    flag: int,
    flag_1: int,
):
    """Event 12900351"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    ForceAnimation(entity, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region)
    ForceAnimation(entity, 1, wait_for_completion=True)
    DisableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    EnableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900353)
def Event_12900353(
    _,
    entity: int,
    obj: int,
    obj_1: int,
    region: int,
    region_1: int,
    obj_act_id: int,
    flag: int,
    flag_1: int,
):
    """Event 12900353"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region_1)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(flag)
    EnableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    ForceAnimation(entity, 20, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region)
    ForceAnimation(entity, 21, wait_for_completion=True)
    DisableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    EnableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900354)
def Event_12900354(
    _,
    entity: int,
    obj: int,
    obj_1: int,
    region: int,
    region_1: int,
    obj_act_id: int,
    flag: int,
    flag_1: int,
):
    """Event 12900354"""
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    ForceAnimation(entity, 10, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    ForceAnimation(entity, 11, wait_for_completion=True)
    DisableFlag(flag_1)
    EnableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900356)
def Event_12900356(
    _,
    entity: int,
    obj: int,
    obj_1: int,
    region: int,
    region_1: int,
    obj_act_id: int,
    flag: int,
    flag_1: int,
):
    """Event 12900356"""
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagDisabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfObjectActivated(2, obj_act_id=obj_act_id)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    ForceAnimation(entity, 30, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    ForceAnimation(entity, 31, wait_for_completion=True)
    DisableFlag(flag_1)
    EnableObjectActivation(obj, obj_act_id=9902)
    DisableObjectActivation(obj_1, obj_act_id=9902)
    Restart()


@NeverRestart(12900357)
def Event_12900357(_, entity: int, entity_1: int, flag: int, flag_1: int):
    """Event 12900357"""
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=entity)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=entity_1)
    IfFlagEnabled(3, flag_1)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=entity)
    IfFlagEnabled(4, flag_1)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=entity_1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()


@NeverRestart(12900361)
def Event_12900361(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, entity: int, entity_1: int):
    """Event 12900361"""
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)
    EnableFlag(flag_3)
    DisableFlag(flag_4)
    ForceAnimation(entity, 2, wait_for_completion=True)
    ForceAnimation(entity_1, 2, wait_for_completion=True)
    End()


@NeverRestart(12900363)
def Event_12900363(_, flag: int, flag_1: int, region: int, region_1: int, entity: int, flag_2: int):
    """Event 12900363"""
    Wait(1.0)
    SkipLinesIfFlagDisabled(19, flag_2)
    SkipLinesIfFlagEnabled(18, flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 4, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 121, wait_for_completion=True)
    ForceAnimation(entity, 122, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()


@NeverRestart(12900365)
def Event_12900365(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    entity: int,
    entity_1: int,
    region_2: int,
    region_3: int,
):
    """Event 12900365"""
    Wait(0.5)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(6, flag_1)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=region)
    IfCharacterInsideRegion(4, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity_1, 123)
    ForceAnimation(entity, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity_1, 24)
    ForceAnimation(entity, 4, wait_for_completion=True)
    ForceAnimation(entity_1, 0, wait_for_completion=True)
    ForceAnimation(entity, 120, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 121)
    ForceAnimation(entity_1, 1, wait_for_completion=True)
    ForceAnimation(entity, 122, wait_for_completion=True)
    ForceAnimation(entity_1, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=region_2)
    IfAllPlayersOutsideRegion(5, region=region_3)
    IfConditionTrue(0, input_condition=5)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(12900367)
def Event_12900367(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    entity: int,
    entity_1: int,
    region_2: int,
    region_3: int,
):
    """Event 12900367"""
    Wait(0.5)
    IfFlagEnabled(2, flag)
    IfFlagEnabled(6, flag_1)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=region)
    IfCharacterInsideRegion(4, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 123)
    ForceAnimation(entity_1, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity_1, 4)
    ForceAnimation(entity, 24, wait_for_completion=True)
    ForceAnimation(entity_1, 120, wait_for_completion=True)
    ForceAnimation(entity, 0, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 1)
    ForceAnimation(entity_1, 121, wait_for_completion=True)
    ForceAnimation(entity, 2, wait_for_completion=True)
    ForceAnimation(entity_1, 122, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=region_2)
    IfAllPlayersOutsideRegion(5, region=region_3)
    IfConditionTrue(0, input_condition=5)
    EnableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(12900369)
def Event_12900369(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, entity: int, entity_1: int):
    """Event 12900369"""
    EnableFlag(flag)
    EnableFlag(flag_1)
    DisableFlag(flag_2)
    EnableFlag(flag_3)
    DisableFlag(flag_4)
    ForceAnimation(entity, 12, wait_for_completion=True)
    ForceAnimation(entity_1, 12, wait_for_completion=True)
    End()


@NeverRestart(12900371)
def Event_12900371(_, flag: int, flag_1: int, region: int, region_1: int, entity: int, flag_2: int):
    """Event 12900371"""
    Wait(1.0)
    SkipLinesIfFlagDisabled(19, flag_2)
    SkipLinesIfFlagEnabled(18, flag_1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 14, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 101, wait_for_completion=True)
    ForceAnimation(entity, 102, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=region_1)
    DisableFlag(flag)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    End()


@NeverRestart(12900373)
def Event_12900373(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    entity: int,
    entity_1: int,
    region_2: int,
    region_3: int,
):
    """Event 12900373"""
    Wait(0.5)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(6, flag_1)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=region)
    IfCharacterInsideRegion(4, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity_1, 103)
    ForceAnimation(entity, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity_1, 5)
    ForceAnimation(entity, 14, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 101)
    ForceAnimation(entity_1, 11, wait_for_completion=True)
    ForceAnimation(entity, 102, wait_for_completion=True)
    ForceAnimation(entity_1, 12, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=region_2)
    IfAllPlayersOutsideRegion(5, region=region_3)
    IfConditionTrue(0, input_condition=5)
    DisableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(12900375)
def Event_12900375(
    _,
    flag: int,
    flag_1: int,
    region: int,
    region_1: int,
    entity: int,
    entity_1: int,
    region_2: int,
    region_3: int,
):
    """Event 12900375"""
    Wait(0.5)
    IfFlagEnabled(2, flag)
    IfFlagEnabled(6, flag_1)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=region)
    IfCharacterInsideRegion(4, PLAYER, region=region_1)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag_1)
    Wait(1.0)
    ForceAnimation(entity, 103)
    ForceAnimation(entity_1, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity_1, 14)
    ForceAnimation(entity, 5, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(entity, 11)
    ForceAnimation(entity_1, 101, wait_for_completion=True)
    ForceAnimation(entity, 12, wait_for_completion=True)
    ForceAnimation(entity_1, 102, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=region_2)
    IfAllPlayersOutsideRegion(5, region=region_3)
    IfConditionTrue(0, input_condition=5)
    EnableFlag(flag)
    DisableFlag(flag_1)
    Restart()


@NeverRestart(12900377)
def Event_12900377(_, obj: int, obj_flag: int):
    """Event 12900377"""
    GotoIfFlagEnabled(Label.L7, flag=92905107)
    GotoIfFlagEnabled(Label.L6, flag=92905106)
    GotoIfFlagEnabled(Label.L5, flag=92905105)
    GotoIfFlagEnabled(Label.L4, flag=92905104)
    GotoIfFlagEnabled(Label.L3, flag=92905103)
    GotoIfFlagEnabled(Label.L2, flag=92905102)
    GotoIfFlagEnabled(Label.L1, flag=92905101)
    GotoIfFlagEnabled(Label.L0, flag=92905100)

    # --- 0 --- #
    DefineLabel(0)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6130,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6131,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 2 --- #
    DefineLabel(2)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6132,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 3 --- #
    DefineLabel(3)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6133,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 4 --- #
    DefineLabel(4)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6134,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 5 --- #
    DefineLabel(5)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6135,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 6 --- #
    DefineLabel(6)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6136,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )
    End()

    # --- 7 --- #
    DefineLabel(7)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6137,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )


@NeverRestart(12900395)
def Event_12900395(_, obj: int, obj_flag: int):
    """Event 12900395"""
    CreateObjectVFX(obj, vfx_id=704, model_point=900110)
    GotoIfFlagEnabled(Label.L7, flag=92905107)
    GotoIfFlagEnabled(Label.L6, flag=92905106)
    GotoIfFlagEnabled(Label.L5, flag=92905105)
    GotoIfFlagEnabled(Label.L4, flag=92905104)
    GotoIfFlagEnabled(Label.L3, flag=92905103)
    GotoIfFlagEnabled(Label.L2, flag=92905102)
    GotoIfFlagEnabled(Label.L1, flag=92905101)
    GotoIfFlagEnabled(Label.L0, flag=92905100)

    # --- 0 --- #
    DefineLabel(0)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6160,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6161,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 2 --- #
    DefineLabel(2)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6162,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 3 --- #
    DefineLabel(3)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6163,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 4 --- #
    DefineLabel(4)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6164,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 5 --- #
    DefineLabel(5)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6165,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 6 --- #
    DefineLabel(6)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6166,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    End()

    # --- 7 --- #
    DefineLabel(7)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=704,
        behavior_param_id=6167,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )


@NeverRestart(12900423)
def Event_12900423(_, region: int, obj: int):
    """Event 12900423"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreatePlayLog(name=152)
    CreateTemporaryVFX(vfx_id=929209, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, 997400000, sound_type=SoundType.o_Object)
    DestroyObject(obj)


@NeverRestart(12900430)
def Event_12900430(_, entity: int):
    """Event 12900430"""
    DisableSpawner(entity=entity)


@NeverRestart(12901000)
def Event_12901000(_, character: int, entity: int):
    """Event 12901000"""
    DisableSpawner(entity=entity)
    IfCharacterDrawGroupEnabled(1, character=character)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfCharacterHasTAEEvent(1, character, tae_event_id=100)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(entity=entity)
    IfCharacterDrawGroupDisabled(-1, character=character)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(12901200)
def Event_12901200(_, copy_draw_parent: int, character: int):
    """Event 12901200"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=copy_draw_parent,
    )
    IfCharacterDoesNotHaveTAEEvent(0, character, tae_event_id=100)
    IfCharacterDead(0, character)
    AddSpecialEffect_WithUnknownEffect(character, 5751)
    Restart()


@NeverRestart(12901272)
def Event_12901272(_, character: int, entity: int, character_1: int):
    """Event 12901272"""
    IfCharacterHasTAEEvent(0, character_1, tae_event_id=100)
    IfCharacterDead(1, character_1)
    IfCharacterDead(2, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    DisableSpawner(entity=entity)
    Kill(character_1, award_souls=True)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(12901347)
def Event_12901347(_, region: int, entity: int, flag: int):
    """Event 12901347"""
    IfFlagDisabled(1, flag)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfFlagEnabled(2, flag)
    IfAllPlayersOutsideRegion(2, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    ForceAnimation(entity, 0, wait_for_completion=True)
    EnableFlag(flag)
    Wait(2.0999999046325684)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(flag)
    ForceAnimation(entity, 1, wait_for_completion=True)
    Restart()


@NeverRestart(12901400)
def Event_12901400(_, obj__source_entity: int, flag: int):
    """Event 12901400"""
    IfObjectNotDestroyed(1, obj__source_entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    EndIfFinishedConditionFalse(input_condition=1)
    CreatePlayLog(name=188)
    CreateTemporaryVFX(
        vfx_id=150005,
        anchor_entity=obj__source_entity,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    PlaySoundEffect(obj__source_entity, 990100001, sound_type=SoundType.o_Object)
    SkipLinesIfFlagEnabled(84, 92905107)
    SkipLinesIfFlagEnabled(72, 92905106)
    SkipLinesIfFlagEnabled(60, 92905105)
    SkipLinesIfFlagEnabled(48, 92905104)
    SkipLinesIfFlagEnabled(36, 92905103)
    SkipLinesIfFlagEnabled(24, 92905102)
    SkipLinesIfFlagEnabled(12, 92905101)
    SkipLinesIfFlagEnabled(0, 92905100)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6230,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(77)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6201,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6211,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6221,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6231,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(66)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6202,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6212,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6222,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6232,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(55)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6203,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6213,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6223,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6233,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(44)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6204,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6214,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6224,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6234,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(33)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6205,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6215,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6225,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6235,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(22)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6206,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6216,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6226,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6236,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(11)
    SkipLinesIfFlagEnabled(8, 92905310)
    SkipLinesIfFlagEnabled(5, 92905204)
    SkipLinesIfFlagEnabled(2, 92905202)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6207,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6217,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6227,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6237,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(0)
    Wait(0.699999988079071)
    IfFlagDisabled(0, flag)
    Restart()


@NeverRestart(12901447)
def Event_12901447(_, obj_act_id: int, navmesh_id: int):
    """Event 12901447"""
    EndIfThisEventSlotFlagEnabled()
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)


@NeverRestart(12901525)
def Event_12901525(_, obj_act_id: int, navmesh_id: int):
    """Event 12901525"""
    EndIfThisEventSlotFlagEnabled()
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(3.0)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)


@RestartOnRest(12901532)
def Event_12901532(_, character: int, flag: int):
    """Event 12901532"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@NeverRestart(12901550)
def Event_12901550(_, obj_act_id: int, obj: int, obj_1: int):
    """Event 12901550"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=1)
    EndOfAnimation(obj=obj_1, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=2931100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    ForceAnimation(obj_1, 0, wait_for_completion=True)
    CreatePlayLog(name=224)


@NeverRestart(12901554)
def Event_12901554(_, character__targeting_character: int, ai_param_id: int):
    """Event 12901554"""
    IfCharacterTargeting(-1, targeting_character=character__targeting_character, targeted_character=PLAYER)
    IfAttacked(-1, attacked_entity=character__targeting_character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character__targeting_character, ai_param_id=ai_param_id)
    ReplanAI(character__targeting_character)


@NeverRestart(12901555)
def Event_12901555():
    """Event 12901555"""
    CreateProjectileOwner(entity=2900000)
    DisableCharacter(2900000)


@NeverRestart(12901556)
def Event_12901556(_, start_climbing_flag: int, stop_climbing_flag: int, obj: int):
    """Event 12901556"""
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)


@NeverRestart(12901588)
def Event_12901588(_, character__game_area_param_id: int, obj: int, vfx_id: int, left: int, obj_1: int, vfx_id_1: int):
    """Event 12901588"""
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()
    IfCharacterDead(0, character__game_area_param_id)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    IfCharacterHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680)
    AddSpecialEffect(PLAYER, 4680)
    KillBoss(game_area_param_id=character__game_area_param_id)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)


@NeverRestart(12901589)
def Event_12901589(
    _,
    character__game_area_param_id: int,
    obj: int,
    vfx_id: int,
    left: int,
    obj_1: int,
    vfx_id_1: int,
    character: int,
):
    """Event 12901589"""
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()
    IfCharacterDead(1, character__game_area_param_id)
    IfCharacterDead(1, character)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    IfCharacterHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680)
    AddSpecialEffect(PLAYER, 4680)
    KillBoss(game_area_param_id=character__game_area_param_id)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)


@NeverRestart(12901590)
def Event_12901590(_, character__game_area_param_id: int, obj: int, vfx_id: int, flag: int, obj_1: int, vfx_id_1: int):
    """Event 12901590"""
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()
    IfCharacterDead(0, character__game_area_param_id)
    CreatePlayLog(name=262)
    StopPlayLogMeasurement(measurement_id=2900020)
    KillBoss(game_area_param_id=character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    EnableFlag(flag)


@NeverRestart(12901591)
def Event_12901591(
    _,
    character__game_area_param_id: int,
    obj: int,
    vfx_id: int,
    left: int,
    obj_1: int,
    vfx_id_1: int,
    character: int,
    character_1: int,
):
    """Event 12901591"""
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()
    IfCharacterDead(1, character__game_area_param_id)
    IfCharacterDead(1, character)
    IfCharacterDead(1, character_1)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    IfCharacterHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680)
    AddSpecialEffect(PLAYER, 4680)
    KillBoss(game_area_param_id=character__game_area_param_id)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)


@NeverRestart(12901592)
def Event_12901592(_, flag: int, obj: int):
    """Event 12901592"""
    SkipLinesIfThisEventSlotFlagEnabled(5)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, 92905360)
    IfFlagDisabled(1, 12907220)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(12907220)
    DisableObject(obj)


@NeverRestart(12901593)
def Event_12901593(_, flag: int, obj: int):
    """Event 12901593"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfFlagEnabled(0, flag)
    DisableObject(obj)


@NeverRestart(12901594)
def Event_12901594(
    _,
    flag: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
    item_lot_param_id_2: int,
    item_lot_param_id_3: int,
    item_lot_param_id_4: int,
    item_lot_param_id_5: int,
    flag_1: int,
):
    """Event 12901594"""
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    IfFlagEnabled(1, 92905377)
    IfFlagDisabled(1, flag_1)
    SkipLinesIfConditionFalse(2, 1)
    AwardItemLot(item_lot_param_id_3, host_only=False)
    End()
    SkipLinesIfFlagEnabled(2, 92905378)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    IfFlagEnabled(2, 92905360)
    IfFlagEnabled(2, 12907220)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(item_lot_param_id_3, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_4, host_only=False)
    End()
    SkipLinesIfClient(9)
    EndIfFlagRangeAllDisabled(flag_range=(92905370, 92905373))
    SkipLinesIfFlagEnabled(3, flag_1)
    AwardItemLot(item_lot_param_id_4, host_only=False)
    EnableFlag(flag_1)
    SkipLines(1)
    AwardItemLot(item_lot_param_id_5, host_only=False)
    EndIfFlagRangeAllDisabled(flag_range=(92905371, 92905373))
    AwardItemLot(item_lot_param_id_4, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=True)
    End()
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(item_lot_param_id_2, host_only=True)
    End()


@NeverRestart(12901595)
def Event_12901595(
    _,
    flag: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
    item_lot_param_id_2: int,
    item_lot_param_id_3: int,
    item_lot_param_id_4: int,
    item_lot_param_id_5: int,
    flag_1: int,
):
    """Event 12901595"""
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    IfFlagEnabled(1, 92905377)
    IfFlagDisabled(1, flag_1)
    SkipLinesIfConditionFalse(2, 1)
    AwardItemLot(item_lot_param_id_3, host_only=False)
    End()
    SkipLinesIfFlagEnabled(2, 92905378)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    IfFlagEnabled(2, 92905360)
    IfFlagEnabled(2, 12907220)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(item_lot_param_id_3, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_4, host_only=False)
    End()
    SkipLinesIfClient(11)
    EndIfFlagDisabled(92905360)
    AwardItemLot(item_lot_param_id_3, host_only=False)
    EndIfFlagRangeAllDisabled(flag_range=(92905370, 92905373))
    SkipLinesIfFlagEnabled(3, flag_1)
    AwardItemLot(item_lot_param_id_4, host_only=False)
    EnableFlag(flag_1)
    SkipLines(1)
    AwardItemLot(item_lot_param_id_5, host_only=False)
    EndIfFlagRangeAllDisabled(flag_range=(92905371, 92905373))
    AwardItemLot(item_lot_param_id_4, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=True)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(item_lot_param_id_2, host_only=True)
    End()


@NeverRestart(12901596)
def Event_12901596(_, flag: int, item_lot_param_id: int, item_lot_param_id_1: int, item_lot_param_id_2: int):
    """Event 12901596"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    SkipLinesIfClient(2)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=False)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(item_lot_param_id_2, host_only=True)
    End()


@NeverRestart(12901597)
def Event_12901597(_, flag: int, item_lot_param_id: int, item_lot_param_id_1: int, item_lot_param_id_2: int):
    """Event 12901597"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    SkipLinesIfClient(2)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=False)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(item_lot_param_id_2, host_only=True)
    End()


@NeverRestart(12901598)
def Event_12901598(_, flag: int, item_lot_param_id: int, item_lot_param_id_1: int):
    """Event 12901598"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    SkipLinesIfClient(2)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=False)
    End()


@NeverRestart(12901599)
def Event_12901599(_, character: int, region: int, animation_id: int, animation: int):
    """Event 12901599"""
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    RotateToFaceEntity(character, PLAYER, animation=animation)


@NeverRestart(12901600)
def Event_12901600(_, character: int, region: int):
    """Event 12901600"""
    IfCharacterBackreadEnabled(0, character)
    DisableCharacter(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=205, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=10)
    EnableCharacter(character)


@NeverRestart(12901601)
def Event_12901601(_, obj: int):
    """Event 12901601"""
    DisableObject(obj)


@NeverRestart(12901602)
def Event_12901602(_, region: int, obj: int):
    """Event 12901602"""
    CreateObjectVFX(obj, vfx_id=200, model_point=8020)
    ForceAnimation(obj, 200, loop=True, wait_for_completion=True)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(obj, 1000000, wait_for_completion=True)
    CreateObjectVFX(obj, vfx_id=100, model_point=8023)
    ForceAnimation(obj, 1000100, loop=True, wait_for_completion=True)


@NeverRestart(12901684)
def Event_12901684(_, flag: int, achievement_id: int):
    """Event 12901684"""
    IfFlagEnabled(0, flag)
    AwardAchievement(achievement_id=achievement_id)


@NeverRestart(12901685)
def Event_12901685():
    """Event 12901685"""
    StartPlayLogMeasurement(measurement_id=2900000, name=380, overwrite=False)
    SkipLinesIfFlagEnabled(5, 12901809)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=398,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=398,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=398,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=398,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(12901809)
    SkipLinesIfFlagEnabled(5, 12901800)
    StartPlayLogMeasurement(measurement_id=2901000, name=426, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2901001, name=462, overwrite=True)
    IfFlagEnabled(0, 12901800)
    StopPlayLogMeasurement(measurement_id=2901000)
    StopPlayLogMeasurement(measurement_id=2901001)
    SkipLinesIfFlagEnabled(5, 12901801)
    StartPlayLogMeasurement(measurement_id=2901010, name=502, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2901011, name=538, overwrite=True)
    IfFlagEnabled(0, 12901801)
    StopPlayLogMeasurement(measurement_id=2901010)
    StopPlayLogMeasurement(measurement_id=2901011)
    SkipLinesIfFlagEnabled(5, 12901802)
    StartPlayLogMeasurement(measurement_id=2901020, name=578, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2901021, name=614, overwrite=True)
    IfFlagEnabled(0, 12901802)
    StopPlayLogMeasurement(measurement_id=2901020)
    StopPlayLogMeasurement(measurement_id=2901021)
    SkipLinesIfFlagDisabled(6, 92905360)
    SkipLinesIfFlagEnabled(5, 12901803)
    StartPlayLogMeasurement(measurement_id=2901030, name=654, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2901031, name=692, overwrite=True)
    IfFlagEnabled(0, 12901803)
    StopPlayLogMeasurement(measurement_id=2901030)
    StopPlayLogMeasurement(measurement_id=2901031)
    StopPlayLogMeasurement(measurement_id=2900000)
    End()


@NeverRestart(12901686)
def Event_12901686(_, character__game_area_param_id: int, obj: int, obj_1: int, vfx_id: int, vfx_id_1: int, left: int):
    """Event 12901686"""
    GotoIfFlagDisabled(Label.L0, flag=left)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, character__game_area_param_id)
    IfHealthEqual(-1, character__game_area_param_id, value=0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, character__game_area_param_id)
    IfTimeElapsed(-2, seconds=15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    KillBoss(game_area_param_id=character__game_area_param_id)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(left)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(left)


@NeverRestart(12901690)
def Event_12901690(_, character__game_area_param_id: int, obj: int, vfx_id: int, left: int):
    """Event 12901690"""
    GotoIfFlagDisabled(Label.L0, flag=left)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, character__game_area_param_id)
    IfHealthEqual(-1, character__game_area_param_id, value=0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, character__game_area_param_id)
    IfTimeElapsed(-2, seconds=15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    Wait(3.0)
    KillBoss(game_area_param_id=character__game_area_param_id)
    SetNetworkUpdateRate(character__game_area_param_id, is_fixed=False, update_rate=CharacterUpdateRate.EveryTwoFrames)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(left)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(left)


@NeverRestart(12901692)
def Event_12901692(_, character__miniboss_id: int, obj: int, obj_1: int, vfx_id: int, vfx_id_1: int, left: int):
    """Event 12901692"""
    GotoIfFlagDisabled(Label.L0, flag=left)
    DisableCharacter(character__miniboss_id)
    Kill(character__miniboss_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, character__miniboss_id)
    IfHealthEqual(-1, character__miniboss_id, value=0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, character__miniboss_id)
    IfTimeElapsed(-2, seconds=15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    HandleMinibossDefeat(miniboss_id=character__miniboss_id)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(left)


@NeverRestart(12901693)
def Event_12901693(
    _,
    flag: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
    item_lot_param_id_2: int,
    item_lot_param_id_3: int,
    item_lot_param_id_4: int,
    item_lot_param_id_5: int,
):
    """Event 12901693"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    GotoIfClient(Label.L0)
    IfFlagEnabled(1, 92905385)
    IfFlagEnabled(-1, 12907212)
    IfFlagEnabled(-1, 12907213)
    IfConditionTrue(1, input_condition=-1)
    SkipLinesIfConditionFalse(6, 1)
    IfFlagEnabled(2, 12907213)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(item_lot_param_id_4, host_only=False)
    Goto(Label.L1)
    AwardItemLot(item_lot_param_id_5, host_only=False)
    Goto(Label.L1)
    IfFlagDisabled(3, 92905385)
    IfFlagEnabled(3, 92905378)
    IfFlagEnabled(-2, 12907211)
    IfFlagEnabled(-2, 12907212)
    IfConditionTrue(3, input_condition=-2)
    GotoIfConditionTrue(Label.L3, input_condition=3)
    Goto(Label.L1)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(4, 12907212)
    SkipLinesIfConditionTrue(2, 4)
    AwardItemLot(item_lot_param_id_4, host_only=False)
    Goto(Label.L1)
    AwardItemLot(item_lot_param_id_5, host_only=False)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=92905360)
    GotoIfFlagDisabled(Label.L0, flag=12907212)
    EnableFlag(12907221)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L0, flag=12907213)
    EnableFlag(12907221)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfClient(Label.L4)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(item_lot_param_id, host_only=True)
    Goto(Label.L9)
    AwardItemLot(item_lot_param_id_1, host_only=True)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(item_lot_param_id_2, host_only=True)
    Goto(Label.L9)
    AwardItemLot(item_lot_param_id_3, host_only=True)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    IfCharacterInsideRegion(-15, PLAYER, region=2902960)
    IfCharacterInsideRegion(-15, PLAYER, region=2902961)
    SkipLinesIfConditionFalse(16, -15)
    SkipLinesIfFlagDisabled(2, 92905100)
    AwardItemLot(110001000, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905101)
    AwardItemLot(110002000, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905102)
    AwardItemLot(110003000, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905103)
    AwardItemLot(110004000, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905104)
    AwardItemLot(110005000, host_only=True)
    End()
    End()
    IfCharacterInsideRegion(-14, PLAYER, region=2902962)
    IfCharacterInsideRegion(-14, PLAYER, region=2902963)
    SkipLinesIfConditionFalse(16, -14)
    SkipLinesIfFlagDisabled(2, 92905100)
    AwardItemLot(110001010, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905101)
    AwardItemLot(110002010, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905102)
    AwardItemLot(110003010, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905103)
    AwardItemLot(110004010, host_only=True)
    End()
    SkipLinesIfFlagDisabled(2, 92905104)
    AwardItemLot(110005010, host_only=True)
    End()
    End()
    End()


@NeverRestart(12901697)
def Event_12901697(
    _,
    character: int,
    region: int,
    animation_id: int,
    animation: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    obj_act_id: int,
):
    """Event 12901697"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    IfFlagDisabled(1, flag)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableFlag(flag_1)
    EnableFlag(flag_2)


@NeverRestart(12901701)
def Event_12901701(_, character: int, region: int, flag: int, flag_1: int, flag_2: int, obj_act_id: int):
    """Event 12901701"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    DisableCharacter(character)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=6, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=15)
    EnableCharacter(character)


@NeverRestart(12901705)
def Event_12901705(
    _,
    character: int,
    region: int,
    animation_id: int,
    animation: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    obj_act_id: int,
):
    """Event 12901705"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    IfFlagDisabled(1, flag)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    EnableFlag(flag_1)
    EnableFlag(flag_2)


@NeverRestart(12901706)
def Event_12901706(_, character: int, region: int, flag: int, flag_1: int, flag_2: int, obj_act_id: int):
    """Event 12901706"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    DisableCharacter(character)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=6, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=15)
    EnableCharacter(character)


@NeverRestart(12901707)
def Event_12901707(
    _,
    character: int,
    region: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    character_1: int,
    character_2: int,
    obj_act_id: int,
):
    """Event 12901707"""
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(flag_2)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_2)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    EnableFlag(flag_2)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=6, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=15)
    EnableCharacter(character)
    WaitFrames(frames=15)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character_1, model_point=6, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=15)
    EnableCharacter(character_1)
    WaitFrames(frames=15)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character_2, model_point=6, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=15)
    EnableCharacter(character_2)


@NeverRestart(12901708)
def Event_12901708(_, flag: int, left: int):
    """Event 12901708"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=127000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=216000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=304000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=313000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=750000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=7200)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=7040)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=106000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=218000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=209000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=257000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=305000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=305010)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=501000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=504000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=510000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=251000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=306000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=508000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=509000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=509010)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 0 --- #
    DefineLabel(0)


@NeverRestart(12901712)
def Event_12901712(_, flag: int, left: int):
    """Event 12901712"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=216000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=216000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=304000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=313000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=750000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=7200)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=209000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=257000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=305000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=305010)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=501000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=504000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=510000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=251000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=306000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=508000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=509000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=509010)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 0 --- #
    DefineLabel(0)


@NeverRestart(12901713)
def Event_12901713(_, obj_act_id: int, obj: int, obj_act_id_1: int, flag: int):
    """Event 12901713"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12901717)
def Event_12901717(_, obj_act_id: int, obj: int, obj_act_id_1: int, flag: int):
    """Event 12901717"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12901718)
def Event_12901718(_, flag: int, left: int, flag_1: int):
    """Event 12901718"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(0, flag)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=216000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=209000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=305000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=305010)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=501000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=510000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=251000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=306000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=508000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=509000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=509010)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)
    EnableFlag(flag_1)


@NeverRestart(12901722)
def Event_12901722(_, flag: int, left: int, flag_1: int):
    """Event 12901722"""
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(0, flag)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=216000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=209000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=305000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=305010)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=501000)
    GotoIfValueComparison(Label.L2, comparison_type=ComparisonType.Equal, left=left, right=510000)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=251000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=306000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=508000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=509000)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=509010)
    GotoIfValueComparison(Label.L3, comparison_type=ComparisonType.Equal, left=left, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680)
    WaitFrames(frames=10)
    EnableFlag(flag_1)


@NeverRestart(12901723)
def Event_12901723(
    _,
    character__game_area_param_id: int,
    obj: int,
    vfx_id: int,
    left: int,
    obj_1: int,
    vfx_id_1: int,
    character: int,
):
    """Event 12901723"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character__game_area_param_id)
    Kill(character__game_area_param_id)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, character__game_area_param_id)
    IfHealthEqual(-1, character__game_area_param_id, value=0.0)
    IfCharacterDead(-2, character)
    IfHealthEqual(-2, character, value=0.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(2, character__game_area_param_id)
    IfCharacterDead(2, character)
    IfConditionTrue(-3, input_condition=2)
    IfTimeElapsed(-3, seconds=15.0)
    IfConditionTrue(0, input_condition=-3)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    KillBoss(game_area_param_id=character__game_area_param_id)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(left)


@NeverRestart(12901725)
def Event_12901725(
    _,
    character__game_area_param_id: int,
    obj: int,
    vfx_id: int,
    left: int,
    obj_1: int,
    vfx_id_1: int,
    character: int,
    character_1: int,
):
    """Event 12901725"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character__game_area_param_id)
    DisableCharacter(character)
    DisableCharacter(character_1)
    Kill(character__game_area_param_id)
    Kill(character)
    Kill(character_1)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, character__game_area_param_id)
    IfHealthEqual(-1, character__game_area_param_id, value=0.0)
    IfCharacterDead(-2, character)
    IfHealthEqual(-2, character, value=0.0)
    IfCharacterDead(-3, character_1)
    IfHealthEqual(-3, character_1, value=0.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(2, character__game_area_param_id)
    IfCharacterDead(2, character)
    IfCharacterDead(2, character_1)
    IfConditionTrue(-4, input_condition=2)
    IfTimeElapsed(-4, seconds=15.0)
    IfConditionTrue(0, input_condition=-4)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(obj)
    DisableObject(obj_1)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    Wait(3.0)
    KillBoss(game_area_param_id=character__game_area_param_id)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(name=262)
    SkipLinesIfNotEqual(5, left=left, right=12901800)
    StopPlayLogMeasurement(measurement_id=2900010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=274,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901801)
    StopPlayLogMeasurement(measurement_id=2900011)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=300,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901802)
    StopPlayLogMeasurement(measurement_id=2900012)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=326,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    SkipLinesIfNotEqual(5, left=left, right=12901803)
    StopPlayLogMeasurement(measurement_id=2900013)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=352,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    EnableFlag(left)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(left)


@NeverRestart(12901727)
def Event_12901727(_, flag: int, obj: int):
    """Event 12901727"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag)
    ForceAnimation(obj, 0, wait_for_completion=True)
    DisableObject(obj)


@NeverRestart(12901728)
def Event_12901728(_, flag: int, obj: int):
    """Event 12901728"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag)
    IfFlagEnabled(1, 92905360)
    IfFlagDisabled(1, 12907220)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(obj, 0, wait_for_completion=True)
    EnableFlag(12907220)
    DisableObject(obj)


@NeverRestart(12901730)
def Event_12901730(
    _,
    flag: int,
    item_lot_param_id: int,
    item_lot_param_id_1: int,
    item_lot_param_id_2: int,
    item_lot_param_id_3: int,
):
    """Event 12901730"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(item_lot_param_id, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_1, host_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(item_lot_param_id_2, host_only=False)
    End()
    AwardItemLot(item_lot_param_id_3, host_only=False)
    End()


@NeverRestart(12901754)
def Event_12901754(_, character: int):
    """Event 12901754"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    End()


@RestartOnRest(12904000)
def Event_12904000(_, character: int, character_1: int):
    """Event 12904000"""
    DisableCharacter(character_1)
    IfHealthLessThanOrEqual(1, character, value=0.0)
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=90,
        short_move=True,
    )
    EnableCharacter(character_1)
    ForceAnimation(character_1, 2250, loop=True)
    WaitFrames(frames=5)
    DropMandatoryTreasure(character_1)
    WaitFrames(frames=135)
    DisableCharacter(character)
    DisableBackread(character)


@RestartOnRest(12904013)
def Event_12904013(_, character: int):
    """Event 12904013"""
    IfCharacterHasSpecialEffect(0, character, 5676)
    CancelSpecialEffect(character, 5333)


@NeverRestart(12904026)
def Event_12904026(_, character: int, character_1: int, flag: int):
    """Event 12904026"""
    EndIfFlagEnabled(flag)
    DisableHealthBar(character)
    DisableHealthBar(character_1)
    EnableImmortality(character)
    EnableImmortality(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)


@NeverRestart(12904027)
def Event_12904027(_, character: int, character_1: int, character_2: int, flag: int):
    """Event 12904027"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthValueEqual(0, character, value=0)
    Kill(character_1)
    Kill(character_2)


@NeverRestart(12904028)
def Event_12904028(_, character: int, character_1: int, character_2: int, flag: int):
    """Event 12904028"""
    EndIfFlagEnabled(flag)
    IfHealthLessThanOrEqual(0, character, value=0.4000000059604645)
    AICommand(character_1, command_id=100, command_slot=1)
    AICommand(character_2, command_id=100, command_slot=1)


@NeverRestart(12904029)
def Event_12904029(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12904029"""
    EndIfClient()
    EndIfFlagEnabled(flag_4)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    IncrementEventValue(flag, bit_count=10, max_value=9)
    IfEventValueEqual(-1, flag=flag, bit_count=10, value=1)
    IfEventValueEqual(-1, flag=flag, bit_count=10, value=3)
    IfEventValueEqual(-1, flag=flag, bit_count=10, value=7)
    IfEventValueEqual(-2, flag=flag, bit_count=10, value=2)
    IfEventValueEqual(-2, flag=flag, bit_count=10, value=5)
    IfEventValueEqual(-2, flag=flag, bit_count=10, value=9)
    IfEventValueEqual(-3, flag=flag, bit_count=10, value=4)
    IfEventValueEqual(-3, flag=flag, bit_count=10, value=6)
    IfEventValueEqual(-3, flag=flag, bit_count=10, value=8)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    GotoIfConditionTrue(Label.L1, input_condition=-2)
    GotoIfConditionTrue(Label.L2, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag_1)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_2)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(flag_3)

    # --- 3 --- #
    DefineLabel(3)
    IfEventValueEqual(1, flag=flag, bit_count=10, value=9)
    SkipLinesIfConditionFalse(1, 1)
    ClearEventValue(flag, bit_count=10)
    DisableCharacter(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=90)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    Restart()


@NeverRestart(12904030)
def Event_12904030(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int):
    """Event 12904030"""
    EndIfClient()
    EndIfFlagEnabled(flag_5)
    IfFlagEnabled(0, flag)
    IncrementEventValue(flag_1, bit_count=10, max_value=12)
    IfEventValueEqual(-1, flag=flag_1, bit_count=10, value=4)
    IfEventValueEqual(-1, flag=flag_1, bit_count=10, value=6)
    IfEventValueEqual(-1, flag=flag_1, bit_count=10, value=8)
    IfEventValueEqual(-1, flag=flag_1, bit_count=10, value=11)
    IfEventValueEqual(-2, flag=flag_1, bit_count=10, value=1)
    IfEventValueEqual(-2, flag=flag_1, bit_count=10, value=5)
    IfEventValueEqual(-2, flag=flag_1, bit_count=10, value=9)
    IfEventValueEqual(-2, flag=flag_1, bit_count=10, value=12)
    IfEventValueEqual(-3, flag=flag_1, bit_count=10, value=2)
    IfEventValueEqual(-3, flag=flag_1, bit_count=10, value=3)
    IfEventValueEqual(-3, flag=flag_1, bit_count=10, value=7)
    IfEventValueEqual(-3, flag=flag_1, bit_count=10, value=10)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    GotoIfConditionTrue(Label.L1, input_condition=-2)
    GotoIfConditionTrue(Label.L2, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag_2)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_3)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(flag_4)

    # --- 3 --- #
    DefineLabel(3)
    IfEventValueEqual(1, flag=flag_1, bit_count=10, value=12)
    SkipLinesIfConditionFalse(1, 1)
    ClearEventValue(flag_1, bit_count=10)
    IfCharacterHasTAEEvent(0, character, tae_event_id=90)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    DisableFlag(flag_4)
    Restart()


@NeverRestart(12904033)
def Event_12904033(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    destination: int,
    destination_1: int,
    destination_2: int,
    flag_3: int,
):
    """Event 12904033"""
    EndIfFlagEnabled(flag_3)
    IfFlagEnabled(1, flag)
    IfCharacterDoesNotHaveSpecialEffect(1, character, 5516)
    IfFlagEnabled(2, flag_1)
    IfCharacterDoesNotHaveSpecialEffect(2, character, 5516)
    IfFlagEnabled(3, flag_2)
    IfCharacterDoesNotHaveSpecialEffect(3, character, 5516)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Wait(2.0)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, short_move=True)

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    ForceAnimation(character, 3021)
    WaitFrames(frames=70)
    Restart()


@NeverRestart(12904036)
def Event_12904036(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    destination: int,
    destination_1: int,
    destination_2: int,
    flag_3: int,
):
    """Event 12904036"""
    EndIfFlagEnabled(flag_3)
    IfFlagEnabled(1, flag)
    IfCharacterHasSpecialEffect(1, character, 5516)
    IfFlagEnabled(2, flag_1)
    IfCharacterHasSpecialEffect(2, character, 5516)
    IfFlagEnabled(3, flag_2)
    IfCharacterHasSpecialEffect(3, character, 5516)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Wait(2.0)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, short_move=True)

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(character)
    ForceAnimation(character, 3022)
    WaitFrames(frames=70)
    Restart()


@NeverRestart(12904039)
def Event_12904039(
    _,
    character: int,
    destination: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    character_1: int,
    character_2: int,
    flag_3: int,
):
    """Event 12904039"""
    EndIfFlagEnabled(flag_3)
    IfCharacterHasTAEEvent(1, character_2, tae_event_id=90)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(character, 5610)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableCharacter(character_1)
    ReplanAI(character)
    ForceAnimation(character, 3021, wait_for_completion=True)
    DisableFlag(flag)
    EnableFlag(flag_1)
    IfFlagEnabled(0, flag)
    Restart()


@NeverRestart(12904040)
def Event_12904040(_, character: int, flag: int, flag_1: int, character_1: int, character_2: int, flag_2: int):
    """Event 12904040"""
    EndIfFlagEnabled(flag_2)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHasTAEEvent(2, character_2, tae_event_id=80)
    IfFlagEnabled(2, flag_1)
    IfCharacterHasSpecialEffect(3, character_2, 5517)
    IfFlagEnabled(3, flag_1)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    ForceAnimation(character, 7010, wait_for_completion=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3020)
    WaitFrames(frames=65)

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableFlag(flag_1)
    EnableFlag(flag)
    Restart()


@RestartOnRest(12904041)
def Event_12904041(_, character__set_draw_parent: int, character: int):
    """Event 12904041"""
    DisableGravity(character)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, character__set_draw_parent)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, character__set_draw_parent, value=0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(character)
    End()
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=6,
        set_draw_parent=character__set_draw_parent,
    )
    Restart()


@RestartOnRest(12904042)
def Event_12904042(_, character: int, character_1: int):
    """Event 12904042"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    AICommand(character_1, command_id=100, command_slot=0)
    IfCharacterHasTAEEvent(0, character, tae_event_id=90)
    AICommand(character_1, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12904043)
def Event_12904043(_, character: int, region: int):
    """Event 12904043"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 9000, loop=True)
    DisableCharacterCollision(character)
    DisableGravity(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    CreatePlayLog(name=734)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, 1500, wait_for_completion=True)
    ReplanAI(character)


@RestartOnRest(12904070)
def Event_12904070(_, character: int, character_1: int, flag: int):
    """Event 12904070"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterHasTAEEvent(0, character, tae_event_id=70)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=230,
        copy_draw_parent=character,
    )

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    IfCharacterDrawGroupDisabled(0, character=character_1)
    CreatePlayLog(name=768)
    EnableCharacter(character_1)
    ReplanAI(character_1)


@RestartOnRest(12904156)
def Event_12904156(_, character: int, copy_draw_parent: int, model_point: int):
    """Event 12904156"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=copy_draw_parent,
    )
    IfCharacterDoesNotHaveTAEEvent(0, character, tae_event_id=100)
    IfCharacterDead(0, character)
    AddSpecialEffect_WithUnknownEffect(character, 5751)
    Restart()


@RestartOnRest(12904183)
def Event_12904183(_, character: int, source_flag: int):
    """Event 12904183"""
    IfCharacterDead(0, character)
    IncrementEventValue(source_flag, bit_count=3, max_value=6)
    IfCharacterAlive(0, character)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    Restart()


@RestartOnRest(12904210)
def Event_12904210(_, flag: int, character: int, flag_1: int, flag_2: int):
    """Event 12904210"""
    GotoIfFlagEnabled(Label.L0, flag=flag_2)
    IfFlagEnabled(0, flag)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag_2)
    IfTimeElapsed(0, seconds=2.0)
    AICommand(character, command_id=-1, command_slot=0)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag)
    IfEventValueGreaterThanOrEqual(1, flag=flag_1, bit_count=3, value=3)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfTimeElapsed(0, seconds=2.0)
    AICommand(character, command_id=-1, command_slot=0)
    IfTimeElapsed(0, seconds=3.0)
    Restart()


@RestartOnRest(12904216)
def Event_12904216(_, flag: int, character: int, entity: int):
    """Event 12904216"""
    DisableSpawner(entity=entity)
    IfFlagEnabled(1, flag)
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(entity=entity)
    Wait(3.0)
    IfFlagDisabled(-1, flag)
    IfCharacterDoesNotHaveTAEEvent(-1, character, tae_event_id=10)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest(12904222)
def Event_12904222(_, flag: int, character: int):
    """Event 12904222"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, character)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, character)
    IfCharacterBackreadDisabled(-2, character)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(flag)
    Restart()


@RestartOnRest(12904228)
def Event_12904228(_, character: int, source_flag: int):
    """Event 12904228"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    IncrementEventValue(source_flag, bit_count=3, max_value=6)
    IfCharacterDead(0, character)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=3,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    Restart()


@RestartOnRest(12904274)
def Event_12904274(_, flag: int, character: int, flag_1: int):
    """Event 12904274"""

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, flag)
    IfEventValueLessThanOrEqual(1, flag=flag_1, bit_count=3, value=2)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 3011)
    AICommand(character, command_id=10, command_slot=2)
    ReplanAI(character)
    IfTimeElapsed(0, seconds=2.0)
    AICommand(character, command_id=-1, command_slot=2)
    IfTimeElapsed(0, seconds=3.0)
    Restart()


@RestartOnRest(12904285)
def Event_12904285(_, flag: int, character: int, entity: int, entity_1: int, entity_2: int):
    """Event 12904285"""
    DisableSpawner(entity=entity)
    DisableSpawner(entity=entity_1)
    DisableSpawner(entity=entity_2)
    IfFlagEnabled(1, flag)
    IfCharacterHasTAEEvent(1, character, tae_event_id=20)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(entity=entity)
    EnableSpawner(entity=entity_1)
    EnableSpawner(entity=entity_2)
    Wait(3.0)
    IfFlagDisabled(-1, flag)
    IfCharacterDoesNotHaveTAEEvent(-1, character, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest(12904326)
def Event_12904326(_, flag: int, character: int):
    """Event 12904326"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, character)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, character)
    IfCharacterBackreadDisabled(-2, character)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(flag)
    Restart()


@RestartOnRest(12904337)
def Event_12904337(_, character: int, obj_act_id: int):
    """Event 12904337"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, character)
    DisableAnimations(character)
    AddSpecialEffect(character, 5401)
    DisableAI(character)
    DisableCharacter(character)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    CreatePlayLog(name=806)
    Wait(3.0)
    EnableCharacter(character)
    EnableAnimations(character)
    EnableAI(character)


@RestartOnRest(12904338)
def Event_12904338(_, obj: int, obj_act_id: int, character: int, flag: int):
    """Event 12904338"""
    EndIfFlagEnabled(flag)
    CreateTemporaryVFX(vfx_id=0, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    IfCharacterBackreadEnabled(0, character)
    DisableAI(character)
    DisableCharacter(character)
    IfObjectActivated(1, obj_act_id=obj_act_id)
    IfObjectDestroyed(2, obj)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(flag)
    CreatePlayLog(name=806)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    Wait(2.0)
    EnableCharacter(character)
    WaitFrames(frames=2)
    ForceAnimation(character, 3020)
    IfFramesElapsed(-1, frames=40)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)


@NeverRestart(12904342)
def Event_12904342(_, obj: int, obj_flag: int, obj_1: int, obj_flag_1: int, anchor_entity: int):
    """Event 12904342"""
    DisableObject(obj_1)
    EnableObject(obj)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj, 0)
    WaitFrames(frames=10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(8.5)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 10)
    WaitFrames(frames=1)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    DisableObject(obj_1)
    Restart()


@NeverRestart(12904343)
def Event_12904343(_, character: int):
    """Event 12904343"""
    SetCollisionMask(character, bit_index=0, switch_type=OnOffChange.Off)


@NeverRestart(12904345)
def Event_12904345(_, character: int):
    """Event 12904345"""
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 7007)
    AICommand(character, command_id=10, command_slot=1)
    ReplanAI(character)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 404)
    IfTimeElapsed(-1, seconds=10.0)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)


@NeverRestart(12904361)
def Event_12904361(_, character: int, character_1: int):
    """Event 12904361"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    DisableCharacter(character_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=10, part_index=NPCPartType.Part1, part_health=30)
    SetNPCPartEffects(character, npc_part_id=10, material_sfx_id=59, material_vfx_id=59)
    DisableCharacter(character_1)
    IfCharacterPartHealthLessThanOrEqual(-1, character, npc_part_id=10, value=0)
    IfHealthLessThanOrEqual(-1, character, value=0.0)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=121001)
    DisableGravity(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=40,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    SetDisplayMask(character, bit_index=0, switch_type=OnOffChange.On)
    ForceAnimation(character_1, 8100, wait_for_completion=True)
    DisableCharacter(character_1)


@NeverRestart(12904369)
def Event_12904369(_, obj: int, obj_1: int, flag: int, animation_id: int, animation_id_1: int, animation_id_2: int):
    """Event 12904369"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    PostDestruction(obj)
    ForceAnimation(obj_1, animation_id)
    EnableTreasure(obj=obj_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=900201)
    ForceAnimation(obj_1, animation_id_1)
    IfObjectDestroyed(0, obj)
    ForceAnimation(obj_1, animation_id_2, wait_for_completion=True)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)
    EnableFlag(flag)


@RestartOnRest(12904373)
def Event_12904373(_, character: int, region: int, radius: float, radius_1: float, animation_id: int):
    """Event 12904373"""
    IfCharacterInsideRegion(0, character, region=region)
    IfEntityBeyondDistance(1, entity=character, other_entity=PLAYER, radius=radius)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=radius_1)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=radius)
    IfEntityBeyondDistance(-1, entity=character, other_entity=PLAYER, radius=radius_1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(6, condition=2)
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    EnableGravity(character)
    EnableCharacterCollision(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    Restart()


@NeverRestart(12904374)
def Event_12904374(_, obj_act_id: int, character: int, obj: int):
    """Event 12904374"""
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(2.299999952316284)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    AddSpecialEffect(character, 5580)
    ForceAnimation(obj, 1)
    Wait(1.0)
    CancelSpecialEffect(character, 5580)
    WaitFrames(frames=30)
    EnableObjectActivation(obj, obj_act_id=9800)
    Restart()


@NeverRestart(12904382)
def Event_12904382(_, character: int, obj: int, radius: float, region: int, region_1: int):
    """Event 12904382"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=character, other_entity=obj, radius=radius)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=region)
    IfCharacterInsideRegion(-3, PLAYER, region=region_1)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    ActivateObjectWithSpecificCharacter(obj=obj, objact_id=9800, relative_index=-1, character=character)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest(12904390)
def Event_12904390(
    _,
    entity: int,
    entity_1: int,
    region: int,
    region_1: int,
    anchor_entity: int,
    anchor_entity_1: int,
    flag: int,
):
    """Event 12904390"""
    ForceAnimation(entity, 0)
    ForceAnimation(entity_1, 0)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(name=844)
    PlaySoundEffect(anchor_entity, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity, 0)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=anchor_entity, model_point=101, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(anchor_entity_1, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity_1, 0)
    CreateTemporaryVFX(
        vfx_id=150005,
        anchor_entity=anchor_entity_1,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    Wait(0.10000000149011612)
    EnableFlag(flag)
    ForceAnimation(entity_1, 1)
    ForceAnimation(entity, 1, wait_for_completion=True)
    ForceAnimation(entity_1, 10)
    ForceAnimation(entity, 10, wait_for_completion=True)
    DisableFlag(flag)
    Wait(0.10000000149011612)
    ForceAnimation(entity_1, 11)
    ForceAnimation(entity, 11, wait_for_completion=True)
    IfCharacterOutsideRegion(0, PLAYER, region=region)
    PlaySoundEffect(anchor_entity, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity, 1)
    PlaySoundEffect(anchor_entity_1, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity_1, 1)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest(12904398)
def Event_12904398(_, obj: int, flag: int, obj_flag: int, obj_flag_1: int, obj_flag_2: int):
    """Event 12904398"""
    AwaitFlagEnabled(flag=flag)
    SkipLinesIfFlagDisabled(3, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=6257,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=6257,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=6257,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(3, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=100,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=101,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=102,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    AwaitFlagDisabled(flag=flag)
    Restart()


@RestartOnRest(12904406)
def Event_12904406(_, character: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12904406"""
    End()
    IfEntityWithinDistance(0, entity=character, other_entity=PLAYER, radius=35.0)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfEntityBeyondDistance(0, entity=character, other_entity=PLAYER, radius=55.0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    Restart()


@RestartOnRest(12904410)
def Event_12904410(_, character: int):
    """Event 12904410"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 9000, loop=True)
    DisableCharacterCollision(character)
    DisableGravity(character)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(name=880)
    Wait(0.30000001192092896)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, 9060, wait_for_completion=True)
    ReplanAI(character)


@RestartOnRest(12904426)
def Event_12904426(_, character: int, region: int):
    """Event 12904426"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 7000, loop=True)
    DisableCharacterCollision(character)
    DisableGravity(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(name=920)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, 7001, wait_for_completion=True)
    ReplanAI(character)


@RestartOnRest(12904466)
def Event_12904466(_, character: int, region: int):
    """Event 12904466"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 9000, loop=True)
    DisableCharacterCollision(character)
    DisableGravity(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(name=920)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, 9060, wait_for_completion=True)
    ReplanAI(character)


@RestartOnRest(12904477)
def Event_12904477(_, character: int, character_1: int):
    """Event 12904477"""
    DisableCharacter(character_1)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(character_1)


@RestartOnRest(12904487)
def Event_12904487(_, character: int, character_1: int):
    """Event 12904487"""
    DisableGravity(character_1)
    IfHealthLessThanOrEqual(0, character, value=0.0)
    Wait(1.0)
    ForceAnimation(character_1, 2200, wait_for_completion=True)
    DisableCharacter(character_1)


@RestartOnRest(12904501)
def Event_12904501(_, character: int, animation_id: int):
    """Event 12904501"""
    ForceAnimation(character, 7010, loop=True)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, animation_id)


@NeverRestart(12904506)
def Event_12904506(
    _,
    character: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
    animation_id: int,
    special_effect_id: int,
    special_effect_id_1: int,
):
    """Event 12904506"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id_1)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    AddSpecialEffect(character, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904540)
def Event_12904540(
    _,
    character: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    part_health: int,
    animation_id: int,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12904540"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    AddSpecialEffect(character, 5667, affect_npc_part_hp=True)
    ReplanAI(character)


@NeverRestart(12904544)
def Event_12904544(_, character: int, bit_index: uchar):
    """Event 12904544"""
    IfCharacterBackreadEnabled(0, character)
    Wait(3.0)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)


@RestartOnRest(12904568)
def Event_12904568(_, character: int, obj: int):
    """Event 12904568"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    DisableAI(character)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, obj)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(name=970)
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=900257, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, 124005001, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(obj, 43000000, sound_type=SoundType.o_Object)
    EnableCharacter(character)
    IfFramesElapsed(0, frames=3)
    RotateToFaceEntity(character, PLAYER, animation=3024)
    IfFramesElapsed(0, frames=1)
    EnableAI(character)


@RestartOnRest(12904579)
def Event_12904579(_, character: int, obj: int, character_1: int, animation: int, radius: float):
    """Event 12904579"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableAI(character)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=radius)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, obj)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(name=970)
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=900257, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, 124005001, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(obj, 43000000, sound_type=SoundType.o_Object)
    EnableCharacter(character)
    IfFramesElapsed(0, frames=3)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    IfFramesElapsed(0, frames=1)
    EnableAI(character)


@RestartOnRest(12904584)
def Event_12904584(_, character: int, obj: int, destination: int, animation: int, region: int):
    """Event 12904584"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    DisableAI(character)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, obj)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(name=1008)
    DestroyObject(obj)
    CreateTemporaryVFX(vfx_id=900257, anchor_entity=obj, anchor_type=CoordEntityType.Object)
    PlaySoundEffect(obj, 124005001, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(obj, 43000000, sound_type=SoundType.o_Object)
    EnableCharacter(character)
    Move(
        character,
        destination=destination,
        destination_type=CoordEntityType.Character,
        model_point=101,
        short_move=True,
    )
    IfFramesElapsed(0, frames=3)
    RotateToFaceEntity(character, PLAYER, animation=animation)
    IfFramesElapsed(0, frames=1)
    EnableAI(character)


@RestartOnRest(12904594)
def Event_12904594(_, character: int, region: int, region_1: int, command_id: int, flag: int):
    """Event 12904594"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12904595)
def Event_12904595(_, character: int, region: int):
    """Event 12904595"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, character, region=region)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=3.0)
    IfAttackedWithDamageType(3, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12904596)
def Event_12904596(_, character: int, command_id: int, flag: int):
    """Event 12904596"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    IfHasAIStatus(3, character, ai_status=AIStatusType.Normal)
    IfFlagEnabled(4, flag)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12904597)
def Event_12904597(_, character: int, region: int, anchor_entity: int, vfx_id: int):
    """Event 12904597"""
    IfThisEventSlotFlagEnabled(-1)
    IfCharacterDead(-1, character)
    SkipLinesIfConditionFalse(2, -1)
    EnableCharacter(character)
    End()
    DisableCharacter(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(name=1052)
    PlaySoundEffect(anchor_entity, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity, 0, wait_for_completion=True)
    CreateTemporaryVFX(vfx_id=929200, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Object)
    EnableCharacter(character)
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)


@RestartOnRest(12904634)
def Event_12904634(
    _,
    character: int,
    summon_flag: int,
    dismissal_flag: int,
    flag: int,
    flag_1: int,
    seconds: float,
    seconds_1: float,
):
    """Event 12904634"""
    SetBackreadStateAlternate(character, False)
    DisableCharacter(character)
    End()
    DisableCharacter(character)
    IfOnline(0)
    SkipLines(1)
    EndIfFlagEnabled(flag)
    EndIfFlagEnabled(dismissal_flag)
    GotoIfFlagDisabled(Label.L0, flag=summon_flag)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfClient()
    AddSpecialEffect(character, 9025)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfCharacterHasSpecialEffect(2, PLAYER, 9020)
    IfFlagEnabled(2, flag_1)
    IfConditionTrue(0, input_condition=2)
    Wait(seconds)
    SummonNPC(
        SingleplayerSummonSignType.ScriptedInvasion,
        character,
        region=0,
        summon_flag=summon_flag,
        dismissal_flag=dismissal_flag,
    )
    Wait(seconds_1)


@RestartOnRest(12904643)
def Event_12904643(_, character__source_entity: int):
    """Event 12904643"""
    IfHasAIStatus(1, character__source_entity, ai_status=AIStatusType.Caution)
    IfHasAIStatus(2, character__source_entity, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, entity=character__source_entity, other_entity=PLAYER, radius=8.800000190734863)
    IfHealthEqual(4, character__source_entity, value=1.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(5, input_condition=-1)
    IfConditionTrue(5, input_condition=3)
    IfConditionTrue(5, input_condition=4)
    IfConditionTrue(0, input_condition=5)
    IfEntityWithinDistance(6, entity=character__source_entity, other_entity=PLAYER, radius=5.800000190734863)
    SkipLinesIfConditionTrue(9, 6)
    ForceAnimation(character__source_entity, 3010)
    WaitFrames(frames=40)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6064,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHealthNotEqual(7, character__source_entity, value=1.0)
    SkipLinesIfConditionTrue(5, 7)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=205,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=60)
    IfHealthNotEqual(8, character__source_entity, value=1.0)
    SkipLinesIfConditionTrue(1, 8)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=205,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHasAIStatus(0, character__source_entity, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(12904677)
def Event_12904677(_, character: int, character_1: int, animation_id: int):
    """Event 12904677"""
    IfCharacterHasSpecialEffect(0, character_1, 5622)
    WaitFrames(frames=5)
    ForceAnimation(character_1, animation_id)
    WaitFrames(frames=2)
    DisableCharacter(character)
    CreatePlayLog(name=1096)


@RestartOnRest(12904733)
def Event_12904733(_, region: int, obj: int):
    """Event 12904733"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    AddSpecialEffect(PLAYER, 71)
    CreateTemporaryVFX(vfx_id=850, anchor_entity=PLAYER, model_point=7, anchor_type=CoordEntityType.Character)
    IfObjectDestroyed(0, obj)
    CancelSpecialEffect(PLAYER, 71)
    CreateTemporaryVFX(vfx_id=851, anchor_entity=PLAYER, model_point=200, anchor_type=CoordEntityType.Character)


@RestartOnRest(12904736)
def Event_12904736(_, attacker__character: int, region: int, radius: float):
    """Event 12904736"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(attacker__character)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(-1, input_condition=1)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=attacker__character, radius=radius)
    IfAttacked(-1, attacked_entity=PLAYER, attacker=attacker__character)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfFinishedConditionFalse(6, condition=1)
    ForceAnimation(attacker__character, 3007)
    WaitFrames(frames=50)
    RotateToFaceEntity(attacker__character, PLAYER, animation=3006)
    EnableAI(attacker__character)
    ReplanAI(attacker__character)
    End()
    EnableAI(attacker__character)
    ReplanAI(attacker__character)


@RestartOnRest(12904737)
def Event_12904737(_, obj__source_entity: int):
    """Event 12904737"""
    EnableObjectInvulnerability(obj__source_entity)
    IfActionButtonParamActivated(-1, action_button_id=2400900, entity=obj__source_entity)
    IfObjectDamaged(-1, obj__source_entity, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(name=1132)
    ForceAnimation(obj__source_entity, 1)
    PlaySoundEffect(obj__source_entity, 24011006, sound_type=SoundType.a_Ambient)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6063,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=10)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=90)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6059,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=80)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=6062,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


@NeverRestart(12904754)
def Event_12904754(_, character: int, entity: int, entity_1: int, region: int):
    """Event 12904754"""
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 0)
    ForceAnimation(entity, 0)
    ForceAnimation(entity_1, 0, wait_for_completion=True)
    IfCharacterOutsideRegion(0, character, region=region)
    Restart()


@RestartOnRest(12904755)
def Event_12904755(_, character: int, region: int, anchor_entity: int, vfx_id: int, region_1: int):
    """Event 12904755"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EnableCharacter(character)
    End()
    DisableCharacter(character)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(name=1170)
    PlaySoundEffect(anchor_entity, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(anchor_entity, 0, wait_for_completion=True)
    CreateTemporaryVFX(vfx_id=929200, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Object)
    EnableCharacter(character)
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)
    Wait(1.0)
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=region_1)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region_1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@NeverRestart(12904759)
def Event_12904759(_, character: int, region: int):
    """Event 12904759"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(-1, input_condition=-2)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    EndIfFinishedConditionTrue(input_condition=-2)
    CreatePlayLog(name=1224)
    ForceAnimation(character, 3024, wait_for_completion=True)


@NeverRestart(12904772)
def Event_12904772(_, region: int, obj: int, character: int, region_1: int):
    """Event 12904772"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfObjectNotDestroyed(1, obj)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(character, region=region_1)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    End()


@NeverRestart(12904773)
def Event_12904773(_, target_entity: int, entity: int, flag: int):
    """Event 12904773"""
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=101130)
    Restart()


@NeverRestart(12904774)
def Event_12904774(_, flag: int, region: int, flag_1: int):
    """Event 12904774"""
    SkipLinesIfThisEventSlotFlagEnabled(3)
    IfFlagDisabled(1, flag)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfHost(1)
    NotifyBossBattleStart()
    EnableFlag(flag_1)


@NeverRestart(12904775)
def Event_12904775(_, target_entity: int, entity: int, flag: int, flag_1: int):
    """Event 12904775"""
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=101130)
    Restart()


@NeverRestart(12904776)
def Event_12904776(
    _,
    character: int,
    region: int,
    vfx_id: int,
    name: int,
    flag: int,
    flag_1: int,
    vfx_id_1: int,
    obj: int,
):
    """Event 12904776"""
    DeleteVFX(vfx_id)
    DisableCharacter(character)
    SkipLinesIfFlagDisabled(1, flag_1)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreatePlayLog(name=1260)
    StartPlayLogMeasurement(measurement_id=2900020, name=1276, overwrite=True)
    EnableObject(obj)
    CreateVFX(vfx_id)
    Wait(2.5)
    CreateTemporaryVFX(
        vfx_id=vfx_id_1,
        anchor_entity=character,
        model_point=205,
        anchor_type=CoordEntityType.Character,
    )
    WaitFrames(frames=10)
    EnableCharacter(character)
    ActivateMultiplayerBuffs(character)
    EnableAI(character)
    ReplanAI(character)
    EnableBossHealthBar(character, name=name)
    EnableFlag(flag)


@NeverRestart(12904777)
def Event_12904777(_, flag: int, flag_1: int, region: int, sound_id: int, sound_id_1: int, character: int):
    """Event 12904777"""
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=sound_id)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    DisableBossMusic(sound_id=sound_id)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=sound_id_1)


@NeverRestart(12904778)
def Event_12904778(_, character: int, flag: int):
    """Event 12904778"""
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityBeyondDistance(0, entity=PLAYER, other_entity=character, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12904779)
def Event_12904779(_, flag: int, sound_id: int, sound_id_1: int):
    """Event 12904779"""
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12904780)
def Event_12904780(_, character: int):
    """Event 12904780"""
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    ReplanAI(character)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 404)
    ReplanAI(character)
    Restart()


@NeverRestart(12904852)
def Event_12904852(_, character: int, character_1: int, character_2: int):
    """Event 12904852"""
    DisableCharacter(character_1)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    WaitFrames(frames=5)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=character,
    )
    EnableCharacter(character_1)
    ForceAnimation(character_1, 7000)
    ReplanAI(character_2)


@RestartOnRest(12904858)
def Event_12904858(_, character: int):
    """Event 12904858"""
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    AddSpecialEffect(character, 5631)
    AICommand(character, command_id=100, command_slot=0)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 5630)
    AICommand(character, command_id=110, command_slot=0)
    Restart()


@RestartOnRest(12904859)
def Event_12904859(_, character: int, first_flag: uint, last_flag: uint):
    """Event 12904859"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    EnableRandomFlagInRange(flag_range=(first_flag, last_flag))
    Wait(1.0)
    Restart()


@RestartOnRest(12904860)
def Event_12904860(_, character: int, flag: int, region: int, destination: int):
    """Event 12904860"""
    DisableFlag(flag)
    IfFlagEnabled(0, flag)
    IfCharacterInsideRegion(1, character, region=region)
    SkipLinesIfConditionTrue(3, 1)
    DisableCharacter(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SkipLines(2)
    DisableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Wait(2.0)
    EnableCharacter(character)
    RequestAnimation(character, animation_id=7000, wait_for_completion=True)
    Restart()


@RestartOnRest(12904861)
def Event_12904861(_, character: int, destination: int):
    """Event 12904861"""
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    EnableCharacter(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 7000)


@NeverRestart(12904862)
def Event_12904862(_, character: int, character_1: int, character_2: int):
    """Event 12904862"""
    IfHealthLessThanOrEqual(0, character, value=0.0)
    Kill(character_1)
    Kill(character_2)


@NeverRestart(12904863)
def Event_12904863(_, character: int, character_1: int, character_2: int, region: int, flag: int, left: int, name: int):
    """Event 12904863"""
    DisableAI(character_2)
    DisableGravity(character_2)
    DisableAI(character)
    DisableAI(character_1)
    SkipLinesIfFlagDisabled(4, left)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    DisableHealthBar(character)
    DisableHealthBar(character_1)
    ReferDamageToEntity(character, target_entity=character_2)
    ReferDamageToEntity(character_1, target_entity=character_2)
    EnableBossHealthBar(character_2, name=name)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)
    EnableFlag(flag)


@NeverRestart(12904864)
def Event_12904864(
    _,
    flag: int,
    obj: int,
    vfx_id: int,
    character: int,
    character_1: int,
    character_2: int,
    vfx_id_1: int,
    flag_1: int,
):
    """Event 12904864"""
    DisableObject(obj)
    DeleteVFX(vfx_id)
    DisableCharacter(character)
    IfFlagEnabled(0, flag)
    EnableObject(obj)
    CreateVFX(vfx_id)
    DisableFlag(flag)
    Wait(2.5)
    CreateTemporaryVFX(
        vfx_id=vfx_id_1,
        anchor_entity=character,
        model_point=205,
        anchor_type=CoordEntityType.Character,
    )
    WaitFrames(frames=10)
    EnableCharacter(character)
    ActivateMultiplayerBuffs(character)
    ActivateMultiplayerBuffs(character_1)
    ActivateMultiplayerBuffs(character_2)
    EnableAI(character)
    EnableAI(character_1)
    EnableFlag(flag_1)


@NeverRestart(12904865)
def Event_12904865(_, character: int, value: float, character_1: int):
    """Event 12904865"""
    DisableCharacter(character)
    IfCharacterHasTAEEvent(1, character_1, tae_event_id=20)
    IfHealthLessThanOrEqual(1, character_1, value=value)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)


@NeverRestart(12904866)
def Event_12904866(_, character: int, character_1: int, flag: int):
    """Event 12904866"""
    SkipLinesIfFlagDisabled(3, flag)
    DisableCharacter(character_1)
    Kill(character_1)
    End()
    IfCharacterDead(0, character)
    Kill(character_1, award_souls=True)


@NeverRestart(12904867)
def Event_12904867(_, character: int, region: int):
    """Event 12904867"""
    DisableAI(character)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    WaitFrames(frames=45)
    EnableAI(character)


@NeverRestart(12904868)
def Event_12904868(_, character: int, destination: int, destination_1: int):
    """Event 12904868"""
    IfHealthLessThanOrEqual(0, character, value=0.75)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    DisableCharacter(character)
    Wait(2.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ForceAnimation(character, 3021)
    AICommand(character, command_id=101, command_slot=0)
    ReplanAI(character)
    IfHealthLessThanOrEqual(0, character, value=0.5)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    DisableCharacter(character)
    Wait(2.0)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ForceAnimation(character, 3021)
    AICommand(character, command_id=111, command_slot=0)
    ReplanAI(character)


@NeverRestart(12904869)
def Event_12904869(_, character: int):
    """Event 12904869"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=2, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(character, npc_part_id=2, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfCharacterHasTAEEvent(3, character, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, 7000)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(5, character, value=0.0)
    IfCharacterHasTAEEvent(6, character, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(character)
    ForceAnimation(character, 7001)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(8, character, value=0.0)
    IfCharacterHasTAEEvent(9, character, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(character)
    ForceAnimation(character, 7002)
    CreateNPCPart(
        character,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=2, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=-1, overwrite_max=True)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904870)
def Event_12904870(_, character: int):
    """Event 12904870"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(character, npc_part_id=3, part_index=NPCPartType.Part3, part_health=200)
    SetNPCPartEffects(character, npc_part_id=3, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfCharacterHasTAEEvent(3, character, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, 7005)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(5, character, value=0.0)
    IfCharacterHasTAEEvent(6, character, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(character)
    ForceAnimation(character, 7006)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, character, value=0.0)
    IfCharacterHasTAEEvent(9, character, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(character)
    ForceAnimation(character, 7007)
    CreateNPCPart(
        character,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=3, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=-1, overwrite_max=True)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904871)
def Event_12904871(_, character: int):
    """Event 12904871"""
    IfCharacterBackreadEnabled(0, character)
    CreateNPCPart(
        character,
        npc_part_id=1,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=0.5,
        body_damage_correction=0.5,
    )
    SetNPCPartEffects(character, npc_part_id=1, material_sfx_id=61, material_vfx_id=61)


@NeverRestart(12904872)
def Event_12904872(_, character: int, flag: int, region: int, vfx_id: int):
    """Event 12904872"""
    DisableCharacter(character)
    SkipLinesIfFlagDisabled(1, flag)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    Wait(2.5999999046325684)
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=character, model_point=205, anchor_type=CoordEntityType.Character)
    WaitFrames(frames=10)
    EnableCharacter(character)


@NeverRestart(12904877)
def Event_12904877(
    _,
    character: int,
    region: int,
    vfx_id: int,
    character_1: int,
    flag: int,
    left: int,
    obj: int,
    character_2: int,
):
    """Event 12904877"""
    DisableAI(character)
    DisableAI(character_1)
    DisableAI(character_2)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    SkipLinesIfFlagDisabled(2, flag)
    EnableObject(obj)
    CreateVFX(vfx_id)
    SkipLinesIfFlagDisabled(4, left)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)
    SkipLinesIfFlagEnabled(2, flag)
    EnableObject(obj)
    CreateVFX(vfx_id)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 7501, affect_npc_part_hp=True)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(character)
    EnableBossHealthBar(character, name=304001)
    DisableHealthBar(character)
    EnableAI(character_1)
    EnableBossHealthBar(character_1, name=304002, bar_slot=1)
    DisableHealthBar(character_1)
    EnableAI(character_2)
    EnableBossHealthBar(character_2, name=304003, bar_slot=2)
    DisableHealthBar(character_2)
    EnableFlag(flag)


@NeverRestart(12904878)
def Event_12904878(_, target_entity: int, entity: int, flag: int, flag_1: int):
    """Event 12904878"""
    AwaitFlagEnabled(flag=flag_1)
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=101130)
    Restart()


@NeverRestart(12904879)
def Event_12904879(_, flag: int, region: int, flag_1: int):
    """Event 12904879"""
    SkipLinesIfThisEventSlotFlagEnabled(3)
    IfFlagDisabled(1, flag)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfHost(1)
    NotifyBossBattleStart()
    EnableFlag(flag_1)


@NeverRestart(12904880)
def Event_12904880(_, target_entity: int, entity: int, flag: int, flag_1: int):
    """Event 12904880"""
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=101130)
    Restart()


@NeverRestart(12904881)
def Event_12904881(_, character: int, region: int, vfx_id: int, name: int, flag: int, left: int, obj: int):
    """Event 12904881"""
    DisableAI(character)
    DisableObject(obj)
    DeleteVFX(vfx_id)
    SkipLinesIfFlagDisabled(2, flag)
    EnableObject(obj)
    CreateVFX(vfx_id)
    SkipLinesIfFlagDisabled(2, left)
    DisableCharacter(character)
    End()
    ForceAnimation(character, 7020, loop=True, skip_transition=True)
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, 7020, loop=True, skip_transition=True)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)
    SkipLinesIfFlagEnabled(2, flag)
    EnableObject(obj)
    CreateVFX(vfx_id)
    RotateToFaceEntity(character, PLAYER, animation=7021)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 7501, affect_npc_part_hp=True)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(character)
    EnableBossHealthBar(character, name=name)
    DisableHealthBar(character)
    EnableFlag(flag)


@NeverRestart(12904882)
def Event_12904882(_, flag: int, flag_1: int, region: int, sound_id: int, sound_id_1: int, character: int):
    """Event 12904882"""
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=sound_id)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    DisableBossMusic(sound_id=sound_id)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=sound_id_1)


@NeverRestart(12904883)
def Event_12904883(_, character: int, flag: int):
    """Event 12904883"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, character, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=character, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12904886)
def Event_12904886(_, flag: int, sound_id: int, sound_id_1: int):
    """Event 12904886"""
    EndIfFlagEnabled(flag)
    DisableNetworkSync()
    IfFlagEnabled(0, flag)
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12904887)
def Event_12904887(_, character: int, character_1: int, flag: int, destination: int, name: int, value: float):
    """Event 12904887"""
    DisableCharacter(character)
    IfFlagEnabled(1, flag)
    IfHealthLessThanOrEqual(1, character_1, value=value)
    IfConditionTrue(0, input_condition=1)
    Move(
        character,
        destination=character_1,
        destination_type=CoordEntityType.Character,
        model_point=-1,
        short_move=True,
    )
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    CreateTemporaryVFX(vfx_id=929203, anchor_entity=character, model_point=203, anchor_type=CoordEntityType.Character)


@RestartOnRest(12904888)
def Event_12904888(_, character: int):
    """Event 12904888"""
    IfHealthLessThan(0, character, value=0.5)
    AICommand(character, command_id=1, command_slot=1)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    AICommand(character, command_id=-1, command_slot=1)


@NeverRestart(12904890)
def Event_12904890(
    _,
    character: int,
    region: int,
    vfx_id: int,
    name: int,
    flag: int,
    flag_1: int,
    right: int,
    obj: int,
):
    """Event 12904890"""
    DisableObject(obj)
    DeleteVFX(vfx_id)
    DisableCharacter(character)
    SkipLinesIfFlagDisabled(1, flag_1)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    EnableObject(obj)
    CreateVFX(vfx_id)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=205, anchor_type=CoordEntityType.Character)
    IfValueEqual(0, left=right, right=right)
    WaitFrames(frames=10)
    EnableCharacter(character)
    ActivateMultiplayerBuffs(character)
    ForceAnimation(character, 7010, wait_for_completion=True)
    EnableAI(character)
    ReplanAI(character)
    EnableBossHealthBar(character, name=name)
    EnableFlag(flag)


@NeverRestart(12904891)
def Event_12904891(
    _,
    character: int,
    region: int,
    vfx_id: int,
    name: int,
    flag: int,
    flag_1: int,
    right: int,
    obj: int,
):
    """Event 12904891"""
    DisableObject(obj)
    DeleteVFX(vfx_id)
    DisableCharacter(character)
    SkipLinesIfFlagDisabled(1, flag_1)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    EnableObject(obj)
    CreateVFX(vfx_id)
    Wait(2.5)
    CreateTemporaryVFX(vfx_id=929227, anchor_entity=character, model_point=205, anchor_type=CoordEntityType.Character)
    IfValueEqual(0, left=right, right=right)
    WaitFrames(frames=10)
    EnableCharacter(character)
    ActivateMultiplayerBuffs(character)
    ForceAnimation(character, 7010, wait_for_completion=True)
    EnableAI(character)
    ReplanAI(character)
    EnableBossHealthBar(character, name=name)
    EnableFlag(flag)


@NeverRestart(12904892)
def Event_12904892(_, sound_id: int, sound_id_1: int):
    """Event 12904892"""
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)


@NeverRestart(12904893)
def Event_12904893(_, character: int):
    """Event 12904893"""
    IfHealthLessThan(0, character, value=0.5)
    AICommand(character, command_id=1, command_slot=1)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AICommand(character, command_id=-1, command_slot=1)


@NeverRestart(12904894)
def Event_12904894(_, character: int, flag: int):
    """Event 12904894"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    EnableFlag(flag)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)
    DisableFlag(flag)
    Restart()


@NeverRestart(12904895)
def Event_12904895(_, vfx_id: int, vfx_id_1: int, vfx_id_2: int, region: int):
    """Event 12904895"""
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    DeleteVFX(vfx_id_2, erase_root_only=False)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    CreateVFX(vfx_id)
    CreateVFX(vfx_id_1)
    CreateVFX(vfx_id_2)


@NeverRestart(12904896)
def Event_12904896(
    _,
    character: int,
    npc_part_id: short,
    npc_part_id_1: int,
    special_effect_id: int,
    special_effect_id_1: int,
    part_index: short,
    flag: int,
    flag_1: int,
):
    """Event 12904896"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfCharacterHasSpecialEffect(2, character, 5021)
    IfCharacterPartHealthLessThanOrEqual(3, character, npc_part_id=npc_part_id_1, value=0)
    IfCharacterDoesNotHaveSpecialEffect(3, character, 5021)
    IfFlagEnabled(4, flag_1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EndIfFinishedConditionTrue(input_condition=4)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=50)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    AddSpecialEffect(character, 5021, affect_npc_part_hp=True)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id_1)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 7003)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AddSpecialEffect(character, 5911, affect_npc_part_hp=True)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    CancelSpecialEffect(character, 5021)
    AddSpecialEffect(character, special_effect_id_1)
    CancelSpecialEffect(character, special_effect_id)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904897)
def Event_12904897(
    _,
    character: int,
    npc_part_id: short,
    npc_part_id_1: int,
    special_effect_id: int,
    special_effect_id_1: int,
    part_index: short,
    flag: int,
    flag_1: int,
):
    """Event 12904897"""
    EndIfFlagEnabled(flag_1)
    IfFlagEnabled(1, flag)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfCharacterHasSpecialEffect(2, character, 5021)
    IfCharacterPartHealthLessThanOrEqual(3, character, npc_part_id=npc_part_id_1, value=0)
    IfCharacterDoesNotHaveSpecialEffect(3, character, 5021)
    IfFlagEnabled(4, flag_1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EndIfFinishedConditionTrue(input_condition=4)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=50)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=66, material_vfx_id=66)
    AddSpecialEffect(character, 5021, affect_npc_part_hp=True)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id_1)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 7000)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AddSpecialEffect(character, 5911, affect_npc_part_hp=True)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    CancelSpecialEffect(character, 5021)
    AddSpecialEffect(character, special_effect_id_1)
    CancelSpecialEffect(character, special_effect_id)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904898)
def Event_12904898(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904898"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904899)
def Event_12904899(_, character: int, npc_part_id: short, npc_part_id_1: int, flag: int, flag_1: int):
    """Event 12904899"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=130)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=130, overwrite_max=True)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12904900)
def Event_12904900(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904900"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904901)
def Event_12904901(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904901"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904902)
def Event_12904902(_, character: int, npc_part_id: short, npc_part_id_1: int, flag: int, flag_1: int):
    """Event 12904902"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=150, overwrite_max=True)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12904903)
def Event_12904903(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904903"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904904)
def Event_12904904(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904904"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904905)
def Event_12904905(_, character: int, npc_part_id: short, npc_part_id_1: int, flag: int, flag_1: int):
    """Event 12904905"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=150, overwrite_max=True)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12904906)
def Event_12904906(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904906"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904907)
def Event_12904907(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904907"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904908)
def Event_12904908(_, character: int, npc_part_id: short, npc_part_id_1: int, flag: int, flag_1: int):
    """Event 12904908"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=200, overwrite_max=True)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12904909)
def Event_12904909(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904909"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904910)
def Event_12904910(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904910"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904913)
def Event_12904913(_, character: int, npc_part_id: short, npc_part_id_1: int, flag: int, flag_1: int):
    """Event 12904913"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=200, overwrite_max=True)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12904911)
def Event_12904911(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12904911"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12904912)
def Event_12904912(_, character: int):
    """Event 12904912"""
    IfHealthLessThan(0, character, value=0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 7010)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    IfHealthLessThan(0, character, value=0.33000001311302185)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 7011)
    AICommand(character, command_id=101, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@NeverRestart(12904914)
def Event_12904914(
    _,
    special_effect: int,
    special_effect_1: int,
    bit_index: uchar,
    bit_index_1: uchar,
    bit_index_2: uchar,
    character: int,
):
    """Event 12904914"""
    IfCharacterHasSpecialEffect(1, character, special_effect)
    IfCharacterDoesNotHaveSpecialEffect(1, character, special_effect_1)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_2, switch_type=OnOffChange.On)
    IfCharacterDoesNotHaveSpecialEffect(2, character, special_effect)
    IfCharacterHasSpecialEffect(2, character, special_effect_1)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904915)
def Event_12904915(_, character: int):
    """Event 12904915"""
    IfCharacterHasSpecialEffect(0, character, 482)
    ChangeCharacterCloth(character, bit_count=15, state_id=2)


@NeverRestart(12904916)
def Event_12904916(_, character: int):
    """Event 12904916"""
    IfCharacterHasSpecialEffect(0, character, 420)
    WaitFrames(frames=10)
    CancelSpecialEffect(character, 420)
    Restart()


@NeverRestart(12904917)
def Event_12904917(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    special_effect_id: int,
    flag: int,
    character: int,
):
    """Event 12904917"""
    IfFlagEnabled(1, flag)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=1)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfCharacterPartHealthLessThanOrEqual(3, character, npc_part_id=npc_part_id_1, value=0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    IfCharacterHasSpecialEffect(7, character, 420)
    SkipLinesIfConditionFalse(1, 7)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12904918)
def Event_12904918(
    _,
    special_effect__special_effect_id: int,
    animation_id: int,
    npc_part_id: int,
    flag: int,
    character: int,
):
    """Event 12904918"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfFlagEnabled(0, flag)
    IfCharacterHasSpecialEffect(1, character, special_effect__special_effect_id)
    IfCharacterHasSpecialEffect(1, character, 421)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=npc_part_id, value=0)
    IfCharacterHasSpecialEffect(2, character, special_effect__special_effect_id)
    IfCharacterHasSpecialEffect(2, character, 421)
    IfCharacterPartHealthComparison(
        2,
        character,
        npc_part_id=npc_part_id,
        value=0,
        comparison_type=ComparisonType.GreaterThan,
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    SkipLines(1)
    AddSpecialEffect(character, special_effect__special_effect_id, affect_npc_part_hp=True)
    Restart()


@RestartOnRest(12904919)
def Event_12904919(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12904919"""
    IfFlagEnabled(-1, 92905320)
    IfFlagEnabled(-1, 92905324)
    IfFlagEnabled(-1, 92905325)
    IfFlagEnabled(-1, 92905326)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12904979)
def Event_12904979(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12904979"""
    IfFlagEnabled(-1, 92905321)
    IfFlagEnabled(-1, 92905327)
    IfFlagEnabled(-1, 92905328)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905000)
def Event_12905000(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905000"""
    IfFlagEnabled(-1, 92905322)
    IfFlagEnabled(-1, 92905329)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905013)
def Event_12905013(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905013"""
    IfFlagEnabled(-1, 92905323)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905026)
def Event_12905026(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905026"""
    EndIfFlagRangeAllDisabled(flag_range=(92905320, 92905329))
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905042)
def Event_12905042(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905042"""
    IfFlagEnabled(-1, 92905320)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905097)
def Event_12905097(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905097"""
    IfFlagEnabled(-1, 92905321)
    IfFlagEnabled(-1, 92905324)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905108)
def Event_12905108(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905108"""
    IfFlagEnabled(-1, 92905322)
    IfFlagEnabled(-1, 92905325)
    IfFlagEnabled(-1, 92905327)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905119)
def Event_12905119(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905119"""
    IfFlagEnabled(-1, 92905323)
    IfFlagEnabled(-1, 92905326)
    IfFlagEnabled(-1, 92905328)
    IfFlagEnabled(-1, 92905329)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905130)
def Event_12905130(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    obj: int,
):
    """Event 12905130"""
    EndIfFlagRangeAllDisabled(flag_range=(92905320, 92905329))
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableCharacter(character_6)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableBackread(character_6)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    End()


@RestartOnRest(12905147)
def Event_12905147(_, character: int, flag: int):
    """Event 12905147"""
    DisableHealthBar(character)
    EnableImmortality(character)
    AddSpecialEffect(character, 5626)
    IfFlagEnabled(0, flag)
    WaitRandomFrames(min_frames=0, max_frames=50)
    DisableImmortality(character)
    Kill(character, award_souls=True)
    End()


@RestartOnRest(12905178)
def Event_12905178(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    character_6: int,
    flag: int,
):
    """Event 12905178"""
    IfCharacterBackreadEnabled(-1, character)
    IfCharacterBackreadEnabled(-1, character_1)
    IfCharacterBackreadEnabled(-1, character_2)
    IfCharacterBackreadEnabled(-1, character_3)
    IfCharacterBackreadEnabled(-1, character_4)
    IfCharacterBackreadEnabled(-1, character_5)
    IfCharacterBackreadEnabled(-1, character_6)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(character, 5913)
    AddSpecialEffect(character_1, 5913)
    AddSpecialEffect(character_2, 5913)
    AddSpecialEffect(character_3, 5913)
    AddSpecialEffect(character_4, 5913)
    AddSpecialEffect(character_5, 5913)
    AddSpecialEffect(character_6, 5913)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_1, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_2, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_3, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_4, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_5, radius=7.0)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character_6, radius=7.0)
    RestartIfConditionFalse(-2)
    CancelSpecialEffect(character, 5913)
    CancelSpecialEffect(character_1, 5913)
    CancelSpecialEffect(character_2, 5913)
    CancelSpecialEffect(character_3, 5913)
    CancelSpecialEffect(character_4, 5913)
    CancelSpecialEffect(character_5, 5913)
    CancelSpecialEffect(character_6, 5913)
    AddSpecialEffect(character, 5625)
    AddSpecialEffect(character_1, 5625)
    AddSpecialEffect(character_2, 5625)
    AddSpecialEffect(character_3, 5625)
    AddSpecialEffect(character_4, 5625)
    AddSpecialEffect(character_5, 5625)
    AddSpecialEffect(character_6, 5625)
    EnableHealthBar(character)
    EnableHealthBar(character_1)
    EnableHealthBar(character_2)
    EnableHealthBar(character_3)
    EnableHealthBar(character_4)
    EnableHealthBar(character_5)
    EnableHealthBar(character_6)
    Wait(1.0)
    IfCharacterHasSpecialEffect(-3, character, 5913)
    IfValueEqual(-3, left=character, right=0)
    IfCharacterHasSpecialEffect(-4, character_1, 5913)
    IfValueEqual(-4, left=character_1, right=0)
    IfCharacterHasSpecialEffect(-5, character_2, 5913)
    IfValueEqual(-5, left=character_2, right=0)
    IfCharacterHasSpecialEffect(-6, character_3, 5913)
    IfValueEqual(-6, left=character_3, right=0)
    IfCharacterHasSpecialEffect(-7, character_4, 5913)
    IfValueEqual(-7, left=character_4, right=0)
    IfCharacterHasSpecialEffect(-8, character_5, 5913)
    IfValueEqual(-8, left=character_5, right=0)
    IfCharacterHasSpecialEffect(-8, character_6, 5913)
    IfValueEqual(-8, left=character_6, right=0)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(1, input_condition=-5)
    IfConditionTrue(1, input_condition=-6)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(1, input_condition=-8)
    IfConditionTrue(1, input_condition=-9)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)
    End()


@RestartOnRest(12905188)
def Event_12905188(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
):
    """Event 12905188"""
    IfFlagEnabled(-1, 92905330)
    IfFlagEnabled(-1, 92905332)
    IfFlagEnabled(-1, 92905333)
    IfFlagEnabled(-1, 92905334)
    IfFlagRangeAnyEnabled(-1, flag_range=(92905385, 92905389))
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-2, 92905332)
    IfFlagEnabled(-2, 92905334)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(-3, 1423)
    IfFlagEnabled(-3, 1432)
    IfConditionTrue(1, input_condition=-3)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()


@RestartOnRest(12905190)
def Event_12905190(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
):
    """Event 12905190"""
    IfFlagEnabled(-1, 92905331)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()


@RestartOnRest(12905192)
def Event_12905192(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
):
    """Event 12905192"""
    SkipLinesIfFlagRangeAnyEnabled(1, (92905385, 92905389))
    EndIfFlagRangeAllDisabled(flag_range=(92905330, 92905334))
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()


@RestartOnRest(12905195)
def Event_12905195():
    """Event 12905195"""
    End()


@RestartOnRest(12905198)
def Event_12905198(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
):
    """Event 12905198"""
    IfFlagEnabled(-1, 92905331)
    IfFlagEnabled(-1, 92905333)
    IfFlagEnabled(-1, 92905334)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()


@RestartOnRest(12905201)
def Event_12905201(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    obj: int,
    obj_1: int,
    obj_2: int,
    obj_3: int,
):
    """Event 12905201"""
    IfFlagDisabled(1, 92905331)
    IfFlagDisabled(1, 92905333)
    IfFlagDisabled(1, 92905334)
    EndIfConditionTrue(1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    DisableObject(obj_2)
    DisableObjectActivation(obj_2, obj_act_id=-1)
    DisableTreasure(obj=obj_2)
    DisableObject(obj_3)
    DisableObjectActivation(obj_3, obj_act_id=-1)
    DisableTreasure(obj=obj_3)
    End()


@RestartOnRest(12905209)
def Event_12905209(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905209"""
    IfFlagEnabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905210)
def Event_12905210(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905210"""
    IfFlagDisabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905211)
def Event_12905211(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905211"""
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905212)
def Event_12905212(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905212"""
    IfFlagEnabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905221)
def Event_12905221(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905221"""
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905226)
def Event_12905226(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    character_5: int,
    obj: int,
    obj_1: int,
):
    """Event 12905226"""
    IfFlagDisabled(-1, 92905340)
    EndIfConditionTrue(-1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    DisableCharacter(character_2)
    DisableCharacter(character_3)
    DisableCharacter(character_4)
    DisableCharacter(character_5)
    DisableBackread(character)
    DisableBackread(character_1)
    DisableBackread(character_2)
    DisableBackread(character_3)
    DisableBackread(character_4)
    DisableBackread(character_5)
    DisableObject(obj)
    DisableObjectActivation(obj, obj_act_id=-1)
    DisableTreasure(obj=obj)
    DisableObject(obj_1)
    DisableObjectActivation(obj_1, obj_act_id=-1)
    DisableTreasure(obj=obj_1)
    End()


@RestartOnRest(12905232)
def Event_12905232(_, first_flag: int, last_flag: int, character: int):
    """Event 12905232"""
    IfFlagRangeAllDisabled(0, flag_range=(first_flag, last_flag))
    DisableCharacter(character)


@RestartOnRest(12905233)
def Event_12905233(_, character: int, character_1: int):
    """Event 12905233"""
    DisableAnimations(character)
    DisableAnimations(character_1)
    DisableGravity(character)
    DisableGravity(character_1)
    DisableCharacterCollision(character)
    DisableCharacterCollision(character_1)


@RestartOnRest(12905235)
def Event_12905235(_, entity: int, entity_1: int):
    """Event 12905235"""
    ForceAnimation(entity, 7001, loop=True)
    ForceAnimation(entity_1, 7002, loop=True)
    IfFlagEnabled(0, 12907224)
    ForceAnimation(entity, 7005)
    ForceAnimation(entity_1, 7006)
    WaitFrames(frames=29)
    ForceAnimation(entity, 7003, loop=True)
    ForceAnimation(entity_1, 7004, loop=True)
    IfFlagDisabled(0, 12907224)
    ForceAnimation(entity, 7007)
    ForceAnimation(entity_1, 7008)
    WaitFrames(frames=28)
    Restart()


@RestartOnRest(12905237)
def Event_12905237(_, character: int, character_1: int):
    """Event 12905237"""
    WaitFrames(frames=12)
    IfPlayerHasGood(1, 4111)
    SkipLinesIfConditionTrue(2, 1)
    SetDisplayMask(character, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.On)
    IfPlayerHasGood(2, 4112)
    SkipLinesIfConditionTrue(2, 2)
    SetDisplayMask(character, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=13, switch_type=OnOffChange.On)
    IfPlayerHasGood(3, 4113)
    SkipLinesIfConditionTrue(1, 3)
    SetDisplayMask(character, bit_index=3, switch_type=OnOffChange.On)
    IfPlayerHasGood(4, 4114)
    SkipLinesIfConditionTrue(1, 4)
    SetDisplayMask(character_1, bit_index=0, switch_type=OnOffChange.On)
    IfPlayerHasGood(5, 4115)
    SkipLinesIfConditionTrue(2, 5)
    SetDisplayMask(character_1, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(character_1, bit_index=12, switch_type=OnOffChange.On)
    IfPlayerHasGood(6, 4116)
    SkipLinesIfConditionTrue(2, 6)
    SetDisplayMask(character_1, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(character_1, bit_index=11, switch_type=OnOffChange.On)
    IfPlayerHasGood(7, 4117)
    SkipLinesIfConditionTrue(1, 7)
    SetDisplayMask(character_1, bit_index=3, switch_type=OnOffChange.On)


@RestartOnRest(12905239)
def Event_12905239(_, first_flag: int, last_flag: int, character: int):
    """Event 12905239"""
    IfFlagRangeAnyEnabled(0, flag_range=(first_flag, last_flag))
    DisableCharacter(character)


@RestartOnRest(12905243)
def Event_12905243(_, first_flag: int, last_flag: int, obj: int):
    """Event 12905243"""
    IfFlagRangeAllDisabled(0, flag_range=(first_flag, last_flag))
    DisableObject(obj)
    DisableTreasure(obj=obj)


@RestartOnRest(12905244)
def Event_12905244(_, first_flag: int, last_flag: int, obj: int):
    """Event 12905244"""
    IfFlagRangeAnyEnabled(0, flag_range=(first_flag, last_flag))
    DisableObject(obj)
    DisableTreasure(obj=obj)


@NeverRestart(12905245)
def Event_12905245(_, map_piece_id: int, flag: int, map_piece_id_1: int):
    """Event 12905245"""
    SkipLinesIfFlagDisabled(2, flag)
    DisableMapPiece(map_piece_id=map_piece_id)
    SkipLines(1)
    DisableMapPiece(map_piece_id=map_piece_id_1)
    End()


@NeverRestart(12905271)
def Event_12905271(_, collision: int, flag: int, collision_1: int):
    """Event 12905271"""
    SkipLinesIfFlagDisabled(2, flag)
    DisableMapCollision(collision=collision)
    SkipLines(1)
    DisableMapCollision(collision=collision_1)
    End()


@NeverRestart(12905302)
def Event_12905302(_, collision: int):
    """Event 12905302"""
    DisableMapCollision(collision=collision)
    SkipLines(1)


@NeverRestart(12905303)
def Event_12905303(_, entity: int, collision: int):
    """Event 12905303"""
    IfPlayerMovingOnCollision(0, collision)
    ForceAnimation(entity, 0, wait_for_completion=True)
    Restart()


@RestartOnRest(12905314)
def Event_12905314(_, character: int, flag: int):
    """Event 12905314"""
    WaitFrames(frames=1)
    End()
    IfFlagEnabled(0, flag)
    IfHealthEqual(0, character, value=1.0)
    WaitFrames(frames=1)
    End()


@RestartOnRest(12905337)
def Event_12905337(_, character__set_draw_parent: int, character: int):
    """Event 12905337"""
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, character__set_draw_parent)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, character__set_draw_parent, value=0.0)
    SkipLinesIfConditionFalse(3, 1)
    DisableAI(character)
    ForceAnimation(character, 3002, wait_for_completion=True)
    End()
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=6,
        set_draw_parent=character__set_draw_parent,
    )
    Restart()


@RestartOnRest(12905347)
def Event_12905347(_, character: int, character_1: int):
    """Event 12905347"""
    IfCharacterHasSpecialEffect(0, character, 5401)
    AICommand(character_1, command_id=100, command_slot=0)
    IfCharacterHasSpecialEffect(0, character, 5400)
    AICommand(character_1, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12905357)
def Event_12905357(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    ai_param_id: int,
    ai_param_id_1: int,
):
    """Event 12905357"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfHealthNotEqual(-1, character, value=1.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=5.0)
    SkipLinesIfConditionTrue(1, 1)
    ForceAnimation(character, animation_id_2)


@RestartOnRest(12905369)
def Event_12905369(_, character: int, animation_id: int, animation_id_1: int):
    """Event 12905369"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(character, animation_id, loop=True)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfHealthNotEqual(-1, character, value=1.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)


@RestartOnRest(12905387)
def Event_12905387(_, character: int):
    """Event 12905387"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(character, 7000, loop=True)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=2.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7001)
    ReplanAI(character)


@RestartOnRest(12905396)
def Event_12905396(_, character: int):
    """Event 12905396"""
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(character, 7000, loop=True)
    SetAIParamID(character, ai_param_id=218085)
    AddSpecialEffect(character, 5629)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=2.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7001)
    SetAIParamID(character, ai_param_id=218080)
    CancelSpecialEffect(character, 5629)
    ReplanAI(character)


@RestartOnRest(12905401)
def Event_12905401(_, obj_act_id: int, flag: int):
    """Event 12905401"""
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=45)
    EnableFlag(flag)


@RestartOnRest(12905402)
def Event_12905402(_, obj: int, flag: int):
    """Event 12905402"""
    IfObjectDamaged(-1, obj, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=45)
    EnableFlag(flag)


@RestartOnRest(12905403)
def Event_12905403(_, flag: int, flag_1: int):
    """Event 12905403"""
    IfFlagEnabled(0, flag)
    Wait(8.0)
    EnableFlag(flag_1)


@NeverRestart(12905404)
def Event_12905404(_, obj_act_id: int, flag: int):
    """Event 12905404"""
    IfObjectActivated(0, obj_act_id=obj_act_id)
    CreatePlayLog(name=0)
    WaitFrames(frames=100)
    EnableFlag(flag)


@NeverRestart(12905406)
def Event_12905406(_, character: int, flag: int):
    """Event 12905406"""
    DisableCharacter(character)
    End()
    IfPlayerInsightAmountGreaterThanOrEqual(1, value=10)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)
    EnableFlag(flag)


@NeverRestart(12905407)
def Event_12905407(_, character: int, flag: int):
    """Event 12905407"""
    End()
    IfFlagEnabled(1, flag)
    IfPlayerInsightAmountLessThanOrEqual(1, value=8)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(character)


@RestartOnRest(12906400)
def Event_12906400(_, obj__source_entity: int):
    """Event 12906400"""
    IfAttackedWithDamageType(1, attacked_entity=obj__source_entity, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(2, attacked_entity=obj__source_entity, damage_type=DamageType.NoType)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfObjectHealthValueComparison(-1, obj__source_entity, ComparisonType.LessThan, value=999)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(7, condition=-2)
    DestroyObject(obj__source_entity)
    PlaySoundEffect(obj__source_entity, 299961000, sound_type=SoundType.o_Object)
    WaitFrames(frames=10)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=45)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    End()
    CreatePlayLog(name=1462)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6150,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6151,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6152,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6153,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6154,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6155,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6156,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6157,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    IfFlagEnabled(-2, 92905100)
    IfFlagEnabled(-2, 92905101)
    IfFlagEnabled(-2, 92905102)
    IfFlagEnabled(-2, 92905103)
    IfFlagEnabled(-2, 92905104)
    IfFlagEnabled(-2, 92905105)
    IfFlagEnabled(-2, 92905106)
    IfFlagEnabled(-2, 92905107)
    SkipLinesIfConditionTrue(1, -2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6000,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=200,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__source_entity)
    PlaySoundEffect(obj__source_entity, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(12906500)
def Event_12906500(_, character: int, character_1: int):
    """Event 12906500"""
    EnableImmortality(character)
    IfCharacterDead(0, character_1)
    DisableImmortality(character)
    Kill(character, award_souls=True)


@NeverRestart(12906534)
def Event_12906534(
    _,
    obj: int,
    obj_flag: int,
    obj_1: int,
    obj_flag_1: int,
    obj_2: int,
    obj_flag_2: int,
    anchor_entity: int,
):
    """Event 12906534"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(frames=45)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 0)
    WaitFrames(frames=10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    Wait(5.599999904632568)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    DisableObject(obj_1)
    EnableObject(obj_2)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_2, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(obj_flag=obj_flag_2)
    DisableObject(obj_2)
    Restart()


@NeverRestart(12906537)
def Event_12906537(
    _,
    obj: int,
    obj_flag: int,
    obj_1: int,
    obj_flag_1: int,
    obj_2: int,
    obj_flag_2: int,
    anchor_entity: int,
):
    """Event 12906537"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(frames=45)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 0)
    WaitFrames(frames=10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(6.0)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    DisableObject(obj_1)
    EnableObject(obj_2)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_2, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(obj_flag=obj_flag_2)
    DisableObject(obj_2)
    Restart()


@NeverRestart(12906540)
def Event_12906540(
    _,
    obj: int,
    obj_flag: int,
    obj_1: int,
    obj_flag_1: int,
    obj_2: int,
    obj_flag_2: int,
    anchor_entity: int,
    region: int,
):
    """Event 12906540"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    ForceAnimation(obj, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(frames=45)
    RemoveObjectFlag(obj_flag=obj_flag)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 0)
    WaitFrames(frames=10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj_1,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    Wait(12.0)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    DisableObject(obj_1)
    EnableObject(obj_2)
    PlaySoundEffect(anchor_entity, 290000004, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000005, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_2, 10)
    WaitFrames(frames=5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    IfFlagEnabled(-1, 92905100)
    IfFlagEnabled(-1, 92905101)
    IfFlagEnabled(-1, 92905102)
    IfFlagEnabled(-1, 92905103)
    IfFlagEnabled(-1, 92905104)
    IfFlagEnabled(-1, 92905105)
    IfFlagEnabled(-1, 92905106)
    IfFlagEnabled(-1, 92905107)
    SkipLinesIfConditionTrue(1, -1)
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj_2,
        model_point=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(obj_flag=obj_flag_2)
    DisableObject(obj_2)
    End()


@NeverRestart(12906541)
def Event_12906541(
    _,
    obj: int,
    obj_1: int,
    obj_2: int,
    region: int,
    region_1: int,
    character: int,
    anchor_entity: int,
    obj_flag: int,
):
    """Event 12906541"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    ForceAnimation(obj, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterDead(-1, character)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 3000, wait_for_completion=True)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 20)
    CreateObjectVFX(obj_1, vfx_id=100, model_point=900260)
    WaitFrames(frames=30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    IfFlagEnabled(-4, 92905100)
    IfFlagEnabled(-4, 92905101)
    IfFlagEnabled(-4, 92905102)
    IfFlagEnabled(-4, 92905103)
    IfFlagEnabled(-4, 92905104)
    IfFlagEnabled(-4, 92905105)
    IfFlagEnabled(-4, 92905106)
    IfFlagEnabled(-4, 92905107)
    SkipLinesIfConditionTrue(1, -4)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    WaitFrames(frames=370)
    RemoveObjectFlag(obj_flag=obj_flag)
    DeleteObjectVFX(obj_1)
    EnableObject(obj_2)
    ForceAnimation(obj_2, 100)
    DestroyObject(obj_2)
    DisableObject(obj_1)


@NeverRestart(12906543)
def Event_12906543(
    _,
    obj: int,
    obj_1: int,
    obj_2: int,
    region: int,
    region_1: int,
    character: int,
    anchor_entity: int,
    obj_flag: int,
):
    """Event 12906543"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    ForceAnimation(obj, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterDead(-1, character)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 3000, wait_for_completion=True)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 30)
    CreateObjectVFX(obj_1, vfx_id=100, model_point=900260)
    WaitFrames(frames=30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    IfFlagEnabled(-4, 92905100)
    IfFlagEnabled(-4, 92905101)
    IfFlagEnabled(-4, 92905102)
    IfFlagEnabled(-4, 92905103)
    IfFlagEnabled(-4, 92905104)
    IfFlagEnabled(-4, 92905105)
    IfFlagEnabled(-4, 92905106)
    IfFlagEnabled(-4, 92905107)
    SkipLinesIfConditionTrue(1, -4)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    WaitFrames(frames=270)
    RemoveObjectFlag(obj_flag=obj_flag)
    DeleteObjectVFX(obj_1)
    EnableObject(obj_2)
    ForceAnimation(obj_2, 100)
    DestroyObject(obj_2)
    DisableObject(obj_1)


@NeverRestart(12906545)
def Event_12906545(
    _,
    obj: int,
    obj_1: int,
    obj_2: int,
    region: int,
    region_1: int,
    character: int,
    anchor_entity: int,
    obj_flag: int,
):
    """Event 12906545"""
    DisableObject(obj_1)
    DisableObject(obj_2)
    EnableObject(obj)
    ForceAnimation(obj, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterInsideRegion(-1, PLAYER, region=region_1)
    IfCharacterDead(-1, character)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 3000, wait_for_completion=True)
    DisableObject(obj)
    EnableObject(obj_1)
    PlaySoundEffect(anchor_entity, 290000002, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(anchor_entity, 290000003, sound_type=SoundType.a_Ambient)
    ForceAnimation(obj_1, 40)
    CreateObjectVFX(obj_1, vfx_id=100, model_point=900260)
    WaitFrames(frames=30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=6147,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    IfFlagEnabled(-4, 92905100)
    IfFlagEnabled(-4, 92905101)
    IfFlagEnabled(-4, 92905102)
    IfFlagEnabled(-4, 92905103)
    IfFlagEnabled(-4, 92905104)
    IfFlagEnabled(-4, 92905105)
    IfFlagEnabled(-4, 92905106)
    IfFlagEnabled(-4, 92905107)
    SkipLinesIfConditionTrue(1, -4)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj_1,
        model_point=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    WaitFrames(frames=270)
    RemoveObjectFlag(obj_flag=obj_flag)
    DeleteObjectVFX(obj_1)
    EnableObject(obj_2)
    ForceAnimation(obj_2, 100)
    DestroyObject(obj_2)
    DisableObject(obj_1)


@RestartOnRest(12906548)
def Event_12906548(_, character: int, character_1: int):
    """Event 12906548"""
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfEntityWithinDistance(1, entity=character, other_entity=character_1, radius=25.0)
    IfCharacterAlive(1, character_1)
    IfConditionTrue(0, input_condition=1)
    AICommand(character_1, command_id=200, command_slot=1)
    IfCharacterHasTAEEvent(0, character_1, tae_event_id=20)
    AddSpecialEffect(character_1, 5645)
    AICommand(character_1, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(12906567)
def Event_12906567(_, character: int, special_effect_id: int):
    """Event 12906567"""
    IfCharacterHasSpecialEffect(0, character, 5645)
    AddSpecialEffect(character, special_effect_id)
    IfCharacterDoesNotHaveSpecialEffect(0, character, 5645)
    CancelSpecialEffect(character, special_effect_id)
    Restart()


@RestartOnRest(12906586)
def Event_12906586(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    ai_param_id: int,
    ai_param_id_1: int,
    ai_param_id_2: int,
    animation_id_2: int,
):
    """Event 12906586"""
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(2, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(3, character, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(4, character, 4740)
    IfAttackedWithDamageType(5, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    IfHasAIStatus(6, character, ai_status=AIStatusType.Normal)
    IfHasAIStatus(7, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(8, character, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(9, character, 4740)
    IfAttackedWithDamageType(10, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(-3, input_condition=10)
    IfConditionTrue(-4, input_condition=7)
    IfConditionTrue(-4, input_condition=8)
    IfConditionTrue(-4, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=10)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-4)
    Wait(3.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, animation_id_2)

    # --- 1 --- #
    DefineLabel(1)
    SetAIParamID(character, ai_param_id=ai_param_id_2)


@RestartOnRest(12906648)
def Event_12906648(_, character: int, character_1: int, animation_id: int, destination: int):
    """Event 12906648"""
    IfCharacterBackreadEnabled(0, character_1)
    DisableAI(character_1)
    DisableGravity(character_1)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=60)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character_1, animation_id, wait_for_completion=True)
    EnableGravity(character_1)
    EnableAI(character_1)
    ReplanAI(character_1)


@RestartOnRest(12906654)
def Event_12906654(_, character__source_entity: int, region: int):
    """Event 12906654"""
    IfHasAIStatus(-1, character__source_entity, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__source_entity, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character__source_entity, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(character__source_entity, region=region)
    AICommand(character__source_entity, command_id=10, command_slot=0)
    ResetAnimation(character__source_entity)
    ReplanAI(character__source_entity)
    Wait(3.0)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=32,
        behavior_id=210200599,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    PlaySoundEffect(character__source_entity, 225000000, sound_type=SoundType.a_Ambient)
    IfCharacterInsideRegion(0, character__source_entity, region=region)
    ForceAnimation(character__source_entity, 3010, wait_for_completion=True)
    PlaySoundEffect(character__source_entity, 225000000, sound_type=SoundType.a_Ambient)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=32,
        behavior_id=210200599,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__source_entity, 7004, wait_for_completion=True)
    AICommand(character__source_entity, command_id=-1, command_slot=0)
    ReplanAI(character__source_entity)


@RestartOnRest(12906655)
def Event_12906655(_, character: int, animation_id: int):
    """Event 12906655"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(12906656)
def Event_12906656(_, character: int, sound_id: int, character__source_entity: int):
    """Event 12906656"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfHealthEqual(1, character, value=1.0)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    IfEntityWithinDistance(3, entity=character, other_entity=PLAYER, radius=5.0)
    SkipLinesIfConditionTrue(23, 3)
    Move(
        character__source_entity,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        model_point=236,
        copy_draw_parent=PLAYER,
    )
    PlaySoundEffect(character, sound_id, sound_type=SoundType.c_CharacterMotion)
    ForceAnimation(character, 3020)
    WaitFrames(frames=40)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6064,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHealthNotEqual(4, character, value=1.0)
    SkipLinesIfConditionTrue(17, 4)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=90)
    IfHealthNotEqual(5, character, value=1.0)
    SkipLinesIfConditionTrue(13, 5)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6054,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=90)
    IfHealthNotEqual(6, character, value=1.0)
    SkipLinesIfConditionTrue(9, 6)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=60)
    IfHealthNotEqual(7, character, value=1.0)
    SkipLinesIfConditionTrue(5, 7)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(frames=60)
    IfHealthNotEqual(8, character, value=1.0)
    SkipLinesIfConditionTrue(1, 8)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@NeverRestart(12906660)
def Event_12906660(_, obj__source_entity: int):
    """Event 12906660"""
    EndIfObjectDestroyed(obj__source_entity)
    GotoIfFlagEnabled(Label.L1, flag=92905310)
    GotoIfFlagEnabled(Label.L0, flag=92905301)
    CreateObjectVFX(obj__source_entity, vfx_id=600, model_point=929302)
    IfObjectDamaged(0, obj__source_entity, attacker=-1)
    Goto(Label.L3)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(obj__source_entity, vfx_id=600, model_point=929305)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6090,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(obj__source_entity, vfx_id=600, model_point=929304)
    SkipLinesIfFlagEnabled(21, 92905107)
    SkipLinesIfFlagEnabled(18, 92905106)
    SkipLinesIfFlagEnabled(15, 92905105)
    SkipLinesIfFlagEnabled(12, 92905104)
    SkipLinesIfFlagEnabled(9, 92905103)
    SkipLinesIfFlagEnabled(6, 92905102)
    SkipLinesIfFlagEnabled(3, 92905101)
    SkipLinesIfFlagEnabled(0, 92905100)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6120,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6121,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6122,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6123,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6124,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6125,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6126,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=obj__source_entity,
        model_point=100,
        behavior_id=6127,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- 2 --- #
    DefineLabel(2)
    IfTimeElapsed(1, seconds=0.5)
    IfObjectHealthValueComparison(2, obj__source_entity, ComparisonType.LessThan, value=999)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionFalse(input_condition=2)

    # --- 3 --- #
    DefineLabel(3)
    DeleteObjectVFX(obj__source_entity)
    IfFramesElapsed(0, frames=1)
    DestroyObject(obj__source_entity)


@RestartOnRest(12906726)
def Event_12906726(_, character: int, sound_id: int, radius: float):
    """Event 12906726"""
    IfCharacterBackreadEnabled(0, character)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(character, sound_id, sound_type=SoundType.c_CharacterMotion)
    IfCharacterDead(-1, character)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=radius)
    IfFramesElapsed(-2, frames=120)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=-1)
    Restart()


@RestartOnRest(12906738)
def Event_12906738(_, character: int):
    """Event 12906738"""
    SkipLinesIfFlagDisabled(1, 1431)
    End()
    IfCharacterDead(0, character)
    DisableFlagRange((1420, 1437))
    EnableFlag(1431)


@RestartOnRest(12906740)
def Event_12906740(_, character: int, flag: int):
    """Event 12906740"""
    EndIfFlagRangeAnyEnabled(flag_range=(1431, 1432))
    IfHealthLessThan(1, character, value=0.8999999761581421)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1432)


@RestartOnRest(12906742)
def Event_12906742(_, character: int):
    """Event 12906742"""
    SetTeamType(character, TeamType.FriendlyNPC)
    IfFlagEnabled(0, 1432)
    SetTeamType(character, TeamType.HostileNPC)


@RestartOnRest(12906744)
def Event_12906744(_, attacked_entity: int, flag: int):
    """Event 12906744"""
    IfAttacked(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttacked(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttacked(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    EnableFlag(flag)


@NeverRestart(12906746)
def Event_12906746(_, character: int):
    """Event 12906746"""
    ForceAnimation(character, 7015, loop=True, wait_for_completion=True, skip_transition=True)
    DisableFlag(72900001)
    IfFlagEnabled(-1, 72900001)
    IfFlagEnabled(-1, 1432)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(character, 151, affect_npc_part_hp=True)


@NeverRestart(12906748)
def Event_12906748(_, character: int):
    """Event 12906748"""
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHasSpecialEffect(1, character, 5543)
    IfHealthGreaterThan(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 7021, wait_for_completion=True)


@RestartOnRest(12906750)
def Event_12906750(_, character: int, character_1: int, model_point: int):
    """Event 12906750"""
    DisableNetworkSync()
    IfCharacterAlive(1, character)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        short_move=True,
    )
    Restart()


@RestartOnRest(12906764)
def Event_12906764(
    _,
    character: int,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12906764"""
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        body_damage_correction=2.0,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=2.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id_1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(character, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12906765)
def Event_12906765(
    _,
    character: int,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12906765"""
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    AddSpecialEffect(character, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id_1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=100)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(character, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906766)
def Event_12906766(_, character: int, flag: int, flag_1: int):
    """Event 12906766"""
    EndIfFlagEnabled(flag)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(0, character, value=0.699999988079071)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag_1)


@NeverRestart(12906767)
def Event_12906767(_, character: int, flag: int, flag_1: int):
    """Event 12906767"""
    EndIfFlagEnabled(flag)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(1, character, value=0.30000001192092896)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12906768)
def Event_12906768(
    _,
    character: int,
    flag: int,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12906768"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(0, character, 5402)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)


@NeverRestart(12906769)
def Event_12906769(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906769"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906770)
def Event_12906770(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906770"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906771)
def Event_12906771(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906771"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906772)
def Event_12906772(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906772"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906773)
def Event_12906773(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906773"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906774)
def Event_12906774(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906774"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906775)
def Event_12906775(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906775"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906776)
def Event_12906776(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906776"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906777)
def Event_12906777(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906777"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906778)
def Event_12906778(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906778"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906779)
def Event_12906779(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906779"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906780)
def Event_12906780(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906780"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906781)
def Event_12906781(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906781"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906782)
def Event_12906782(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906782"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906783)
def Event_12906783(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906783"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906784)
def Event_12906784(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906784"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906785)
def Event_12906785(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906785"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906786)
def Event_12906786(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906786"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906787)
def Event_12906787(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906787"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906788)
def Event_12906788(
    _,
    character: int,
    source_flag: int,
    flag: int,
    flag_1: int,
    part_index: short,
    npc_part_id: int,
    npc_part_id_1: short,
    desired_health__part_health: int,
):
    """Event 12906788"""
    IfFlagEnabled(1, flag_1)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id_1, part_index=part_index, part_health=desired_health__part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id_1,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=3,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Add,
    )
    EnableFlag(flag)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(
        character,
        npc_part_id=npc_part_id,
        desired_health=desired_health__part_health,
        overwrite_max=True,
    )
    EventValueOperation(
        source_flag=source_flag,
        source_flag_bit_count=10,
        operand=2,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )
    EnableFlag(flag)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906827)
def Event_12906827(
    _,
    character: int,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    animation_id: int,
    special_effect_id: int,
):
    """Event 12906827"""
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=100)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    AddSpecialEffect(character, special_effect_id)
    ReplanAI(character)
    Wait(30.0)
    CancelSpecialEffect(character, special_effect_id)
    ReplanAI(character)
    Restart()


@NeverRestart(12906828)
def Event_12906828(
    _,
    character: int,
    part_index: short,
    npc_part_id: short,
    npc_part_id_1: int,
    animation_id: int,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12906828"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(character, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=2, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=3, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=4, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=9, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=11, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=12, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=100,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    AddSpecialEffect(character, 5667, affect_npc_part_hp=True)
    ReplanAI(character)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetDisplayMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)


@NeverRestart(12906789)
def Event_12906789(
    _,
    region: int,
    obj: int,
    obj_1: int,
    vfx_id: int,
    vfx_id_1: int,
    flag: int,
    flag_1: int,
    flag_2: int,
):
    """Event 12906789"""
    EndIfFlagEnabled(flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    SkipLinesIfClient(2)
    DisableObject(obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    DisableObject(obj_1)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableObject(obj)
    EnableObject(obj_1)
    CreateVFX(vfx_id)
    CreateVFX(vfx_id_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=obj)
    IfFlagEnabled(3, flag)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, region, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, seconds=4.0)
    IfCharacterHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    EnableFlag(flag_2)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


@NeverRestart(12906790)
def Event_12906790(_, region: int, entity: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12906790"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, region, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(2, input_condition=-1)
    IfTimeElapsed(3, seconds=4.0)
    IfCharacterWhitePhantom(3, PLAYER)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EnableFlag(flag_3)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(12906791)
def Event_12906791(_, character: int, name: int, left: int, flag: int, flag_1: int):
    """Event 12906791"""
    EndIfFlagEnabled(left)
    DisableAI(character)
    DisableHealthBar(character)
    EnableInvincibility(character)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, flag)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(character)
    DisableInvincibility(character)
    EnableBossHealthBar(character, name=name)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(flag_1)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)


@NeverRestart(12906792)
def Event_12906792(_, character: int, region: int, sound_id: int, sound_id_1: int, flag: int, flag_1: int, flag_2: int):
    """Event 12906792"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, flag_2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=sound_id)
    IfCharacterHasTAEEvent(2, character, tae_event_id=500)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(2, flag_1)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, flag_2)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=sound_id)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=sound_id_1)


@NeverRestart(12906794)
def Event_12906794(_, character: int, flag: int, radius: float, radius_1: float):
    """Event 12906794"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, character, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=character, radius=radius_1)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12906795)
def Event_12906795(_, character: int, name: int, left: int, flag: int, flag_1: int, character_1: int, character_2: int):
    """Event 12906795"""
    EndIfFlagEnabled(left)
    DisableAI(character)
    DisableAI(character_1)
    DisableAI(character_2)
    DisableHealthBar(character)
    DisableHealthBar(character_1)
    DisableHealthBar(character_2)
    EnableInvincibility(character)
    EnableInvincibility(character_1)
    EnableInvincibility(character_2)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, flag)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(character_1, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(character_2, authority_level=UpdateAuthority.Forced)
    DisableFlag(12907230)
    DisableFlag(12907231)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(character_1, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(character_2, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(character_1, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(character_2, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(character)
    EnableAI(character_1)
    EnableAI(character_2)
    DisableInvincibility(character)
    DisableInvincibility(character_1)
    DisableInvincibility(character_2)
    EnableBossHealthBar(character, name=name)
    EnableBossHealthBar(character_1, name=304002, bar_slot=1)
    EnableBossHealthBar(character_2, name=304003, bar_slot=2)
    EnableFlag(flag_1)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)


@NeverRestart(12906796)
def Event_12906796(
    _,
    region: int,
    obj: int,
    obj_1: int,
    vfx_id: int,
    vfx_id_1: int,
    flag: int,
    flag_1: int,
    flag_2: int,
):
    """Event 12906796"""
    EndIfFlagEnabled(flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    SkipLinesIfClient(2)
    DisableObject(obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    DisableObject(obj_1)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableObject(obj)
    EnableObject(obj_1)
    CreateVFX(vfx_id)
    CreateVFX(vfx_id_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=obj)
    IfFlagEnabled(3, flag)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, region, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, seconds=4.0)
    IfCharacterHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    EnableFlag(flag_2)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


@NeverRestart(12906800)
def Event_12906800(_, region: int, obj: int, vfx_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12906800"""
    EndIfFlagEnabled(flag)
    GotoIfFlagEnabled(Label.L0, flag=flag_1)
    SkipLinesIfClient(2)
    DisableObject(obj)
    DeleteVFX(vfx_id, erase_root_only=False)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableObject(obj)
    CreateVFX(vfx_id)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=obj)
    IfFlagEnabled(3, flag)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, region, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, seconds=4.0)
    IfCharacterHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    EnableFlag(flag_2)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


@NeverRestart(12906802)
def Event_12906802(_, target_entity: int, entity: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12906802"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=entity)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, target_entity, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2412801)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(2, input_condition=-1)
    IfTimeElapsed(3, seconds=4.0)
    IfCharacterWhitePhantom(3, PLAYER)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EnableFlag(flag_3)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


@NeverRestart(12906806)
def Event_12906806(_, character: int, name: int, left: int, flag: int, flag_1: int):
    """Event 12906806"""
    EndIfFlagEnabled(left)
    DisableAI(character)
    DisableHealthBar(character)
    EnableInvincibility(character)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, flag)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    DisableFlag(12907230)
    DisableFlag(12907231)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(character, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(character)
    DisableInvincibility(character)
    EnableBossHealthBar(character, name=name)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(flag_1)
    CreatePlayLog(name=1260)
    SkipLinesIfNotEqual(1, left=left, right=12901800)
    StartPlayLogMeasurement(measurement_id=2900010, name=1316, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901801)
    StartPlayLogMeasurement(measurement_id=2900011, name=1352, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901802)
    StartPlayLogMeasurement(measurement_id=2900012, name=1388, overwrite=True)
    SkipLinesIfNotEqual(1, left=left, right=12901803)
    StartPlayLogMeasurement(measurement_id=2900013, name=1424, overwrite=True)


@NeverRestart(12906810)
def Event_12906810(_, character: int, region: int, sound_id: int, sound_id_1: int, flag: int, flag_1: int, flag_2: int):
    """Event 12906810"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, flag)
    IfFlagEnabled(1, flag_1)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, flag_2)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=sound_id)
    IfCharacterHasTAEEvent(2, character, tae_event_id=500)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag)
    IfFlagEnabled(2, flag_1)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, flag_2)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=sound_id)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=sound_id_1)


@NeverRestart(12906978)
def Event_12906978(_, flag: int, region: int, sound_id: int, sound_id_1: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12906978"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)
    EndIfFlagEnabled(flag_1)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, flag_3)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=sound_id)
    IfFlagEnabled(2, flag)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, flag_1)
    IfFlagEnabled(2, flag_2)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, flag_3)
    IfCharacterInsideRegion(2, PLAYER, region=region)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=sound_id)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=sound_id_1)


@NeverRestart(12906818)
def Event_12906818(_, character: int, flag: int, radius: float, radius_1: float):
    """Event 12906818"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, character, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=character, radius=radius_1)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12906822)
def Event_12906822(_, character: int, flag: int, radius: float, radius_1: float, character_1: int, character_2: int):
    """Event 12906822"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfHealthGreaterThan(2, character_1, value=0.0)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character_1, radius=radius)
    IfHealthGreaterThan(3, character_2, value=0.0)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=character_2, radius=radius)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(4, character, value=0.0)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=character, radius=radius_1)
    IfHealthGreaterThan(5, character_1, value=0.0)
    IfEntityWithinDistance(5, entity=PLAYER, other_entity=character_1, radius=radius_1)
    IfHealthGreaterThan(6, character_2, value=0.0)
    IfEntityWithinDistance(6, entity=PLAYER, other_entity=character_2, radius=radius_1)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionFalse(0, input_condition=-2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12906823)
def Event_12906823(_, character: int, flag: int, radius: float, radius_1: float, character_1: int, flag_1: int):
    """Event 12906823"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfHealthGreaterThan(1, character, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=radius)
    IfHealthGreaterThan(2, character_1, value=0.0)
    IfFlagEnabled(2, flag_1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character_1, radius=radius)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(3, character, value=0.0)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=character, radius=radius_1)
    IfHealthGreaterThan(4, character_1, value=0.0)
    IfFlagEnabled(4, flag_1)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=character_1, radius=radius_1)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionFalse(0, input_condition=-2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


@NeverRestart(12906824)
def Event_12906824(_, flag: int, flag_1: int):
    """Event 12906824"""
    IfFlagEnabled(0, flag)
    EnableFlag(flag_1)


@NeverRestart(12906825)
def Event_12906825(
    _,
    character: int,
    character_1: int,
    flag: int,
    destination: int,
    name: int,
    value: float,
    flag_1: int,
    flag_2: int,
):
    """Event 12906825"""
    GotoIfFlagDisabled(Label.L0, flag=flag_2)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    DisableCharacter(character)
    IfFlagEnabled(1, flag)
    IfHealthLessThanOrEqual(1, character_1, value=value)
    IfConditionTrue(0, input_condition=1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    CreateTemporaryVFX(vfx_id=929203, anchor_entity=character, model_point=6, anchor_type=CoordEntityType.Character)

    # --- 1 --- #
    DefineLabel(1)
    EnableBossHealthBar(character, name=name, bar_slot=1)
    EnableFlag(flag_1)


@NeverRestart(12906841)
def Event_12906841(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906841"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=400,
        body_damage_correction=0.75,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=2.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906843)
def Event_12906843(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906843"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=80)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906845)
def Event_12906845(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906845"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=80)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906847)
def Event_12906847(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906847"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=280)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.149999976158142,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906849)
def Event_12906849(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906849"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=280)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.149999976158142,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906851)
def Event_12906851(_, character: int, flag: int):
    """Event 12906851"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    EndIfFlagDisabled(flag)
    IfCharacterBackreadEnabled(0, character)
    ForceAnimation(character, 7020, loop=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    ForceAnimation(character, 7021)


@NeverRestart(12906853)
def Event_12906853(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906853"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=100)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906855)
def Event_12906855(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906855"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.2000000476837158,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906857)
def Event_12906857(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906857"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=150)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.2000000476837158,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906859)
def Event_12906859(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906859"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.149999976158142,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906861)
def Event_12906861(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906861"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.149999976158142,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906831)
def Event_12906831(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906831"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906833)
def Event_12906833(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906833"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906835)
def Event_12906835(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906835"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906837)
def Event_12906837(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906837"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906839)
def Event_12906839(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906839"""
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906793)
def Event_12906793(_, flag: int, sound_id: int, sound_id_1: int):
    """Event 12906793"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12906814)
def Event_12906814(_, flag: int, sound_id: int, sound_id_1: int):
    """Event 12906814"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    DisableBossMusic(sound_id=sound_id)
    DisableBossMusic(sound_id=sound_id_1)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12906869)
def Event_12906869(_, character: int, flag: int):
    """Event 12906869"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(2, character, value=0.699999988079071)
    IfHealthNotEqual(2, character, value=0.0)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag)


@NeverRestart(12906870)
def Event_12906870(_, character: int, flag: int):
    """Event 12906870"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(2, character, value=0.33000001311302185)
    IfHealthNotEqual(2, character, value=0.0)
    IfFlagEnabled(2, flag)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12906865)
def Event_12906865(
    _,
    character: int,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12906865"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    IfCharacterHasSpecialEffect(0, character, 5402)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)


@NeverRestart(12906871)
def Event_12906871(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906871"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=300,
        body_damage_correction=1.399999976158142,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=2.0999999046325684,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906879)
def Event_12906879(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906879"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=400,
        body_damage_correction=0.20000000298023224,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=0.30000001192092896,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 488, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 498)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 498, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 488)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906872)
def Event_12906872(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906872"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 485, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 495)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 495, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 485)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906875)
def Event_12906875(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906875"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=230)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906873)
def Event_12906873(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906873"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part6, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part6,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 486, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 496)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 496, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 486)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906876)
def Event_12906876(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906876"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part7, part_health=170)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part7,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906874)
def Event_12906874(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906874"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part8, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part8,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 487, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 497)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 497, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 487)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906877)
def Event_12906877(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906877"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part9, part_health=170)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part9,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906878)
def Event_12906878(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906878"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part10, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part10,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906880)
def Event_12906880(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906880"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part11,
        part_health=150,
        body_damage_correction=0.20000000298023224,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part11,
        part_health=9999999,
        body_damage_correction=0.30000001192092896,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 488, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 498)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 498, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 488)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@NeverRestart(12906881)
def Event_12906881(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12906881"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part12,
        part_health=150,
        body_damage_correction=0.20000000298023224,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part12,
        part_health=9999999,
        body_damage_correction=0.30000001192092896,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 488, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 498)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=100, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    AddSpecialEffect(character, 498, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 488)
    AICommand(character, command_id=-1, command_slot=1)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12904889)
def Event_12904889(_, character: int):
    """Event 12904889"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    AICommand(character, command_id=2, command_slot=1)
    IfHealthLessThan(2, character, value=0.6700000166893005)
    IfCharacterHasSpecialEffect(2, character, 5402)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    AICommand(character, command_id=100, command_slot=2)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)
    AICommand(character, command_id=-1, command_slot=2)
    ReplanAI(character)
    Wait(0.10000000149011612)
    AICommand(character, command_id=3, command_slot=1)


@RestartOnRest(12904723)
def Event_12904723(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904723"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=180)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8000)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=130, overwrite_max=True)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@RestartOnRest(12904724)
def Event_12904724(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904724"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8010)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=150, overwrite_max=True)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@RestartOnRest(12904725)
def Event_12904725(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904725"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=200)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8030)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=150, overwrite_max=True)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@RestartOnRest(12904726)
def Event_12904726(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904726"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=250)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8020)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=200, overwrite_max=True)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@RestartOnRest(12904727)
def Event_12904727(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904727"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part5, part_health=250)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(character, bit_count=10, state_id=2)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 8040)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=200, overwrite_max=True)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    ChangeCharacterCloth(character, bit_count=10, state_id=1)
    Restart()


@NeverRestart(12906882)
def Event_12906882(_, character: int, character_1: int, flag: int):
    """Event 12906882"""
    EndIfFlagEnabled(flag)
    DisableAI(character)
    DisableGravity(character)
    AddSpecialEffect(character, 5401)
    WaitFrames(frames=1)
    IfCharacterDead(1, character_1)
    EndIfConditionTrue(1)
    IfFlagEnabled(2, flag)
    IfRandomTimeElapsed(-1, min_seconds=0.0, max_seconds=1.0)
    IfTimeElapsed(3, seconds=1.0)
    IfCharacterWhitePhantom(3, PLAYER)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    EnableGravity(character)
    ForceAnimation(character, 7000)
    WaitFrames(frames=64)
    EnableAI(character)


@NeverRestart(12906863)
def Event_12906863(_, character: int, destination: int, destination_1: int, flag: int, flag_1: int):
    """Event 12906863"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHealthLessThanOrEqual(2, character, value=0.75)
    IfHealthNotEqual(2, character, value=0.0)
    IfConditionTrue(0, input_condition=2)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(3, character, tae_event_id=10)
    IfHealthNotEqual(3, character, value=0.0)
    IfConditionTrue(0, input_condition=3)
    DisableCharacter(character)
    Wait(2.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ForceAnimation(character, 3021)
    AICommand(character, command_id=101, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag)
    IfHealthLessThanOrEqual(4, character, value=0.5)
    IfHealthNotEqual(4, character, value=0.0)
    IfConditionTrue(0, input_condition=4)
    AICommand(character, command_id=110, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(5, character, tae_event_id=10)
    IfHealthNotEqual(5, character, value=0.0)
    IfConditionTrue(0, input_condition=5)
    DisableCharacter(character)
    Wait(2.0)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ForceAnimation(character, 3021)
    AICommand(character, command_id=111, command_slot=0)
    ReplanAI(character)
    EnableFlag(flag_1)


@NeverRestart(12906912)
def Event_12906912(_, character: int, character_1: int, flag: int):
    """Event 12906912"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableCharacter(character_1)
    Kill(character_1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, character)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Kill(character_1)


@NeverRestart(12906864)
def Event_12906864(_, character: int):
    """Event 12906864"""
    CreateNPCPart(character, npc_part_id=2, part_index=NPCPartType.Part2, part_health=250)
    SetNPCPartEffects(character, npc_part_id=2, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfCharacterHasTAEEvent(3, character, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, 7000)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(5, character, value=0.0)
    IfCharacterHasTAEEvent(6, character, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(character)
    ForceAnimation(character, 7001)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, character, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(8, character, value=0.0)
    IfCharacterHasTAEEvent(9, character, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(character)
    ForceAnimation(character, 7002)
    CreateNPCPart(
        character,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=2, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(character)
    IfTimeElapsed(0, seconds=30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(character, npc_part_id=2, desired_health=-1, overwrite_max=True)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12906867)
def Event_12906867(_, character: int):
    """Event 12906867"""
    CreateNPCPart(character, npc_part_id=3, part_index=NPCPartType.Part3, part_health=250)
    SetNPCPartEffects(character, npc_part_id=3, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfCharacterHasTAEEvent(3, character, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(character)
    ForceAnimation(character, 7005)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(5, character, value=0.0)
    IfCharacterHasTAEEvent(6, character, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(character)
    ForceAnimation(character, 7006)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, character, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, character, value=0.0)
    IfCharacterHasTAEEvent(9, character, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(character)
    ForceAnimation(character, 7007)
    CreateNPCPart(
        character,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.2999999523162842,
    )
    SetNPCPartEffects(character, npc_part_id=3, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(character)
    IfTimeElapsed(0, seconds=30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(character, npc_part_id=3, desired_health=-1, overwrite_max=True)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()
    Restart()


@NeverRestart(12906868)
def Event_12906868(_, character: int):
    """Event 12906868"""
    EndIfFlagEnabled(13201800)
    CreateNPCPart(
        character,
        npc_part_id=1,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=0.5,
        body_damage_correction=0.5,
    )
    SetNPCPartEffects(character, npc_part_id=1, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=1, value=0)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    Restart()


@RestartOnRest(12906829)
def Event_12906829(_, character: int, character_1: int, model_point: int, flag: int):
    """Event 12906829"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, character)
    DisableGravity(character_1)

    # --- 0 --- #
    DefineLabel(0)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character,
    )
    Restart()


@RestartOnRest(12904873)
def Event_12904873(_, character: int, character_1: int, flag: int):
    """Event 12904873"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    IfCharacterDead(0, character)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)


@RestartOnRest(12904875)
def Event_12904875(_, character: int, entity: int, flag: int):
    """Event 12904875"""
    EndIfFlagEnabled(flag)
    IfHealthLessThanOrEqual(0, character, value=0.5)
    ForceAnimation(entity, 3000)


@RestartOnRest(12904884)
def Event_12904884(_, character: int):
    """Event 12904884"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHealthLessThan(0, character, value=0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 7010)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    IfHealthLessThan(0, character, value=0.33000001311302185)
    Wait(0.10000000149011612)
    ResetAnimation(character, disable_interpolation=True)
    ForceAnimation(character, 7011)
    AICommand(character, command_id=101, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=20)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12904734)
def Event_12904734(_, character__source_entity: int):
    """Event 12904734"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character__source_entity)
    EndIfConditionTrue(1)
    IfCharacterHasSpecialEffect(2, character__source_entity, 5650)
    IfHealthValueLessThan(2, character__source_entity, value=0)
    IfConditionTrue(0, input_condition=2)
    ShootProjectile(
        owner_entity=2900000,
        source_entity=character__source_entity,
        model_point=6,
        behavior_id=225100310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    Restart()


@NeverRestart(12904735)
def Event_12904735(_, character: int):
    """Event 12904735"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHealthLessThan(0, character, value=0.5)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12904728)
def Event_12904728(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904728"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=400,
        body_damage_correction=2.0,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        body_damage_correction=2.5,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 480, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 490)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AddSpecialEffect(character, 490, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 480)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12904729)
def Event_12904729(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904729"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part1, part_health=250)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 481, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 491)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AddSpecialEffect(character, 491, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 481)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12904730)
def Event_12904730(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904730"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part2, part_health=250)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 482, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 492)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AddSpecialEffect(character, 492, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 482)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12904731)
def Event_12904731(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904731"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part3, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 483, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 493)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AddSpecialEffect(character, 493, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 483)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12904732)
def Event_12904732(_, character: int, npc_part_id: short, npc_part_id_1: int):
    """Event 12904732"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=NPCPartType.Part4, part_health=300)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, character, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, character, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        character,
        npc_part_id=npc_part_id,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        body_damage_correction=1.25,
    )
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(character, 484, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 494)
    ReplanAI(character)
    ResetAnimation(character)
    ForceAnimation(character, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(character, command_id=1, command_slot=0)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=500)
    AddSpecialEffect(character, 494, affect_npc_part_hp=True)
    CancelSpecialEffect(character, 484)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=False)
    WaitFrames(frames=15)
    Restart()


@RestartOnRest(12906942)
def Event_12906942(_, character: int, destination: int, flag: int, flag_1: int, flag_2: int, character_1: int):
    """Event 12906942"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character_1)
    EndIfConditionTrue(1)
    IfCharacterHasTAEEvent(2, character_1, tae_event_id=90)
    IfFlagEnabled(2, flag_2)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(character, 5610)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(character)
    ReplanAI(character)
    ForceAnimation(character, 3021, wait_for_completion=True)
    DisableFlag(flag)
    EnableFlag(flag_1)
    IfFlagEnabled(0, flag)
    Restart()


@RestartOnRest(12906960)
def Event_12906960(_, character: int, flag: int, flag_1: int, character_1: int):
    """Event 12906960"""
    WaitFrames(frames=1)
    IfCharacterDead(1, character_1)
    EndIfConditionTrue(1)
    IfAttacked(-2, attacked_entity=character, attacker=PLAYER)
    IfAttacked(-2, attacked_entity=character, attacker=2900248)
    IfAttacked(-2, attacked_entity=character, attacker=2900249)
    IfAttacked(-2, attacked_entity=character, attacker=2900250)
    IfCharacterHasTAEEvent(3, character_1, tae_event_id=80)
    IfFlagEnabled(3, flag_1)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=-2)
    WaitFrames(frames=1)
    ForceAnimation(character, 3020)
    WaitFrames(frames=65)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 3020)
    WaitFrames(frames=65)

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableFlag(flag_1)
    EnableFlag(flag)
    Restart()


@NeverRestart(12907000)
def Event_12907000(_, character: int, obj: int, flag: int, flag_1: int):
    """Event 12907000"""
    DisableNetworkSync()
    IfCharacterBackreadEnabled(0, character)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    DisableObject(obj)
    IfFlagEnabled(0, flag)
    EnableObject(obj)
    EnableCharacter(character)
    CreateTemporaryVFX(vfx_id=100330, anchor_entity=obj, model_point=100, anchor_type=CoordEntityType.Object)

    # --- 0 --- #
    DefineLabel(0)
    RegisterLantern(flag=flag_1, obj=obj, reaction_distance=0.0, reaction_angle=0.0)


@NeverRestart(12907010)
def Event_12907010(_, flag: int, warp_object_id: int):
    """Event 12907010"""
    EndIfFlagEnabled(flag)
    IfFlagEnabled(0, flag)
    RotateToFaceEntity(PLAYER, warp_object_id, animation=101170)
    WaitFrames(frames=32)
    InitializeWarpObject(warp_object_id=warp_object_id)


@NeverRestart(12907020)
def Event_12907020(_, flag: int, anchor_entity: int):
    """Event 12907020"""
    EndIfClient()
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    RotateToFaceEntity(PLAYER, anchor_entity, animation=101160)
    Wait(1.0)
    CreateTemporaryVFX(vfx_id=100320, anchor_entity=anchor_entity, model_point=100, anchor_type=CoordEntityType.Object)
    Wait(3.0)
    SkipLinesIfFlagDisabled(2, 9020)
    WarpPlayerToRespawnPoint(2102954)
    End()
    SkipLinesIfFlagDisabled(2, 9021)
    WarpPlayerToRespawnPoint(2102955)
    End()
    SkipLinesIfFlagDisabled(2, 9022)
    WarpPlayerToRespawnPoint(2102956)
    End()
    SkipLinesIfFlagDisabled(2, 9023)
    WarpPlayerToRespawnPoint(2102957)
    End()
    SkipLinesIfFlagDisabled(2, 9024)
    WarpPlayerToRespawnPoint(2102958)
    End()
    SkipLinesIfFlagDisabled(2, 9025)
    WarpPlayerToRespawnPoint(2102959)
    End()
    SkipLinesIfFlagDisabled(2, 9026)
    WarpPlayerToRespawnPoint(2102960)
    End()
    WarpPlayerToRespawnPoint(2102954)


@NeverRestart(12907030)
def Event_12907030(_, flag: int, warp_object_id: int):
    """Event 12907030"""
    EndIfClient()
    IfFlagEnabled(0, flag)
    WaitFrames(frames=1)
    CreateTemporaryVFX(
        vfx_id=100321,
        anchor_entity=warp_object_id,
        model_point=100,
        anchor_type=CoordEntityType.Object,
    )
    InitializeWarpObject(warp_object_id=warp_object_id)
    DisableFlag(flag)


@NeverRestart(12907300)
def Event_12907300(_, item: int, flag: int):
    """Event 12907300"""
    IfPlayerHasGood(0, item)
    EnableFlag(flag)


@NeverRestart(12907400)
def Event_12907400():
    """Event 12907400"""
    IfFlagEnabled(1, 12907230)
    IfFlagEnabled(1, 12907231)
    IfClientTypeCountComparison(1, client_type=ClientType.Invader, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagEnabled(-1, 12907230)
    IfFlagEnabled(-1, 12907231)
    IfClientTypeCountComparison(2, client_type=ClientType.Invader, comparison_type=ComparisonType.LessThan, value=1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    AwaitConditionTrue(-2)
    IfTimeElapsed(7, seconds=10.0)
    IfCharacterHuman(7, PLAYER)
    IfConditionTrue(0, input_condition=7)
    AddSpecialEffect(PLAYER, 9020)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    IfFlagDisabled(3, 12907230)
    IfFlagDisabled(3, 12907231)
    IfFlagEnabled(4, 12907230)
    IfFlagDisabled(4, 12907231)
    IfClientTypeCountComparison(
        4,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfFlagDisabled(5, 12907230)
    IfFlagEnabled(5, 12907231)
    IfClientTypeCountComparison(
        5,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfFlagEnabled(6, 12907230)
    IfFlagEnabled(6, 12907231)
    IfClientTypeCountComparison(
        6,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=2,
    )
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(-3, input_condition=6)
    AwaitConditionTrue(-3)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    Restart()


@NeverRestart(12907401)
def Event_12907401(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12907401"""
    GotoIfFlagEnabled(Label.L0, flag=92905340)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(flag)
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    IfOnline(1)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    SkipLinesIfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(
        2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagEnabled(1, flag_4)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, seconds=10.0)
    SkipLinesIfFlagDisabled(1, flag_3)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    IfFramesElapsed(0, frames=59)
    EnableAI(character)
    EnableFlag(flag)
    EnableFlag(12907230)


@NeverRestart(12907405)
def Event_12907405(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int):
    """Event 12907405"""
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    DisableAI(character)
    ForceAnimation(character, 7010)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(flag)
    DisableAI(character)
    ForceAnimation(character, 7010, loop=True)
    IfOnline(1)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, value=30)
    IfFlagDisabled(4, flag_3)
    IfFlagEnabled(4, flag_5)
    SkipLinesIfConditionTrue(1, 4)
    IfClientTypeCountComparison(
        2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.GreaterThanOrEqual,
        value=1,
    )
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagEnabled(1, flag_4)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, seconds=10.0)
    SkipLinesIfFinishedConditionTrue(1, condition=4)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(character, 7011)
    IfFramesElapsed(0, frames=59)
    EnableAI(character)
    EnableFlag(flag)
    EnableFlag(12907231)


@NeverRestart(12907409)
def Event_12907409(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12907409"""
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(3, flag_2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    DisableFlag(12907230)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    EnableFlag(flag_3)
    EndIfFlagEnabled(12907231)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@NeverRestart(12907413)
def Event_12907413(_, character: int, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12907413"""
    IfFlagEnabled(-15, flag_1)
    IfFlagEnabled(-15, flag_2)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, flag)
    IfHealthEqual(2, character, value=0.0)
    IfFlagEnabled(3, flag_2)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag_1)
    DisableFlag(12907231)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    EnableFlag(flag_3)
    EndIfFlagEnabled(12907230)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    ForceAnimation(character, 7012)
    WaitFrames(frames=88)
    ForceAnimation(character, 7010)


@NeverRestart(12907440)
def Event_12907440(_, character: int, flag: int, flag_1: int):
    """Event 12907440"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(0, PLAYER, 9020)
    AddSpecialEffect(character, 9100)
    ReplanAI(character)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 9020)
    IfFlagEnabled(-1, flag_1)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(character, 9100)
    ReplanAI(character)
    Restart()


@NeverRestart(12907420)
def Event_12907420(_, special_effect_id: int, flag: int, special_effect_id_1: int, special_effect_id_2: int):
    """Event 12907420"""
    EndIfFlagDisabled(flag)
    SkipLinesIfClient(2)
    AddSpecialEffect(PLAYER, special_effect_id)
    End()
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfCharacterWhitePhantom(1, PLAYER)
    SkipLinesIfConditionTrue(2, 1)
    AddSpecialEffect(PLAYER, special_effect_id_1)
    End()
    AddSpecialEffect(PLAYER, special_effect_id_2)


@NeverRestart(12907430)
def Event_12907430(_, region: int, flag: int):
    """Event 12907430"""
    DisableFlag(flag)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    EnableFlag(flag)
    IfCharacterOutsideRegion(2, PLAYER, region=region)
    IfHost(2)
    IfConditionTrue(0, input_condition=2)
    Restart()


@NeverRestart(12907600)
def Event_12907600(_, obj: int, vfx_id: int):
    """Event 12907600"""
    DisableNetworkSync()
    DisableObject(obj)
    DeleteVFX(vfx_id)
    IfConnectingMultiplayer(-1)
    IfMultiplayer(-1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(obj)
    CreateVFX(vfx_id)
    IfConnectingMultiplayer(-2)
    IfMultiplayer(-2)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@RestartOnRest(12906962)
def Event_12906962(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12906962"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagEnabled(4, 12906992)
    IfFlagDisabled(4, 12906988)
    IfFlagEnabled(5, 12906993)
    IfFlagDisabled(5, 12906989)
    IfFlagEnabled(6, 12906994)
    IfFlagDisabled(6, 12906990)
    IfFlagEnabled(7, 12906995)
    IfFlagDisabled(7, 12906991)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionFalse(-1, input_condition=-2)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagEnabled(8, 12906992)
    IfFlagDisabled(8, 12906988)
    IfFlagEnabled(9, 12906993)
    IfFlagDisabled(9, 12906989)
    IfFlagEnabled(10, 12906994)
    IfFlagDisabled(10, 12906990)
    IfFlagEnabled(11, 12906995)
    IfFlagDisabled(11, 12906991)
    IfConditionTrue(-4, input_condition=8)
    IfConditionTrue(-4, input_condition=9)
    IfConditionTrue(-4, input_condition=10)
    IfConditionTrue(-4, input_condition=11)
    IfConditionFalse(-3, input_condition=-4)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12906966)
def Event_12906966(
    _,
    sign_type: int,
    character: int,
    region: int,
    summon_flag: int,
    dismissal_flag: int,
    action_button_id: int,
    flag: int,
    flag_1: int,
):
    """Event 12906966"""
    SkipLinesIfFlagEnabled(1, summon_flag)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    IfClient(1)
    IfFlagEnabled(1, summon_flag)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(character)
    EndIfFlagEnabled(flag)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, summon_flag)
    IfFlagDisabled(2, dismissal_flag)
    IfFlagState(2, FlagState.On, FlagType.RelativeToThisEventSlot, 14)
    IfFlagDisabled(2, flag)
    IfActionButtonParamActivated(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    EnableFlag(flag_1)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest(12906970)
def Event_12906970(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12906970"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12906974)
def Event_12906974(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12906974"""
    EndIfClient()
    EnableGravity(character)
    EnableCharacterCollision(character)
    IfFlagEnabled(1, flag)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    DisableGravity(character)
    DisableCharacterCollision(character)
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    IfCharacterInsideRegion(2, character, region=region_2)
    RestartIfConditionFalse(2)
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(0, character, region=region_3)
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12907610)
def Event_12907610(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 12907610"""
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(character, 35)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12907620)
def Event_12907620(_, flag: int, flag_1: int):
    """Event 12907620"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(flag)
    EnableFlag(flag_1)


@RestartOnRest(12907625)
def Event_12907625(_, flag: int, flag_1: int, character: int):
    """Event 12907625"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(flag)
    EnableFlag(flag_1)
    WaitFrames(frames=15)
    EnableCharacter(character)


@RestartOnRest(12907630)
def Event_12907630(_, flag: int, flag_1: int, character: int, character_1: int, character_2: int):
    """Event 12907630"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(flag)
    EnableFlag(flag_1)
    WaitFrames(frames=15)
    EnableCharacter(character)
    WaitFrames(frames=15)
    WaitFrames(frames=15)
    EnableCharacter(character_1)
    WaitFrames(frames=15)
    WaitFrames(frames=15)
    EnableCharacter(character_2)
