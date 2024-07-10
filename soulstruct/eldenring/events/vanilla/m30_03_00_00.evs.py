"""
Road's End Catacombs

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
from soulstruct.eldenring.game_types import *
from .enums.m30_03_00_00_enums import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    CommonFunc_90005646(
        0,
        flag=30030800,
        left_flag=30032840,
        cancel_flag__right_flag=30032841,
        asset=Assets.AEG099_065_9000,
        player_start=30032840,
        area_id=30,
        block_id=3,
        cc_id=0,
        dd_id=0,
    )
    RegisterGrace(grace_flag=300300, asset=Assets.AEG099_060_9001)
    Event_30032800()
    Event_30032810()
    Event_30032849()
    Event_30032821()
    Event_30032838()
    Event_30032890()
    Event_30032845()
    Event_30032870(0, character=Characters.CrucibleKnight0, flag=30032882)
    Event_30032871(0, character=Characters.CrucibleKnight3, flag=30032883)
    Event_30032871(1, character=Characters.CrucibleKnight4, flag=30032884)
    Event_30032871(2, character=Characters.CrucibleKnight5, flag=30032884)
    Event_30032871(3, character=Characters.CrucibleKnight1, flag=30032885)
    Event_30032871(4, character=Characters.CrucibleKnight2, flag=30032885)
    Event_30032871(5, character=Characters.CrucibleKnight6, flag=30032886)
    Event_30032871(6, character=Characters.CrucibleKnight7, flag=30032886)
    Event_30032871(7, character=Characters.CrucibleKnight8, flag=30032887)
    Event_30032871(8, character=Characters.CrucibleKnight9, flag=30032887)
    CommonFunc_90005650(
        0,
        flag=30030540,
        asset=Assets.AEG027_041_0500,
        asset_1=Assets.AEG027_115_0500,
        obj_act_id=30033541,
        obj_act_id_1=27115,
    )
    CommonFunc_90005651(0, flag=30030540, anchor_entity=Assets.AEG027_041_0500)
    Event_30032400(
        0,
        owner_entity=Characters.TalkDummy2,
        entity=Assets.AEG027_044_0500,
        region=30032600,
        behavior_id=0,
        source_entity=30032601,
        source_entity_1=30032602,
        source_entity_2=30032603,
    )
    CommonFunc_90005525(0, flag=30030570, asset=Assets.AEG027_157_0500)
    CommonFunc_90005525(0, flag=30030571, asset=Assets.AEG027_157_0501)
    CommonFunc_90005525(0, flag=30030572, asset=Assets.AEG027_157_0502)
    CommonFunc_90005525(0, flag=30030573, asset=Assets.AEG027_157_0503)
    CommonFunc_90005525(0, flag=30030574, asset=Assets.AEG027_157_0504)
    CommonFunc_90005525(0, flag=30030575, asset=Assets.AEG027_157_0505)
    CommonFunc_90005525(0, flag=30030576, asset=Assets.AEG027_157_0506)
    CommonFunc_90005525(0, flag=30030577, asset=Assets.AEG027_157_0507)
    Event_30032579()
    CommonFunc_90005410(0, flag=30032100, character=30031100, entity_b=30035100)
    CommonFunc_90005411(0, asset=Assets.AEG099_053_9000, character=Characters.TalkDummy1, left=10)
    CommonFunc_91005600(0, flag=30030800, asset=30031695, vfx_id=3)
    CommonFunc_90005920(0, flag=30030520, asset=Assets.AEG099_630_9000, obj_act_id=30033520)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_30030050()
    CommonFunc_90005250(0, character=Characters.Imp0, region=30032200, seconds=0.0, animation_id=3005)
    CommonFunc_90005261(0, character=Characters.Imp1, region=30032201, radius=1.0, seconds=0.0, animation_id=3012)
    CommonFunc_90005211(
        0,
        character=Characters.Imp2,
        animation_id=30010,
        animation_id_1=20010,
        region=30032202,
        radius=5.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005200(
        0,
        character=Characters.Imp3,
        animation_id=30001,
        animation_id_1=20001,
        region=30032203,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005201(
        0,
        character=Characters.Imp4,
        animation_id=30010,
        animation_id_1=20010,
        radius=15.0,
        seconds=2.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30032205(
        0,
        character=Characters.Imp5,
        animation_id=30010,
        animation_id_1=20010,
        region=30032204,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    Event_30032205(
        1,
        character=Characters.Imp6,
        animation_id=30010,
        animation_id_1=20010,
        region=30032204,
        radius=1.0,
        seconds=0.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )
    CommonFunc_90005250(0, character=Characters.Imp7, region=30032207, seconds=0.0, animation_id=0)
    CommonFunc_90005250(0, character=Characters.Imp8, region=30032208, seconds=0.0, animation_id=0)
    Event_30032207(0, character=Characters.Imp7, region=30032307)
    Event_30032207(1, character=Characters.Imp8, region=30032308)
    Event_30032207(2, character=Characters.Imp9, region=30032307)
    CommonFunc_90005200(
        0,
        character=Characters.Imp9,
        animation_id=30002,
        animation_id_1=20002,
        region=30032207,
        seconds=3.0,
        left=0,
        left_1=0,
        left_2=0,
        left_3=0,
    )


@ContinueOnRest(30030050)
def Event_30030050():
    """Event 30030050"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(30030500)


