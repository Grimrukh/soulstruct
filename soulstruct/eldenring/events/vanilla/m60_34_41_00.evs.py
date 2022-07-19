"""
Southwest Liurnia (SE) (NW)

linked:
0

strings:
0: N:\\GR\\data\\Param\\event\\common_func.emevd
82: 
84: 
86: 
88: 
90: 
92: 
94: 
"""
# [COMMON_FUNC]
from .common_func import *
from soulstruct.eldenring.events import *
from soulstruct.eldenring.events.instructions import *
from .entities.m60_34_41_00_entities import *
from .entities.m12_04_00_00_entities import Assets as m12_04_Assets


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterGrace(grace_flag=1034410000, asset=Assets.AEG099_060_9000)
    CommonFunc_90005501(
        0,
        flag=1034410510,
        flag_1=1034410511,
        left=1,
        asset=Assets.AEG239_010_2000,
        asset_1=Assets.AEG239_020_2000,
        asset_2=m12_04_Assets.AEG239_021_0500,
        flag_2=1034410512,
    )
    Event_1034412510()
    CommonFunc_90005640(0, 1034410540, 1034411540)


@NeverRestart(1034412510)
def Event_1034412510():
    """Event 1034412510"""
    CommonFunc_90005500(
        0,
        1034410510,
        1034410511,
        1,
        1034411510,
        1034411511,
        1034413511,
        1034411512,
        1034413512,
        1034412511,
        1034412512,
        1034410512,
        1034412513,
        0,
    )


@NeverRestart(1034410519)
def Event_1034410519():
    """Event 1034410519"""
    if FlagEnabled(1034410519):
        return
    DisableFlag(1034410510)
