#What is the sum of the digits of the number 2^1000?

num_sum = 0

num = 2**1000

for x in str(num):
    num_sum += int(x)

print num_sum