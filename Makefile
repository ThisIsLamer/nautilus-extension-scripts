DESTDIR = ~/.local/share/nautilus-python/extensions
SOURCES = src/ sublime.py vscode.py

install: copy close-nautilus

copy: $(SOURCES)
    mkdir -p $(DESTDIR)
    cp -f -r $(SOURCES) $(DESTDIR)

close-nautilus:
    @nautilus -q || true

clean:
    rm -r ${DESTDIR}/src ${DESTDIR}/sublime.py ${DESTDIR}/vscode.py