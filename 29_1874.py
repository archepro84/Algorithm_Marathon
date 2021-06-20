import sys

list1 = []
loop_index = int(sys.stdin.readline())
for x in range(loop_index):
    list1.append(int(sys.stdin.readline()))

stack_list = [0]
insert_index, list_index = 1, 0
result_list = []
while insert_index <= loop_index + 1:
    if list_index >= len(list1):
        break
    elif list1[list_index] != stack_list[-1]:
        stack_list.append(insert_index)
        result_list.append("+")
        insert_index += 1
    else:
        stack_list.pop()
        result_list.append("-")
        list_index += 1

if list_index < loop_index:
    print("NO")
else:
    for x in result_list:
        print(x)
