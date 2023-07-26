from __future__ import annotations

__all__ = ["MapAreaTextureManager"]

import logging
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.models import FLVER
from soulstruct.containers import Binder, BinderEntry
from soulstruct.containers.tpf import TPF, TPFPlatform, TPFTexture, TextureType
from .msb import MSB

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MapAreaTextureManager:
    """Manages all the `TPF`-containing `BXF` binders for a map area (e.g. 'm10') in DSR.

    Main purpose is to keep track of which textures are loaded in maps in this area and to make sure all Map Pieces in
    any MSBs in this area have their textures present.

    Also manages the 'miscellaneous' `mXX_9999.tpf.dcx` TPF, which typically contains `EnvDif`/`EnvSpc` cube map DDS
    textures, water/sky textures, and other seemingly random textures.

    TODO: It's worth testing whether the game engine loads ALL `tpfbhd` binders it finds in this folder, or just all
     `mXX_####.tpfbhd` binders, or even just when #### is 0003 or less. If either of the latter, m12 must have an
     additional `m12dlc_####.tpfbhd` check hard-coded into the game engine too. But if the former, that would make it
     easier to keep all new Nightfall textures separate and prevent the binders from getting out of control (though
     given that we will want to *remove* old redundant textures, most binders will need to be changed from vanilla
     anyway).
    """

    # The vanilla TPF binders are separated into multiple binders (generally four) that each contain no more than this
    # many TPF entries. There is no total size limit. However, the game seems to be fine loading more than this many
    # textures, which is why thus far we've been adding them to the last binder (which is usually `mXX_0003.tpfbhd`).
    MAX_TPF_ENTRY_COUNT = 324  # i.e. last entry ID is 323

    map_directory: Path
    area_id: int

    # TODO: manage `GI_EnvM` environment event light map cubes?
    tpf_binders: dict[str, Binder] = field(default_factory=dict)
    tpf_9999: TPF | None = None

    def __post_init__(self):
        self._load_tpf_binders()
        self._load_tpf_9999()

    def check_msb_map_piece_textures(self):
        """Check all Map Pieces in all MSBs in this area to make sure their textures are present in the binders."""

        unused_textures = set()
        for tpf_binder in self.tpf_binders.values():
            for tpf_entry in tpf_binder.entries:
                unused_textures.add(tpf_entry.minimal_stem)
        if self.tpf_9999:
            for texture in self.tpf_9999.textures:
                if texture.name.startswith("EnvDif") or texture.name.startswith("EnvSpc"):
                    continue  # these are not used by Map Pieces and not managed here
                unused_textures.add(texture.name)

        msb_directory = self.map_directory / "MapStudio"

        for msb_path in msb_directory.glob(f"m{self.area_id:02}_*.msb.dcx"):
            map_piece_directory = self.map_directory / msb_path.name.split(".")[0]
            if not map_piece_directory.is_dir():
                _LOGGER.warning(f"Map Piece directory not found for MSB {msb_path.name}. Ignoring this MSB.")
                continue

            msb = MSB.from_path(msb_path)
            for map_piece_model in msb.map_piece_models:
                flver_path = map_piece_directory / f"{map_piece_model.name}A{self.area_id:02d}.flver.dcx"
                if not flver_path.is_file():
                    _LOGGER.warning(
                        f"Map Piece FLVER not found for Map Piece {map_piece_model.name} in MSB {msb_path.stem}."
                    )
                    continue
                flver = FLVER.from_path(flver_path)
                missing = self.check_map_piece_textures(flver)
                if missing:
                    _LOGGER.warning(
                        f"Map Piece FLVER {flver_path.name} in MSB {msb_path.stem} is missing textures in area:\n"
                        f"    {', '.join(missing)}"
                    )

    def check_map_piece_textures(self, map_piece_flver: FLVER) -> list[str]:
        """Returns a list of textures in this Map Piece FLVER model that are currently missing from area textures."""
        missing = []
        for material in map_piece_flver.materials:
            for texture in material.textures:
                if not self.has_texture(texture.stem):
                    missing.append(texture.stem)
        return missing

    def has_texture(self, texture_stem: str) -> bool:
        """Check if a texture is present in any of the binders or TPF 9999."""
        tpf_name = f"{texture_stem}.tpf.dcx"
        for binder in self.tpf_binders.values():
            if tpf_name in binder.entries_by_name:
                return True
        if self.tpf_9999:
            for texture in self.tpf_9999.textures:
                if texture_stem == texture.name:
                    return True

        # Texture not found.
        return False

    def add_texture(
        self,
        dds_path: str | Path,
        texture_format=1,
        texture_type=TextureType.Texture,
        mipmap_count=0,  # TODO: should this just be copied from the DDS header?
        texture_flags=0,
        to_tpf_9999=False,
        overwrite=False,
    ):
        """Add a DDS texture file to the binders (as a one-texture TPF) or TPF 9999 (as a straight DDS)."""
        dds_path = Path(dds_path)
        texture_stem = dds_path.stem
        texture_data = dds_path.read_bytes()

        texture = TPFTexture(
            name=texture_stem,
            format=texture_format,
            texture_type=texture_type,
            mipmap_count=mipmap_count,
            texture_flags=texture_flags,
            data=texture_data,
        )

        if to_tpf_9999:
            if self.tpf_9999 is None:
                self.tpf_9999 = self._get_tpf()
                existing = []
            else:
                existing = [tex for tex in self.tpf_9999.textures if tex.name == texture_stem]
            if existing:
                if not overwrite:
                    _LOGGER.warning(f"Texture {texture_stem} already present in TPF 9999. Not overwriting.")
                    return
                existing_index = self.tpf_9999.textures.index(existing[0])
                existing[existing_index] = texture
            else:
                self.tpf_9999.textures.append(texture)
            return

        # Add new TPF to binders, or replace existing binder entry.

        tpf = self._get_tpf(texture)

        for binder in self.tpf_binders.values():
            for entry in binder.entries:
                if texture_stem == entry.minimal_stem:
                    # Found existing texture with the same name.
                    if not overwrite:
                        _LOGGER.warning(f"Texture {texture_stem} already present in binders. Not overwriting.")
                        return
                    entry.set_from_binary_file(tpf)
                    _LOGGER.info(f"Replaced texture '{texture_stem}' in area TPF binder {binder.path.name}.")
                    return

        # Texture not found in any binders, so add it to the last-numbered binder (usually `mXX_0003.tpfbhd`).
        binder = sorted(self.tpf_binders.values(), key=lambda b: int(b.path.stem.split("_")[-1]))[-1]
        entry_id = binder.highest_entry_id + 1
        tpf_entry = BinderEntry(bytes(tpf), entry_id, f"\\{texture_stem}.tpf.dcx")
        binder.add_entry(tpf_entry)

    def _load_tpf_binders(self):
        for binder_path in self.area_directory.glob(f"m{self.area_id:02}*.tpfbhd"):
            binder = Binder.from_path(binder_path)
            self.tpf_binders[binder_path.name] = binder

    def _load_tpf_9999(self):
        tpf_9999_path = self.area_directory / f"m{self.area_id:02}_9999.tpf.dcx"
        self.tpf_9999 = TPF.from_path(tpf_9999_path) if tpf_9999_path.is_file() else None

    @staticmethod
    def _get_tpf(texture: TPFTexture = None) -> TPF:
        """Returns a new one-texture or zero-texture (default) TPF with the correct values for DSR."""
        return TPF(
            platform=TPFPlatform.PC,
            encoding_type=2,
            tpf_flags=3,
            textures=[texture] if texture is not None else [],
        )

    @property
    def area_directory(self) -> Path:
        return self.map_directory / f"m{self.area_id:02}"
