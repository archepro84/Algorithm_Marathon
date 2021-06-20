import itertools

n, k = map(int, input().split())
l = itertools.combinations(range(1, n + 1), k)

for x in l:
    print(*x)
