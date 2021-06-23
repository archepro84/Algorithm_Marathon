import sys

n = int(sys.stdin.readline())


def dfs_queen(n):
    columns, diagonals1, diagonals2 = list(), list(), list()

    return dfs(n, 0, columns, diagonals1, diagonals2)


def dfs(n, row, columns, diagonals1, diagonals2):
    if row == n:
        return 1

    cnt = 0
    for col in range(n):
        # 현재의 퀸 자리에서 대각선 또는 좌우, 상하를 검색하는 것
        if col in columns or (row + col) in diagonals1 or (row - col) in diagonals2:
            continue

        columns.append(col)  # 상하
        diagonals1.append(row + col)  # 좌측 대각선
        diagonals2.append(row - col)  # 우측 대각선

        # 다음줄에 퀸 설치 가능 확인
        cnt += dfs(n, row + 1, columns, diagonals1, diagonals2)

        columns.pop()
        diagonals1.pop()
        diagonals2.pop()

    return cnt


print(dfs_queen(n))
