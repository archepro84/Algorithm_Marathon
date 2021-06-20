import sys


def search_item(string):
    small_list = []
    big_list = []
    index = []
    for x in string:
        if x == "[":
            big_list.append(x)
            index.append("[")
        elif x == "]":
            # 파이썬 if문의 특성을 이용함
            # if 안에 or 이 있으면 왼쪽부터 True가 발생하면 오른쪽의 연산은 보지않는다.
            # 그러므로 index.pop()의 데이터가 없어도 오류가 발생하지 않음.
            if not len(big_list) or index.pop() != "[":
                return 1
            big_list.pop()
        elif x == "(":
            index.append("(")
            small_list.append(x)
        elif x == ")":
            if not len(small_list) or index.pop() != "(":
                return 1
            small_list.pop()
    return len(big_list) + len(small_list)


result_list = []

while True:
    # string = "So when I die (the [first] I will see in (heaven) is a score list)."
    string = sys.stdin.readline()
    if string[0] == ".":
        break

    result = search_item(string)
    if result:
        result_list.append("no")
    else:
        result_list.append("yes")

for x in result_list:
    print(x)
