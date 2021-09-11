from functools import reduce

numbers = [4, 17, 3, 90, 28, 55]

def func(a, b):
    return a*b

result = reduce(func, numbers)

print(result)

numbers.append(15)

result2 = reduce(func, numbers)

print(result2)