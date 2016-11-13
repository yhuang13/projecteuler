def name_value(name):
    name = name.lower()
    val = 0
    for char in range(len(name)):
        val += (ord(name[char]) - 96)
    return val

def value_names():
    f = open('p022_names.txt', 'r')
    lines = f.readlines()
    names = ''
    for line in lines:
        names += line
    names = names.split(',')
    names = [name.strip('"') for name in names]
    names = sorted(names)

    name_pos = 0
    n_value = 0
    for name in names:
        n_value += (name_pos+1)*name_value(name)
        name_pos += 1
    print n_value

print value_names()


