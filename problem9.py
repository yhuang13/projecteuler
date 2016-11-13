#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.



def check_pythagorean(a, b, c):
    return a**2 + b**2 == c**2



def check_triplet():
    for a in range(1,1001):
        for b in range(a+1,1001):
            if check_pythagorean(a,b,(1000-a-b)):
                return a*b*(1000-a-b)


print check_triplet()