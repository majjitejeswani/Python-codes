#python program to print student grade
maths_marks = float(input("Enter maths marks:"))
physics_marks = float(input("Enter physics marks:"))
chemistry_marks = float(input("Enter chemistry marks:"))
telugu_marks = float(input("Enter telugu marks:"))
english_marks = float(input("Enter english marks:"))
total_marks = maths_marks + physics_marks + chemistry_marks + telugu_marks + english_marks
percentage = (total_marks/500) * 100
print("Total marks %.2f:" %total_marks)
print("Percentage %.2f" %percentage)
if(percentage>=90):
    print("A Grade")
elif(80 <= percentage < 90):
    print("B Grade")
elif(70 <= percentage < 80):
    print("C Grade")
elif(60 <= percentage < 70):
    print("D Grade")
else:
    print("Fail")
