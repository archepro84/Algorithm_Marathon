import sys

n = int(sys.stdin.readline())
count = 0
for x in range(666, 10000000):
    if 666 in str(x):
        count += 1
    if n == count:
        print(x)
        break
