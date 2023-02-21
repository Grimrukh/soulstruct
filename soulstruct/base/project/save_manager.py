__all__ = ["SaveManager"]

import shutil
import os

from soulstruct.games import Game
from .exceptions import SoulstructProjectError


class SaveManager:

    game: Game

    def __init__(self, game: Game):
        self.game = game

    def get_game_saves(self):
        # TODO: Is this DS1 specific?
        save_folder = self._get_save_folder()
        return [save_file.stem for save_file in save_folder.glob("*.sl2") if save_file.stem != "DRAKS0005"]

    def _get_save_folder(self):
        game = self.game
        if not game.save_file_path:
            raise SoulstructProjectError(f"No save file directory known for {game.name}.")
        if not game.save_file_path.is_dir():
            raise SoulstructProjectError(f"Could not find save file directory root: {game.save_file_path}")
        if game.name == "Dark Souls Remastered":
            # DSR save files are saved under a Steam ID subfolder.
            steam_id_folders = list(game.save_file_path.glob("*"))
            if len(steam_id_folders) > 1:
                raise SoulstructProjectError(
                    f"Multiple Dark Souls Remastered save folders found in {str(game.save_file_path)}. Please "
                    f"remove all of them except the real one that matches your Steam ID."
                )
            elif not steam_id_folders:
                raise SoulstructProjectError(
                    f"No Dark Souls Remastered save folders found in {str(game.save_file_path)}."
                )
            return steam_id_folders[0]
        return game.save_file_path

    def load_game_save(self, save_name):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        if not save_file_path.is_file():
            raise SoulstructProjectError(f"Could not find save file: {str(save_file_path)}")
        active_path_str = str(save_folder / "DRAKS0005.sl2")
        try:
            os.remove(active_path_str)
        except FileNotFoundError:
            pass
        shutil.copy2(str(save_file_path), active_path_str)

    def delete_game_save(self, save_name):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        if not save_file_path.is_file():
            raise SoulstructProjectError(f"Could not find save file: {str(save_file_path)}")
        os.remove(save_file_path)

    def create_game_save(self, save_name, overwrite=False):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        active_path = save_folder / "DRAKS0005.sl2"
        if save_file_path.is_file() and not overwrite:
            raise SoulstructProjectError(f"Save file already exists: {str(save_file_path)}")
        if not active_path.is_file():
            raise SoulstructProjectError(f"Active game save file {str(active_path)} could not be found.")
        shutil.copy2(str(active_path), str(save_file_path))
