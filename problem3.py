#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


def is_factor(num, factor):
    if num % factor == 0:
        return True
    return False

#num = 13195
num = 600851475143
factor_list = []


factor = 2
checknum = num/2

#check for the prime factors of factors
while factor < checknum and num > 1:
    if is_factor(num, factor):
        factor_list.append(factor)
        num = num/factor
    else:
        factor += 1

print max(factor_list)