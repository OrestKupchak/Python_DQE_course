import time
import sys
import random
from collections import Counter






wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', 'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny'
, 'tenacious', 'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell', 'pique', 'paradigm'
, 'oxymoron', 'optimistically', 'nostalgic', 'narrative', 'misanthrope', 'melancholy', 'lucid', 'lethargic', 'ken'
, 'karma', 'jurisdiction', 'jejune', 'irony', 'integrity', 'hypnosis', 'hyperbole', 'guise', 'gallivant', 'fortitude']

#for word in wordlist:

    #if word.isalpha() == True:
    #    print("All characters are alphabets")
    #else:
    #    print("All characters are not alphabets.")

    #print(len(word.strip('')))


#word_len_request = True
#while word_len_request = True:
#
#    word_len = 
#    response = input("Is this a {} letter(s) word? Y / N ...")

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



def choose_word():
    #randomize = input("Do you want to choose word by yourself or select a word randmoly? Choose / Random...")
    randomize = 'Random'
    if randomize == 'Choose':
        word_to_guess =  input("Choose the word from to be guessed from a list")
    elif randomize == 'Random':
        word_to_guess = random.choice(wordlist)
        print("Word to guess is :", word_to_guess)
    return word_to_guess
    
def pick_up_letter():
    letters_freq = Counter(open( "dummy.txt", "r").read()) #.most_common()
    #letters_freq = Counter(text)
    #print(letters_freq)

    for char, freq in letters_freq.items():
        if char.isalpha():
            #print(char, freq )
            letter = char
    print("pick_up_letter: ", letter)
    return letter

#pick_up_letter()
def letter_appearance(letter):
    letter_approval = input("Is there a letter '%s' in a word? Y / N..." % (letter))
    
    if letter_approval == 'Y':
        pass
    elif letter_approval == 'N':
        pass
    else:
        raise ValueError
    
    return letter_approval

def draw_mask(word_to_guess, letter_approval):
    letters_num = len(word_to_guess)
    #print(letters)
    word_placeholder = [' __' for letter in range(letters_num)]
    if letter_approval

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
    word_to_guess = choose_word()
    letter = pick_up_letter()
    letter_appearance(letter)
    draw_mask(word_to_guess)
main()  

