#python program to calculate compound interest
principal_amount = float(input("Enter principal amount:"))
rate_of_interest = float(input("Enter rate of interest:"))
time_period = float(input("Enter time period in years:"))
compound_future = principal_amount*((1+rate_of_interest/100)**time_period)
compound_interest = compound_future-principal_amount
print("compound interest:%f" %compound_interest)
