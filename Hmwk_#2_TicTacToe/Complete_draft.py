import random
#import board 

#---------------------------------------------------
#draw board/ set players/ apply player's choice to the board cells
# TO DO
vertical = '|     |'
horizontal = ' _____ ' 

board_size = 4
fields_to_win = 3


board = [[' ' for x in range(board_size)] for y in range(board_size)] #grafical board 'X'/'O'
choices_board = [[0 for x in range(board_size)] for y in range(board_size)] #logical board 1/-1 to store players moves for win check
     #prepare structures for storing all posible columns, rows, diagonals of the board of defined size
max_col = len(choices_board[0]) 
max_row = len(choices_board)    
   
cols = [ list() for elements in range(max_col)] 
rows = [ list()  for elements in range(max_row)]
leftToRightDiagonal = [ list() for elements in range(max_row + max_col - 1)]
rightToLeftDiagonal = [ list() for elements in range(len(leftToRightDiagonal))]
min_rightToLeftDiagonal = -max_row + 1

valid_verticals = []
valid_horizontals = []
valid_leftToRightDiagonal = []
valid_rightToLeftDiagonal = []

#------------------------------------------------------------
#draw graphical board of given size

def render_board(): 
    placeholder = ''  #invisible cells within each board field, where players previous move's choice will be showed
    x_axis = ''      #sequence of numbers for user's navigation of fileds on 'X' axis

    for i in range(len(board[0])):
        x_axis += str(i) + '      ' #add padding for alignment between axis flags 
    print('    ', x_axis)           #add margin for alignment of axis flags to board fields

    for i in range(len(board)):
        y_axis = i                          #sequence of numbers for users navigation of fileds on 'Y' axis
        for j in range(len(board[i])):
            placeholder += '|  '+ board[i][j] +'  |' #add placehoder for players input into field on visible board
        print(' ', horizontal*board_size)   #|
        print(' ', vertical*board_size)     #|add vertical and horizontal lines for fields 
        print(y_axis, placeholder)          #|
        placeholder = ''                    #|
    print(' ', horizontal*board_size)  

#---------------------------------------------------
#get columns, rows, diagonals from current board
def define_valid_directions(choices_board):
        #populate respective structures with data from current board state
    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(choices_board[y][x])
            rows[y].append(choices_board[y][x])
            leftToRightDiagonal[x+y].append(choices_board[y][x])
            rightToLeftDiagonal[x-y-min_rightToLeftDiagonal].append(choices_board[y][x])


#------------------------------------------------------------
#switch players and make moves on board

player = 1 #define Player: 1 = 'X'/ 2 = 'O'
def playerMove(board):
    x = int(input("Player {}, please enter x: ".format(player))) #input x,y coordinates of field on board to make choice 
    y = int(input("Player {}, please enter y: ".format(player)))

    # Check whether x, y is a valid choice, that is: not taken yet
    if player == 1:
        board[x][y] = 'X'       #show choice on visual board
        choices_board[x][y] = 1 #add choice to logical board for win tracking
    else: 
        board[x][y] ='O'
        choices_board[x][y] = -1
    #return choices_board
    define_valid_directions(choices_board)

#move = playerMove(board)



 #---------------------------------------------------------      
 #define_valid_directions(move), only posiible win combiantions of filed for definex 'size' and 'fields_to_win' values
def validate_moves(): 
    #define_valid_directions(move)   #receive current state of board after each player's move

         #prepare structures for possible win combinations based on defined 'fields_to_win' value, may be variable 
    for valid in cols:
        if len(valid) >= fields_to_win :
            valid_verticals.append(valid)

    for valid in rows:
        if len(valid) >= fields_to_win :
            valid_horizontals.append(valid)

    for valid in leftToRightDiagonal:
        if len(valid) >= fields_to_win :
            valid_leftToRightDiagonal.append(valid)

    for valid in rightToLeftDiagonal:
        if len(valid) >= fields_to_win :
            valid_rightToLeftDiagonal.append(valid)

    #return valid_verticals, valid_horizontals, valid_leftToRightDiagonal, valid_rightToLeftDiagonal

#---------------------------------------------------
#define_win_combinations_map

temp_res = list() #prepare structure to store interim results

def define_win_combinations_map(list):
    for comb in list:
        if len(comb) >= fields_to_win:

             for i, item in enumerate(comb):                      # valid win combinations should be chunks 
                if len(comb[i:i+fields_to_win]) == fields_to_win: # with length of defined 'fields_to_win'
                    temp_res.append(comb[i:i+fields_to_win]) 
        
#valid_verticals, valid_horizontals, valid_leftToRightDiagonal ,valid_rightToLeftDiagonal  = define_valid_directions(choices_board)

def boards_status():
    define_win_combinations_map(valid_verticals)
    define_win_combinations_map(valid_horizontals)
    define_win_combinations_map(valid_leftToRightDiagonal)
    define_win_combinations_map(valid_rightToLeftDiagonal)


#------------------------------------------------------
#compare current board with winning combinations

def checkTotalTurns(fields_combination): 
    choice_results = 0
    for choice_map in fields_combination:
        
        for choice in choice_map:
            choice_results += choice
            #print(choice_results)
        if choice_results == fields_to_win:
            #print(choice_results, fields_to_win)
            #return print("Winner is player 'X' !")   
            return "Winner is player 'X' !"               
        elif choice_results == -fields_to_win:
            #print(choice_results, fields_to_win)
            return print("Winner is player '0' !")               
        else:
            choice_results = 0
        #choice_results = 0


#checkTotalTurns(temp_res)

#--------------------------------------
#play Game
def playGame():
    finished = False
    player = 1  #define Player: 1 = 'X'/ 2 = 'O'
    define_valid_directions(choices_board)
    while not finished:
        render_board()                  # print board with current state after previous move
        playerMove(board)               # make another player move (set value to board on empty field)
        validate_moves()
        boards_status()
        win = checkTotalTurns(temp_res)
        if win:       # check for win/end, set finished accordingly
            finished = True         
        player = 3 - player             # switch players 1/2
    
playGame()