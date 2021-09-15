def evaluate_round_winner(person1,person2):
    if person1==person2:
        return 0
    elif person1 == "rock" and person2 == "paper":
        return 2
    elif person1 == "rock" and person2 == "scissor":
        return 1
    elif person1 == "paper" and person2 == "rock":
        return 1
    elif person1 == "paper" and person2 == "scissor":
        return 2
    elif person1 == "scissor" and person2 == "paper":
        return 1
    elif person1 == "scissor" and person2 == "rock":
        return 2 
import random

print("Welcome to ROCK - PAPER - SCISSOR GAME\n")
print("Instructions\n")
print("1) This game will have 7 rounds.\n")
print("2) In Each round there may be a winner or it may tie\n")
print("We are starting the game!!! Have Fun!!!\n")

rounds=1
p1 = 0
p2 = 0

while(rounds<=7):
    startover: print("..............Enter your choice...............\n")
    print("option 1 for rock ... option 2 for paper and option 3 for scissor\n")
    userInputVal = int(input())
    options = [1,2,3]
    optionsDict = {1:"rock",2:"paper",3:"scissor"}
    if userInputVal not in options:
        print("Please select the right option\n")
        continue
    else:
        rounds = rounds+1
        val = evaluate_round_winner(optionsDict[userInputVal],optionsDict[random.choice(options)])
        if(val == 1):
            print("You are the winner of this round.\n")
            p1 = p1+1
        elif(val == 2):
            print("Computer is the winner of this round.\n")
            p2 = p2+1
        else:
            print("Its a tie!!\n")
print("................Game completed.........\n")
print("Your game score: ",p1)
print("\n")
print("Computer score: ",p2)
print("\n")

if(p1==p2):
    print("................Its a tie!!!..............\n")
elif(p1>p2):
    print("................Congrats!! Your are the winner...........\n")
else:
    print("................Sorry!!   You lost..please try again.............\n")

print("...GAME OVER...GAME OVER...GAME OVER...GAME OVER...GAME OVER...GAME OVER...GAME OVER...\n")    