"""
Program to calculate the monthly payments of a fixed term
mortgage over given Nth terms at a given interest rate

"""


principal_amount = int(raw_input("Enter Principal Amount:"))
annual_interest = float(raw_input("Enter Annual Interest Rate:")) 
loan_term = int(raw_input("Enter Loan Term:"))

monthly_interest = (float)(annual_interest/100)/12

number_of_payments = loan_term * 12

mortgage_payment = (principal_amount * monthly_interest)/( 1-(1+monthly_interest)**-number_of_payments)

#print "Principal Amount = %d" %principal_amount
#print "Interest Rate = %f" %annual_interest
#print "Loan Term = %d" %loan_term

print "\nYour mortgage payment per month is %f $" %mortgage_payment 

 
