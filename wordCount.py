"""
Program to count number of words in a string

"""

if __name__=="__main__":

    print "Enter a string:"
    string=raw_input()
    word =[]
    word = string.split(' ')
    numOfWords = len(word)
    print "number of words in a string:%d" %numOfWords
