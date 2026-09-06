# soulstruct
Python tools for inspecting and modding FromSoftware games.

**YouTube channel with some tutorials: https://youtube.com/grimrukh**

**Like my stuff? Consider supporting me on Patreon <3 https://patreon.com/Grimrukh**

Game abbreviations used below and in package:
- **DS1PTDE**: Dark Souls: Prepare to Die Edition
- **DS1R**: Dark Souls Remastered
- **DS2**: Dark Souls II (either version)
- **BB**: Bloodborne
- **DS3**: Dark Souls III
- **SEK**: Sekiro: Shadows Die Twice
- **ER**: Elden Ring

**Related libraries:**
- [soulstruct-havok](https://github.com/Grimrukh/soulstruct-havok): Havok classes and tools for Soulstruct,
supporting map collision, character collision, animation, ragdolls, and more.
- [soulstruct-vanilla](https://github.com/Grimrukh/soulstruct-vanilla): Vanilla event scripts (`.evs.py`)
and other vanilla dumps from Soulstruct.
- [soulstruct-gui](https://github.com/Grimrukh/soulstruct-gui): Graphical interface for Soulstruct-based
modding projects, including tabs for Maps, Events, Params, Lighting, Text, AI, and Talk scripts (plus some
Runtime utilities for supported games).
- [Firelink](https://github.com/Grimrukh/Firelink): My FromSoftware modding framework written in C++, which
is MUCH faster than Soulstruct for core classes such as FLVERs and Binders. Also includes memory-hooking
implementations for supported games and an Elden Ring MSB class (Python is generally too slow for these).

Features
--------

- Unified graphical application for modifying maps, events, parameters, text, AI, and talk scripts in *Dark Souls* 
  (both versions) and *Bloodborne*. Game data is imported as a **project**, edited in the window (or in Python if you 
  prefer), and exported back to game-ready files whenever you want. Keep track of map entities, quickly navigate between 
  data types, and view custom syntax highlighting for event scripts and AI scripts.
  - Supported games: DS1PTDE, DS1R, BB

- Event scripts (**EMEVD**) and EzState state machines (**ESD**) can be translated to and from valid Python-based 
languages with high-level programming features.
    - Supported games: DS1PTDE, DS1R, DS2 (ESD only), BB, DS3

- Map data (**MSB**), game parameters (**GameParam**), lighting parameters (**DrawParam**), text data (**FMG**) can be 
loaded into Python structures, edited, and repacked.
    - Supported games: DS1PTDE, DS1R, BB (map, game parameters, and text only), DS3 (map and text only)

- AI scripts in can be decompiled, edited, and recompiled.
    - Supported games: DS1PTDE (no decompiling), DS1R

- Unpack/repack **BND** archives and automatically manage **DCX** compression.
    - Supported games: all
