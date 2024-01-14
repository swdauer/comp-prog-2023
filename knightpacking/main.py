boardSize = int(input())
board = [[False for _ in range(boardSize)] for _ in range(boardSize)]

def nextSpace():
    for i in range(boardSize):
        for j in range(boardSize):
            if not board[i][j]:
                return (i, j)
    return False

def printBoard():
    for i in board:
        for j in i:
            if j:
                print(1, end = "")
            else:
                print(0, end = "")
        print()

def placeKnight(space):
    x = space[0]
    y = space[1]

    board[x][y] = True
    if x - 2 >= 0 and y - 1 >= 0:
        board[x-2][y-1] = True
    if x - 1 >= 0 and y - 2 >= 0:
        board[x-1][y-2] = True
    if x - 2 >= 0 and y + 1 < boardSize:
        board[x-2][y+1] = True
    if x - 1 >= 0 and y + 2 < boardSize:
        board[x-1][y+2] = True
    if x + 2 < boardSize and y - 1 >= 0:
        board[x+2][y-1] = True
    if x + 1 < boardSize and y - 2 >= 0:
        board[x+1][y-2] = True
    if x + 2 < boardSize and y + 1 < boardSize:
        board[x+2][y+1] = True
    if x + 1 < boardSize and y + 2 < boardSize:
        board[x+1][y+2] = True

player = 0
while True:
    space = nextSpace()
    if space == False:
        break   
    placeKnight(space)
    printBoard()
    print()
    player = (player + 1) % 2

if player == 0:
    print("second")
else:
    print("first")
