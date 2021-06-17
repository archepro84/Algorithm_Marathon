length = 7
lumber_list = [20, 15, 10, 17]
lumber_list.sort()

start, end = 0, max(lumber_list)
while start <= end:
    mid = (start + end) // 2
    lumber = 0
    for x in lumber_list:
        if x > mid:
            lumber += x - mid
    print(mid)
    if lumber < length:
        end = mid - 1
    else:
        start = mid + 1
print()
print(end)



#
# my_length = 7
# lumber_list = [20, 15, 10, 17]
# lumber_list.sort()
#
# # def binary_search(my_list, target_item):
# #     index = len(my_list) // 2
# #     # print(my_list, index, my_list[index])
# #     if len(my_list) < 1:
# #         return False
# #     if my_list[index] == target_item:
# #         return True
# #     elif my_list[index] < target_item:
# #         # print("HEllo", my_list[:index - 1])
# #         return binary_search(my_list[index + 1:len(my_list)], target_item)
# #     else:
# #         # print("HEllo", my_list[:index - 1])
# #         return binary_search(my_list[:index - 1], target_item)
# #
# #
# # # print(lumber_list)
# # print(binary_search(lumber_list, 20))
#
#
# start, end = 1, max(lumber_list)
# count = 0
# while start <= end:
#     mid = (start + end) // 2
#     log = 0
#     for i in lumber_list:
#         if i >= mid:
#             log += i - mid
#     if log >= my_length:
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(end)
