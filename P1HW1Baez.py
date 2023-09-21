
"""
CTI 110
P1HW1 - variables
BaezS
9/5/23

do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them

"""
#PART ONE: MATH
# variables. first and second
first = 0
second = 0

print("enter interger:")
first = int(input()) # take input, then convert it to int
print(first, "squared is", first * first )
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("enter another interger")
second = int(input())
#print("first + second =", first + second)
print(first, "+", second, "=", first + second)
#print("first * second =", first * second)
print(first, "*", second, "=", first * second)


#PART TWO: MOVIES
#three variables
#int - the year of the movie
#float - the gross (in million dollars)
#finally, print a quote from the movie
name = "bullet train"
year = 2022
gross = 239.26 # mil $
quote = "Yeah. Have you tried these smart toilets? Theyre a pleasure to the senses."

# print out this information
# then print a movie quote
print()
print("movie:")
print(name)
print("year of release:", year)
print("gross:", gross,"million")
print("quote:", quote)


