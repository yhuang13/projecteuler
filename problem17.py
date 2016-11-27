#f the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


num_name = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "onethousand"
}

def convert_num(num):
    global num_name
    if num < 20 or num == 1000:
        return num_name[num]
    elif num < 100:
        return num_name[(num/10)*10]+num_name[num%10]
    else:
        if (num % 100) == 0:
            return num_name[(num / 100)] + num_name[100]
        elif 10 < (num % 100) < 20:
            return num_name[(num / 100)] + num_name[100] + 'and' + num_name[(num % 100)]
        else:
            return num_name[(num/100)] + num_name[100] + 'and' + num_name[(((num)/10)%10)*10] + num_name[(num % 10)]



print [convert_num(x) for x in range(200,220)]

def len_num():
    return sum([len(convert_num(x)) for x in range(1,1001)])

print len_num()
