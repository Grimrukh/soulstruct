# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- `BoneTree` class for manipulating bones outside index-based `FLVER`.
- `soulstruct.containers.Binder` methods refactored to match signatures of new `pyrelink.core.Binder`.
- UV utilities for FLVER meshes.
- Elden Ring shader sampler group improvements.
- Added this Changelog (with rough collected history).

### Changed
- Minimum Python version raised to 3.13.
- Python 3.13 generic syntax `class Container[T: Element]: ...` used instead of `TypeVar/Generic`.
- FLVER: support for multiple vertex arrays per mesh; improved batch operations.
- `str`/`Path` hybrid methods now use single dispatch.
- DCX resources included in package data.
- `ELDEN_RING_PATH` constant changed to `ER_PATH` for game consistency.
- `SEKIRO_PATH` constant changed to `SEK_PATH` for game consistency.
- `Config` dataclass added to `soulstruct.config` (legacy global constants still supported but deprecated).
- Core dataclass metaclasses cleaned up.
- Unified `MatDef` vertex array layout creation into one method per game.
- `frozendict` package used for genuine frozen dictionaries (not yet applied everywhere).
- Bones per mesh for `MergedMesh` split must be >= 12 (minimum that a single face could weight to).
- Streamlined `bone_indices` vs. `normal_w` bone indices for static meshes in `MergedMesh` split.
- Euler base class name changed to `EulerBase` for consistency.

### Fixed
- Fixed `FLVERMesh.uv_count` validation.
- Fixed PTDE EMEVD import bug.
- Improved `MatDef` material prasing.
- Fixed NVM big-endian vertex write bug.
- `typing.cast(typing.Self, ...)` used for ambiguous type coercion with `super()`, `cls.new()`.
- Fixed dupe-vertex searching bug in `MergedMesh`.
- Fixed hashing of `EulerDeg/EulerRad` types.
- Fixed SIBCAM rotation fields from `Vector3` to `EulerRad`.

