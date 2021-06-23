import sys

list_size, _ = map(int, sys.stdin.readline().split())
queue = [x for x in range(1, list_size + 1)]
input_list = list(map(int, sys.stdin.readline().split()))
# list_size = 10
# queue = [x for x in range(1, list_size + 1)]
# input_list = [2, 9, 5]
count = 0


def left_queue():
    temp = queue.pop(0)
    queue.append(temp)


def right_queue():
    temp = queue.pop()
    queue.insert(0, temp)


while input_list:
    find_index = queue.index(input_list[0], 0, len(queue))
    # print(len(queue), len(queue) // 2)

    if find_index > len(queue) // 2:
        while input_list[0] != queue[0]:
            right_queue()
            count += 1
    else:
        while input_list[0] != queue[0]:
            left_queue()
            count += 1

    queue.pop(0)
    input_list.pop(0)
print(count)
