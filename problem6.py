#etween the sum of the squares of the first one hundred natural numbers and the square of the sum.

min_num = 1
max_num = 100

sum_square = 0

for x in range(min_num, max_num + 1):
    sum_square += x**2


square_sum = 0
for x in range(min_num, max_num + 1):
    square_sum += x

square_sum = square_sum ** 2

print square_sum - sum_square