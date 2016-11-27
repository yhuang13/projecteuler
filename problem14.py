def divide_collatz(num):
    if num % 2 == 0:
        num = num/2
    else:
        num = 3 * num + 1
    return num

def return_collatz(num):
    chain = 0
    while num > 1:
        num = divide_collatz(num)
        chain += 1
    return chain

def collatz():
    longest_chain = 0
    collatz_num = 0
    for x in range(1,1000001):
        if return_collatz(x) > longest_chain:
            longest_chain = return_collatz(x)
            collatz_num = x
    return collatz_num

print collatz()