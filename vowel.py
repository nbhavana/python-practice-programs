"""

Program to count number of vowels in the text
and report sum of each vowel in the string

"""

if __name__=="__main__":

    print "Enter a string:"
    string = raw_input()
    
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    counter=0
    for i in range(0,len(string)):
        
        if string[i] in vowels:
            counter= counter+1
            
    print "Number of vowels:%d" %counter
    
