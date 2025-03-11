# the game function in a program lets a user play a game and return the score as an integer you need to read a file Hi-score.txt which is either blank or contains the previous hi-score you need to write the program to update the Hi-score wheever the game fuction breaks the Hi-score
import random

def game():
    print("you are playing the game..")
    score=random.randint(1,62)

    #Fetch the Hiscore
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=  0  
    print(f"your score:{score}")
    if(score>hiscore or hiscore==""):
        #write the hisore  to the file
        with open("hiscore.txt","w") as f:
          f.write(str(score))

    return   score     


game()              