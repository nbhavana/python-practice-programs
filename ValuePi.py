
"""
Find the value Pi to the Nth Digit - Enter a number and the program will
generate a value of PI up to that many decimal places.

"""

pi=list()

def generatePi(n):
    quotient=22
    divisor=7
    i=1
    flag=0
    while i<n: 
        if quotient / divisor != 0:
            remainder = quotient % divisor
            pi.append(quotient / divisor)
        else:
            if flag==0:
                flag=i
                i=0
            remainder =(quotient * 10)%divisor
            pi.append((quotient * 10)/divisor)
        i+=1
        quotient = remainder
    valueOfPi = ""
    for i in range(len(pi)):
        if i+1==flag:
            valueOfPi = valueOfPi + "." + str(pi[i])
        else: 
            valueOfPi = valueOfPi + str(pi[i])
    print valueOfPi
    return


if __name__=="__main__":
    
    print "Enter the value for the limit of decimal digits for  PI:"
    n=int(raw_input())
    generatePi(n)

    
