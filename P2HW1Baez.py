"""
CTI 110
BaezS
P2HW1 - travel expense
9/28/2023

"""


print("what is your budget?", end="")
budget = int(input())
print("where are you going?", end="")
location = input()
print("how much on gas?", end="")
gas = int(input())
print("how much for accomodations/hotel?", end="")
accomodations = int(input())
print("how much on food?", end="")
food = int(input())
expense = gas + accomodations + food

print("-"*10,"travel expenses","-"*10)
print("location:\t\t", location)
print("budget:\t\t ", "$",budget)
print("fuel:\t\t ", "$",gas)
print("accomodation: ", "$",accomodations)
print("food:\t\t ", "$",food)
print("-"*37)
print("remaining balance: ", budget - expense)
