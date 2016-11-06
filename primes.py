def sieve_list(num):
    num_list = []
    x = 2
    while x <= num:
        num_list.append(x)
        x += 1
    return num_list

def remove_multiple(x, num_list):
    multiple = 2
    while multiple * x <= len(num_list) + 1:
        num_list[multiple * x - 2] = 0
        multiple += 1


def sieve(num):
    num_list = sieve_list(num)
    prime_list = []
    x = 2
    while x <= num:
        remove_multiple(x, num_list)
        x += 1
    for n in num_list:
        if n:
            prime_list.append(n)
    return prime_list

