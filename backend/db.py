import databases
import sqlalchemy

DATABASE = 'postgresql'
USER = 'testuser'
PASSWORD = 'secret'
HOST = 'postgres'
PORT = '5432'
DB_NAME = 'testdb'

DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()
