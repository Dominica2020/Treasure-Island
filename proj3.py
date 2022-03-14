print('''
*********************************             
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
*********************************
''')
print(">>>>> Welcome to Treasure Island! <<<<<")
print("")
print("Your mission is to find the treasure.")
print("")

choice_1 = input("You're at a fork in the road. Where do you want to go?\nType \"left\" or \"right\".\n")

if choice_1.lower() == "left":
  choice_2 = input("You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
  if choice_2.lower() == "wait":
    choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice_3 == "yellow":
      print("YOU WIN!")
    elif choice_3 == "red":
      print("Bitten by a gang of komodo dragons.\nGAME OVER.")
    elif choice_3 == "blue":
      print("Sprayed by molten lava.\nGAME OVER.")
    else:
      print("No treasure for you.\nGAME OVER.")
  else:
    print("Attacked by mutated piranhas.\nGAME OVER.")  
else:
  print("Stuck in quicksand.\nGAME OVER.")
