import itertools
import re 
import os
from collections import Counter, OrderedDict
#from os import path
from datetime import datetime

file_to_read = "words.txt"

class FileException(Exception):

    def __init__(self, datasource):
       
        if not os.path.exists(datasource):
            Exception.__init__(self, "File '" + datasource + "' doesn't exist under the defined path!")
        elif not datasource.lower().endswith('.txt'):
            Exception.__init__(self, 'Wrong file format, file is not ".txt" !')
        elif (os.stat(datasource).st_size == 0):
            #print(datasource.name)
            Exception.__init__(self,'File is empty!')

            



class Hangman():
    
    #access file needed to be processed
    def __init__(self, textfile):    
        
        self.textfile = textfile

    def __enter__(self):

        if os.path.exists(self.textfile):
            if not self.textfile.lower().endswith('.txt'):
                raise FileException(self.textfile)
            elif (os.stat(self.textfile).st_size == 0):
                raise FileException(self.textfile)
            else:
                self.datasource = open(self.textfile, "r")
        else:
            raise FileException(self.textfile)

        return self


    #Print resuls without putting into result file
    def get_data(self):

        #get data from file
        text = self.datasource.read()

        #if file is not empty check text using defined patter
        if text is not None:
            #words_list = text.split()
            words_list = str(text)
        else:
            print('No text found!')
            raise FileException(self.textfile)

        #return result as list 
        print(words_list)
        return words_list #dict(OrderedDict(sorted(Counter(words).items(), key=lambda t: t[0])))

    # close the file after reading
    def __exit__(self, exc_type, exc_value, traceback):
        result = self.datasource.__exit__(exc_type, exc_value, traceback)
        self.datasource.close()
        #print("__exit__")
        return result
    

        
# pass "file_name.txt" and type of result "on_screen"/"in_file"
def main(file, result_type = None):
    #hangman_words.get_data()
    get_data()
    return None 



        
    #print(result)

if __name__ == "__main__": 
    #filename = input("Enter file name to check words: ") 
    filename = file_to_read
    
    #with Hangman(filename) as hangman_words:
    #    main(filename)

    main(filename)