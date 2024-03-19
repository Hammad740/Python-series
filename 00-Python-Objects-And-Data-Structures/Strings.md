# Stings

Strings are used in Python to record text information, such as names. Strings in Python are actually a _sequence_, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

This idea of a sequence is an important one in Python and we will touch upon it later on in the future.

In this we'll learn about the following:

    1.) Creating Strings
    2.) Printing Strings
    3.) String Indexing and Slicing
    4.) String Properties
    5.) String Methods
    6.) Print Formatting

## Creating a String

To create a string in Python you need to use either single quotes or double quotes. For example:

```python
s='hammad'

# Be careful with quotes!
' I'm using single quotes, but this will create an error'

The reason for the error above is because the single quote in <code>I'm</code> stopped the string. You can use combinations of double and single quotes to get the complete statement.

"Now I'm ready to use the single quotes inside a string!"
```

## Creating a String

```python
print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')
print('See what I mean?')
```

## String Basics

We can also use a function called len() to check the length of a string!

```python
len('Hello World')
```

Python's built-in len() function counts all of the characters in the string, including spaces and punctuation.

## String Indexing

We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.

In Python, we use brackets <code>[]</code> after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called <code>s</code> and then walk through a few examples of indexing.

We can use a <code>:</code> to perform _slicing_ which grabs everything up to a designated point. For example:

```python
# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]

# Note that there is no change to the original s
s

# Grab everything UP TO the 3rd index
s[:3]

Note the above slicing. Here we're telling Python to grab everything from 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in Python, where statements and are usually in the context of "up to, but not including".

#Everything
s[:]

# Last letter (one index behind 0 so it loops back around)
s[-1]

# Grab everything but the last letter
s[:-1]

We can also use index and slice notation to grab elements of a sequence by a specified step size (the default is 1). For instance we can use two colons in a row and then a number specifying the frequency to grab elements. For example:

# Grab everything, but go in steps size of 1
s[::1]

# Grab everything, but go in step sizes of 2
s[::2]

# We can use this to print a string backwards
s[::-1]
```

## String Properties

It's important to note that strings have an important property known as _immutability_. This means that once a string is created, the elements within it can not be changed or replaced. For example:

```python
s = 'hammad'
print(s)
s[0] = 'f'
print(s)
s[0] = 'f'

TypeError: 'str' object does not support item assignment
```

Notice how the error tells us directly what we can't do, change the item assignment!

Something we _can_ do is concatenate strings!

```python
s='hammad'
s=s+'ansari'
```

## Basic Built-in String methods

Objects in Python usually have built-in methods. These methods are functions inside the object (we will learn about these in much more depth later) that can perform actions or commands on the object itself.

We call methods with a period and then the method name. Methods are in the form:

object.method(parameters)

Where parameters are extra arguments we can pass into the method. Don't worry if the details don't make 100% sense right now. Later on we will be creating our own objects and functions!

Here are some examples of built-in methods in strings:
s.upper()
s.lower()
s.spilt()

## Print Formatting

We can use the .format() method to add formatted objects to printed string statements.

The easiest way to show this is through an example:

```python
'Insert another string with curly brackets: {}'.format('The inserted string')
```
