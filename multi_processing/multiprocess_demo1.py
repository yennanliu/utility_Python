"""
modify from 
http://yaoyao.codes/python/2018/01/23/pandas-split-a-dataframe-into-chunks
https://stackoverflow.com/questions/36587211/easiest-way-to-read-csv-files-with-multiprocessing-in-pandas
"""

import os
import pandas as pd 
import numpy as np 
from multiprocessing import Pool
from sklearn import datasets

# make toy df 
toydata = datasets.make_regression(n_samples=100,n_features=100)
df_toydata = pd.DataFrame(i for i in toydata[0])

# ---------------------------------------------
# V1 
def index_marks(nrows, chunk_size):
    print ('chunk_size : ', chunk_size)
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def split(df, chunk_size):
    indices = index_marks(df.shape[0], chunk_size)
    return np.split(df, indices)

def print_df(df):
    print (df)
    #return pd.read_csv(filename)

def main(df):  
    # set up your pool
    pool = Pool(processes=4) # or whatever your hardware can support  
    # get a list of df names   
    df_list = [df_split for df_split in split(df,3) ]
    # have your pool map the file names to dataframes
    df_list = pool.map(print_df, df)
    print ('df_list : ', df_list)
    # reduce the list of dataframes to a single dataframe
    combined_df = pd.concat(df_list, ignore_index=True)

# ---------------------------------------------
# V2 
def demo():
    """
    ref 
    https://stackoverflow.com/questions/37305014/python-running-n-number-of-functions-in-parallel    
    """
    def g(df):                   
        for i in range(5): 
            print (i)
        print ('this is job log')
        return i
            #pass
    pool = Pool(processes=5)     # 5 worker processes
    print (pool.map(g, range(3)))  # 3 jobs, a list will be returned when all are finished
