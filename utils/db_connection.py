import psycopg2
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import CONF, DB_NAME, DB_PORT, DB_HOST, DB_USER, DB_PASS, DB_URL


class DatabaseConnection(object):

    def __init__(self): 
        pass
        
    def __enter__(self):
        
        self.dbconn = self.db_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()

    def db_connection(self):
        eng = create_engine(DB_URL)
        
        return eng.connect()

def make_conn():
    conn = psycopg2.connect(database='doc_gen',
                            user='python',
                            host='localhost',
                            password='python',
                            port=5432)
    return conn

class SQLAlchemyDB(object):

    def __init__(self):

        self.connection = None
        self.session = None
        mypool = pool.QueuePool(make_conn, pool_size=15)
        self.engine = create_engine('postgresql://', pool=mypool)
        print("init method called")

    def __enter__(self):

        session_maker = sessionmaker()
        self.connection = self.engine.connect()
        self.session = session_maker(bind=self.connection)
        print("enter method called")
        return self.session

    def __exit__(self,*_):

        self.session.close()
        self.connection.close()
        print("Exit method called")
