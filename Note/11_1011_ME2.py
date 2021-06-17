"""
일시적이 변수가 많아져서 코드가 햇갈리기 시작함 쓸모 없는 변수들을 정리해봐야겠다.
now_length를 매번 계산하는게 연산을 많이 잡아먹는다고 생각함
"""

loop_count = int(input())
result_list = []
while loop_count:
    start_length, end_length = map(int, input().split(' '))
    speed = 1
    count = 0

    now_length = speed
    length = end_length - start_length

    while length:
        length -= speed
        count += 1

        next_length = now_length + speed + 1

        if next_length <= length:
            speed += 1
            now_length += speed
        elif now_length <= length and next_length > length:
            pass
        else:
            now_length -= speed
            speed -= 1

    result_list.append(count)
    loop_count -= 1

for x in result_list:
    print(x)
