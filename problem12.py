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




def power_set(num_list):
    p_set = [[]]
    for x in num_list:
        p_set_copy = list(p_set)
        p_set_copy = [y + [x] for y in p_set_copy]
        p_set.extend(p_set_copy)
    return p_set


def calculate_500_divisor():
    factors = set([])
    while len(factors) < 500:
        prime_factors = return_prime_factor_list(nth_triangle_num())
        p_set = power_set(prime_factors)
        factors = set([])
        for x in p_set:
            factors.add(reduce(lambda a, b: a*b, x, 1))
    return last_triangle_num

print calculate_500_divisor()