from src.NautilusExtension import NautilusExtension
from gi.repository import Nautilus, GObject, Gio


class SublimeExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        self.nautilus = NautilusExtension(Nautilus, Gio, "subl", "Sublime Text", "ru")

    def get_file_items(self, window, files):
        return self.nautilus.get_file_items(window, files, True)

    def get_background_items(self, window, file):
        return self.nautilus.get_background_items(window, file)