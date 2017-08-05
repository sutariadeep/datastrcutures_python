#word
#dowr
#doar

import collections

def isSameString(string1, string2):
    list_string1, list_string2 = list(string1), list(string2)
    if len(string1) != len(string2):
        return False
    #Create dictionary named count to handle the number of inputs
    counts = collections.defaultdict(int)    
    for letter in list_string1:
        counts[letter] += 1
    for letter in list_string2:
        counts[letter] -= 1
        if counts[letter] < 0:
            return False
    return True
    
print isSameString('aabb','bbaa')
print isSameString('aabb','acba')
print isSameString('1234','4123')
print isSameString(' ','')    
    