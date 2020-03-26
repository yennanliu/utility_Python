import sqlalchemy
from datetime import datetime

def get_db_conn():
    try:
        conn = sqlalchemy.create_engine("db_url")
    except Exception as e:
        print (e)

    if str(sqlalchemy.create_engine) == '<function create_engine at 0x104695620>':
        return sqlalchemy

    # conn = sqlalchemy.create_engine(
    #      {"db":"my_db", 
    #       "user":"my_user", 
    #       "password":"my_password"
    #      }
    #     )
    #return conn