import typing as tp

from soulstruct.games import get_game, Game
from soulstruct.utilities.window import SmartFrame, bind_to_all_children


class GameSelector(SmartFrame):

    def __init__(self, *name_options):
        super().__init__(window_title="Game Selector")

        self.protocol("WM_DELETE_WINDOW", lambda: self.done(None))
        self.resizable(width=False, height=False)
        bind_to_all_children(self.toplevel, "<Escape>", lambda _: self.done(None))

        self.output = None  # type: tp.Optional[Game]
        self.build(name_options)

    def build(self, name_options):
        with self.set_master(padx=20, pady=10, auto_rows=0):
            self.Label(text="Choose the game you are modding:", padx=10, pady=20)
            for name_option in name_options:
                try:
                    game = get_game(name_option)
                except ValueError:
                    raise ValueError(f"Invalid game name: {name_option}")
                self.Button(
                    text=game.name,
                    command=lambda g=game: self.done(g),
                    bg="#422",
                    fg="#FFF",
                    width=30,
                    pady=10,
                    padx=10,
                )

    def go(self) -> Game:
        self.toplevel.wait_visibility()
        self.toplevel.grab_set()
        self.toplevel.mainloop()
        self.toplevel.destroy()
        return self.output

    def done(self, game: tp.Optional[Game]):
        self.output = game
        self.toplevel.quit()
