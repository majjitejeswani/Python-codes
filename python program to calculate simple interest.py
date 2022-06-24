#python program to calculate simple interest
principal_amount = float(input("Enter amount:"))
rate_of_interest = float(input("Enter rate of interest:"))
time_period = float(input("Enter time period in years:"))
simple_interest = (principal_amount*rate_of_interest*time_period)/100
print("simple interest %.2f:" %simple_interest)
