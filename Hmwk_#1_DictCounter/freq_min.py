import itertools
import re, os
from collections import Counter, OrderedDict
from os import path

print(dict(OrderedDict(sorted(Counter(re.findall(re.compile(r'([\w\'+]+\w)'), open("Book.txt", "r").read().lower()) ).items(), key=lambda t: t[0]))))


