"""
Northwest Caelid (SE) (SW)

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
from .entities.m60_46_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1046400000, asset=Assets.AEG099_060_9000)
    RegisterGrace(grace_flag=1046400001, asset=Assets.AEG099_060_9001)
    CommonFunc_90005100(
        0,
        flag=76418,
        flag_1=76401,
        asset=Assets.AEG099_090_9000,
        source_flag=77400,
        value=0,
        flag_2=78400,
        flag_3=78401,
        flag_4=78402,
        flag_5=78403,
        flag_6=78404,
        flag_7=78405,
        flag_8=78406,
        flag_9=78407,
        flag_10=78408,
        flag_11=78409,
    )
    CommonFunc_90005790(
        0,
        right=0,
        flag=1046400180,
        summon_flag=1046402181,
        dismissal_flag=1046402182,
        character=Characters.AnastasiaTarnishedEater,
        sign_type=22,
        region=1046402701,
        region_1=1046402700,
        seconds=0.0,
        right_1=0,
        unknown=0,
        right_2=0,
    )
    CommonFunc_90005791(
        0,
        flag=1046400180,
        flag_1=1046402181,
        flag_2=1046402182,
        character=Characters.AnastasiaTarnishedEater,
    )
    CommonFunc_90005792(
        0,
        flag=1046400180,
        flag_1=1046402181,
        flag_2=1046402182,
        character=Characters.AnastasiaTarnishedEater,
        item_lot=1046400700,
        seconds=0.0,
    )
    CommonFunc_90005793(
        0,
        flag=1046400180,
        flag_1=1046402181,
        flag_2=1046402182,
        character=Characters.AnastasiaTarnishedEater,
        other_entity=1046402701,
        region=1046402182,
        left=0,
    )
    CommonFunc_90005250(0, character=Characters.PutridCorpseBare, region=1046402303, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse0, region=1046402301, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse1, region=1046402303, seconds=0.0, animation_id=-1)
    CommonFunc_90005250(0, character=Characters.PutridCorpse2, region=1046402303, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.LivingMass, radius=2.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005706(0, character=Characters.WanderingNoble, animation_id=930025, left=0)
    CommonFunc_90005631(0, anchor_entity=Assets.AEG099_376_1000, text=61011)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(1046400700)
    DisableBackread(Characters.WanderingNoble)
