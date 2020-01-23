from xml.etree.ElementTree import parse, Element
import xml.etree.ElementTree as ET


testfile = 'mondial-3.0.xml'
path = 'population'


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    print("path ", path, "path_parts ", path_parts)
    doc = ET.iterparse(filename, ('start', 'end'))
    # Skip root element
    print("doc ", doc)
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
           tag_stack.append(elem.tag)
           elem_stack.append(elem)
        elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                    print("elem ", elem)
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass
    print("tag_stack ", tag_stack, "elem_stack ", elem_stack)                
    return tag_stack, elem_stack     
                         
    #return tag_stack, elem_stack    

def main():
    xmldata = parse_and_remove(testfile, 'government')
    print("xmldata", xmldata)

if __name__ == "__main__":
    main() 


'''
path_parts = path.split('/')
doc = ET.iterparse(testfile, ('start', 'end'))

print(path_parts)
print(doc)
next(doc)

tag_stack = []
elem_stack = []
for event, elem in doc:
    #print(event, elem)
    if event == 'start':
        tag_stack.append(elem.tag)
        elem_stack.append(elem)
        print(elem, elem.tag)
    elif event == 'end':
        if tag_stack == path_parts:
            #yield elem
            print(elem)
        try:
            tag_stack.pop()
            elem_stack.pop()
        except IndexError:
            pass
print(tag_stack, elem_stack)  
'''