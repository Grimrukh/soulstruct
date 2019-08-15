"""Script that creates the extra DrawParam slot in the DrawParam.parambnd resources for all maps.

In the vanilla game, only m15 (Sen's Fortress and Anor Londo) uses the additional DrawParam slot, but it works for all
maps. (Unfortunately, no more than two slots can be used.)
"""
import os
from soulstruct import BND

DRAW_PARAM_DIR = 'G:\\Steam\\steamapps\\common\\DARK SOULS REMASTERED\\params\\DrawParam'
REMASTERED = True

for map_id in (10, 11, 12, 13, 14, 16, 17, 18):  # skip 15, which already has both slots
    dcx = '.dcx' if REMASTERED else ''
    draw = BND(os.path.join(DRAW_PARAM_DIR, f'a{map_id}_DrawParam.parambnd{dcx}'))
    if len(list(draw)) == 12:
        s = draw[11]
        draw.remove_entry(11)
        for i in range(11):
            slot_0 = draw[i].copy()
            slot_0.id += 11
            draw[i].name = draw[i].name.replace(f'm{map_id}_', f'm{map_id}_1_')
            draw.add_entry(slot_0)
        s_0 = s.copy()
        s_0.id = 23
        s.name = s.name.replace(f's{map_id}_', f's{map_id}_1_')
        s.id = 22
        draw.add_entry(s)
        draw.add_entry(s_0)
    draw.write()
