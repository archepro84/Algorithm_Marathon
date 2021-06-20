list1 = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1]
]

# list1 = [
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]
# list1 = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ]

# print(list1)

"""
재귀 함수로 풀어야 할듯
"""

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
        print("white ", row, colum, size, count)
        white += 1
    elif count == size ** 2:
        print("blue", row, colum, size, count)
        blue += 1
    else:
        size = size // 2
        paper(row, colum, size)
        paper(row + size, colum, size)
        paper(row, colum + size, size)
        paper(row + size, colum + size, size)


# size = size // 2


# print(size)
# paper(row, colum, size)


paper(0, 0, len(list1[0]))
print(white, blue)
