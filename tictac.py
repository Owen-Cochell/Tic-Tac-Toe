#Tic-Tac-Toe game
#Written by: Owen Cochell

#Simple, easy-to-import, Tic-Tac_Toe game

#Board config:

# +==============+
# | 00 | 01 | 02 |
# |----+----+----|
# | 10 | 11 | 12 |
# |----+----+----|
# | 20 | 21 | 22 |
# +==============+

#Nested lists are our best friends here!

def boardDisplay(b):

    #Displays board

    print("  +===========+")
    print("1.| {} | {} | {} |".format(b[0][0], b[0][1], b[0][2]))
    print("  |---+---+---|")
    print("2.| {} | {} | {} |".format(b[1][0], b[1][1], b[1][2]))
    print("  |---+---+---|")
    print("3.| {} | {} | {} |".format(b[2][0], b[2][1], b[2][2]))
    print("  +===========+")
    print("    1.  2.  3.")

    return

def boardCheck(b, col, row):

    #Checks if move is legal

    if col > 3 or row > 3 or col < 0 or row < 0:

        return False

    if b[col][row] == " ":

        return True

    return False

def boardFull(b):

    #Checks for full board - Cat's game!

    for i in range(len(b)):

        for j in range(len(b)):

            if b[i][j] == " ":

                return False

    return True

def boardUpdate(b, col, row, letter):

    #Updates board with given value

    check = boardCheck(b, col, row)

    if check is False:

        return False

    b[col][row] = letter

    return True

def checkDiag(b):

    #Checking for diagonal three in a row

    if b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[0][0] != " ":

        return True

    if b[2][0] == b[1][1] and b[1][1] == b[0][2] and b[2][0] != " ":

        return True

    return False

def checkDiagWin(b, letter, playLetter):

    #Checking for a possible diagonal three in a row.
    #For blocking and winning

    count = 0
    emptyPos = (9, 9)

    for i in range(0, 3):

        currValue = b[i][i]

        if currValue == playLetter:

            count += 1

        if currValue == " ":

            emptyPos = (i, i)

        if count == 2:

            if emptyPos == (9, 9) and b[2][2] == " ":

                emptyPos = (2, 2)

            if emptyPos == (9, 9):

                break

            boardUpdate(b, emptyPos[0], emptyPos[1], letter)

            return True

    count = 0
    emptyPos = (9, 9)

    for i in range(2, -1, -1):

        j = 2-i
        currValue = b[i][j]

        if currValue == playLetter:

            count += 1

        if currValue == " ":

            emptyPos = (i, j)

        if count == 2:

            if emptyPos == (9, 9):

                break

            boardUpdate(b, emptyPos[0], emptyPos[1], letter)

            return True

    return False

def checkHoriz(b):

    #Checking for a horizontal three in a row.

    for i in range(len(b)):

        if b[i][0] == b[i][1] and b[i][1] == b[i][2] and b[i][0] != " ":

            return True

    return False

def checkVertWin(b, letter, playLetter):

    #Function for checking for a possible Three in a row Vertically.
    #For blocking and winning

    for i in range(len(b)):

        count = 0
        emptyPos = (9,9)

        for j in range(len(b)):

            currValue = b[j][i]

            if currValue == playLetter:

                count += 1

            if currValue == " ":

                emptyPos = (j, i)

            if count == 2:

                #if emptyPos == (9, 9) and b[j][2] == " ":

                  #  emptyPos = (2, i)

                if emptyPos == (9, 9):

                    break

                win = boardUpdate(b, emptyPos[0], emptyPos[1], letter)

                if win:

                    print("Valid move")

                if win is False:

                    print("Computer invalid move")

                return True

    return

def checkVet(b):

    #Code for diagonal three in a row
    
    for i in range(len(b)):

        for j in range(len(b)):

            if b[0][i] == b[1][i] and b[1][i] == b[2][i] and b[0][i] != " ":

                return True

    return False

def checkHorizWin(b, letter, playLetter):

    #Code for finding possible horizontal three in a row
    #For blocking and winning

    for i in range(len(b)):

        count = 0
        emptyPos = (9, 9)

        for j in range(len(b)):

            # Checking for horizontal player win

            currValue = b[i][j]

            if currValue == playLetter:

                count += 1

            if currValue == " ":

                emptyPos = (i, j)

            if count == 2:

                #if emptyPos == (9, 9) and b[i][2] == " ":

                 #   emptyPos = (i, 2)

                if emptyPos == (9, 9):

                    break

                boardUpdate(b, emptyPos[0], emptyPos[1], letter)

                return True

    return False

