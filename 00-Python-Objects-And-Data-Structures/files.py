# myfile = open('file.txt')
# contents = myfile.read()
# print(contents)
# myfile.close()


# # with open('myfile.txt') as my_new_file:
# #     contents = my_new_file.read()

# # with open("myfile.txt", mode='w') as myfile:
# #     contents


# //https://www.geeksforgeeks.org/file-handling-python/

f = open('files.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()
