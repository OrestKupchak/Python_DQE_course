vertical = '|     |'
horizontal = ' _____ ' 

board_size = 4
fields_to_win = 3
#------------------------------------------------------------
board = [[' ' for x in range(board_size)] for y in range(board_size)] 
choices_board = [[0 for x in range(board_size)] for y in range(board_size)] 
#print(board)



def render_board():
    placeholder = ''
    x_axis = ''

    for i, item in enumerate(board[0]):
        x_axis += str(i) + '      '

    print('    ', x_axis)



    for i in range(len(board)):
        y_axis = i
        for j in range(len(board[i])):
            placeholder += '|  '+ board[i][j] +'  |'
        print(' ', horizontal*board_size)  
        print(' ', vertical*board_size)
        print(y_axis, placeholder)
        placeholder = ''
    print(' ', horizontal*board_size)  




#------------------------------------------------------------
player = 1
def playerMove(board):
    x = int(input("Player {}, please enter x: ".format(player)))
    y = int(input("Player {}, please enter y: ".format(player)))
    # Check whether x, y is a valid choice, that is: not yet taken
    if player == 1:
        board[x][y] = 'X'  
        choices_board[x][y] = 1
    else: 
        board[x][y] ='O'
        choices_board[x][y] = -1

#---------------------------------------------------
#get columns, rows, diaginals from current board


max_col = len(board[0]) #5
max_row = len(board)    #5

cols = [ list() for elements in range(max_col)]
rows = [ list() for elements in range(max_row)]

leftToRightDiagonal = [ list() for elements in range(max_row + max_col - 1)]
rightToLeftDiagonal = [ list() for elements in range(len(leftToRightDiagonal))]


min_rightToLeftDiagonal = -max_row + 1

#for row in board:
    #print(row)

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(board[y][x])
        rows[y].append(board[y][x])
        leftToRightDiagonal[x+y].append(board[y][x])
        rightToLeftDiagonal[x-y-min_rightToLeftDiagonal].append(board[y][x])

valid_verticals = []
for valid in cols:
    if len(valid) >= fields_to_win :
        valid_verticals.append(valid)

valid_horizontals = []
for valid in rows:
    if len(valid) >= fields_to_win :
        valid_horizontals.append(valid)


valid_leftToRightDiagonal = []
for valid in leftToRightDiagonal:
    if len(valid) >= fields_to_win :
        valid_leftToRightDiagonal.append(valid)

valid_rightToLeftDiagonal = []
for valid in rightToLeftDiagonal:
    if len(valid) >= fields_to_win :
        valid_rightToLeftDiagonal.append(valid)

#---------------------------------------------------
#define_win_combinations_map


temp_res = list()

def define_win_combinations_map(list):
    for comb in list:
        if len(comb) >= fields_to_win:
            #print(comb)
             for i in range(len(comb)): #valid win combinations should be chunks
                if len(comb[i:i+fields_to_win]) == fields_to_win: # with length of defined 'fields_to_win'
                    temp_res.append(comb[i:i+fields_to_win]) 
    #print(temp_res)            

define_win_combinations_map(valid_verticals)
define_win_combinations_map(valid_horizontals)
define_win_combinations_map(valid_leftToRightDiagonal)
define_win_combinations_map(valid_rightToLeftDiagonal)




#------------------------------------------------------------
def checkTotalTurns(fields_combination):
    choice_results = 0
    for choice_map in fields_combination:
        #print(choice_map)
        for choice in choice_map:
            choice_results += choice
            print(choice_results, fields_to_win)
            #print("choice_map --> ", choice_map, "; choice_results --> ", choice_results)
            #print("[choice] = ",[choice],"choice_map[choice] = ", choice_map[choice], "; choice_results =", choice_results)

        if choice_results == fields_to_win:
            #print("Winner is player 'X' !")
            print(choice_results, fields_to_win)
            return print("Winner is player 'X' !")                
        elif choice_results == -fields_to_win:
            #print("Winner is player 'O' !")
            print(choice_results, fields_to_win)
            return print("Winner is player '0' !")               
        else:
            choice_results = 0
        #    print("It's a draw!")
        #    #return "It's a draw!"
        #choice_results = 0





def playGame():
    #board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    finished = False
    player = 1
    while not finished:
        render_board()    #print board with current state after previous move
        playerMove(board) #make another player move (set value to board on empty field)
        checkTotalTurns(choices_board)#check for win/end, set finished accordingly
       
        player = 3 - player # change players between 1 and 2

playGame()