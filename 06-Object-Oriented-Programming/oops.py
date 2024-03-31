
# ? https://www.w3schools.com/python/python_classes.asp


class Sample():
    pass


my_sample = Sample()
print(type(my_sample))
print(type(Sample))


class Dog():
    def __init__(self, breed, name, spots):
        # // Attributes
        # // Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots


my_dog = Dog("poppy", 'hh', True)
print(my_dog.breed)
my_dog1 = Dog('lab', 'smmay', False, )
print(my_dog1.breed, my_dog1.name)
