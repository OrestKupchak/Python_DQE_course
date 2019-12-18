vertical = '|    |'
horizontal = ' ____ '
board_size = 3

matrix = [[' ' for x in range(board_size)] for y in range(board_size)] 
print(matrix)

x_axis = ''
for i, item in enumerate(matrix[0]):
    x_axis += str(i) + '  '

print(('  ')*board_size , x_axis)


for i, item in enumerate(matrix):
    #print(i)
    print("    ---+---+---")
    for j, item in enumerate(item):
        #print(j)
        #print(matrix[i][j])
        print(" " + str(j) + "   " + matrix[i][j] + " | " + matrix[i][j] +" | " + matrix[i][j] +" ")
        print("    ---+---+---")
        

#print("     0   1   2  ")
#print([ list()] in range board_size).split()
#print()
#print(" 0   " + board[0][0] + " | " + board[0][1] +" | " + board[0][2] +" ")
#print("    ---+---+---")
#print(" 1   " + board[1][0] + " | " + board[1][1] +" | " + board[1][2] +" ")
#print("    ---+---+---")
#print(" 2   " + board[2][0] + " | " + board[2][1] +" | " + board[2][2] +" ")
#print()



player = 1
def playerMove(board):
    x = int(input("Player {}, please enter x: ".format(player)))
    y = int(input("Player {}, please enter y: ".format(player)))
    # Check whether x, y is a valid choice, that is: not yet taken
    board[x][y] = 'X' if player == 1 else 'O'

def playGame():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    finished = False
    player = 1
    while not finished:
        #print board with current state after previous move
        #make another player move (set value to board on empty field)
        #check for win/end, set finished accordingly
       
        player = 3 - player # change players between 1 and 2

playGame()