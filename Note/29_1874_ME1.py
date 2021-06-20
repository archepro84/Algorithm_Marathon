"""
Max값과, 다음에 나온 값보다 높을 수 없다.
즉,
4 2 3 과 같이 한번 뛰어 넘은 경우 나올 수 없다.
"""

import sys

# list1 = [4, 3, 6, 8, 7, 5, 2, 1]
# loop_index = 8
# list1 = [1, 2, 5, 3, 4]
# loop_index = 5

list1 = []
loop_index = int(sys.stdin.readline())
temp_inedx = loop_index
while temp_inedx:
    list1.append(int(sys.stdin.readline()))
    temp_inedx -= 1
# print(list1)

stack_list = [0]
insert_index = 1
list_index = 0
result_list = []
while insert_index <= loop_index + 1:
    try:
        if list_index >= len(list1):
            break
        if list1[list_index] != stack_list[-1]:
            stack_list.append(insert_index)
            result_list.append("+")
            insert_index += 1
        else:
            stack_list.pop()
            # print(stack_list.pop())
            result_list.append("-")
            list_index += 1
    except:
        # print(list_index, len(list1))
        result_list = ["NO"]
        break

# print(list_index, insert_index, loop_index)

if list_index < loop_index:
    print("NO")
else:
    for x in result_list:
        print(x)
