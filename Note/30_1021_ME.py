list_size = 10
list1 = [x for x in range(1, list_size + 1)]
input_list = [2, 9]
# input_list = [2, 9, 5]
index, input_list_index = 0, 0
count = 0
# find_index = None

# 현재 input_list의 첫번째 값이 리스트의 몇 번째 값에 있는가?
find_index = list1.index(input_list[0], 0, len(list1) - 1)
# 현재 input_list의 첫번째 값이 리스트의 뒤에서 몇 번째 있는가?
find_index_reverse = -(len(list1) - find_index)

while input_list:
    # if find_index == None:
    #     # 현재 input_list의 첫번째 값이 리스트의 몇 번째 값에 있는가?
    #     find_index = list1.index(input_list[0], 0, len(list1) - 1) + 1
    #     # 현재 input_list의 첫번째 값이 리스트의 뒤에서 몇 번째 있는가?
    #     find_index_reverse = -(len(list1) - find_index)

    if input_list[0] == list1[index]:
        list1.pop(index)
        input_list.pop(0)
        # find_index = None

        # 현재 input_list의 첫번째 값이 리스트의 몇 번째 값에 있는가?
        find_index = list1.index(input_list[0], 0, len(list1) - 1)
        # 현재 input_list의 첫번째 값이 리스트의 뒤에서 몇 번째 있는가?
        find_index_reverse = len(list1) - find_index

    elif abs(find_index_reverse - index) < find_index - index:
    # elif index - find_index < index - find_index_reverse:
        index -= 1
        count += 1
        if index < 0:
            index = len(list1) - 1
    else:
        index += 1
        count += 1

    print(find_index, find_index_reverse)
    print(index - find_index)
    print(index - find_index_reverse)
    print(abs(index - find_index))
    print(abs(index - find_index_reverse))
    print(list1, input_list, index, count)
print(list1)
print(count)
