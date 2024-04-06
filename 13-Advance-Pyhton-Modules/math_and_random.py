import random
import math
# print(help(math))

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))  # not in math,provided by python

print(math.pi)
print(math.e)
print(math.nan)


print(math.log(math.e))
print(math.log(100, 10))

print(math.sin(10))
print(math.sin(100))

print(math.degrees(10))
print(math.radians(100))

# ? random module
print(random.randint(0, 100))

random.seed(101)
print(random.randint(0, 100))


mylist = list(range(1, 21))
print(mylist)
print(random.choice(mylist))
print(random.choice(mylist))
