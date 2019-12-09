import itertools
import re
from collections import Counter, OrderedDict
from os import path

class FileFormatException(Exception):

    def __init__(self, datasource):
        #self.datasource = datasource
        if not path.exists(datasource):
            raise FileNotFoundError("File '" + datasource + "' doesn't exist under the defined path!")
        #elif not datasource.lower().endswith('.txt'):
        #   print('Wrong file format, file is not ".txt" !')
        elif open(datasource, "r").getsize() == 0:
            print('File is empty!')

            



class FrequencyCheck():
    
    #access file needed to be processed
    def __init__(self, textfile):    
        
        self.textfile = textfile

        if path.exists(self.textfile):
            if not self.textfile.lower().endswith('.txt'):
                raise FileFormatException(self.textfile)
            else:
                self.datasource = open(self.textfile, "r")
        else:
            raise FileFormatException(self.textfile)


    #@classmethod
    def get_freq(self, pattern = None):
        
        #use default check pattern or add explicitly
        if pattern is None:
            self.pattern = re.compile(r'([\w\'+]+\w)')
        else:
            self.pattern = re.compile(r'' + pattern)

        #get data from gile
        text = self.datasource.read()

        #if file is not empty check text using defined patter
        if text is not None:
            words = re.findall(self.pattern, text.lower()) 
        else:
            print('No text found!')
            raise FileFormatException(self.textfile)

        #return result as dictionary {"word": freq_count} sorted alphabetically
        return dict(OrderedDict(sorted(Counter(words).items(), key=lambda t: t[0])))
        

    #Put result into resultfile
    def get_freq_file(self):
        
        result_file = "Frequency_check_" + self.textfile + str(path.getatime()) + ".txt"
        frequency = open(result_file,"w+")
        for item in result:
            frequency.write(str(item) + "\n")
        frequency.close()


    # close the file after reading
    def __exit__(self):
        self.datasource.close()
    

        

def main():
    doc = FrequencyCheck("xxx.docx")
    result = doc.get_freq()

    print(result)

if __name__ == "__main__":
    main()

