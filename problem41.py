#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

from primefactors import *
from itertools import *


def pandigital(num):
    digits = set([])
    for x in range(len(str(num))):
        digits.add(str(num)[x])
    return len(str(num)) == len(digits)

def pan_prime():
    largest_pan = 0
    check_list = []
    for x in range(9, 0, -1):
        check_list.extend([int(''.join([str(e) for e in x])) for x in permutations(range(1, x+1), x)])
        check_list.sort(reverse=True)
        for y in check_list:
            if len(return_prime_factor_list(y)) == 1 and y > largest_pan:
                return y


print pan_prime()