
# ref :  https://gist.github.com/stefanthoss/364b2a99521d5bb76d51

# ref : https://github.com/PyMySQL/PyMySQL

# ref : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html

# ref : http://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python

# ref : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html



import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import csv
import requests
from bs4 import BeautifulSoup
import lxml
import urllib, json
import pandas as pd, numpy as np
import pprint


localtime = time.asctime( time.localtime(time.time()) )


def taxi_df():
		# Make the HTTP request.
	request_headers = {"api-key": "gWpVyvnoSuAeW1J27L7W4nNG4gbQwfVC"}
	request = urllib.request.Request('https://api.data.gov.sg/v1/transport/taxi-availability',headers=request_headers)
	response = urllib.request.urlopen(request)
	result = json.loads(response.readall().decode('utf-8'))
	(json.loads(json.dumps(result, ensure_ascii=False)))
	data = result['features'][0]['geometry']['coordinates']
	df = pd.DataFrame(result['features'][0]['geometry']['coordinates'])
	df.columns = ['lon', 'lat']
	df['timestamp']=dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
	df_=[]
	for k in data:
		df_.append(k[::-1])
	
	for k in df_:
		k.append(0.5)
	print (df)	
	return (df)


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
		print ('insert csv OK')
	except:
		print ('insert csv failed')
		
		


def insert_data_df_new_table():
	
	'''
	if_exists : {‘fail’, ‘replace’, ‘append’}, default ‘fail’
	fail: If table exists, do nothing.
	replace: If table exists, drop it, recreate it, and insert data.
	append: If table exists, insert data. Create if does not exist.
	
	'''
	try:
		
		engine = create_engine('mysql+pymysql://<user>:<password>@<host>[:<port>]/<dbname>', echo=True)
		df=taxi_df()
		df.to_sql('taxi', engine, if_exists = 'append') 
		
		print ('insert df OK')
	except:
		print ('insert df failed')

		
		
		






