##5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of 
# subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F....completed

Marathi = int(input("Enter marks for Marathi : "))
English = int(input("Enter marks for English : "))
Hindi = int(input("Enter marks for Hindi : "))

avrg = (Marathi + English + Hindi)/3

print("Marks are as below")
print(f"Marathi = {Marathi}, Engish = {English}, Hindi = {Hindi}")
print(f"Average is {avrg}")

if (avrg<100) and (avrg>90):
    print("Grade is A")
elif (avrg>80) and (avrg<89):
    print("Grade is B")
elif (avrg>70) and (avrg<79):
    print("Grade is C")  
elif (avrg>60) and (avrg<69):
    print("Grade is D")
else:
    print("Grade if F")              