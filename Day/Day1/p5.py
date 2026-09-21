#concept:decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
        return wrapper
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()  