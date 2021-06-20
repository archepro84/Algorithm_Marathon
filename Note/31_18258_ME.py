import sys


class Queue():
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if self.empty():
            return -1
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        if not len(self.queue):
            return 1
        return 0

    def front(self):
        if self.empty():
            return -1
        return self.queue[0]

    def back(self):
        if self.empty():
            return -1
        return self.queue[-1]


# queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# print(queue.front())
# print(queue.back())
# print(queue.empty())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.empty())
