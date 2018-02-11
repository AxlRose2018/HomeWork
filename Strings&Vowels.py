# Enter a string value to string
string = ("Masters of the Universe")

# created a function that counts the vowels in a string
def vowelscounter():
    #defined a counter for the iteration
    count = 0
    # the function will run on every cell and check it for vowel, if true 1 shall be added to the count
    for i in string:
       if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
         count +=1
     #when the roll is finished the function will return the final count
    return count

print("The Number of Vowels in","**",string,"**","is:",vowelscounter())
