import functools
import random
from functools import reduce
import time
import hangman_graphics

#get data from file but not read so later it can be accesed twice without reopening
def get_words(filename):
    text = open(filename, "r", encoding="utf-8")

    return text

#define mode PC vs. PC, Player vs. PC
def set_game_mode():
    game_mode = input("What type of game you wanna play? (Manual / Auto) ").lower()
    
    if game_mode == "manual":
        print("Manual game mode requires to interact with PC !")
    elif game_mode == "auto":
        print("Auto game mode allows just to watch the flow")

    return game_mode

#counter for PC tries to guess word
def guess_counter(guesses):

    if guesses == 9:
        print("You have last try left...!")
    elif guesses == 10:
        print("Out of tries, you've lost!")

    return guesses

#get word to guess from file randomly or define it manually
def choose_word(text):

    words = text
    randomize = input("Do you want to choose word by yourself or select a word randmoly? (Choose / Random)...").lower()
    wordlist = [word.lower().strip() for word in words.readlines()]

    if randomize == 'choose':
        word_to_guess =  input("Choose the word from to be guessed from a list")
    elif randomize == 'random':
        word_to_guess = random.choice(wordlist)

    return word_to_guess

#function to be used in 'reduce' to count characters frequency on fly
def counter(letter_freq, char):

    if char.isalpha() == True:
        letter_freq[char] = letter_freq.get(char, 0) + 1 #count each appearance of character and sore it as a value for 'character' key in dict
        
    return letter_freq

#wrapper function to use 'counter' for letters frequncy check
def get_letter_freq(text):

    text.seek(0) #go to beginning if the file to avoid reopening
    characters = text.read()

    return reduce (counter, characters, {}) #use 'counter'

#finction to receive letter to try to guess based on frequency, letters stored as sorted ascending dictionary
def pick_up_letter(letters_freq):

    letter = ''
    most_frequent = {k: v for k, v in sorted(letters_freq.items(), key=lambda item: item[1])} #sort ascending
    for char, freq in most_frequent.items():
        letter = char

    return letter

#chech if received letter is present in word_to_guess
def letter_appearance(game_mode, word_to_guess, letter):

    if game_mode == 'manual':
        letter_approval = input("Is there a letter '%s' in a word? (Y / N) " % (letter))
    elif game_mode == 'auto':
        word_letters = set([ch for ch in word_to_guess])
        print("PC: Is there a letter '%s' in a word? (Y / N) " % (letter))
        if letter in word_letters:
            letter_approval ='Y'    
            print("Player: ", "'", letter_approval , "'"," Correct, you've guessed the letter!", '\n')
        elif letter not in word_letters:
            letter_approval = 'N'
            print("Player: ", "'", letter_approval , "'"," Nope, there's no such letter in that word! Try again...", '\n')
    else:
        raise ValueError("Player: What? Choose coorect mode!")

    return letter_approval

#draw placeholder for word for game start
def initial_mask(word_to_guess):
    letters_num = len(word_to_guess)
    word_placeholder = [' __' for letter in range(letters_num)] #generate empty filds for letters

    return word_placeholder

#draw placeholder including guessed letter dynamically on each turn
def draw_mask(word_to_guess, letter_approval, guesses, placeholder, letter):
   
    word_placeholder = placeholder
    letters_to_guess = [letter for letter in word_to_guess]
    if letter_approval == 'Y':
        letter_indices = [ind for ind, character in enumerate(letters_to_guess) if character == letter] #receive index where guessed letter shoul be stored
        for i in letter_indices:
           
            word_placeholder[i] = ' ' + letter + ' ' #set guessed letter on it's place in the word
    mask = '\n' + ' '.join(word_placeholder) + '\n'
    print(mask)

    return word_placeholder

#run the flow
def play_game(filename):

    logo = hangman_graphics.get_logo() #add some graphics
    print(logo)
    game_mode = set_game_mode() #define mode
    image = hangman_graphics.get_image() #add graphics for each turn
    words = get_words(filename) #receive string from file
    characters = words #use string copy for letters frequency check without reopening the file
    word_to_guess = choose_word(words) #define word
    letter_freq = get_letter_freq(characters) #get dictionary of characters and their frequency

    guesses = 0 
    fail_counter = 0 #add counter to draw appropriate 'hangman' graphics if letter was guessed after a fail turn
    word_placeholder = initial_mask(word_to_guess)

    while guesses <= 10: #player have 10 tries
        print("Word to guess: ", word_to_guess)
        print("Guess try #", guesses, '\n')
        letter = pick_up_letter(letter_freq) 
        letter_approval = letter_appearance(game_mode, word_to_guess, letter) #check if letter exists in word
        letter_freq.pop(letter) # remove letters from end of dictionary (ascending sort allows to move form most frequent to lower ones)
                                # despite if it was guessed or not, letter cannot be used twice
        guesses = guess_counter(guesses)
        time.sleep(1.5) #add delay for realistic rendering
        draw_mask(word_to_guess, letter_approval, guesses, word_placeholder, letter) #render word placeholder with guessed and yet not guessed letters

        if letter_approval == "Y":
            for i in image[fail_counter]: #render previous failed 'hangman' step, failed turns shoul not rollback 
                print(i)
        elif letter_approval == "N":
            fail_counter += 1
            for i in  image[fail_counter]: #render next failed 'hangman' step, + 1 step to loss
                print(i)
        if guesses == 10 and word_placeholder != [ch for ch in word_to_guess]:
            print("You couldn't guess the word!")
        elif word_placeholder == [ch for ch in word_to_guess]:
            print("Hooray, congrats, you've guessed the word!") 
        guesses += 1
        print("=================================================")
        time.sleep(5) #add delay for realistic rendering of turns



play_game("words.txt")