@RestartOnRest(30032579)
def Event_30032579():
    """Event 30032579"""
    DisableAsset(Assets.AEG027_157_0505)


@RestartOnRest(30032400)
def Event_30032400(
    _,
    owner_entity: uint,
    entity: uint,
    region: Region | int,
    behavior_id: int,
    source_entity: uint,
    source_entity_1: uint,
    source_entity_2: uint,
):
    """Event 30032400"""
    CreateProjectileOwner(entity=owner_entity)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, 1, wait_for_completion=True)
    Wait(0.5)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L0)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L1)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(0.6000000238418579)
    if ValueNotEqual(left=behavior_id, right=0):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=behavior_id,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        Goto(Label.L2)
    if FlagEnabled(50):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032000,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(51):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032010,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(52):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032020,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(53):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032030,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(54):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032040,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(55):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032050,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(56):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032060,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
    if FlagEnabled(57):
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_1,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )
        ShootProjectile(
            owner_entity=owner_entity,
            source_entity=source_entity_2,
            dummy_id=-1,
            behavior_id=801032070,
            launch_angle_x=0,
            launch_angle_y=0,
            launch_angle_z=0,
        )

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(3.0)
    
    MAIN.Await(AllPlayersOutsideRegion(region=region))
    
    ForceAnimation(entity, 3, wait_for_completion=True)
    Restart()


