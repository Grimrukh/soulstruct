from soulstruct.config import BB_PATH
from soulstruct.bloodborne.events import EMEVD, EMEVDDirectory


def main():

    ed = EMEVDDirectory(BB_PATH + "/event")
    ed.write_evs("vanilla")
    chalice_dungeon = EMEVD(BB_PATH + "/event/m29.emevd.dcx")
    chalice_dungeon.write_evs("vanilla/m29.evs.py")

    # Test EVS read.
    EMEVDDirectory("vanilla")
    EMEVD("vanilla/m29.evs.py")
    print("Bloodborne `vanilla` events successfully written and re-read.")


if __name__ == '__main__':
    main()
