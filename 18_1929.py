len_prime = 1000000
prime_list = [True] * len_prime
prime_list[0] = False
result_list = []
for x in range(2, len(prime_list) + 1):
    if prime_list[x - 1]:
        for y in range(x * 2, len(prime_list) + 1, x):
            prime_list[y - 1] = False

for j in range(1, len(prime_list) + 1):
    if prime_list[j - 1]:
        result_list.append(j)

start, end = map(int, input().split(' '))

for x in result_list:
    if start <= x and x <= end:
        print(x)
