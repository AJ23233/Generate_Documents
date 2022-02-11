import psycopg2
from config import CONF, DB_NAME, DB_PORT, DB_HOST, DB_USER, DB_PASS, DB_URL
from sqlalchemy import create_engine


# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(
#                                 database=DB_NAME,
#                                 user=DB_USER,
#                                 password=DB_PASS,
#                                 host=DB_HOST,
#                                 port=DB_PORT
#                                     )

		
#         # create a cursor
#         cur = conn.cursor()
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
       
# 	# close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


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

# >>> abc.execute("select * from employee_data")


# def db_connection():
#     # this method connects with databas

#     print('Connecting to the PostgreSQL database...')
#     conn = psycopg2.connect(
#                             database=DB_NAME,
#                             user=DB_USER,
#                             password=DB_PASS,
#                             host=DB_HOST,
#                             port=DB_PORT
#                       0      )
#     pool.
    