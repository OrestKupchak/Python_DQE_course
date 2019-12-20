import time
import sys

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

word = 'jurisdiction'
letters = len(word)
#print(letters)
word_placeholder = [' __' for letter in range(letters)]
mask = ' '.join([' __' for letter in range(letters)]) 
print('\n' + mask + '\n')



