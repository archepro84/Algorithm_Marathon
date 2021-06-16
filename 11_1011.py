"""
이전 작동시기에 k 광년을 이동하였을 때는 k-1, k 혹은 k+1 광년만을 다시 이동할 수 있다.
처음 작동 시킬 경우 -1, 0 , 1 광년을 이론상 이동할 수 있으나
사실상 음수 혹은 0거리만큼의 이동은 의미가 없으므로 1광년을 이동할 수 있으며
그다음에는 0, 1,2 광년을 이동할 수 있는 것이다.
여기서 다시 2광년을 이동한다면 1,2,3광년을 이동할 수 있다.
마지막 도착 직전의 거리는 반드시 1광년으로 하려한다
x지점에서 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램

그래프를 그리자면 좌상향 우하향의 그래프를 그래야 한다.
현재의 값에서 -1씩하여 1로 도착할때까지의 총 거리를 계산할 수 있어야 한다.
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

