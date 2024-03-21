my_iterable = [1, 2, 3, 4, 5, 6]
for item in my_iterable:
    print(item)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    # ? check for event
    if num % 2 == 0:
        print(f'even number :{num}')
    else:
        print(
            f'odd number  :{num}'
        )

list_sum = 0
for num in my_list:
    list_sum += num
print(list_sum)

for letter in 'hello world':
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

# // tuple unpacking
tup_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(len(tup_list))

for (a, b) in tup_list:
    print(a)
    print(b)

another_tup_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

for a, b, c in another_tup_list:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d.items():
    print(item)
for key, value in d.items():
    print(key)
    print(value)
