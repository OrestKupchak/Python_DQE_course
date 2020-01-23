import argparse
import csv
import os
import sys
import json
from typing import List, Union

#--csvfilepath    -f    path to file needed to read
#--jsonfile   -f    path to file to write




def getArgs(argv = None): 
    parser = argparse.ArgumentParser(description='Add filepath to file to read from.') #add arguments
    parser.add_argument('-cf','--csvfilepath', type=str,help='path to file needed to read')
    parser.add_argument('-jf','--jsonfile', type=str,help='path to file to write')
    print("parser.parse_args(argv)", parser.parse_args(argv))
    return parser.parse_args(argv) #return arguments passed from cmd



def checkFile(args):
    #check for file
    path_csv  = args.csvfilepath #path to directory c:\smth or /smth
    path_json = args.jsonfile 
    path_folder = os.path.split(path_csv)[0] #get path to folder only

    print("path_csv", path_csv, "path_json", path_json)
    print("os.path.basename(path_csv)", os.path.basename(path_csv))
    print("os.path.basename(path_csv).split('.')", os.path.basename(path_csv).split('.'))
    filename = os.path.basename(path_csv).split('.')[0] #name without extension to check if such actually exists
    extension = '.' + os.path.basename(path_csv).split('.')[1] #file extension in format .smth

    csv_to_read = None #initialze value for result file to read

    result: List[Union[bytes, str]] = []            #store path + file, if exists in passed directory

    for dirroot, dirname, filenames in os.walk(path_folder): #run through directory and retrieve filenames
        for file in filenames:                      #check each filename
            if extension == os.path.splitext(file)[1]:   #if file extension is what we're looking for
                result.append(os.path.join(dirroot, file))  #add filename to direcory path to work with
        
        if len(result) < 1:     #if no files found - nothing to process
            print('"{}" folder is empty'.format(dirroot))

        for item in result:
            if os.path.split(item)[1] == os.path.basename(path_csv):
                csv_to_read = item    

    if csv_to_read == None:
        print('There is no file with "{}" name in "{}" folder'.format(filename, dirroot)) #if file doesn't exsit - stop processing
 
    return csv_to_read, path_json


def getData(csv_to_read):
    #read file and get data from column
    data = {}
    try:
        
        with open(csv_to_read) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for i, csvRow in enumerate(csvReader, start = 1):
                row_id = i
                data[row_id] = csvRow
                data[row_id]["password"] = "NULL"
    except Exception:
        print("Error Reading from file: ", csv_to_read)
    return data


def load_json(jsonFilePath, jsonobject):
    with open(jsonFilePath,'w') as jsonFile:
        jsonFile.write(json.dumps(jsonobject, indent = 4))


def main():
    argvals = None       #init

    argvs = getArgs(argvals) 
    csvfile, jsonfile = checkFile(argvs)
    jsonobject = getData(csvfile)
    load_json(jsonfile, jsonobject)

if __name__ == "__main__":
    main()
