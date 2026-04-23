import time
import os

def clear():
    os.system('cls')

score_list = []



while True:

    timer = int(input("How many second do you need?: "))

    for x in range(timer, 0, -1):
        clear()
        print(x)
        time.sleep(1)
        clear()

    print("Time is up!")

    score = int(input("What is your score?: "))
    score_list.append(score)
    clear()

    answer = input("Do you want to continue, or to see your scores?(Yes/No/score):").lower()
    if answer == "yes":
        continue
    elif answer == "no":
        break
    elif answer == "score":
        print(score_list)
        input("Press any key to continue....")
