import sys

max_depth = 10
depth = [[1], [1, 1]]

for x in range(2, max_depth + 1):
    depth_append_list = []
    for index in range(x + 1):
        if index == 0 or index == x:
            depth_append_list.append(1)
        else:
            depth_append_list.append(depth[x - 1][index - 1] + depth[x - 1][index])

    depth.append(depth_append_list)

# for x in depth:
#     print(x)

a, b = map(int, sys.stdin.readline().split())
print(depth[a][b])
