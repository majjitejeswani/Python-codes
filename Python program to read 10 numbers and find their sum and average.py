#Python program to read 10 numbers and find their sum and average
sum = 0
print("Enter 10 numbers")
for i in range(1,11):
    num = int(input("Number %d:" %i))
    sum = sum + num
print("sum of first 10 numbers: %d" %sum)
average = sum/10
print("Average of first 10 numbers:%f" %average)
    
