import collections

def findMissingNumber1(array1, array2):
    array1.sort()
    array2.sort()
    for num1, num2 in zip(array1, array2):
        if num1!=num2:
            return num1
    return array1[-1]

def findMissingNumber2(array1, array2):
    d=collections.defaultdict(int)
    for num in array2:
        d[num]+=1
    for num in array1:
        if d[num]==0:
            return num
        else:
            d[num]-=1    

def findMissingNumber3(array1, array2):
    result=0
    for num in array1+array2:
        result^=num
    return result


a = [4,1,0,2,9,6,8,7,5,3]
b = [6,4,7,2,1,0,8,3,9]
print findMissingNumber1(a,b)
print findMissingNumber2(a,b)
print findMissingNumber3(a,b)