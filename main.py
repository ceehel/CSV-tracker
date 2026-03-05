from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label
from bindings import BINDINGS_LIST
from mmenu import MAIN_MENU


class Tracker(App):
    """A task tracking app"""

    CSS_PATH = "tracker.css"
    BINDINGS = BINDINGS_LIST

    def compose(self) -> ComposeResult:
        """Initiate the main frame in which the interface will appear.
        Display the mainm menu"""
        yield Header(name="Tracker", icon="T")
        yield Footer()
        yield MAIN_MENU

    @on(MAIN_MENU.OptionSelected)
    def mmenu_input(self):
        input = MAIN_MENU.OptionSelected.index()
        choice = input.value
        self.mount(Label(choice))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = Tracker()
    app.run()
