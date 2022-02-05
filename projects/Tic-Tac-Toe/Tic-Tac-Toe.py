import random
import sys

gameboard = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]
currentPlayer = "X"
opponent = 'O'
win = None
gRunning = True
j = 0
i = 0
k = 0
def input1():
    global j
    if j==0:
        c = str(input('Are you want to play One Player Mode Or two plyer(1/2): '))
        j+=1
        return c
play = input1()
if play == '1':
    k = 1
elif play == '2':
    k = 0
else:
    print('invalid')
    j = 0
    input1()
# gameboard
def showgameboard(gameboard):
    print('  |GAMEBOARD|   |TABLE POSITION| ')
    print()
    print('   ' + gameboard[0] + " | " + gameboard[1] + " | " + gameboard[2] + '     ' + " 1 | 2 | 3")
    #print()
    print('   ' + gameboard[3] + " | " + gameboard[4] + " | " + gameboard[5] + '     ' + " 4 | 5 | 6")
    #print()
    print('   ' + gameboard[6] + " | " + gameboard[7] + " | " + gameboard[8]+ '     ' + " 7 | 8 | 9")
    print()


# take player input
def playerInput(gameboard):
    inp = int(input("Select a spot 1-9 Player("+currentPlayer+ ") : "))
    global i
    if 1 <= inp <= 9:
        if gameboard[inp-1] == "_":
            gameboard[inp-1] = currentPlayer
            i = 0
        elif gameboard[inp-1] == opponent:
            print('opponent has already occupied that place')
            i = 1
        elif gameboard[inp-1] == currentPlayer:
            print('how manny times are you gonna take that same move')
            i = 1
    else:
        print('invalid move')
        i = 1
# check for win or tie
def checkyaxis(gameboard):
    global win
    if gameboard[0] == gameboard[1] == gameboard[2] and gameboard[0] != "_":
        win = gameboard[0]
        return True
    elif gameboard[3] == gameboard[4] == gameboard[5] and gameboard[3] != "_":
        win = gameboard[3]
        return True
    elif gameboard[6] == gameboard[7] == gameboard[8] and gameboard[6] != "_":
        win = gameboard[6]
        return True

def checkxaxis(gameboard):
    global win
    if gameboard[0] == gameboard[3] == gameboard[6] and gameboard[0] != "_":
        win = gameboard[0]
        return True
    elif gameboard[1] == gameboard[4] == gameboard[7] and gameboard[1] != "_":
        win = gameboard[1]
        return True
    elif gameboard[2] == gameboard[5] == gameboard[8] and gameboard[2] != "_":
        win = gameboard[2]
        return True


def checkzaxis(gameboard):
    global win
    if gameboard[0] == gameboard[4] == gameboard[8] and gameboard[0] != "_":
        win = gameboard[0]
        return True
    elif gameboard[2] == gameboard[4] == gameboard[6] and gameboard[4] != "_":
        win = gameboard[2]
        return True


def checkWin(gameboard):
    global gRunning
    global i
    if checkyaxis(gameboard):
        showgameboard(gameboard)
        print("The winner is " + win + "!")
        gRunning = False
        i = 2
        input('press any key to exit')
        sys.exit()
    elif checkxaxis(gameboard):
        showgameboard(gameboard)
        print("The winner is " + win + "!")
        gRunning = False
        i = 2
        input('press any key to exit')
        sys.exit()
    elif checkzaxis(gameboard):
        showgameboard(gameboard)
        print("The winner is " + win + "!")
        gRunning = False
        i = 2
        input('press any key to exit')
        sys.exit()
def Tiechecking(gameboard):
    global gRunning
    if "_" not in gameboard:
        showgameboard(gameboard)
        print("It is a tie!")
        gRunning = False
        input('press any key to exit')
        sys.exit()

# switch player
def switchplayer():
    global currentPlayer
    global opponent
    if currentPlayer == "X":
        currentPlayer = "O"
        opponent = 'X'
    else:
        currentPlayer = "X"
        opponent = 'O'

def AI(gameboard):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if gameboard[position] == "_":
            gameboard[position] = "O"
            switchplayer()


while gRunning:
    showgameboard(gameboard)
    playerInput(gameboard)
    checkWin(gameboard)
    Tiechecking(gameboard)
    if i==0:
        switchplayer()
    if k == 1:
        AI(gameboard)
    checkWin(gameboard)
    Tiechecking(gameboard)
    if j==0:
        input1()