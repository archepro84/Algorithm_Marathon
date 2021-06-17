start, end = 3, 16
len_prime = 1000000
prime_list = [True] * len_prime
prime_list[0] = False
result_list = []
for x in range(2, len(prime_list) + 1):
    if prime_list[x - 1]:
        for y in range(x * 2, len(prime_list) + 1, x):
            prime_list[y - 1] = False

# print()
# print(prime_list)
# print(prime_list[1])
for j in range(1, len(prime_list) + 1):
    # print(j, end=" ")
    if prime_list[j - 1]:
        result_list.append(j)
# print()
print(result_list[-3:])

# for x in result_list:
#     if start <= x and x <= end:
#         print(x)
