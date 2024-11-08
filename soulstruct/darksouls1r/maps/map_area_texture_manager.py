from __future__ import annotations

__all__ = ["MapAreaTextureManager"]

import logging
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.models import FLVER
from soulstruct.containers import Binder, BinderEntry
from soulstruct.containers.tpf import TPF, TPFPlatform, TPFTexture
from soulstruct.dcx import DCXType
from .msb import MSB

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MapAreaTextureManager:
    """Manages all the `TPF`-containing `BXF` binders for a map area (e.g. 'm10') in DSR.

    Main purpose is to keep track of which textures are loaded in maps in this area and to make sure all Map Pieces in
    any MSBs in this area have their textures present.

    Also manages the 'miscellaneous' `mXX_9999.tpf.dcx` TPF, which typically contains `EnvDif`/`EnvSpc` cube map DDS
    textures, water/sky textures, and sometimes other seemingly random textures.

    TODO: It's worth testing whether the game engine loads ALL `tpfbhd` binders it finds in this folder, or just all
     `mXX_####.tpfbhd` binders, or even just when #### is 0003 or less. If either of the latter, m12 must have an
     additional `m12dlc_####.tpfbhd` check hard-coded into the game engine too. But if the former, that would make it
     easier to keep all new Nightfall textures separate and prevent the binders from getting out of control (though
     given that we will want to *remove* old redundant textures, most binders will need to be changed from vanilla
     anyway).

    TODO: Is it possible that ALL loose TPF files in the directory are loaded, not just `mXX_9999.tpf.dcx`?
     Simple test: try renaming it for a map and see if the textures load.
    """

    # The vanilla TPF binders are separated into multiple binders (generally four) that each contain no more than this
    # many TPF entries. There is no total size limit. However, the game seems to be fine loading more than this many
    # textures, which is why thus far we've been adding them to the last binder (which is usually `mXX_0003.tpfbhd`).
    MAX_TPF_ENTRY_COUNT = 324  # i.e. last entry ID is 323

    map_directory: Path
    area_id: int
    tpfbhd_entries: dict[str, BinderEntry] = field(default_factory=dict)
    tpf_9999: TPF | None = None

    # By default, texture lookup is not case-sensitive, but you can change this if you want to enforce case sensitivity.
    case_sensitive: bool = False

    @classmethod
    def from_existing_area_directory(cls, map_directory: Path, area_id: int) -> MapAreaTextureManager:
        """Load all existing TPFBHDs and TPF 9999 from the given map area directory."""
        self = cls(map_directory, area_id)
        self._load_tpfbhd_entries()
        self._load_tpf_9999()
        return self

    def get_all_texture_stems(self) -> list[str]:
        """Return a list of all texture stems in a TPFBHD (as a `BinderEntry` stem) or inside TPF 9999.

        If `self.case_sensitive` is False, all stems are returned in lower case.
        """
        stems = list(self.tpfbhd_entries)
        if self.tpf_9999:
            stems.extend(texture.stem for texture in self.tpf_9999.textures)
        if not self.case_sensitive:
            return [stem.lower() for stem in stems]
        return stems

    def get_tpf_binder_entry(self, texture_stem: str) -> BinderEntry:
        """Find the `BinderEntry` in the TPFBHDs that contains the given texture stem.

        Does NOT check TPF 9999, which has no Binder.
        """
        if not self.case_sensitive:
            texture_stem = texture_stem.lower()
            for stem in self.tpfbhd_entries:
                if stem.lower() == texture_stem:
                    return self.tpfbhd_entries[stem]
            raise KeyError(f"Texture '{texture_stem}' (case-insensitive) not found in map area m{self.area_id:02}.")
        try:
            return self.tpfbhd_entries[texture_stem]
        except KeyError:
            raise KeyError(f"Texture '{texture_stem}' (case-sensitive) not found in map area m{self.area_id:02}.")

    def get_tpf(self, texture_stem: str) -> TPF:
        """Find the `TPF` in the TPFBHDs that contains the given texture stem."""
        binder_entry = self.get_tpf_binder_entry(texture_stem)  # will raise KeyError if not found
        return TPF.from_binder_entry(binder_entry)

    def get_tpf_9999_texture(self, texture_stem: str) -> TPFTexture:
        """Find the `TPFTexture` in TPF 9999 that contains the given texture stem."""
        if not self.tpf_9999:
            raise ValueError("No TPF 9999 loaded for this map area.")
        if not self.case_sensitive:
            texture_stem = texture_stem.lower()
            for texture in self.tpf_9999.textures:
                if texture.stem.lower() == texture_stem:
                    return texture
            raise KeyError(f"Texture '{texture_stem}' (case-insensitive) not found in TPF 9999.")
        for texture in self.tpf_9999.textures:
            if texture.stem == texture_stem:
                return texture
        raise KeyError(f"Texture '{texture_stem}' (case-sensitive) not found in TPF 9999.")

    def get_tpf_texture(self, texture_stem: str) -> TPFTexture:
        """Find the `TPFTexture` in the TPFBHDs or TPF 9999 (checked last) that contains the given texture stem."""
        try:
            binder_entry = self.get_tpf_binder_entry(texture_stem)
        except KeyError:
            # Try TPF 9999.
            if self.tpf_9999:
                try:
                    return self.get_tpf_9999_texture(texture_stem)
                except KeyError:
                    pass
            raise KeyError(f"Texture '{texture_stem}' not found in map area m{self.area_id:02}.")
        else:
            tpf = TPF.from_binder_entry(binder_entry)
            if not tpf.textures:
                raise ValueError(
                    f"TPF '{texture_stem}' was found in map area m{self.area_id:02}, but it contains no textures."
                )
            if len(tpf.textures) > 1:
                _LOGGER.warning(
                    f"Expected TPF in `TPFBHD` to contain exactly one texture, but found {len(tpf.textures)} textures. "
                    f"Only returning the first."
                )
            return tpf.textures[0]

    def __getitem__(self, texture_stem: str) -> TPFTexture:
        """Shortcut for `get_tpf_texture()`."""
        return self.get_tpf_texture(texture_stem)

    def log_missing_unused_msb_map_piece_textures(self):
        """Compare list of present textures to all textures used by all Map Pieces in this area's MSBs to find both
        missing textures and unused textures.

        Does NOT check Map Piece FLVERs that are not actually used in the corresponding MSB.
        """

        unused_textures = set(self.tpfbhd_entries)  # stems removed as they are found in MSBs
        # NOTE: I strongly suspect that TPF 9999 is intended for textures whose usage is not immediately apparent from
        # Map Piece FLVER materials, so we don't check them here.

        msb_directory = self.map_directory / "MapStudio"

        for msb_path in msb_directory.glob(f"m{self.area_id:02}_??_??_??.msb.dcx"):
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
                missing = self.scan_map_piece_textures(flver, unused_textures)
                if missing:
                    _LOGGER.warning(
                        f"Map Piece FLVER {flver_path.name} in MSB {msb_path.stem} is missing textures in area:\n"
                        f"    {', '.join(missing)}"
                    )

        if unused_textures:
            _LOGGER.info(
                f"Found {len(unused_textures)} textures in map area m{self.area_id:02}:\n"
                f"    {', '.join(sorted(unused_textures))}"
            )

    def scan_map_piece_textures(self, map_piece_flver: FLVER, unused_textures: set[str]) -> list[str]:
        """Returns a list of textures in this Map Piece FLVER model that are currently missing from area textures."""
        missing = []
        all_stems = self.get_all_texture_stems()
        for mesh in map_piece_flver.meshes:
            for texture in mesh.material.textures:
                texture_stem = texture.stem.lower() if not self.case_sensitive else texture.stem
                if texture_stem not in all_stems:
                    missing.append(texture.stem)
                unused_textures.discard(texture.stem)
        return missing

    def add_tpfbhd_texture(self, tpf_texture: TPFTexture, overwrite=False):
        """Add a TPF texture to the binders."""
        texture_stem = tpf_texture.stem
        entry = None

        if not self.case_sensitive:
            # We need to CHECK existing textures in a case-insensitive manner, but we want to STORE them with case.
            stem_lower = tpf_texture.stem.lower()
            for existing_stem, existing_entry in self.tpfbhd_entries.items():
                if existing_stem.lower() == stem_lower:
                    # Found existing entry with same stem (case-insensitive).
                    if not overwrite:
                        raise ValueError(f"Texture {texture_stem} already present in binders and `overwrite = False`.")
                    entry = self.tpfbhd_entries[texture_stem]
                    break
        else:
            for existing_stem, existing_entry in self.tpfbhd_entries.items():
                if existing_stem == texture_stem:
                    # Found existing entry with same stem (case-sensitive).
                    if not overwrite:
                        raise ValueError(f"Texture {texture_stem} already present in binders and `overwrite = False`.")
                    entry = self.tpfbhd_entries[texture_stem]
                    break

        if entry is None:
            # Existing entry not found. Create a new one.
            entry = BinderEntry(data=b"", entry_id=0, path=f"\\{texture_stem}.tpf.dcx", flags=0x2)
            self.tpfbhd_entries[texture_stem] = entry

        tpf = self._get_new_tpf(tpf_texture)
        entry.set_from_binary_file(tpf)

    def add_tpf_9999_texture(self, tpf_texture: TPFTexture, overwrite=False):
        """Add a TPF texture to special TPF 9999."""
        texture_stem = tpf_texture.stem
        check_stem = texture_stem.lower() if not self.case_sensitive else texture_stem

        if not self.tpf_9999:
            # Create now.
            self.tpf_9999 = self._get_new_tpf()

        for i, existing_tpf_texture in enumerate(tuple(self.tpf_9999.textures)):
            check_existing_stem = existing_tpf_texture.stem
            if not self.case_sensitive:
                check_existing_stem = existing_tpf_texture.stem.lower()
            if check_existing_stem == check_stem:
                if not overwrite:
                    raise ValueError(f"Texture {texture_stem} already present in TPF 9999 and `overwrite = False`.")
                self.tpf_9999.textures[i] = tpf_texture
                return

        # Append new texture.
        self.tpf_9999.textures.append(tpf_texture)

    def get_tpfbhds(self) -> list[Binder]:
        max_entry_count = self.MAX_TPF_ENTRY_COUNT

        # Sort TPFBHD entries by stem.
        queued_entries = sorted(self.tpfbhd_entries.values(), key=lambda e: e.minimal_stem)
        tpfbhds = []
        while queued_entries:
            tpfbhd = Binder.empty_bxf3()
            tpfbhd.entries, queued_entries = queued_entries[:max_entry_count], queued_entries[max_entry_count:]
            for i in range(len(tpfbhd.entries)):
                tpfbhd.entries[i].entry_id = i
            tpfbhds.append(tpfbhd)

        return tpfbhds

    def write_tpf_9999(self):
        if not self.tpf_9999:
            raise ValueError("No TPF 9999 to write.")
        self.tpf_9999.write(self.area_directory / f"m{self.area_id:02}_9999.tpf.dcx")

    def write_all(self):
        """Create and sort new TPFBHDs (capped at max entry count) and write them along with TPF 9999."""
        tpfbhds = self.get_tpfbhds()
        for i, tpfbhd in enumerate(tpfbhds):
            tpfbhd_path = self.area_directory / f"m{self.area_id:02}_{i:04}.tpfbhd"
            tpfbdt_path = self.area_directory / f"m{self.area_id:02}_{i:04}.tpfbdt"
            tpfbhd.write(tpfbhd_path, bdt_file_path=tpfbdt_path)
        if self.tpf_9999:
            self.write_tpf_9999()

    def _load_tpfbhd_entries(self):
        """Scan all existing TPFBHDs in area directory and load their entries into our one big dictionary."""
        for binder_path in self.area_directory.glob(f"m{self.area_id:02}_*.tpfbhd"):
            binder = Binder.from_path(binder_path)
            for entry in binder.entries:
                if entry.minimal_stem in self.tpfbhd_entries:
                    _LOGGER.warning(
                        f"Duplicate texture entry found in map TPFBHD binders: {entry.minimal_stem}. Using last found."
                    )
                if ".tpf" not in entry.suffixes:
                    _LOGGER.warning(
                        f"Ignoring non-TPF entry '{entry.name}' in TPFBHD binder {binder_path.name}."
                    )
                    continue
                self.tpfbhd_entries[entry.minimal_stem] = entry

    def _load_tpf_9999(self):
        tpf_9999_path = self.area_directory / f"m{self.area_id:02}_9999.tpf.dcx"
        if not tpf_9999_path.is_file():
            return  # no TPF 9999 to load in this map area
        self.tpf_9999 = TPF.from_path(tpf_9999_path)

    @staticmethod
    def _get_new_tpf(texture: TPFTexture = None) -> TPF:
        """Returns a new one-texture or zero-texture (default) TPF with the correct values for DSR."""
        return TPF(
            platform=TPFPlatform.PC,
            encoding_type=2,
            tpf_flags=3,
            textures=[texture] if texture is not None else [],
            dcx_type=DCXType.DS1_DS2,
        )

    @property
    def area_directory(self) -> Path:
        return self.map_directory / f"m{self.area_id:02}"
