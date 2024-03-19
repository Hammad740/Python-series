print(len('hello'))
mystring = 'Hello world'
print(len(mystring))
print(mystring[0])
print(mystring[6])
print(mystring[-2])

mystring = 'abcdefghijk'
print(mystring[2:])
# // : means upto so  last one is not included
print(mystring[:5])
print(mystring[3:6])
print(mystring[::3])
# //[start:end:step]

# // shortcut to reverse the string
print(mystring[::-1])

# // strings are immutable
# s = 'hammad'
# print(s)
# s[0] = 'f'
# print(s)
# s[0] = 'f'

# //TypeError: 'str' object does not support item assignment

# // we can concatenate strings

l = 'mohammad fazil'
print(l)
l = l+'ansari'
print(l)

# // we can create repeatation through multiplication (*)
m = 'beauty'
print(m)
m = m*5
print(m)

# // basic string methods
x = 'Hello world'
x = x.upper()  # Return a copy of the string converted to uppercase.
print(x)
x = x.lower()  # Return a copy of the string converted to lowercase.
print(x)
print(x.split())

# // formatting with .format method in strings
a = 'This is the formatting of the strings:{}'.format('this is inserted')
print(a)

b = 'The {} brown {} fox jumps over the fence.'.format('quick', 'brown')
print(b)
c = 'The {0} brown {0} fox jumps over the fence.'.format('quick', 'brown')
print(c)
d = 'The {q} brown {b} fox jumps over the fence.'.format(q='quick', b='brown')
print(d)
# // float formatting follows "{value:width.precision.f}"
result = 100/7
print(result)
print('The result is: {r:1.4f}'.format(r=result))
# // f strings

name = 'Hammad'
age = 23
print(f'Hello,my name is {name} and i am {age} years old.')
