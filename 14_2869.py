import math

a, b, v = map(int, input().split(' '))

# a, b, v = [2, 1, 5]
# a, b, v = 5, 1, 6
# a, b, v = 100, 99, 1000000000


result1 = v - b
result2 = a - b
# print(result1, result2)
# print(result1 / result2)
print(math.ceil(result1 / result2))

"""
5 2
7 4
9 6
11 8
13 10
15 12
17 14
19 16
21 18
23
"""
"""
4 2 
6 4
8 6 
10 8
12
"""

"""
5 4
9
"""
