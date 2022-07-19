"""
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
from .entities.m60_51_58_00_entities import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005501(
        0,
        flag=1051580510,
        flag_1=1051580511,
        left=1,
        asset=Assets.AEG030_095_2000,
        asset_1=Assets.AEG030_183_2003,
        asset_2=Assets.AEG099_026_2001,
        flag_2=1051580512,
    )
    Event_1051582510()
    CommonFunc_90005706(0, 1051580700, 930023, 0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.WanderingNoble)


@NeverRestart(1051582510)
def Event_1051582510():
    """Event 1051582510"""
    CommonFunc_90005500(
        0,
        1051580510,
        1051580511,
        1,
        1051581510,
        1051581511,
        1051583511,
        1051581512,
        1051583512,
        1051582511,
        1051582512,
        1051580512,
        1051580513,
        0,
    )


@NeverRestart(1051580519)
def Event_1051580519():
    """Event 1051580519"""
    if ThisEventSlotFlagEnabled():
        return
    DisableFlag(1051580510)
