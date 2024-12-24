#3) Find and display the largest number of a list without using built-in function max(). Your program should
#ask the user to input values in list from keyboard.

list = []
n = (int(input("Enter the number of elements :  ")))
for i in range(n):
    element = input(f"Enter the value {i+1} :  ")
    list.append(element)

print(f"list = {list}")

def find_max(list):
    max_val = list[0]
    for n in list:
        if n > max_val:
            max_val = n
    return max_val

print(f"Max num = {find_max(list)}")

