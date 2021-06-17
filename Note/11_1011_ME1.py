loop_count = int(input())
result_list = []
while loop_count:
    start_length, end_length = map(int, input().split(' '))

    speed = 1
    length = end_length - start_length
    location = start_length
    count = 0

    while location < end_length:
        length -= speed
        location += speed
        count += 1

        now_length = sum([x for x in range(1, speed + 1)])
        next_length = now_length + speed + 1

        if next_length <= length:
            speed += 1
        elif now_length == length or \
                (now_length < length and next_length > length):
            pass
        else:
            speed -= 1

    result_list.append(count)
    loop_count -= 1

for x in result_list:
    print(x)