@RestartOnRest(30032205)
def Event_30032205(
    _,
    character: uint,
    animation_id: int,
    animation_id_1: int,
    region: Region | int,
    radius: float,
    seconds: float,
    left: uint,
    left_1: uint,
    left_2: uint,
    left_3: uint,
):
    """Event 30032205"""
    EndIffSpecialStandbyEndedFlagEnabled(character=character)
    if UnsignedNotEqual(left=left, right=0):
        DisableGravity(character)
        DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BluePhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    if UnsignedNotEqual(left=0, right=region):
        OR_3.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    OR_11.Add(CharacterHasSpecialEffect(character, 5080))
    OR_11.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_11)
    AND_9.Add(UnsignedEqual(left=left_1, right=0))
    AND_9.Add(UnsignedEqual(left=left_2, right=0))
    AND_9.Add(UnsignedEqual(left=left_3, right=0))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    if UnsignedNotEqual(left=left_1, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if UnsignedNotEqual(left=left_2, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown5))
    if UnsignedNotEqual(left=left_3, right=0):
        OR_9.Add(HasAIStatus(character, ai_status=AIStatusType.Unknown4))
    AND_1.Add(OR_9)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_4.Add(CharacterHasSpecialEffect(character, 481))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90110))
    AND_4.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterHasSpecialEffect(character, 482))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90120))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_5.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_6.Add(CharacterHasSpecialEffect(character, 483))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90140))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_6.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterHasSpecialEffect(character, 484))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90130))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90161))
    AND_7.Add(CharacterDoesNotHaveSpecialEffect(character, 90162))
    AND_8.Add(CharacterHasSpecialEffect(character, 487))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90100))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90150))
    AND_8.Add(CharacterDoesNotHaveSpecialEffect(character, 90160))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=436))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=2))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=5))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=6))
    OR_2.Add(CharacterHasStateInfo(character=character, state_info=260))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(0.10000000149011612)
    EnableThisNetworkSlotFlag()
    SetSpecialStandbyEndedFlag(character=character, state=True)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5080))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, loop=True)
    Wait(2.0)
    ForceAnimation(character, 3016, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if UnsignedNotEqual(left=left, right=0):
        EnableGravity(character)
        EnableCharacterCollision(character)
    End()


@RestartOnRest(30032207)
def Event_30032207(_, character: Character | int, region: Region | int):
    """Event 30032207"""
    OR_15.Add(CharacterDead(character))
    OR_15.Add(ThisEventSlotFlagEnabled())
    if OR_15:
        return
    AddSpecialEffect(character, 17155)
    AND_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_15.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_15)
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.Alive))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.GrayPhantom))
    OR_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.WhitePhantom))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_2)
    
    RemoveSpecialEffect(character, 17155)
    EnableThisNetworkSlotFlag()


@RestartOnRest(30032800)
def Event_30032800():
    """Event 30032800"""
    if FlagEnabled(30030800):
        return
    
    MAIN.Await(HealthValue(Characters.Snail) <= 0)
    
    Kill(Characters.CrucibleKnight0)
    Kill(Characters.CrucibleKnight3)
    Kill(Characters.CrucibleKnight4)
    Kill(Characters.CrucibleKnight5)
    Kill(Characters.CrucibleKnight1)
    Kill(Characters.CrucibleKnight2)
    Kill(Characters.CrucibleKnight6)
    Kill(Characters.CrucibleKnight7)
    Kill(Characters.CrucibleKnight8)
    Kill(Characters.CrucibleKnight9)
    DisableSpawner(entity=30033801)
    DisableSpawner(entity=30033802)
    DisableSpawner(entity=30033803)
    DisableSpawner(entity=30033804)
    DisableSpawner(entity=30033805)
    DisableSpawner(entity=30033806)
    Wait(4.0)
    PlaySoundEffect(Characters.Snail, 888880000, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(Characters.Snail))
    
    KillBossAndDisplayBanner(character=Characters.Snail, banner_type=BannerType.EnemyFelled)
    EnableFlag(30030800)
    if PlayerInOwnWorld():
        EnableFlag(61206)
    EnableFlag(9206)


