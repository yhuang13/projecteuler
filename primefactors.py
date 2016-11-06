def is_factor(num, factor):
    if num % factor == 0:
        return True
    return False

def return_prime_factor_list(num):
    factor_list = []
    factor = 2

    # check for the prime factors of factors
    while factor <= num and num > 1:
        print factor
        print is_factor(num, factor)
        if is_factor(num, factor):

            factor_list.append(factor)
            num = num / factor
        else:
            factor += 1
            print factor
            print num
        return factor_list