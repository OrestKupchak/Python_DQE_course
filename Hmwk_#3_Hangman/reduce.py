import functools
import random
from functools import reduce


wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', 'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny'
, 'tenacious', 'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell', 'pique', 'paradigm'
, 'oxymoron', 'optimistically', 'nostalgic', 'narrative', 'misanthrope', 'melancholy', 'lucid', 'lethargic', 'ken'
, 'karma', 'jurisdiction', 'jejune', 'irony', 'integrity', 'hypnosis', 'hyperbole', 'guise', 'gallivant', 'fortitude']

def check_alpha(wordlist):
    for word in wordlist:
        if word.isalpha() == True:
            wordlist.append(word)

stripped = []


print(reduce(check_alpha(wordlist), wordlist))

'''
def mult(words):
    #print("x=",x," y=",y)
    #return (x * y)
    words.strip('')

fact = functools.reduce(mult, range(1, 6))
print ('Factorial of 3: ', fact)
'''