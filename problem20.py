from math import factorial

num = factorial(100)
numsum = 0
for x in str(num):
    numsum += int(x)

print numsum