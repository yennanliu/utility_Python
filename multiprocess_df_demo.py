# python 3 


"""

modify from 
http://yaoyao.codes/python/2018/01/23/pandas-split-a-dataframe-into-chunks

"""


import os
import pandas as pd 
import numpy as np 
from multiprocessing import Pool
from sklearn import datasets


# make toy df 
toydata = datasets.make_regression(n_samples=100,n_features=100)
df_toydata = pd.DataFrame(i for i in toydata[0])

# split df 


def index_marks(nrows, chunk_size):
    print ('chunk_size : ', chunk_size)
    return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def split(df, chunk_size):
    indices = index_marks(df.shape[0], chunk_size)
    return np.split(df, indices)


def print_df(df_name):
    print (df.head())
    #return pd.read_csv(filename)

def main():
    # set up your pool
    pool = Pool(processes=4) # or whatever your hardware can support

    # get a list of file names
    #files = os.listdir('.')
    #file_list = [filename for filename in files if filename.split('.')[1]=='csv']
    df_list = [df_split for df_split in df if filename.split('.')[1]=='csv']

    # have your pool map the file names to dataframes
    df_list = pool.map(print_df, df)

    # reduce the list of dataframes to a single dataframe
    combined_df = pd.concat(df_list, ignore_index=True)
