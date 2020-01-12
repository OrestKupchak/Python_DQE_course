import os
import sys
import csv
from typing import List, Union
import argparse

def getArgs(argv=None):
    parser = argparse.ArgumentParser(description='Add filepath.')
    parser.add_argument('-f','--filepath', type=str,help='path to file needed to read')
    #parser.add_argument('-e','--extension', type=str,help='extension of the  file needed to read')
    parser.add_argument('-c','--columnname', type=str,help='column from csv to read')

    #args = parser.parse_args()

    #print(parser)
    #print("args: ", args)
    #print(args.filepath)
    print("getArgs() result: ", parser.parse_args(argv))
    return parser.parse_args(argv)



def checkFile(args):
    #check for file
    path_csv  = args.filepath #path to directory c:\smth or /smth
    path_folder = os.path.split(path_csv)[0]
    
    print("os.path.basename(path_csv).split('.')", os.path.basename(path_csv).split('.'))

    filename = os.path.basename(path_csv).split('.')[0]
    extension = '.' + os.path.basename(path_csv).split('.')[1] #file extension in format .smth
    print("filename ", filename, "extension", extension)

    columnname =  args.columnname  #column name to retrieve data from

    print("path_folder", path_folder)

    result: List[Union[bytes, str]] = []            #store path + file, if exists in passed directory
    print("path_csv: ", path_csv)
    print("extension: " , extension)
    print("columnname : ", columnname)

    for dirroot, dirname, filenames in os.walk(path_folder): #run through directory and retrieve filenames
        print("dirroot :", dirroot)
        print("dirname :", dirname)
        print("filenames :", filenames)
        for file in filenames:                      #check each filename
            if extension == os.path.splitext(file)[1]:   #if file extension is what we're looking for
                print('here - > ', file, os.path.basename(path_csv))
                print('extension - > ', extension, os.path.splitext(file)[1])

                result.append(os.path.join(dirroot, file))  #add filename to direcory path to work with
                #else:
                #    print("No file with '{}' name in this folder".format(filename))
            #else:
            #    print("No file with {} extension in this folder".format(extension))

        for item in result:
            if item == os.path.basename(path_csv):
                print('item - > ', item, filename, os.path.basename(path_csv))
            csv_to_read = item    
        print("os.path.splitext(file) :",os.path.splitext(file))
    print('Result is :', result, "csv_to_read ", csv_to_read)    
#-f D:\PYTHON\Python_DQE_course\Hmwk#4_CSV -e .py -c Sample
    return csv_to_read, columnname
    

def getData(filename, columnname):
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



#-f D:\PYTHON\Python_DQE_course\Hmwk#4_CSV -e .py -c Sample
def main():
    argvals = None             # init argv in case not testing

    #argvals = '-f D:\PYTHON\Python_DQE_course\Hmwk#4_CSV -e .py -c Sample'.split() # example of passing test params to parser
    args = getArgs(argvals)
    csvfile, column = checkFile(args)
    getData(csvfile, column)



if __name__ == "__main__":
    main()







