import sqlalchemy
from datetime import datetime

def get_db_conn():
    conn = sqlalchemy.create_engine(
         {"db":"my_db", 
          "user":"my_user", 
          "password":"my_password"
         }
        )
    return conn