"""
Program to find if the string entered is a palidrome or not

"""

def reverseString(string):
    revString = []
    i= len(string)-1
    while i>=0:
            revString.append(string[i])
            i-=1
            
    newString = ""
    
    for i in range(len(revString)):
        newString = newString + str(revString[i])
        
        
    if string == newString:
        print "The string you entered is palindrome"
    else:
        print "The string you entered is not palindrome"
        
if __name__=="__main__":

    print "Enter the string :"
    string = raw_input()
    
    reverseString(string)
