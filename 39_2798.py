import sys

_, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

# n, m = 5, 21
# data = [5, 6, 7, 8, 9]
# n, m = 10, 500
# data = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
# data = [93, 181, 251, 214, 315, 36, 185, 138, 227, 295]

data.sort()

result = []


def dfs(elements, start):
    # print(abs(m - sum(result)), abs(m - sum(elements)))
    # print(m - sum(result), m - sum(elements))

    if sum(result) == m:
        return m
    if len(elements) == 3 and abs(m - sum(result)) > abs(m - sum(elements)):
        if m - sum(elements) < 0:
            return
        # print(abs(m - sum(result)), elements)
        result.clear()
        result.extend(elements[:])
    elif len(elements) > 3:
        return

    for x in range(start, len(data)):
        # print(elements)
        elements.append(data[x])
        dfs(elements, x + 1)
        elements.pop()


dfs([], 0)

# print(result)
print(sum(result))
