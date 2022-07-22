"""
North Caelid (SW) (SE)

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
from .entities.m60_49_40_00_entities import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005560(0, flag=1049400600, asset=Assets.AEG099_635_9000, left=0)
    CommonFunc_90005251(0, character=Characters.PutridCorpse0, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.PutridCorpse1, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.PutridCorpse2, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.PutridCorpse3, radius=0.0, seconds=0.0, animation_id=-1)
    CommonFunc_90005251(0, character=Characters.PutridCorpse4, radius=0.0, seconds=0.0, animation_id=-1)
    Event_1049402390()
    CommonFunc_90005250(0, character=Characters.Omenkiller, region=1049402381, seconds=0.0, animation_id=-1)
    CommonFunc_900005610(0, asset=Assets.AEG099_090_9001, vfx_id=100, model_point=800, right=0)
    RunEvent(1049402650, slot=0, args=(0,))
    Event_1049400500()
    CommonFunc_90005511(0, flag=1049400560, asset=1049404550, obj_act_id=1049405560, obj_act_id_1=257013, left=0)
    CommonFunc_90005512(0, flag=1049400560, region=1049402550, region_1=1049402551)
    CommonFunc_90005640(0, flag=1049400540, asset=Assets.AEG239_001_2000)
    CommonFunc_90005706(0, 1049400700, 90100, 0)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableBackread(Characters.DragonbarrowSilentSpirit)
    Event_1046400510()


@RestartOnRest(1049402390)
def Event_1049402390():
    """Event 1049402390"""
    Kill(Characters.PutridCorpse0)
    Kill(Characters.PutridCorpse1)
    Kill(Characters.PutridCorpse2)
    Kill(Characters.PutridCorpse3)
    Kill(Characters.PutridCorpse4)


@ContinueOnRest(1046400510)
def Event_1046400510():
    """Event 1046400510"""
    if ThisEventSlotFlagEnabled():
        return


@RestartOnRest(1049400500)
def Event_1049400500():
    """Event 1049400500"""
    if FlagEnabled(12020570):
        return
    Wait(0.5)
    DisableAssetActivation(Assets.AEG239_020_2000, obj_act_id=227050)
    
    MAIN.Await(FlagEnabled(12020570))
    
    EnableAssetActivation(Assets.AEG239_020_2000, obj_act_id=227050)
