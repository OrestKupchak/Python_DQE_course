import itertools
import re
from collections import Counter, OrderedDict
from os import path


class FileException(Exception):

    def __init__(self, datasource):
       
        if not path.exists(datasource):
            Exception.__init__(self, "File '" + datasource + "' doesn't exist under the defined path!")
        elif not datasource.lower().endswith('.txt'):
            Exception.__init__(self, 'Wrong file format, file is not ".txt" !')
        elif open(datasource, "r").getsize() == 0:
            Exception.__init__(self,'File is empty!')

            



class FrequencyCheck():
    
    #access file needed to be processed
    def __init__(self, textfile):    
        
        self.textfile = textfile

        if path.exists(self.textfile):
            if not self.textfile.lower().endswith('.txt'):
                raise FileException(self.textfile)
            else:
                self.datasource = open(self.textfile, "r")
        else:
            raise FileException(self.textfile)

    #Put result into resultfile
    def get_freq_file(self):
        
        result_file = "Frequency_check_" + self.textfile + '_' + str(path.getatime(self.textfile)) + ".txt"
        frequency = open(result_file,"w+")
        result = self.get_freq()
        for word in result:
            frequency.write(str(result[key] + " : " + result[value] + "\n")
            #print(str(item) + "\n")
        frequency.close()



    #Print resuls without putting into result file
    def get_freq(self, pattern = None):
        
        #use default check pattern or add explicitly
        if pattern is None:
            self.pattern = re.compile(r'([\w\'+]+\w)')
        else:
            self.pattern = re.compile(r'' + pattern)

        #get data from file
        text = self.datasource.read()

        #if file is not empty check text using defined patter
        if text is not None:
            words = re.findall(self.pattern, text.lower()) 
        else:
            print('No text found!')
            raise FileException(self.textfile)

        #return result as dictionary {"word": freq_count} sorted alphabetically
        return dict(OrderedDict(sorted(Counter(words).items(), key=lambda t: t[0])))
        



    # close the file after reading
    def __exit__(self):
        self.datasource.close()
    

        

def main():
    doc = FrequencyCheck("dummy.txt")
    #result = doc.get_freq()
    doc.get_freq_file()
    #print(result)

if __name__ == "__main__":
    main()

