"""
linked:
0
72
154
220

strings:
0: N:\\GR\\data\\Param\\event\\common.emevd
72: N:\\GR\\data\\Param\\event\\common_func.emevd
154: N:\\GR\\data\\Param\\event\\m60.emevd
220: N:\\GR\\data\\Param\\event\\common_macro.emevd
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_37_46_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1037460000, asset=Assets.AEG099_060_9001)
    CommonFunc_90005760(
        0,
        flag=1037460800,
        character=Characters.BellBearingHunter,
        region=1037462340,
        flag_1=1037462716,
    )
    CommonFunc_90005860(
        0,
        flag=1037460800,
        left=0,
        character=Characters.BellBearingHunter,
        left_1=0,
        item_lot__item_lot_param_id=1037460400,
        seconds=0.0,
    )
    CommonFunc_90005870(0, character=Characters.BellBearingHunter, name=903100601, npc_threat_level=10)
    CommonFunc_90005872(0, character=Characters.BellBearingHunter, npc_threat_level=10, right=0)
    CommonFunc_90005702(0, character=Characters.GiantTurtle, flag=3723, first_flag=3720, last_flag=3723)
    Event_1037460700(0, character=Characters.GiantTurtle)
    Event_1037460702(0, character=Characters.GiantTurtle)
    CommonFunc_90005770(0, flag=1037460701)
    Event_1037460710(0, flag=1037469280)
    Event_1037460711(0, flag=1037469281)
    Event_1037460719(0, flag=1037469289)
    CommonFunc_90005631(0, 1037461640, 61021)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.GiantTurtle)
    CommonFunc_90005261(0, character=1037460200, region=1037462600, radius=3.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(0, character=1037460201, region=1037462600, radius=3.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(0, character=1037460202, region=1037462600, radius=3.0, seconds=0.0, animation_id=3020)
    CommonFunc_90005261(0, character=1037460203, region=1037462600, radius=3.0, seconds=0.0, animation_id=1700)
    CommonFunc_90005261(0, 1037460204, 1037462600, 3.0, 0.0, 1700)


@RestartOnRest(1037460700)
def Event_1037460700(_, character: uint):
    """Event 1037460700"""
    DisableNetworkSync()
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L10)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L4, flag=1037462717)
    DisableNetworkFlag(1037462716)
    OR_1.Add(FlagEnabled(1037460701))
    OR_1.Add(FlagEnabled(3723))
    AND_1.Add(TimeOfDayInRange(earliest=(20, 0, 0), latest=(5, 30, 0)))
    AND_1.Add(FlagDisabled(1037460800))
    AND_1.Add(OR_1)
    GotoIfConditionFalse(Label.L4, input_condition=AND_1)
    EnableNetworkFlag(1037462716)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableNetworkFlag(1037462717)
    GotoIfFlagEnabled(Label.L5, flag=3725)
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagEnabled(3725))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagEnabled(Label.L0, flag=3720)
    GotoIfFlagEnabled(Label.L3, flag=3723)

    # --- Label 0 --- #
    DefineLabel(0)
    if FlagEnabled(1037462716):
        DisableCharacter(character)
        DisableBackread(character)
        Goto(Label.L20)
    EnableCharacter(character)
    EnableBackread(character)
    ForceAnimation(character, 930001)
    Goto(Label.L20)

    # --- Label 3 --- #
    DefineLabel(3)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    
    MAIN.Await(FlagDisabled(3725))
    
    Restart()


@RestartOnRest(1037460702)
def Event_1037460702(_, character: uint):
    """Event 1037460702"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=0))
    
    AddSpecialEffect(character, 9750)
    Restart()


