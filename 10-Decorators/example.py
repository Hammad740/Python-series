# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} ran in {end-start}')
#         return result
#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)


# example_function(2)


# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(
#             f"{key}->{value}" for key, value in kwargs.items())
#         print(
#             f"calling:{func.__name__} with args {args_value} and kwargs {kwargs_value}")
#         return func(*args, **kwargs)

#     return wrapper


# @debug
# def hello():
#     print("Hello")


# @debug
# def greet(name, greeting="hello"):
#     print(f"{greeting},{name}")


def log_function_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args{args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_function_calls
def add(a, b):
    return a+b


print(add(34, 56))


def smart_div(func):
    def inner(*args):
        a = args[0]
        b = args[1]
        if a < b:
            a, b = b, a
            return func(a, b)
    return inner


@smart_div
def div(a, b):
    print(a/b)


div(2, 5)
