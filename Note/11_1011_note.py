"""
일시적이 변수가 많아져서 코드가 햇갈리기 시작함 쓸모 없는 변수들을 정리해봐야겠다.
now_length를 매번 계산하는게 연산을 많이 잡아먹는다고 생각함
"""

# start_length, end_length = 0, 3
# start_length, end_length = 1, 5
# start_length, end_length = 45, 50
start_length, end_length = 0, 5000
speed = 1
count = 0

now_length = speed
length = end_length - start_length
# location = start_length

# while location < end_length:
while length:
    # print(length, speed, location)
    print(length, speed)
    length -= speed
    # location += speed
    count += 1

    next_length = now_length + speed + 1
    print(now_length, next_length, length)

    if next_length <= length:
        speed += 1
        now_length += speed
    elif now_length == length or \
            (now_length < length and next_length > length):
        print(now_length, next_length, length)
        print("Hello")
        pass
    else:
        now_length -= speed
        speed -= 1

    # if count > 5:
    #     break
    print()

# print(length, speed, location)
print(length, speed)
print(count)
