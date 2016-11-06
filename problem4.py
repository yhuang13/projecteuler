def is_palindrome(num):
    return str(num) == str(num)[::-1]

# palindrome_list = []
# while min_num <= max_num:
#     if is_palindrome(min_num):
#         palindrome_list.append(min_num)
#     min_num += 1
# print palindrome_list

multiples = []
for x in range(100,1000):
    for y in range(100,1000):
        multiples.append(x*y)


multiples = sorted(multiples)
for x in range(len(multiples) - 1, 0, -1):
    if is_palindrome(multiples[x]):
        print multiples[x]
        break