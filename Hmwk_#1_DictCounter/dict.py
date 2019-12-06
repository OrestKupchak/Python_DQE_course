import itertools
import re
from os import path

words = []
resultDict = {}


    #1 open  file with text
FilePath = "Book.txt"
source = open(FilePath, "r")


    ##2 define characters you need to escape when reading text
#special = r"\\'{}$&#^_%~"

    #read file, lowercase all words and push into string only words escaping special characters

text = (" ".join(re.findall("[a-z\']+", source.read().lower())))
print(text)

#print(re.sub(r"(?<!\\)([" + special + "])", r"\\\1", text))


    #3 split raw string into the list of words to be processed
words = re.split(r'\s', text)

print(words)
#if text is not None:
#        for word in words:
#            # Word Exist?
#            if word in hash_map:
#                hash_map[word] = hash_map[word] + 1
#            else:
#                hash_map[word] = 1
#        return hash_map
#    else:
#        return None


    #7 close the file after reading
source.close()


#re.sub(re.compile("<!\[.*?\]>"), "", "<![if support]> hello")
