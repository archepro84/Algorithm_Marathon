alphabet = input().upper()
# alphabet = "Mississipi".upper()
# alphabet = "zZa".upper()
# alphabet = "z".upper()
# alphabet = "baaa".upper()
alphabet_list = [0] * 26
for x in alphabet:
    alphabet_list[ord(x) - ord("A")] += 1
# print(alphabet_list)

count = 0
index = 0
for i, x in enumerate(alphabet_list):
    if x == max(alphabet_list):
        count += 1
        index = i
if count > 1:
    print("?")
else:
    print(chr(index + ord("A")))
