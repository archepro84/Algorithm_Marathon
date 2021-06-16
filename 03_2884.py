a, b = map(int, input().split(' '))
# a, b = 10, 10
# a, b = 0, 30
# a, b = 23, 40
b -= 45

if b < 0:
    a -= 1
    b += 60
if a > 24:
    a -= 24
elif a < 0:
    a += 24

print(a, b)
