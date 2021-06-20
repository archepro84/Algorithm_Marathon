import sys

"""
1, 4 [4] 
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
"""
"""
2 , 4 [6] 
0 0 1 1 
0 1 0 1
0 1 1 0 
1 0 0 1
1 0 1 0
1 1 0 0
"""
""" [4]
3 ,4 
0 1 1 1 
1 0 1 1
1 1 0 1
1 1 1 0
"""
"""
4 ,4 [1]
1 1 1 1
"""

"""
1, 5  [5]
0 0 0 0 1
0 0 0 1 0
0 0 1 0 0
0 1 0 0 0
1 0 0 0 0
"""
"""
2 ,5 [10]
0 0 0 1 1
0 0 1 0 1
0 0 1 1 0
0 1 0 0 1
0 1 0 1 0
0 1 1 0 0
1 0 0 0 1
1 0 0 1 0 
1 0 1 0 0
1 1 0 0 0
"""
""" 
3, 5 [10]
0 0 1 1 1 
0 1 0 1 1
0 1 1 0 1
0 1 1 1 0
1 0 0 1 1
1 0 1 0 1
1 0 1 1 0
1 1 0 0 1
1 1 0 1 0
1 1 1 0 0
"""
"""
4 ,5 [5]
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1 
1 1 1 1 0
"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# r, n = 3, 5
# r, n = 13, 29
# permutation = factorial(n) / factorial(n - r)
# print(int(permutation / factorial(r)))

# loop_count = int(sys.stdin.readline())
# result_list = []
# while loop_count:
# r, n = map(int, sys.stdin.readline().split())
r, n = 30, 30
# if r > n:
#     print(0)
# elif r == n:
#     print(1)
# else:
permutation = factorial(n) // factorial(n - r)
result = permutation // factorial(r)
print(result)
# result_list.append(result)
# loop_count -= 1

# for x in result_list:
#     print(x)
