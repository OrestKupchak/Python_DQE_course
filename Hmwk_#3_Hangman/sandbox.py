import functools
import random
from functools import reduce


#letter_approval = ''
#letter = 'e'
#word_to_guess = 'elephant'
#word_placeholder = [' __' for letter in range(len(word_to_guess))]

#a = [ch for ch in word_to_guess]
#letter_indices = [i for i, e in enumerate(a) if e == letter]
#for i in letter_indices:
#    word_placeholder[i] = letter
#print(word_placeholder)



def get_words(filename):
    text = open(filename, "r", encoding="utf-8")#.read()
    #print(text)
    return text


def guess_counter(guesses):
    #word_guess_try = guesses
    #failed = 0
    
    #while guesses <= 10:
    if guesses == 9:
        print("You have last try left...!")
    elif guesses == 10:
        print("Out of tries, you;ve lost!")
        #return guesses
    #else:
    #    if word_guess_try == letter:
    #        print("Correct, you've guessed the letter!")
    #    else:
    #        print("Nope, there's no such letter in that word! Try again...")
    #guesses += 1
    #print(guesses)
    return guesses

def choose_word(text):
    words = text
    #print("words",words )
    #randomize = input("Do you want to choose word by yourself or select a word randmoly? Choose / Random...")
    wordlist = [word.lower().strip() for word in words.readlines()]

    randomize = 'Random'
    if randomize == 'Choose':
        word_to_guess =  input("Choose the word from to be guessed from a list")
    elif randomize == 'Random':
        word_to_guess = random.choice(wordlist)
        #print("Word to guess is :", word_to_guess)
    return word_to_guess

def counter(letter_freq, char):
    if char.isalpha() == True:
        letter_freq[char] = letter_freq.get(char, 0) + 1
    return letter_freq

def get_letter_freq(text):
    text.seek(0) #go to beginning if the file to avoid reopening
    characters = text.read()
    #print("characters ",characters)
    #print("reduce (counter, text, {})", reduce (counter, characters, {}))
    return reduce (counter, characters, {})
    
def pick_up_letter(letters_freq):
    letter = ''
    #print("letters_freq: ", letters_freq)
    most_frequent = {k: v for k, v in sorted(letters_freq.items(), key=lambda item: item[1])}
    #print("most_frequent: ", most_frequent)
    for char, freq in most_frequent.items():
       
            #print(char, freq ) #
        letter = char
        #print("pick_up_letter: ", letter, "freq: ", freq )
    return letter


def letter_appearance(word_to_guess, letter_approval):
    letter_approval = input("Is there a letter '%s' in a word? Y / N..." % (letter))
    #letter_approval = 'N'
    word_letters = set([ch for ch in word_to_guess])
    #print("word_letters ", word_letters)

    if letter in word_letters:
        letter_approval ='Y'    
        print("Correct, you've guessed the letter!")
    elif letter not in word_letters:
        letter_approval = 'N'
        print("Nope, there's no such letter in that word! Try again...")
    else:
        raise ValueError("What?")
    return letter_approval


def initial_mask(word_to_guess):
    letters_num = len(word_to_guess)
    word_placeholder = [' __' for letter in range(letters_num)]
    return word_placeholder


def draw_mask(word_to_guess, letter_approval, guesses, placeholder):
    #letters_num = len(word_to_guess)
    #print(letters)
    #if guesses == 0:
    #    word_placeholder = [' __' for letter in range(letters_num)]
        #print("initial placeholder", word_placeholder)
    #else:
    word_placeholder = placeholder
    print(word_placeholder)
    letters_to_guess = [letter for letter in word_to_guess]
    if letter_approval == 'Y':
        letter_indices = [ind for ind, character in enumerate(letters_to_guess) if character == letter]
        for i in letter_indices:
            #print("i", i, "word_placeholder", word_placeholder, "word_placeholder[i]", word_placeholder[i])
            word_placeholder[i] = ' ' + letter + ' '
        #print(word_placeholder) 
    mask = '\n' + ' '.join(word_placeholder) + '\n'
    print("mask ", mask)
    return word_placeholder


words = get_words("dummy.txt")
characters = words
word_to_guess = choose_word(words)
letter_freq = get_letter_freq(characters) #read ???
#print("letter_freq ",letter_freq)
guesses = 0
word_placeholder = initial_mask(word_to_guess)
print('\n' + ' '.join(word_placeholder) + '\n')
while guesses <= 10:
    print("word_to_guess ",word_to_guess)
   
    letter = pick_up_letter(letter_freq)
    print("letter ",letter)
    letter_approval = letter_appearance(word_to_guess, letter)
    #print("letter_approval", letter_approval)
    #if letter_approval == 'N':
    letter_freq.pop(letter) #remove letter from try list
    #else :
    guesses = guess_counter(guesses)
    
#print("letter_approval", letter_approval)
    draw_mask(word_to_guess, letter_approval, guesses, word_placeholder)
    guesses += 1
