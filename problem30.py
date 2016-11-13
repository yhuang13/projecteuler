def sum_5th(num):
    num = str(num)
    num_sum = 0
    for digit in num:
        num_sum += int(digit)**5
    return num_sum

def digit_fifth():
    num_list = []
    for x in range(1,1000000):
        if sum_5th(x) == x:
            num_list.append(x)

    return num_list

print sum(digit_fifth()) - 1

