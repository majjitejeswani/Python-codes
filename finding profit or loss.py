#program to find profit or loss
actual_cost = float(input("Enter actual cost:"))
sales_cost = float(input("Enter sales cost:"))
if (actual_cost > sales_cost):
    loss = actual_cost-sales_cost
    print("Loss %d" %loss)
elif (actual_cost < sales_cost):
    profit = sales_cost-actual_cost
    print("profit %d" %profit)
else:
    print("No loss No profit")
