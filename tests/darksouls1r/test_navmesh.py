import unittest

from soulstruct.darksouls1r.maps import MSB
from soulstruct.darksouls1r.maps.navmesh import NavmeshGraph


class NavmeshTest(unittest.TestCase):

    def test_rewrite(self):
        """Test:

        - Opening the (vanilla) Depths NavGraph (MCG, MCP, and MSB).
        """
        navmesh = NavmeshGraph(
            map_path="resources",
            msb=MSB.from_path("resources/m10_00_00_00.msb"),
            map_stem="m10_00_00_00",
        )
        navmesh.draw()


if __name__ == '__main__':
    unittest.main()
