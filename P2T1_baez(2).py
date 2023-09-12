import matplotlib.pyplot as plt

# collect data
data=[] #empty list


"""
print("enter pokemon data")
print("day 1:", end="")
day1 = int(input())
print("day 2:", end="")
day2 = int(input())
print("day 3:", end="")
day3 = int(input())
"""
# new version
num_days =  int(input("how many days? "))
for day in range(num_days):
  print("day ", day, ":", end="")
  today = int(input())
  data.append(today) #add it to the end of the list

# put the data in a list(DONE)


# TODO: graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("pokemon data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()
