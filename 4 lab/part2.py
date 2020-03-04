from functools import *
import math

#1
def avg(numbers): return sum(numbers) / len(numbers)

print(avg([1, 2, 3, 4, 5, 6, 7]))

#2
def div_2(number): return number / 2

print(*map(div_2, [2, 4, 6, 8]))

#3
def sum_num(x, y):
    if isinstance(y, int) or isinstance(y, float):
        return x + y
    else:
        return x + 0

print(reduce(sum_num, [1, 2, 3, 4, 'ee'], 0))

#4
def not_nil(num): return num != 0
print(*filter(not_nil, [1, 2, 3, 0, 4, 5, 0]))

#5
def to_factorial(num): return math.factorial(num)
print(*map(to_factorial, [1, 2, 3, 4, 5]))

#6
def sum_abs(x, y): return abs(x) + abs(y)
print(*map(sum_abs, [1, -2, 3, 4], [2, 3, 1, -5]))

#7
a = [1, 2, 3, 4, 5, 6]
b = [5, 2, 4, 56, 7, 7]

print([x*y for x in a for y in b])