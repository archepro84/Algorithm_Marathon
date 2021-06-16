# from datetime import datetime

data = int(input())
result = 0
# now = datetime.now()

five = data // 5
three = (data % 5)
while three % 3 != 0:
    five -= 1
    three += 5

    if five < 0:
        break

if five < 0:
    print("-1")
else:
    # print("data : ", data)
    print(five + (three // 3))

# print(datetime.now() - now)
