my_tuple = (1, 2, 3)
# ? tuples are very similar to lists.However they have one key difference i.e immutability.Once the element is inside the tuple,it can never be reassigned.
my_list = [1, 2, 3]
print(type(my_list))
print(type(my_tuple))
print(my_tuple[1])
print(len(my_tuple))

t = ('a', 'a',
     'b', 'e', 'e', 'e')
print(t.count('e'))  # ?Return number of occurrences of value
print(t.index('a'))
# ?Return first index of value.Raises ValueError if the value is not present.
