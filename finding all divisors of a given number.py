#python program to find all the divisors of a given number
num = int(input("Enter a integer:"))
for i in range(1,num+1):
    if(num%i==0):
        print(i)
