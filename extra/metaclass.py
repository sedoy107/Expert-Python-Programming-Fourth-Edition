from typing import Any


class Metaclass(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("Metaclass.__new__ called")
        print(f"kwargs: {kwargs}")
        namespace["attr"] = 42
        namespace["__repr__"] = lambda self: f"Foo(attr={self.attr})"
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("Metaclass.__prepare__ called")
        print(f"kwargs: {kwargs}")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print("Metaclass.__init__ called")
        print(f"kwargs: {kwargs}")
        super().__init__(name, bases, namespace)

    def __call__(self, *args, **kwargs):
        print("Metaclass.__call__ called")
        print(f"kwargs: {kwargs}")
        return super().__call__(*args, **kwargs)


class Foo(metaclass=Metaclass, extra="my_value"):
    a: int
    b: str

    def __init__(self, a, b):
        print("Foo.__init__ called")
        self.a = a
        self.b = b


if __name__ == "__main__":
    foo = Foo(a=5, b="bar")
    print(foo)
