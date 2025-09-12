DPG context managment:
```python
from contextlib import contextmanager
import dearpygui.dearpygui as dpg


@contextmanager
def dpg_context_manager():
    """DearPyGui context manager.
    Example usage:
    ```python
    def main():
        with dpg_context_manager():
            dpg.create_viewport()
            dpg.setup_dearpygui()
            # Some code here
            dpg.show_viewport()
            dpg.start_dearpygui()
    ```
    """
    dpg.create_context()
    try:
        yield
    finally:
        dpg.destroy_context()
```
