Sure, let's delve into each data type in Python with examples:

1. **Numeric Types**:

   - **int**: Represents integer numbers without decimal points.
     ```python
     x = 5
     y = -10
     ```
   - **float**: Represents floating-point numbers with decimal points.
     ```python
     pi = 3.14
     e = 2.71828
     ```
   - **complex**: Represents complex numbers with real and imaginary parts.
     ```python
     z = 3 + 4j
     ```

2. **Sequence Types**:

   - **str**: Represents strings, which are sequences of characters.
     ```python
     message = "Hello, World!"
     ```
   - **list**: Represents ordered collections of items.
     ```python
     numbers = [1, 2, 3, 4, 5]
     fruits = ['apple', 'banana', 'orange']
     ```
   - **tuple**: Represents ordered collections of items (immutable).
     ```python
     coordinates = (3, 4)
     colors = ('red', 'green', 'blue')
     ```
   - **range**: Represents a sequence of numbers.
     ```python
     nums = range(1, 10)
     ```

3. **Mapping Type**:

   - **dict**: Represents key-value pairs.
     ```python
     person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
     ```

4. **Set Types**:

   - **set**: Represents unordered collections of unique items.
     ```python
     primes = {2, 3, 5, 7}
     ```
   - **frozenset**: Immutable variant of sets.
     ```python
     vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
     ```

5. **Boolean Type**:

   - **bool**: Represents boolean values, `True` or `False`.
     ```python
     is_raining = True
     is_sunny = False
     ```

6. **None Type**:
   - **NoneType**: Represents the absence of a value.
     ```python
     result = None
     ```

Understanding these data types and when to use them is crucial for writing Python code efficiently and effectively. Each data type comes with its own set of operations and methods for manipulation and processing.

The names you use when creating these labels need to follow a few rules:

    1. Names can not start with a number.
    2. There can be no spaces in the name, use _ instead.
    3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
    4. It's considered best practice (PEP8) that names are lowercase.
    5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
       or 'I' (uppercase letter eye) as single character variable names.
    6. Avoid using words that have special meaning in Python like "list" and "str"

Using variable names can be a very useful way to keep track of different variables in Python. For example:
my_income = 100

tax_rate = 0.1

my_taxes = my_income\*tax_rate