@RestartOnRest(1037460710)
def Event_1037460710(_, flag: uint):
    """Event 1037460710"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(3101))
    OR_1.Add(FlagEnabled(3121))
    OR_1.Add(FlagEnabled(3161))
    OR_1.Add(FlagEnabled(3181))
    OR_1.Add(FlagEnabled(3221))
    OR_1.Add(FlagEnabled(3241))
    OR_1.Add(FlagEnabled(3261))
    OR_1.Add(FlagEnabled(3281))
    OR_1.Add(FlagEnabled(3301))
    OR_1.Add(FlagEnabled(3361))
    OR_1.Add(FlagEnabled(3381))
    OR_1.Add(FlagEnabled(3401))
    OR_1.Add(FlagEnabled(3421))
    OR_1.Add(FlagEnabled(3441))
    OR_1.Add(FlagEnabled(3461))
    OR_1.Add(FlagEnabled(3481))
    OR_1.Add(FlagEnabled(3501))
    OR_1.Add(FlagEnabled(3521))
    OR_1.Add(FlagEnabled(3541))
    OR_1.Add(FlagEnabled(3561))
    OR_1.Add(FlagEnabled(3581))
    OR_1.Add(FlagEnabled(3601))
    OR_1.Add(FlagEnabled(3621))
    OR_1.Add(FlagEnabled(3661))
    OR_1.Add(FlagEnabled(3701))
    OR_1.Add(FlagEnabled(3721))
    OR_1.Add(FlagEnabled(3741))
    OR_1.Add(FlagEnabled(3761))
    OR_1.Add(FlagEnabled(3781))
    OR_1.Add(FlagEnabled(3801))
    OR_1.Add(FlagEnabled(3821))
    OR_1.Add(FlagEnabled(3861))
    OR_1.Add(FlagEnabled(3881))
    OR_1.Add(FlagEnabled(3901))
    OR_1.Add(FlagEnabled(3921))
    OR_1.Add(FlagEnabled(3941))
    OR_1.Add(FlagEnabled(3961))
    OR_1.Add(FlagEnabled(3981))
    OR_1.Add(FlagEnabled(4001))
    OR_1.Add(FlagEnabled(4021))
    OR_1.Add(FlagEnabled(4041))
    OR_1.Add(FlagEnabled(4061))
    OR_1.Add(FlagEnabled(4081))
    OR_1.Add(FlagEnabled(4101))
    OR_1.Add(FlagEnabled(4121))
    OR_1.Add(FlagEnabled(4141))
    OR_1.Add(FlagEnabled(4161))
    OR_1.Add(FlagEnabled(4181))
    OR_1.Add(FlagEnabled(4201))
    OR_1.Add(FlagEnabled(4221))
    OR_1.Add(FlagEnabled(4241))
    OR_1.Add(FlagEnabled(4261))
    OR_1.Add(FlagEnabled(4281))
    OR_1.Add(FlagEnabled(4301))
    OR_1.Add(FlagEnabled(4321))
    OR_1.Add(FlagEnabled(4341))
    OR_1.Add(FlagEnabled(4361))
    OR_1.Add(FlagEnabled(4381))
    OR_1.Add(FlagEnabled(4401))
    OR_1.Add(FlagEnabled(4421))
    OR_1.Add(FlagEnabled(4441))
    OR_1.Add(FlagEnabled(4461))
    OR_1.Add(FlagEnabled(4481))
    OR_1.Add(FlagEnabled(4501))
    OR_1.Add(FlagEnabled(4521))
    OR_1.Add(FlagEnabled(4541))
    OR_1.Add(FlagEnabled(4561))
    OR_1.Add(FlagEnabled(4581))
    OR_1.Add(FlagEnabled(4701))
    OR_1.Add(FlagEnabled(4721))
    OR_1.Add(FlagEnabled(4726))
    OR_1.Add(FlagEnabled(4731))
    OR_1.Add(FlagEnabled(4736))
    OR_1.Add(FlagEnabled(4741))
    OR_1.Add(FlagEnabled(4746))
    OR_1.Add(FlagEnabled(4751))
    OR_1.Add(FlagEnabled(4756))
    OR_1.Add(FlagEnabled(4761))
    OR_1.Add(FlagEnabled(4766))
    OR_1.Add(FlagEnabled(4771))
    OR_1.Add(FlagEnabled(4776))
    OR_1.Add(FlagEnabled(4781))
    OR_1.Add(FlagEnabled(4786))
    OR_1.Add(FlagEnabled(4791))
    OR_1.Add(FlagEnabled(4796))
    OR_1.Add(FlagEnabled(4801))
    OR_1.Add(FlagEnabled(4806))
    OR_1.Add(FlagEnabled(4811))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    OR_2.Add(FlagEnabled(3101))
    OR_2.Add(FlagEnabled(3121))
    OR_2.Add(FlagEnabled(3161))
    OR_2.Add(FlagEnabled(3181))
    OR_2.Add(FlagEnabled(3221))
    OR_2.Add(FlagEnabled(3241))
    OR_2.Add(FlagEnabled(3261))
    OR_2.Add(FlagEnabled(3281))
    OR_2.Add(FlagEnabled(3301))
    OR_2.Add(FlagEnabled(3361))
    OR_2.Add(FlagEnabled(3381))
    OR_2.Add(FlagEnabled(3401))
    OR_2.Add(FlagEnabled(3421))
    OR_2.Add(FlagEnabled(3441))
    OR_2.Add(FlagEnabled(3461))
    OR_2.Add(FlagEnabled(3481))
    OR_2.Add(FlagEnabled(3501))
    OR_2.Add(FlagEnabled(3521))
    OR_2.Add(FlagEnabled(3541))
    OR_2.Add(FlagEnabled(3561))
    OR_2.Add(FlagEnabled(3581))
    OR_2.Add(FlagEnabled(3601))
    OR_2.Add(FlagEnabled(3621))
    OR_2.Add(FlagEnabled(3661))
    OR_2.Add(FlagEnabled(3701))
    OR_2.Add(FlagEnabled(3721))
    OR_2.Add(FlagEnabled(3741))
    OR_2.Add(FlagEnabled(3761))
    OR_2.Add(FlagEnabled(3781))
    OR_2.Add(FlagEnabled(3801))
    OR_2.Add(FlagEnabled(3821))
    OR_2.Add(FlagEnabled(3861))
    OR_2.Add(FlagEnabled(3881))
    OR_2.Add(FlagEnabled(3901))
    OR_2.Add(FlagEnabled(3921))
    OR_2.Add(FlagEnabled(3941))
    OR_2.Add(FlagEnabled(3961))
    OR_2.Add(FlagEnabled(3981))
    OR_2.Add(FlagEnabled(4001))
    OR_2.Add(FlagEnabled(4021))
    OR_2.Add(FlagEnabled(4041))
    OR_2.Add(FlagEnabled(4061))
    OR_2.Add(FlagEnabled(4081))
    OR_2.Add(FlagEnabled(4101))
    OR_2.Add(FlagEnabled(4121))
    OR_2.Add(FlagEnabled(4141))
    OR_2.Add(FlagEnabled(4161))
    OR_2.Add(FlagEnabled(4181))
    OR_2.Add(FlagEnabled(4201))
    OR_2.Add(FlagEnabled(4221))
    OR_2.Add(FlagEnabled(4241))
    OR_2.Add(FlagEnabled(4261))
    OR_2.Add(FlagEnabled(4281))
    OR_2.Add(FlagEnabled(4301))
    OR_2.Add(FlagEnabled(4321))
    OR_2.Add(FlagEnabled(4341))
    OR_2.Add(FlagEnabled(4361))
    OR_2.Add(FlagEnabled(4381))
    OR_2.Add(FlagEnabled(4401))
    OR_2.Add(FlagEnabled(4421))
    OR_2.Add(FlagEnabled(4441))
    OR_2.Add(FlagEnabled(4461))
    OR_2.Add(FlagEnabled(4481))
    OR_2.Add(FlagEnabled(4501))
    OR_2.Add(FlagEnabled(4521))
    OR_2.Add(FlagEnabled(4541))
    OR_2.Add(FlagEnabled(4561))
    OR_2.Add(FlagEnabled(4581))
    OR_2.Add(FlagEnabled(4701))
    OR_2.Add(FlagEnabled(4721))
    OR_2.Add(FlagEnabled(4726))
    OR_2.Add(FlagEnabled(4731))
    OR_2.Add(FlagEnabled(4736))
    OR_2.Add(FlagEnabled(4741))
    OR_2.Add(FlagEnabled(4746))
    OR_2.Add(FlagEnabled(4751))
    OR_2.Add(FlagEnabled(4756))
    OR_2.Add(FlagEnabled(4761))
    OR_2.Add(FlagEnabled(4766))
    OR_2.Add(FlagEnabled(4771))
    OR_2.Add(FlagEnabled(4776))
    OR_2.Add(FlagEnabled(4781))
    OR_2.Add(FlagEnabled(4786))
    OR_2.Add(FlagEnabled(4791))
    OR_2.Add(FlagEnabled(4796))
    OR_2.Add(FlagEnabled(4801))
    OR_2.Add(FlagEnabled(4806))
    OR_2.Add(FlagEnabled(4811))
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(1037460711)
def Event_1037460711(_, flag: uint):
    """Event 1037460711"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(3617))
    AND_1.Add(FlagEnabled(3603))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    AND_2.Add(FlagDisabled(3617))
    AND_2.Add(FlagEnabled(3603))
    OR_2.Add(AND_2)
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(1037460719)
def Event_1037460719(_, flag: uint):
    """Event 1037460719"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    if FlagEnabled(3101):
        DisableNetworkConnectedFlagRange(flag_range=(3100, 3103))
        EnableNetworkFlag(3100)
    if FlagEnabled(3121):
        DisableNetworkConnectedFlagRange(flag_range=(3120, 3123))
        EnableNetworkFlag(3120)
    if FlagEnabled(3161):
        DisableNetworkConnectedFlagRange(flag_range=(3160, 3163))
        EnableNetworkFlag(3160)
    if FlagEnabled(3181):
        DisableNetworkConnectedFlagRange(flag_range=(3180, 3183))
        EnableNetworkFlag(3180)
    if FlagEnabled(3221):
        DisableNetworkConnectedFlagRange(flag_range=(3220, 3223))
        EnableNetworkFlag(3220)
    if FlagEnabled(3241):
        DisableNetworkConnectedFlagRange(flag_range=(3240, 3243))
        EnableNetworkFlag(3240)
    if FlagEnabled(3261):
        DisableNetworkConnectedFlagRange(flag_range=(3260, 3263))
        EnableNetworkFlag(3260)
    if FlagEnabled(3281):
        DisableNetworkConnectedFlagRange(flag_range=(3280, 3283))
        EnableNetworkFlag(3280)
    if FlagEnabled(3301):
        DisableNetworkConnectedFlagRange(flag_range=(3300, 3303))
        EnableNetworkFlag(3300)
    if FlagEnabled(3361):
        DisableNetworkConnectedFlagRange(flag_range=(3360, 3363))
        EnableNetworkFlag(3360)
    if FlagEnabled(3381):
        DisableNetworkConnectedFlagRange(flag_range=(3380, 3383))
        EnableNetworkFlag(3380)
    if FlagEnabled(3401):
        DisableNetworkConnectedFlagRange(flag_range=(3400, 3403))
        EnableNetworkFlag(3400)
    if FlagEnabled(3421):
        DisableNetworkConnectedFlagRange(flag_range=(3420, 3423))
        EnableNetworkFlag(3420)
    if FlagEnabled(3441):
        DisableNetworkConnectedFlagRange(flag_range=(3440, 3443))
        EnableNetworkFlag(3440)
    if FlagEnabled(3461):
        DisableNetworkConnectedFlagRange(flag_range=(3460, 3463))
        EnableNetworkFlag(3460)
    if FlagEnabled(3481):
        DisableNetworkConnectedFlagRange(flag_range=(3480, 3483))
        EnableNetworkFlag(3480)
    if FlagEnabled(3501):
        DisableNetworkConnectedFlagRange(flag_range=(3500, 3503))
        EnableNetworkFlag(3500)
    if FlagEnabled(3521):
        DisableNetworkConnectedFlagRange(flag_range=(3520, 3523))
        EnableNetworkFlag(3520)
    if FlagEnabled(3541):
        DisableNetworkConnectedFlagRange(flag_range=(3540, 3543))
        EnableNetworkFlag(3540)
    if FlagEnabled(3561):
        DisableNetworkConnectedFlagRange(flag_range=(3560, 3563))
        EnableNetworkFlag(3560)
    if FlagEnabled(3581):
        DisableNetworkConnectedFlagRange(flag_range=(3580, 3583))
        EnableNetworkFlag(3580)
    if FlagEnabled(3601):
        DisableNetworkConnectedFlagRange(flag_range=(3600, 3603))
        EnableNetworkFlag(3600)
    if FlagEnabled(3621):
        DisableNetworkConnectedFlagRange(flag_range=(3620, 3623))
        EnableNetworkFlag(3620)
    if FlagEnabled(3661):
        DisableNetworkConnectedFlagRange(flag_range=(3660, 3663))
        EnableNetworkFlag(3660)
    if FlagEnabled(3701):
        DisableNetworkConnectedFlagRange(flag_range=(3700, 3703))
        EnableNetworkFlag(3700)
    if FlagEnabled(3721):
        DisableNetworkConnectedFlagRange(flag_range=(3720, 3723))
        EnableNetworkFlag(3720)
    if FlagEnabled(3741):
        DisableNetworkConnectedFlagRange(flag_range=(3740, 3743))
        EnableNetworkFlag(3740)
    if FlagEnabled(3761):
        DisableNetworkConnectedFlagRange(flag_range=(3760, 3763))
        EnableNetworkFlag(3760)
    if FlagEnabled(3781):
        DisableNetworkConnectedFlagRange(flag_range=(3780, 3783))
        EnableNetworkFlag(3780)
    if FlagEnabled(3801):
        DisableNetworkConnectedFlagRange(flag_range=(3800, 3803))
        EnableNetworkFlag(3800)
    if FlagEnabled(3821):
        DisableNetworkConnectedFlagRange(flag_range=(3820, 3823))
        EnableNetworkFlag(3820)
    if FlagEnabled(3861):
        DisableNetworkConnectedFlagRange(flag_range=(3860, 3863))
        EnableNetworkFlag(3860)
    if FlagEnabled(3881):
        DisableNetworkConnectedFlagRange(flag_range=(3880, 3883))
        EnableNetworkFlag(3880)
    if FlagEnabled(3901):
        DisableNetworkConnectedFlagRange(flag_range=(3900, 3903))
        EnableNetworkFlag(3900)
    if FlagEnabled(3921):
        DisableNetworkConnectedFlagRange(flag_range=(3920, 3923))
        EnableNetworkFlag(3920)
    if FlagEnabled(3941):
        DisableNetworkConnectedFlagRange(flag_range=(3940, 3943))
        EnableNetworkFlag(3940)
    if FlagEnabled(3961):
        DisableNetworkConnectedFlagRange(flag_range=(3960, 3963))
        EnableNetworkFlag(3960)
    if FlagEnabled(3981):
        DisableNetworkConnectedFlagRange(flag_range=(3980, 3983))
        EnableNetworkFlag(3980)
    if FlagEnabled(4001):
        DisableNetworkConnectedFlagRange(flag_range=(4000, 4003))
        EnableNetworkFlag(4000)
    if FlagEnabled(4021):
        DisableNetworkConnectedFlagRange(flag_range=(4020, 4023))
        EnableNetworkFlag(4020)
    if FlagEnabled(4041):
        DisableNetworkConnectedFlagRange(flag_range=(4040, 4043))
        EnableNetworkFlag(4040)
    if FlagEnabled(4061):
        DisableNetworkConnectedFlagRange(flag_range=(4060, 4063))
        EnableNetworkFlag(4060)
    if FlagEnabled(4081):
        DisableNetworkConnectedFlagRange(flag_range=(4080, 4083))
        EnableNetworkFlag(4080)
    if FlagEnabled(4101):
        DisableNetworkConnectedFlagRange(flag_range=(4100, 4103))
        EnableNetworkFlag(4100)
    if FlagEnabled(4121):
        DisableNetworkConnectedFlagRange(flag_range=(4120, 4123))
        EnableNetworkFlag(4120)
    if FlagEnabled(4141):
        DisableNetworkConnectedFlagRange(flag_range=(4140, 4143))
        EnableNetworkFlag(4140)
    if FlagEnabled(4161):
        DisableNetworkConnectedFlagRange(flag_range=(4160, 4163))
        EnableNetworkFlag(4160)
    if FlagEnabled(4181):
        DisableNetworkConnectedFlagRange(flag_range=(4180, 4183))
        EnableNetworkFlag(4180)
    if FlagEnabled(4201):
        DisableNetworkConnectedFlagRange(flag_range=(4200, 4203))
        EnableNetworkFlag(4200)
    if FlagEnabled(4221):
        DisableNetworkConnectedFlagRange(flag_range=(4220, 4223))
        EnableNetworkFlag(4220)
    if FlagEnabled(4241):
        DisableNetworkConnectedFlagRange(flag_range=(4240, 4243))
        EnableNetworkFlag(4240)
    if FlagEnabled(4261):
        DisableNetworkConnectedFlagRange(flag_range=(4260, 4263))
        EnableNetworkFlag(4260)
    if FlagEnabled(4281):
        DisableNetworkConnectedFlagRange(flag_range=(4280, 4283))
        EnableNetworkFlag(4280)
    if FlagEnabled(4301):
        DisableNetworkConnectedFlagRange(flag_range=(4300, 4303))
        EnableNetworkFlag(4300)
    if FlagEnabled(4321):
        DisableNetworkConnectedFlagRange(flag_range=(4320, 4323))
        EnableNetworkFlag(4320)
    if FlagEnabled(4341):
        DisableNetworkConnectedFlagRange(flag_range=(4340, 4343))
        EnableNetworkFlag(4340)
    if FlagEnabled(4361):
        DisableNetworkConnectedFlagRange(flag_range=(4360, 4363))
        EnableNetworkFlag(4360)
    if FlagEnabled(4381):
        DisableNetworkConnectedFlagRange(flag_range=(4380, 4383))
        EnableNetworkFlag(4380)
    if FlagEnabled(4401):
        DisableNetworkConnectedFlagRange(flag_range=(4400, 4403))
        EnableNetworkFlag(4400)
    if FlagEnabled(4421):
        DisableNetworkConnectedFlagRange(flag_range=(4420, 4423))
        EnableNetworkFlag(4420)
    if FlagEnabled(4441):
        DisableNetworkConnectedFlagRange(flag_range=(4440, 4443))
        EnableNetworkFlag(4440)
    if FlagEnabled(4461):
        DisableNetworkConnectedFlagRange(flag_range=(4460, 4463))
        EnableNetworkFlag(4460)
    if FlagEnabled(4481):
        DisableNetworkConnectedFlagRange(flag_range=(4480, 4483))
        EnableNetworkFlag(4480)
    if FlagEnabled(4501):
        DisableNetworkConnectedFlagRange(flag_range=(4500, 4503))
        EnableNetworkFlag(4500)
    if FlagEnabled(4521):
        DisableNetworkConnectedFlagRange(flag_range=(4520, 4523))
        EnableNetworkFlag(4520)
    if FlagEnabled(4541):
        DisableNetworkConnectedFlagRange(flag_range=(4540, 4543))
        EnableNetworkFlag(4540)
    if FlagEnabled(4561):
        DisableNetworkConnectedFlagRange(flag_range=(4560, 4563))
        EnableNetworkFlag(4560)
    if FlagEnabled(4581):
        DisableNetworkConnectedFlagRange(flag_range=(4580, 4583))
        EnableNetworkFlag(4580)
    if FlagEnabled(4701):
        DisableNetworkConnectedFlagRange(flag_range=(4700, 4703))
        EnableNetworkFlag(4700)
    if FlagEnabled(4721):
        DisableNetworkConnectedFlagRange(flag_range=(4720, 4723))
        EnableNetworkFlag(4720)
    if FlagEnabled(4726):
        DisableNetworkConnectedFlagRange(flag_range=(4725, 4728))
        EnableNetworkFlag(4725)
    if FlagEnabled(4731):
        DisableNetworkConnectedFlagRange(flag_range=(4730, 4733))
        EnableNetworkFlag(4730)
    if FlagEnabled(4736):
        DisableNetworkConnectedFlagRange(flag_range=(4735, 4738))
        EnableNetworkFlag(4735)
    if FlagEnabled(4741):
        DisableNetworkConnectedFlagRange(flag_range=(4740, 4743))
        EnableNetworkFlag(4740)
    if FlagEnabled(4746):
        DisableNetworkConnectedFlagRange(flag_range=(4745, 4748))
        EnableNetworkFlag(4745)
    if FlagEnabled(4751):
        DisableNetworkConnectedFlagRange(flag_range=(4750, 4753))
        EnableNetworkFlag(4750)
    if FlagEnabled(4756):
        DisableNetworkConnectedFlagRange(flag_range=(4755, 4758))
        EnableNetworkFlag(4755)
    if FlagEnabled(4761):
        DisableNetworkConnectedFlagRange(flag_range=(4760, 4763))
        EnableNetworkFlag(4760)
    if FlagEnabled(4766):
        DisableNetworkConnectedFlagRange(flag_range=(4765, 4768))
        EnableNetworkFlag(4765)
    if FlagEnabled(4771):
        DisableNetworkConnectedFlagRange(flag_range=(4770, 4773))
        EnableNetworkFlag(4770)
    if FlagEnabled(4776):
        DisableNetworkConnectedFlagRange(flag_range=(4775, 4778))
        EnableNetworkFlag(4775)
    if FlagEnabled(4781):
        DisableNetworkConnectedFlagRange(flag_range=(4780, 4783))
        EnableNetworkFlag(4780)
    if FlagEnabled(4786):
        DisableNetworkConnectedFlagRange(flag_range=(4785, 4788))
        EnableNetworkFlag(4785)
    if FlagEnabled(4791):
        DisableNetworkConnectedFlagRange(flag_range=(4790, 4793))
        EnableNetworkFlag(4790)
    if FlagEnabled(4796):
        DisableNetworkConnectedFlagRange(flag_range=(4795, 4798))
        EnableNetworkFlag(4795)
    if FlagEnabled(4801):
        DisableNetworkConnectedFlagRange(flag_range=(4800, 4803))
        EnableNetworkFlag(4800)
    if FlagEnabled(4806):
        DisableNetworkConnectedFlagRange(flag_range=(4805, 4808))
        EnableNetworkFlag(4805)
    if FlagEnabled(4811):
        DisableNetworkConnectedFlagRange(flag_range=(4810, 4813))
        EnableNetworkFlag(4810)
    AND_1.Add(FlagDisabled(3617))
    AND_1.Add(FlagEnabled(3603))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(3600, 3603))
    EnableNetworkFlag(3600)
    EnableNetworkFlag(3158)
    EnableNetworkFlag(3218)
    EnableNetworkFlag(3338)
    EnableNetworkFlag(3358)
    EnableNetworkFlag(3658)
    EnableNetworkFlag(3698)
    EnableNetworkFlag(3858)
    EnableNetworkFlag(3118)
    EnableNetworkFlag(3138)
    EnableNetworkFlag(3178)
    EnableNetworkFlag(3198)
    EnableNetworkFlag(3238)
    EnableNetworkFlag(3258)
    EnableNetworkFlag(3278)
    EnableNetworkFlag(3298)
    EnableNetworkFlag(3318)
    EnableNetworkFlag(3378)
    EnableNetworkFlag(3398)
    EnableNetworkFlag(3418)
    EnableNetworkFlag(3438)
    EnableNetworkFlag(3458)
    EnableNetworkFlag(3478)
    EnableNetworkFlag(3498)
    EnableNetworkFlag(3518)
    EnableNetworkFlag(3538)
    EnableNetworkFlag(3558)
    EnableNetworkFlag(3578)
    EnableNetworkFlag(3598)
    EnableNetworkFlag(3618)
    EnableNetworkFlag(3638)
    EnableNetworkFlag(3678)
    EnableNetworkFlag(3718)
    EnableNetworkFlag(3738)
    EnableNetworkFlag(3758)
    EnableNetworkFlag(3778)
    EnableNetworkFlag(3798)
    EnableNetworkFlag(3818)
    EnableNetworkFlag(3838)
    EnableNetworkFlag(3878)
    EnableNetworkFlag(3898)
    EnableNetworkFlag(3918)
    EnableNetworkFlag(3938)
    EnableNetworkFlag(3958)
    EnableNetworkFlag(3978)
    EnableNetworkFlag(3998)
    EnableNetworkFlag(4018)
    EnableNetworkFlag(4038)
    EnableNetworkFlag(4058)
    EnableNetworkFlag(4078)
    EnableNetworkFlag(4098)
    EnableNetworkFlag(4118)
    EnableNetworkFlag(4138)
    EnableNetworkFlag(4158)
    EnableNetworkFlag(4178)
    EnableNetworkFlag(4198)
    EnableNetworkFlag(4218)
    EnableNetworkFlag(4238)
    EnableNetworkFlag(4258)
    EnableNetworkFlag(4278)
    EnableNetworkFlag(4298)
    EnableNetworkFlag(4318)
    EnableNetworkFlag(4338)
    EnableNetworkFlag(4358)
    EnableNetworkFlag(4378)
    EnableNetworkFlag(4398)
    EnableNetworkFlag(4418)
    EnableNetworkFlag(4438)
    EnableNetworkFlag(4458)
    EnableNetworkFlag(4478)
    EnableNetworkFlag(4498)
    EnableNetworkFlag(4518)
    EnableNetworkFlag(4538)
    EnableNetworkFlag(4558)
    EnableNetworkFlag(4578)
    EnableNetworkFlag(4598)
    EnableNetworkFlag(4718)
    EnableFlag(1037469277)
    SaveRequest()
    Restart()
