# CTI 110
# P5LAB1 - CYOA
# name
# date
# Feel free to fork this REPL and make changes.

# first function: main_menu().
import time

def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        # Call choice 2 here (You can add the corresponding function)
      choice_back_door()
    elif choice == '3':
        # Call choice 3 here (You can add the corresponding function)
      choice_go_home()
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        choice_go_home()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("you died")

def choice_go_home():
  print("to go home you must challenge yugi in a duel!")
  duel()

def duel():
  print("you have been given a branded despia deck to duel yugi!")
  branded_despia()
  yugis_turn()
  
def branded_despia():
  print("youre the challenger so you are going first!")
  starting_hand()

def starting_hand():
  print()
  print("your starting hand is: ")
  print()
  print("aluber of despia, fallen of albaz, maxx C, branded fusion, and PSY-framegear gamma")
  print()
  print("what do you do?")
  print("1. summon aluber of despia")
  print("2. summon fallen of albaz")
  print("3. activate maxx c")  
  print("4. activate branded fusion")
  print("5. you cannot do anything with PSY-framegear gamma unless responding to a monster effect")
  choice = input()
  #summon = input()
  your_turn = True
  while your_turn:
    if choice == "summon aluber of despia": 
      summon = input("summon face up or in face down defense position?")
      if summon == "summon face up":
        print()
        print("you summon aluber of despia in face up attack position!")
        print()
        time.sleep(1)
        print("aluber activates its effect to add a despia card from your deck!")
        print()
        time.sleep(1)
        print("yugi activates infinite impermanence to negate aluber of despia!")
        your_turn = False
      elif summon == "summon face down":
        print("you summon aluber of despia in face down defence position and pass the turn!")
        time.sleep(1)
        your_turn = False
      
    
    elif choice == "summon fallen of albaz":
      summon = input("summon face up or in face down defense position?")
      if summon == "summon face up":
        print("you summon fallen of albaz in face up attack position!")
        time.sleep(1)
        your_turn = False
      elif summon == "summon face down":
        print("you summon fallen of albaz in face down defence position and pass the turn!")
        time.sleep(1)
        your_turn = False
        your_turn = False
    
    elif choice == "activate maxx c":
      print("maxx C activates its effect!")
      print()
      time.sleep(1)
      print("nothing happens...")
      time.sleep(1)
      your_turn = False
    
    elif choice == "activate branded fusion":
      print("you activate branded fusion!")
      time.sleep(1)
      print()
      print("yugi activates ash blossom and joyous spring, negating branded fusion!")
      time.sleep(1)
      your_turn = False
    
    else:
      print("you must use what is available in your hand!")
      starting_hand()
  

def yugis_turn():
  print()
  print("*" * 10, "its now yugis turn!", "*" * 10)
  time.sleep(2)
  print()
  print("yugi special summons SSGSS GOKU from his deck allowing him to draw his entire deck!")
  time.sleep(2)
  print()
  print("yugi drew all five pieces of exodia!")
  time.sleep(2)
  print()
  print("EXODIA OBLITERATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  time.sleep(2)
  print()
  choice_back_door()
# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print()
    print("Thanks for playing!")

#start the program
main()
