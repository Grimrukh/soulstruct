"""Reads Matt's entity ID dump to vanilla `entities` modules.

Source: https://soulsmods.github.io/data/er/entities.html
"""

__all__ = [
    "create_vanilla_entities",
    "copy_vanilla_entities",
]

import re
import shutil
from pathlib import Path


CHARACTER_RE = re.compile(
    r"(?P<entity_id>\d+): (?P<map_id>m\d\d_\d\d_\d\d_\d\d) (?P<map_tile_id>m\d\d_\d\d_\d\d_\d\d-)?"
    r"(?P<name>c\d\d\d\d_\d\d\d\d) \(.*?\) (Enemy|Player) \((?P<chr_name>.*?)\) (?P<desc>.*)"
)
ASSET_RE = re.compile(
    r"(?P<entity_id>\d+): (?P<map_id>m\d\d_\d\d_\d\d_\d\d) (?P<map_tile_id>m\d\d_\d\d_\d\d_\d\d-)?"
    r"(?P<name>AEG[\d_]+) \(.*?\) Asset \((?P<desc>.*)\)"
)


def to_py_name(name: str):
    """Removes all incompatible characters from name."""
    invalid = " -,.'"
    for i in invalid:
        name = name.replace(i, "")
    if name in NEW_NAMES:
        return NEW_NAMES[name]
    if name[-1] in "0123456789":
        name += "_"  # for separating real number from instance number. Will be removed on write if necessary.
    return name


# Model names I prefer over Matt's.
NEW_NAMES = {
    "Rennala1": "RennalaPhaseOne",
    "Rennala2": "RennalaPhaseTwo",
    "DepravedPerfumer": "PerfumerTricia",
    "DepravedPerfumer2": "DepravedPerfumer",
    "PutridCorpse2": "PutridCorpseBare",
    "LargeCrab2": "LargeCrabInjured",
    "SmallCrab2": "SmallCrabWorms",
    "LargeCrab3": "LargeCrabSnow",
    "SmallCrab3": "SmallCrabCrystal",
    "Wormface1": "WormfaceSmall",
    "Wormface2": "WormfaceLarge",
    "LivingMass2": "LivingMassAlt",
}


def create_vanilla_entities(entities_dir: Path | str = None):

    entities = {}

    entities_dir = Path(entities_dir)
    if entities_dir is None:
        entities_dir = Path(__file__).parent / "vanilla/entities"
    entities_dir.mkdir(parents=True, exist_ok=True)

    for line in (Path(__file__).parent / "entities.txt").read_text(encoding="utf-8").split("\n"):
        if match := CHARACTER_RE.match(line):
            m = match.groupdict()
            entity_id = int(m["entity_id"])
            if entity_id == 0:
                continue
            if m["map_tile_id"]:
                map_id = m["map_tile_id"][:-1]  # removed trailing hyphen
            else:
                map_id = m["map_id"]
            if map_id not in entities:
                entities[map_id] = {"Characters": {}, "Assets": {}}
            d = entities[map_id]["Characters"]

            real_chr_name = to_py_name(m["chr_name"])
            if real_chr_name not in d and f"{real_chr_name}1" not in d:
                # First occurrence of this name. Don't use numerical suffix (yet).
                chr_name = real_chr_name
            elif real_chr_name in d:
                # Second occurrence of this name. Use "1" suffix and add "0" suffix to first occurrence.
                d[f"{real_chr_name}0"] = d.pop(real_chr_name)
                chr_name = f"{real_chr_name}1"
            else:
                # Third or later occurrence of this name.
                i = 2
                chr_name = f"{real_chr_name}{i}"
                while chr_name in d:
                    i += 1
                    chr_name = f"{real_chr_name}{i}"
            d[chr_name] = (entity_id, m["name"] + " " + m["desc"])
        elif match := ASSET_RE.match(line):
            m = match.groupdict()
            entity_id = int(m["entity_id"])
            if entity_id == 0:
                continue
            if m["map_tile_id"]:
                map_id = m["map_tile_id"][:-1]  # removed trailing hyphen
            else:
                map_id = m["map_id"]
            if map_id not in entities:
                entities[map_id] = {"Characters": {}, "Assets": {}}
            d = entities[map_id]["Assets"]
            d[m["name"]] = (entity_id, m["desc"])

    for map_id, map_entities in entities.items():
        module_string = "from soulstruct.eldenring.game_types import *\n\n\n"

        module_string += "class Characters(Character):\n"
        if not map_entities["Characters"]:
            module_string += "    pass\n\n\n"
        else:
            for name, (entity_id, desc) in map_entities["Characters"].items():
                module_string += f"    {name.rstrip('_')} = {entity_id}  # {desc}\n"
            module_string += "\n\n"

        module_string += "class Assets(Asset):\n"
        if not map_entities["Assets"]:
            module_string += "    pass\n"
        else:
            for name, (entity_id, desc) in map_entities["Assets"].items():
                module_string += f"    {name} = {entity_id}  # {desc}\n"

        (entities_dir / f"{map_id}_entities.py").write_text(module_string)


def copy_vanilla_entities(entities_dir: Path | str):
    """Save time by copying vanilla entities bundled in Soulstruct.

    May require updates when Elden Ring updates.
    """
    source_entities = Path(__file__).parent / "vanilla/entities"
    shutil.copytree(source_entities, entities_dir)


if __name__ == '__main__':
    create_vanilla_entities()
