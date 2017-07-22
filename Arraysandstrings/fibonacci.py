#Reference https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
#Recursive method
def Fibonnacci1(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonnacci1(n-1)+Fibonnacci1(n-2)

#Iterative method. This is the fastest method by far
def Fibonnacci2(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a


## Example 3: Using generators
a,b = 0,1
def Fibonnacci3():
 global a,b
 while True:
  a,b = b, a+b
  yield a

##Prints the list of Fibonacci numbers
def Fibonnaccilist(n):
 a,b = 1,1
 for i in range(n-1):
  print a,
  a,b = b,a+b
 return a


print Fibonnacci1(10)
print Fibonnacci2(10)
f=Fibonnacci3()
for i in range(9):
	f.next()
print f.next()
print Fibonnaccilist(10)
