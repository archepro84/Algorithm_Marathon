data = input()
# data = "ljes=njak"
# data = "ljddd-dz="
# data = "ddz=z="
# data = "nljj"
# data = "c=c="
# data = "dz=ak"

alphabet_count = 0
equal_list = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
else_alphabet = "dz="
count = 1  # 맨 마지막의 값은 크로아티아 전용 알파벳이 될 수 없다.
for i in range(len(data) - 1):
    if data[i] + data[i + 1] in equal_list:
        count -= 1
    elif data[i] == "d" and len(data) - i >= 3:
        if data[i:i + 3] == else_alphabet:
            count -= 1
    count += 1

print(count)
