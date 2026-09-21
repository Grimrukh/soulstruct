"""Cutscene TAE (`RemoTAE`, format 0x1000B with 32-bit offsets) tests.

The vanilla round trip needs an unpacked DSR install (skipped otherwise); the from-scratch test does not.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from soulstruct.base.animations.tae import RemoTAE, RemoTAEAnimation, RemoTAEEvent, RemoTAEEventGroup
from soulstruct.containers import Binder, EntryNotFoundError


def _vanilla_remo_taes(dsr_root: Path) -> list[tuple[str, bytes]]:
    taes = []
    for path in sorted((dsr_root / "remo").glob("scn*.remobnd.dcx")):
        binder = Binder.from_path(path)
        try:
            entry = binder.find_entry_by_name_regex(r".*\.tae")
        except EntryNotFoundError:
            continue  # scn150010 has no TAE
        taes.append((path.name, entry.get_uncompressed_data()))
    return taes


def test_vanilla_remo_tae_byte_exact_round_trip(dsr_root: Path):
    """Every vanilla DSR cutscene TAE must survive `RemoTAE` read -> write byte for byte."""
    taes = _vanilla_remo_taes(dsr_root)
    assert len(taes) >= 100, "expected the full set of vanilla DSR cutscenes"
    mismatches = []
    for name, data in taes:
        tae = RemoTAE.from_bytes(data)
        out = bytes(tae)
        if out != data:
            first = next((i for i in range(min(len(out), len(data))) if out[i] != data[i]), min(len(out), len(data)))
            mismatches.append(f"{name}: first difference at 0x{first:X} (sizes {len(data)} -> {len(out)})")
    assert not mismatches, "\n".join(mismatches)


def test_vanilla_remo_tae_conventions(dsr_root: Path):
    """Facts the from-scratch builder relies on: cut animations exist per cut, constant header values."""
    for name, data in _vanilla_remo_taes(dsr_root)[:20]:
        tae = RemoTAE.from_bytes(data)
        assert tae.flags == [1, 0, 1, 2, 2, 1, 1, 1], name
        assert tae.unk_x20 == 0x10002, name
        assert tae.animations, name
        assert [a.animation_id for a in tae.animations] == sorted(a.animation_id for a in tae.animations), name


def test_remo_tae_from_scratch_round_trip():
    tae = RemoTAE.new([10, 20, 35])
    assert [a.animation_id for a in tae.animations] == [10, 20, 35]
    data = bytes(tae)
    reread = RemoTAE.from_bytes(data)
    assert [a.animation_id for a in reread.animations] == [10, 20, 35]
    assert all(not a.events and not a.event_groups for a in reread.animations)
    assert bytes(reread) == data


def test_remo_tae_events_and_groups_round_trip():
    """Events with and without payloads, grouped with and without group payloads, plus consecutive animation IDs."""
    animation = RemoTAEAnimation(
        animation_id=20,
        events=[
            RemoTAEEvent(0, 0.0, 0.6667, bytes(16)),
            RemoTAEEvent(198, 0.0, 2.0, bytes.fromhex("1f001f00") + bytes(12)),
            RemoTAEEvent(161, 0.0, 33.3),  # no payload
            RemoTAEEvent(210, 1.0, 33.3, b"\xff" * 12 + bytes(20)),  # 32-byte payload
        ],
        event_groups=[
            RemoTAEEventGroup(0, [0]),
            RemoTAEEventGroup(192, [1, 3]),
            RemoTAEEventGroup(128, [2], bytes.fromhex("00000000" "0000ffff") + bytes(8)),
        ],
        animation_file_name="a0020.HKXwin",
    )
    tae = RemoTAE(animations=[animation, RemoTAEAnimation(21), RemoTAEAnimation(99999)])
    data = bytes(tae)
    reread = RemoTAE.from_bytes(data)
    assert bytes(reread) == data
    anim = reread.get_animation(20)
    assert repr(anim.events) == repr(animation.events)
    assert repr(anim.event_groups) == repr(animation.event_groups)
    assert anim.animation_file_name == "a0020.HKXwin"
    assert anim.get_event_times() == pytest.approx([0.0, 0.6667, 1.0, 2.0, 33.3], abs=1e-6)


def test_remo_tae_rejects_character_tae_version():
    data = bytearray(bytes(RemoTAE.new([10])))
    data[8:12] = (0x1000C).to_bytes(4, "little")
    with pytest.raises(ValueError, match="0x1000C"):
        RemoTAE.from_bytes(bytes(data))
