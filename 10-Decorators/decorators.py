# Decorators allow you to decorate a function

def hello():
    print("Hello")


hello()
del hello


def hey(name="Hammad"):
    print("The hey function has been executed!")

    def greet():
        print("This is the greet() function inside the hey!")

    def welcome():
        print("This is welcome() inside the hello")

    print("I am going to return a function!")

    if name == "Hammad":
        return welcome()
    else:
        return greet()


y = hey()
print(y)
x = hey("Jose")
print(x)


def cool():
    def super_cool():
        return "I am very cool"
    return super_cool()


z = cool()
print(z)


# // passing one function to another function
def say_hi():
    return "Hi"


def other(some_def_func):
    print("Other code runs here")
    print(some_def_func())


m = other(say_hi)
print(m)


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code,before the original function")
        original_func()
        print("Some extra code,after the original function!")
    return wrap_func()


def func_needs_decorator():
    print("I want to be decorated!")


n = new_decorator(func_needs_decorator)
print(n)


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")
