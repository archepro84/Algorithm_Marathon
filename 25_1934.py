import sys

loop_count = int(sys.stdin.readline())
result_list = []
while loop_count:
    a, b = map(int, sys.stdin.readline().split())
    max_number = 1
    for x in range(min(a, b), 1, -1):
        # print(x, end=" ")
        if a % x == 0 and b % x == 0:
            max_number = x
            break
    # print(max_number)

    result = (a * b) // max_number
    # print(result)
    result_list.append(result)
    loop_count -= 1
    # print()

for x in result_list:
    print(x)
#
#
# # a, b = 1, 45000
# # a, b = 6, 10
# # a, b = 13, 17
# # a, b = 44444, 450000
# a,b = 60,48
# # a, b = 72, 126
#
# max_number = 1
# for x in range(2, min(a, b) + 1):
#     if a % x == 0 and b % x == 0:
#         max_number = x
#         break
# print(max_number)
# result = (a * b) // max_number
# print(result)
