#5). Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******


def histo(arr):

    s = '\n'.join('*'*i for i in arr)
    return s

print(histo([4,9,7]))