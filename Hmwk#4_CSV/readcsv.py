import argparse
import csv
import os
import re
from typing import List, Union

#--filename    -f    Path to a file containing a list of users to scrape.
#--columnname   -f    name of column to read from csv file.

def getArgs(argv = None): 
    parser = argparse.ArgumentParser(description='Add filepath to file to read from.') #add arguments
    parser.add_argument('filepath', type=str,help='path to file needed to read')
    parser.add_argument('columnname', type=str,help='column from csv file needed to read')

    return parser.parse_args(argv) #return arguments passed from cmd



def checkFile(args):
    #check for file
    path_csv  = args.filepath #path to directory c:\smth or /smth
    path_folder = os.path.split(path_csv)[0] #get path to folder only

    filename = os.path.basename(path_csv).split('.')[0] #name without extension to check if such actually exists
    extension = '.' + os.path.basename(path_csv).split('.')[1] #file extension in format .smth
    
    columnname =  re.sub(r'[^a-zA-Z0-9]',r' ', args.columnname)  #column name to retrieve data from, 
                                                                 #remove '_' undersocre to resolve column names with 'space' input for cmd issue
    
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

    if csv_to_read is None:
        print('There is no file with "{}" name in "{}" folder'.format(filename, dirroot)) #if file doesn't exsit - stop processing
 
    return csv_to_read, columnname


def getData(csv_to_read, columnname):
    #read file and get data from column
    try:
        with open(csv_to_read, newline='') as csvfile:
            d_reader = csv.DictReader(csvfile)

            #get fieldnames from DictReader object and store in list
            headers = d_reader.fieldnames
            
            if columnname not in headers: 
                print('No column with "{}" name in "{}" file found'.format(columnname, os.path.split(csv_to_read)[1]))
                
            #print value in <column_name> for each row
            for line in d_reader:
               print(line[columnname])
    except Exception:
        print("Error Reading from file: ", csv_to_read)



def main():
    args = getArgs() 
    csvfile, column = checkFile(args)
    getData(csvfile, column)


if __name__ == "__main__":
    main()