@RestartOnRest(30032810)
def Event_30032810():
    """Event 30032810"""
    GotoIfFlagDisabled(Label.L0, flag=30030800)
    DisableCharacter(Characters.Snail)
    DisableAnimations(Characters.Snail)
    Kill(Characters.Snail)
    Kill(Characters.CrucibleKnight0)
    DisableSpawner(entity=30033801)
    DisableSpawner(entity=30033802)
    DisableSpawner(entity=30033803)
    DisableSpawner(entity=30033804)
    DisableSpawner(entity=30033805)
    DisableSpawner(entity=30033806)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(Characters.Snail)
    if PlayerInOwnWorld():
        ForceAnimation(Characters.Snail, 30013)
    AND_2.Add(FlagEnabled(30032805))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=30032800))
    
    MAIN.Await(AND_2)
    
    EnableAI(Characters.Snail)
    SetNetworkUpdateRate(Characters.Snail, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(Characters.Snail, name=904140300)
    GotoIfPlayerNotInOwnWorld(Label.L1)
    DisableNetworkConnectedFlagRange(flag_range=(30032822, 30032839))
    EnableNetworkFlag(30032822)
    EnableNetworkFlag(30032839)
    Wait(1.2000000476837158)
    EnableFlag(30032812)
    ForceSpawnerToSpawn(spawner=30033801)
    EnableNetworkFlag(30032882)
    ForceAnimation(Characters.Snail, 20013)

    # --- Label 1 --- #
    DefineLabel(1)


@RestartOnRest(30032849)
def Event_30032849():
    """Event 30032849"""
    CommonFunc_9005800(
        0,
        flag=30030800,
        entity=Assets.AEG099_001_9000,
        region=30032800,
        flag_1=30032805,
        character=30035800,
        action_button_id=10000,
        left=0,
        region_1=0,
    )
    CommonFunc_9005801(
        0,
        flag=30030800,
        entity=Assets.AEG099_001_9000,
        region=30032800,
        flag_1=30032805,
        flag_2=30032806,
        action_button_id=10000,
    )
    CommonFunc_9005811(0, flag=30030800, asset=Assets.AEG099_001_9000, vfx_id=3, right=0)
    CommonFunc_9005822(
        0,
        flag=30030800,
        bgm_boss_conv_param_id=920200,
        flag_1=30032805,
        flag_2=30032806,
        right=0,
        flag_3=30032860,
        left=0,
        left_1=0,
    )


@RestartOnRest(30032890)
def Event_30032890():
    """Event 30032890"""
    DisableNetworkSync()
    if FlagEnabled(30030800):
        return
    if PlayerNotInOwnWorld():
        return
    AwaitFlagEnabled(flag=30032805)
    GotoIfFlagEnabled(Label.L1, flag=30032813)
    
    MAIN.Await(CharacterDead(Characters.CrucibleKnight0))
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)
    AND_1.Add(HealthRatio(Characters.Snail) < 0.8999999761581421)
    SkipLinesIfConditionTrue(4, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(30032822, 30032839))
    EnableNetworkFlag(30032822)
    EnableNetworkFlag(30032839)
    Goto(Label.L0)
    DisableNetworkFlag(30032822)
    EnableNetworkFlag(30032813)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L2, flag=30032814)
    
    MAIN.Await(CharacterDead(Characters.CrucibleKnight3))
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)
    EnableNetworkFlag(30032814)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagEnabled(Label.L10, flag=30032815)
    AND_9.Add(CharacterDead(Characters.CrucibleKnight4))
    AND_9.Add(CharacterDead(Characters.CrucibleKnight5))
    
    MAIN.Await(AND_9)
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)
    EnableNetworkFlag(30032815)
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L11, flag=30032816)
    AND_10.Add(CharacterDead(Characters.CrucibleKnight1))
    AND_10.Add(CharacterDead(Characters.CrucibleKnight2))
    
    MAIN.Await(AND_10)
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)
    EnableNetworkFlag(30032816)
    Goto(Label.L0)

    # --- Label 11 --- #
    DefineLabel(11)
    GotoIfFlagEnabled(Label.L12, flag=30032817)
    AND_2.Add(CharacterDead(Characters.CrucibleKnight6))
    AND_2.Add(CharacterDead(Characters.CrucibleKnight7))
    
    MAIN.Await(AND_2)
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)
    EnableNetworkFlag(30032817)
    Goto(Label.L0)

    # --- Label 12 --- #
    DefineLabel(12)
    AND_11.Add(CharacterDead(Characters.CrucibleKnight8))
    AND_11.Add(CharacterDead(Characters.CrucibleKnight9))
    
    MAIN.Await(AND_11)
    
    Wait(1.0)
    AddSpecialEffect(Characters.Snail, 15044)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterHasSpecialEffect(Characters.Snail, 15007))
    
    AND_3.Add(HealthRatio(Characters.Snail) >= 0.8999999761581421)
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    ForceSpawnerToSpawn(spawner=30033801)
    
    MAIN.Await(CharacterAlive(Characters.CrucibleKnight0))
    
    EnableNetworkFlag(30032882)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L9, flag=30032817)
    ForceSpawnerToSpawn(spawner=30033806)
    AND_8.Add(CharacterAlive(Characters.CrucibleKnight8))
    AND_8.Add(CharacterAlive(Characters.CrucibleKnight9))
    
    MAIN.Await(AND_8)
    
    EnableNetworkFlag(30032887)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L8, flag=30032816)
    ForceSpawnerToSpawn(spawner=30033805)
    AND_6.Add(CharacterAlive(Characters.CrucibleKnight6))
    AND_6.Add(CharacterAlive(Characters.CrucibleKnight7))
    
    MAIN.Await(AND_6)
    
    EnableNetworkFlag(30032886)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    GotoIfFlagDisabled(Label.L4, flag=30032815)
    ForceSpawnerToSpawn(spawner=30033804)
    AND_5.Add(CharacterAlive(Characters.CrucibleKnight1))
    AND_5.Add(CharacterAlive(Characters.CrucibleKnight2))
    
    MAIN.Await(AND_5)
    
    EnableNetworkFlag(30032885)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L5, flag=30032814)
    ForceSpawnerToSpawn(spawner=30033803)
    EnableFlag(30032860)
    AND_7.Add(CharacterAlive(Characters.CrucibleKnight4))
    AND_7.Add(CharacterAlive(Characters.CrucibleKnight5))
    
    MAIN.Await(AND_7)
    
    EnableNetworkFlag(30032884)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    GotoIfFlagDisabled(Label.L6, flag=30032813)
    ForceSpawnerToSpawn(spawner=30033802)
    
    MAIN.Await(CharacterAlive(Characters.CrucibleKnight3))
    
    EnableNetworkFlag(30032883)
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    GotoIfFlagDisabled(Label.L7, flag=30032812)
    ForceSpawnerToSpawn(spawner=30033801)
    EnableNetworkFlag(30032882)
    
    MAIN.Await(CharacterAlive(Characters.CrucibleKnight0))
    
    AddSpecialEffect(Characters.Snail, 15045)
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)


