import random

while True:
    choices=["R", "P","S"]
    computer = random.choice(choices)  
    player= input("What's your choice? 'R'for rock ,'P'for paper,'S'for scissors:")
    print(f"\ncomputer:{computer},player:{player}.\n")

    if player not in choices:
        print("error")
    
    if player == computer:
        print("Tie")
    elif player== "R":
        if computer =="P":
            print("You lose")
        if computer=="S":
            print("You win")
    elif player=="P":
        if computer=="S":
            print("You lose")
        if computer=="R":
            print("You win")
    elif player=="S":
        if computer=="R":
            print("You lose")
        if computer=="P":
            print("You win")

    play_again=input("play again?(y/n):")

    if play_again!="y":
         break

print("Bye!")
