#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

from primes import *

prime_list = sieve(2000000)

num_sum = 0
for x in prime_list:
    num_sum += x

print num_sum