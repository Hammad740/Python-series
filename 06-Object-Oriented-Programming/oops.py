
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


class Cat():

    # // class object attribute
    # // same for any instance of a class
    species = 'mammal'

    def __init__(self, name, breed, spots):
        self.name = name
        self.breed = breed
        self.spots = spots

# ** methods are functions inside the class
    def bark(self):
        print("meeeeeow! my name is {}".format(self.name))


my_cat = Cat("jessie", 'german', True)
print(my_cat.species, my_cat.name, my_cat.breed, my_cat.spots)
print(my_cat.bark())


class Circle():
    # ? class object attribute
    pi = 3.14
    def __init__(self, radius): self.radius = radius

    def get_circumference(self):
        return self.radius*self.pi*2

    def get_area(self):
        area = self.radius*self.radius*Circle.pi
        # ? we are referencing class object attribute
        return area


my_circle = Circle(5)
print(my_circle.get_circumference())
print(my_circle.get_area())
