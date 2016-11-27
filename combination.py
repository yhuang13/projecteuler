
def power_set(num_list):
    p_set = [[]]
    for x in num_list:
        p_set_copy = list(p_set)
        p_set_copy = [y + [x] for y in p_set_copy]
        p_set.extend(p_set_copy)
    return p_set