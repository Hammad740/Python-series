**Inheritance in Python:**

Inheritance is a powerful feature of object-oriented programming (OOP) that allows a new class (subclass) to inherit properties and behaviors (attributes and methods) from an existing class (superclass or base class). The subclass can then extend or modify the functionality of the superclass.

**Syntax for creating a subclass in Python:**

```python
class BaseClass:
    # Base class attributes and methods

class SubClass(BaseClass):
    # Subclass inherits from BaseClass
    # Additional attributes and methods can be defined here
```

**Example of Inheritance in Python:**

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Dog inherits from Animal
# Dog class inherits the 'speak' method from Animal class
```

**Polymorphism in Python:**

Polymorphism is the ability of different classes to be treated as objects of a common superclass. It allows objects of different classes to be used interchangeably based on their common interface (methods).

**Types of Polymorphism in Python:**

1. **Method Overriding:** Inheritance allows a subclass to override a method of its superclass with a new implementation.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Dog overrides the 'speak' method of Animal
```

2. **Method Overloading:** Python does not support method overloading in the same way as other languages like Java or C++. However, you can achieve similar behavior using default arguments or variable arguments.

```python
class Calculator:
    def add(self, x, y):
        return x + y

# Method Overloading-like behavior using default arguments
# If only one argument is provided, it defaults to 0
# If two arguments are provided, it performs addition
```

3. **Duck Typing:** Python follows the principle of "duck typing," which means that the type or class of an object is less important than the methods it defines. If an object implements a particular method, it can be used wherever that method is expected, regardless of its actual class.

```python
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

# Both Bird and Airplane classes have a 'fly' method
# They can be treated interchangeably in functions expecting a 'fly' method
```

**Example of Polymorphism in Python:**

```python
def make_sound(animal):
    animal.speak()

# This function can accept any object that has a 'speak' method
# It can accept objects of classes such as Animal, Dog, Cat, etc.
```

In summary, inheritance allows classes to inherit attributes and methods from other classes, while polymorphism allows objects of different classes to be treated interchangeably based on their common interface. These concepts help in creating reusable, modular, and flexible code in Python.
