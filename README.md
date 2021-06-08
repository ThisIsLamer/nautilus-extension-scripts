<div align="center">
    <h1>Nautilus Extensions</h1>
    <img src="https://img.shields.io/badge/-Python-2C2F33?style=flat&logo=Python" alt="python">
    <img src="https://img.shields.io/badge/-Gnome-2C2F33?style=flat&logo=gnome">
</div>

### This is a small wrapper over nautilus-python designed to easily add extensions to the context menu

### To quickly add items to the context menu, simply create a new file and add the following content there using the visual-studio-code example.


```py
from src.NautilusExtension import NautilusExtension
from gi.repository import Nautilus, GObject, Gio


# The class must contain the name of the extension
class YOUNAMEExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        # We initialize the shell and pass the required parameters: 
        # Nautilus, Gio, "The command of which you will call the 
        # application", "Program name", "Localization, ru, en supported,
        # for en, leave this field empty" 
        self.nautilus = NautilusExtension(Nautilus, Gio, "code", "VSCode", "ru")

    # This event occurs when we right-click on a folder or file
    def get_file_items(self, window, files):
        return self.nautilus.get_file_items(window, files)

    # This event occurs when we right-click on an empty space.
    def get_background_items(self, window, file):
        return self.nautilus.get_background_items(window, file)
```

### to add to the context menu when clicking on the right mouse button, pass the last parameter to the function `get_file_items` value `True`
```py
def get_file_items(self, window, files):
        return self.nautilus.get_file_items(window, files, True)
```


<div align="center">
    <h1>Installing</h1>
</div>

### Install the package `nautilus-python` then move all files from the current directory to the next one: `~/.local/share/nautilus-python/extensions/` and restart nautilus.