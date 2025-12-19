```python
class Child:
    def __init__(self, callback: Callable[[Self], Any]):
        self.callback = callback

    def method(self):
        pass

class Parent:
    def action1(self):
        Child(callback1)

    def callback1(self, sender: Child):
        ...

```
