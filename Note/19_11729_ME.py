def swap_index(hanoi_list, index1, index2):
    print(hanoi_list, index1, index2)


def hanoi_top(hanoi_list, start=1, end=3):
    other = 6 - start - end
    if hanoi_list == 1:
        swap_index(hanoi_list, start, end)
        return
        # swap_index(hanoi_list, start, end)
    hanoi_top(hanoi_list - 1, start, other)
    swap_index(hanoi_list, start, end)
    hanoi_top(hanoi_list - 1, other, end)


in_number = 3
hanoi_top(in_number)

print(2 ** in_number - 1)
