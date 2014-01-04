

import random
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
    
    #price_of_item=int(float(raw_input("Enter the Total Amount:"))*100)
     
    #amount_paid=int(float(raw_input("Enter the Amount Paid:"))*100)
    print "Welcome"
    n=100
    counter1 =0
    counter2 =0
    while n>0 :
        print "in while loop"
        price_of_item = int(random.uniform(1,10)*100)
        amount_paid = random.randint(10,15)*100
        change_to_return = amount_paid - price_of_item
        change_to_print =  float(change_to_return)/100

        print "price of item:%s" %price_of_item
        print "amount paid:%s" %amount_paid
        print "The Amount to be returned:%s" %change_to_return
        print "The Distribution of Money is:"

        ones,quarters,dimes,nickels,pennies = calculateChange(change_to_return)
        print "ones=%s,quarters=%s,dimes=%s,nickels=%s,pennies=%s" %(ones,quarters,dimes,nickels,pennies)

        amount_to_return = ones*100 + quarters*25 + dimes*10 + nickels*5 + pennies*1
        print "amount_to_return =%s" %amount_to_return

        
        if amount_to_return == change_to_return:
            #print "Program Worked !!!"
            counter1+=1
        else:
            #print "Program Failed !!!"
            counter2+=1
     
        n-=1

        print "counter1 :%s" %counter1
        print "counter2 :%s" %counter2
