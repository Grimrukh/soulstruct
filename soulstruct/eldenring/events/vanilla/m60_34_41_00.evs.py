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


@ContinueOnRest(0)
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
    CommonFunc_90005640(0, flag=1034410540, asset=Assets.AEG239_001_2000)


@ContinueOnRest(1034412510)
def Event_1034412510():
    """Event 1034412510"""
    CommonFunc_90005500(
        0,
        flag=1034410510,
        flag_1=1034410511,
        left=1,
        asset=Assets.AEG239_010_2000,
        asset_1=Assets.AEG239_020_2000,
        obj_act_id=1034413511,
        asset_2=m12_04_Assets.AEG239_021_0500,
        obj_act_id_1=1034413512,
        region=1034412511,
        region_1=1034412512,
        flag_2=1034410512,
        flag_3=1034412513,
        left_1=0,
    )


@ContinueOnRest(1034410519)
def Event_1034410519():
    """Event 1034410519"""
    if FlagEnabled(1034410519):
        return
    DisableFlag(1034410510)
