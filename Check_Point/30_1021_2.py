import sys
import collections

list_size, _ = map(int, sys.stdin.readline().split())
queue = collections.deque([x for x in range(1, list_size + 1)])
input_list = collections.deque(map(int, sys.stdin.readline().split()))
# list_size = 10
# queue = collections.deque([x for x in range(1, list_size + 1)])
# input_list = [2, 9, 5]
count = 0

while input_list:
    find_index = queue.index(input_list[0], 0, len(queue))
    # print(len(queue), len(queue) // 2)
    if find_index > len(queue) // 2:
        while input_list[0] != queue[0]:
            # print(queue)
            queue.rotate(1)
            count += 1
    else:
        while input_list[0] != queue[0]:
            queue.rotate(-1)
            count += 1

    queue.popleft()
    input_list.popleft()
print(count)
