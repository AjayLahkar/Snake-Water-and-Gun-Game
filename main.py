         # --- Exercise 5 ---
          # Snake Water And Gun

# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a Snake, Water or a Gun. The Gun Beats The Snake, The Water Beats The Gun and The Snake Beats The Water.
# Write a python programme to create a Snake, Water and Gun Game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

      # [S W G]
      # [0 1 2]
  # S 0 |D W L|
  # W 1 |L D W|
  # G 2 |W L D|


import random

def gamewin(u):
    ch = 0;

    values = ["snake","water","gun"];
    while(ch != 10):
      u = input("choose between snake , water and gun :- ")
      c = values[random.randint(0, 2)];
    
      if (c == "snake" and u == "gun"):
        print("Yah..! You win")
        break;
      elif (c == "snake" and u == "water"):
        print("computer win")
    
      elif (c == "snake" and u == "snake"):
        print("Oooho..! Game Draw")
    
      elif (c == "water" and u == "water"):
        print("Oooho..! Game Draw")
    
      elif (c == "water" and u == "gun"):
        print("computer win")
    
      elif (c == "water" and u == "snake"):
        print("Yah..! You win")
        break;
        
      elif (c == "gun" and u == "snake"):
        print("computer win")
    
      elif (c == "gun" and u == "gun"):
        print("Oooho..! Game Draw")
    
      elif (c == "gun" and u == "water"):
        print("Yah..! You win")
        break;    
        ch = ch+1;
    print("computer guess was :- " + c)
    print("user guess was :- " + u)
    
u = 0;
gamewin(u)

# ask = input("want to play again ? :- ");  
# while(ask == y):
  
# else:
#   print("Thanks..! Visit again to play this game.")

    