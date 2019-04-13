# python 3 
import pandas as pd 

tsv_file='name.tsv'
csv_file='name.tsv'
csv_table=pd.read_table(tsv_file,sep='\t',encoding = "ISO-8859-1")
csv_table.to_csv(csv_file,index=False)
