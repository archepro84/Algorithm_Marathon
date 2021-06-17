loop_count = int(input())
list2 = []
while loop_count:
    data = list(map(int, input().split(' ')))
    list2.append(data)
    loop_count -= 1

list2.sort(key=lambda dd: (dd[1], dd[0]))

for x in list2:
    print(x[0], x[1])
