from soulstruct.config import BB_PATH
from soulstruct.bloodborne.events import EMEVD, EMEVDDirectory


def main():

    ed = EMEVDDirectory(BB_PATH + "/event")
    ed.write_evs("vanilla")
    chalice_dungeon = EMEVD(BB_PATH + "/event/m29.emevd.dcx")
    chalice_dungeon.write_evs("vanilla/m29.evs.py")

    # For fun.
    from pathlib import Path
    lines = 0
    chalice_lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text(encoding="utf-8").splitlines())
        if evs_file.name == "m29.evs.py":
            chalice_lines = len(evs_file.read_text(encoding="utf-8").splitlines())

    # Test EVS read.
    EMEVDDirectory("vanilla")
    EMEVD("vanilla/m29.evs.py")
    print("Bloodborne `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines} ({lines - chalice_lines} excluding m29)")


if __name__ == '__main__':
    main()
