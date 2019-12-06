import itertools
import re
from os import path

words = []
resultDict = {}


    #1 open  file with text
FilePath = "Text.txt"
source = open(FilePath, "r")

def tokenize():
    if source is not None:
        text = (" ".join(re.findall("[a-z\']+", source.read().lower())))
        return text
    else:
        return None


#close the file after reading
source.close()


def map_book(text):
    hash_map = {}

    if text is not None:
        for element in text:
            # Remove Punctuation
            word = element.replace(",","")
            word = word.replace(".","")

            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None






# Create a Hash Map (Dictionary)
map = map_book(words)

# Show Word Information
for word in word_list:
    print('Word: [' + word + '] Frequency: ' + str(map[word]))




def main():
    doc = myReport()
    doc.get_report(source)
    #doc.get_JSON(csvFilePath, target)

if __name__ == "__main__":
    main()

