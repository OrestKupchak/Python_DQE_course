
def board(size, ):
    brd = []
    cells =  [0 for x in range(size+1)]
    if size >= 3:
        for row in range(size+1):
            brd.append(cells)
    else:
        return "Board should be at lease 3x3 cells size!"

    for row in brd:
        print(row)
    return brd


board = [[17,15,1,2,3],
        [75,53,4,5,6],
        [71,45,7,8,9],
        [27,25,10,11,12],
        [37,55,9,1,1],
        ]

max_col = len(board[0])
max_row = len(board)


cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(board[y][x])
        rows[y].append(board[y][x])
        fdiag[x+y].append(board[y][x])
        bdiag[x-y-min_bdiag].append(board[y][x])

print(cols)
#print(rows)
#print(fdiag)
#print(bdiag)

#dummy_board = [
#    ["X", "X", "O", "X", "O"],
#    ["O", "0", "X", "X", "O"],
#    ["x", "X", "O", "O", "x"],
#    ["O", "O", "X", "O", "O"],
#    ["x", "O", "O", "X", "O"]
#]



#a = [x for x in range(5)]
#b = (x for x in range(5))
#c = tuple(range(5))
