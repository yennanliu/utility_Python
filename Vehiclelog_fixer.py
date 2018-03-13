# python 3 

"""
ref 
https://stackoverflow.com/questions/33137506/extracting-appending-pandas-dataframe-rows-which-meet-a-complex-condition-involv


for index, row in dataframe1.iterrows():
    if row['a'] > .5:

        dataframe2.loc[index] =  row

dataframe2

          a         b         c         d         e
1  1.651437 -2.426679 -0.428913  1.265936 -0.866740
4  0.737369  1.490732 -0.935834  1.175829 -1.253881




"""


# ops 
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os

 
# analysis 
import numpy as np





def main():
	# shift the category col, for following N row and N-1 row comparision 
	df__vehiclelog_sample_dev['category_shifted'] = df__vehiclelog_sample_dev.category.shift(-1)
	# define output rows (as new dataframe)
	dataframe2 = pd.DataFrame(columns=df__vehiclelog_sample_dev.columns)
	dataframe2
	# for loop every row put data back (if fit the conditions)
	#for index, row in df__vehiclelog_sample_dev.iloc[1282:1310].iterrows():
	for index, row in df__vehiclelog_sample_dev.iloc[0:].iterrows():
		#print (row['category'])
		print (row)
		"""
		before : Out of Service -> Create booking
		after  : Out of Service -> Return to Service -> Create booking

		"""
		if (str(row['category']) =='Out of Service') and (str(row['category_shifted']) =='Create booking'):
			dataframe2.loc[index] =  row
			dataframe2['category'] = 'Return to Service'
			print ('missing event Return to Service ')
		#elif (str(row['category']) =='Return to Service') and (str(row['category_shifted']) =='Create booking'):
		elif (str(row['category']) =='Create booking') and (str(row['category_shifted']) =='Out of Service'):
			dataframe2.loc[index] =  row
			dataframe2['category'] = 'Out of Service'
			print ('missing event Out of Service')
		else:
			pass























