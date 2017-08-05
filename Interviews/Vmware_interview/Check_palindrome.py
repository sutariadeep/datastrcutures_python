#Check if the string can be a palindrome. String can be out of order
# acb

def isPalindrome(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char,0) + 1
    odd_count = 0
    
    for count in counter.values():
        odd_count += count % 2
    return odd_count in [0,1]
    
print isPalindrome('aacc')
print isPalindrome('ca')