# 2] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
# ut should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639
#pending

num = int(input("Enter 4 digit number : "))
th_place = num//1000
h_place = (th_place//100)
t_place = (h_place//10)
u_place = (num%1000)
