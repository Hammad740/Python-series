def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

# // map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# //Python map() Function Syntax
# Syntax: map(fun, iter)

# Parameters:

# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.
# NOTE: You can pass one or more iterable to the map() function.

# Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]


names = ['Andy', "Eve", "Sally"]
print(map(splicer, names))
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


my_numbers = [1, 2, 3, 4, 5, 6]
print(filter(check_even, my_numbers))

for n in filter(check_even, my_numbers):
    print(n)

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# Python filter() Syntax
# The filter() method in Python has the following syntax:

# Syntax: filter(function, sequence)

# Parameters:

# function: function that tests if each element of a sequence is true or not.
# sequence: sequence which needs to be filtered, it can be sets, lists, tuples, or containers of any iterators.
# Returns: an iterator that is already filtered.


# ? LAMBDA FUNCTIONS
# // A lamda function is a small anonymous function

# ** lambda arguments:expression
def x(a): return a+10


print(x(5))

# // Lambda functions can take any number of arguments:


def y(a, b): return a*b


print(y(5, 6))

print(list(map(lambda num: num**2, my_numbers)))


print(list(filter(lambda num: num % 2 == 0, my_nums)))
