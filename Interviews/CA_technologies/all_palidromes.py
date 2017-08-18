#Part 1: A palindrome is a sequence of characters that is the same backwards or forward. 
#Write a function that tests a string passed in for whether it is a palindrome or not.
#Test strings: aa, aba, zboba, zamanaplanacanalpanamaxbobx

#Part 2: Write a function that finds and returns all the palindrome(s) in a string.
#'momyyydad' -> ['mom', 'yy', 'yyy', 'dad']


#print "Hello"

def isPalindrome(string):
    return string == string[::-1]


def all_palindromes1(string):
    left, right = 0, len(string)
    i = right
    results = []
    
    while left < right-1:
        temp = string[left:i]
        i -= 1
        
        if isPalindrome(temp):
            results.append(temp)
        
        if i < left+2:
            left += 1
            i = right
            
    return list(set(results))

def all_palindromes2(text):
    """Return list with all palindrome strings within text.

    The base of this algorithm is to start with a given character,
    and then see if the surrounding characters are equal. If they
    are equal then it's a palindrome and is added to results set,
    extend to check if the next character on either side is equal, 
    adding to set if equal, and breaking out of loop if not.

    This needs to be repeated twice, once for palindromes of 
    odd lengths, and once for palindromes of an even length."""

    results = set()
    text_length = len(text)
    for idx, char in enumerate(text):

        # Check for longest odd palindrome(s)
        start, end = idx - 1, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = idx, idx + 1
        while start >= 0 and end < text_length and text[start] == text[end]:
            results.add(text[start:end+1])
            start -= 1
            end += 1

    return list(results)

# print isPalindrome('aa')
# print isPalindrome('aba')
# print isPalindrome('zboba')
# print isPalindrome('zamanaplanacanalpanamaxbobx')
print all_palindromes1('momyyydad')
print all_palindromes2('momyyydad')
