# python 3 

import csv 
import psycopg2

with open('example.csv') as f:
	"""
	example.csv : 

		 id                             email           name  \
	0   0               cbenjamin@yahoo.com   Joseph Kirby   
	1   1  morganlopez@matthews-hickman.com  Erin Figueroa   
	2   2                   ypark@russo.biz  Leon Matthews   

	                                             address  
	0  3594 Fox Ford Apt. 192 West Kristen GA 22838-8977  
	1  64763 Li Meadows Apt. 554 New Marcoton MA 9901...  
	2  91144 Hamilton Manors Suite 421 Ronaldland WA ...  

	​
	"""
    reader = csv.reader(f)
    next(reader)
    rows = [row for row in reader]

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
for row in rows:
    cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", row)
conn.commit()
cur.execute('SELECT * FROM users')
users = cur.fetchall()
conn.close()






