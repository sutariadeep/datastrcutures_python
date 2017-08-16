def permutations1(word):
    if len(word) ==1:
        return [word]
 
    #get all permutations of length N-1
    perms=permutations1(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result

# Python program to print all permutations with
# duplicates allowed using recursion
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permutaions2(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permutaions2(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
print permutations1('abc')
string = "ABC"
n = len(string)
a = list(string)
permutaions2(a, 0, n-1)
