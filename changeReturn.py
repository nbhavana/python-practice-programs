
"""
The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change.
The user have to enter the price of an item and the amount of money given
"""

def calculateChange(change_to_return):

    
    ones=change_to_return/100
    change_after_ones = change_to_return % 100
    
    quarters=change_after_ones/25
    change_after_quarters = change_after_ones-(quarters*25)
    
    dimes=change_after_quarters/10
    change_after_dimes=change_after_quarters-(dimes*10)
    
    nickels=change_after_dimes/5
    change_after_nickels=change_after_dimes-(nickels*5)
    
    pennies=change_after_nickels
    
    return ones,quarters,dimes,nickels,pennies



if __name__=="__main__":
    
    price_of_item = int(float(raw_input("Enter the Total Amount:"))*100)
     
    amount_paid = int(float(raw_input("Enter the Amount Paid:"))*100)
    
    change_to_return = amount_paid - price_of_item
    change_to_print =  float(change_to_return)/100

    print "The Amount to be returned:%s" %change_to_print
    print "The Distribution of Money is:"

    ones,quarters,dimes,nickels,pennies = calculateChange(change_to_return)
    print "ones=%s,quarters=%s,dimes=%s,nickels=%s,pennies=%s" %(ones,quarters,dimes,nickels,pennies)

    
