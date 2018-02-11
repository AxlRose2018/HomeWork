# we have a given array of numbers, we must create a function for sum of the arrays objects

# here I create the list of numbers
list = [4, 2, 7, 8, 9, 10, 2, 8, 6]

#here I have created the function which sums the list named "listsum"
def listsum():
# "sum" is going to get and save all the added numbers so for starters it was set to 0
    sum = 0
# the for loop is created and "i" stands for the index of numbers on the list
# and then sum gets the value of the current index cell plus the current sum and finally returns the value
    for i in list:
        sum = sum + i
    return sum

# the next print shows the final value of the listsum function
print("The Sum of the list is:",listsum())

# the listavg function calculate and returns the average of the list above using avg
def listavg():
    avg = listsum() / len(list)
    return avg

print ("The Average of the list is:",listavg())
