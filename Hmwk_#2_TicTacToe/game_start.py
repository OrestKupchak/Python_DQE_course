import random
import board 

class Game():

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Starting new game!')
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

    def newGameStart(self):
        board.main()

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (Y / N)')
        return input().upper().startswith('Y')



def main():
    new_game = Game()
    new_game.inputPlayerLetter()
    new_game.whoGoesFirst()
    new_game.newGameStart()


    if new_game.playAgain():
        main()
    else:
        return "Game over!"
    

if __name__ == "__main__":
    main()