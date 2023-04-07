import random
#Generates a random input from computer and assigns a string to it
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"
#Main game function
def game(comp, you):
#If user input matches with the comp
    if comp == you:
        return None
#Check all possibilites if computer picks rock
    elif comp == "r":
        if you == "p":
            return True
        if you == "s":
            return False
#Check all possibilites if computer picks paper
    elif comp == "p":
        if you == "s":
            return True
        if you == "r":
            return False
 #Check all possibilites if computer picks scissors   
    elif comp == "s":
        if you == "p":
            return False
        if you == "r":
            return True
#While loop to get a valid input from player
while True:
    print("Computer's turn! Please wait")
    you = input("Your turn. Choose between (r)ock,(p)aper or (s)cissors: ")
    if you == "s" or you == "p" or you == "r":
        break
#Some red color to show some intimidation
    else:
        print("\033[1;31;40mPick between r, s or p")
        continue
#Self explanatory from now on xd!
z = game(comp, you)
if z is None:
    print(f"Tie! Computer chose {comp}")
elif z:
    print(f"You win! Computer chose {comp} ")
else:
    print(f"You lose Computer chose {comp}")
