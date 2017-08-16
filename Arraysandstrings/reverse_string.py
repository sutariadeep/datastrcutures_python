def reverse_list(letters, first=0, last=None):
    "reverses the elements of a list in-place"
    if last is None:
        last = len(letters)
    last -= 1
    while first < last:
        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1

def reverse_words(string):
    """reverses the words in a string using a list, with each character
    as a list element"""
    characters = list(string)
    reverse_list(characters)
    first = last = 0
    while first < len(characters) and last < len(characters):
        if characters[last] != ' ':
            last += 1
            continue
        reverse_list(characters, first, last)
        last += 1
        first = last
    if first < last:
        reverse_list(characters, first, last=len(characters))
    return ''.join(characters)

print reverse_words("Deep is working hard")
    
