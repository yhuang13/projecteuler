def distinct():
    min_range = 2
    max_range = 100

    num_list = []

    for a in range(min_range,max_range+1):
        for b in range(min_range,max_range+1):
            num_list.append(a**b)
            print a**b
    
    num_list = set(num_list)

    return len(num_list)