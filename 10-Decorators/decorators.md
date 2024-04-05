<!-- // must read article https://www.geeksforgeeks.org/decorators-in-python/ -->

**_First Class Objects_**

In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.

Properties of first class functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists, …

Decorators are a powerful feature in Python that allows you to modify or extend the behavior of functions or methods without changing their source code. Decorators provide a way to wrap a function or method with another function, called a decorator function, which can perform additional tasks before or after the execution of the original function.

Here's a basic overview of how decorators work:

1. **Defining a Decorator Function:**

   A decorator function is a regular Python function that takes another function as its argument and returns a new function. This new function can modify or enhance the behavior of the original function.

   ```python
   def my_decorator(func):
       def wrapper():
           print("Something is happening before the function is called.")
           func()
           print("Something is happening after the function is called.")
       return wrapper
   ```

2. **Applying a Decorator:**

   To apply a decorator to a function, you use the `@` symbol followed by the name of the decorator function on the line directly before the function definition.

   ```python
   @my_decorator
   def say_hello():
       print("Hello!")
   ```

   This syntax is equivalent to:

   ```python
   say_hello = my_decorator(say_hello)
   ```

3. **Calling the Decorated Function:**

   When you call the decorated function, it actually calls the wrapper function created by the decorator, which in turn calls the original function.

   ```python
   say_hello()
   ```

   Output:

   ```
   Something is happening before the function is called.
   Hello!
   Something is happening after the function is called.
   ```

**Example Use Cases of Decorators:**

- **Logging:** You can use decorators to log function calls, input arguments, and return values.
- **Authentication and Authorization:** Decorators can be used to restrict access to certain functions based on user roles or permissions.
- **Caching:** Decorators can cache function results to improve performance by avoiding redundant calculations.
- **Error Handling:** Decorators can handle exceptions raised by functions and perform error logging or recovery actions.

**Predefined Decorators:**

Python provides several predefined decorators in the standard library, such as `@property`, `@staticmethod`, and `@classmethod`, which are commonly used for specific purposes like defining properties, static methods, and class methods in classes.

Decorators are a powerful tool in Python for adding functionality to functions or methods in a modular and reusable way, enabling you to write cleaner and more maintainable code.
