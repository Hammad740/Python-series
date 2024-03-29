# Dictionaries

We've been learning about _sequences_ in Python but now we're going to switch gears and learn about _mappings_ in Python. If you're familiar with other languages you can think of these Dictionaries as hash tables.

This section will serve as a brief introduction to dictionaries and consist of:

    1.) Constructing a Dictionary
    2.) Accessing objects from a dictionary
    3.) Nesting Dictionaries
    4.) Basic Dictionary Methods

So what are mappings? Mappings are a collection of objects that are stored by a _key_, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

## Constructing a Dictionary

Let's see how we can construct dictionaries to get a better understanding of how they work!

```python
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}

# Call values by their key
my_dict['key2']
'value2'
```

Its important to note that dictionaries are very flexible in the data types they can hold. For example:

```python
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Let's call items from the dictionary
my_dict['key3']
['item0', 'item1', 'item2']

# Can call an index on that value
my_dict['key3'][0]
'item0'

# Can then even call methods on that value
my_dict['key3'][0].upper()
'ITEM0'
```

We can affect the values of a key as well. For instance:

```python
my_dict['key1']

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
#Check
my_dict['key1']
0
```

A quick note, Python has a built-in method of doing a self subtraction or addition (or multiplication or division). We could have also used += or -= for the above statement. For example:

```python
# Set the object equal to itself minus 123
my_dict['key1'] -= 123
my_dict['key1']
```

We can also create keys by assignment. For instance if we started off with an empty dictionary, we could continually add to it:

```python
# Create a new dictionary
d = {}

# Create a new key through assignment
d['animal'] = 'Dog'

# Can do this with any object
d['answer'] = 42

#Show
d

{'animal': 'Dog', 'answer': 42}
```
