import functools
import random
from functools import reduce


letter_approval = ''
letter = 'e'
word_to_guess = 'elephant'
word_placeholder = [' __' for letter in range(len(word_to_guess))]

#a = [ch for ch in word_to_guess]
#letter_indices = [i for i, e in enumerate(a) if e == letter]
#for i in letter_indices:
#    word_placeholder[i] = letter
#print(word_placeholder)

def guess_counter(letter):
    word_guess_try = ''
    failed = 0
    guesses = 0
    #while guesses <= 10:
    if guesses == 9:
        print("You have last try left...!")
    elif guesses == 10:
        print("Out of tries, you;ve lost!")
        failed = 1
        return
    else:
        if word_guess_try == letter:
            print("Correct, you've suess the word!")
        else:
            print("Nope, it's not that word! Try once more...")
    guesses += 1
    return guesses

def letter_appearance(word_to_guess, letter_approval):
    #letter_approval = input("Is there a letter '%s' in a word? Y / N..." % (letter))
    letter_approval = 'N'
    word_letters = set([ch for ch in word_to_guess])
    #print("word_letters ", word_letters)

    if letter in word_letters:
        letter_approval ='Y'    
    elif letter not in word_letters:
        letter_approval = 'N'
    else:
        raise ValueError
    
    return letter_approval


def draw_mask(word_to_guess, letter_approval, guesses):
    letters_num = len(word_to_guess)
    #print(letters)
    if guesses == 0:
        word_placeholder = [' __' for letter in range(letters_num)]
    else:
        letters_to_guess = [letter for letter in word_to_guess]
        if letter_approval == 'Y':
            letter_indices = [ind for ind, character in enumerate(letters_to_guess) if character == letter]
            for i in letter_indices:
                word_placeholder[i] = letter
            #print(word_placeholder) 
    mask = '\n' + ' '.join(word_placeholder) + '\n'
    print(mask)
    return mask

while failed != 1:
    guesses = guess_counter(letter)
letter_approval = letter_appearance(word_to_guess, letter)
#print("letter_approval", letter_approval)
draw_mask(word_to_guess, letter_approval)
    
