def say_hello():
    print('hello')
    print('how are you?')


say_hello()
say_hello()
say_hello()


def say_hello2(name):
    print(f'Hello,{name} how are you?')


say_hello2("Jose")


def say_hello3(name='Default'):
    print(f'Hello,{name} how are you?')


say_hello3("James")
say_hello3()


def add_num(num1, num2):
    return num1+num2

# ?A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value None is returned. A return statement is overall used to invoke a function so that the passed statements can be executed.


# ?Note: Return statement can not be used outside the function.

result = add_num(10, 20)
print(result)


def even_check(num):
    result = num % 2 == 0
    return result


print(even_check(20))
print(even_check(27))
print(even_check(82))


# return true if any number is event inside a list

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            return False


x = [k for k in range(0, 35)]
print(x)
y = [k for k in range(1, 35, 2)]
print(y)
print(check_even_list(x))
print(check_even_list(y))


def check_even_list2(num_list):
    even_numbers = []
    odd_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return [even_numbers, odd_numbers]


print(check_even_list2(x))


# ? Tuple unpacking

stock_prices = [("Apple", 200), ('Banana', 150), ("Grapes", 300)]

for item in stock_prices:
    print(item)

for x, y in stock_prices:
    print(y+y*0.1)


work_hours = [("Abby", 100), ("James", 300), ("Cassie", 700)]


def employee_check():
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max)


result = employee_check()
print(result)
name, hours = employee_check()
print(name)
print(hours)
