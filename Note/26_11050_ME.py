max_depth = 10
depth = [[1], [1, 1]]

for x in range(2, max_depth + 1):
    depth_append_list = []
    print("Hello")
    for index in range(x + 1):
        # print(index, end=" ")
        if index == 0 or index == x:
            print(index)
            depth_append_list.append(1)
        else:
            # append_result =
            depth_append_list.append(depth[x - 1][index - 1] + depth[x - 1][index])

    depth.append(depth_append_list)

    # depth.append(depth[x - 1])

for x in depth:
    print(x)
