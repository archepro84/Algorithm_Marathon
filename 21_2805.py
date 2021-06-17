import sys

n, length = map(int, sys.stdin.readline().split(' '))
lumber_list = list(map(int, sys.stdin.readline().split(' ')))


def tree_sum(height):
    sum_data = 0
    for i in lumber_list:
        if i - height > 0:
            sum_data += i - height
    return sum_data


def binary_search(target):
    start, end = 0, max(lumber_list)
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        sum_data = tree_sum(mid)
        if sum_data < target:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans


print(binary_search(length))
