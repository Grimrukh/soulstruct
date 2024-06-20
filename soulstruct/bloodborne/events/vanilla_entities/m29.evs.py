"""CHALICE DUNGEONS

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


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfClient(1)
    AddSpecialEffect(PLAYER, 9920, affect_npc_part_hp=False)
    SkipLinesIfHost(1)
    DisableFlagRange((12906660, 12906725))
    Event12901685()
    RunEvent(12907000, slot=0, args=(2900950, 2901950, 999, 12907800))
    RunEvent(12907000, slot=1, args=(2900951, 2901951, 999, 12907820))
    RunEvent(12907000, slot=2, args=(2900952, 2901952, 12901800, 12907840))
    RunEvent(12907000, slot=3, args=(2900953, 2901953, 999, 12907860))
    RunEvent(12907000, slot=4, args=(2900954, 2901954, 12901801, 12907880))
    RunEvent(12907000, slot=5, args=(2900955, 2901955, 999, 12907900))
    RunEvent(12907000, slot=6, args=(2900956, 2901956, 12901802, 12907920))
    RunEvent(12907000, slot=7, args=(2900957, 2901957, 999, 12907940))
    RunEvent(12907000, slot=8, args=(2900958, 2901958, 12901803, 12907960))
    RunEvent(12907010, slot=0, args=(72900200, 2901950))
    RunEvent(12907010, slot=1, args=(72900201, 2901951))
    RunEvent(12907010, slot=2, args=(72900202, 2901952))
    RunEvent(12907010, slot=3, args=(72900203, 2901953))
    RunEvent(12907010, slot=4, args=(72900204, 2901954))
    RunEvent(12907010, slot=5, args=(72900205, 2901955))
    RunEvent(12907010, slot=6, args=(72900206, 2901956))
    RunEvent(12907010, slot=7, args=(72900207, 2901957))
    RunEvent(12907010, slot=8, args=(72900208, 2901958))
    RunEvent(12907020, slot=0, args=(72900100, 2901950))
    RunEvent(12907020, slot=1, args=(72900101, 2901951))
    RunEvent(12907020, slot=2, args=(72900102, 2901952))
    RunEvent(12907020, slot=3, args=(72900103, 2901953))
    RunEvent(12907020, slot=4, args=(72900104, 2901954))
    RunEvent(12907020, slot=5, args=(72900105, 2901955))
    RunEvent(12907020, slot=6, args=(72900106, 2901956))
    RunEvent(12907020, slot=7, args=(72900107, 2901957))
    RunEvent(12907020, slot=8, args=(72900108, 2901958))
    RunEvent(12907030, slot=0, args=(72102900, 2901950))
    RunEvent(12907030, slot=1, args=(72102901, 2901951))
    RunEvent(12907030, slot=2, args=(72102902, 2901952))
    RunEvent(12907030, slot=3, args=(72102903, 2901953))
    RunEvent(12907030, slot=4, args=(72102904, 2901954))
    RunEvent(12907030, slot=5, args=(72102905, 2901955))
    RunEvent(12907030, slot=6, args=(72102906, 2901956))
    RunEvent(12907030, slot=7, args=(72102907, 2901957))
    RunEvent(12907030, slot=8, args=(72102908, 2901958))
    RunEvent(12907420, slot=0, args=(4730, 92905370, 4735, 4736))
    RunEvent(12907420, slot=1, args=(4731, 92905371, 4735, 4736))
    RunEvent(12907420, slot=2, args=(4732, 92905372, 4735, 4736))
    DisableFlag(12907230)
    DisableFlag(12907231)
    Event12907400()


def Event12900000(_, arg_0_3: int, arg_4_7: int):
    """ 12900000: Event 12900000 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SkipLinesIfObjectDestroyed(1, arg_0_3)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=arg_4_7)
    IfObjectDestroyed(-1, arg_0_3)
    AwaitConditionTrue(-1)
    WaitFrames(10)
    EnableTreasure(arg_0_3)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)


def Event12900060(_, arg_0_3: int, arg_4_7: int):
    """ 12900060: Event 12900060 """
    SkipLinesIfFlagDisabled(4, 92905335)
    DisableObject(arg_0_3)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    DisableTreasure(arg_0_3)
    End()
    DisableObject(arg_4_7)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    DisableTreasure(arg_4_7)
    End()


