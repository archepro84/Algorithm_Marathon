import sys


class Queue():
    def __init__(self):
        self.queue = []

    # O(1)
    def push(self, value):
        self.queue.append(value)

    # O(1)
    def pop(self):
        if self.empty():
            return -1
        return self.queue.pop(0)

    # O(1)
    def size(self):
        return len(self.queue)

    # O(1)
    def empty(self):
        if not len(self.queue):
            return 1
        return 0

    # O(1)
    def front(self):
        if self.empty():
            return -1
        return self.queue[0]

    # O(1)
    def back(self):
        if self.empty():
            return -1
        return self.queue[-1]


loop_count = int(sys.stdin.readline())
queue = Queue()
# result_list = []
while loop_count:
    input_text = list(sys.stdin.readline().split())
    if input_text[0] == "push":
        queue.push(int(input_text[1]))
    elif input_text[0] == "pop":
        # result_list.append(queue.pop())
        print(queue.pop())
    elif input_text[0] == "front":
        # result_list.append(queue.front())
        print(queue.front())
    elif input_text[0] == "back":
        # result_list.append(queue.back())
        print(queue.back())
    elif input_text[0] == "size":
        # result_list.append(queue.size())
        print(queue.size())
    elif input_text[0] == "empty":
        # result_list.append(queue.empty())
        print(queue.empty())
    loop_count -= 1
# for x in result_list:
#     print(x)
