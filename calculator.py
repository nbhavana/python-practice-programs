"""
Program to implement simple calculator to do basic operations
"""

if __name__=="__main__":


    print "Enter number for any of following operations:\n1-Addition \n2-Subtraction \n3-Multiplication \n4-Division"
    function = input()

    if function ==1:
        print "\nYou chose to perform Addition"
    if function ==2:
        print "\nYou chose to perform Subtraction"
    if function ==3:
        print "\nYou chose to perform Multiplication"
    if function ==4:
        print "\nYou chose to perform Division"

    print "Enter two numbers for your operation:\n"
    number1=input()
    number2=input()

    if function ==1:
        ans = number1 + number2
    if function ==2:
        ans = number1 - number2
    if function ==3:
        ans = number1 * number2
    if function ==4:
        ans = number1 / number2

    print "Answer = %f" %ans
