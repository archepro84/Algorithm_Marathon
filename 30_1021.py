import sys
"""
list를 회전 시킬 때 Input_list의 값이 
"""

list_size, loop_count = map(int, sys.stdin.readline().split())
# list_size = 10
list1 = [x for x in range(1, list_size + 1)]
# input_list = [2, 9, 5]
input_list = list(map(int, sys.stdin.readline().split()))

result_count = 0


def left_queue(list1):
    temp = list1.pop(0)
    list1.append(temp)


def right_queue(list1):
    # TODO list의 insert가 시간 복잡도 O(N)이기 때문에 다른방식으로 수정가능한지 생각해볼 것
    temp = list1.pop()
    list1.insert(0, temp)


# left_queue(list1)
# print(list1)
# right_queue(list1)
# print(list1)

while input_list:
    # print(list1.index(input_list[0], 0, len(list1) - 1))
    find_index = list1.index(input_list[0], 0, len(list1))
    # print(find_index)

    if find_index > len(list1) // 2:
        # print("Right")
        while input_list[0] != list1[0]:
            right_queue(list1)
            result_count += 1
        list1.pop(0)
        input_list.pop(0)
        # print("Result Right : ", result_count)
    else: # Left 우선으로 설정하지 않으면 오류 발생
        # print("Left")
        while input_list[0] != list1[0]:
            left_queue(list1)
            result_count += 1
        list1.pop(0)
        input_list.pop(0)
        # print("Result Left : ", result_count)

    # print(list1)

print(result_count)
