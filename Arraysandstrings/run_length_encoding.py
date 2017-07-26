#http://rosettacode.org/wiki/Run-length_encoding#Python
def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character,count)
    lst.append(entry)
    return lst
 
def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
 
#Method call
print encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
print decode([('a', 5), ('h', 6), ('m', 7), ('u', 1), ('i', 7), ('a', 6)])
