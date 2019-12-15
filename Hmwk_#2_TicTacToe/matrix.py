board = [
        [17, 15, 1,  2,  3],
        [75, 53, 4,  5,  6],
        [71, 45, 7,  8,  9],
        [27, 25, 10, 11, 12],
        [37, 55, 9,  1,  1],
        ]
#board = [
#        [1,  2,  3],
#        [4,  5,  6],
#        [7,  8,  9]
#        ]

max_col = len(board[0]) #5
max_row = len(board)    #5


cols = [ list() for elements in range(max_col)]
rows = [ list()  for elements in range(max_row)]


leftToRightDiagonal = [ list() for elements in range(max_row + max_col - 1)]
rightToLeftDiagonal = [ list() for elements in range(len(leftToRightDiagonal))]

#print(leftToRightDiagonal)
#print(rightToLeftDiagonal)
min_rightToLeftDiagonal = -max_row + 1
#print(min_rightToLeftDiagonal)
for row in board:
    print(row)
for x in range(max_col):
    print('\n' +"x :", x)
    for y in range(max_row):
        print( "y, x ->", y, ',', x, "------> board[y][x] :", board[y][x])
#       cols[x].append(board[y][x])
#       rows[y].append(board[y][x])
        #if len(board[y][x]) >= 3:
        leftToRightDiagonal[x+y].append(board[y][x])
        print(leftToRightDiagonal)
        rightToLeftDiagonal[x-y-min_rightToLeftDiagonal].append(board[y][x])
    #print(leftToRightDiagonal)
#print(cols)
#print(rows)
print(leftToRightDiagonal)
#print(rightToLeftDiagonal)
valid_leftToRightDiagonal = []
for valid in leftToRightDiagonal:
    if len(valid) == 4 :
        valid_leftToRightDiagonal.append(valid)

valid_rightToLeftDiagonal = []
for valid in rightToLeftDiagonal:
    if len(valid) == 4 :
        valid_rightToLeftDiagonal.append(valid)

print(valid_leftToRightDiagonal)
print(valid_rightToLeftDiagonal)