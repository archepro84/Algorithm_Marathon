import sys

_, length = map(int, sys.stdin.readline().split())
lumber_list = list(map(int, sys.stdin.readline().split()))
# length = 7
# lumber_list = [20, 15, 10, 17]

start, end = 0, max(lumber_list)
axe_index = 0

# End 포인트가 Start보인트보다 작아졌을 경우 종료한다.
while start <= end:
    result_sum = 0

    # 이진탐색으로 중앙값을 찾는다.
    mid = (start + end) // 2

    # 잘린 나무의 길이를 계산
    for x in lumber_list:
        if x - mid > 0:
            result_sum += x - mid

    # 잘린 나무의 길이를 비교
    if result_sum < length:
        end = mid - 1
    else:
        axe_index = mid
        start = mid + 1
print(axe_index)
