
positions_groups = (
    [
        [(x, y) for y in range(5)] for x in range(5)
        ] + # horizontals
    [
        [(x, y) for x in range(5)] for y in range(5)
        ] + # verticals
    [
        [(d, d) for d in range(5)]
        ] + # diagonal from top-left to bottom-right
    [
        [(2-d, d) for d in range(5)]
        ] # diagonal from top-right to bottom-left
)
def get_winner(board):
    """Return winner piece in board (None if no winner)."""
    for positions in positions_groups:
        values = [board[x][y] for (x, y) in positions]
        print(positions)
        print(values)
        if len(set(values)) == 1 and values[0]:
            return values[0]

for group in positions_groups:
    print(group)
    print("------")

board = [
    ["X", "X", "O", "X", "O"],
    ["O", "0", "X", "X", "O"],
    ["x", "X", "O", "O", "x"],
    ["O", "O", "X", "O", "O"],
    ["x", "O", "O", "X", "O"]
]

for group in positions_groups:
    values = [board[x][y] for (x, y) in group]
    print(group)
    print(values)
    print(len(set(values)))
    print(values[0])
    #if len(set(values)) == 1 and values[0]:
    #    print(len(set(values)))
    #    print(values[0])
        #return values[0]

#for group in positions_groups:
#    #print(group)
#    for row, col in group:
#        print(group[row], group[col])
#    #print(group[row][col])    
##print(get_winner(board)) # "X"