@RestartOnRest(30032845)
def Event_30032845():
    """Event 30032845"""
    DisableNetworkSync()
    if FlagEnabled(30030800):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(HealthRatio(Characters.Snail) < 0.8999999761581421)
    
    DisableNetworkFlag(30032822)
    EnableNetworkFlag(30032834)


@RestartOnRest(30032821)
def Event_30032821():
    """Event 30032821"""
    DisableNetworkSync()
    if FlagEnabled(30030800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_15.Add(CharacterHasSpecialEffect(Characters.Snail, 15046))
    AND_15.Add(FlagEnabled(30032839))
    
    MAIN.Await(AND_15)
    
    OR_15.Add(HealthRatio(Characters.Snail) >= 0.8999999761581421)
    GotoIfConditionTrue(Label.L0, input_condition=OR_15)
    GotoIfFlagEnabled(Label.L0, flag=30032822)
    GotoIfFlagEnabled(Label.L1, flag=30032823)
    GotoIfFlagEnabled(Label.L1, flag=30032824)
    GotoIfFlagEnabled(Label.L1, flag=30032825)
    GotoIfFlagEnabled(Label.L2, flag=30032826)
    GotoIfFlagEnabled(Label.L2, flag=30032827)
    GotoIfFlagEnabled(Label.L2, flag=30032828)
    GotoIfFlagEnabled(Label.L3, flag=30032829)
    GotoIfFlagEnabled(Label.L3, flag=30032830)
    GotoIfFlagEnabled(Label.L3, flag=30032831)
    GotoIfFlagEnabled(Label.L4, flag=30032832)
    GotoIfFlagEnabled(Label.L4, flag=30032833)
    GotoIfFlagEnabled(Label.L4, flag=30032834)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032829, 30032834))
    DisableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032829, 30032834))
    DisableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032823, 30032828))
    DisableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableNetworkConnectedFlagRange(flag_range=(30032823, 30032834))
    EnableRandomFlagInRange(flag_range=(30032823, 30032828))
    DisableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()


