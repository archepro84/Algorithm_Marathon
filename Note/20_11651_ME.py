def swap_list(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


def partition(my_list, start, end):
    index, big_index = start, start

    while index < end:
        if my_list[index] < my_list[end]:
            swap_list(my_list, index, big_index)
            big_index += 1
        index += 1

    swap_list(my_list, big_index, end)
    return big_index


def quicksort(my_list, start, end):
    if end - start < 1:
        return
    r = partition(my_list, start, end)
    quicksort(my_list, start, r - 1)
    quicksort(my_list, r + 1, end)


# list1 = [1, 3, 2, 77, 66, 4745, 6655, 4, 23, 232, 4, 2, 3, 2, 3, 4, 11, 1, 1, 3, 222, 33, 344, 2, 2, 3, 2, 22, 3, 4]
# quicksort(list1, 0, len(list1) - 1)
# print(list1)

# list2 = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
# list2 = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3), (2, 3), (2, 2), (1, 2),(9,2)]
# print(list2)

loop_count = int(input())
list2 = []
while loop_count:
    data = list(map(int, input().split(' ')))
    list2.append(data)
    loop_count -= 1

list2.sort(key=lambda dd: (dd[1], dd[0]))
# print(list2)

for x in list2:
    print(x[0], x[1])
