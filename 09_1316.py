loop_count = int(input())
# loop_count = 1
count = 0
while loop_count:
    data = input()
    # data = "ccazzzzzbb"
    check_alphabet = data[0]
    duplication_list = []
    for i in range(len(data)):
        if data[i] in duplication_list:
            # print(data[i], duplication_list)
            count -= 1
            break
        if data[i] != check_alphabet:
            # print("import", i, data[i])
            duplication_list.append(data[i - 1])
            check_alphabet = data[i]
    # print(duplication_list)
    count += 1
    loop_count -= 1

print(count)
