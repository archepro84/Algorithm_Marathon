import sys

loop_count = int(sys.stdin.readline())
queue = []
len_queue = len(queue)
while loop_count:
    input_text = list(sys.stdin.readline().split())
    if input_text[0] == "push":
        queue.append(int(input_text[1]))
        len_queue = len(queue)
    elif input_text[0] == "pop":
        if not len_queue:
            print(-1)
        else:
            print(queue.pop(0))
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
    loop_count -= 1
