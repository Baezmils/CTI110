# CTI 110
# P5HW1 - math quiz
# baezs
# 12/5/23
import random

def main_menu():
  print("welcome to the math quiz")
  print("")
  print("MAIN MENU")
  print("-"*20)
  print("1. Adding random numbers")
  print("2. Subtracting random numbers")
  print("3. Exit")
  print("")
  print("please choose one of the menu options:", end=" ")
  choice = input()
  if choice == '1':
    add_quiz()
  elif choice == '2':
    sub_quiz()
  elif choice == '3':
    exit()
  else:
    print("invalid choice")
    main_menu()


def generate_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_quiz():
    
    num1, num2 = generate_random_numbers()
    total = num1 + num2
    print(f"\t{num1} \n+\t{num2}\n")
   #AN - Example
    try:
      user_input = int(input())
    except ValueError:
      print("That isn't a number")
      user_input = 0
      
    while user_input != total:
    
      if user_input > total:
        print("your answer is too high")
        print("try again: ", end="")
        user_input = int(input())
      elif user_input < total:
        print("your answer is too low")
        print("try again:", end="")
        user_input = int(input())
          
      
    if user_input == total:
        print("congratulations!!! your answer is correct.")
        print()
        main_menu()
def sub_quiz():

  num1, num2 = generate_random_numbers()
  total = num1 - num2
  print(f"\t{num1} \n-\t{num2}\n")
  # AN - Example
  try:
    user_input = int(input())
  except ValueError:
    print("That isn't a number")
    user_input = 0
  while user_input != total:

      if user_input > total:
        print("your answer is too high")
        print("try again: ", end="")
        user_input = int(input())
      elif user_input < total:
        print("your answer is too low")
        print("try again:", end="")
        user_input = int(input())
      
      
  if user_input == total:
      print("congratulations!!! your answer is correct.")
      print()
      main_menu()
  
main_menu()
