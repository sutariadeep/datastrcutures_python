#Reference: http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/
#Prints redundant pairs [1,3] and [3,1]
def pairSum1(arr, k):
    if len(arr)<2:
        return
    arr.sort()
    left, right = (0, len(arr)-1)
    while left<right:
        currentSum=arr[left]+arr[right]
        if currentSum==k:
            print arr[left], arr[right]
            left+=1 #or right-=1
        elif currentSum<k:
            left+=1
        else:
            right-=1

#No redundant pairs. Avoids sorting 
def pairSum2(arr, k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    print '\n'.join( map(str, list(output)) )


#pairSum1([1,1,2,2,3,4],4)
#pairSum2([1,1,2,2,3,4],4)
pairSum2([1,1,2,2,3,4,-1,5],4)