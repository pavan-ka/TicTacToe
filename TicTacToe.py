board = [1,2,3,4,5,6,7,8,9]

def printboard():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def checkwin():
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True

def xwin():
    if board[0] == board[1] == board[2] == 'X':
        return True
    if board[3] == board[4] == board[5] == 'X':
        return True
    if board[6] == board[7] == board[8] == 'X':
        return True
    if board[0] == board[3] == board[6] == 'X':
        return True
    if board[1] == board[4] == board[7] == 'X':
        return True
    if board[2] == board[5] == board[8] == 'X':
        return True
    if board[0] == board[4] == board[8] == 'X':
        return True
    if board[2] == board[4] == board[6] == 'X':
        return True

def owin():
    if board[0] == board[1] == board[2] == 'O':
        return True
    if board[3] == board[4] == board[5] == 'O':
        return True
    if board[6] == board[7] == board[8] == 'O':
        return True
    if board[0] == board[3] == board[6] == 'O':
        return True
    if board[1] == board[4] == board[7] == 'O':
        return True
    if board[2] == board[5] == board[8] == 'O':
        return True
    if board[0] == board[4] == board[8] == 'O':
        return True
    if board[2] == board[4] == board[6] == 'O':
        return True

print('Welcome to Tic-Tac-Toe!!!')
p1name = input('Player 1, you are X! What is your name ==> ')
print('Hello', p1name,'!')
p2name = input('Player 2, you are O! What is your name ==> ')
print('Hello', p2name, '!')

board = [1,2,3,4,5,6,7,8,9]
checker = 0

print('If the slot has a number then it is free to use! If it has an X or an O, it is taken! Let the games begin!!!')

printboard()

while checkwin() != True and checker < 9:
    if checker % 2 == 0:
        cellno = input(p1name + ' where would you like to print your marker? ')
        board[int(cellno)-1] = 'X'
        printboard()
        checker = checker + 1
        if checkwin() == True:
            break
    else:
        cellnum = input(p2name + ' where would you like to place your marker? ')
        board[int(cellnum)-1] = 'O'
        printboard()
        checker = checker + 1
        if checkwin() == True:
            break

if xwin() == True:
    print(p1name, ' who was X has won the game!!! Great job! Rerun for a rematch!')
elif owin() == True:
    print(p2name, 'who was O has won the game!!! Great job! Rerun for a rematch!')
else:
    print('Looks like we had a draw! Looks like we will need a rematch!')

print('That is it for Tic-Tac-Toe!')