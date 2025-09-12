from contextlib import contextmanager
import asyncio
import threading


def run_loop(loop: asyncio.AbstractEventLoop):
    try:
        asyncio.set_event_loop(loop)
        loop.run_forever()
    except Exception as e:
        print(f"Error in loop: {e}")


def run_loop_in_thread(loop: asyncio.AbstractEventLoop):
    thread = threading.Thread(target=run_loop, args=(loop,), daemon=True)
    thread.start()
    return thread


def finalize(loop):
    tasks = asyncio.all_tasks(loop)
    for task in tasks:
        task.cancel()

@contextmanager
def asyncio_loop_in_thread():
    """
    Context manager to run an asyncio loop in a separate thread.
    Example usage:
    ```python
    from asyncio_thread import asyncio_loop_in_thread
    with asyncio_loop_in_thread() as loop:
        asyncio.run_coroutine_threadsafe(asyncio.sleep(1), loop)
        while True:
            pass
    ```
    """
    loop = asyncio.new_event_loop()
    thread = run_loop_in_thread(loop)
    try:
        yield loop
    finally:
        finalize(loop)
        loop.call_soon_threadsafe(loop.stop)
        thread.join()


def with_asyncio_loop_in_thread(func):
    """
    Decorator to run a function with an asyncio loop in a separate thread.
    Example usage:
    ```python
    from asyncio_thread import with_asyncio_loop_in_thread
    @with_asyncio_loop_in_thread
    def my_function(loop):
        asyncio.run_coroutine_threadsafe(asyncio.sleep(1), loop)
        while True:
            pass
    ```
    """
    def wrapper(*args, **kwargs):
        with asyncio_loop_in_thread() as loop:
            return func(loop, *args, **kwargs)
    return wrapper
