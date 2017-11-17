import random
print("              _______. ")
print("   ______    | .   . |\ ")
print("  /     /\   |   .   |.\ ")
print(" /  '  /  \  | .   . |.'| ")
print("/_____/. . \ |_______|.'| ")
print("\ . . \    /  \ ' .   \'| ")
print(" \ . . \  /    \____'__\| ")
print("  \_____\/ ")
print("                            ")
print("__________________________")
print(" Ludo Game By Lubi")
print("--------------------------")

def RollTwoDice():
    die1=random.randint(1, 6)
    die2=random.randint(1, 6)

    roll=die1 + die2

    if die1 == 1:
        ShowDie1()

    elif die1==2:
        ShowDie2()

    elif die1==3:
        ShowDie3()

    elif die1==4:
        ShowDie4()

    elif die1==5:
        ShowDie5()

    elif die1==6:
        ShowDie6()
#Next dice
    if die2==1:
        ShowDie1()

    elif die2==2:
        ShowDie2()

    elif die2==3:
        ShowDie3()

    elif die2==4:
        ShowDie4()

    elif die2==5:
        ShowDie5()

    elif die2==6:
        ShowDie6()      
        
    return roll

def ShowDie1():
    print('---------')
    print('|       |')
    print('|   1   |')
    print('|       |')
    print('---------')
    return

def ShowDie2():
    print('---------')
    print('|       |')
    print('|   2   |')
    print('|       |')
    print('---------')
    return

def ShowDie3():
    print('---------')
    print('|       |')
    print('|   3   |')
    print('|       |')
    print('---------')
    return

def ShowDie4():
    print('---------')
    print('|       |')
    print('|   4   |')
    print('|       |')
    print('---------')
    return

def ShowDie5():
    print('---------')
    print('|       |')
    print('|   5   |')
    print('|       |')
    print('---------')
    return

def ShowDie6():
    print('---------')
    print('|       |')
    print('|   6   |')
    print('|       |')
    print('---------')
    return


print("Press \'Enter\' to roll the dice")
input()
myRoll=RollTwoDice()
print("You rolled a "+str(myRoll)+'!')

        
        

    
    