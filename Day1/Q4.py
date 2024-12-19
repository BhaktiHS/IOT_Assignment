#4] Write a Python function to find the maximum of three numbers....c

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num1 : "))
num3 = int(input("Enter num1 : "))

if num1 > num2:
    if num1 > num3:
        print(f"num1 = {num1} is greatest")
    else:
        print(f"num3 = {num3} is greatest")
else:
    if num2 > num3:
        print(f"num2 = {num2} is greatest")
    else:
        print(f"num3 = {num3} is greatest")                