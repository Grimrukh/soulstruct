import unittest

from soulstruct.containers.tpf import TPF


class TPFTest(unittest.TestCase):

    def test_tpf(self):
        tpf = TPF("resources/m10_00_arch_01.tpf.dcx")
        print(tpf)
        print(tpf.textures[0])
        dds_header = tpf.textures[0].get_dds_header()
        with open("_test_dds.dds", "wb") as f:
            f.write(tpf.textures[0].data)


if __name__ == '__main__':
    unittest.main()
