"""
Program to convert binary number into decimal and vce versa

"""
def binaryToDecimal(binaryNum):
    decNum = 0
    j=1
    while(binaryNum !=0):
        remainder = binaryNum%10
        decNum=decNum+remainder*j
        j=j*2
        binaryNum = binaryNum/10
        
    print "Equivalent decimal number : %ld" %decNum
    

def decimalToBinary(decimalNum):
    binaryNum = ""
    while(decimalNum>0):
        binaryNum = str(decimalNum%2)+binaryNum
        decimalNum>>=1
    
    print "Equivalent Binary number: %s" %binaryNum
        

print "Usage:"
print "B - Convert Binary number to Decimal"
print "D - Convert Decimal number to Binary"
print "\nEnter your choice:"
choice = raw_input()

if (choice == 'B') | (choice =='b'):
    print "Enter any Binary number:"
    binaryNum  = long (input())
    binaryToDecimal(binaryNum)

elif (choice == 'D')|(choice == 'd'):
    print "Enter any Decimal number:"
    decimalNum = long (input())
    decimalToBinary(decimalNum)
    
else:
    print "You have entered wrong choice"
