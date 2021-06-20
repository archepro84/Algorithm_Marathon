# import sys

result = []
# loop_count = int(sys.stdin.readline())
loop_count = int(input())
while loop_count:
    # a = int(sys.stdin.readline())
    a = int(input())
    # if a == 0:
    #     result.pop()
    # else:
    #     result.append(a)

    result.pop() if a == 0 else result.append(a)
    loop_count -= 1
    # print(result)

print(sum(result))
