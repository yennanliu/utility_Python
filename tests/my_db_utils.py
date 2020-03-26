import sqlalchemy
from datetime import datetime

def get_db_conn():
    try:
        conn = sqlalchemy.create_engine("db_url")
    except Exception as e:
        print (e)
        return None
        
    # conn = sqlalchemy.create_engine(
    #      {"db":"my_db", 
    #       "user":"my_user", 
    #       "password":"my_password"
    #      }
    #     )
    #return conn