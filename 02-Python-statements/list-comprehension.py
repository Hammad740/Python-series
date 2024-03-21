my_string = 'Mohammad Hammad Ansari'
my_list = []
for letter in my_string:
    my_list.append(letter)

print(my_list)

my_list2 = [letter for letter in my_string]
print(my_list2)

my_list3 = [x for x in 'word']
print(my_list3)

my_list4 = [num**2 for num in range(0, 21)]
print(my_list4)

my_list5 = [x for x in range(0, 11) if x % 2 == 0]
print(my_list5)

celcius = [0, 10, 12, 24, 56]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

nested_list = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        nested_list.append(x*y)
print(nested_list)

nested_list2 = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
print(nested_list2)
