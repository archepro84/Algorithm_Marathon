import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.empty():
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if not len(self.stack):
            return 1
        return 0

    def top(self):
        if self.empty():
            return -1
        return self.stack[-1]


stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.pop())
# print(stack.empty())
# print(stack.size())

loop_count = int(sys.stdin.readline())

while loop_count:
    a = list(sys.stdin.readline().split())
    # a = ["push", "14"]
    if a[0] == "push":
        stack.push(int(a[1]))
    elif a[0] == "top":
        print(stack.top())
    elif a[0] == "size":
        print(stack.size())
    elif a[0] == "pop":
        print(stack.pop())
    elif a[0] == "empty":
        print(stack.empty())
    loop_count -= 1
