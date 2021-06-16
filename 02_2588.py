a = int(input())
b = int(input())
# a = 472
# b = 385
number_list = []
result = 0
while b:
    temp_b = b % 10
    number_list.append(temp_b)
    b = b // 10

# print(number_list)
for x in range(len(number_list)):
    print(a * number_list[x])
    result += a * number_list[x] * (10 ** x)
print(result)


