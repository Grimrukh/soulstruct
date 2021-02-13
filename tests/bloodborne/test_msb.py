import os
import unittest
from soulstruct.bloodborne.maps import MSB


class MSBTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Hunter's Dream MSB.
        - Copying Moon Presence character, 'c5400_0000'.
        - Changing the entity ID, translate, and rotate of the new bonfire.
        - Writing the MSB.
        - Re-opening that new MSB.
        - Comparing every entry field.
        """
        msb = MSB("m21_00_00_00.msb.dcx")
        msb.parts.new_character(
            copy_entry="c5400_0000", name="c5400_0000_COPY", entity_id=2100999, translate=(1.0, 2.0, 3.0)
        )
        msb.write("_test.msb.dcx")

        msb_reload = MSB("_test.msb.dcx")
        print(msb_reload.parts["c5400_0000_COPY"])
        for msb_type in ("parts", "regions", "events", "models"):
            source_entries = msb[msb_type].get_entries()
            test_entries = msb_reload[msb_type].get_entries()
            self.assertEqual(len(source_entries), len(test_entries))
            for i, entry in enumerate(msb[msb_type].get_entries()):
                test_entry = test_entries[i]
                for field_name in entry.field_names:
                    source_value = getattr(entry, field_name)
                    test_value = getattr(test_entry, field_name)
                    self.assertEqual(source_value, test_value)

    def tearDown(self):
        os.remove("_test.msb.dcx")


if __name__ == '__main__':
    unittest.main()
