fields_to_win = 3

board = [
        [17, 15, 1,  2,  3],
        [75, 53, 4,  5,  6],
        [71, 45, 7,  8,  9],
        [27, 25, 10, 11, 12],
        [37, 55, 9,  1,  1],
        ]

max_col = len(board[0]) #5
max_row = len(board)    #5

cols = [ list() for elements in range(max_col)]
rows = [ list()  for elements in range(max_row)]

leftToRightDiagonal = [ list() for elements in range(max_row + max_col - 1)]
rightToLeftDiagonal = [ list() for elements in range(len(leftToRightDiagonal))]


min_rightToLeftDiagonal = -max_row + 1

for row in board:
    print(row)
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


print("---------------------------------------------------")
print(valid_verticals)
print(valid_horizontals)
print(valid_leftToRightDiagonal)
print(valid_rightToLeftDiagonal)
print("---------------------------------------------------")


#---------------------------------------------------
#combinations


temp_res = list()

def define_win_combinations_map(list):
    for comb in list:
        if len(comb) >= 3:
            #print(comb)
             for i, item in enumerate(comb): #valid win combinations should be chunks
                if len(comb[i:i+fields_to_win]) == fields_to_win: # with length of defined 'fields_to_win'
                    temp_res.append(comb[i:i+fields_to_win]) 
    #print(temp_res)            

define_win_combinations_map(valid_verticals)
define_win_combinations_map(valid_horizontals)
define_win_combinations_map(valid_leftToRightDiagonal)
define_win_combinations_map(valid_rightToLeftDiagonal)

print(temp_res)  