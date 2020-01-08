import csv
import os
import sys
from typing import List, Union

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))


filename = 'example.csv'


#if os.path.isfile(filename):
#    print ("File exist")
#else:
#    print ("File not exist")


#check for file
putdir = sys.argv[1] #path to directory c:\smth or /smth
putextension = sys.argv[2] #file extension in format .smth
columnname = sys.argv[3]  #column name to retrieve data from


result: List[Union[bytes, str]] = []            #store path + file, if exists in passed directory
for dirroot, dirname, filenames in os.walk(putdir): #run through directory and retrieve filenames
    for file in filenames:                      #check each filename
        if putextension == os.path.splitext(file)[1]:   #if file extension is wajt we're looking for
            result.append(os.path.join(dirroot, file))  #add filename to direcory path to work with

print(result)


with open('example.csv', newline='') as csvfile:
    d_reader = csv.DictReader(csvfile)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames
    print(headers)

#    #print value in <column_name> for each row
#    for line in d_reader:
#        print(line['Samples'])



'''
with open('example.csv', newline='') as csvfile:
    filecheck = csv.Sniffer()
    dialect = filecheck.sniff(csvfile.read())
    #print(dialect)
    csvfile.seek(0)
    data = csv.reader(csvfile, dialect)   
    
    if filecheck.has_header(csvfile.read()) == True:
        print(csvfile.fieldnames) 
    for row in data:
        print(row)    
'''                        