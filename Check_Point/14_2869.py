import math

# move, back, length = map(int, input().split(' '))

# move, back, length = [2, 1, 5]
move, back, length = 5, 1, 6
# move, back, length = 100, 99, 1000000000


back_length = length - back
day_move = move - back
# print(back_length, day_move)
# print(back_length / day_move)
# print(math.ceil(back_length / day_move))

print(f"Input : {move, back, length}")
print(f"DayMove : {day_move}")
print(f"Lenght - Back : {back_length}")
print(f"(Lenght - Back) / DayMove  : {back_length / day_move}")
print(f"math.ceil( ( Lenght - Back ) / DayMove )  : {math.ceil(back_length / day_move)}")
