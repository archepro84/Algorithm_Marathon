import math

loop_count = int(input())
result_list = []
while loop_count:
    h, w, n = map(int, input().split(' '))
    # h, w, n = 6, 12, 10
    # h, w, n = 30, 50, 72

    x = math.ceil(n / h)
    # print(x)
    y = h if n % h == 0 else n % h
    # print(y)
    # print(y * 100 + x)
    result_list.append(y * 100 + x)
    loop_count -= 1
for x in result_list:
    print(x)
#
# # h, w, n = map(int, input().split(' '))
# h, w, n = 6, 12, 10
# # h, w, n = 30, 50, 72
# # h, w, n = 7, 88, 14
#
# x = math.ceil(n / h)
# # print(x)
# # y = n % h
# # if y == 0:
# #     y = h
# y = h if n % h == 0 else n % h
# # print(y)
# print(y * 100 + x)
