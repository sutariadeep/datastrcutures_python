#To check for a string 
def palindrome1(num):
    return num == num[::-1]

#To check for a number
def palindrome2(num):
    n = num
    newnum=0
    while n>0:
        newnum = newnum*10 + n % 10
        n//=10
    return newnum == num


print palindrome1('1221')
print palindrome1('deep')
print palindrome1('acbca')
print palindrome2(121)

#Recursive check for palindrome of a number
def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n // 10, partial * 10 + n % 10)

trial = 123454321    
if ReverseNumber(trial) == trial:
    print("It's a Palindrome!")