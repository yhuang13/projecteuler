#What is the value of the first triangle number to have over five hundred divisors?

from primefactors import *

last_triangle_num = 0
next_x = 1



def nth_triangle_num():
    global last_triangle_num
    global next_x
    last_triangle_num += next_x
    next_x += 1
    return last_triangle_num


def factor_list(n):
    f_list = set([])
    for x in range(1,n/2):
        if n % x == 0:
            f_list.add(x)
            f_list.add(n/x)
    print(len(f_list))
    return len(f_list)

def power_set(num_list):
    x = len(num_list)
    for i in range (1 < x):
        return num_list[x] for j in range(x) if 

def get_factors(prime_list):
    power_set = []
    pos = 0
    if pos == 0:
        power_set.append([])
    else:
        power_set.append(prime_list[pos])

print get_factors(return_prime_factor_list(6))

def calculate_500_divisor():
    factors = set([])
    while len(factors) <= 500:
        factors = get_factors(return_prime_factor_list(nth_triangle_num()))

#print calculate_500_divisor()