__all__ = ["print_hitbox_info"]

import typing as tp
from soulstruct.models.darksouls1 import PLAYER_WEAPON_BEHAVIOR_VARIATIONS, BEHAVIOR_SUB_ID

if tp.TYPE_CHECKING:
    from soulstruct.params.dark_souls_params import DarkSoulsGameParameters


def print_hitbox_info(params: DarkSoulsGameParameters):
    current_var_id = None
    for b_id, b_entry in params.PlayerBehaviors.items():
        if b_id > 100000:
            if current_var_id != b_entry["variationId"]:
                current_var_id = b_entry["variationId"]
                print(f"{PLAYER_WEAPON_BEHAVIOR_VARIATIONS[current_var_id]} ({current_var_id})")
            sub_id = b_entry["behaviorJudgeId"]
            sub_name = BEHAVIOR_SUB_ID.get(sub_id, "UNKNOWN")
            if b_entry["refType"] == 0:
                attack_id = b_entry["refId"]
                try:
                    attack_param = params.PlayerAttacks[b_entry["refId"]]
                except KeyError:
                    print(f"    {sub_id}: {sub_name} -> Attack {attack_id} (DOES NOT EXIST!)")
                    continue
                print(f"    {sub_id}: {sub_name} -> Attack {attack_id}")
                for i in range(4):
                    start_point = attack_param[f"hit{i}_DmyPoly1"]
                    if start_point != -1:
                        end_point = attack_param[f"hit{i}_DmyPoly2"]
                        radius = attack_param[f"hit{i}_Radius"]
                        print(f"         {i}. R = {radius:.3f}")
                        print(f"         {i}. Dmy = ({start_point}, {end_point})")
