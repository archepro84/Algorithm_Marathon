a = int(input())
# a = 1
b = a % 10
result = (a // 10) + b

count = 1
while True:
    result = (b * 10) + result % 10
    if a == result:
        break
    b = result % 10
    result = result // 10 + result % 10
    count += 1
    # print(b, result)

# print(result, count)
print(count)

"""
어째서 1이 60이되고 0이 1이 되는것인가?
# (0 // 10) + (0 % 10)
# 0 +  0
"""
