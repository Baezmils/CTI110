"""
CTI-110
P3HW2 - Salary
BaezS
10/4/2023
"""
print("what is your name? ")
name = input()
print("number of hours worked? ")
hours_worked = int(input())
print("pay rate? ")
Pay_rate = int(input())

if hours_worked > 40:
  overtime = hours_worked - 40
else:
  overtime = 0
reg_pay = hours_worked * Pay_rate

overtime_pay = overtime * 26.25
gross = reg_pay + overtime_pay 

print("-"*20)
print("employee name: ", name)
print()
print("""Hours worked  Pay rate  Overtime  overtime pay  RegHour pay  gross pay""")
print("-"*80)
print("\t", hours_worked, "\t\t",Pay_rate,"\t",overtime,"\t","\t", overtime_pay,"\t\t", reg_pay,"\t\t", gross)