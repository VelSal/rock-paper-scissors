import random

userWins = 0
computerWins = 0
draw = 0
options = ["rock" , "paper" , "scissors"]

print("Welcome to a classical Rock, Paper, Scissors game against the computer")
while True:
    userPick = input("Type \"Rock\", \"Paper\" or \"Scissors\" to make your pick. Type Q to quit. ").lower()
    if userPick == "q":
        break
    elif userPick not in options:
        print("There is no", userPick , "in the classical Rock, Paper, Scissors game!")
        continue
    else:
        pickIndex = random.randint(0 , 2)
        computerPick = options[pickIndex]
        
        if userPick == computerPick:
            draw += 1
            print("It's a draw")
        elif userPick == "rock" and computerPick == "scissors":
            userWins += 1
            print("You won!")
        elif userPick == "paper" and computerPick == "rock":
            userWins += 1
            print("You won!")
        elif userPick == "scissors" and computerPick == "paper":
            userWins += 1
            print("You won!")
        else:
            computerWins += 1
            print("Computer wins!")
            
print("You won" , userWins , "times.")            
print("Computer won" , computerWins , "times.")
print(draw , "draws.")
print("Have a great day!")
        
        
    