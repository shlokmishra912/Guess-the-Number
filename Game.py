import random

Player = -1
Guess = 0
Computer = random.randint(1,100)

while Player != Computer:
    Player = int(input("Your number :"))
    if Player > Computer:
        print("Lower Number plzz....")
        Guess += 1
    elif Player < Computer:
        print("Higher Number plzz....")
        Guess += 1

print(f"Congrats {Player} is answer ,{Guess} it taken")
