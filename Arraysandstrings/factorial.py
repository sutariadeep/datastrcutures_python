#Please refer to this link in case you are interested
#https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

#Recursion way
def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)


#Iterative way
def factorial2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

#Pythonic way
import math
print math.factorial(10)    


print factorial1(10)
print factorial2(10)