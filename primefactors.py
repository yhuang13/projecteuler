def is_factor(num, factor):
    return num % factor == 0

def return_prime_factor_list(num):
    factor_list = []
    factor = 2

    while num > 1:
        if is_factor(num, factor):
            factor_list.append(factor)
            num = num/factor
        else:
            factor += 1
    return factor_list
