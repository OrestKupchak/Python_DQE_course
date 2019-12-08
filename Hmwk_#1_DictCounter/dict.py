import itertools
import re
from collections import Counter, OrderedDict
from os import path

class FileFormatException():

    def __init__(self, datasource):
        #self.datasource = datasource
        if not datasource.lower().endswith('.txt'):
            print('Wrong file extension, file is not ".txt" !')
        elif open(datasource, "r").getsize() == 0:
            print('File is empty!')
        else:
            print('File with given name doesn\'t exist !')



class FrequencyCheck():

    #access file needed to be processed
    def __init__(self, textfile):    
        if path.exists(textfile):
            if not textfile.lower().endswith('.txt'):
                raise FileFormatException(textfile)
            else:
                self.datasource = open(textfile, "r")
        else:
            raise FileFormatException(textfile)



    #@classmethod
    def get_freq(self):
        text = self.datasource.read()
        if text is not None:
            words = re.findall(r'\w+', text.lower())
        else:
            return None
        return dict(OrderedDict(sorted(Counter(words).items(), key=lambda t: t[0])))
        #print(result)

    def get_freq_file(self):
        #Put result into resultfile
        result_file = "Frequency_check_" + textfile + str(path.getatime()) + ".txt"
        frequency = open(result_file,"w+")
        for item in result:
            frequency.write(str(item) + "\n")
        frequency.close()


    # close the file after reading
    def __exit__(self):
        self.datasource.close()
    

        

def main():
    doc = FrequencyCheck("xxx.txt")
    result = doc.get_freq()
    #doc.get_JSON(csvFilePath, target)
    print(result)

if __name__ == "__main__":
    main()

