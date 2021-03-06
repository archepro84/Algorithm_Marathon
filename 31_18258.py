import sys
from collections import deque

loop_count = int(sys.stdin.readline())
queue = deque()

len_queue = len(queue)
for _ in range(loop_count):
    input_text = list(sys.stdin.readline().split())
    if input_text[0] == "push":
        queue.append(input_text[1]) #형변환 삭제
        len_queue = len(queue)
    elif input_text[0] == "pop":
        if not len_queue:
            print(-1)
        else:
            print(queue.popleft())
            len_queue = len(queue)
    elif input_text[0] == "front":
        if not len_queue:
            print(-1)
        else:
            print(queue[0])
    elif input_text[0] == "back":
        if not len_queue:
            print(-1)
        else:
            print(queue[len_queue - 1])
    elif input_text[0] == "size":
        print(len_queue)
    elif input_text[0] == "empty":
        if not len_queue:
            print(1)
        else:
            print(0)
