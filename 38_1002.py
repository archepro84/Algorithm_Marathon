import sys
import math


def circle_turret(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif abs(r1 - r2) == d or r1 + r2 == d:
        print(1)
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)
    else:
        print(0)


_loop = int(sys.stdin.readline())
# results = []
for _ in range(_loop):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    # print(x1, y1, r1, x2, y2, r2)
    circle_turret(x1, y1, r1, x2, y2, r2)
    # result = circle_turret(x1, y1, r1, x2, y2, r2)
    # results.append(result)

# for x in results:
#     print(x)
