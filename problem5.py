#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

start = 2520

factor_list = [11, 13, 17, 19]

for x in factor_list:
    start = start * x

start = start * 2

factors = range(1,21)

for factor in factors:
    if start % factor != 0:
        print factor

print start