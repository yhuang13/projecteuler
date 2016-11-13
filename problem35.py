#How many circular primes are there below one million?

from primes import *
from itertools import *


def rotate_digit(num):
    num = str(num)
    num_list = [num]
    i = 0
    while len(num_list) < len(num):
        num_list.append(num_list[i][-1]+num_list[i][:-1])
        i += 1
    return [int(n) for n in num_list]



def circ_primes(num):
    primes = set(sieve(num))
    circle_list = []
    for prime in primes:
        check_list = rotate_digit(prime)
        valid_circle = True
        for n in check_list:
            if n not in primes:
                valid_circle = False
                break
        if valid_circle:
            circle_list.append(prime)
    return len(circle_list)

print circ_primes(1000000)
