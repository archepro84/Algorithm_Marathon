import sys

list_size = int(sys.stdin.readline())
list1 = []
for x in range(list_size):
    list1.append(list(map(int, sys.stdin.readline().split())))
# list_size = 8
#
# list1 = [
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1]
# ]

white = 0
blue = 0


def paper(row, colum, size):
    global white
    global blue
    if size < 2:
        if list1[row][colum] == 0:
            white += 1
        else:
            blue += 1
        return
    count = 0
    for x in range(row, row + size):
        for j in range(colum, colum + size):
            if list1[x][j] == 1:
                count += 1
    if count == 0:
        # print("white ", row, colum, size, count)
        white += 1
    elif count == size ** 2:  #핵심
        # print("blue", row, colum, size, count)
        blue += 1
    else:
        size = size // 2
        paper(row, colum, size)
        paper(row + size, colum, size)
        paper(row, colum + size, size)
        paper(row + size, colum + size, size)


paper(0, 0, list_size)
print(white)
print(blue)
