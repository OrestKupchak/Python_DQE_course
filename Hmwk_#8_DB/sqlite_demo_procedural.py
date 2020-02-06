import csv
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, MetaData, ForeignKey, Integer, String, Date
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.exc import IntegrityError
from sqlalchemy.schema import CreateTable, UniqueConstraint
from tabulate import tabulate #pretty printer

#read data from CSV file to insert into DB
def getData(csv_to_read):
    result = []
    #read file and get data from column
    try:
        with open(csv_to_read, 'r', encoding="utf-8") as csvfile:
            d_reader = csv.DictReader(csvfile)
            for line in d_reader:
               result.append(line)      
    except Exception:
        print("Error Reading from file: ", csv_to_read)
        
    return result


#create DB and connection
engine = create_engine('sqlite:///C:\\sqlite\\sqlite_DBs\\orest_database.db')

if database_exists(engine.url):
    drop_database(engine.url)

create_database(engine.url)
connection = engine.connect()



#create tables
meta = MetaData()

project = Table(
   'project', meta, 
   Column('id', Integer, autoincrement=True, primary_key = True), 
   Column('name', String(100), sqlite_on_conflict_unique='IGNORE', index=True, nullable=False), 
   Column('description', String(1000)), 
   Column('deadline', Date),
   UniqueConstraint('name', sqlite_on_conflict='IGNORE')
)

tasks = Table(
   'tasks', meta, 
   Column('id', Integer, autoincrement=True, primary_key = True), 
   Column('priority', Integer), 
   Column('details', String(1000)), 
   Column('status', String(100)), 
   Column('deadline', Date),
   Column('completed', Date),
   Column('project', String(100), ForeignKey("project.id"), nullable=False)
)

meta.create_all(engine) #execute create statements


#insert records from CSV into tables
records = getData('test.csv')
project_insert = project.insert().prefix_with('OR IGNORE')  #ignore duplicates
tasks_insert = tasks.insert() 

#execute insert statements
connection.execute(project_insert, [{
                                    "name": row["project_name"], 
                                    "description": row["project_description"], 
                                    "deadline" : datetime.strptime(row["project_deadline"], '%m-%d-%Y').date() #convert to proper date format
                                    }
                    for row in records])


connection.execute(tasks_insert, [{
                                    "priority": row["task_priority"], 
                                    "details": row["task_details"], 
                                    "status" : row["task_status"],
                                    "deadline" : datetime.strptime(row["task_deadline"], '%m-%d-%Y').date(), #convert to proper date format
                                    "completed" : datetime.strptime(row["task_completed"], '%m-%d-%Y').date(), #convert to proper date format
                                    "project" : row["project_name"]
                                    }
                    for row in records])

#use parametrisation in query
parameter = input('select Project Name to query: ')
projects = connection.execute('SELECT * FROM Project Join Tasks on Project.name = Tasks.project WHERE name = :x', x = parameter)

print(tabulate(projects)) #pretty print results as table
connection.close()

