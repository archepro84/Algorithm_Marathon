def search_function(data_list):
    result_list = []
    for x in range(len(data_list)):
        if (x == 0 and data_list[x] == ")") or \
                (x == len(data_list) - 1 and data_list[x] == "("):
            return "NO"
        elif data_list[x] == "(":
            result_list.append("(")
        elif data_list[x] == ")":
            if not len(result_list):
                return "NO"
            result_list.pop()

    if not len(result_list):
        return "YES"
    return "NO"


loop_count = int(input())
while loop_count:
    print(search_function(input()))
    loop_count -= 1

# print(search_function("()()()()(()()())()"))
