vertical = '|  ?  |'
horizontal = ' _____ '

def draw_raw(board_size):
        print(horizontal * board_size)
        print(vertical * board_size)
        #print(vertical * board_size)


def draw_visual_board(board_size, size = 0):

    while size < board_size:
        draw_raw(board_size) 
        size += 1
       
    print(horizontal * board_size)

def placer(plane, choice, side):		#function to place user's choice on the field
    splitSide1, splitSide2 = choice[0], choice[1]
    if side == "X":
        sider=1
    elif side == "O":
        sider=-1
    plane[splitSide1][splitSide2] = sider
    return plane

    

def printer(plane):		                    #function to print out the current board
    for w in range(len(plane)):
        for e in range(len(plane)):
            if plane[w][e]== 1:
                print('{:>3}'.format('X'), end="")
            elif plane[w][e] == -1:
                print('{:>3}'.format('O'), end="")
            elif plane[w][e] == 0:
                print('{:>3d}'.format((len(plane)*w+e)), end="")
        print("")
    

def main():  
    draw_visual_board(5)
    
    plane=[]
    for g in range(5):               #create initial (empty) 2-Dimensional array with user-chosen size
        plane.append([0]*5)

    #printer(plane)
    for w in range(len(plane)):
        #print("w --> ", w)
        for e in range(len(plane)):
            #print("e --> ", e)
            if plane[w][e]== 1:
                print(format('X'), end="")
            elif plane[w][e] == -1:
                print(format('O'), end="")
            elif plane[w][e] == 0:
                print(format((len(plane)*w+e)), end="")


if __name__ == "__main__":
    main()


