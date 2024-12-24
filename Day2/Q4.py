#4).Write a function find_longest_word() that takes a list of words and returns the length of the longest one.


list = []
n = (int(input("Enter the number of elements :  ")))
for i in range(n):
    element = input(f"Enter the value {i+1} :  ")
    list.append(element)

print(f"list = {list}")

def find_max_word(list):
    maxl = len(list[0])

    for  word in list:
        if(len(word)> maxl):
            maxl = len(word)
            temp = word
    
    print(f"Word with max length is : {temp}, length of max word is :{maxl}")
    
find_max_word(list)

