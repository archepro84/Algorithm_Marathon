"""
666이 연속으로 나오는 것 ..
666이 나오고
6660 부터는 + 10
66600 부터는 + 100
666000 부터는 + 1000

최초 구현시 시간복잡도를 생각하지 않고 구현하자
"""
data = 10
shom_list = [False] * 100000
index = 666
i = 0
one_squal = 1
two_squal = 2


def squal_divid(data, sqaul):
    return data // (10 ** sqaul) * (10 ** sqaul)


for i in range(0, 10 ** 2):
    index = (1000 * i) + 666
    print(index)

    if index // (10 ** two_squal) % 1000 == 666:
        for x in range(0, 10 ** two_squal):
            result = squal_divid(index, two_squal) + x
            print(result)

    # if index // 100 % 1000 == 666:
    #     for x in range(0, 10 ** two_squal):
    #         result = index - 66 + x
    #         print(result)
    # elif index // 10 % 1000 == 666:
    #     for x in range(0, 10 ** one_squal):
    #         result = index - 6 + x
    #         print(result)
