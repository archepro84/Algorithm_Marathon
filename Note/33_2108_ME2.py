from collections import defaultdict, Counter
import sys

loop_count = int(sys.stdin.readline())
list1 = []
for _ in range(loop_count):
    list1.append(int(sys.stdin.readline()))

# list1 = [1, 3, 8, -2, 2]
list1.sort()

avg = f'{sum(list1) / len(list1):.0f}'
median = list1[len(list1) // 2]
list_range = list1[-1] - list1[0]
# print(avg, median, list_range)

mode = defaultdict(int)
for x in list1:
    mode[x] += 1
# print(Counter(mode).most_common(2))
most_counter = Counter(mode).most_common(2)

if len(list1) != 1:
    print(avg)
    print(median)
    if most_counter[0][1] > most_counter[1][1]:
        print(most_counter[0][0])
    else:
        print(most_counter[1][0])
else:
    print(list1[0])
    print(list1[0])
    print(list1[0])
print(list_range)
