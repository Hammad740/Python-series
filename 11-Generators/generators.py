def create_cube(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


print(create_cube(7))


# // A Generator in Python is a function that returns an iterator using the Yield keyword.

def create_cubesII(n):
    for x in range(n):
        yield x**3


print(create_cubesII(11))
print(list(create_cubesII(11)))

# The yield keyword in Python is similar to a return statement used for returning values in Python which returns a generator object to the one who calls the function which contains yield, instead of simply returning a value. The main difference between them is, the return statement terminates the execution of the function. Whereas, the yield statement only pauses the execution of the function. Another difference is return statements are never executed. whereas, yield statements are executed when the function resumes its execution.

# Advantages of yield:

# Using yield keyword is highly memory efficient, since the execution happens only when the caller iterates over the object.
# As the variables states are saved, we can pause and resume from the same point, thus saving time.
# Disadvantages of yield:

# Sometimes it becomes hard to understand the flow of code due to multiple times of value return from the function generator.
# Calling of generator functions must be handled properly, else might cause errors in program.


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(10):
        yield x


for n in simple_gen():
    print(n)

g = simple_gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# ? Return the next item from the iterator.If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

s = 'Hammad'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
