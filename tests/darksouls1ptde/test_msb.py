import os
import unittest

from soulstruct.darksouls1ptde.maps import MSB
from soulstruct.utilities.maths import Vector3


class MSBTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Depths MSB.
        - Copying the main bonfire character, 'c1000_0000'.
        - Changing the entity ID, translate, and rotate of the new bonfire.
        - Writing the MSB.
        - Re-opening that new MSB.
        - Comparing every entry field.
        """
        msb = MSB.from_path("m10_00_00_00.msb")
        source_chr = msb.characters.find_entry_name("c1000_0000")
        msb.characters.duplicate(
            source_chr, name="c1000_0000_COPY", entity_id=1000999, translate=Vector3(1.0, 2.0, 3.0)
        )
        msb.treasures.duplicate(0, name="TREASURE_0_COPY")
        msb.write("_test.msb")
        try:
            msb_reload = MSB.from_path("_test.msb")
            new_chr = msb_reload.characters.find_entry_name("c1000_0000_COPY")
            new_treasure = msb_reload.treasures.find_entry_name("TREASURE_0_COPY")
            print(new_chr)
            print(new_treasure)
            for subtype in MSB.get_subtype_list_names():
                source_entries = msb[subtype]
                test_entries = msb_reload[subtype]
                self.assertEqual(len(source_entries), len(test_entries))
                for i, entry in enumerate(msb[subtype]):
                    test_entry = test_entries[i]
                    self.assertEqual(entry, test_entry)
        finally:
            os.remove("_test.msb")

    def test_json(self):
        msb = MSB.from_path("m10_00_00_00.msb")

        try:
            msb.write_json("_test_msb.json")
            msb_reload = MSB.from_json("_test_msb.json")

            for subtype in MSB.get_subtype_list_names():
                source_entries = msb[subtype]
                test_entries = msb_reload[subtype]
                self.assertEqual(len(source_entries), len(test_entries))
                for i, entry in enumerate(msb[subtype]):
                    test_entry = test_entries[i]
                    self.assertEqual(entry, test_entry)
        finally:
            # os.remove("_test_msb.json")
            pass


if __name__ == '__main__':
    unittest.main()
