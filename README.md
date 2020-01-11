# soulstruct
Python tools for inspecting and modding From Software games, including an "all in one" GUI.

Features:
- Unified graphical application for modifying maps, events, parameters, text, AI, and scripts in *Dark Souls* 
(either version). Game data is imported as a **project**, edited in the window (or in Python if you prefer), and 
exported back to game-ready files whenever you want. Keep track of map entities, quickly navigate between data types,
and view custom syntax highlighting for event scripts and AI scripts. *Mildly experimental: exported project data has
not been thoroughly tested in-game, particularly AI.* 

- Event scripts (**EMEVD**) and EzState state machines (**ESD**) can be translated to and from valid Python-based 
languages with high-level programming features. 
(*Dark Souls | Bloodborne | Dark Souls 3*)

- Map data (**MSB**), game parameters (**GameParam**), lighting parameters (**DrawParam**), text data (**FMG**) can be 
loaded into Python structures, edited, and repacked. 
(*Dark Souls only*)

- AI scripts in *Dark Souls* can be decompiled, edited, and recompiled.

- Unpack/repack **BND** archives and automatically manage **DCX** compression. 
(*Dark Souls | Bloodborne | Dark Souls 3*) 

- Includes my ongoing documentation for game IDs in *Dark Souls*.

Still to come:
- Support for animation events (**TAE**) and Lua AI scripts.

