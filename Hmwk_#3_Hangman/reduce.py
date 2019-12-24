import functools
import random
from functools import reduce

'''
wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', 'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny'
, 'tenacious', 'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell', 'pique', 'paradigm'
, 'oxymoron', 'optimistically', 'nostalgic', 'narrative', 'misanthrope', 'melancholy', 'lucid', 'lethargic', 'ken'
, 'karma', 'jurisdiction', 'jejune', 'irony', 'integrity', 'hypnosis', 'hyperbole', 'guise', 'gallivant', 'fortitude']
'''

#wordlist = str(open("words.txt", "r").readlines())
#print(wordlist)
wordlist = [word.strip().lower() for word in open("words.txt", "r").readlines()]
#print(wordlist)



stripped = ["aaa", "bbb"]
print(stripped)
def check_alpha(wordlist):
#    for word in wordlist:
#        #if word.isalpha() == True:
#        stripped.append(word)

#print(stripped)
    #lambda wordlist, word : [print('xxx') if word.isalpha() == True else None for word in wordlist]
    #functools.reduce(lambda wordlist, word : [stripped.append(word) if word.isalpha() == True else None for word in wordlist], wordlist)
#functools.reduce(check_alpha(wordlist), wordlist)


    return lambda wordlist : [stripped.append(word) if word.isalpha() == True else None for word in wordlist]
#check = doc(wordlist)
print(stripped)

check_alpha(wordlist)
'''
def mult(words):
    #print("x=",x," y=",y)
    #return (x * y)
    words.strip('')

fact = functools.reduce(mult, range(1, 6))
print ('Factorial of 3: ', fact)
'''