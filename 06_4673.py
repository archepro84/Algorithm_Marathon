number = 1
loop_count = 10000
number_list = [True] * loop_count

while number <= loop_count:
    temp_number = number
    result = number

    while temp_number:
        remainder = temp_number % 10
        result += remainder
        temp_number = temp_number // 10
    # print(number, result)

    if result - 1 < loop_count:
        number_list[result - 1] = False
    number += 1

for i, x in enumerate(number_list):
    if x:
        print(i + 1)
