import os
import unittest
from soulstruct.darksouls1ptde.maps import MSB


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
        msb = MSB("m10_00_00_00.msb")
        msb.parts.new_character(
            copy_entry="c1000_0000", name="c1000_0000_COPY", entity_id=1000999, translate=(1.0, 2.0, 3.0)
        )
        msb.events.new_treasure(copy_entry=0, name="TREASURE_0_COPY")
        msb.write("_test.msb")
        try:
            msb_reload = MSB("_test.msb")
            print(msb_reload.parts["c1000_0000_COPY"])
            print(msb_reload.events["TREASURE_0_COPY"])
            self.assertIs(msb_reload.events["TREASURE_0_COPY"], msb_reload.events.Treasure[1])
            for msb_type in ("parts", "regions", "events", "models"):
                source_entries = msb[msb_type].get_entries()
                test_entries = msb_reload[msb_type].get_entries()
                self.assertEqual(len(source_entries), len(test_entries))
                for i, entry in enumerate(msb[msb_type].get_entries()):
                    test_entry = test_entries[i]
                    for field_name in entry.field_names:
                        self.assertEqual(getattr(entry, field_name), getattr(test_entry, field_name))
        finally:
            os.remove("_test.msb")


if __name__ == '__main__':
    unittest.main()
