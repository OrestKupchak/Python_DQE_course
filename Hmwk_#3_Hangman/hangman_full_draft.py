import time
import sys
import random
from collections import Counter
from functools import reduce

'''
1. Let the player pick a word from the file attached to the letter (words.txt).
2. The program guesses based on the player's answers.
3. On the first move we show the number of letters in the word.
4. Application  analyzes the list available to it and offers the most likely letter (you can display the percentage of probability AND/OR the number of words from which to choose).
5. If the player agrees with the choice, then he/she writes out a word with letters in the correct positions.
6. If you do not agree, then the application gives the next option.… and so on.
 
7. When the word is guessed - print the word and the number of attempts.

'''


def get_words(filename):
    text = open(filename, "r", encoding="utf-8")#.read()
    #print(text)
    return text


def guess_counter(word):
    word_guess_try = ''
    failed = 0
    guesses = 0
    while guesses <= 10:
        pass
        if guesses == 9:
            print("You have last try left...!")
        elif guesses == 10:
            print("Out of tries, you;ve lost!")
            failed = 1
        else:
            if word_guess_try == word:
                print("Correct, you've suess the word!")
            else:
                print("Nope, it's not that word! Try once more...")
    return guesses
 
def choose_word(text):
    words = text
    #print("words",words )
    #randomize = input("Do you want to choose word by yourself or select a word randmoly? Choose / Random...")
    wordlist = [word.lower().strip() for word in words.readlines()]
    randomize = 'Random' #remove later

    if randomize == 'Choose':
        word_to_guess =  input("Choose the word from to be guessed from a list")
    elif randomize == 'Random':
        word_to_guess = random.choice(wordlist)
    return word_to_guess
#------------------------------------------------------------------------
def counter(letter_freq, char):
    if char.isalpha() == True:
        letter_freq[char] = letter_freq.get(char, 0) + 1
    freq_sorted = sorted(letter_freq.items(), key=lambda x: x[1])
    return freq_sorted

def get_letter_freq(text):
    text.seek(0) #go to beginning if the file to avoid reopening
    characters = text.read()
    return reduce (counter, characters, {})
#------------------------------------------------------------------------    
def pick_up_letter(letters_freq):
    letter = ''

    for char, freq in letters_freq.items():
            letter = char
    return letter

def letter_appearance(word_to_guess, letter):
    #letter_approval = input("Is there a letter '%s' in a word? Y / N..." % (letter))
    letter_approval = 'N' #remove later
    word_letters = word_to_guess.split()
    if letter_approval == 'Y':
        pass
    elif letter_approval == 'N':
        pass
    else:
        raise ValueError
    
    return letter_approval

def draw_mask(word_to_guess):
    letters_num = len(word_to_guess)
    word_placeholder = [' __' for letter in range(letters_num)]
    mask = '\n' + ' '.join(word_placeholder) + '\n'
    print(mask)
    return mask




def main():
    words = get_words("dummy.txt")
    characters = words
    word_to_guess = choose_word(words)
    letter_freq = get_letter_freq(characters) 
    letter = pick_up_letter(letter_freq)
    letter_appearance(word_to_guess, letter)
    draw_mask(word_to_guess)
    guess = guess_counter()
main()  