### Removed
- Removed placeholder DeSR (Demon's Souls Remastered) support stub.
- Removed support for Python < 3.13.

---

## [2.3.3] - 2026-03-30

### Changed
- JSON resource files built as part of package; EXEs and DLLs included in package build.

## [2.3.2] - 2026-03-29

### Changed
- Added `bumpversion` tooling and `version` module.

## [2.3.1] - 2026-03-29

### Fixed
- Fixed Binder V4 file size write.

## [2.3.0] - 2026-03-12

### Added
- `MATBIN`/`MTD` load-all convenience methods.

### Changed
- `FLVERMesh.is_bind_pose` renamed to `is_dynamic`.
- Removed `use_lazy_load` from MATBIN/MTD.
- EVS parser error handling refactored.
- `typing.Union` replaced throughout with `X | Y` syntax.

### Fixed
- DSR snow shader handling.
- Binder name now included in entry error messages.
- EVS: underscored `Flag` arguments now correctly detected.

## [2.2.0] - 2026-02-27

### Added
- Elden Ring DLC map properties in MSB.
- `Euler` angle classes; user-facing MSB fields refactored.

### Changed
- Vectors are now immutable; removed dynamic `BinaryStruct` creation (constrata 1.3.1).
- Non-map-piece vertex layout generation now excludes bone weights when `is_dynamic` is off.

## [2.1.0] - 2025-07-14

### Added
- Migrated to `pyproject.toml` build system with `rich` and `typer` as core dependencies.
- Moved to `src/` layout with namespace package; removed setuptools.
- `EnumModuleGenerator` added to all game `maps` subpackages.
- MSB utility functions added to all game subpackages.
- Support for `DCX_ZSTD` compression (Shadow of the Erdtree regulation file).
- Elden Ring `GameParamBND` properties.
- Elden Ring `ParamDef` update with versioned paramdef support.
- Logging handler improvements: soft wrapping and hyperlinks.
- Config and log files now stored in AppData.

### Changed
- License changed to GPL 3.0+.
- Config paths changed to `Path` objects.
- `constrata` updated to 1.2.0.
- Param classes significantly refactored; `ParamRow` cleanup for Elden Ring.

### Fixed
- Fixed config bug.
- Fixed default log level.
- `PACKAGE_PATH` renamed and corrected.

## [2.0.0] - 2025-03-23

This section covers approximately two years of development (January 2023 – June 2025) between the
last tagged release (1.4.0) and the unofficial 2.1.0 version commit.

### Added
- **Demon's Souls support**: FLVER 0x10/0x14, TPF (PS3), MSB, DCX, bundled MTD resources, HKX DCX.
- `constrata` adopted as external binary IO package; `BinaryStruct` nesting and varints.
- Initial TAE/ANIBND animation file parsing.
- SIBCAM (camera data) full parsing and writing.
- MTD and MATBIN material definition file parsing; bundled MTDBNDs for DS1.
- `DivBinder` class for Elden Ring split binders.
- `MapAreaTextureManager` for DS1R; `MapTextureManager` for DSR.
- **Elden Ring MSB** support.
- Elden Ring EMEVD/EVS support including DLC instructions and `DCX_ZSTD`.
- `DSRMapMonitor` for runtime map monitoring.
- NavGraph (`MCG`/`MCP`) overhaul and auto-generation.
- `NVM` quadtree box auto-generation (vectorized NumPy).
- NVMBND methods; navmesh added to game submodules.
- `GroupBitSet` improvements and methods.
- `BinderEntry.suffix` property.
- `restorebak` CLI subcommand.
- Binary compare and param row finder utilities.
- `Game.abbreviated_name` property.
- `RegionShape.SHAPE_FIELDS` and GUI support for region shapes.
- `MSBEntry` referrer tracking.
- `Material.mat_def_stem` property.
- `MSBGenericEntryType` for unknown MSB entry subtypes.

### Changed
- **GUI editor moved to separate `soulstruct-gui` repository** (2024-01-24).
- FLVER completely overhauled to use NumPy arrays for all vertex data.
- `Submesh` renamed to `FLVERMesh` throughout.
- `FLVERBone` children/siblings changed from indices to direct object references.
- FLVER `mtd_path`/`mtd_name` renamed to `mat_def_path`/`mat_def_name`.
- Materials and GX lists moved out of FLVER root onto individual meshes.
- `FLVERDummy.flag_1` renamed to `follows_attach_bone`.
- MSB comprehensively overhauled across all games; entry references refactored.
- `UnusedCharacter`/`UnusedObject` renamed to `DummyCharacter`/`DummyObject`.
- `NavmeshType` renamed to `NavmeshFlags`; `NavInfo` renamed to `NavGraph`.
- EMEVD `model_point` argument renamed to `dummy_id`.
- EVS compiler streamlined; enum decompilation and skip reversal improved.
- `typing.Type` replaced with built-in `type` throughout.
- Minimum Python version raised to 3.11.
- `MSBEntryList.duplicate` now duplicates to next available ID.
- `write()` now returns a list of written paths.
- Unified Soulstruct loggers.
- Binder entry manifest flags/IDs made optional.

### Fixed
- Numerous FLVER read/write fixes: bone packing, 32-bit face set indices, vertex colors, tangents,
  bounding boxes, bone sibling assignment, GXItem, vertex weight data, normal_w bone guessing.
- Fixed MSB JSON read/write, entry duplication, field display, and entry reference reattachment.
- Fixed NVM 64-bit vertex read, NVM write, big-endian vertex handling.
- Fixed MCG edge map ID write and MCP auto-generation and repr.
- Fixed DSR DrawParams injection and memory hook reliability.
- Fixed various EMEVD/EVS compiler bugs (common function parser, arg type detection, etc.).
- Fixed TPF byte order bug; fixed PS3 TPF write.
- Fixed `PACKAGE_PATH` for PyInstaller (`MEIPASS`) environments.
- Fixed NVMBND name detection and defaults; fixed `GameParamBND.get_param`.
- Fixed ER param bugs and `ER MSGDirectory`.
- Fixed fatal FLVER write bug (2024-01-31).
- Fixed DSR UV name bug, snow MatDef bug, and DS1R layout botch handling.
- Fixed `DrawParamBND` and `FFXBND` bugs.

### Removed
- GUI editor extracted to `soulstruct-gui` repo.
- Removed `MTDInfo` class; MTD param accessors added as replacement.
- Removed `MSB.set_auto_references()`.
- Removed old `find_dcx` function.
- Removed `colorama` dependency.
- Removed Python 3.10 support.

---

## [1.4.0] - 2023-01-13

### Changed
- Overhauled internals to use dataclasses for basic structs, significantly improving performance.

## [1.3.2] - 2022-02-17

### Fixed
- Fixed name of `MapCollision` event instructions when decompiling EMEVD to EVS (`EnableCollision`/`DisableCollision` → `EnableMapCollision`/`DisableMapCollision`).

## [1.3.1] - 2022-01-18

### Fixed
- Fixed encoding used by JSON files for Params/Lighting/Text (Params and Lighting use UTF-8; Text enforces ASCII).

## [1.3.0] - 2022-01-17

### Added
- Maps, Params, Lighting, and Text can now be stored in the project as JSON files via `"PreferJSON": true` in `project_config.json`.

### Changed
- Params, Lighting, and Text entry right-click duplication now duplicates to the next *available* ID rather than the immediately next ID.

## [1.2.4] - 2021-11-13

### Fixed
- Fixed bug breaking some param/lighting tables in PTDE (Weapons, Weapon Upgrades, Goods, Tone Map, Tone Correction).
- MSB fields referencing other MSB entry names can now be set to empty string to revert to `None`.
- Stable footing flag of collisions can now be properly set to -1.

## [1.2.2] - 2021-08-20

### Added
- `PreferJSON` config option to save and load all map data (MSBs) as JSON files in a `maps/` folder instead of a single pickled `.ssp` file.

## [1.2.1] - 2021-08-19

### Added
- `HeldCondition(x)` as a shortcut for `Condition(x, hold=True)` in EVS.
- `CoordEntityType` is now auto-detected from event arguments annotated as Object, Character, or Region.

## [1.2.0] - 2021-08-14

### Added
- Real-time DrawParam injection for DSR while hooked — changes are visible without reloading.

## [1.1.1] - 2021-02-13

### Added
- Custom script support: Python scripts in a `scripts/` folder can be run from the Scripts menu.

### Fixed
- Fixed data import bug (1.1.1).
- Fixed compiler bug preventing Bloodborne projects from being created/opened (1.1.0).
- Fixed export bug for certain data types (1.0.1).

## [1.1.0] - 2021-02-13

### Added
- Support for Dark Souls 1 PTDE, Dark Souls Remastered, and Bloodborne.

## [0.10.3] - 2020-01-11

### Fixed
- Fixed config export (e.g. from File menu).
- Removed Dead Knockback reference from Character params.
- Map Connection lighting fields now link to the connected map.

## [0.10.2] - 2020-01-11

### Fixed
- Errors are now logged properly.
- Some map field name changes.

## [0.10.1] - 2020-01-11

### Fixed
- DSR hook draw parent access fixed for both release and debug DLL.

## [0.10.0] - 2020-01-11

### Added
- DSR runtime hook can now set the draw parent for objects/characters.
- Improved cross-param reference search.

### Changed
- DSR runtime hook is significantly faster.

## [0.9.0] - 2020-01-11

### Added
- More map fields supported.
- Better data field documentation with more docstrings, types, and suggested values.
- New entries can be added to empty Map categories.

### Fixed
- Various GUI bugs fixed.

## [0.8.0] - 2020-01-11

### Added
- More Map fields supported.
- Param reference finder now checks both item lots and shops for item IDs.

### Fixed
- Bugs fixed with AI script handling; exporting now possible.

## [0.7.1] - 2020-01-11

### Fixed
- Made memory hook more reliable.
- Better errors when cross-map references are missing.
- Refactored some map rotation/translation methods.

## [0.7.0] - 2020-01-11

### Added
- Tool for editing all item text at once (right-click param entry).
- Option to replace default Japanese item param entry names with English text.
- Popout box can edit entry ID and text simultaneously.

### Fixed
- Fixed a couple of param field type bugs.

## [0.6.4] - 2020-01-11

### Fixed
- Fixed bug with switching maps while a talk script is selected.
- Fixed bug corrupting area banners in collisions on map import.

## [0.6.3] - 2020-01-11

### Fixed
- Fixed `talk` subfolder names (now map IDs, not map names).

## [0.6.2] - 2020-01-11

### Fixed
- Fixed incorrect types for `[X] Defence Addition` fields in Special Effects params.

## [0.6.1] - 2020-01-11

### Fixed
- Fixed swapped player Y and Z in game hook.
- Relative project paths now resolve next to the executable.

## [0.6.0] - 2020-01-11

### Added
- Growth Curves parameter table (`CalcCorrectGraph`).
- Runtime hooks for copying player position/rotation into Maps data entries.
- Game backup/restore options in Tools menu.
- Easy model addition to Maps via right-click on Model field.
- Comment/uncomment hotkey (Ctrl+/) in text editors.

### Fixed
- Fixed AI compile bugs.
- Fixed false "unsaved changes" warning in Events tab.

## [0.5.4] - 2020-01-11

### Changed
- Clicking away from an editing field now confirms changes; press Escape to cancel.

### Fixed
- Soulstruct now warns when an older version export is needed.
- Fixed input/links for map fields referencing multiple other map entries (e.g. Patrol Regions).

## [0.5.3] - 2020-01-11

### Fixed
- Disabled AI export pending debug.
- Fixed BND-from-unpacked bugs for BND3.

## [0.5.2] - 2020-01-11

### Fixed
- Fixed bugs with some maps not loading.
- Descriptions now loaded when importing entity ID modules.

## [0.5.1] - 2020-01-11

### Fixed
- GUI warns when save directory cannot be found, rather than crashing.

## [0.5.0] - 2020-01-11

### Added
- Right-click param entries to find other param references to that entry.

### Changed
- Categories now remember scroll position.
- Default param values are visually faded out.

## [0.4.0] - 2020-01-11

### Added
- Progress bars for lengthy import/export operations.
- Entity import option.
- Better verbose map names.

### Fixed
- Fixed multiple ESD, Param, and Text export bugs.

## [0.3.0] - 2020-01-11

### Added
- Talk ESD script editing.

### Fixed
- Fixed `PTDE_PATH`/`DSR_PATH` swap bug.
- Fixed some AI compile bugs.

## [0.2.1] - 2020-01-11

### Fixed
- Fixed typo preventing event scripts from loading.
- Fixed typo limiting entities list length.

## [0.2.0] - 2020-01-11

### Added
- Global save/export buttons with keyboard shortcuts.
- BND unpack/repack tools.

### Changed
- Better fonts and logging.
- Project window title added.
- Enter/Escape buttons enabled for appropriate dialogs.

## [0.1.2] - 2020-01-11

### Fixed
- Fixed AI tab-switching.
- Allowed lone minus sign in numeric fields.

## [0.1.1] - 2020-01-11

### Fixed
- Fixed AI decompile/compile bug.
- Fixed EMEVD import file types.

## [0.1.0] - 2020-01-11

### Added
- Initial release.