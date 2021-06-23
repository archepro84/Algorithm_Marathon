import sys

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0] * (n + 1)

print(matrix)


def dfs(v):
    visit_list[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if (visit_list[i] == 0 and matrix[v][i] == 1):
            dfs(i)


def bfs(v):
    queue = [v]
    visit_list[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            if (visit_list[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visit_list[i] = 0


dfs(v)
print()
bfs(v)
