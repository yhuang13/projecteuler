#Evaluate the sum of all the amicable numbers under 10000.

def factor_list(n):
    f_list = set([])
    if n == 2 or n == 3:
        for x in range(1,n):
            if n % x == 0:
                f_list.add(x)
                f_list.add(n/x)
    else:
        for x in range(1,n/2+1):
            if n % x == 0:
                f_list.add(x)
                f_list.add(n/x)
    return f_list

def factor_sum(num_list):
    num_sum = 0
    for x in num_list:
        num_sum += x
    return num_sum

def amicable():
    x = 2
    ami_total = 0
    while x < 10000:
        a = factor_sum(factor_list(x)) - x
        b = factor_sum(factor_list(a)) - a
        if b == x and a != b:
            ami_total += x
        x += 1
    return ami_total


print amicable()