import math
# change the values of lower and upper for a different result


# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

#Reference https://www.programiz.com/python-programming/examples/prime-number-intervals

def prime_in_range(lower,upper):
    print("Prime numbers between",lower,"and",upper,"are:")

    for num in range(lower,upper + 1):
    #prime numbers are greater than 1
        if num > 1:
            for i in range(2,int(math.sqrt(num))):
                if (num % i) == 0:
                    break
            else:
                print(num),
    print        
prime_in_range(900,1000)

#Reference: http://www.geeksforgeeks.org/sieve-of-eratosthenes/
# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
 
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
    lis =[]
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print p,
 

n = 30
print "Following are the prime numbers smaller",
print "than or equal to", n
SieveOfEratosthenes(n)

#Reference:https://www.programiz.com/python-programming/examples/prime-number
# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,int(math.sqrt(num))):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

