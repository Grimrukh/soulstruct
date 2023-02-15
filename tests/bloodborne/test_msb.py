import os
import unittest

from soulstruct.bloodborne.maps import MSB


class MSBTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Hunter's Dream MSB.
        - Copying Moon Presence character, 'c5400_0000'.
        - Writing the MSB.
        - Re-opening that new MSB.
        - Comparing every entry field.
        """
        msb = MSB.from_path("m21_00_00_00.msb.dcx")
        source_chr = msb.characters.find_entry_name("c5400_0000")
        msb.characters.duplicate(
            source_chr, name="c5400_0000_COPY", entity_id=2100999, translate=(1.0, 2.0, 3.0)
        )
        msb.treasures.duplicate(0, name="TREASURE_0_COPY")
        msb.write("_test.msb.dcx")
        msb_reload = MSB.from_path("_test.msb.dcx")
        new_chr = msb_reload.characters.find_entry_name("c5400_0000_COPY")
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

    def test_json(self):
        msb = MSB.from_path("m21_00_00_00.msb.dcx")

        msb.write_json("_test_msb.json")
        msb_reload = MSB.from_json("_test_msb.json")

        for subtype in MSB.get_subtype_list_names():
            source_entries = msb[subtype]
            test_entries = msb_reload[subtype]
            self.assertEqual(len(source_entries), len(test_entries))
            for i, entry in enumerate(msb[subtype]):
                test_entry = test_entries[i]
                self.assertEqual(entry, test_entry)

    def tearDown(self) -> None:
        for file in ("_test.msb.dcx", "_test_msb.json"):
            try:
                os.remove(file)
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    unittest.main()
