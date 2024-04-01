

try:
    def add(n1, n2):
        return (n1+n2)

    number1 = 10
    number2 = int(input("Give second number:"))
    y = add(number1, number2)

except:
    print("Looks like you are not adding correctly")
else:
    print("Add went well")
    print(y)

# ** The try block lets you test a block of code for errors.

# * The except block lets you handle the error.

# * The finally block lets you execute code, regardless of the result of the try- and except blocks.


try:
    f = open('testfile', 'w')  # // w
    f.write("Write a test line...")
except TypeError:
    print("There was a type error!")
except OSError:
    print("There is some os error!")
finally:
    print("I always run..")


def ask_for_int():
    while True:
        try:
            result = int(input("please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End of try/except/finally")


ask_for_int()


try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print(TypeError)


try:
    x = 5
    y = 0
    z = x/y
except:
    print("There is some error")
finally:
    print("All done")


def func_square():
    while True:
        try:
            n = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
        else:
            print(f"The square of the number is: {n * n}")
            break


func_square()
