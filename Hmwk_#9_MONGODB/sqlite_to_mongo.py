import datetime
import sqlalchemy
import json
from pymongo import MongoClient


source_db_path = 'sqlite:///C:\\sqlite\\sqlite_DBs\\orest_database.db' #use local path to SQLite DB file

#connect to SQLite source DB and retrieve data for migration to MongoDB
def getSourceData(source_db_path):

    engine = sqlalchemy.create_engine(source_db_path)
    sqlite_source = engine.connect() #connecto to source DB

    projects = sqlite_source.execute('SELECT * FROM Project')  #query data from tables
    tasks = sqlite_source.execute('SELECT * FROM Tasks')

    projects_data = json.dumps([(dict(row.items())) for row in projects]) #convert o JSON for migration
    tasks_data = json.dumps([(dict(row.items())) for row in tasks]) #convert o JSON for migration
    
    return projects_data, tasks_data


#connect to MongoDB and create respective DB and collections to store data
def loadToMongo(projects_data, tasks_data):

    connection = MongoClient(host='localhost', port=27017) 

    db = connection["orest_db"]  #In MongoDB, a database is not created until it gets content, 
                                #you should create collection and create document before you check if the database exists!
                                                
    if db["project"].estimated_document_count() > 0: #delete existing for initial ETL
        db["project"].drop()
        db["tasks"].drop()

    projects_collection = db["project"] #assign collections to store data
    tasks_collection = db["tasks"]

    projects_collection.insert_many(json.loads(projects_data)) #load SQLite data dump into MongoDB
    tasks_collection.insert_many(json.loads(tasks_data))

    return projects_collection, tasks_collection


#query from MongoDB and show projects and cancelled tasks if such exist
def getCancelled(projects_collection, tasks_collection):

    projects = []
    cancelled = {}

    # get a list of ids and author_ids for every message
    for project in projects_collection.find():
        projects.append(project['name'])
    # iterate through every author_ids to find the corresponding username
    for item in projects:
        task = tasks_collection.find_one({"project": item, "status": "cancelled" }, { "_id": 0, "details": 1, "status": 1 })
        cancelled["Project"] = item
        cancelled["CancelledTask"] = task
        print(cancelled)



if '__main__' == __name__:

    projects_data, tasks_data = getSourceData(source_db_path)
    projects, tasks = loadToMongo(projects_data, tasks_data)
    getCancelled(projects, tasks)
