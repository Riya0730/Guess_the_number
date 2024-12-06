import random
target = random.randint(1,100)
while True:
    userchoice = input("guess the target or Quit(Q):")
    if(userchoice == "Q"):
      break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("\nGuess Correctly")
        break
    elif(userchoice < target):
        print("your number is too small...choose another one")
    else :
        print("your number is too big...choose another one")
print("\n**********GAME OVER*********")
