# Hello, this is my solution to the test question. The data sets are inserted by me for clarity. 
#I tried a lot working with the google-api. But due to lack of time not able to dig deep in to the problem
#I am using two heaps here maxHeap and mimHeap to track the in coming stream. The insert() function gets the stream and puts the 
#values in Maxheap and Minheap. The median is the middle element in case of odd number of elements and average of two elements in case of 
# even number of elements. The mean of the data entered in the two functions is found out by summing the two heaps and getting the absolute value from it 
# then dividing by number of elemnts in the heaps

# Thank you
import heapq

class streamMedian:
    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        self.N=0
 
    def insert(self, num):
        if self.N%2==0:
            heapq.heappush(self.maxHeap, -1*num)
            self.N+=1
            if len(self.minHeap)==0:
                return
            if -1*self.maxHeap[0]>self.minHeap[0]:
                toMin=-1*heapq.heappop(self.maxHeap)
                toMax=heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1*toMax)
                heapq.heappush(self.minHeap, toMin)
        else:
            toMin=-1*heapq.heappushpop(self.maxHeap, -1*num)
            heapq.heappush(self.minHeap, toMin)
            self.N+=1
 
    def getMedian(self):
        if self.N%2==0:
            return (-1*self.maxHeap[0]+self.minHeap[0])/2.0
        else:
            return -1*self.maxHeap[0]

    def getMean(self):
        return (abs(sum(self.maxHeap)) + sum(self.minHeap))/self.N

test = streamMedian()
test.insert(1)
test.insert(2)
test.insert(3)
print "Median at this stage is:"
print "***********************"
print test.getMedian()
print "Mean at this stage is:"
print "***********************"
print test.getMean()
test.insert(4)
print "Median at this stage is:"
print "***********************"
print test.getMedian()
test.insert(9)
print "Median at this stage is:"
print "***********************"
print test.getMedian()
print "Mean at this stage is:"
print "***********************"
print test.getMean()
