"""
CTI 110
P4T3 - three loops
baezs
10/10/23

"""
# write three loops
# 1. for loop
# 2. while loops
# 3. while with sentinel
# for each of these, do the following
# ask the user how many cars they saw today
# find the total and the average
MAX_DAYS = 5
day = 1
cars_today = 0
cars_total = 0
average = 0
# 1 - for the loop
for day in range(1, MAX_DAYS+1):
  print("day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
# print the total
print("total cars =", cars_total)
average = cars_total / MAX_DAYS
print("average per day  =", average)

# 2 - while loop
day = 1
cars_today = 0
cars_total = 0
print()
print("enter how many cars you saw each day")
while day <= MAX_DAYS:
  print("day #", day, end=": ")
  cars_today = int(input())
  cars_total = cars_total + cars_today
  day = day + 1
print("total # of cars seen: " , cars_total)
average = cars_total / MAX_DAYS
print("average per day =", average)

# take 3 - "sentinel"
cars_total = 0
print("\n\nEnter -1 to finish")
DONE_VALUE = -1 # if they type this, finish
# go until they say to stop wiht DONE_VALUE
keep_going = True
days = 0
while keep_going:
  print("cars seen today:", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    # exit
    keep_going = False
  else:
    # add the value to total
    cars_total = cars_total + cars_today
    days = days + 1
print("total cars =", cars_total)
print("over", days, "days")
average = cars_total / days
print("average = ", average)