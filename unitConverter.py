"""
Program to convert various units between one another.
The user enters the type of unit being
entered, the type of unit they want to convert to and
then the value.
This program converts following units:
Temperature: Fahrenheit to Degree Celcius and vice versa
Volume: cubic feet to cubic meter and vice versa
Currency: USD to INR and vice versa
Mass: pound to kg and vice versa
"""

if __name__=="__main__":
    
    print "This program converts following units:\n"
    print "Temperature: Fahrenheit to Degree Celcius and vice versa"
    print "Volume: cubic feet to cubic meter and vice versa"
    print "Currency: USD to INR and vice versa\nMass: pounds to kg and vice versa\n"
    print "Usage: \nEnter 1 for Temperature\nEnter 2 for Volume\nEnter 3 for Currency\nEnter 4 for Mass\n"
    
    print "Choose the type of unit you need to convert:\n"
    unitType = input()
    print "You chose %d to convert" %unitType

    if unitType == 1:
        
        print "Usage:\nEnter 'F' to convert Fahrenheit to degree celcius\n"
        print "Enter'C' to convert degree celcuis to Farenheit\n"
        print "Enter your choice and value to convert:\n"
        
        temp = raw_input()
        value = float(input())
               
        if (temp == 'F')| (temp == 'f'):
            C = (value -32)*5/9
            print "%f degree Celcius" %C
        elif (temp == 'C')|(temp == 'c'):
            F = value * 9/5 +32
            print "%f degree Fahrenheit" %F  
        else:
            print "You entered wrong value !"

    if unitType == 2:
        
        print "Usage:\nEnter 'P' to convert kg into pounds\n"
        print "Enter 'K' to convert pounds to kg\n"
        print "Enter your choice and value to convert:\n"
        
        mass = raw_input() 
        value = float(input())
        
        if ( mass == 'P')| (mass == 'p'):
            P = value*2.2046
            print "%f pounds" %P
        elif (mass == 'K')|(mass == 'k'):
            K = value/2.2046
            print "%f kg" %K  
        else:
            print "You entered wrong value !"


    if unitType == 3:
        
        print "Usage:\nEnter 'D' to convert INR into Dollar\n"
        print "Enter 'I' to convert Dollars to INR\n"
        print "Enter your choice and value to convert:\n"
        
        currency = raw_input() 
        value = float(input())
        
        if ( currency == 'D')| (currency == 'd'):
            D = value/61.2839
            print "%f $" %D
        elif (currency == 'I')|(currency == 'i'):
            I = value*61.2839
            print "%f Rs" %I 
        else:
            print "You entered wrong value !"


    if unitType == 4:
        
        print "Usage:\nEnter 'F' to convert cubic meter into cubic feet\n"
        print "Enter 'M' to convert cubic feet into cubic meter\n"
        print "Enter your choice and value to convert:\n"
        
        volume = raw_input() 
        value = float(input())
        
        if ( volume == 'F')| (volume == 'f'):
            F = value*35.315
            print "%f cubic feet" %F
        elif (volume == 'M')|(volume == 'm'):
            M = value/35.315
            print "%f cubic meter" %M 
        else:
            print "You entered wrong value !"















