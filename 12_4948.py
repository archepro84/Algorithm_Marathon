# from datetime import datetime
# now = datetime.now()

prime_list = [True] * 123456 * 2
prime_list[0] = False
index = 2
while index < len(prime_list):
    if prime_list[index - 1]:
        for x in range(index * 2, len(prime_list), index):
            prime_list[x - 1] = False
    index += 1
count = [x for x in range(1, len(prime_list)) if prime_list[x - 1]]
# print(count[-3:])

case = int(input())
result_list = []
while case:
    result = 0
    # case = 100000
    for number in count:
        if case < number and number <= case * 2:
            # print(number)
            result += 1
    result_list.append(result)
    # print(result)
    case = int(input())

for x in result_list:
    print(x)

# print(datetime.now() - now)
