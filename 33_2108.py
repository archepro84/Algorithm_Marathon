from collections import defaultdict, Counter
import sys

_loop = int(sys.stdin.readline())
list1 = []
for _ in range(_loop):
    list1.append(int(sys.stdin.readline()))
list1.sort()

avg = f'{sum(list1) / len(list1):.0f}'
median = list1[len(list1) // 2]
list_range = list1[-1] - list1[0]
mode = defaultdict(int)

for x in list1:
    mode[x] += 1
cunter = Counter(mode).most_common(2)

print(avg)
print(median)
if len(list1) != 1:
    if cunter[0][1] > cunter[1][1]:
        print(cunter[0][0])
    else:
        print(cunter[1][0])
else:
    print(list1[0])
print(list_range)
