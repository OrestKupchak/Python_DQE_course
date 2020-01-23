from xml.etree.ElementTree import parse, Element
import xml.etree.ElementTree as ET
from collections import Counter 
import re

testfile = 'mondial-3.0.xml' #filename hardcoded as required in task, no logical flexibility was required

def parse_and_remove(filename, path):
    path_parts = path.split('/') #tag 
    doc = ET.iterparse(filename, ('start', 'end')) #retrieve tags form XML file
    # Skip root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
           tag_stack.append(elem.tag) 
           elem_stack.append(elem)
        elif event == 'end':
                if tag_stack == path_parts: #if tag is what we're looking for, get it's value
                    yield elem
                try:
                    tag_stack.pop() #remove as not needed for processing
                    elem_stack.pop()  #remove as not needed for processing
                except IndexError:
                    pass            
    return tag_stack, elem_stack     

def readXML(filename):
    country_government = []
    distinct_governments = set() #use Set to avoid dulpicates and store only unique values as required in task
    countries = parse_and_remove(filename, 'country') #get all countreis names form XML using our function

    for country in countries:
        name = country.attrib['name']
        if re.search(r'\s', name): #check if country name has whitespaces, which means that it consist of more than 1 word, 
                                   #which was a goal for comlicated version of hmwk
            government = country.attrib['government'] #tagname hardcoded as required in task, no logical flexibility was required
            if len(government.strip()) > 0: #skip empty string and get governmant values only where it exists
                country_government.append((name, government.strip()))
    for name, government in country_government:
        distinct_governments.add(government) 

    return sorted(distinct_governments) #sort alphabetically before pinting the result

def main():

    result = readXML(testfile)
    print(*result, sep = ", ")  #print unique government values as a comma separated string

if __name__ == "__main__":
    main()