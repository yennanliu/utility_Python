import pandas as pd 
import glob

files = glob.glob('20*.csv')
print (files)
df_final = pd.concat([pd.read_csv(f, index_col=0, header=None) for f in files], keys=files)
# save to csv 
#df_final.to_csv('df_final.csv')
# save to compression file 
df_final.to_csv('df_final_gz.gz', compression='gzip')