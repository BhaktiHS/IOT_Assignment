#7) Using for loop, write and run a Python program to find factorial from 0 to 10....c

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

for num in range(0, 11):
    print(f"{num}! = {factorial(num)}")
