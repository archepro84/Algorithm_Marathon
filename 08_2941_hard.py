data = input()
# data = "ljes=njak"
# data = "ljddd-dz="
# data = "ddz=z="
# data = "nljj"
# data = "c=c="
# data = "dz=ak"
data_index = len(data)
equal_list = ["c=", "c-", "d-", "lj", "nj", "s=", "z=", "dz="]
for l in equal_list:
    data_index -= data.count(l)
print(data_index)
