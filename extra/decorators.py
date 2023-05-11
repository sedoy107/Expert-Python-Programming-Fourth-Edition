import ctypes

# simple decorator function


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# decorator with arguments


def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Before function call with args: {}, {}".format(arg1, arg2))
            result = func(*args, **kwargs)
            print("After function call with args: {}, {}".format(arg1, arg2))
            return result
        return wrapper
    return decorator


@decorator
def foo2(a, b):
    return a + b


l1 = [1, 2, 3, 4, 5]
s1 = {1, 2, 3, 4, 5}


@decorator_with_args(l1, s1)
def foo3(a, b):
    return a + b


l1_addr = id(l1)
s1_addr = id(s1)

del l1
del s1

l1_recovered = ctypes.cast(l1_addr, ctypes.py_object).value
s1_recovered = ctypes.cast(s1_addr, ctypes.py_object).value
l1_recovered.append(6)
s1_recovered.add(6)

foo2(1, 2)
foo3(1, 2)
breakpoint()
