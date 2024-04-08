import timeit
import time


def func_one(n):
    return [str(num) for num in range(n)]


a = func_one(10)
print(a)


def func_two(n):
    return list(map(str, range(n)))


b = func_two(10)
print(b)


# ? current time before

start_time = time.time()

# ? run code
result = func_one(10000000)

# ? current time after running code

end_time = time.time()

# ? elapsed time

elapsed_time = end_time-start_time
print(elapsed_time)
# ? current time before

start_time2 = time.time()

# ? run code
result2 = func_two(10000000)

# ? current time after running code

end_time2 = time.time()

# ? elapsed time

elapsed_time2 = end_time2-start_time2
print(elapsed_time2)


stmt = '''
func_one(100)
'''

setup = '''

def func_one(n):
    return [str(num) for num in range(n)]

'''
x = timeit.timeit(stmt, setup, number=1000000)
print(x)
