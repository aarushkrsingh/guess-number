
import random
target=random.randint(1,100)
while True:
    userchoice=int(input("Guess the number:"))
    if userchoice < target:
        print("the guessed number is smaller")
    elif userchoice > target:
        print("the guessed number is larger")
    else:
        print("Success! you guessed the number")
        break
print("GAME OVER") 