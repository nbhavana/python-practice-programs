"""
Program to reverse a string and print it out

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
    
    print "The reverse string is: %s" %newString
        
if __name__=="__main__":

    print "Enter the string that you need to reverse:"
    string = raw_input()
    
    reverseString(string)
