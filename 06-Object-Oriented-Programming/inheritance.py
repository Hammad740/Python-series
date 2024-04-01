# https://www.w3schools.com/python/python_inheritance.asp

# // parent class
class Animal():
    def __init__(self):
        print("Animal Created!")

    def who_am_i(self):
        print("I am an animal!")

    def eat(serf):
        print("I am eating.")


my_animal = Animal()
print(my_animal.who_am_i(), my_animal.eat())

# // base class


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")


my_dog = Dog()
print(my_dog)
print(my_dog.who_am_i())


class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(f'My name is {self.fname} {self.lname}')


x = Person('John', 'doe')
print(x.printname())


class Student(Person):
    pass


y = Student("Mike", "Tyson")
print(y.printname())
# // Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Example
# Add the __init__() function to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname):
# #add properties etc.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


z = Student("Barack", "Obama")
print(z.printname())

# //The super() function is used to give access to methods and properties of a parent or sibling class.

# // The super() function returns an object that represents the parent class.


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # // represents the parent class
        self.graduation_year = year

    def welcome(self):
        print(
            f'My name is {self.fname}  {self.lname} and my graduation year is {self.graduation_year}')


m = Student("Ronne", "Jackson", 2025
            )
print(m.printname())
print(m.graduation_year)
print(m.welcome())
