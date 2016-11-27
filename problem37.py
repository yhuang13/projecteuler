from primes import *



def truncate_list(num):
    truncated = set([])
    num = str(num)
    x = 0
    while x < len(num):
        # left to right remove numbers
        truncated.add(int(num[x:len(num)]))
        # right to left remove numbers
        truncated.add(int(num[0:x+1]))
        x += 1
    return truncated



def truncate_prime():
    prime_list = set(sieve(900000))
    t_prime = set([])
    for x in prime_list:
        t_list = truncate_list(x)
        if x > 10 and reduce(lambda r, y: r and y in prime_list, t_list, True):
            t_prime.add(x)
    return t_prime

print sum(truncate_prime())
