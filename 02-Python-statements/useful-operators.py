from random import shuffle, randint
my_list = [1, 2, 3, 4, 5]
for item in range(0, 10):
    print(item)
# ?Return an object that produces a sequence of integers from start (inclusive)to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.These are exactly the valid indices for a list of 4 elements.When step is given, it specifies the increment (or decrement).

for _ in range(0, 21, 2):
    print(_)

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcdef'
for item in enumerate(word):
    print(item)
# ? Return an enumerate object.iterable an object supporting iterationThe enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)
# ? https://www.w3schools.com/python/ref_func_zip.asp

'z' in [1, 2, 3]
print('z' in [1, 2, 3])

d = {'k1': 45}
print(34 in d.values())

list3 = [1, 2, 3, 4, 4, 53656, 723, 41]
print(max(list3))
print(min(list3))

list4 = [1, 2, 2, 4, 678, 4, 78, 3, 4]

print(shuffle(list4))  # // inplace
print(list4)

print(randint(0, 100))

# // how to accept user input in python
# ? input always accept things as a string
result = input("what is your name?")
print(result)
result2 = input("favorite number?")
print(result2)
print(type(result2))
print(type(int(result2)))
