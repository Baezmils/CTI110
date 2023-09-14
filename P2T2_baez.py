import matplotlib.pyplot as plt
import turtle 

# collect data
data=[] #empty list
# new version - loop and get each day at a time
#num_days = int(input("how many days?))
num_days = turtle.numinput("input","how many days? ")
num_days = int(num_days)
for day in range(num_days):
  #print("day ", day, ":", end="")
  #today = int(input())
  label = "day#" + str(day) # "day 1" and so on
  today = turtle.numinput(label, "how many pokemon?")
  data.append(today) #add it to the end of the list

# put the data in a list(DONE)
# print min and max
print()
print("best day:", max(data))
print("worst day:", min(data))
# TODO: total and average
total = 0
for num in data:
  total += num
  # total is now all the numbers in data, added up
average = total / num_days
print("total:", total)
print("average:", average)

# graph the data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("pokemon data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()

