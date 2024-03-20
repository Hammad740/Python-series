# list are ordered sequence that can hold variety of object types

my_list = [1, 2, 3]
print(my_list)
print(len(my_list))

mylist = ['one', 'two', 'three']
print(mylist[0])
print(mylist[1])
anotherlist = ['four', 'five']
newlist = mylist+anotherlist
print(newlist)

# // lists are mutable
newlist[0] = 'one all caps'
print(newlist)

# ? basic lists methods
newlist.append('six')
newlist.append('seven')
print(newlist)
newlist.pop()
print(newlist)
newlist.pop(2)
print(newlist)

num_list = [4, 1, 6, 9]
alphabet_list = ['e', 'b', 'a', 'i', 'p']
num_list.sort()
alphabet_list.sort()
# // Sort the list in ascending order and return None.

# // The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
print(num_list)
print(alphabet_list)

num_list.reverse()
print(num_list)
