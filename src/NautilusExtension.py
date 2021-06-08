from gettext import gettext as _
from subprocess import call


class NautilusExtension():
    def __init__(self, Nautilus, Gio, COMMAND, APPLICATION_NAME, LANG):
        self.Nautilus = Nautilus
        self.Gio = Gio

        self.COMMAND = COMMAND

        if LANG == "ru": 
            # Label
            self.LABEL_FILE = u"Открыть в " + APPLICATION_NAME
            self.LABEL_BACKGROUND = u"Открыть " + APPLICATION_NAME + " здесь"
            #Tip
            self.TIP_FILE = u"Открыть в " + APPLICATION_NAME
            self.TIP_BACKGROUND = u"Открыть " + APPLICATION_NAME + " в этой директории"
        else:
            # Label
            self.LABEL_FILE = u"Open In " + APPLICATION_NAME
            self.LABEL_BACKGROUND = u"Open " + APPLICATION_NAME + " Here"
            #Tip
            self.TIP_FILE = u"Opens " + APPLICATION_NAME + " In"
            self.TIP_BACKGROUND = u"Opens " + APPLICATION_NAME + " In This Directory"
            
    def _checkdecode(self, s):
        return s.decode('utf-8') if isinstance(s, bytes) else s

    def _open(self, file):
        filename = self.Gio.File.new_for_uri(file.get_uri()).get_path()
        if filename:
            call('{0} -w "{1}" &'.format(self.COMMAND, filename), shell=True)
        else:
            call("{0} &".format(self.COMMAND), shell=True)

    def _menu_activate_cb(self, menu, file):
        self._open(file)

    def _menu_background_activate_cb(self, menu, file):
        self._open(file)

    def get_file_items(self, window, files, text_file=False):
        if len(files) != 1:
            return
        
        item, file = None, files[0]

        if file.is_directory():
            filename = self._checkdecode(file.get_name())
            item = self.Nautilus.MenuItem(
                name="NautilusPython::open_file_item",
                label=_(self.LABEL_FILE),
                tip=_(self.TIP_FILE + " {}").format(filename)
            )
            item.connect('activate', self._menu_activate_cb, file)
        elif text_file:
            filename = self._checkdecode(file.get_name())
            item = self.Nautilus.MenuItem(
                name="NautilusPython::open_file_item",
                label=_(self.LABEL_FILE),
                tip=_(self.TIP_FILE + " {}").format(filename)
            )
            item.connect('activate', self._menu_activate_cb, file)

        return [item]
    
    def get_background_items(self, window, file):
        items, item = [], self.Nautilus.MenuItem(
            name='NautilusPython::open_bg_file_item',
            label=_(self.LABEL_BACKGROUND),
            tip=_(self.TIP_BACKGROUND)
        )
        item.connect('activate', self._menu_background_activate_cb, file)
        items.append(item)

        return items
