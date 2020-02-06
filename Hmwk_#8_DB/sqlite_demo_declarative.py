import csv
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, MetaData, ForeignKey, Integer, String, Date, event
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateTable, UniqueConstraint
from sqlalchemy.sql import Insert
from sqlalchemy.engine import Engine


#add logic to ignore duplicates insertion
_ignore_tables = set() #define tables to listen

@event.listens_for(Engine, "before_execute", retval=True)
def _ignore_insert(conn, element, multiparams, params):
    if isinstance(element, Insert) and \
        element.table.name in _ignore_tables:
        element = element.prefix_with("OR IGNORE")
    return element, multiparams, params

def ignore_inserts(cls):
    _ignore_tables.add(cls.__table__.name)
    return cls


if '__main__' == __name__:

    #create DB and connection
    engine = create_engine('sqlite:///C:\\sqlite\\sqlite_DBs\\orest_database.db')

    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)

    connection = engine.connect()
    #print(database_exists(engine.url))

    Base = declarative_base()
    

    #create tables
    class Project(Base):
        __tablename__ = 'project'

        id = Column(Integer, primary_key=True,  autoincrement=True)
        name = Column(String(100), unique=True, nullable=False,  sqlite_on_conflict_primary_key='IGNORE', index=True)
        description = Column(String(1000), nullable=False) 
        deadline = Column(Date, nullable=True)

        __table_args__ = (
            UniqueConstraint(name, sqlite_on_conflict='IGNORE'), #add constraint to ignore duplicates
        )

    class Tasks(Base):
        __tablename__ = 'tasks'

        id = Column(Integer, primary_key=True)
        priority = Column(Integer, nullable=False)
        details = Column(String(1000), nullable=False)
        status = Column(String(100), nullable=False)
        deadline = Column(Date, nullable=False)
        completed = Column(Date, nullable=False)
        project_id = Column(Integer, ForeignKey('project.id'), nullable=False)


        print(CreateTable(Project.__table__).compile(engine))


    #execute create statements
    Base.metadata.create_all(engine)
    maker = sessionmaker(bind=engine)
    session = maker()

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


    
    def load_data(data, session):
        # Create some data
        for prj in data: 
            row = Project(name=prj["project_name"], description=prj["project_description"], deadline= datetime.strptime(prj["project_deadline"], '%m-%d-%Y').date())

            session.add(row)
            print(row)
    
        for task in data:
            row = Tasks(priority=task["task_priority"], details=task["task_details"], status=task["task_status"],
                        deadline=datetime.strptime(task["task_deadline"], '%m-%d-%Y').date(), #convert to proper date format
                        completed= datetime.strptime(task["task_completed"], '%m-%d-%Y').date(), #convert to proper date format
                        project=task["project_name"])
            session.add(task)
            print(task)
        session.commit()

    parameter = input('select Project Name to query: ')
    query = connection.execute('SELECT * FROM Project  WHERE name = :x', x = parameter)
    for row in query:
        print(row)

    data = getData('test.csv')
    load_data(data, session)

    connection.close()




