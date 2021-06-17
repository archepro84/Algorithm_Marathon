result_list = []
count = 0


def swap_index(hanoi_list, index1, index2):
    global count
    global result_list
    # print(hanoi_list, index1, index2)
    result_list.append(f"{index1} {index2}")
    count += 1


def hanoi_top(hanoi_list, start=1, end=3):
    other = 6 - start - end
    if hanoi_list == 1:
        swap_index(hanoi_list, start, end)
        return
    hanoi_top(hanoi_list - 1, start, other)
    swap_index(hanoi_list, start, end)
    hanoi_top(hanoi_list - 1, other, end)


hanoi_top(int(input()))

print(count)
for x in result_list:
    print(x)

"""
Start 의 Other의 Other  = End
"""
