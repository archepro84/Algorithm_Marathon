# string = "So when I die (the [first] I will see in (heaven) is a score list)."
string = "([ (([( [ ] ) ( ) (( ))] )) ])."


# string = "Half Moon tonight (At least it is better than no Moon at all]."
# string = "Help( I[m being held prisoner in a fortune cookie factory)]."


def search_item(string):
    small_list = []
    big_list = []
    index = []
    for x in string:
        if x == "[":
            big_list.append(x)
            index.append("[")
        elif x == "]":
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


result = search_item(string)
if result:
    print("no")
else:
    print("yes")
