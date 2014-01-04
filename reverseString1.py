"""
Program to reverse a string and print it out.

"""



def string_reverse(string):
    
    return string[::-1]

print "Enter s string that you want to reverse:"
string = raw_input()

print "\nYou have entered the string:%s" %string

print "\nThe reverse of the string you entered is: %s" %string_reverse(string)
