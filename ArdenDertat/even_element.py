import collections

def getEven1(arr):
    counts=collections.defaultdict(int)
    for num in arr:
        counts[num]+=1
    for num, count in counts.items():
        if count%2==0:
            return num


def getEven2(arr):
    return reduce(lambda x, y: x^y, arr+list(set(arr)))

arr = [2,1,3,1]
print getEven1(arr)
print getEven2(arr)