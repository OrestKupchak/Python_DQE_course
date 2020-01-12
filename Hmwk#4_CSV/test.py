import csv
import os
import sys
import argparse
from typing import List, Union


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List (sys.argv):', str(sys.argv))


#check for file
path_csv  = sys.argv[1] #path to directory c:\smth or /smth
putextension = sys.argv[2] #file extension in format .smth
columnname = sys.argv[3]  #column name to retrieve data from

result: List[Union[bytes, str]] = []            #store path + file, if exists in passed directory
print("path_csv: ", path_csv)
print("putextension: " , putextension)
print("columnname : ", columnname)

for dirroot, dirname, filenames in os.walk(path_csv ): #run through directory and retrieve filenames
    print("dirroot :", dirroot)
    print("dirname :", dirname)
    print("filenames :", filenames)
    for file in filenames:                      #check each filename
        if putextension == os.path.splitext(file)[1]:   #if file extension is what we're looking for
            result.append(os.path.join(dirroot, file))  #add filename to direcory path to work with
print('Result is :', result)




#read file and get data from column
try:
    filename = sys.argv[1]
    with open(filename, newline='') as csvfile:
        d_reader = csv.DictReader(csvfile)

        #get fieldnames from DictReader object and store in list
        headers = d_reader.fieldnames
        print(headers)

        #print value in <column_name> for each row
        for line in d_reader:
            print(line[columnname])
except Exception:
    print("Error Reading from file: ", filename)

'''
parser = argparse.ArgumentParser(description='Add filepath.')
parser.add_argument('--filepath', type=str, nargs='+',help='filepath')
parser.add_argument('--sum', action='store_const', const=sum, default=sum, help='add file to path')
args = parser.parse_args()

#print(parser)
print(args)

#print(args.filepath)
#print(args.sum(args.filepath))
'''


'''
import argparse
parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')
parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.integers)
print(args.sum(args.integers))
'''


