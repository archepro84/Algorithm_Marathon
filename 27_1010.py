import sys


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


loop_count = int(sys.stdin.readline())
result_list = []
while loop_count:
    r, n = map(int, sys.stdin.readline().split())
    permutation = factorial(n) // factorial(n - r)
    result = permutation // factorial(r)
    result_list.append(result)
    loop_count -= 1

for x in result_list:
    print(x)
