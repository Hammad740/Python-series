# // https://www.geeksforgeeks.org/python-collections-module/
from collections import namedtuple
from collections import defaultdict
from collections import Counter


mylist = [1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 2, 2, 2]
print(Counter(mylist))

# // The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc. In this article, we will discuss the different containers provided by the collections module.

print(Counter('aaaaabbbbbvccccbbvvvddd'))

letters = 'aaaaaaaaaaaaaaannnnnnnnnnbbbbbbbbbllllttttmnkjokpppiimmnn'
c = Counter(letters)
print(c)
print("#######")
print(c.most_common())

d = Counter(cats=4, dogs=6)
print(d)


h = {'a': 10}
print(h['a'])
# print(h['wrong'])

n = defaultdict(lambda: 0)
n['correct'] = 100
print(n)
# print(n['wrong key'])


mytuple = (10, 20, 30, 40)

Dog = namedtuple("Dog", ['age', 'breed', 'name'])
sammy = Dog(age=5, breed="Husky", name='Sam')
print(sammy)
print(sammy.age)
print(sammy.breed)
