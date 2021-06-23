import sys

# stairs = [10, 20, 15, 25, 10, 20]
# stairs = [10, 20]


n = int(sys.stdin.readline())
stairs = []
dp = [0] * (n + 1)
for x in range(n):
    stairs.append(int(sys.stdin.readline()))


def stairs_2597(stairs):
    dp[0] = stairs[0]
    if n == 1:
        print(dp[0])
        return
    dp[1] = stairs[1] + stairs[0]
    if n == 2:
        print(dp[1])
        return
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    print(dp[n - 1])


stairs_2597(stairs)
