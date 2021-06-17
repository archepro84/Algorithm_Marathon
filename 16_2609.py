# a, b = map(int, input().split(' '))
a, b = 20, 13
# a, b = 24, 18
# a, b = 72, 126
# a, b = 60, 48
# a, b = 24, 18
# a, b = 24, 18
max_measure = 1
for x in range(min(a, b), 1, -1):
    # print(x, end=" ")
    if a % x == 0 and b % x == 0:
        max_measure = x
        break
print(max_measure)

# result = a % b if a > b else b % a
# print(result)
result = a * b // max_measure
print(result)