@ContinueOnRest(30032838)
def Event_30032838():
    """Event 30032838"""
    DisableNetworkSync()
    if FlagEnabled(30030800):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(30032823, 30032834)))
    AND_1.Add(FlagDisabled(30032839))
    AND_1.Add(CharacterHasSpecialEffect(Characters.Snail, 15046))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=30032822)
    GotoIfFlagEnabled(Label.L1, flag=30032823)
    GotoIfFlagEnabled(Label.L2, flag=30032824)
    GotoIfFlagEnabled(Label.L3, flag=30032825)
    GotoIfFlagEnabled(Label.L4, flag=30032826)
    GotoIfFlagEnabled(Label.L5, flag=30032827)
    GotoIfFlagEnabled(Label.L6, flag=30032828)
    GotoIfFlagEnabled(Label.L7, flag=30032829)
    GotoIfFlagEnabled(Label.L8, flag=30032830)
    GotoIfFlagEnabled(Label.L9, flag=30032831)
    GotoIfFlagEnabled(Label.L10, flag=30032832)
    GotoIfFlagEnabled(Label.L11, flag=30032833)
    GotoIfFlagEnabled(Label.L12, flag=30032834)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableNetworkFlag(30032839)
    DisableNetworkFlag(30032822)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    Move(Characters.Snail, destination=30032823, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(Characters.Snail, destination=30032824, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 3 --- #
    DefineLabel(3)
    Move(Characters.Snail, destination=30032825, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 4 --- #
    DefineLabel(4)
    Move(Characters.Snail, destination=30032826, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 5 --- #
    DefineLabel(5)
    Move(Characters.Snail, destination=30032827, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 6 --- #
    DefineLabel(6)
    Move(Characters.Snail, destination=30032828, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 7 --- #
    DefineLabel(7)
    Move(Characters.Snail, destination=30032829, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 8 --- #
    DefineLabel(8)
    Move(Characters.Snail, destination=30032830, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    Move(Characters.Snail, destination=30032831, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 10 --- #
    DefineLabel(10)
    Move(Characters.Snail, destination=30032832, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 11 --- #
    DefineLabel(11)
    Move(Characters.Snail, destination=30032833, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()

    # --- Label 12 --- #
    DefineLabel(12)
    Move(Characters.Snail, destination=30032834, destination_type=CoordEntityType.Region, set_draw_parent=30034200)
    EnableNetworkFlag(30032839)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(Characters.Snail, 15046))
    
    Restart()


@RestartOnRest(30032870)
def Event_30032870(_, character: Character | int, flag: Flag | int):
    """Event 30032870"""
    if FlagEnabled(30030800):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(character))
    
    MAIN.Await(AND_1)
    
    Wait(1.0)
    ActivateMultiplayerBuffs(character)
    
    MAIN.Await(CharacterDead(character))
    
    Restart()


@RestartOnRest(30032871)
def Event_30032871(_, character: Character | int, flag: Flag | int):
    """Event 30032871"""
    if FlagEnabled(30030800):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterAlive(character))
    AND_2.Add(AND_1)
    AND_3.Add(Singleplayer())
    AND_2.Add(not AND_3)
    
    MAIN.Await(AND_2)
    
    ActivateMultiplayerBuffs(character)
    Wait(1.0)
    OR_1.Add(CharacterHasSpecialEffect(character, 7820))
    OR_1.Add(CharacterHasSpecialEffect(character, 7821))
    OR_1.Add(CharacterHasSpecialEffect(character, 7822))
    SkipLinesIfConditionTrue(1, OR_1)
    Restart()
