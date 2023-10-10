#cti 110
#P4T2 - time cards
#norris
#10/5/23

#get the users work info for the week
#find the pay
"""
#take 1: Use a list
hours = [8,8,8,7,9]
print("you worked:")
total_hours = sum(hours)
print(total_hours, "hours")
print("Longest shift was", max(hours), "hours")
print("Shortest shift was", min(hours), "hours")
#find the avg
average = total_hours / len(hours)
print("for an average of", average, "hours per shift.")
"""

#take 2: by hand
print("timecard program")
#set up variables
DAYS_OF_WEEK = 5 # constant
todays_hours = 0
total_hours = 0
#ask for time worked each day
#and take a running total
for day in range(DAYS_OF_WEEK):
  print("hours worked for day", day+1, end=":") # well print 1-5, not 0-4 
  todays_hours = float(input())
  #total_hours = total_hours + todays_hours
  total_hours += todays_hours #shortcut += operator
average = total_hours / DAYS_OF_WEEK
#print the total and average hours
print("total hours this week:", total_hours)
print("average shift time:", format(average,"0.2f"), "hours")