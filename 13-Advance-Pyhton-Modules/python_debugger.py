import pdb
x = [1, 2, 3, 4, 5]
y = 2
z = 3
result = y+z
# result2 = x+y
# print(result)
# print(result2)

result_one = y+z
breakpoint()  # // new version
result_two = y+x

print(result_one)
# pdb.set_trace() #// old version

print(result_two)