def checkWin(b):

    #Function for checking for win

    diag = checkDiag(b)
    horis = checkHoriz(b)
    vert = checkVet(b)

    if diag or horis or vert:

        return True

    return False

def compPlan(b, letter):

    #Code for OTTTP!
    #Basicly, just occupies three corners.
    #Almost guaranteed win!

    for i in range(0, 3, 2):

        for j in range(0, 3, 2):

            if boardCheck(b, i, j):

                boardUpdate(b, i, j, letter)
                return True

    return False

def randomPlay(b, letter):

    #Code for playing first open position:

    for i in range(len(b)):

        for j in range(len(b)):

            if boardCheck(b, i, j):

                boardUpdate(b, i, j, letter)
                return
    return

def computer(b, letter):

    #A.I Algorithm is as follows:

    #1. Checks for win. If win, win!
    #2. Checks for block. If block, block!
    #3. Dose Owen's Tic-Tac-Toe-Plan(OTTTP). If spaces available, OTTTP!
    #4. PLays first open position

    #Determining letter here:

    if letter in ('X', 'x'):

        playLetter = 'O'

    if letter in ('O', 'o'):

        playLetter = 'X'

    #Checking for win move

    if checkHorizWin(b, letter, letter):

        return

    if checkVertWin(b, letter, letter):

        return

    if checkDiagWin(b, letter, letter):

        return

    #Checking for block move

    if checkHorizWin(b, letter, playLetter):

        return

    if checkVertWin(b, letter, playLetter):

        return

    if checkDiagWin(b, letter, playLetter):

        return

    #Checks for OTTTP!

    if compPlan(b, letter):

        return

    #Playing first open position:

    randomPlay(b, letter)

    return

def banner():

    #Super cool banner

    print("+==============================================================+")
    print('''
     _____ _           _____               _____          
    |_   _(_)         |_   _|             |_   _|         
      | |  _  ___ ______| | __ _  ___ ______| | ___   ___ 
      | | | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \\
      | | | | (__       | | (_| | (__       | | (_) |  __/
      \_/ |_|\___|      \_/\__,_|\___|      \_/\___/ \___|
    ''')
    print("                   A game by: Owen Cochell")
    print("                       Version 1.0.0")

    return

def start():

    #Basic instructions

    print("\nWelcome to Tic-Tac-Toe!")
    print("The goal is simple:\nGet three in a row horizontally, vertically, or diagonally to win!")
    print("You will have to enter a collum number, and a row number. They will be listed on the side of the diagram.")
    print("Have fun!")

def letterChoice():

    #Allowing player to choose letter

    while True:

        print("\nWould you like to be 'X' or 'O'?")
        inp = input("Please choose a letter:")

        if inp not in ('X', 'x', 'o', 'O'):

            print("'{}' Is not a valid letter! Please try again!".format(inp))
            continue

        inp = inp.upper()

        return inp

def ticStart():

    #Main function were code is executed
    #This is were the magic happens!

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    banner()
    start()
    letter = letterChoice()

    if letter in ('X', 'x'):

        compLetter = 'O'

    if letter in ('O', 'o'):

        compLetter = 'X'

    while True:

        if boardFull(board):

            # If board is full

            boardDisplay(board)
            print("Cat's game. Nobody wins!")
            break

        #Displaying board

        boardDisplay(board)

        #Getting input from user and cleaning it up

        col = int(input("\nPlease enter a collum number:"))
        row = int(input("Please enter a row number:"))

        col -= 1
        row -= 1

        if boardUpdate(board, col, row, letter):

            #User move successful!

            print("\nMove successful!")

            if checkWin(board):

                #If user wins

                boardDisplay(board)
                print("\nCongrats you win!")
                empty = input("Press enter to continue...")
                break

        else:

            #If move is invalid

            print("Invalid move!")
            continue

        if boardFull(board):

            # If board is full

            boardDisplay(board)
            print("Cat's game. Nobody wins!")
            empty = input("Press enter to continue...")
            break

        print("\nComputer's move...\n")

        computer(board, compLetter)

        if checkWin(board):

            #If computer wins

            boardDisplay(board)
            print("\nYou lose :(")
            empty = input("Press enter to continue...")
            break

ticStart()
