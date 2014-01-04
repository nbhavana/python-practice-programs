"""
Program to calculate Fibonacci sequence for the given number

"""


print("Enter the limit for the Fibonacci Sequence:")
n = int(raw_input())
 
print "First %d numbers of Fibonacci series are :-\n" %n

first = 0
second = 1

for i in range(1,n+1):

   # if i <= 1:
    #    next = i
        
    #else:        
    next = first + second
    first = second
    second = next
        
    print next
    


