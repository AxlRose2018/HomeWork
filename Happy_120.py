
# asks the user to type his name and age which are string and integer
name = input("Please Enter Your Name:")
age = int(input("Please Enter Your Age:"))

# next function  used to calculate the year you'll turn 120, using the "datetime" module
def YearsCalc():

    import datetime
    now = datetime.datetime.now()
    newage = (120-age)+now.year
    return newage

print("Hi",name,"You shall reach the age of 120 in the Year of:",YearsCalc())

