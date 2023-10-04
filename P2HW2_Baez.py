"""
CTI 110 
BaezS
P2HW2 - List
9/28/2023

"""
data = []
num_modules = int(input("input, how many modules? "))
for module in range(num_modules):
  module_name = "module#" + str(module)
  print(module_name)
  grade = int(input("what are the grades?"))
  data.append(grade)
total = 0
for num in data:
  total += num 
average = sum(data) / num_modules
print("-"*10, "Results","-"*10)
print("Lowest grade:", min(data))
print("highest grade:", max(data))
print("sum of grades:", sum(data))
print("average:", average)
print("-"*30)