def Event12900067(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900067: Event 12900067 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SkipLinesIfObjectDestroyed(1, arg_0_3)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=arg_4_7)
    IfObjectDestroyed(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(10)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    EndIfLastConditionResultTrue(2)
    EnableFlag(arg_8_11)


def Event12900078(_, arg_0_3: int, arg_4_7: int):
    """ 12900078: Event 12900078 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, arg_4_7)
    CreatePlayLog(0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=90,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=90,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=90,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )


def Event12900089(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900089: Event 12900089 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    End()


def Event12900163(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900163: Event 12900163 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    EnableFlag(arg_12_15)
    End()


def Event12900174(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900174: Event 12900174 """
    GotoIfFlagDisabled(Label.L0, arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParamActivated(1, action_button_id=7011, entity=arg_0_3)
    IfObjectActivated(2, obj_act_id=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisplayDialog(
        10010161,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900185(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900185: Event 12900185 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_8_11)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    EnableFlag(arg_12_15)


def Event12900186(_, arg_0_3: int, arg_4_7: int):
    """ 12900186: Event 12900186 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=arg_0_3)
    IfActionButtonParamActivated(2, action_button_id=7011, entity=arg_0_3)
    IfFlagEnabled(3, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    DisplayDialog(
        10010160,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900187(_, arg_0_3: int, arg_4_7: int):
    """ 12900187: Event 12900187 """
    DisableNetworkSync()
    IfFlagEnabled(1, arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010170,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900188(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900188: Event 12900188 """
    EndIfFlagEnabled(arg_12_15)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 1)
    EnableObjectActivation(arg_0_3, obj_act_id=9921)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(arg_0_3, obj_act_id=9921)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    ForceAnimation(arg_0_3, 1)
    Wait(2.5)
    EnableObjectActivation(arg_0_3, obj_act_id=9921)
    Wait(0.5)
    EnableFlag(arg_8_11)


def Event12900189(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900189: Event 12900189 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=9921)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    EnableFlag(arg_8_11)
    Wait(0.0)


def Event12900190(_, arg_0_3: int, arg_4_7: int):
    """ 12900190: Event 12900190 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfFlagDisabled(1, arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010160,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900191(_, arg_0_3: int, arg_4_7: int):
    """ 12900191: Event 12900191 """
    DisableNetworkSync()
    IfFlagEnabled(1, arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010170,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900192(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900192: Event 12900192 """
    SkipLinesIfFlagDisabled(3, arg_4_7)
    DisableObjectActivation(arg_8_11, obj_act_id=2902000)
    CreateObjectVFX(929136, obj=arg_8_11, dummy_id=703)
    End()
    CreateObjectVFX(929134, obj=arg_8_11, dummy_id=703)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    WaitFrames(56)
    EnableFlag(arg_4_7)
    DeleteObjectVFX(arg_8_11, erase_root=True)
    CreateObjectVFX(929136, obj=arg_8_11, dummy_id=703)
    DisplayBanner(BannerType.YouWin)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.v_Voice, sound_id=888880000)
    WaitFrames(44)
    Wait(1.0)
    DisplayBattlefieldMessage(10011260, display_location_index=0)


def Event12900197(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900197: Event 12900197 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=2900100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    EnableFlag(arg_8_11)
    Wait(0.0)


def Event12900202(_, arg_0_3: int, arg_4_7: int):
    """ 12900202: Event 12900202 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfFlagDisabled(1, arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7010, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010167,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900207(_, arg_0_3: int, arg_4_7: int):
    """ 12900207: Event 12900207 """
    DisableNetworkSync()
    IfFlagEnabled(0, arg_4_7)
    Wait(3.0)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=arg_0_3)
    DisplayDialog(
        10010170,
        anchor_entity=arg_0_3,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900229(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900229: Event 12900229 """
    WaitFrames(2)
    SkipLinesIfFlagDisabled(2, arg_8_11)
    CreateObjectVFX(929136, obj=arg_0_3, dummy_id=703)
    End()
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 1)
    CreateObjectVFX(929136, obj=arg_0_3, dummy_id=703)
    EnableObjectActivation(arg_0_3, obj_act_id=2900100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(arg_0_3, obj_act_id=2900100)
    CreateObjectVFX(929134, obj=arg_0_3, dummy_id=703)
    IfFlagEnabled(0, arg_4_7)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    ForceAnimation(arg_0_3, 1)
    Wait(2.5)
    CreateObjectVFX(929136, obj=arg_0_3, dummy_id=703)
    EnableObjectActivation(arg_0_3, obj_act_id=2900100)
    Wait(0.5)


def Event12900234(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12900234: Event 12900234 """
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_16_19)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_20_23)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    SkipLinesIfClient(2)
    DisplayDialog(
        arg_8_11,
        anchor_entity=PLAYER,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    RemoveGoodFromPlayer(arg_4_7)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_16_19)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_20_23)


def Event12900235(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12900235: Event 12900235 """
    SkipLinesIfThisEventSlotFlagDisabled(3)
    DisableObjectActivation(arg_8_11, obj_act_id=arg_12_15)
    DisableObjectActivation(arg_8_11, obj_act_id=arg_16_19)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    SkipLinesIfClient(1)
    DisplayDialog(
        arg_4_7,
        anchor_entity=PLAYER,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    DisableObjectActivation(arg_8_11, obj_act_id=arg_12_15)
    DisableObjectActivation(arg_8_11, obj_act_id=arg_16_19)


def Event12900236(_, arg_0_3: int):
    """ 12900236: Event 12900236 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(0, arg_0_3)
    CreatePlayLog(38)


def Event12901760(_, arg_0_3: int):
    """ 12901760: Event 12901760 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(0, arg_0_3)
    CreatePlayLog(38)


def Event12900238(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12900238: Event 12900238 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    EnableFlag(arg_16_19)


def Event12900239(_, arg_0_3: int, arg_4_7: int):
    """ 12900239: Event 12900239 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(0, arg_4_7)
    CreatePlayLog(76)
    Wait(1.5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=120,
        behavior_id=6020,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )


def Event12900240(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12900240: Event 12900240 """
    GotoIfFlagEnabled(Label.L0, arg_12_15)
    EndOfAnimation(arg_0_3, 10)
    EndOfAnimation(arg_4_7, 0)
    EndOfAnimation(arg_8_11, 1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(arg_0_3, 0)
    EndOfAnimation(arg_4_7, 1)
    EndOfAnimation(arg_8_11, 0)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(arg_16_19)


def Event12900245(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900245: Event 12900245 """
    IfFlagEnabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfFlagEnabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfCharacterInsideRegion(2, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_28_31)
    DisableFlag(arg_24_27)
    ForceAnimation(arg_8_11, 1)
    ForceAnimation(arg_0_3, 10, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_16_19)
    DisableFlag(arg_28_31)
    ForceAnimation(arg_4_7, 0)
    Restart()


def Event12900250(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900250: Event 12900250 """
    IfFlagDisabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_16_19)
    IfFlagDisabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfCharacterInsideRegion(2, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_28_31)
    EnableFlag(arg_24_27)
    ForceAnimation(arg_4_7, 1)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    DisableFlag(arg_28_31)
    ForceAnimation(arg_8_11, 0)
    Restart()


def Event12900255(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900255: Event 12900255 """
    DisableNetworkSync()
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfFlagDisabled(2, arg_8_11)
    IfFlagDisabled(2, arg_12_15)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=arg_4_7)
    IfFlagEnabled(3, arg_12_15)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=arg_0_3)
    IfFlagEnabled(4, arg_12_15)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900260(_, arg_0_3: int):
    """ 12900260: Event 12900260 """
    IfCharacterHasSpecialEffect(1, PLAYER, 6100)
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfCharacterIsHuman(-1, PLAYER)
    IfCharacterIsType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    EndIfConditionFalse(2)
    AwardItemLot(5530, host_only=True)


def Event12900293(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900293: Event 12900293 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    CreatePlayLog(112)
    EnableFlag(arg_8_11)
    WaitFrames(6)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_0_3)
    RestartIfConditionTrue(1)
    ResetAnimation(PLAYER, disable_interpolation=False)
    ForceAnimation(PLAYER, 101161)
    WaitFrames(59)
    EnableFlag(arg_4_7)
    IfFlagDisabled(0, arg_4_7)
    Restart()


def Event12900304(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12900304: Event 12900304 """
    DisableNetworkSync()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    PlayCutsceneAndMovePlayer_Dummy(arg_4_7, CHALICE_DUNGEON)
    WaitFrames(2)
    EnableFlag(arg_8_11)
    ForceAnimation(PLAYER, 101162, wait_for_completion=True)
    DisableFlag(arg_0_3)
    Restart()


def Event12901732(_, arg_0_3: int, arg_4_7: int):
    """ 12901732: Event 12901732 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    CreateObjectVFX(929102, obj=arg_4_7, dummy_id=700)
    CreateObjectVFX(929102, obj=arg_4_7, dummy_id=702)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, arg_0_3)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    CreateObjectVFX(929102, obj=arg_4_7, dummy_id=700)
    CreateObjectVFX(929102, obj=arg_4_7, dummy_id=702)

    # --- 1 --- #
    DefineLabel(1)
    CreateTemporaryVFX(929213, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=200)
    DisableFlag(arg_0_3)
    Restart()


def Event12901743(_, arg_0_3: int, arg_4_7: int):
    """ 12901743: Event 12901743 """
    IfFlagEnabled(0, arg_0_3)
    CreateTemporaryVFX(929215, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=-1)
    DisableFlag(arg_0_3)
    Restart()


def Event12900315(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12900315: Event 12900315 """
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfLastConditionResultTrue(4, 1)
    EndOfAnimation(arg_4_7, 12)
    DisableObjectActivation(arg_8_11, obj_act_id=arg_12_15)
    EnableObjectActivation(arg_16_19, obj_act_id=arg_12_15)
    SkipLines(3)
    EndOfAnimation(arg_4_7, 132)
    DisableObjectActivation(arg_16_19, obj_act_id=arg_12_15)
    EnableObjectActivation(arg_8_11, obj_act_id=arg_12_15)
    DisableFlag(arg_20_23)


def Event12900323(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900323: Event 12900323 """
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagEnabled(2, arg_0_3)
    IfFlagDisabled(2, arg_4_7)
    IfObjectActivated(2, obj_act_id=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 133, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 35, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 11, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_20_23)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    DisableObjectActivation(arg_24_27, obj_act_id=9902)
    EnableObjectActivation(arg_28_31, obj_act_id=9902)
    Restart()


def Event12900331(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900331: Event 12900331 """
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagDisabled(2, arg_0_3)
    IfFlagDisabled(2, arg_4_7)
    IfObjectActivated(2, obj_act_id=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 16, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 131, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_20_23)
    EnableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    DisableObjectActivation(arg_24_27, obj_act_id=9902)
    EnableObjectActivation(arg_28_31, obj_act_id=9902)
    Restart()


def Event12900339(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900339: Event 12900339 """
    DisableNetworkSync()
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_4_7)
    IfFlagDisabled(2, arg_0_3)
    IfFlagEnabled(2, arg_8_11)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=arg_12_15)
    IfFlagEnabled(3, arg_0_3)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=arg_12_15)
    IfFlagEnabled(4, arg_0_3)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12900347(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12900347: Event 12900347 """
    GotoIfFlagEnabled(Label.L0, arg_12_15)
    EndOfAnimation(arg_0_3, arg_20_23)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    EnableObjectActivation(arg_8_11, obj_act_id=9902)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(arg_0_3, arg_24_27)
    EnableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(arg_16_19)


def Event12900351(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900351: Event 12900351 """
    IfFlagEnabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_16_19)
    IfFlagEnabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfObjectActivated(2, obj_act_id=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_24_27)
    EnableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    EnableObjectActivation(arg_8_11, obj_act_id=9902)
    Restart()


def Event12900353(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900353: Event 12900353 """
    IfFlagEnabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_16_19)
    IfFlagEnabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfObjectActivated(2, obj_act_id=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_24_27)
    EnableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    ForceAnimation(arg_0_3, 20, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    ForceAnimation(arg_0_3, 21, wait_for_completion=True)
    DisableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    EnableObjectActivation(arg_8_11, obj_act_id=9902)
    Restart()


def Event12900354(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900354: Event 12900354 """
    IfFlagDisabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfFlagDisabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfObjectActivated(2, obj_act_id=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_24_27)
    EnableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    ForceAnimation(arg_0_3, 10, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_16_19)
    ForceAnimation(arg_0_3, 11, wait_for_completion=True)
    DisableFlag(arg_28_31)
    EnableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    Restart()


def Event12900356(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900356: Event 12900356 """
    IfFlagDisabled(1, arg_24_27)
    IfFlagDisabled(1, arg_28_31)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfFlagDisabled(2, arg_24_27)
    IfFlagDisabled(2, arg_28_31)
    IfObjectActivated(2, obj_act_id=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_24_27)
    EnableFlag(arg_28_31)
    DisableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    ForceAnimation(arg_0_3, 30, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_16_19)
    ForceAnimation(arg_0_3, 31, wait_for_completion=True)
    DisableFlag(arg_28_31)
    EnableObjectActivation(arg_4_7, obj_act_id=9902)
    DisableObjectActivation(arg_8_11, obj_act_id=9902)
    Restart()


def Event12900357(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12900357: Event 12900357 """
    DisableNetworkSync()
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfFlagEnabled(2, arg_8_11)
    IfFlagDisabled(2, arg_12_15)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=arg_4_7)
    IfFlagEnabled(3, arg_12_15)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=arg_0_3)
    IfFlagEnabled(4, arg_12_15)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()


def Event12900361(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12900361: Event 12900361 """
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    EnableFlag(arg_12_15)
    DisableFlag(arg_16_19)
    ForceAnimation(arg_20_23, 2, wait_for_completion=True)
    ForceAnimation(arg_24_27, 2, wait_for_completion=True)
    End()


def Event12900363(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12900363: Event 12900363 """
    Wait(1.0)
    SkipLinesIfFlagDisabled(19, arg_20_23)
    SkipLinesIfFlagEnabled(18, arg_4_7)
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 4, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 121, wait_for_completion=True)
    ForceAnimation(arg_16_19, 122, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    DisableFlag(arg_20_23)
    End()


def Event12900365(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900365: Event 12900365 """
    Wait(0.5)
    IfFlagDisabled(2, arg_0_3)
    IfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_20_23, 123)
    ForceAnimation(arg_16_19, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_20_23, 24)
    ForceAnimation(arg_16_19, 4, wait_for_completion=True)
    ForceAnimation(arg_20_23, 0, wait_for_completion=True)
    ForceAnimation(arg_16_19, 120, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 121)
    ForceAnimation(arg_20_23, 1, wait_for_completion=True)
    ForceAnimation(arg_16_19, 122, wait_for_completion=True)
    ForceAnimation(arg_20_23, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=arg_24_27)
    IfAllPlayersOutsideRegion(5, region=arg_28_31)
    IfConditionTrue(0, input_condition=5)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    Restart()


def Event12900367(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900367: Event 12900367 """
    Wait(0.5)
    IfFlagEnabled(2, arg_0_3)
    IfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 123)
    ForceAnimation(arg_20_23, 3, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_20_23, 4)
    ForceAnimation(arg_16_19, 24, wait_for_completion=True)
    ForceAnimation(arg_20_23, 120, wait_for_completion=True)
    ForceAnimation(arg_16_19, 0, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 1)
    ForceAnimation(arg_20_23, 121, wait_for_completion=True)
    ForceAnimation(arg_16_19, 2, wait_for_completion=True)
    ForceAnimation(arg_20_23, 122, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=arg_24_27)
    IfAllPlayersOutsideRegion(5, region=arg_28_31)
    IfConditionTrue(0, input_condition=5)
    EnableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    Restart()


def Event12900369(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12900369: Event 12900369 """
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    EnableFlag(arg_12_15)
    DisableFlag(arg_16_19)
    ForceAnimation(arg_20_23, 12, wait_for_completion=True)
    ForceAnimation(arg_24_27, 12, wait_for_completion=True)
    End()


def Event12900371(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12900371: Event 12900371 """
    Wait(1.0)
    SkipLinesIfFlagDisabled(19, arg_20_23)
    SkipLinesIfFlagEnabled(18, arg_4_7)
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 14, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 101, wait_for_completion=True)
    ForceAnimation(arg_16_19, 102, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    DisableFlag(arg_20_23)
    End()


def Event12900373(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900373: Event 12900373 """
    Wait(0.5)
    IfFlagDisabled(2, arg_0_3)
    IfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_20_23, 103)
    ForceAnimation(arg_16_19, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_20_23, 5)
    ForceAnimation(arg_16_19, 14, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 101)
    ForceAnimation(arg_20_23, 11, wait_for_completion=True)
    ForceAnimation(arg_16_19, 102, wait_for_completion=True)
    ForceAnimation(arg_20_23, 12, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=arg_24_27)
    IfAllPlayersOutsideRegion(5, region=arg_28_31)
    IfConditionTrue(0, input_condition=5)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    Restart()


def Event12900375(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12900375: Event 12900375 """
    Wait(0.5)
    IfFlagEnabled(2, arg_0_3)
    IfFlagEnabled(6, arg_4_7)
    IfFlagEnabled(7, 12900500)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    SkipLinesIfConditionTrue(28, -2)
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, 12900500)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    Wait(1.0)
    ForceAnimation(arg_16_19, 103)
    ForceAnimation(arg_20_23, 13, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_20_23, 14)
    ForceAnimation(arg_16_19, 5, wait_for_completion=True)
    Wait(0.5)
    ForceAnimation(arg_16_19, 11)
    ForceAnimation(arg_20_23, 101, wait_for_completion=True)
    ForceAnimation(arg_16_19, 12, wait_for_completion=True)
    ForceAnimation(arg_20_23, 102, wait_for_completion=True)
    IfAllPlayersOutsideRegion(5, region=arg_24_27)
    IfAllPlayersOutsideRegion(5, region=arg_28_31)
    IfConditionTrue(0, input_condition=5)
    EnableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    Restart()


def Event12900377(_, arg_0_3: int, arg_4_7: int):
    """ 12900377: Event 12900377 """
    GotoIfFlagEnabled(Label.L7, 92905107)
    GotoIfFlagEnabled(Label.L6, 92905106)
    GotoIfFlagEnabled(Label.L5, 92905105)
    GotoIfFlagEnabled(Label.L4, 92905104)
    GotoIfFlagEnabled(Label.L3, 92905103)
    GotoIfFlagEnabled(Label.L2, 92905102)
    GotoIfFlagEnabled(Label.L1, 92905101)
    GotoIfFlagEnabled(Label.L0, 92905100)

    # --- 0 --- #
    DefineLabel(0)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6137,
        target_type=DamageTargetType.Character,
        radius=0.30000001192092896,
        life=0.0,
        repetition_time=2.0,
    )


def Event12900395(_, arg_0_3: int, arg_4_7: int):
    """ 12900395: Event 12900395 """
    CreateObjectVFX(900110, obj=arg_0_3, dummy_id=704)
    GotoIfFlagEnabled(Label.L7, 92905107)
    GotoIfFlagEnabled(Label.L6, 92905106)
    GotoIfFlagEnabled(Label.L5, 92905105)
    GotoIfFlagEnabled(Label.L4, 92905104)
    GotoIfFlagEnabled(Label.L3, 92905103)
    GotoIfFlagEnabled(Label.L2, 92905102)
    GotoIfFlagEnabled(Label.L1, 92905101)
    GotoIfFlagEnabled(Label.L0, 92905100)

    # --- 0 --- #
    DefineLabel(0)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
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
        arg_4_7,
        arg_0_3,
        dummy_id=704,
        behavior_param_id=6167,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )


def Event12900423(_, arg_0_3: int, arg_4_7: int):
    """ 12900423: Event 12900423 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    CreatePlayLog(152)
    CreateTemporaryVFX(929209, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=-1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=997400000)
    DestroyObject(arg_4_7)


def Event12900430(_, arg_0_3: int):
    """ 12900430: Event 12900430 """
    DisableSpawner(arg_0_3)


def Event12901000(_, arg_0_3: int, arg_4_7: int):
    """ 12901000: Event 12901000 """
    DisableSpawner(arg_4_7)
    IfCharacterDrawGroupActive(1, arg_0_3)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=100)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(arg_4_7)
    IfCharacterDrawGroupInactive(-1, arg_0_3)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12901200(_, arg_0_3: int, arg_4_7: int):
    """ 12901200: Event 12901200 """
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, arg_4_7, tae_event_id=100)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        dummy_id=30,
        copy_draw_parent=arg_0_3,
    )
    IfCharacterDoesNotHaveTAEEvent(0, arg_4_7, tae_event_id=100)
    IfCharacterDead(0, arg_4_7)
    AddSpecialEffect_WithUnknownEffect(arg_4_7, 5751, affect_npc_parts_hp=False)
    Restart()


def Event12901272(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901272: Event 12901272 """
    IfCharacterHasTAEEvent(0, arg_8_11, tae_event_id=100)
    IfCharacterDead(1, arg_8_11)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultFalse(Label.L0, input_condition=2)
    DisableSpawner(arg_4_7)
    Kill(arg_8_11, award_souls=True)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


def Event12901347(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901347: Event 12901347 """
    IfFlagDisabled(1, arg_8_11)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfFlagEnabled(2, arg_8_11)
    IfAllPlayersOutsideRegion(2, region=arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=2)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    EnableFlag(arg_8_11)
    Wait(2.0999999046325684)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(arg_8_11)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    Restart()


def Event12901400(_, arg_0_3: int, arg_4_7: int):
    """ 12901400: Event 12901400 """
    IfObjectNotDestroyed(1, arg_0_3)
    IfFlagEnabled(2, arg_4_7)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    EndIfLastConditionResultFalse(1)
    CreatePlayLog(188)
    CreateTemporaryVFX(150005, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, dummy_id=101)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=990100001)
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6200,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6210,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6220,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6201,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6211,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6221,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6202,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6212,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6222,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6203,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6213,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6223,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6204,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6214,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6224,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6205,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6215,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6225,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6206,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6216,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6226,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
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
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6207,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6217,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(3)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6227,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(1)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6237,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    SkipLines(0)
    Wait(0.699999988079071)
    IfFlagDisabled(0, arg_4_7)
    Restart()


def Event12901447(_, arg_0_3: int, arg_4_7: int):
    """ 12901447: Event 12901447 """
    EndIfThisEventSlotFlagEnabled()
    AddNavmeshFaceFlag(arg_4_7, NavmeshFlag.Disable)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    RemoveNavmeshFaceFlag(arg_4_7, NavmeshFlag.Disable)


def Event12901525(_, arg_0_3: int, arg_4_7: int):
    """ 12901525: Event 12901525 """
    EndIfThisEventSlotFlagEnabled()
    AddNavmeshFaceFlag(arg_4_7, NavmeshFlag.Disable)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(3.0)
    RemoveNavmeshFaceFlag(arg_4_7, NavmeshFlag.Disable)


@RestartOnRest
def Event12901532(_, arg_0_3: int, arg_4_7: int):
    """ 12901532: Event 12901532 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterIsHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


def Event12901550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901550: Event 12901550 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_4_7, 1)
    EndOfAnimation(arg_8_11, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=2931100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    ForceAnimation(arg_8_11, 0, wait_for_completion=True)
    CreatePlayLog(224)


def Event12901554(_, arg_0_3: int, arg_4_7: int):
    """ 12901554: Event 12901554 """
    IfCharacterTargeting(-1, arg_0_3, PLAYER)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_4_7)
    ReplanAI(arg_0_3)


def Event12901555():
    """ 12901555: Event 12901555 """
    CreateProjectileOwner(2900000)
    DisableCharacter(2900000)


def Event12901556(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901556: Event 12901556 """
    RegisterLadder(start_climbing_flag=arg_0_3, stop_climbing_flag=arg_4_7, obj=arg_8_11)


def Event12901588(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901588: Event 12901588 """
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()
    IfCharacterDead(0, arg_0_3)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    Wait(3.0)
    IfCharacterIsHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    KillBoss(arg_0_3)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_12_15)


def Event12901589(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12901589: Event 12901589 """
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()
    IfCharacterDead(1, arg_0_3)
    IfCharacterDead(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    Wait(3.0)
    IfCharacterIsHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    KillBoss(arg_0_3)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_12_15)


def Event12901590(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901590: Event 12901590 """
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()
    IfCharacterDead(0, arg_0_3)
    CreatePlayLog(262)
    StopPlayLogMeasurement(2900020)
    KillBoss(arg_0_3)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    EnableFlag(arg_12_15)


def Event12901591(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901591: Event 12901591 """
    SkipLinesIfThisEventSlotFlagDisabled(7)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()
    IfCharacterDead(1, arg_0_3)
    IfCharacterDead(1, arg_24_27)
    IfCharacterDead(1, arg_28_31)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    Wait(3.0)
    IfCharacterIsHuman(0, PLAYER)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    KillBoss(arg_0_3)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_12_15)


def Event12901592(_, arg_0_3: int, arg_4_7: int):
    """ 12901592: Event 12901592 """
    SkipLinesIfThisEventSlotFlagEnabled(5)
    IfFlagEnabled(1, arg_0_3)
    IfFlagEnabled(1, 92905360)
    IfFlagDisabled(1, 12907220)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(12907220)
    DisableObject(arg_4_7)


def Event12901593(_, arg_0_3: int, arg_4_7: int):
    """ 12901593: Event 12901593 """
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfFlagEnabled(0, arg_0_3)
    DisableObject(arg_4_7)


def Event12901594(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901594: Event 12901594 """
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagEnabled(0, arg_0_3)
    IfFlagEnabled(1, 92905377)
    IfFlagDisabled(1, arg_28_31)
    SkipLinesIfConditionFalse(2, 1)
    AwardItemLot(arg_16_19, host_only=False)
    End()
    SkipLinesIfFlagEnabled(2, 92905378)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    IfFlagEnabled(2, 92905360)
    IfFlagEnabled(2, 12907220)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(arg_16_19, host_only=False)
    End()
    AwardItemLot(arg_20_23, host_only=False)
    End()
    SkipLinesIfClient(9)
    EndIfFlagRangeAllDisabled((92905370, 92905373))
    SkipLinesIfFlagEnabled(3, arg_28_31)
    AwardItemLot(arg_20_23, host_only=False)
    EnableFlag(arg_28_31)
    SkipLines(1)
    AwardItemLot(arg_24_27, host_only=False)
    EndIfFlagRangeAllDisabled((92905371, 92905373))
    AwardItemLot(arg_20_23, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=True)
    End()
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(arg_12_15, host_only=True)
    End()


def Event12901595(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901595: Event 12901595 """
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagEnabled(0, arg_0_3)
    IfFlagEnabled(1, 92905377)
    IfFlagDisabled(1, arg_28_31)
    SkipLinesIfConditionFalse(2, 1)
    AwardItemLot(arg_16_19, host_only=False)
    End()
    SkipLinesIfFlagEnabled(2, 92905378)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    IfFlagEnabled(2, 92905360)
    IfFlagEnabled(2, 12907220)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(arg_16_19, host_only=False)
    End()
    AwardItemLot(arg_20_23, host_only=False)
    End()
    SkipLinesIfClient(11)
    EndIfFlagDisabled(92905360)
    AwardItemLot(arg_16_19, host_only=False)
    EndIfFlagRangeAllDisabled((92905370, 92905373))
    SkipLinesIfFlagEnabled(3, arg_28_31)
    AwardItemLot(arg_20_23, host_only=False)
    EnableFlag(arg_28_31)
    SkipLines(1)
    AwardItemLot(arg_24_27, host_only=False)
    EndIfFlagRangeAllDisabled((92905371, 92905373))
    AwardItemLot(arg_20_23, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=True)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(arg_12_15, host_only=True)
    End()


def Event12901596(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901596: Event 12901596 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfClient(2)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=False)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(arg_12_15, host_only=True)
    End()


def Event12901597(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901597: Event 12901597 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfClient(2)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=False)
    SkipLinesIfFlagRangeAllDisabled(1, (92905370, 92905373))
    AwardItemLot(arg_12_15, host_only=True)
    End()


def Event12901598(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901598: Event 12901598 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfClient(2)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=False)
    End()


def Event12901599(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901599: Event 12901599 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11, loop=True, skip_transition=True)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    FaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)


def Event12901600(_, arg_0_3: int, arg_4_7: int):
    """ 12901600: Event 12901600 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    DisableCharacter(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=205)
    WaitFrames(10)
    EnableCharacter(arg_0_3)


def Event12901601(_, arg_0_3: int):
    """ 12901601: Event 12901601 """
    DisableObject(arg_0_3)


def Event12901602(_, arg_0_3: int, arg_4_7: int):
    """ 12901602: Event 12901602 """
    CreateObjectVFX(8020, obj=arg_4_7, dummy_id=200)
    ForceAnimation(arg_4_7, 200, loop=True, wait_for_completion=True)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    ForceAnimation(arg_4_7, 1000000, wait_for_completion=True)
    CreateObjectVFX(8023, obj=arg_4_7, dummy_id=100)
    ForceAnimation(arg_4_7, 1000100, loop=True, wait_for_completion=True)


def Event12901684(_, arg_0_3: int, arg_4_7: int):
    """ 12901684: Event 12901684 """
    IfFlagEnabled(0, arg_0_3)
    AwardAchievement(arg_4_7)


def Event12901685():
    """ 12901685: Event 12901685 """
    StartPlayLogMeasurement(2900000, 380, overwrite=False)
    SkipLinesIfFlagEnabled(5, 12901809)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 398, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 398, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 398, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 398, PlayLogMultiplayerType.HostOnly)
    EnableFlag(12901809)
    SkipLinesIfFlagEnabled(5, 12901800)
    StartPlayLogMeasurement(2901000, 426, overwrite=False)
    StartPlayLogMeasurement(2901001, 462, overwrite=True)
    IfFlagEnabled(0, 12901800)
    StopPlayLogMeasurement(2901000)
    StopPlayLogMeasurement(2901001)
    SkipLinesIfFlagEnabled(5, 12901801)
    StartPlayLogMeasurement(2901010, 502, overwrite=False)
    StartPlayLogMeasurement(2901011, 538, overwrite=True)
    IfFlagEnabled(0, 12901801)
    StopPlayLogMeasurement(2901010)
    StopPlayLogMeasurement(2901011)
    SkipLinesIfFlagEnabled(5, 12901802)
    StartPlayLogMeasurement(2901020, 578, overwrite=False)
    StartPlayLogMeasurement(2901021, 614, overwrite=True)
    IfFlagEnabled(0, 12901802)
    StopPlayLogMeasurement(2901020)
    StopPlayLogMeasurement(2901021)
    SkipLinesIfFlagDisabled(6, 92905360)
    SkipLinesIfFlagEnabled(5, 12901803)
    StartPlayLogMeasurement(2901030, 654, overwrite=False)
    StartPlayLogMeasurement(2901031, 692, overwrite=True)
    IfFlagEnabled(0, 12901803)
    StopPlayLogMeasurement(2901030)
    StopPlayLogMeasurement(2901031)
    StopPlayLogMeasurement(2900000)
    End()


def Event12901686(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901686: Event 12901686 """
    GotoIfFlagDisabled(Label.L0, arg_20_23)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    DeleteVFX(arg_12_15, erase_root_only=True)
    DeleteVFX(arg_16_19, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, arg_0_3)
    IfHealthRatioEqual(-1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, arg_0_3)
    IfTimeElapsed(-2, 15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    DeleteVFX(arg_12_15, erase_root_only=True)
    DeleteVFX(arg_16_19, erase_root_only=True)
    Wait(3.0)
    KillBoss(arg_0_3)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(arg_20_23)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(arg_20_23)


def Event12901690(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901690: Event 12901690 """
    GotoIfFlagDisabled(Label.L0, arg_12_15)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, arg_0_3)
    IfHealthRatioEqual(-1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, arg_0_3)
    IfTimeElapsed(-2, 15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    Wait(3.0)
    KillBoss(arg_0_3)
    SetNetworkUpdateRate(arg_0_3, is_fixed=False, update_rate=CharacterUpdateRate.EveryTwoFrames)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(arg_12_15)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(arg_12_15)


def Event12901692(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901692: Event 12901692 """
    GotoIfFlagDisabled(Label.L0, arg_20_23)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    DeleteVFX(arg_12_15, erase_root_only=True)
    DeleteVFX(arg_16_19, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, arg_0_3)
    IfHealthRatioEqual(-1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterDead(-2, arg_0_3)
    IfTimeElapsed(-2, 15.0)
    IfConditionTrue(0, input_condition=-2)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    DeleteVFX(arg_12_15, erase_root_only=True)
    DeleteVFX(arg_16_19, erase_root_only=True)
    Wait(3.0)
    HandleMinibossDefeat(arg_0_3)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_20_23, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_20_23)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(arg_20_23)


def Event12901693(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12901693: Event 12901693 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    GotoIfClient(Label.L0)
    IfFlagEnabled(1, 92905385)
    IfFlagEnabled(-1, 12907212)
    IfFlagEnabled(-1, 12907213)
    IfConditionTrue(1, input_condition=-1)
    SkipLinesIfConditionFalse(6, 1)
    IfFlagEnabled(2, 12907213)
    SkipLinesIfConditionTrue(2, 2)
    AwardItemLot(arg_20_23, host_only=False)
    Goto(Label.L1)
    AwardItemLot(arg_24_27, host_only=False)
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
    AwardItemLot(arg_20_23, host_only=False)
    Goto(Label.L1)
    AwardItemLot(arg_24_27, host_only=False)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, 92905360)
    GotoIfFlagDisabled(Label.L0, 12907212)
    EnableFlag(12907221)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L0, 12907213)
    EnableFlag(12907221)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfClient(Label.L4)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(arg_4_7, host_only=True)
    Goto(Label.L9)
    AwardItemLot(arg_8_11, host_only=True)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(arg_12_15, host_only=True)
    Goto(Label.L9)
    AwardItemLot(arg_16_19, host_only=True)
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


def Event12901697(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901697: Event 12901697 """
    EndIfFlagEnabled(arg_16_19)
    EndIfFlagEnabled(arg_24_27)
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11, loop=True, skip_transition=True)
    IfObjectActivated(0, obj_act_id=arg_28_31)
    IfFlagDisabled(1, arg_16_19)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterIsHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    EnableFlag(arg_20_23)
    EnableFlag(arg_24_27)


def Event12901701(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901701: Event 12901701 """
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_16_19)
    DisableCharacter(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_20_23)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_16_19)
    IfCharacterIsHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=6)
    WaitFrames(15)
    EnableCharacter(arg_0_3)


def Event12901705(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901705: Event 12901705 """
    EndIfFlagEnabled(arg_16_19)
    EndIfFlagEnabled(arg_24_27)
    ForceAnimation(arg_0_3, arg_8_11, loop=True, skip_transition=True)
    IfObjectActivated(0, obj_act_id=arg_28_31)
    IfFlagDisabled(1, arg_16_19)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterIsHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    EnableFlag(arg_20_23)
    EnableFlag(arg_24_27)


def Event12901706(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12901706: Event 12901706 """
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_16_19)
    DisableCharacter(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_20_23)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_16_19)
    IfCharacterIsHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=6)
    WaitFrames(15)
    EnableCharacter(arg_0_3)


def Event12901707(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901707: Event 12901707 """
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_16_19)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    IfObjectActivated(0, obj_act_id=arg_28_31)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_16_19)
    IfCharacterIsHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=6)
    WaitFrames(15)
    EnableCharacter(arg_0_3)
    WaitFrames(15)
    CreateTemporaryVFX(929227, anchor_entity=arg_20_23, anchor_type=CoordEntityType.Character, dummy_id=6)
    WaitFrames(15)
    EnableCharacter(arg_20_23)
    WaitFrames(15)
    CreateTemporaryVFX(929227, anchor_entity=arg_24_27, anchor_type=CoordEntityType.Character, dummy_id=6)
    WaitFrames(15)
    EnableCharacter(arg_24_27)


def Event12901708(_, arg_0_3: int, arg_4_7: int):
    """ 12901708: Event 12901708 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=127000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=216000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=304000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=313000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=750000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=7200)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=7040)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=106000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=218000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=209000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=257000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=305000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=305010)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=501000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=504000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=510000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=251000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=306000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=508000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=509000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=509010)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 0 --- #
    DefineLabel(0)


def Event12901712(_, arg_0_3: int, arg_4_7: int):
    """ 12901712: Event 12901712 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=216000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=216000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=304000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=313000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=750000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=7200)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=209000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=257000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=305000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=305010)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=501000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=504000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=510000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=251000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=306000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=508000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=509000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=509010)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 0 --- #
    DefineLabel(0)


def Event12901713(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901713: Event 12901713 """
    GotoIfFlagDisabled(Label.L0, arg_12_15)
    EndOfAnimation(arg_4_7, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(0.0)


def Event12901717(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12901717: Event 12901717 """
    GotoIfFlagDisabled(Label.L0, arg_12_15)
    EndOfAnimation(arg_4_7, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(0.0)


def Event12901718(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901718: Event 12901718 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(0, arg_0_3)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=216000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=209000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=305000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=305010)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=501000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=510000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=251000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=306000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=508000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=509000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=509010)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)
    EnableFlag(arg_8_11)


def Event12901722(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12901722: Event 12901722 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(0, arg_0_3)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=216000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=209000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=305000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=305010)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=501000)
    GotoIfValueComparison(Label.L2, ComparisonType.Equal, left=arg_4_7, right=510000)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=251000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=306000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=508000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=509000)
    GotoIfValueComparison(Label.L1, ComparisonType.Equal, left=arg_4_7, right=509010)
    GotoIfValueComparison(Label.L3, ComparisonType.Equal, left=arg_4_7, right=512000)
    End()

    # --- 9 --- #
    DefineLabel(9)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 8 --- #
    DefineLabel(8)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 7 --- #
    DefineLabel(7)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 6 --- #
    DefineLabel(6)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 5 --- #
    DefineLabel(5)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 4 --- #
    DefineLabel(4)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)

    # --- 1 --- #
    DefineLabel(1)
    AddSpecialEffect(PLAYER, 4680, affect_npc_part_hp=False)
    WaitFrames(10)
    EnableFlag(arg_8_11)


def Event12901723(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12901723: Event 12901723 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, arg_0_3)
    IfHealthRatioEqual(-1, arg_0_3, 0.0)
    IfCharacterDead(-2, arg_24_27)
    IfHealthRatioEqual(-2, arg_24_27, 0.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(2, arg_0_3)
    IfCharacterDead(2, arg_24_27)
    IfConditionTrue(-3, input_condition=2)
    IfTimeElapsed(-3, 15.0)
    IfConditionTrue(0, input_condition=-3)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    Wait(3.0)
    KillBoss(arg_0_3)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_12_15)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(arg_12_15)


def Event12901725(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12901725: Event 12901725 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_24_27)
    DisableCharacter(arg_28_31)
    Kill(arg_0_3, award_souls=False)
    Kill(arg_24_27, award_souls=False)
    Kill(arg_28_31, award_souls=False)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(-1, arg_0_3)
    IfHealthRatioEqual(-1, arg_0_3, 0.0)
    IfCharacterDead(-2, arg_24_27)
    IfHealthRatioEqual(-2, arg_24_27, 0.0)
    IfCharacterDead(-3, arg_28_31)
    IfHealthRatioEqual(-3, arg_28_31, 0.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(2, arg_0_3)
    IfCharacterDead(2, arg_24_27)
    IfCharacterDead(2, arg_28_31)
    IfConditionTrue(-4, input_condition=2)
    IfTimeElapsed(-4, 15.0)
    IfConditionTrue(0, input_condition=-4)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(arg_4_7)
    DisableObject(arg_16_19)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DeleteVFX(arg_20_23, erase_root_only=True)
    Wait(3.0)
    KillBoss(arg_0_3)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    CreatePlayLog(262)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901800)
    StopPlayLogMeasurement(2900010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 274, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 274, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901801)
    StopPlayLogMeasurement(2900011)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 300, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 300, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901802)
    StopPlayLogMeasurement(2900012)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 326, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 326, PlayLogMultiplayerType.HostOnly)
    SkipLinesIfValueNotEqual(5, left=arg_12_15, right=12901803)
    StopPlayLogMeasurement(2900013)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 352, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 352, PlayLogMultiplayerType.HostOnly)
    EnableFlag(arg_12_15)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Wait(0.0)
    EnableFlag(arg_12_15)


def Event12901727(_, arg_0_3: int, arg_4_7: int):
    """ 12901727: Event 12901727 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, arg_0_3)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    DisableObject(arg_4_7)


def Event12901728(_, arg_0_3: int, arg_4_7: int):
    """ 12901728: Event 12901728 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableObject(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_0_3)
    IfFlagEnabled(1, 92905360)
    IfFlagDisabled(1, 12907220)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    EnableFlag(12907220)
    DisableObject(arg_4_7)


def Event12901730(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12901730: Event 12901730 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(arg_4_7, host_only=False)
    End()
    AwardItemLot(arg_8_11, host_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagEnabled(2, 92905370)
    AwardItemLot(arg_12_15, host_only=False)
    End()
    AwardItemLot(arg_16_19, host_only=False)
    End()


def Event12901754(_, arg_0_3: int):
    """ 12901754: Event 12901754 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event12904000(_, arg_0_3: int, arg_4_7: int):
    """ 12904000: Event 12904000 """
    DisableCharacter(arg_4_7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, dummy_id=90, short_move=True)
    EnableCharacter(arg_4_7)
    ForceAnimation(arg_4_7, 2250, loop=True)
    WaitFrames(5)
    DropMandatoryTreasure(arg_4_7)
    WaitFrames(135)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)


@RestartOnRest
def Event12904013(_, arg_0_3: int):
    """ 12904013: Event 12904013 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5676)
    RemoveSpecialEffect(arg_0_3, 5333)


def Event12904026(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904026: Event 12904026 """
    EndIfFlagEnabled(arg_8_11)
    DisableHealthBar(arg_0_3)
    DisableHealthBar(arg_4_7)
    EnableImmortality(arg_0_3)
    EnableImmortality(arg_4_7)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)


def Event12904027(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904027: Event 12904027 """
    GotoIfFlagDisabled(Label.L0, arg_12_15)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthValueEqual(0, arg_0_3, 0)
    Kill(arg_4_7, award_souls=False)
    Kill(arg_8_11, award_souls=False)


def Event12904028(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904028: Event 12904028 """
    EndIfFlagEnabled(arg_12_15)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.4000000059604645)
    AICommand(arg_4_7, command_id=100, slot=1)
    AICommand(arg_8_11, command_id=100, slot=1)


def Event12904029(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904029: Event 12904029 """
    EndIfClient()
    EndIfFlagEnabled(arg_20_23)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    IncrementEventValue(arg_4_7, bit_count=10, max_value=9)
    IfEventValueEqual(-1, arg_4_7, bit_count=10, value=1)
    IfEventValueEqual(-1, arg_4_7, bit_count=10, value=3)
    IfEventValueEqual(-1, arg_4_7, bit_count=10, value=7)
    IfEventValueEqual(-2, arg_4_7, bit_count=10, value=2)
    IfEventValueEqual(-2, arg_4_7, bit_count=10, value=5)
    IfEventValueEqual(-2, arg_4_7, bit_count=10, value=9)
    IfEventValueEqual(-3, arg_4_7, bit_count=10, value=4)
    IfEventValueEqual(-3, arg_4_7, bit_count=10, value=6)
    IfEventValueEqual(-3, arg_4_7, bit_count=10, value=8)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    GotoIfConditionTrue(Label.L1, input_condition=-2)
    GotoIfConditionTrue(Label.L2, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_8_11)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_12_15)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(arg_16_19)

    # --- 3 --- #
    DefineLabel(3)
    IfEventValueEqual(1, arg_4_7, bit_count=10, value=9)
    SkipLinesIfConditionFalse(1, 1)
    ClearEventValue(arg_4_7, bit_count=10)
    DisableCharacter(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=90)
    DisableFlag(arg_8_11)
    DisableFlag(arg_12_15)
    DisableFlag(arg_16_19)
    Restart()


def Event12904030(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12904030: Event 12904030 """
    EndIfClient()
    EndIfFlagEnabled(arg_24_27)
    IfFlagEnabled(0, arg_4_7)
    IncrementEventValue(arg_8_11, bit_count=10, max_value=12)
    IfEventValueEqual(-1, arg_8_11, bit_count=10, value=4)
    IfEventValueEqual(-1, arg_8_11, bit_count=10, value=6)
    IfEventValueEqual(-1, arg_8_11, bit_count=10, value=8)
    IfEventValueEqual(-1, arg_8_11, bit_count=10, value=11)
    IfEventValueEqual(-2, arg_8_11, bit_count=10, value=1)
    IfEventValueEqual(-2, arg_8_11, bit_count=10, value=5)
    IfEventValueEqual(-2, arg_8_11, bit_count=10, value=9)
    IfEventValueEqual(-2, arg_8_11, bit_count=10, value=12)
    IfEventValueEqual(-3, arg_8_11, bit_count=10, value=2)
    IfEventValueEqual(-3, arg_8_11, bit_count=10, value=3)
    IfEventValueEqual(-3, arg_8_11, bit_count=10, value=7)
    IfEventValueEqual(-3, arg_8_11, bit_count=10, value=10)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    GotoIfConditionTrue(Label.L1, input_condition=-2)
    GotoIfConditionTrue(Label.L2, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_12_15)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_16_19)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(arg_20_23)

    # --- 3 --- #
    DefineLabel(3)
    IfEventValueEqual(1, arg_8_11, bit_count=10, value=12)
    SkipLinesIfConditionFalse(1, 1)
    ClearEventValue(arg_8_11, bit_count=10)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=90)
    DisableFlag(arg_12_15)
    DisableFlag(arg_16_19)
    DisableFlag(arg_20_23)
    Restart()


def Event12904033(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904033: Event 12904033 """
    EndIfFlagEnabled(arg_28_31)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 5516)
    IfFlagEnabled(2, arg_8_11)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 5516)
    IfFlagEnabled(3, arg_12_15)
    IfCharacterDoesNotHaveSpecialEffect(3, arg_0_3, 5516)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Wait(2.0)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=2)
    GotoIfLastConditionResultTrue(Label.L2, input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_16_19, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    Move(arg_0_3, destination=arg_20_23, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    Move(arg_0_3, destination=arg_24_27, destination_type=CoordEntityType.Region, short_move=True)

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3021)
    WaitFrames(70)
    Restart()


def Event12904036(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904036: Event 12904036 """
    EndIfFlagEnabled(arg_28_31)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5516)
    IfFlagEnabled(2, arg_8_11)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5516)
    IfFlagEnabled(3, arg_12_15)
    IfCharacterHasSpecialEffect(3, arg_0_3, 5516)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Wait(2.0)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=2)
    GotoIfLastConditionResultTrue(Label.L2, input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_16_19, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    Move(arg_0_3, destination=arg_20_23, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    Move(arg_0_3, destination=arg_24_27, destination_type=CoordEntityType.Region, short_move=True)

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3022)
    WaitFrames(70)
    Restart()


def Event12904039(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904039: Event 12904039 """
    EndIfFlagEnabled(arg_28_31)
    IfCharacterHasTAEEvent(1, arg_24_27, tae_event_id=90)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, 5610, affect_npc_part_hp=False)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    EnableCharacter(arg_20_23)
    ReplanAI(arg_0_3)
    ForceAnimation(arg_0_3, 3021, wait_for_completion=True)
    DisableFlag(arg_8_11)
    EnableFlag(arg_12_15)
    IfFlagEnabled(0, arg_8_11)
    Restart()


def Event12904040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904040: Event 12904040 """
    EndIfFlagEnabled(arg_20_23)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfCharacterHasTAEEvent(2, arg_16_19, tae_event_id=80)
    IfFlagEnabled(2, arg_8_11)
    IfCharacterHasSpecialEffect(3, arg_16_19, 5517)
    IfFlagEnabled(3, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultFalse(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, 7010, wait_for_completion=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 3020)
    WaitFrames(65)

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_12_15)
    DisableFlag(arg_8_11)
    EnableFlag(arg_4_7)
    Restart()


@RestartOnRest
def Event12904041(_, arg_0_3: int, arg_4_7: int):
    """ 12904041: Event 12904041 """
    DisableGravity(arg_4_7)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(arg_4_7)
    End()
    Move(
        arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, dummy_id=6, set_draw_parent=arg_0_3
    )
    Restart()


@RestartOnRest
def Event12904042(_, arg_0_3: int, arg_4_7: int):
    """ 12904042: Event 12904042 """
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    AICommand(arg_4_7, command_id=100, slot=0)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=90)
    AICommand(arg_4_7, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12904043(_, arg_0_3: int, arg_4_7: int):
    """ 12904043: Event 12904043 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, 9000, loop=True)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    CreatePlayLog(734)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, 1500, wait_for_completion=True)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904070: Event 12904070 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_4_7)
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=70)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        dummy_id=230,
        copy_draw_parent=arg_0_3,
    )

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    IfCharacterDrawGroupInactive(0, arg_4_7)
    CreatePlayLog(768)
    EnableCharacter(arg_4_7)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12904156(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904156: Event 12904156 """
    DisableNetworkSync()
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    Move(
        arg_0_3,
        destination=arg_4_7,
        destination_type=CoordEntityType.Character,
        dummy_id=arg_8_11,
        copy_draw_parent=arg_4_7,
    )
    IfCharacterDoesNotHaveTAEEvent(0, arg_0_3, tae_event_id=100)
    IfCharacterDead(0, arg_0_3)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 5751, affect_npc_parts_hp=False)
    Restart()


@RestartOnRest
def Event12904183(_, arg_0_3: int, arg_4_7: int):
    """ 12904183: Event 12904183 """
    IfCharacterDead(0, arg_0_3)
    IncrementEventValue(arg_4_7, bit_count=3, max_value=6)
    IfCharacterAlive(0, arg_0_3)
    EventValueOperation(arg_4_7, 3, 1, 0, 1, CalculationType.Subtract)
    Restart()


@RestartOnRest
def Event12904210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904210: Event 12904210 """
    GotoIfFlagEnabled(Label.L0, arg_12_15)
    IfFlagEnabled(0, arg_0_3)
    AICommand(arg_4_7, command_id=100, slot=0)
    ReplanAI(arg_4_7)
    EnableFlag(arg_12_15)
    IfTimeElapsed(0, 2.0)
    AICommand(arg_4_7, command_id=-1, slot=0)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_0_3)
    IfEventValueComparison(1, arg_8_11, bit_count=3, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=100, slot=0)
    ReplanAI(arg_4_7)
    IfTimeElapsed(0, 2.0)
    AICommand(arg_4_7, command_id=-1, slot=0)
    IfTimeElapsed(0, 3.0)
    Restart()


@RestartOnRest
def Event12904216(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904216: Event 12904216 """
    DisableSpawner(arg_8_11)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHasTAEEvent(1, arg_4_7, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(arg_8_11)
    Wait(3.0)
    IfFlagDisabled(-1, arg_0_3)
    IfCharacterDoesNotHaveTAEEvent(-1, arg_4_7, tae_event_id=10)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest
def Event12904222(_, arg_0_3: int, arg_4_7: int):
    """ 12904222: Event 12904222 """
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, arg_4_7)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfHasAIStatus(-2, arg_4_7, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, arg_4_7)
    IfCharacterBackreadDisabled(-2, arg_4_7)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(arg_0_3)
    Restart()


@RestartOnRest
def Event12904228(_, arg_0_3: int, arg_4_7: int):
    """ 12904228: Event 12904228 """
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    IncrementEventValue(arg_4_7, bit_count=3, max_value=6)
    IfCharacterDead(0, arg_0_3)
    EventValueOperation(arg_4_7, 3, 1, 0, 1, CalculationType.Subtract)
    Restart()


@RestartOnRest
def Event12904274(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904274: Event 12904274 """

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_0_3)
    IfEventValueComparison(1, arg_8_11, bit_count=3, comparison_type=ComparisonType.LessThanOrEqual, value=2)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_4_7, 3011)
    AICommand(arg_4_7, command_id=10, slot=2)
    ReplanAI(arg_4_7)
    IfTimeElapsed(0, 2.0)
    AICommand(arg_4_7, command_id=-1, slot=2)
    IfTimeElapsed(0, 3.0)
    Restart()


@RestartOnRest
def Event12904285(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904285: Event 12904285 """
    DisableSpawner(arg_8_11)
    DisableSpawner(arg_12_15)
    DisableSpawner(arg_16_19)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHasTAEEvent(1, arg_4_7, tae_event_id=20)
    IfConditionTrue(0, input_condition=1)
    EnableSpawner(arg_8_11)
    EnableSpawner(arg_12_15)
    EnableSpawner(arg_16_19)
    Wait(3.0)
    IfFlagDisabled(-1, arg_0_3)
    IfCharacterDoesNotHaveTAEEvent(-1, arg_4_7, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@RestartOnRest
def Event12904326(_, arg_0_3: int, arg_4_7: int):
    """ 12904326: Event 12904326 """
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, arg_4_7)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    IfHasAIStatus(-2, arg_4_7, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, arg_4_7)
    IfCharacterBackreadDisabled(-2, arg_4_7)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(arg_0_3)
    Restart()


@RestartOnRest
def Event12904337(_, arg_0_3: int, arg_4_7: int):
    """ 12904337: Event 12904337 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterBackreadEnabled(0, arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5401, affect_npc_part_hp=False)
    DisableAI(arg_0_3)
    DisableCharacter(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    CreatePlayLog(806)
    Wait(3.0)
    EnableCharacter(arg_0_3)
    EnableAnimations(arg_0_3)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12904338(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904338: Event 12904338 """
    EndIfFlagEnabled(arg_12_15)
    CreateTemporaryVFX(0, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, dummy_id=-1)
    IfCharacterBackreadEnabled(0, arg_8_11)
    DisableAI(arg_8_11)
    DisableCharacter(arg_8_11)
    IfObjectActivated(1, obj_act_id=arg_4_7)
    IfObjectDestroyed(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_12_15)
    CreatePlayLog(806)
    SkipLinesIfLastConditionResultTrue(1, 2)
    Wait(2.0)
    EnableCharacter(arg_8_11)
    WaitFrames(2)
    ForceAnimation(arg_8_11, 3020)
    IfFramesElapsed(-1, 40)
    IfAttackedWithDamageType(-1, attacked_entity=arg_8_11, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_8_11)


def Event12904342(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904342: Event 12904342 """
    DisableObject(arg_8_11)
    EnableObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_0_3, 0)
    WaitFrames(10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(8.5)
    RemoveObjectFlag(arg_4_7)
    DisableObject(arg_0_3)
    EnableObject(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_8_11, 10)
    WaitFrames(1)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(arg_12_15)
    DisableObject(arg_8_11)
    Restart()


def Event12904343(_, arg_0_3: int):
    """ 12904343: Event 12904343 """
    SetCollisionMask(arg_0_3, bit_index=0, switch_type=OnOffChange.Off)


def Event12904345(_, arg_0_3: int):
    """ 12904345: Event 12904345 """
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=9.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 7007)
    AICommand(arg_0_3, command_id=10, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 404)
    IfTimeElapsed(-1, 10.0)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)


def Event12904361(_, arg_0_3: int, arg_4_7: int):
    """ 12904361: Event 12904361 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    DisableCharacter(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=10,
        part_index=NPCPartType.Part1,
        part_health=30,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=10, material_sfx_id=59, material_vfx_id=59)
    DisableCharacter(arg_4_7)
    IfCharacterPartHealthLessThanOrEqual(-1, arg_0_3, npc_part_id=10, value=0)
    IfHealthLessThanOrEqual(-1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, 121001)
    DisableGravity(arg_4_7)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        dummy_id=40,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    SetDisplayMask(arg_0_3, bit_index=0, switch_type=OnOffChange.On)
    ForceAnimation(arg_4_7, 8100, wait_for_completion=True)
    DisableCharacter(arg_4_7)


def Event12904369(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904369: Event 12904369 """
    GotoIfFlagDisabled(Label.L0, arg_8_11)
    PostDestruction(arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15)
    EnableTreasure(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    CreateObjectVFX(900201, obj=arg_4_7, dummy_id=90)
    ForceAnimation(arg_4_7, arg_16_19)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_20_23, wait_for_completion=True)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)
    EnableFlag(arg_8_11)


@RestartOnRest
def Event12904373(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int):
    """ 12904373: Event 12904373 """
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    IfEntityBeyondDistance(1, arg_0_3, PLAYER, radius=arg_8_11)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_12_15)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_8_11)
    IfEntityBeyondDistance(-1, arg_0_3, PLAYER, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfLastConditionResultTrue(6, 2)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, arg_16_19, wait_for_completion=True)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    Restart()


def Event12904374(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904374: Event 12904374 """
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(2.299999952316284)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, dummy_id=200, short_move=True)
    AddSpecialEffect(arg_4_7, 5580, affect_npc_part_hp=False)
    ForceAnimation(arg_8_11, 1)
    Wait(1.0)
    RemoveSpecialEffect(arg_4_7, 5580)
    WaitFrames(30)
    EnableObjectActivation(arg_8_11, obj_act_id=9800)
    Restart()


def Event12904382(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int):
    """ 12904382: Event 12904382 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, arg_4_7, radius=arg_8_11)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-3, PLAYER, region=arg_16_19)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=4)
    ActivateObjectWithSpecificCharacter(arg_4_7, objact_id=9800, relative_index=-1, character=arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event12904390(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12904390: Event 12904390 """
    ForceAnimation(arg_0_3, 0)
    ForceAnimation(arg_4_7, 0)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(844)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_16_19, 0)
    CreateTemporaryVFX(150005, anchor_entity=arg_16_19, anchor_type=CoordEntityType.Object, dummy_id=101)
    PlaySoundEffect(anchor_entity=arg_20_23, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_20_23, 0)
    CreateTemporaryVFX(150005, anchor_entity=arg_20_23, anchor_type=CoordEntityType.Object, dummy_id=101)
    Wait(0.10000000149011612)
    EnableFlag(arg_24_27)
    ForceAnimation(arg_4_7, 1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    ForceAnimation(arg_4_7, 10)
    ForceAnimation(arg_0_3, 10, wait_for_completion=True)
    DisableFlag(arg_24_27)
    Wait(0.10000000149011612)
    ForceAnimation(arg_4_7, 11)
    ForceAnimation(arg_0_3, 11, wait_for_completion=True)
    IfCharacterOutsideRegion(0, PLAYER, region=arg_8_11)
    PlaySoundEffect(anchor_entity=arg_16_19, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_16_19, 1)
    PlaySoundEffect(anchor_entity=arg_20_23, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_20_23, 1)
    Wait(0.10000000149011612)
    Restart()


@RestartOnRest
def Event12904398(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904398: Event 12904398 """
    AwaitFlagEnabled(arg_4_7)
    SkipLinesIfFlagDisabled(3, 92905100)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6250,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905101)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6251,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905102)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6252,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905103)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6253,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905104)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6254,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905105)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6255,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905106)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=6256,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(3, 92905107)
    CreateHazard(
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=6257,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6257,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
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
        arg_8_11,
        arg_0_3,
        dummy_id=100,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_16_19,
        arg_0_3,
        dummy_id=102,
        behavior_param_id=5041,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=1.0,
        repetition_time=0.0,
    )
    AwaitFlagDisabled(arg_4_7)
    Restart()


@RestartOnRest
def Event12904406(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904406: Event 12904406 """
    End()
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=35.0)
    SetAIParamID(arg_0_3, arg_4_7)
    IfEntityBeyondDistance(0, arg_0_3, PLAYER, radius=55.0)
    SetAIParamID(arg_0_3, arg_8_11)
    Restart()


@RestartOnRest
def Event12904410(_, arg_0_3: int):
    """ 12904410: Event 12904410 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, 9000, loop=True)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(880)
    Wait(0.30000001192092896)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, 9060, wait_for_completion=True)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904426(_, arg_0_3: int, arg_4_7: int):
    """ 12904426: Event 12904426 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, 7000, loop=True)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(920)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, 7001, wait_for_completion=True)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904466(_, arg_0_3: int, arg_4_7: int):
    """ 12904466: Event 12904466 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, 9000, loop=True)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(920)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, 9060, wait_for_completion=True)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904477(_, arg_0_3: int, arg_4_7: int):
    """ 12904477: Event 12904477 """
    DisableCharacter(arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(arg_4_7)


@RestartOnRest
def Event12904487(_, arg_0_3: int, arg_4_7: int):
    """ 12904487: Event 12904487 """
    DisableGravity(arg_4_7)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    Wait(1.0)
    ForceAnimation(arg_4_7, 2200, wait_for_completion=True)
    DisableCharacter(arg_4_7)


@RestartOnRest
def Event12904501(_, arg_0_3: int, arg_4_7: int):
    """ 12904501: Event 12904501 """
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_4_7)


def Event12904506(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_13: short,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904506: Event 12904506 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_12_13,
        part_index=arg_4_5,
        part_health=arg_16_19,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_12_13,
        part_index=arg_4_5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_20_23)
    AddSpecialEffect(arg_0_3, arg_24_27, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_28_31)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=arg_16_19, overwrite_max=True)
    AddSpecialEffect(arg_0_3, arg_28_31, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_24_27)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904540(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_13: short,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_24: uchar,
    arg_25_25: uchar,
):
    """ 12904540: Event 12904540 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_12_13,
        part_index=arg_4_5,
        part_health=arg_16_19,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_20_23)
    SetCollisionMask(arg_0_3, bit_index=arg_24_24, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_0_3, bit_index=arg_25_25, switch_type=OnOffChange.On)
    AddSpecialEffect(arg_0_3, 5667, affect_npc_part_hp=True)
    ReplanAI(arg_0_3)


def Event12904544(_, arg_0_3: int, arg_4_4: uchar):
    """ 12904544: Event 12904544 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(3.0)
    SetCollisionMask(arg_0_3, bit_index=arg_4_4, switch_type=OnOffChange.Off)


@RestartOnRest
def Event12904568(_, arg_0_3: int, arg_4_7: int):
    """ 12904568: Event 12904568 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    DisableAI(arg_0_3)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, arg_4_7)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(970)
    DestroyObject(arg_4_7)
    CreateTemporaryVFX(900257, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=-1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.a_Ambient, sound_id=124005001)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=43000000)
    EnableCharacter(arg_0_3)
    IfFramesElapsed(0, 3)
    FaceEntity(arg_0_3, PLAYER, animation=3024, wait_for_completion=False)
    IfFramesElapsed(0, 1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12904579(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 12904579: Event 12904579 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_8_11)
    DisableAI(arg_0_3)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, arg_4_7)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(970)
    DestroyObject(arg_4_7)
    CreateTemporaryVFX(900257, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=-1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.a_Ambient, sound_id=124005001)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=43000000)
    EnableCharacter(arg_0_3)
    IfFramesElapsed(0, 3)
    FaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    IfFramesElapsed(0, 1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12904584(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904584: Event 12904584 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfObjectDestroyed(-1, arg_4_7)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfConditionFalse(1, 1)
    CreatePlayLog(1008)
    DestroyObject(arg_4_7)
    CreateTemporaryVFX(900257, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=-1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.a_Ambient, sound_id=124005001)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=43000000)
    EnableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Character, dummy_id=101, short_move=True)
    IfFramesElapsed(0, 3)
    FaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    IfFramesElapsed(0, 1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12904594(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904594: Event 12904594 """
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterIsHuman(-1, PLAYER)
    IfCharacterIsType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    AICommand(arg_0_3, command_id=arg_12_15, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904595(_, arg_0_3: int, arg_4_7: int):
    """ 12904595: Event 12904595 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfCharacterIsHuman(-1, PLAYER)
    IfCharacterIsType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=3.0)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904596(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904596: Event 12904596 """
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Normal)
    IfFlagEnabled(4, arg_8_11)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfLastConditionResultTrue(4)
    AICommand(arg_0_3, command_id=arg_4_7, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12904597(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904597: Event 12904597 """
    IfThisEventSlotFlagEnabled(-1)
    IfCharacterDead(-1, arg_0_3)
    SkipLinesIfConditionFalse(2, -1)
    EnableCharacter(arg_0_3)
    End()
    DisableCharacter(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(1052)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_8_11, 0, wait_for_completion=True)
    CreateTemporaryVFX(929200, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, dummy_id=-1)
    EnableCharacter(arg_0_3)
    CreateTemporaryVFX(arg_12_15, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=203)


@RestartOnRest
def Event12904634(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float, arg_24_27: float
):
    """ 12904634: Event 12904634 """
    SetBackreadStateAlternate(arg_0_3, state=False)
    DisableCharacter(arg_0_3)
    End()
    DisableCharacter(arg_0_3)
    IfOnline(0)
    SkipLines(1)
    EndIfFlagEnabled(arg_12_15)
    EndIfFlagEnabled(arg_8_11)
    GotoIfFlagDisabled(Label.L0, arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfClient()
    AddSpecialEffect(arg_0_3, 9025, affect_npc_part_hp=False)
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    IfCharacterHasSpecialEffect(2, PLAYER, 9020)
    IfFlagEnabled(2, arg_16_19)
    IfConditionTrue(0, input_condition=2)
    Wait(arg_20_23)
    SummonNPC(SingleplayerSummonSignType.ScriptedInvasion, arg_0_3, 0, summon_flag=arg_4_7, dismissal_flag=arg_8_11)
    Wait(arg_24_27)


@RestartOnRest
def Event12904643(_, arg_0_3: int):
    """ 12904643: Event 12904643 """
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(3, arg_0_3, PLAYER, radius=8.800000190734863)
    IfHealthRatioEqual(4, arg_0_3, 1.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(5, input_condition=-1)
    IfConditionTrue(5, input_condition=3)
    IfConditionTrue(5, input_condition=4)
    IfConditionTrue(0, input_condition=5)
    IfEntityWithinDistance(6, arg_0_3, PLAYER, radius=5.800000190734863)
    SkipLinesIfConditionTrue(9, 6)
    ForceAnimation(arg_0_3, 3010)
    WaitFrames(40)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6064,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHealthNotEqual(7, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(5, 7)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=205,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(60)
    IfHealthNotEqual(8, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(1, 8)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=205,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12904677(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904677: Event 12904677 """
    IfCharacterHasSpecialEffect(0, arg_4_7, 5622)
    WaitFrames(5)
    ForceAnimation(arg_4_7, arg_8_11)
    WaitFrames(2)
    DisableCharacter(arg_0_3)
    CreatePlayLog(1096)


@RestartOnRest
def Event12904733(_, arg_0_3: int, arg_4_7: int):
    """ 12904733: Event 12904733 """
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 71, affect_npc_part_hp=False)
    CreateTemporaryVFX(850, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, dummy_id=7)
    IfObjectDestroyed(0, arg_4_7)
    RemoveSpecialEffect(PLAYER, 71)
    CreateTemporaryVFX(851, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, dummy_id=200)


@RestartOnRest
def Event12904736(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12904736: Event 12904736 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttacked(-1, PLAYER, attacker=arg_0_3)
    IfCharacterIsHuman(-2, PLAYER)
    IfCharacterIsType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfLastConditionResultFalse(6, 1)
    ForceAnimation(arg_0_3, 3007)
    WaitFrames(50)
    FaceEntity(arg_0_3, PLAYER, animation=3006, wait_for_completion=False)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    End()
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904737(_, arg_0_3: int):
    """ 12904737: Event 12904737 """
    EnableObjectInvulnerability(arg_0_3)
    IfActionButtonParamActivated(-1, action_button_id=2400900, entity=arg_0_3)
    IfObjectDamaged(-1, arg_0_3, attacker=10000)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(1132)
    ForceAnimation(arg_0_3, 1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.a_Ambient, sound_id=24011006)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6063,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(10)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(90)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6059,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(80)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=101,
        behavior_id=6062,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Restart()


def Event12904754(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904754: Event 12904754 """
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 0)
    ForceAnimation(arg_4_7, 0)
    ForceAnimation(arg_8_11, 0, wait_for_completion=True)
    IfCharacterOutsideRegion(0, arg_0_3, region=arg_12_15)
    Restart()


@RestartOnRest
def Event12904755(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904755: Event 12904755 """
    SkipLinesIfThisEventSlotFlagDisabled(2)
    EnableCharacter(arg_0_3)
    End()
    DisableCharacter(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    CreatePlayLog(1170)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_8_11, 0, wait_for_completion=True)
    CreateTemporaryVFX(929200, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, dummy_id=-1)
    EnableCharacter(arg_0_3)
    CreateTemporaryVFX(arg_12_15, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=203)
    Wait(1.0)
    AICommand(arg_0_3, command_id=10, slot=0)
    SetNest(arg_0_3, arg_16_19)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_16_19)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


def Event12904759(_, arg_0_3: int, arg_4_7: int):
    """ 12904759: Event 12904759 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(-1, input_condition=-2)
    IfCharacterIsHuman(-3, PLAYER)
    IfCharacterIsType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    EndIfLastConditionResultTrue(-2)
    CreatePlayLog(1224)
    ForceAnimation(arg_0_3, 3024, wait_for_completion=True)


def Event12904772(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904772: Event 12904772 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfObjectNotDestroyed(1, arg_4_7)
    IfCharacterIsHuman(-1, PLAYER)
    IfCharacterIsType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(arg_8_11, arg_12_15)
    AICommand(arg_8_11, command_id=100, slot=0)
    ReplanAI(arg_8_11)
    IfCharacterHasTAEEvent(0, arg_8_11, tae_event_id=100)
    AICommand(arg_8_11, command_id=-1, slot=0)
    ReplanAI(arg_8_11)
    End()


def Event12904773(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904773: Event 12904773 """
    IfFlagDisabled(1, arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    Restart()


def Event12904774(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904774: Event 12904774 """
    SkipLinesIfThisEventSlotFlagEnabled(3)
    IfFlagDisabled(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfHost(1)
    NotifyBossBattleStart()
    EnableFlag(arg_8_11)


def Event12904775(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904775: Event 12904775 """
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_8_11)
    IfCharacterIsType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    Restart()


def Event12904776(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904776: Event 12904776 """
    DeleteVFX(arg_8_11, erase_root_only=True)
    DisableCharacter(arg_0_3)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    CreatePlayLog(1260)
    StartPlayLogMeasurement(2900020, 1276, overwrite=True)
    EnableObject(arg_28_31)
    CreateVFX(arg_8_11)
    Wait(2.5)
    CreateTemporaryVFX(arg_24_27, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=205)
    WaitFrames(10)
    EnableCharacter(arg_0_3)
    ActivateMultiplayerBuffs(arg_0_3)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_12_15, slot=0)
    EnableFlag(arg_16_19)


def Event12904777(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904777: Event 12904777 """
    DisableBossMusic(arg_12_15)
    DisableBossMusic(arg_16_19)
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagDisabled(1, arg_0_3)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_12_15)
    IfCharacterHasTAEEvent(0, arg_20_23, tae_event_id=500)
    DisableBossMusic(arg_12_15)
    WaitFrames(0)
    EnableBossMusic(arg_16_19)


def Event12904778(_, arg_0_3: int, arg_4_7: int):
    """ 12904778: Event 12904778 """
    EndIfFlagEnabled(arg_4_7)
    DisableNetworkSync()
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityBeyondDistance(0, PLAYER, arg_0_3, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12904779(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904779: Event 12904779 """
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagEnabled(0, arg_0_3)
    DisableBossMusic(arg_4_7)
    DisableBossMusic(arg_8_11)
    DisableBossMusic(-1)


def Event12904780(_, arg_0_3: int):
    """ 12904780: Event 12904780 """
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    ReplanAI(arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 404)
    ReplanAI(arg_0_3)
    Restart()


def Event12904852(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904852: Event 12904852 """
    DisableCharacter(arg_4_7)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    WaitFrames(5)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        dummy_id=30,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    ForceAnimation(arg_4_7, 7000)
    ReplanAI(arg_8_11)


@RestartOnRest
def Event12904858(_, arg_0_3: int):
    """ 12904858: Event 12904858 """
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    AddSpecialEffect(arg_0_3, 5631, affect_npc_part_hp=False)
    AICommand(arg_0_3, command_id=100, slot=0)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 5630)
    AICommand(arg_0_3, command_id=110, slot=0)
    Restart()


@RestartOnRest
def Event12904859(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint):
    """ 12904859: Event 12904859 """
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    EnableRandomFlagInRange((arg_4_7, arg_8_11))
    Wait(1.0)
    Restart()


@RestartOnRest
def Event12904860(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904860: Event 12904860 """
    DisableFlag(arg_4_7)
    IfFlagEnabled(0, arg_4_7)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_8_11)
    SkipLinesIfConditionTrue(3, 1)
    DisableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SkipLines(2)
    DisableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Wait(2.0)
    EnableCharacter(arg_0_3)
    RequestAnimation(arg_0_3, 7000, loop=False, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12904861(_, arg_0_3: int, arg_4_7: int):
    """ 12904861: Event 12904861 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    EnableCharacter(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(arg_0_3, 7000)


def Event12904862(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904862: Event 12904862 """
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    Kill(arg_4_7, award_souls=False)
    Kill(arg_8_11, award_souls=False)


def Event12904863(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12904863: Event 12904863 """
    DisableAI(arg_8_11)
    DisableGravity(arg_8_11)
    DisableAI(arg_0_3)
    DisableAI(arg_4_7)
    SkipLinesIfFlagDisabled(4, arg_20_23)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_12_15)
    DisableHealthBar(arg_0_3)
    DisableHealthBar(arg_4_7)
    ReferDamageToEntity(arg_0_3, arg_8_11)
    ReferDamageToEntity(arg_4_7, arg_8_11)
    EnableBossHealthBar(arg_8_11, name=arg_24_27, slot=0)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)
    EnableFlag(arg_16_19)


def Event12904864(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904864: Event 12904864 """
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DisableCharacter(arg_12_15)
    IfFlagEnabled(0, arg_0_3)
    EnableObject(arg_4_7)
    CreateVFX(arg_8_11)
    DisableFlag(arg_0_3)
    Wait(2.5)
    CreateTemporaryVFX(arg_24_27, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Character, dummy_id=205)
    WaitFrames(10)
    EnableCharacter(arg_12_15)
    ActivateMultiplayerBuffs(arg_12_15)
    ActivateMultiplayerBuffs(arg_16_19)
    ActivateMultiplayerBuffs(arg_20_23)
    EnableAI(arg_12_15)
    EnableAI(arg_16_19)
    EnableFlag(arg_28_31)


def Event12904865(_, arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """ 12904865: Event 12904865 """
    DisableCharacter(arg_0_3)
    IfCharacterHasTAEEvent(1, arg_8_11, tae_event_id=20)
    IfHealthLessThanOrEqual(1, arg_8_11, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)


def Event12904866(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904866: Event 12904866 """
    SkipLinesIfFlagDisabled(3, arg_8_11)
    DisableCharacter(arg_4_7)
    Kill(arg_4_7, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    Kill(arg_4_7, award_souls=True)


def Event12904867(_, arg_0_3: int, arg_4_7: int):
    """ 12904867: Event 12904867 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    WaitFrames(45)
    EnableAI(arg_0_3)


def Event12904868(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904868: Event 12904868 """
    IfHealthLessThanOrEqual(0, arg_0_3, 0.75)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    DisableCharacter(arg_0_3)
    Wait(2.0)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3021)
    AICommand(arg_0_3, command_id=101, slot=0)
    ReplanAI(arg_0_3)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.5)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    DisableCharacter(arg_0_3)
    Wait(2.0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3021)
    AICommand(arg_0_3, command_id=111, slot=0)
    ReplanAI(arg_0_3)


def Event12904869(_, arg_0_3: int):
    """ 12904869: Event 12904869 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=2, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7000)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(5, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(6, arg_0_3, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(5)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=6)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7001)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(8, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(9, arg_0_3, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfLastConditionResultTrue(8)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=9)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7002)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=2, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=-1, overwrite_max=True)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904870(_, arg_0_3: int):
    """ 12904870: Event 12904870 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=3, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7005)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(5, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(6, arg_0_3, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(5)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=6)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7006)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(9, arg_0_3, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfLastConditionResultTrue(8)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=9)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7007)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=3, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=-1, overwrite_max=True)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904871(_, arg_0_3: int):
    """ 12904871: Event 12904871 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=1,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=0.5,
        body_damage_correction=0.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=1, material_sfx_id=61, material_vfx_id=61)


def Event12904872(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904872: Event 12904872 """
    DisableCharacter(arg_0_3)
    SkipLinesIfFlagDisabled(1, arg_4_7)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_8_11)
    Wait(2.5999999046325684)
    CreateTemporaryVFX(arg_12_15, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=205)
    WaitFrames(10)
    EnableCharacter(arg_0_3)


def Event12904877(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904877: Event 12904877 """
    DisableAI(arg_0_3)
    DisableAI(arg_12_15)
    DisableAI(arg_28_31)
    DisableObject(arg_24_27)
    DeleteVFX(arg_8_11, erase_root_only=True)
    SkipLinesIfFlagDisabled(2, arg_16_19)
    EnableObject(arg_24_27)
    CreateVFX(arg_8_11)
    SkipLinesIfFlagDisabled(4, arg_20_23)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_28_31)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)
    SkipLinesIfFlagEnabled(2, arg_16_19)
    EnableObject(arg_24_27)
    CreateVFX(arg_8_11)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(arg_0_3, 7501, affect_npc_part_hp=True)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=304001, slot=0)
    DisableHealthBar(arg_0_3)
    EnableAI(arg_12_15)
    EnableBossHealthBar(arg_12_15, name=304002, slot=1)
    DisableHealthBar(arg_12_15)
    EnableAI(arg_28_31)
    EnableBossHealthBar(arg_28_31, name=304003, slot=2)
    DisableHealthBar(arg_28_31)
    EnableFlag(arg_16_19)


def Event12904878(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904878: Event 12904878 """
    AwaitFlagEnabled(arg_12_15)
    IfFlagDisabled(1, arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    Restart()


def Event12904879(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904879: Event 12904879 """
    SkipLinesIfThisEventSlotFlagEnabled(3)
    IfFlagDisabled(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfHost(1)
    NotifyBossBattleStart()
    EnableFlag(arg_8_11)


def Event12904880(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904880: Event 12904880 """
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_8_11)
    IfCharacterIsType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    Restart()


def Event12904881(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12904881: Event 12904881 """
    DisableAI(arg_0_3)
    DisableObject(arg_24_27)
    DeleteVFX(arg_8_11, erase_root_only=True)
    SkipLinesIfFlagDisabled(2, arg_16_19)
    EnableObject(arg_24_27)
    CreateVFX(arg_8_11)
    SkipLinesIfFlagDisabled(2, arg_20_23)
    DisableCharacter(arg_0_3)
    End()
    ForceAnimation(arg_0_3, 7020, loop=True, skip_transition=True)
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, 7020, loop=True, skip_transition=True)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_20_23, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)
    SkipLinesIfFlagEnabled(2, arg_16_19)
    EnableObject(arg_24_27)
    CreateVFX(arg_8_11)
    FaceEntity(arg_0_3, PLAYER, animation=7021, wait_for_completion=False)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(arg_0_3, 7501, affect_npc_part_hp=True)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_12_15, slot=0)
    DisableHealthBar(arg_0_3)
    EnableFlag(arg_16_19)


def Event12904882(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904882: Event 12904882 """
    DisableBossMusic(arg_12_15)
    DisableBossMusic(arg_16_19)
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagDisabled(1, arg_0_3)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_12_15)
    IfCharacterHasTAEEvent(0, arg_20_23, tae_event_id=500)
    DisableBossMusic(arg_12_15)
    WaitFrames(0)
    EnableBossMusic(arg_16_19)


def Event12904883(_, arg_0_3: int, arg_4_7: int):
    """ 12904883: Event 12904883 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfEntityBeyondDistance(2, PLAYER, arg_0_3, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12904886(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904886: Event 12904886 """
    EndIfFlagEnabled(arg_0_3)
    DisableNetworkSync()
    IfFlagEnabled(0, arg_0_3)
    DisableBossMusic(arg_4_7)
    DisableBossMusic(arg_8_11)
    DisableBossMusic(-1)


def Event12904887(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float):
    """ 12904887: Event 12904887 """
    DisableCharacter(arg_0_3)
    IfFlagEnabled(1, arg_8_11)
    IfHealthLessThanOrEqual(1, arg_4_7, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Character, dummy_id=-1, short_move=True)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_16_19, slot=1)
    CreateTemporaryVFX(929203, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=203)


@RestartOnRest
def Event12904888(_, arg_0_3: int):
    """ 12904888: Event 12904888 """
    IfHealthLessThan(0, arg_0_3, 0.5)
    AICommand(arg_0_3, command_id=1, slot=1)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    AICommand(arg_0_3, command_id=-1, slot=1)


def Event12904890(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904890: Event 12904890 """
    DisableObject(arg_28_31)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DisableCharacter(arg_0_3)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableObject(arg_28_31)
    CreateVFX(arg_8_11)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=205)
    IfValueComparison(0, ComparisonType.Equal, left=arg_24_27, right=arg_24_27)
    WaitFrames(10)
    EnableCharacter(arg_0_3)
    ActivateMultiplayerBuffs(arg_0_3)
    ForceAnimation(arg_0_3, 7010, wait_for_completion=True)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_12_15, slot=0)
    EnableFlag(arg_16_19)


def Event12904891(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904891: Event 12904891 """
    DisableObject(arg_28_31)
    DeleteVFX(arg_8_11, erase_root_only=True)
    DisableCharacter(arg_0_3)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableObject(arg_28_31)
    CreateVFX(arg_8_11)
    Wait(2.5)
    CreateTemporaryVFX(929227, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=205)
    IfValueComparison(0, ComparisonType.Equal, left=arg_24_27, right=arg_24_27)
    WaitFrames(10)
    EnableCharacter(arg_0_3)
    ActivateMultiplayerBuffs(arg_0_3)
    ForceAnimation(arg_0_3, 7010, wait_for_completion=True)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_12_15, slot=0)
    EnableFlag(arg_16_19)


def Event12904892(_, arg_0_3: int, arg_4_7: int):
    """ 12904892: Event 12904892 """
    DisableSoundEvent(arg_0_3)
    DisableSoundEvent(arg_4_7)


def Event12904893(_, arg_0_3: int):
    """ 12904893: Event 12904893 """
    IfHealthLessThan(0, arg_0_3, 0.5)
    AICommand(arg_0_3, command_id=1, slot=1)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AICommand(arg_0_3, command_id=-1, slot=1)


def Event12904894(_, arg_0_3: int, arg_4_7: int):
    """ 12904894: Event 12904894 """
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    EnableFlag(arg_4_7)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)
    DisableFlag(arg_4_7)
    Restart()


def Event12904895(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12904895: Event 12904895 """
    DeleteVFX(arg_0_3, erase_root_only=False)
    DeleteVFX(arg_4_7, erase_root_only=False)
    DeleteVFX(arg_8_11, erase_root_only=False)
    IfCharacterInsideRegion(0, PLAYER, region=arg_12_15)
    CreateVFX(arg_0_3)
    CreateVFX(arg_4_7)
    CreateVFX(arg_8_11)


def Event12904896(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_21: short,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904896: Event 12904896 """
    EndIfFlagEnabled(arg_28_31)
    IfFlagEnabled(1, arg_24_27)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5021)
    IfCharacterPartHealthLessThanOrEqual(3, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfCharacterDoesNotHaveSpecialEffect(3, arg_0_3, 5021)
    IfFlagEnabled(4, arg_28_31)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    EndIfLastConditionResultTrue(4)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=50,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    AddSpecialEffect(arg_0_3, 5021, affect_npc_part_hp=True)
    AddSpecialEffect(arg_0_3, arg_12_15, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_16_19)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7003)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AddSpecialEffect(arg_0_3, 5911, affect_npc_part_hp=True)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    RemoveSpecialEffect(arg_0_3, 5021)
    AddSpecialEffect(arg_0_3, arg_16_19, affect_npc_part_hp=False)
    RemoveSpecialEffect(arg_0_3, arg_12_15)
    WaitFrames(10)
    Restart()


def Event12904897(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_21: short,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904897: Event 12904897 """
    EndIfFlagEnabled(arg_28_31)
    IfFlagEnabled(1, arg_24_27)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5021)
    IfCharacterPartHealthLessThanOrEqual(3, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfCharacterDoesNotHaveSpecialEffect(3, arg_0_3, 5021)
    IfFlagEnabled(4, arg_28_31)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    EndIfLastConditionResultTrue(4)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=50,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_20_21,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=66, material_vfx_id=66)
    AddSpecialEffect(arg_0_3, 5021, affect_npc_part_hp=True)
    AddSpecialEffect(arg_0_3, arg_12_15, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_16_19)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7000)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AddSpecialEffect(arg_0_3, 5911, affect_npc_part_hp=True)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    RemoveSpecialEffect(arg_0_3, 5021)
    AddSpecialEffect(arg_0_3, arg_16_19, affect_npc_part_hp=False)
    RemoveSpecialEffect(arg_0_3, arg_12_15)
    WaitFrames(10)
    Restart()


def Event12904898(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904898: Event 12904898 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904899(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904899: Event 12904899 """
    EndIfFlagEnabled(arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=130,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=130, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12904900(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904900: Event 12904900 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904901(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904901: Event 12904901 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904902(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904902: Event 12904902 """
    EndIfFlagEnabled(arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=150, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12904903(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904903: Event 12904903 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904904(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904904: Event 12904904 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904905(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904905: Event 12904905 """
    EndIfFlagEnabled(arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=150, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12904906(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904906: Event 12904906 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904907(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904907: Event 12904907 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904908(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904908: Event 12904908 """
    EndIfFlagEnabled(arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=200, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12904909(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904909: Event 12904909 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904910(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904910: Event 12904910 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12904913(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904913: Event 12904913 """
    EndIfFlagEnabled(arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=200, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12904911(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12904911: Event 12904911 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=65, material_vfx_id=65)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12904912(_, arg_0_3: int):
    """ 12904912: Event 12904912 """
    IfHealthLessThan(0, arg_0_3, 0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 7010)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfHealthLessThan(0, arg_0_3, 0.33000001311302185)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 7011)
    AICommand(arg_0_3, command_id=101, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


def Event12904914(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar, arg_10_10: uchar, arg_12_15: int):
    """ 12904914: Event 12904914 """
    IfCharacterHasSpecialEffect(1, arg_12_15, arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_12_15, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(arg_12_15, bit_index=arg_8_8, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_12_15, bit_index=arg_9_9, switch_type=OnOffChange.On)
    SetDisplayMask(arg_12_15, bit_index=arg_10_10, switch_type=OnOffChange.On)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_12_15, arg_0_3)
    IfCharacterHasSpecialEffect(2, arg_12_15, arg_4_7)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(arg_12_15, bit_index=arg_9_9, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_12_15, bit_index=arg_8_8, switch_type=OnOffChange.On)
    WaitFrames(10)
    Restart()


def Event12904915(_, arg_0_3: int):
    """ 12904915: Event 12904915 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 482)
    ChangeCharacterCloth(arg_0_3, 15, state_id=2)


def Event12904916(_, arg_0_3: int):
    """ 12904916: Event 12904916 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 420)
    WaitFrames(10)
    RemoveSpecialEffect(arg_0_3, 420)
    Restart()


def Event12904917(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12904917: Event 12904917 """
    IfFlagEnabled(1, arg_16_19)
    IfCharacterBackreadEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_20_23,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=1,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    IfHealthLessThanOrEqual(2, arg_20_23, 0.0)
    IfCharacterPartHealthLessThanOrEqual(3, arg_20_23, npc_part_id=arg_4_7, value=0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    IfCharacterHasSpecialEffect(7, arg_20_23, 420)
    SkipLinesIfConditionFalse(1, 7)
    AddSpecialEffect(arg_20_23, arg_12_15, affect_npc_part_hp=True)
    WaitFrames(10)
    Restart()


def Event12904918(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12904918: Event 12904918 """
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfFlagEnabled(0, arg_12_15)
    IfCharacterHasSpecialEffect(1, arg_16_19, arg_0_3)
    IfCharacterHasSpecialEffect(1, arg_16_19, 421)
    IfCharacterPartHealthLessThanOrEqual(1, arg_16_19, npc_part_id=arg_8_11, value=0)
    IfCharacterHasSpecialEffect(2, arg_16_19, arg_0_3)
    IfCharacterHasSpecialEffect(2, arg_16_19, 421)
    IfCharacterPartHealthComparison(
        2, arg_16_19, npc_part_id=arg_8_11, comparison_type=ComparisonType.GreaterThan, value=0
    )
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfLastConditionResultTrue(2, 2)
    ForceAnimation(arg_16_19, arg_4_7, wait_for_completion=True)
    SkipLines(1)
    AddSpecialEffect(arg_16_19, arg_0_3, affect_npc_part_hp=True)
    Restart()


@RestartOnRest
def Event12904919(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904919: Event 12904919 """
    IfFlagEnabled(-1, 92905320)
    IfFlagEnabled(-1, 92905324)
    IfFlagEnabled(-1, 92905325)
    IfFlagEnabled(-1, 92905326)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12904979(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12904979: Event 12904979 """
    IfFlagEnabled(-1, 92905321)
    IfFlagEnabled(-1, 92905327)
    IfFlagEnabled(-1, 92905328)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905000(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905000: Event 12905000 """
    IfFlagEnabled(-1, 92905322)
    IfFlagEnabled(-1, 92905329)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905013(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905013: Event 12905013 """
    IfFlagEnabled(-1, 92905323)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905026(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905026: Event 12905026 """
    EndIfFlagRangeAllDisabled((92905320, 92905329))
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905042(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905042: Event 12905042 """
    IfFlagEnabled(-1, 92905320)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905097(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905097: Event 12905097 """
    IfFlagEnabled(-1, 92905321)
    IfFlagEnabled(-1, 92905324)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905108(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905108: Event 12905108 """
    IfFlagEnabled(-1, 92905322)
    IfFlagEnabled(-1, 92905325)
    IfFlagEnabled(-1, 92905327)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905119(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905119: Event 12905119 """
    IfFlagEnabled(-1, 92905323)
    IfFlagEnabled(-1, 92905326)
    IfFlagEnabled(-1, 92905328)
    IfFlagEnabled(-1, 92905329)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905130(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905130: Event 12905130 """
    EndIfFlagRangeAllDisabled((92905320, 92905329))
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableCharacter(arg_24_27)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableBackread(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905147(_, arg_0_3: int, arg_4_7: int):
    """ 12905147: Event 12905147 """
    DisableHealthBar(arg_0_3)
    EnableImmortality(arg_0_3)
    AddSpecialEffect(arg_0_3, 5626, affect_npc_part_hp=False)
    IfFlagEnabled(0, arg_4_7)
    WaitRandomFrames(min_frames=0, max_frames=50)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=True)
    End()


@RestartOnRest
def Event12905178(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905178: Event 12905178 """
    IfCharacterBackreadEnabled(-1, arg_0_3)
    IfCharacterBackreadEnabled(-1, arg_4_7)
    IfCharacterBackreadEnabled(-1, arg_8_11)
    IfCharacterBackreadEnabled(-1, arg_12_15)
    IfCharacterBackreadEnabled(-1, arg_16_19)
    IfCharacterBackreadEnabled(-1, arg_20_23)
    IfCharacterBackreadEnabled(-1, arg_24_27)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_0_3, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_4_7, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_8_11, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_12_15, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_16_19, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_20_23, 5913, affect_npc_part_hp=False)
    AddSpecialEffect(arg_24_27, 5913, affect_npc_part_hp=False)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_4_7, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_8_11, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_12_15, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_16_19, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_20_23, radius=7.0)
    IfEntityWithinDistance(-2, PLAYER, arg_24_27, radius=7.0)
    RestartIfConditionFalse(-2)
    RemoveSpecialEffect(arg_0_3, 5913)
    RemoveSpecialEffect(arg_4_7, 5913)
    RemoveSpecialEffect(arg_8_11, 5913)
    RemoveSpecialEffect(arg_12_15, 5913)
    RemoveSpecialEffect(arg_16_19, 5913)
    RemoveSpecialEffect(arg_20_23, 5913)
    RemoveSpecialEffect(arg_24_27, 5913)
    AddSpecialEffect(arg_0_3, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_4_7, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_8_11, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_12_15, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_16_19, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_20_23, 5625, affect_npc_part_hp=False)
    AddSpecialEffect(arg_24_27, 5625, affect_npc_part_hp=False)
    EnableHealthBar(arg_0_3)
    EnableHealthBar(arg_4_7)
    EnableHealthBar(arg_8_11)
    EnableHealthBar(arg_12_15)
    EnableHealthBar(arg_16_19)
    EnableHealthBar(arg_20_23)
    EnableHealthBar(arg_24_27)
    Wait(1.0)
    IfCharacterHasSpecialEffect(-3, arg_0_3, 5913)
    IfValueComparison(-3, ComparisonType.Equal, left=arg_0_3, right=0)
    IfCharacterHasSpecialEffect(-4, arg_4_7, 5913)
    IfValueComparison(-4, ComparisonType.Equal, left=arg_4_7, right=0)
    IfCharacterHasSpecialEffect(-5, arg_8_11, 5913)
    IfValueComparison(-5, ComparisonType.Equal, left=arg_8_11, right=0)
    IfCharacterHasSpecialEffect(-6, arg_12_15, 5913)
    IfValueComparison(-6, ComparisonType.Equal, left=arg_12_15, right=0)
    IfCharacterHasSpecialEffect(-7, arg_16_19, 5913)
    IfValueComparison(-7, ComparisonType.Equal, left=arg_16_19, right=0)
    IfCharacterHasSpecialEffect(-8, arg_20_23, 5913)
    IfValueComparison(-8, ComparisonType.Equal, left=arg_20_23, right=0)
    IfCharacterHasSpecialEffect(-8, arg_24_27, 5913)
    IfValueComparison(-8, ComparisonType.Equal, left=arg_24_27, right=0)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(1, input_condition=-5)
    IfConditionTrue(1, input_condition=-6)
    IfConditionTrue(1, input_condition=-7)
    IfConditionTrue(1, input_condition=-8)
    IfConditionTrue(1, input_condition=-9)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_28_31)
    End()


@RestartOnRest
def Event12905188(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905188: Event 12905188 """
    IfFlagEnabled(-1, 92905330)
    IfFlagEnabled(-1, 92905332)
    IfFlagEnabled(-1, 92905333)
    IfFlagEnabled(-1, 92905334)
    IfFlagRangeAnyEnabled(-1, (92905385, 92905389))
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
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
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905190(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905190: Event 12905190 """
    IfFlagEnabled(-1, 92905331)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905192(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905192: Event 12905192 """
    SkipLinesIfFlagRangeAnyEnabled(1, (92905385, 92905389))
    EndIfFlagRangeAllDisabled((92905330, 92905334))
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905195():
    """ 12905195: Event 12905195 """
    End()


@RestartOnRest
def Event12905198(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905198: Event 12905198 """
    IfFlagEnabled(-1, 92905331)
    IfFlagEnabled(-1, 92905333)
    IfFlagEnabled(-1, 92905334)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905201(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905201: Event 12905201 """
    IfFlagDisabled(1, 92905331)
    IfFlagDisabled(1, 92905333)
    IfFlagDisabled(1, 92905334)
    EndIfConditionTrue(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableObject(arg_16_19)
    DisableObjectActivation(arg_16_19, obj_act_id=-1)
    DisableTreasure(arg_16_19)
    DisableObject(arg_20_23)
    DisableObjectActivation(arg_20_23, obj_act_id=-1)
    DisableTreasure(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905209(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905209: Event 12905209 """
    IfFlagEnabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905210(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905210: Event 12905210 """
    IfFlagDisabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905211(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905211: Event 12905211 """
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905212(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905212: Event 12905212 """
    IfFlagEnabled(1, 92905340)
    IfOnline(1)
    EndIfConditionTrue(1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905221(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905221: Event 12905221 """
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905226(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12905226: Event 12905226 """
    IfFlagDisabled(-1, 92905340)
    EndIfConditionTrue(-1)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    DisableCharacter(arg_16_19)
    DisableCharacter(arg_20_23)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DisableBackread(arg_8_11)
    DisableBackread(arg_12_15)
    DisableBackread(arg_16_19)
    DisableBackread(arg_20_23)
    DisableObject(arg_24_27)
    DisableObjectActivation(arg_24_27, obj_act_id=-1)
    DisableTreasure(arg_24_27)
    DisableObject(arg_28_31)
    DisableObjectActivation(arg_28_31, obj_act_id=-1)
    DisableTreasure(arg_28_31)
    End()


@RestartOnRest
def Event12905232(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905232: Event 12905232 """
    IfFlagRangeAllDisabled(0, (arg_0_3, arg_4_7))
    DisableCharacter(arg_8_11)


@RestartOnRest
def Event12905233(_, arg_0_3: int, arg_4_7: int):
    """ 12905233: Event 12905233 """
    DisableAnimations(arg_0_3)
    DisableAnimations(arg_4_7)
    DisableGravity(arg_0_3)
    DisableGravity(arg_4_7)
    DisableCharacterCollision(arg_0_3)
    DisableCharacterCollision(arg_4_7)


@RestartOnRest
def Event12905235(_, arg_0_3: int, arg_4_7: int):
    """ 12905235: Event 12905235 """
    ForceAnimation(arg_0_3, 7001, loop=True)
    ForceAnimation(arg_4_7, 7002, loop=True)
    IfFlagEnabled(0, 12907224)
    ForceAnimation(arg_0_3, 7005)
    ForceAnimation(arg_4_7, 7006)
    WaitFrames(29)
    ForceAnimation(arg_0_3, 7003, loop=True)
    ForceAnimation(arg_4_7, 7004, loop=True)
    IfFlagDisabled(0, 12907224)
    ForceAnimation(arg_0_3, 7007)
    ForceAnimation(arg_4_7, 7008)
    WaitFrames(28)
    Restart()


@RestartOnRest
def Event12905237(_, arg_0_3: int, arg_4_7: int):
    """ 12905237: Event 12905237 """
    WaitFrames(12)
    IfPlayerHasGood(1, 4111, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    SetDisplayMask(arg_0_3, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=10, switch_type=OnOffChange.On)
    IfPlayerHasGood(2, 4112, including_box=False)
    SkipLinesIfConditionTrue(2, 2)
    SetDisplayMask(arg_0_3, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=13, switch_type=OnOffChange.On)
    IfPlayerHasGood(3, 4113, including_box=False)
    SkipLinesIfConditionTrue(1, 3)
    SetDisplayMask(arg_0_3, bit_index=3, switch_type=OnOffChange.On)
    IfPlayerHasGood(4, 4114, including_box=False)
    SkipLinesIfConditionTrue(1, 4)
    SetDisplayMask(arg_4_7, bit_index=0, switch_type=OnOffChange.On)
    IfPlayerHasGood(5, 4115, including_box=False)
    SkipLinesIfConditionTrue(2, 5)
    SetDisplayMask(arg_4_7, bit_index=1, switch_type=OnOffChange.On)
    SetDisplayMask(arg_4_7, bit_index=12, switch_type=OnOffChange.On)
    IfPlayerHasGood(6, 4116, including_box=False)
    SkipLinesIfConditionTrue(2, 6)
    SetDisplayMask(arg_4_7, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(arg_4_7, bit_index=11, switch_type=OnOffChange.On)
    IfPlayerHasGood(7, 4117, including_box=False)
    SkipLinesIfConditionTrue(1, 7)
    SetDisplayMask(arg_4_7, bit_index=3, switch_type=OnOffChange.On)


@RestartOnRest
def Event12905239(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905239: Event 12905239 """
    IfFlagRangeAnyEnabled(0, (arg_0_3, arg_4_7))
    DisableCharacter(arg_8_11)


@RestartOnRest
def Event12905243(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905243: Event 12905243 """
    IfFlagRangeAllDisabled(0, (arg_0_3, arg_4_7))
    DisableObject(arg_8_11)
    DisableTreasure(arg_8_11)


@RestartOnRest
def Event12905244(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905244: Event 12905244 """
    IfFlagRangeAnyEnabled(0, (arg_0_3, arg_4_7))
    DisableObject(arg_8_11)
    DisableTreasure(arg_8_11)


def Event12905245(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905245: Event 12905245 """
    SkipLinesIfFlagDisabled(2, arg_4_7)
    DisableMapPiece(arg_0_3)
    SkipLines(1)
    DisableMapPiece(arg_8_11)
    End()


def Event12905271(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905271: Event 12905271 """
    SkipLinesIfFlagDisabled(2, arg_4_7)
    DisableMapCollision(arg_0_3)
    SkipLines(1)
    DisableMapCollision(arg_8_11)
    End()


def Event12905302(_, arg_0_3: int):
    """ 12905302: Event 12905302 """
    DisableMapCollision(arg_0_3)
    SkipLines(1)


def Event12905303(_, arg_0_3: int, arg_4_7: int):
    """ 12905303: Event 12905303 """
    IfPlayerMovingOnCollision(0, arg_4_7)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12905314(_, arg_0_3: int, arg_4_7: int):
    """ 12905314: Event 12905314 """
    WaitFrames(1)
    End()
    IfFlagEnabled(0, arg_4_7)
    IfHealthRatioEqual(0, arg_0_3, 1.0)
    WaitFrames(1)
    End()


@RestartOnRest
def Event12905337(_, arg_0_3: int, arg_4_7: int):
    """ 12905337: Event 12905337 """
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    SkipLinesIfConditionFalse(3, 1)
    DisableAI(arg_4_7)
    ForceAnimation(arg_4_7, 3002, wait_for_completion=True)
    End()
    Move(
        arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, dummy_id=6, set_draw_parent=arg_0_3
    )
    Restart()


@RestartOnRest
def Event12905347(_, arg_0_3: int, arg_4_7: int):
    """ 12905347: Event 12905347 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5401)
    AICommand(arg_4_7, command_id=100, slot=0)
    IfCharacterHasSpecialEffect(0, arg_0_3, 5400)
    AICommand(arg_4_7, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12905357(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12905357: Event 12905357 """
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    SetAIParamID(arg_0_3, arg_16_19)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfHealthNotEqual(-1, arg_0_3, 1.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    SetAIParamID(arg_0_3, arg_20_23)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=5.0)
    SkipLinesIfConditionTrue(1, 1)
    ForceAnimation(arg_0_3, arg_12_15)


@RestartOnRest
def Event12905369(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12905369: Event 12905369 """
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfHealthNotEqual(-1, arg_0_3, 1.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)


@RestartOnRest
def Event12905387(_, arg_0_3: int):
    """ 12905387: Event 12905387 """
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=2.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7001)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12905396(_, arg_0_3: int):
    """ 12905396: Event 12905396 """
    SkipLinesIfThisEventSlotFlagDisabled(1)
    End()
    ForceAnimation(arg_0_3, 7000, loop=True)
    SetAIParamID(arg_0_3, 218085)
    AddSpecialEffect(arg_0_3, 5629, affect_npc_part_hp=False)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=2.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7001)
    SetAIParamID(arg_0_3, 218080)
    RemoveSpecialEffect(arg_0_3, 5629)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12905401(_, arg_0_3: int, arg_4_7: int):
    """ 12905401: Event 12905401 """
    IfObjectActivated(0, obj_act_id=arg_0_3)
    WaitFrames(45)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event12905402(_, arg_0_3: int, arg_4_7: int):
    """ 12905402: Event 12905402 """
    IfObjectDamaged(-1, arg_0_3, attacker=10000)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(45)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event12905403(_, arg_0_3: int, arg_4_7: int):
    """ 12905403: Event 12905403 """
    IfFlagEnabled(0, arg_0_3)
    Wait(8.0)
    EnableFlag(arg_4_7)


def Event12905404(_, arg_0_3: int, arg_4_7: int):
    """ 12905404: Event 12905404 """
    IfObjectActivated(0, obj_act_id=arg_0_3)
    CreatePlayLog(0)
    WaitFrames(100)
    EnableFlag(arg_4_7)


def Event12905406(_, arg_0_3: int, arg_4_7: int):
    """ 12905406: Event 12905406 """
    DisableCharacter(arg_0_3)
    End()
    IfPlayerInsightAmountGreaterThanOrEqual(1, 10)
    IfCharacterIsHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 6200, wait_for_completion=True)
    EnableFlag(arg_4_7)


def Event12905407(_, arg_0_3: int, arg_4_7: int):
    """ 12905407: Event 12905407 """
    End()
    IfFlagEnabled(1, arg_4_7)
    IfPlayerInsightAmountLessThanOrEqual(1, 8)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(arg_0_3, award_souls=False)


@RestartOnRest
def Event12906400(_, arg_0_3: int):
    """ 12906400: Event 12906400 """
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.NoType)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfObjectHealthValueComparison(-1, arg_0_3, ComparisonType.LessThan, 999)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfLastConditionResultTrue(7, -2)
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    WaitFrames(10)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(45)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6053,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    End()
    CreatePlayLog(1462)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6150,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6151,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6152,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6153,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6154,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6155,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6156,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
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
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6000,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=200,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@RestartOnRest
def Event12906500(_, arg_0_3: int, arg_4_7: int):
    """ 12906500: Event 12906500 """
    EnableImmortality(arg_0_3)
    IfCharacterDead(0, arg_4_7)
    DisableImmortality(arg_0_3)
    Kill(arg_0_3, award_souls=True)


def Event12906534(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906534: Event 12906534 """
    DisableObject(arg_8_11)
    DisableObject(arg_16_19)
    EnableObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_0_3, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(45)
    RemoveObjectFlag(arg_4_7)
    DisableObject(arg_0_3)
    EnableObject(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_8_11, 0)
    WaitFrames(10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
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
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=5.599999904632568,
        repetition_time=0.0,
    )
    Wait(5.599999904632568)
    RemoveObjectFlag(arg_12_15)
    DisableObject(arg_8_11)
    EnableObject(arg_16_19)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_16_19, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
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
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(arg_20_23)
    DisableObject(arg_16_19)
    Restart()


def Event12906537(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906537: Event 12906537 """
    DisableObject(arg_8_11)
    DisableObject(arg_16_19)
    EnableObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_0_3, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(45)
    RemoveObjectFlag(arg_4_7)
    DisableObject(arg_0_3)
    EnableObject(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_8_11, 0)
    WaitFrames(10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
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
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(6.0)
    RemoveObjectFlag(arg_12_15)
    DisableObject(arg_8_11)
    EnableObject(arg_16_19)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_16_19, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
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
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(arg_20_23)
    DisableObject(arg_16_19)
    Restart()


def Event12906540(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906540: Event 12906540 """
    DisableObject(arg_8_11)
    DisableObject(arg_16_19)
    EnableObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    IfCharacterInsideRegion(0, PLAYER, region=arg_28_31)
    ForceAnimation(arg_0_3, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        dummy_id=101,
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
        arg_4_7,
        arg_0_3,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    WaitFrames(45)
    RemoveObjectFlag(arg_4_7)
    DisableObject(arg_0_3)
    EnableObject(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_8_11, 0)
    WaitFrames(10)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_12_15,
        arg_8_11,
        dummy_id=101,
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
        arg_12_15,
        arg_8_11,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=4.300000190734863,
        repetition_time=0.0,
    )
    Wait(12.0)
    RemoveObjectFlag(arg_12_15)
    DisableObject(arg_8_11)
    EnableObject(arg_16_19)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000004)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000005)
    ForceAnimation(arg_16_19, 10)
    WaitFrames(5)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_20_23,
        arg_16_19,
        dummy_id=101,
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
        arg_20_23,
        arg_16_19,
        dummy_id=101,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=2.5,
        repetition_time=0.0,
    )
    Wait(2.5)
    RemoveObjectFlag(arg_20_23)
    DisableObject(arg_16_19)
    End()


def Event12906541(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906541: Event 12906541 """
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    EnableObject(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterDead(-1, arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_20_23, 3000, wait_for_completion=True)
    DisableObject(arg_0_3)
    EnableObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_4_7, 20)
    CreateObjectVFX(900260, obj=arg_4_7, dummy_id=100)
    WaitFrames(30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
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
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=14.800000190734863,
        repetition_time=0.0,
    )
    WaitFrames(370)
    RemoveObjectFlag(arg_28_31)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableObject(arg_8_11)
    ForceAnimation(arg_8_11, 100)
    DestroyObject(arg_8_11)
    DisableObject(arg_4_7)


def Event12906543(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906543: Event 12906543 """
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    EnableObject(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterDead(-1, arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_20_23, 3000, wait_for_completion=True)
    DisableObject(arg_0_3)
    EnableObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_4_7, 30)
    CreateObjectVFX(900260, obj=arg_4_7, dummy_id=100)
    WaitFrames(30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
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
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=13.699999809265137,
        repetition_time=0.0,
    )
    WaitFrames(270)
    RemoveObjectFlag(arg_28_31)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableObject(arg_8_11)
    ForceAnimation(arg_8_11, 100)
    DestroyObject(arg_8_11)
    DisableObject(arg_4_7)


def Event12906545(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906545: Event 12906545 """
    DisableObject(arg_4_7)
    DisableObject(arg_8_11)
    EnableObject(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterDead(-1, arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_20_23, 3000, wait_for_completion=True)
    DisableObject(arg_0_3)
    EnableObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000002)
    PlaySoundEffect(anchor_entity=arg_24_27, sound_type=SoundType.a_Ambient, sound_id=290000003)
    ForceAnimation(arg_4_7, 40)
    CreateObjectVFX(900260, obj=arg_4_7, dummy_id=100)
    WaitFrames(30)
    SkipLinesIfFlagDisabled(2, 92905100)
    IfFlagEnabled(0, 92905100)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6140,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905101)
    IfFlagEnabled(0, 92905101)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6141,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905102)
    IfFlagEnabled(0, 92905102)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6142,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905103)
    IfFlagEnabled(0, 92905103)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6143,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905104)
    IfFlagEnabled(0, 92905104)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6144,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905105)
    IfFlagEnabled(0, 92905105)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6145,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905106)
    IfFlagEnabled(0, 92905106)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=6146,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    SkipLinesIfFlagDisabled(2, 92905107)
    IfFlagEnabled(0, 92905107)
    CreateHazard(
        arg_28_31,
        arg_4_7,
        dummy_id=100,
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
        arg_28_31,
        arg_4_7,
        dummy_id=100,
        behavior_param_id=5110,
        target_type=DamageTargetType.Character,
        radius=2.0999999046325684,
        life=12.800000190734863,
        repetition_time=0.0,
    )
    WaitFrames(270)
    RemoveObjectFlag(arg_28_31)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableObject(arg_8_11)
    ForceAnimation(arg_8_11, 100)
    DestroyObject(arg_8_11)
    DisableObject(arg_4_7)


@RestartOnRest
def Event12906548(_, arg_0_3: int, arg_4_7: int):
    """ 12906548: Event 12906548 """
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfEntityWithinDistance(1, arg_0_3, arg_4_7, radius=25.0)
    IfCharacterAlive(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=200, slot=1)
    IfCharacterHasTAEEvent(0, arg_4_7, tae_event_id=20)
    AddSpecialEffect(arg_4_7, 5645, affect_npc_part_hp=False)
    AICommand(arg_4_7, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event12906567(_, arg_0_3: int, arg_4_7: int):
    """ 12906567: Event 12906567 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5645)
    AddSpecialEffect(arg_0_3, arg_4_7, affect_npc_part_hp=False)
    IfCharacterDoesNotHaveSpecialEffect(0, arg_0_3, 5645)
    RemoveSpecialEffect(arg_0_3, arg_4_7)
    Restart()


@RestartOnRest
def Event12906586(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906586: Event 12906586 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_12_15)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(4, arg_0_3, 4740)
    IfAttackedWithDamageType(5, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=5)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=4)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=-2)
    SetAIParamID(arg_0_3, arg_16_19)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfHasAIStatus(6, arg_0_3, ai_status=AIStatusType.Normal)
    IfHasAIStatus(7, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(8, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(9, arg_0_3, 4740)
    IfAttackedWithDamageType(10, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(-3, input_condition=10)
    IfConditionTrue(-4, input_condition=7)
    IfConditionTrue(-4, input_condition=8)
    IfConditionTrue(-4, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=10)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=-4)
    Wait(3.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_24_27)

    # --- 1 --- #
    DefineLabel(1)
    SetAIParamID(arg_0_3, arg_20_23)


@RestartOnRest
def Event12906648(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12906648: Event 12906648 """
    IfCharacterBackreadEnabled(0, arg_4_7)
    DisableAI(arg_4_7)
    DisableGravity(arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=60)
    Move(arg_4_7, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableGravity(arg_4_7)
    EnableAI(arg_4_7)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12906654(_, arg_0_3: int, arg_4_7: int):
    """ 12906654: Event 12906654 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=10, slot=0)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ReplanAI(arg_0_3)
    Wait(3.0)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=32,
        behavior_id=210200599,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.a_Ambient, sound_id=225000000)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    ForceAnimation(arg_0_3, 3010, wait_for_completion=True)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.a_Ambient, sound_id=225000000)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=32,
        behavior_id=210200599,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, 7004, wait_for_completion=True)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12906655(_, arg_0_3: int, arg_4_7: int):
    """ 12906655: Event 12906655 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12906656(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906656: Event 12906656 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHealthRatioEqual(1, arg_0_3, 1.0)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    IfEntityWithinDistance(3, arg_0_3, PLAYER, radius=5.0)
    SkipLinesIfConditionTrue(23, 3)
    Move(
        arg_8_11,
        destination=PLAYER,
        destination_type=CoordEntityType.Character,
        dummy_id=236,
        copy_draw_parent=PLAYER,
    )
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.c_CharacterMotion, sound_id=arg_4_7)
    ForceAnimation(arg_0_3, 3020)
    WaitFrames(40)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6064,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHealthNotEqual(4, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(17, 4)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(90)
    IfHealthNotEqual(5, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(13, 5)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6054,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(90)
    IfHealthNotEqual(6, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(9, 6)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(60)
    IfHealthNotEqual(7, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(5, 7)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(60)
    IfHealthNotEqual(8, arg_0_3, 1.0)
    SkipLinesIfConditionTrue(1, 8)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_8_11,
        dummy_id=101,
        behavior_id=6056,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


def Event12906660(_, arg_0_3: int):
    """ 12906660: Event 12906660 """
    EndIfObjectDestroyed(arg_0_3)
    GotoIfFlagEnabled(Label.L1, 92905310)
    GotoIfFlagEnabled(Label.L0, 92905301)
    CreateObjectVFX(929302, obj=arg_0_3, dummy_id=600)
    IfObjectDamaged(0, arg_0_3, attacker=-1)
    Goto(Label.L3)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(929305, obj=arg_0_3, dummy_id=600)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6090,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfThisEventSlotFlagEnabled(1)
    CreateObjectVFX(929304, obj=arg_0_3, dummy_id=600)
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
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6120,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6121,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6122,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6123,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6124,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6125,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6126,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Goto(Label.L2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=100,
        behavior_id=6127,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- 2 --- #
    DefineLabel(2)
    IfTimeElapsed(1, 0.5)
    IfObjectHealthValueComparison(2, arg_0_3, ComparisonType.LessThan, 999)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    RestartIfLastConditionResultFalse(2)

    # --- 3 --- #
    DefineLabel(3)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    IfFramesElapsed(0, 1)
    DestroyObject(arg_0_3)


@RestartOnRest
def Event12906726(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12906726: Event 12906726 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    IfCharacterIsHuman(-3, PLAYER)
    IfCharacterIsType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.c_CharacterMotion, sound_id=arg_4_7)
    IfCharacterDead(-1, arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_8_11)
    IfFramesElapsed(-2, 120)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(-1)
    Restart()


@RestartOnRest
def Event12906738(_, arg_0_3: int):
    """ 12906738: Event 12906738 """
    SkipLinesIfFlagDisabled(1, 1431)
    End()
    IfCharacterDead(0, arg_0_3)
    DisableFlagRange((1420, 1437))
    EnableFlag(1431)


@RestartOnRest
def Event12906740(_, arg_0_3: int, arg_4_7: int):
    """ 12906740: Event 12906740 """
    EndIfFlagRangeAnyEnabled((1431, 1432))
    IfHealthLessThan(1, arg_0_3, 0.8999999761581421)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1432)


@RestartOnRest
def Event12906742(_, arg_0_3: int):
    """ 12906742: Event 12906742 """
    SetTeamType(arg_0_3, TeamType.FriendlyNPC)
    IfFlagEnabled(0, 1432)
    SetTeamType(arg_0_3, TeamType.HostileNPC)


@RestartOnRest
def Event12906744(_, arg_0_3: int, arg_4_7: int):
    """ 12906744: Event 12906744 """
    IfAttacked(0, arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttacked(0, arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttacked(0, arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event12906746(_, arg_0_3: int):
    """ 12906746: Event 12906746 """
    ForceAnimation(arg_0_3, 7015, loop=True, wait_for_completion=True, skip_transition=True)
    DisableFlag(72900001)
    IfFlagEnabled(-1, 72900001)
    IfFlagEnabled(-1, 1432)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_0_3, 151, affect_npc_part_hp=True)


def Event12906748(_, arg_0_3: int):
    """ 12906748: Event 12906748 """
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfCharacterHasSpecialEffect(1, arg_0_3, 5543)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 7021, wait_for_completion=True)


@RestartOnRest
def Event12906750(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906750: Event 12906750 """
    DisableNetworkSync()
    IfCharacterAlive(1, arg_0_3)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    Move(
        arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, dummy_id=arg_8_11, short_move=True
    )
    Restart()


@RestartOnRest
def Event12906764(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_13: short,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906764: Event 12906764 """
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_12_13,
        part_health=arg_16_19,
        damage_correction=1.0,
        body_damage_correction=2.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_12_13,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=2.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_28_31)
    AddSpecialEffect(arg_0_3, arg_20_23, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_24_27)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(arg_0_3, arg_24_27, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_20_23)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12906765(
    _,
    arg_0_3: int,
    arg_4_5: short,
    arg_8_11: int,
    arg_12_13: short,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906765: Event 12906765 """
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_12_13,
        part_health=arg_16_19,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_12_13,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_28_31)
    AddSpecialEffect(arg_0_3, arg_20_23, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_24_27)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(arg_0_3, arg_24_27, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, arg_20_23)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906766(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906766: Event 12906766 """
    EndIfFlagEnabled(arg_4_7)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(0, arg_0_3, 0.699999988079071)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_8_11)


def Event12906767(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906767: Event 12906767 """
    EndIfFlagEnabled(arg_4_7)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(1, arg_0_3, 0.30000001192092896)
    IfFlagEnabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12906768(
    _, arg_0_3: int, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_17: short, arg_18_18: uchar, arg_19_19: uchar
):
    """ 12906768: Event 12906768 """
    EndIfFlagEnabled(arg_4_7)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(arg_0_3, bit_index=arg_19_19, switch_type=OnOffChange.Off)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHasSpecialEffect(0, arg_0_3, 5402)
    SetCollisionMask(arg_0_3, bit_index=arg_18_18, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=arg_19_19, switch_type=OnOffChange.On)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_8_9,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_12_15, material_sfx_id=74, material_vfx_id=74)


def Event12906769(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906769: Event 12906769 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906770(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906770: Event 12906770 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906771(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906771: Event 12906771 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906772(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906772: Event 12906772 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906773(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906773: Event 12906773 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906774(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906774: Event 12906774 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906775(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906775: Event 12906775 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906776(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906776: Event 12906776 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906777(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906777: Event 12906777 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906778(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906778: Event 12906778 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906779(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906779: Event 12906779 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906780(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906780: Event 12906780 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906781(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906781: Event 12906781 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906782(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906782: Event 12906782 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906783(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906783: Event 12906783 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906784(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906784: Event 12906784 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906785(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906785: Event 12906785 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906786(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906786: Event 12906786 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906787(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906787: Event 12906787 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906788(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_17: short,
    arg_20_23: int,
    arg_24_25: short,
    arg_28_31: int,
):
    """ 12906788: Event 12906788 """
    IfFlagEnabled(1, arg_12_15)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=arg_28_31,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_20_23, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_24_25,
        part_index=arg_16_17,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_20_23, material_sfx_id=73, material_vfx_id=73)
    EventValueOperation(arg_4_7, 10, 3, 0, 1, CalculationType.Add)
    EnableFlag(arg_8_11)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_20_23, desired_health=arg_28_31, overwrite_max=True)
    EventValueOperation(arg_4_7, 10, 2, 0, 1, CalculationType.Subtract)
    EnableFlag(arg_8_11)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906827(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12906827: Event 12906827 """
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_12_15)
    AddSpecialEffect(arg_0_3, arg_16_19, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    Wait(30.0)
    RemoveSpecialEffect(arg_0_3, arg_16_19)
    ReplanAI(arg_0_3)
    Restart()


def Event12906828(
    _, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar
):
    """ 12906828: Event 12906828 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(arg_0_3, bit_index=1, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=2, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=3, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=4, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_0_3, bit_index=9, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=10, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=11, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=12, switch_type=OnOffChange.On)
    SetCollisionMask(arg_0_3, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_6_7,
        part_index=arg_4_5,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_12_15)
    AddSpecialEffect(arg_0_3, 5667, affect_npc_part_hp=True)
    ReplanAI(arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(arg_0_3, bit_index=arg_16_16, switch_type=OnOffChange.Off)
    SetDisplayMask(arg_0_3, bit_index=arg_17_17, switch_type=OnOffChange.On)


def Event12906789(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906789: Event 12906789 """
    EndIfFlagEnabled(arg_20_23)
    GotoIfFlagEnabled(Label.L0, arg_24_27)
    SkipLinesIfClient(2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_12_15, erase_root_only=False)
    DisableObject(arg_8_11)
    DeleteVFX(arg_16_19, erase_root_only=False)
    IfFlagDisabled(1, arg_20_23)
    IfFlagEnabled(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    EnableObject(arg_8_11)
    CreateVFX(arg_12_15)
    CreateVFX(arg_16_19)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_20_23)
    IfCharacterIsHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=arg_4_7)
    IfFlagEnabled(3, arg_20_23)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    IfCharacterIsHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_0_3)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, 4.0)
    IfCharacterIsHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=5)
    EnableFlag(arg_28_31)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


def Event12906790(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12906790: Event 12906790 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_8_11)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterIsType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    IfCharacterIsType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(2, input_condition=-1)
    IfTimeElapsed(3, 4.0)
    IfCharacterIsType(3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    EnableFlag(arg_20_23)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


def Event12906791(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12906791: Event 12906791 """
    EndIfFlagEnabled(arg_8_11)
    DisableAI(arg_0_3)
    DisableHealthBar(arg_0_3)
    EnableInvincibility(arg_0_3)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, arg_12_15)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(arg_0_3, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_4_7, slot=0)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(arg_16_19)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)


def Event12906792(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906792: Event 12906792 """
    DisableNetworkSync()
    DisableSoundEvent(arg_8_11)
    DisableSoundEvent(arg_12_15)
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, arg_16_19)
    IfFlagEnabled(1, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, arg_24_27)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_8_11)
    IfCharacterHasTAEEvent(2, arg_0_3, tae_event_id=500)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_16_19)
    IfFlagEnabled(2, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, arg_24_27)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(arg_8_11)
    WaitFrames(0)
    EnableBossMusic(arg_12_15)


def Event12906794(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12906794: Event 12906794 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfEntityBeyondDistance(2, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12906795(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906795: Event 12906795 """
    EndIfFlagEnabled(arg_8_11)
    DisableAI(arg_0_3)
    DisableAI(arg_20_23)
    DisableAI(arg_24_27)
    DisableHealthBar(arg_0_3)
    DisableHealthBar(arg_20_23)
    DisableHealthBar(arg_24_27)
    EnableInvincibility(arg_0_3)
    EnableInvincibility(arg_20_23)
    EnableInvincibility(arg_24_27)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, arg_12_15)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(arg_20_23, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(arg_24_27, UpdateAuthority.Forced)
    DisableFlag(12907230)
    DisableFlag(12907231)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(arg_20_23, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(arg_24_27, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(arg_0_3, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(arg_20_23, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(arg_24_27, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(arg_0_3)
    EnableAI(arg_20_23)
    EnableAI(arg_24_27)
    DisableInvincibility(arg_0_3)
    DisableInvincibility(arg_20_23)
    DisableInvincibility(arg_24_27)
    EnableBossHealthBar(arg_0_3, name=arg_4_7, slot=0)
    EnableBossHealthBar(arg_20_23, name=304002, slot=1)
    EnableBossHealthBar(arg_24_27, name=304003, slot=2)
    EnableFlag(arg_16_19)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)


def Event12906796(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906796: Event 12906796 """
    EndIfFlagEnabled(arg_20_23)
    GotoIfFlagEnabled(Label.L0, arg_24_27)
    SkipLinesIfClient(2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_12_15, erase_root_only=False)
    DisableObject(arg_8_11)
    DeleteVFX(arg_16_19, erase_root_only=False)
    IfFlagDisabled(1, arg_20_23)
    IfFlagEnabled(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    EnableObject(arg_8_11)
    CreateVFX(arg_12_15)
    CreateVFX(arg_16_19)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_20_23)
    IfCharacterIsHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=arg_4_7)
    IfFlagEnabled(3, arg_20_23)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    IfCharacterIsHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_0_3)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, 4.0)
    IfCharacterIsHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=5)
    EnableFlag(arg_28_31)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


def Event12906800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12906800: Event 12906800 """
    EndIfFlagEnabled(arg_12_15)
    GotoIfFlagEnabled(Label.L0, arg_16_19)
    SkipLinesIfClient(2)
    DisableObject(arg_4_7)
    DeleteVFX(arg_8_11, erase_root_only=False)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    EnableObject(arg_4_7)
    CreateVFX(arg_8_11)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_12_15)
    IfCharacterIsHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2900010, entity=arg_4_7)
    IfFlagEnabled(3, arg_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    IfCharacterIsHuman(4, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_0_3)
    IfCharacterHasTAEEvent(-2, PLAYER, tae_event_id=700)
    IfConditionTrue(4, input_condition=-2)
    IfTimeElapsed(5, 4.0)
    IfCharacterIsHuman(5, PLAYER)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(0, input_condition=-3)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=5)
    EnableFlag(arg_20_23)

    # --- 1 --- #
    DefineLabel(1)
    Restart()


def Event12906802(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12906802: Event 12906802 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_8_11)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterIsType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2900010, entity=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    FaceEntity(PLAYER, arg_0_3, animation=101130, wait_for_completion=False)
    IfCharacterIsType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-1, PLAYER, region=2412801)
    IfCharacterHasTAEEvent(-1, PLAYER, tae_event_id=700)
    IfConditionTrue(2, input_condition=-1)
    IfTimeElapsed(3, 4.0)
    IfCharacterIsType(3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    EnableFlag(arg_20_23)

    # --- 0 --- #
    DefineLabel(0)
    Restart()


def Event12906806(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12906806: Event 12906806 """
    EndIfFlagEnabled(arg_8_11)
    DisableAI(arg_0_3)
    DisableHealthBar(arg_0_3)
    EnableInvincibility(arg_0_3)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, arg_12_15)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    DisableFlag(12907230)
    DisableFlag(12907231)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(arg_0_3, 7500, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(arg_0_3, 7501, affect_npc_part_hp=True)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableBossHealthBar(arg_0_3, name=arg_4_7, slot=0)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableFlag(arg_16_19)
    CreatePlayLog(1260)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901800)
    StartPlayLogMeasurement(2900010, 1316, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901801)
    StartPlayLogMeasurement(2900011, 1352, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901802)
    StartPlayLogMeasurement(2900012, 1388, overwrite=True)
    SkipLinesIfValueNotEqual(1, left=arg_8_11, right=12901803)
    StartPlayLogMeasurement(2900013, 1424, overwrite=True)


def Event12906810(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906810: Event 12906810 """
    DisableNetworkSync()
    DisableSoundEvent(arg_8_11)
    DisableSoundEvent(arg_12_15)
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, arg_16_19)
    IfFlagEnabled(1, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, arg_24_27)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_8_11)
    IfCharacterHasTAEEvent(2, arg_0_3, tae_event_id=500)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_16_19)
    IfFlagEnabled(2, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, arg_24_27)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(arg_8_11)
    WaitFrames(0)
    EnableBossMusic(arg_12_15)


def Event12906978(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906978: Event 12906978 """
    DisableNetworkSync()
    DisableSoundEvent(arg_8_11)
    DisableSoundEvent(arg_12_15)
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagDisabled(1, arg_16_19)
    IfFlagEnabled(1, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, arg_24_27)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(arg_8_11)
    IfFlagEnabled(2, arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, arg_16_19)
    IfFlagEnabled(2, arg_20_23)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, arg_24_27)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(arg_8_11)
    WaitFrames(0)
    EnableBossMusic(arg_12_15)


def Event12906818(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12906818: Event 12906818 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfEntityBeyondDistance(2, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12906822(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 12906822: Event 12906822 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfHealthGreaterThan(2, arg_16_19, 0.0)
    IfEntityWithinDistance(2, PLAYER, arg_16_19, radius=arg_8_11)
    IfHealthGreaterThan(3, arg_20_23, 0.0)
    IfEntityWithinDistance(3, PLAYER, arg_20_23, radius=arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(4, arg_0_3, 0.0)
    IfEntityWithinDistance(4, PLAYER, arg_0_3, radius=arg_12_15)
    IfHealthGreaterThan(5, arg_16_19, 0.0)
    IfEntityWithinDistance(5, PLAYER, arg_16_19, radius=arg_12_15)
    IfHealthGreaterThan(6, arg_20_23, 0.0)
    IfEntityWithinDistance(6, PLAYER, arg_20_23, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionFalse(0, input_condition=-2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12906823(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 12906823: Event 12906823 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfHealthGreaterThan(2, arg_16_19, 0.0)
    IfFlagEnabled(2, arg_20_23)
    IfEntityWithinDistance(2, PLAYER, arg_16_19, radius=arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=1)
    IfHealthGreaterThan(3, arg_0_3, 0.0)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_12_15)
    IfHealthGreaterThan(4, arg_16_19, 0.0)
    IfFlagEnabled(4, arg_20_23)
    IfEntityWithinDistance(4, PLAYER, arg_16_19, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionFalse(0, input_condition=-2)
    SetLockedCameraSlot(game_map=CHALICE_DUNGEON, camera_slot=0)
    Restart()


def Event12906824(_, arg_0_3: int, arg_4_7: int):
    """ 12906824: Event 12906824 """
    IfFlagEnabled(0, arg_0_3)
    EnableFlag(arg_4_7)


def Event12906825(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906825: Event 12906825 """
    GotoIfFlagDisabled(Label.L0, arg_28_31)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, arg_24_27)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(1, arg_8_11)
    IfHealthLessThanOrEqual(1, arg_4_7, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    CreateTemporaryVFX(929203, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Character, dummy_id=6)

    # --- 1 --- #
    DefineLabel(1)
    EnableBossHealthBar(arg_0_3, name=arg_16_19, slot=1)
    EnableFlag(arg_24_27)


def Event12906841(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906841: Event 12906841 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=400,
        damage_correction=1.0,
        body_damage_correction=0.75,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=2.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906843(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906843: Event 12906843 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=80,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906845(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906845: Event 12906845 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=80,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906847(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906847: Event 12906847 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=280,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.149999976158142,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906849(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906849: Event 12906849 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=280,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.149999976158142,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=65, material_vfx_id=65)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906851(_, arg_0_3: int, arg_4_7: int):
    """ 12906851: Event 12906851 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    EndIfFlagDisabled(arg_4_7)
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, 7020, loop=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    ForceAnimation(arg_0_3, 7021)


def Event12906853(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906853: Event 12906853 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906855(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906855: Event 12906855 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2000000476837158,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906857(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906857: Event 12906857 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2000000476837158,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906859(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906859: Event 12906859 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.149999976158142,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906861(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906861: Event 12906861 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.149999976158142,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=73, material_vfx_id=73)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906831(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906831: Event 12906831 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906833(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906833: Event 12906833 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906835(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906835: Event 12906835 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906837(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906837: Event 12906837 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906839(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906839: Event 12906839 """
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=60, material_vfx_id=60)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906793(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906793: Event 12906793 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    DisableBossMusic(arg_4_7)
    DisableBossMusic(arg_8_11)
    DisableBossMusic(-1)


def Event12906814(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906814: Event 12906814 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    DisableBossMusic(arg_4_7)
    DisableBossMusic(arg_8_11)
    DisableBossMusic(-1)


def Event12906869(_, arg_0_3: int, arg_4_7: int):
    """ 12906869: Event 12906869 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(2, arg_0_3, 0.699999988079071)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_4_7)


def Event12906870(_, arg_0_3: int, arg_4_7: int):
    """ 12906870: Event 12906870 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    EndIfThisEventSlotFlagEnabled()
    IfHealthLessThan(2, arg_0_3, 0.33000001311302185)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(2, arg_4_7)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12906865(_, arg_0_3: int, arg_4_5: short, arg_8_11: int, arg_12_13: short, arg_14_14: uchar, arg_15_15: uchar):
    """ 12906865: Event 12906865 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetCollisionMask(arg_0_3, bit_index=arg_15_15, switch_type=OnOffChange.Off)
    IfCharacterHasSpecialEffect(0, arg_0_3, 5402)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(arg_0_3, bit_index=arg_14_14, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_0_3, bit_index=arg_15_15, switch_type=OnOffChange.On)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=arg_12_13,
        part_health=9999999,
        damage_correction=0.0,
        body_damage_correction=0.0,
        is_invincible=True,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)


def Event12906871(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906871: Event 12906871 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.399999976158142,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=2.0999999046325684,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906879(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906879: Event 12906879 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=400,
        damage_correction=1.0,
        body_damage_correction=0.20000000298023224,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=0.30000001192092896,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 488, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 498)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 498, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 488)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906872(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906872: Event 12906872 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 485, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 495)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 495, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 485)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906875(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906875: Event 12906875 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=230,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906873(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906873: Event 12906873 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part6,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part6,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 486, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 496)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 496, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 486)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906876(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906876: Event 12906876 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part7,
        part_health=170,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part7,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906874(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906874: Event 12906874 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part8,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part8,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 487, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 497)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 497, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 487)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906877(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906877: Event 12906877 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part9,
        part_health=170,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906878(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906878: Event 12906878 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part10,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part10,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906880(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906880: Event 12906880 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part11,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=0.20000000298023224,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part11,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=0.30000001192092896,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 488, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 498)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 498, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 488)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


def Event12906881(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12906881: Event 12906881 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part12,
        part_health=150,
        damage_correction=1.0,
        body_damage_correction=0.20000000298023224,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part12,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=0.30000001192092896,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 488, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 498)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=100, slot=1)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    AddSpecialEffect(arg_0_3, 498, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 488)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12904889(_, arg_0_3: int):
    """ 12904889: Event 12904889 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    AICommand(arg_0_3, command_id=2, slot=1)
    IfHealthLessThan(2, arg_0_3, 0.6700000166893005)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5402)
    IfConditionTrue(0, input_condition=2)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=100, slot=2)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)
    AICommand(arg_0_3, command_id=-1, slot=2)
    ReplanAI(arg_0_3)
    Wait(0.10000000149011612)
    AICommand(arg_0_3, command_id=3, slot=1)


@RestartOnRest
def Event12904723(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904723: Event 12904723 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=180,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=130, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


@RestartOnRest
def Event12904724(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904724: Event 12904724 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=150, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


@RestartOnRest
def Event12904725(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904725: Event 12904725 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=200,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=150, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


@RestartOnRest
def Event12904726(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904726: Event 12904726 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=200, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


@RestartOnRest
def Event12904727(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904727: Event 12904727 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=2)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    Wait(10.0)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=300)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=200, overwrite_max=True)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    ChangeCharacterCloth(arg_0_3, 10, state_id=1)
    Restart()


def Event12906882(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906882: Event 12906882 """
    EndIfFlagEnabled(arg_8_11)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    AddSpecialEffect(arg_0_3, 5401, affect_npc_part_hp=False)
    WaitFrames(1)
    IfCharacterDead(1, arg_4_7)
    EndIfConditionTrue(1)
    IfFlagEnabled(2, arg_8_11)
    IfRandomTimeElapsed(-1, min_seconds=0.0, max_seconds=1.0)
    IfTimeElapsed(3, 1.0)
    IfCharacterIsType(3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    EnableGravity(arg_0_3)
    ForceAnimation(arg_0_3, 7000)
    WaitFrames(64)
    EnableAI(arg_0_3)


def Event12906863(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12906863: Event 12906863 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.75)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=2)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=10)
    IfHealthNotEqual(3, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=3)
    DisableCharacter(arg_0_3)
    Wait(2.0)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3021)
    AICommand(arg_0_3, command_id=101, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_12_15)
    IfHealthLessThanOrEqual(4, arg_0_3, 0.5)
    IfHealthNotEqual(4, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=4)
    AICommand(arg_0_3, command_id=110, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(5, arg_0_3, tae_event_id=10)
    IfHealthNotEqual(5, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=5)
    DisableCharacter(arg_0_3)
    Wait(2.0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 3021)
    AICommand(arg_0_3, command_id=111, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_16_19)


def Event12906912(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12906912: Event 12906912 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableCharacter(arg_4_7)
    Kill(arg_4_7, award_souls=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, arg_0_3)
    IfFlagEnabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    Kill(arg_4_7, award_souls=False)


def Event12906864(_, arg_0_3: int):
    """ 12906864: Event 12906864 """
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=2, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7000)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(5, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(6, arg_0_3, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(5)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=6)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7001)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, arg_0_3, npc_part_id=2, value=0)
    IfHealthLessThanOrEqual(8, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(9, arg_0_3, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfLastConditionResultTrue(8)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=9)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7002)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=2,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=2, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(arg_0_3)
    IfTimeElapsed(0, 30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(arg_0_3, npc_part_id=2, desired_health=-1, overwrite_max=True)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()


def Event12906867(_, arg_0_3: int):
    """ 12906867: Event 12906867 """
    CreateNPCPart(
        arg_0_3,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=3, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(3, arg_0_3, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7005)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=100, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(5, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(6, arg_0_3, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfLastConditionResultTrue(5)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=6)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7006)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, arg_0_3, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, arg_0_3, 0.0)
    IfCharacterHasTAEEvent(9, arg_0_3, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfLastConditionResultTrue(8)
    GotoIfLastConditionResultTrue(Label.L0, input_condition=9)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 7007)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=3,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=3, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(arg_0_3)
    IfTimeElapsed(0, 30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(arg_0_3, npc_part_id=3, desired_health=-1, overwrite_max=True)
    ReplanAI(arg_0_3)
    WaitFrames(10)
    Restart()
    Restart()


def Event12906868(_, arg_0_3: int):
    """ 12906868: Event 12906868 """
    EndIfFlagEnabled(13201800)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=1,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=0.5,
        body_damage_correction=0.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=1, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(1, arg_0_3, npc_part_id=1, value=0)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(2)
    Restart()


@RestartOnRest
def Event12906829(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12906829: Event 12906829 """
    EndIfFlagEnabled(arg_12_15)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, arg_0_3)
    DisableGravity(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        dummy_id=arg_8_11,
        copy_draw_parent=arg_0_3,
    )
    Restart()


@RestartOnRest
def Event12904873(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904873: Event 12904873 """
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    IfCharacterDead(0, arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_4_7)


@RestartOnRest
def Event12904875(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12904875: Event 12904875 """
    EndIfFlagEnabled(arg_8_11)
    IfHealthLessThanOrEqual(0, arg_0_3, 0.5)
    ForceAnimation(arg_4_7, 3000)


@RestartOnRest
def Event12904884(_, arg_0_3: int):
    """ 12904884: Event 12904884 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHealthLessThan(0, arg_0_3, 0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 7010)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfHealthLessThan(0, arg_0_3, 0.33000001311302185)
    Wait(0.10000000149011612)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 7011)
    AICommand(arg_0_3, command_id=101, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=20)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904734(_, arg_0_3: int):
    """ 12904734: Event 12904734 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfCharacterHasSpecialEffect(2, arg_0_3, 5650)
    IfHealthValueLessThan(2, arg_0_3, 0)
    IfConditionTrue(0, input_condition=2)
    ShootProjectile(
        owner_entity=2900000,
        projectile_id=arg_0_3,
        dummy_id=6,
        behavior_id=225100310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(0.5)
    Restart()


def Event12904735(_, arg_0_3: int):
    """ 12904735: Event 12904735 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHealthLessThan(0, arg_0_3, 0.5)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12904728(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904728: Event 12904728 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=400,
        damage_correction=1.0,
        body_damage_correction=2.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part5,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=2.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 480, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 490)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8040, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AddSpecialEffect(arg_0_3, 490, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 480)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12904729(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904729: Event 12904729 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 481, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 491)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8010, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AddSpecialEffect(arg_0_3, 491, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 481)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12904730(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904730: Event 12904730 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=250,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part2,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 482, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 492)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8000, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AddSpecialEffect(arg_0_3, 492, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 482)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12904731(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904731: Event 12904731 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part3,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 483, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 493)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8030, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AddSpecialEffect(arg_0_3, 493, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 483)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12904732(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 12904732: Event 12904732 """
    WaitFrames(1)
    IfCharacterDead(1, arg_0_3)
    EndIfConditionTrue(1)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=300,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=74, material_vfx_id=74)
    IfCharacterPartHealthLessThanOrEqual(2, arg_0_3, npc_part_id=arg_8_11, value=0)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfLastConditionResultTrue(3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part4,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=75, material_vfx_id=75)
    AddSpecialEffect(arg_0_3, 484, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 494)
    ReplanAI(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 8020, wait_for_completion=True)
    Wait(30.0)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=500)
    AddSpecialEffect(arg_0_3, 494, affect_npc_part_hp=True)
    RemoveSpecialEffect(arg_0_3, 484)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    WaitFrames(15)
    Restart()


@RestartOnRest
def Event12906942(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12906942: Event 12906942 """
    WaitFrames(1)
    IfCharacterDead(1, arg_20_23)
    EndIfConditionTrue(1)
    IfCharacterHasTAEEvent(2, arg_20_23, tae_event_id=90)
    IfFlagEnabled(2, arg_16_19)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(arg_0_3, 5610, affect_npc_part_hp=False)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(arg_0_3)
    ReplanAI(arg_0_3)
    ForceAnimation(arg_0_3, 3021, wait_for_completion=True)
    DisableFlag(arg_8_11)
    EnableFlag(arg_12_15)
    IfFlagEnabled(0, arg_8_11)
    Restart()


@RestartOnRest
def Event12906960(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12906960: Event 12906960 """
    WaitFrames(1)
    IfCharacterDead(1, arg_12_15)
    EndIfConditionTrue(1)
    IfAttacked(-2, arg_0_3, attacker=PLAYER)
    IfAttacked(-2, arg_0_3, attacker=2900248)
    IfAttacked(-2, arg_0_3, attacker=2900249)
    IfAttacked(-2, arg_0_3, attacker=2900250)
    IfCharacterHasTAEEvent(3, arg_12_15, tae_event_id=80)
    IfFlagEnabled(3, arg_8_11)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfLastConditionResultFalse(Label.L0, input_condition=-2)
    WaitFrames(1)
    ForceAnimation(arg_0_3, 3020)
    WaitFrames(65)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 3020)
    WaitFrames(65)

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableFlag(arg_8_11)
    EnableFlag(arg_4_7)
    Restart()


def Event12907000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12907000: Event 12907000 """
    DisableNetworkSync()
    IfCharacterBackreadEnabled(0, arg_0_3)
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    DisableCharacter(arg_0_3)
    DisableObject(arg_4_7)
    IfFlagEnabled(0, arg_8_11)
    EnableObject(arg_4_7)
    EnableCharacter(arg_0_3)
    CreateTemporaryVFX(100330, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=100)

    # --- 0 --- #
    DefineLabel(0)
    RegisterLantern(arg_12_15, arg_4_7, 0.0, reaction_angle=0.0, initial_sword_number=0, sword_level=0)


def Event12907010(_, arg_0_3: int, arg_4_7: int):
    """ 12907010: Event 12907010 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    FaceEntity(PLAYER, arg_4_7, animation=101170, wait_for_completion=False)
    WaitFrames(32)
    InitializeWarpObject(arg_4_7)


def Event12907020(_, arg_0_3: int, arg_4_7: int):
    """ 12907020: Event 12907020 """
    EndIfClient()
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    FaceEntity(PLAYER, arg_4_7, animation=101160, wait_for_completion=False)
    Wait(1.0)
    CreateTemporaryVFX(100320, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=100)
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


def Event12907030(_, arg_0_3: int, arg_4_7: int):
    """ 12907030: Event 12907030 """
    EndIfClient()
    IfFlagEnabled(0, arg_0_3)
    WaitFrames(1)
    CreateTemporaryVFX(100321, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, dummy_id=100)
    InitializeWarpObject(arg_4_7)
    DisableFlag(arg_0_3)


def Event12907300(_, arg_0_3: int, arg_4_7: int):
    """ 12907300: Event 12907300 """
    IfPlayerHasGood(0, arg_0_3, including_box=False)
    EnableFlag(arg_4_7)


def Event12907400():
    """ 12907400: Event 12907400 """
    IfFlagEnabled(1, 12907230)
    IfFlagEnabled(1, 12907231)
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.LessThan, value=2)
    IfFlagEnabled(-1, 12907230)
    IfFlagEnabled(-1, 12907231)
    IfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.LessThan, value=1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    AwaitConditionTrue(-2)
    IfTimeElapsed(7, 10.0)
    IfCharacterIsHuman(7, PLAYER)
    IfConditionTrue(0, input_condition=7)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    IfFlagDisabled(3, 12907230)
    IfFlagDisabled(3, 12907231)
    IfFlagEnabled(4, 12907230)
    IfFlagDisabled(4, 12907231)
    IfClientTypeCountComparison(4, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfFlagDisabled(5, 12907230)
    IfFlagEnabled(5, 12907231)
    IfClientTypeCountComparison(5, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfFlagEnabled(6, 12907230)
    IfFlagEnabled(6, 12907231)
    IfClientTypeCountComparison(6, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(-3, input_condition=6)
    AwaitConditionTrue(-3)
    IfCharacterIsHuman(0, PLAYER)
    RemoveSpecialEffect(PLAYER, 9020)
    Restart()


def Event12907401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12907401: Event 12907401 """
    GotoIfFlagEnabled(Label.L0, 92905340)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfCharacterIsHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, 10.0)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    IfFramesElapsed(0, 59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)
    EnableFlag(12907230)


def Event12907405(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12907405: Event 12907405 """
    GotoIfFlagDisabled(Label.L1, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndIfFlagEnabled(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfCharacterIsHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, 30)
    IfFlagDisabled(4, arg_16_19)
    IfFlagEnabled(4, arg_24_27)
    SkipLinesIfConditionTrue(1, 4)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, 10.0)
    SkipLinesIfLastConditionResultTrue(1, 4)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    IfFramesElapsed(0, 59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)
    EnableFlag(12907231)


def Event12907409(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12907409: Event 12907409 """
    IfFlagEnabled(-15, arg_8_11)
    IfFlagEnabled(-15, arg_12_15)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, arg_4_7)
    IfHealthRatioEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(3, arg_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    DisableFlag(12907230)
    GotoIfLastConditionResultFalse(Label.L0, input_condition=2)
    EnableFlag(arg_16_19)
    EndIfFlagEnabled(12907231)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


def Event12907413(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12907413: Event 12907413 """
    IfFlagEnabled(-15, arg_8_11)
    IfFlagEnabled(-15, arg_12_15)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, arg_4_7)
    IfHealthRatioEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(3, arg_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    DisableFlag(12907231)
    GotoIfLastConditionResultFalse(Label.L0, input_condition=2)
    EnableFlag(arg_16_19)
    EndIfFlagEnabled(12907230)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


def Event12907440(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12907440: Event 12907440 """
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(0, PLAYER, 9020)
    AddSpecialEffect(arg_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(-1, PLAYER, 9020)
    IfFlagEnabled(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    RemoveSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    Restart()


def Event12907420(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12907420: Event 12907420 """
    EndIfFlagDisabled(arg_4_7)
    SkipLinesIfClient(2)
    AddSpecialEffect(PLAYER, arg_0_3, affect_npc_part_hp=False)
    End()
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfCharacterIsType(1, PLAYER, CharacterType.WhitePhantom)
    SkipLinesIfConditionTrue(2, 1)
    AddSpecialEffect(PLAYER, arg_8_11, affect_npc_part_hp=False)
    End()
    AddSpecialEffect(PLAYER, arg_12_15, affect_npc_part_hp=False)


def Event12907430(_, arg_0_3: int, arg_4_7: int):
    """ 12907430: Event 12907430 """
    DisableFlag(arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    EnableFlag(arg_4_7)
    IfCharacterOutsideRegion(2, PLAYER, region=arg_0_3)
    IfHost(2)
    IfConditionTrue(0, input_condition=2)
    Restart()


def Event12907600(_, arg_0_3: int, arg_4_7: int):
    """ 12907600: Event 12907600 """
    DisableNetworkSync()
    DisableObject(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfConnectingMultiplayer(-1)
    IfMultiplayer(-1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(arg_0_3)
    CreateVFX(arg_4_7)
    IfConnectingMultiplayer(-2)
    IfMultiplayer(-2)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@RestartOnRest
def Event12906962(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12906962: Event 12906962 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
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
    IfFlagDisabled(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_8_11)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
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
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12906966(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12906966: Event 12906966 """
    SkipLinesIfFlagEnabled(1, arg_12_15)
    DisableCharacter(arg_4_7)
    SkipLinesIfFlagEnabled(3, arg_16_19)
    IfClient(1)
    IfFlagEnabled(1, arg_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_4_7)
    EndIfFlagEnabled(arg_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(arg_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfFlagState(2, state=FlagSetting.On, flag_type=FlagType.RelativeToThisEventSlot, flag=14)
    IfFlagDisabled(2, arg_24_27)
    IfActionButtonParamActivated(2, action_button_id=arg_20_23, entity=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(arg_0_3, arg_4_7, arg_8_11, summon_flag=arg_12_15, dismissal_flag=arg_16_19)
    EnableFlag(arg_28_31)
    RemoveSpecialEffect(PLAYER, 9005)
    RemoveSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12906970(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12906970: Event 12906970 """
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12906974(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12906974: Event 12906974 """
    EndIfClient()
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    IfFlagEnabled(1, arg_20_23)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    FaceEntity(arg_0_3, arg_8_11, animation=arg_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(arg_0_3, region=arg_8_11, reaction_range=1.0)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_24_27)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12907610(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12907610: Event 12907610 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event12907620(_, arg_0_3: int, arg_4_7: int):
    """ 12907620: Event 12907620 """
    IfCharacterIsHuman(1, PLAYER)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event12907625(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12907625: Event 12907625 """
    IfCharacterIsHuman(1, PLAYER)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    WaitFrames(15)
    EnableCharacter(arg_8_11)


@RestartOnRest
def Event12907630(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12907630: Event 12907630 """
    IfCharacterIsHuman(1, PLAYER)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    WaitFrames(15)
    EnableCharacter(arg_8_11)
    WaitFrames(15)
    WaitFrames(15)
    EnableCharacter(arg_12_15)
    WaitFrames(15)
    WaitFrames(15)
    EnableCharacter(arg_16_19)
