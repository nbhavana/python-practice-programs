"""
Find prime factors of a given number and print them

"""
import math
def prime_factor(number):
    listOfFactors = []
    i = 2
    while i<=number:
        if number%i==0:
            number/=i
            listOfFactors.append(i)
        else:
            i+=1
    return listOfFactors
           

if __name__ =="__main__":

    print "Enter a number:"
    number = int(raw_input())
    print "Prime factors are:"
    print prime_factor(number)
    
