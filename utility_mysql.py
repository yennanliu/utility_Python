
# ref :  https://gist.github.com/stefanthoss/364b2a99521d5bb76d51

# ref : https://github.com/PyMySQL/PyMySQL

# ref : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html

# ref : http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python


from pymysql import * 
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import datetime as dt   
import time, datetime
import csv


localtime = time.asctime( time.localtime(time.time()) )


def pymysql_connect():
	try:
		conn= pymysql.connect(host=dburl,port = 3306,user='root',password=password,db='mysqltest1',cursorclass=pymysql.cursors.DictCursor)
		a=conn.cursor()
		sql='select * from taxi limit 10 ; '
		a.execute(sql)

		for k in a:
			print (k)
		print ('connect sueecss')
	except:
		print ('MySQL connect failed')



def sqlalchemy_connect():
	try:
		engine = create_engine('mysql+pymysql://<user>:<password>@<host>[:<port>]/<dbname>')
		print ('connect sueecss')
		query="SELECT * FROM taxi limit 10"
		df = pd.read_sql_query(query, engine)
		df.head()
		return df 
	except:
		print ('MySQL connect failed')

def save_data():
	print (dt.datetime.today().strftime("%Y-%m-%d"))
	data = 	sqlalchemy_connect()
	data.to_csv('/Users/GGV/Desktop/sg_data/taxi_data %s.csv'%localtime)
	print('save data OK')


def insert_data_csv():
	try:
		conn= pymysql.connect(host=dburl,port = 3306,user='root',password=password,db='mysqltest1',cursorclass=pymysql.cursors.DictCursor)
		a=conn.cursor()
		f = open('/Users/GGV/Desktop/sg_data/taxi_data.csv')
		csv_data = csv.reader(f)              
		for row in csv_data:
			a.execute("INSERT INTO `taxi` (`id`,`lon`,`lat`,`time`) VALUES (%s, %s, %s,%s)", (row[1],row[2],row[3],row[4]))
			print ("INSERT INTO taxi (id,lon,lat,time) values (%s, %s, %s,%s)" % (row[1],row[2],row[3],row[4]))
		conn.commit()
		a.close()
		print ('insert OK')
	except:
		print ('insert failed')




