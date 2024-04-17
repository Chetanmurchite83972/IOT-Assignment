# The marks obtained by a student in 3 different subjects are input by the user. 
# Your program should calculate the average of subjects and display the grade. 
# The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

num1 = float(input("Enter Maths mark: "))
num2 = float(input("Enter Science mark: "))
num3 = float(input("Enter English mark: "))

num4 = (num1 + num2 + num3)/3

if  90 <= num4:
    print("A Grade")

elif  80 <= num4:
    print("B Grade")

elif  70 <= num4:
    print("C Grade")    

elif  60 <= num4:
    print("D Grade")    

else :
    print("F Grade")