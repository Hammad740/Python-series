x = 0
while x < 5:
    print(f'The current value of x is:{x}')
    x += 1

# // break-> breaks out of the current closest enclosing loop
# // continue->Goes to the top of the closest enclosing loop
# // pass-> does nothing

y = [1, 2, 3]
for item in y:
    # comment
    pass
print("end of my code")

name = "Sammy"
for letter in name:
    if letter == 'a':
        continue
    print(letter)

z = 0
while z < 5:
    if z == 2:
        break
    print(z)
    z += 1
