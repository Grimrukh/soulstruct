import os
import unittest

from soulstruct.darksouls1r.maps.navinfo import NavInfo


class NavmeshTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Depths NavInfo (MCG, MCP, and MSB).
        - TODO
        """
        navmesh = NavInfo("resources", msb_source="resources/m10_00_00_00.msb", map_id="m10_00_00_00")
        navmesh.draw()


if __name__ == '__main__':
    unittest.main()
