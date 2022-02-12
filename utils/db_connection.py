import psycopg2
from sqlalchemy import create_engine, pool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import pool
#from utils.configs import POOLSIZE
# POOLSIZE=15

from config import CONF, DB_NAME, DB_PORT, DB_HOST, DB_USER, DB_PASS, DB_URL


class DatabaseConnection(object):

    def __init__(self): 
        # self.dbconn = self.db_connection()
        pass
        
    def __enter__(self):
        
        self.dbconn = self.db_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()

    def db_connection(self):
        eng = create_engine(DB_URL)
        
        return eng.connect()


class SQLAlchemyDB(object):

    def __init__(self):

        self.connection = None
        self.session = None
        mypool = pool.QueuePool(self.db_conn, pool_size=15)
        self.engine = create_engine('postgresql://', pool=mypool)

    def __enter__(self):

        session_maker = sessionmaker()
        self.connection = self.engine.connect()
        self.session = session_maker(bind=self.connection)

    def __exit__(self,*_):

        self.session.close()
        self.connection.close()

    def db_conn():
        conn = psycopg2.connect(database='doc_gen',
                                user='python',
                                host='localhost',
                                password='python',
                                port=5432)
        return conn