# Running asyncio loop in a separate thread

Full code:
[asyncio_thread.py](asyncio_thread.py)

Context manager to run an asyncio loop in a separate thread.
Example usage:
```python
import asyncio
from asyncio_thread import asyncio_loop_in_thread
with asyncio_loop_in_thread() as loop:
    asyncio.run_coroutine_threadsafe(asyncio.sleep(1), loop)
    while True:
        pass
```

Decorator to run a function with an asyncio loop in a separate thread.
Example usage:
```python
import asyncio
from asyncio_thread import with_asyncio_loop_in_thread
@with_asyncio_loop_in_thread
def my_function(loop):
    asyncio.run_coroutine_threadsafe(asyncio.sleep(1), loop)
    while True:
        pass
```
