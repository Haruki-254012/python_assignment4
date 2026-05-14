def say_hello(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

from mypackage.greetings import say_hello
from mypackage.calculator import add

print(say_hello("Alice"))
print(f"Sum: {add(10, 5)}")
