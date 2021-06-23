# import itertools
#
# n, k = map(int, input().split())
# l = itertools.combinations(range(1, n + 1), k)
#
# for x in l:
#     print(*x)

import sys
from typing import List

n, k = map(int, sys.stdin.readline().split())
# n, k = 4, 2
# n, k = 5, 4

results = []


def dfs(elements, start: int, k: int) -> List[List[int]]:
    if k == 0:
        results.append(elements[:])
    # n + 1 : 전체의 갯수를 출력하기 위해 사용 / n개의 갯수만큼 range 하기 위해 n+1을 사용
    for i in range(start, n + 1):
        elements.append(i)
        # i + 1 : 도표에서 한칸 내려가기 위해서 사용
        # k - 1 : 도표에서 한칸 우측으로 이동하기 위해서 사용
        dfs(elements, i + 1, k - 1)
        # 사용한 elements는 회수한다.
        elements.pop()


dfs([], 1, k)

for x in results:
    print(' '.join(map(str, x)))
