import time
import sys
import random
from collections import Counter

import hangman_readFile


'''

wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', 'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny'
, 'tenacious', 'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell', 'pique', 'paradigm'
, 'oxymoron', 'optimistically', 'nostalgic', 'narrative', 'misanthrope', 'melancholy', 'lucid', 'lethargic', 'ken'
, 'karma', 'jurisdiction', 'jejune', 'irony', 'integrity', 'hypnosis', 'hyperbole', 'guise', 'gallivant', 'fortitude']
'''

#wordlist = str(open( "words.txt", "r").read())
#print(wordlist)


def get_words(filename):
    wordlist = str(open(filename, "r").read())
    #print("wordlist ", wordlist)
    print(random.choice(wordlist.strip('\s')))
    return wordlist
#for word in wordlist:

    #if word.isalpha() == True:
    #    print("All characters are alphabets")
    #else:
    #    print("All characters are not alphabets.")

    #print(len(word.strip('')))

    


'''
guess_try = ''
failed = 0
guesses = 10
while guesses > 0:
    pass
    if guesses == 1:
        print("You have last try left...!")
    elif guesses == 1:
        print("Out of tries, you;ve lost!")
        failed = 1
    else:
        if guess_try == word:
            print("Correct, you've suess the word!")
        else:
            print("Nope, it's not that word! Try once more...")
'''



def choose_word(wordlist):
    #randomize = input("Do you want to choose word by yourself or select a word randmoly? Choose / Random...")
    randomize = 'Random'
    if randomize == 'Choose':
        word_to_guess =  input("Choose the word from to be guessed from a list")
    elif randomize == 'Random':
        word_to_guess = random.choice(wordlist)
        print("Word to guess is :", word_to_guess)
    return word_to_guess
    
def pick_up_letter(wordlist):
    letters_freq = Counter(wordlist.lower()) #.most_common()
    #letters_freq = Counter(text)
    print("letters_freq: ", letters_freq)

    for char, freq in letters_freq.items():
        if char.isalpha():
            #print(char, freq )
            letter = char
    print("pick_up_letter: ", letter)
    return letter

#pick_up_letter()
def letter_appearance(word_to_guess, letter):
    #letter_approval = input("Is there a letter '%s' in a word? Y / N..." % (letter))
    letter_approval = 'N'
    
    word_letters = word_to_guess.split()
    print("word_letters ", word_letters)

    if letter_approval == 'Y':
        pass
    elif letter_approval == 'N':
        pass
    else:
        raise ValueError
    
    return letter_approval

def draw_mask(word_to_guess):
    letters_num = len(word_to_guess)
    #print(letters)
    word_placeholder = [' __' for letter in range(letters_num)]
    #if letter_approval

    mask = '\n' + ' '.join(word_placeholder) + '\n'
    #print(mask)
    return mask

    #mask_animation = "__ "
    #for i in range(100):
    #    time.sleep(0.1)
    #    sys.stdout.write("\r" + mask[i % len(mask)])
    #    sys.stdout.flush()
    #print("End!")

def main():
    words = get_words("words.txt")
    word_to_guess = choose_word(words)
    letter = pick_up_letter(words)
    letter_appearance(word_to_guess, letter)
    draw_mask(word_to_guess)
main()  

