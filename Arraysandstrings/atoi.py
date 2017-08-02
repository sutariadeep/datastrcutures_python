# Python program for implementation of atoi
 
# A simple atoi() function
def myAtoi(string):
    res = 0
 
    # Iterate through all characters of input string and 
    # update result
    for i in xrange(len(string)):
        res = res*10 + (ord(string[i]) - ord('0'))
 
    return res
 
# Driver program
string = "89789"
print myAtoi(string)
 
# This code is contributed by BHAVYA JAIN
