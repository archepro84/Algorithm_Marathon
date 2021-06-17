def swap_index(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


def partition(my_list, start, end):
    index, big_index = start, start
    while index < end:
        if my_list[index] <= my_list[end]:
            swap_index(my_list, index, big_index)
            big_index += 1
        index += 1
    swap_index(my_list, big_index, end)
    # print(my_list)
    return big_index


def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1
    if end - start < 1:
        return
    index = partition(my_list, start, end)
    quicksort(my_list, start, index - 1)
    quicksort(my_list, index + 1, end)


# # a = 2
# # measure = [4,2]
# a = 72
# measure = [2, 3, 4, 6, 8, 9, 12, 18, 24, 36]
a = int(input())
measure = list(map(int, input().split(' ')))

# list1 = [1, 3, 2, 6, 2, 4, 7, 77, 44, 32, 1, 1, 1, 1]
# quicksort(list1)
# print(list1)

quicksort(measure)
print(measure[0] * measure[-1])
# print(measure)
