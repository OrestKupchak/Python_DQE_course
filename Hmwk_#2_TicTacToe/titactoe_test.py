class Board():

    vertical = '|    |'
    horizontal = ' ____ '

    def draw_raw(self, board_size):

        vertical = self.vertical
        horizontal = self.horizontal

        print(horizontal*board_size)
        print(vertical *(board_size))
        print(vertical *(board_size))

    def draw_board(self, board_size, size = 0):
        self.board_size = board_size
        while size < self.board_size:
            self.draw_raw(self.board_size) 
            size += 1
            #print(size)
        print(self.horizontal * self.board_size)


    

def main():
    brd = Board()
    print(brd.draw_board(10))

if __name__ == "__main__":
    main()