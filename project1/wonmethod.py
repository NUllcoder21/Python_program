import random

choices={"s": 1, "w": -1, "g": 0}
reverse_choice= {1: "Snake", -1: "Water", 0: "Gun"}

computer=random.choice([1,-1,0])

user_input=(input("Enter your choice"))

if user_input not in choices:
    print("invalid input")
else:
     user_choice = choices[user_input]
     print(f"You chose {reverse_choice[user_choice]}.")
     print(f"Computer chose {reverse_choice[computer]}.")

     if computer==user_choice :
          print("Its draw the game")
     elif((computer-user_choice)==-1 or (computer-user_choice)==2):
          print("you loss!")
     else:
          print("you win!")        
