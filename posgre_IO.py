# python 3 


import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os



def get_data_from_db(sql, db_url):
    try:
        engine = create_engine(db_url)
        #conn = engine.connect()
        # need to double check 
        print (sql)
        df = pd.read_sql(sql=sql, con= engine)
        # close the connection after imput data 
        #conn.close()
        print (df.head())
        return df 
        print("extract data ok")
    except Exception as e:
        print (e)
        print ('fail to get data from db')




def write_data_to_db(df, table_name,db_url):
    try:
        # add insert time 
        df["date_of_insert"] = now
        print ('=============')
        print (df.head())
        print (table_name)
        print ('=============')
        engine = create_engine(db_url)
        conn = engine.connect()
        df.to_sql(name= table_name, con= engine, schema= 'rw', if_exists = "append", index = False)
        # close the connection after imput data 
        conn.close()
        print("insert to DB ok")
    except Exception as e:
        print (e)
        print ('fail to write to db')





        