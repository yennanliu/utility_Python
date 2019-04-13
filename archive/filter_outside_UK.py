# python 3 

def filter_outside_uk(lat,lon):
    if (float(lat) < 58.576745 and float(lat) > 50.474865  
        and float(lon) < 1.727596 and float(lon) > -9.745551) :
        # 58.576745, -4.252387
        # 50.474865, -3.681098
        # 53.425787, -9.745551
        # 52.712887, 1.727596
        return 'in_UK'
    else:
        return 'outside_UK'



def main(df):
    """
    apply function to multiple cols in pandas 
    https://apassionatechie.wordpress.com/2017/12/27/create-multiple-pandas-dataframe-columns-from-applying-a-function-with-multiple-returns/
    
    example :

        df[['sum', 'difference']] = df.apply(lambda row: pd.Series(add_subtract(row['a'], row['b'])), axis=1)
    """
    df['located_UK'] = df.apply(lambda row : pd.Series(filter_outside_uk(row['LATITUDE'],row['LONGITUDE']))  ,axis=1)
    print (df['located_UK'].head(3))
    return df 









