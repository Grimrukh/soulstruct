import os
import unittest

from soulstruct.darksouls1r.maps.navmesh import NavmeshGraph


class NavmeshTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Depths NavmeshGraph (MCG, MCP, and MSB).
        - TODO
        """
        navmesh = NavmeshGraph("resources", msb_path="resources/m10_00_00_00.msb", map_id="m10_00_00_00")
        navmesh.draw()


if __name__ == '__main__':
    unittest.main()
