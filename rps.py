import random 

player_score = 0
computer_score = 0
while True:
    player = input("rock , paper, scissors or ('quit)")
    computer = random.choice(["rock" , "paper" ," scissors"])
    print(f"you choose: {player}, computer choose:{computer}")

    if player == "quit":
            break
    if player not in ["rock", "paper", "scissors"]:
        print("invalid choice ")
        continue
    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("you win")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You wins")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print ("you win") 
        player_score += 1
    else:
        print("computer wins")
        computer_score += 1
    if player == "quit":
        break


print(f"player score:{player_score} computer score:{computer_score}")

if player_score > computer_score:
    print("player wins")
else:
    print("computer wins")

        
      