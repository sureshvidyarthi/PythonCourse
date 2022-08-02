import random
def sgw(com, mine):
    if (com==mine):
        return None
    if(com=='s' and mine=='g'):
        return True
    elif(com=='w' and mine=='s'):
        return True
    elif(com=='g' and mine=='w'):
        return True
    else:
        return False

choise= ('w', 'g', 's')
com= random.randint(0,2)
com= choise[com]
mine= input(" Choose either w or g or s: ")

win = sgw(com, mine)
print(f"You choose {mine} and computer choose {com}")

if win is None:
    print("Match Draw")
if win is True:
    print("You win")
else:
    print("You lose")