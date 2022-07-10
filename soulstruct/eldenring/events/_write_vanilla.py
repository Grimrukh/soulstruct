from soulstruct.eldenring.events import EMEVDDirectory
from soulstruct.config import ELDEN_RING_PATH


def main():
    ed = EMEVDDirectory(ELDEN_RING_PATH + "/../../ELDEN RING (Vanilla Unpacked)/Game/event")
    ed.write_evs("vanilla")

    # For fun.
    from pathlib import Path
    lines = 0
    for evs_file in Path("vanilla").glob("*.evs.py"):
        lines += len(evs_file.read_text().splitlines())

    # Test EVS read.
    EMEVDDirectory("vanilla")
    print("ER `vanilla` events successfully written and re-read.")
    print(f"Total EVS line count: {lines}")


if __name__ == '__main__':
    main()
