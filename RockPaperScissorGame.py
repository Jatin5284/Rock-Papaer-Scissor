import random

li = ["rock", "papper", "scissor"]

# rock vs papper->papper wins
# rock vs scissor-> rock wins
# papper vs scissor -> scissor wins
while True:
    ccount = 0
    ucount = 0
    print("Rock,Paper Scissor Game Start")
    us = int(input('''1.Play Yes
2.No | Exit
 '''))
    if us == 1:
        for i in range(1, 6):
            us1 = int(input('''Please select any one option
                1.Rock
                2.Scissor
                3.Papper
                '''))
            if us1 == 1:
                uchoice = "rock"
            elif us1 == 2:
                uchoice = "scisspr"
            elif us1 == 3:
                uchoice = "papper"
            cchoice = random.choice(li)
            if cchoice == uchoice:
                print("Computer value", cchoice)
                print("User value", uchoice)
                print("Game Draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and cchoice == "scissor") or (uchoice == "papper" and cchoice == "rock") or (
                    uchoice == "scissor" and cchoice == "papper"):
                print("Computer value", cchoice)
                print("User value", uchoice)
                print("You win")
                ucount = ucount + 1
            else:
                print("Computer value", cchoice)
                print("User value", uchoice)
                print("Computer win")
                ccount = ccount + 1
        if (ucount == ccount):
            print("Game draw")
            print("User score", ucount)
            print("Computer score", ccount)
        elif ucount > ccount:
            print("Ypu win the game")
            print("User score", ucount)
            print("Computer score", ccount)
        else:
            print("Computer win the game")
            print("User score", ucount)
            print("Computer score", ccount)
    else:
        break
