from soulstruct.config import BB_PATH
from soulstruct.bloodborne.events import EMEVD, EMEVDDirectory


def main():

    ed = EMEVDDirectory(BB_PATH + "/event")
    ed.write_evs("vanilla")
    chalice_dungeon = EMEVD(BB_PATH + "/event/m29.emevd.dcx")
    chalice_dungeon.write_evs("vanilla/m29.evs.py")


if __name__ == '__main__':
    main()
