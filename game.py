import random 
user=input("rock, paper, or scissors? ").lower()
computer=random.choice(["rock", "paper", "scissors"])
print(f'computer: {computer} ' )
if user==computer:
     print("tie")
elif user=="rock":
     if computer=="paper":
        print("computer wins")
     else:
         print("you win")
elif user=="paper":
     if computer=="scissors":
         print("computer wins")
     else:
         print("you win")
elif user=="scissors":
     if computer=="rock":
         print("computer wins")
     else:
         print("you win")
