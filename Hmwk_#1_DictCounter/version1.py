import itertools
import re
from collections import Counter, OrderedDict
from os import path



class FrequencyCheck():

    #access file needed to be processed
    def __init__(self, textfile):
        self.datasource = open(textfile, "r")


    #@classmethod
    def get_freq(self):
        text = self.datasource.read()
        if text is not None:
            words = re.findall(r'\w+', text.lower())
        else:
            return None

        return dict(OrderedDict(sorted(Counter(words).items(), key=lambda t: t[0])))
        #print(result)

    # close the file after reading
    def __exit__(self):
        self.datasource.close()
    

        


    
    ##Put result into resultfile
        #frequency = open("Frequency.txt","w+")
        #for item in result:
        #    frequency.write(str(item) + "\n")
        #frequency.close()



def main():
    doc = FrequencyCheck("dummy.txt")
    result = doc.get_freq()
    #doc.get_JSON(csvFilePath, target)
    print(result)

if __name__ == "__main__":
    main()

