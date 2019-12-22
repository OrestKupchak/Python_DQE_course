#from graphics import *



wordlist = ['zenith', 'zealot', 'yearn', 'yawner', 'xenophobia', 'x-axis', 'wonky', 'wanton', 'vermillion', 'vague', 'unique', 'uncanny'
, 'tenacious', 'tangible', 'serene', 'saquinavir', 'rhetorical', 'rambunctious', 'quixotic', 'quell', 'pique', 'paradigm'
, 'oxymoron', 'optimistically', 'nostalgic', 'narrative', 'misanthrope', 'melancholy', 'lucid', 'lethargic', 'ken'
, 'karma', 'jurisdiction', 'jejune', 'irony', 'integrity', 'hypnosis', 'hyperbole', 'guise', 'gallivant', 'fortitude']

#for word in wordlist:
#    if word.isalpha() == True:
#        print("All characters are alphabets")
#    else:
#        print("All characters are not alphabets.")
#    print(len(word.strip('')))


#word_len_request = True
#while word_len_request == True:
#
#    word_len = 
#    response = input("Is this a {} letter(s) word? Y / N ...")

word = 'jurisdiction'
letters = len(word)

'''
mask_animation = "__ "

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + mask_animation[i % len(animation)])
    sys.stdout.flush()
print("End!")
'''


man = '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========
 '''

#hang_parts = ['   +---+', '   |   |',  '       |', '       |', '       |', '       |', ' =========']
#man_parts =  ['   +---+', '   |   |',  '   O   |', '   |   |', '  /|   |', '  /|\  |', '  /    |','  / \  |','       |',' =========']

parts = [['   +---+', '   +---+'], 
         ['   |   |', '   |   |'],
         ['       |', '   O   |'],
         ['       |', '   |   |'],
         ['       |', '  /|   |'],
         ['',         '  /|\  |'],
         ['       |', '  /    |'],
         ['       |','  / \  |'],
         ['       |','       |'], 
         [' =========',' =========']
         ]

letter = 'd'
guess_try = 's'


for part in range(len(parts)):
    #if guess_try != letter:
    #    print(part[0])
    #else:
    #    print(part[1])
    print(part)





word = 'jurisdiction'
letters = len(word)
#print(letters)
word_placeholder = [' __' for letter in range(letters)]
mask = ' '.join([' __' for letter in range(letters)]) 
print('\n' + mask + '\n')
