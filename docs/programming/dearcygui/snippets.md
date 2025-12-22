Custom fonts renderer:
```python
import dearcygui as dcg

def make_font(size, *, main_font_path) -> dcg.GlyphSet:
    """
    Usage:
    self.viewport.initialize(font=dcg.AutoFont(self, font_creator=make_font, main_font_path=roboto_regular))
    """
    font_renderer = dcg.FontRenderer(main_font_path)
    glyphs = font_renderer.render_glyph_set(target_size=size)
    return glyphs
```

App class:
```python
class App(dcg.Context):
    def __init__(self):
        super().__init__()
        self.viewport.initialize()
    
    def run(self):
        while self.running:
            self.viewport.render_frame()
```


Resource path:
```python
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller
    pyinstaller --onefile --add-data "res:res" main.py
    """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    return os.path.join(base_path, "res", relative_path)
```
