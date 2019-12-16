import random

class Game():

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the list is the player’s letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (Y / N)')
        return input().upper().startswith('Y')






class Board():

    #board_size = None
    _vertical = '|    |'
    _horizontal = ' ____ '
    

    def __init__(self, board_size):
        self.board_size = board_size
        
        self.draw_board(self.board_size, size = 0)


    def draw_raw(self, board_size):

        print(self._horizontal * board_size)
        print(self._vertical * board_size)
        print(self._vertical * board_size)

    def draw_board(self, board_size, size = 0):
        self.board_size = board_size
        while size < self.board_size:
            self.draw_raw(self.board_size) 
            size += 1
            #print(size)
        print(self._horizontal * self.board_size)



    

def main():
    brd = Board(6)
    print(brd.board_size)

if __name__ == "__main__":
    main()