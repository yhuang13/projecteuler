#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

num0 = 1
num1 = 2
numsum = num0 + num1
evensum = num1
maxnum = 4000000

while numsum < maxnum:
    num0 = num1
    num1 = numsum
    numsum += num0
    if numsum % 2 == 0:
        evensum += numsum

print evensum


#4613732
