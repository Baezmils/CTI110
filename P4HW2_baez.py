"""
CTI-110
P4HW2 - Salaries
BaezS
10/13/2023
"""
list = []
done = "done"
keep_going = True
overtime = 0
overtime_pay = 0
reg_pay = 0
gross = 0
num_employees = 0
total_overtime_pay = 0
total_reg_pay = 0
total_gross = 0
while keep_going:
  print('enter employees name or "done" to terminate : ', end='')
  names = input()
  
  
  if names == done:
    keep_going = False # we're done
    
  else:
    # process the employee
    num_employees += 1
    print("number of hours worked? ")
    hours_worked = int(input())
    print("pay rate? ")
    Pay_rate = int(input())
    
    overtime = hours_worked - 40 if hours_worked > 40 else 0
    reg_pay = hours_worked * Pay_rate
    total_reg_pay += reg_pay
    
    overtime_pay = overtime * 26.25
    total_overtime_pay += overtime_pay
    gross = reg_pay + overtime_pay 
    total_gross += gross
    
    print("-"*20)
    print("employee name: ", names)
    print()
    print("""Hours worked  Pay rate  Overtime  overtime pay  RegHour pay  gross pay""")
    print("-"*50)
    print("\t", hours_worked, "\t\t",Pay_rate,"\t",overtime,"\t","\t", overtime_pay,"\t\t", reg_pay,"\t\t", gross)


# done with entering employees
print("number of employees: ", num_employees)
print("Total amount paid for overtime: ", total_overtime_pay)
print("Total amount paid for regular hours: ", total_reg_pay)
print("Total amount paid for gross: ", total_gross)

