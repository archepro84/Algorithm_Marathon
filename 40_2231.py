import sys

n = int(sys.stdin.readline())


# n = 216
# 핵심 = 각 자릿수를 어떻게 인식할 수 있을까?


def bronze(n):
    for x in range(n // 2, n):
        temp = str(x)
        result = 0
        for i in temp:
            result += int(i)
        if result + x == n:
            return x
    return 0


print(bronze(n))
