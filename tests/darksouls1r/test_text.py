import shutil
import unittest

from soulstruct.config import DSR_PATH
from soulstruct.containers.bnd import BND
from soulstruct.darksouls1r.text import MSGDirectory


class TextTest(unittest.TestCase):
    
    def test_text(self):
        item_msgbnd = BND(DSR_PATH / "msg/ENGLISH/item.msgbnd.dcx")
        print("item.msgbnd.dcx:")
        for entry_id, entry in item_msgbnd.entries_by_id.items():
            print(f"    {entry_id}: {entry.path}")
    
        menu_msgbnd = BND(DSR_PATH / "msg/ENGLISH/menu.msgbnd.dcx")
        print("menu.msgbnd.dcx:")
        for entry_id, entry in menu_msgbnd.entries_by_id.items():
            print(f"    {entry_id}: {entry.path}")
    
        dsr_text = MSGDirectory(DSR_PATH / "msg" / "ENGLISH")
        print(dsr_text.WeaponNames[9014000])
        print(("WeaponNames", 9014000) in dsr_text._is_patch)
    
        dsr_text.write("_test_dsr_text", separate_patch=True)
    
        item_msgbnd = BND("test_dsr_text/item.msgbnd.dcx")
        print("item.msgbnd.dcx:")
        for entry_id, entry in item_msgbnd.entries_by_id.items():
            print(f"    {entry_id}: {entry.path}")
    
        menu_msgbnd = BND("test_dsr_text/menu.msgbnd.dcx")
        print("menu.msgbnd.dcx:")
        for entry_id, entry in menu_msgbnd.entries_by_id.items():
            print(f"    {entry_id}: {entry.path}")
    
        new_text = MSGDirectory("test_dsr_text")
        print(new_text.WeaponNames[9014000])
        print(("WeaponNames", 9014000) in new_text._is_patch)
        print(new_text._is_patch)
    
    def tearDown(self):
        shutil.rmtree("_test_dsr_text")
