"""
CTI 110
P3T2 - Choices and Menus
Baezs
9/26/2023
"""
import random
# the most simple program, with main()
def main():
  #print menu
  print("-"*10, "main menu", "-"*10)
  print("1. Option one")
  print("2. Option two")
  print("3. Option three")
  
  #let the user choose
  print("your choice?", end="")
  choice = int(input())
  print("you chose:", choice)

  # branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print("sorry, that's not an option.")
  
  
def option_1():
    print("Ordering lunch")
    print("would you like a burger or a salad?")
    food = input()
    if food == "burger":
      print("one burger, coming up")
    elif food == "salad":
      print("dressing on the side")
    else:
      print("we dont have any", food)
  
def option_2():
    print("Going outside")
    print("where do you want to go?")
    location = input()
    if location == "park":
      print("get the leash for the dog, were going to the park")
    elif location == "McDonalds":
      print("how do we go to McDonalds?", end="")
      transportation = input()
      print("were going to McDonalds by:", transportation)
      if transportation == "car":
        print("get the keys")
      elif transportation == "walking":
        print("I dont want to walk!")
      else:
        print("im not doing that, ill just order it.")
    else:
      print("im not doing all that")
      
def option_3():
  worlds = ["one piece", "attack on titan"]
  world = random.choice(worlds)
  print("CONGRATULATIONS, you have been transported to a new world")
  print("you have been transported to:", world)
  
  
  # start the program
main()
