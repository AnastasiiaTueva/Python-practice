import random
import os


def clear():
    os.system('cls')

clear()
difficulty = input("Choose the difficulty(easy, medium, hard): ").lower()
numbers = ""
point = 4

if difficulty == "easy":
    randomNum = random.randint(1,5)
    numbers = "1-5"

elif difficulty == "medium":
        randomNum = random.randint(1,10)
        numbers = "1-10"
        point -= 2

elif difficulty == "hard":
        randomNum = random.randint(1,20)
        numbers = "1-20"
        point -= 3
else:
    print("Invalid difficulty")
    exit()

while True:
    clear()
    print(f"Number of possible attempts: {point}")
    game = input(f"Guess the number ({numbers}): ")
    
    if game == randomNum:
        print("You won!")
        break

    else:
        clear()
        point -= 1

        if point == 0:
            print("You lost!")
            break
        
