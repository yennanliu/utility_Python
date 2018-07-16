
# python 3 

# -*- coding: utf-8 -*-
import pandas as pd 
import xlsxwriter


def get_access_request_report2():
    # xlsxwriter write multiple dataframe to one xls 
    # https://stackoverflow.com/questions/32957441/putting-many-python-pandas-dataframes-to-one-excel-worksheet
    # sql 
    # create xls writer 
    writer = pd.ExcelWriter('df_test.xlsx',engine='xlsxwriter')   
    workbook=writer.book
    # save
    df_1.to_excel(writer,sheet_name='df_1',startrow=0 , startcol=0)   
    df_2.to_excel(writer,sheet_name='df_2',startrow=0, startcol=0)
    df_3.to_excel(writer,sheet_name='df_3',startrow=0, startcol=0)
    return df_1, df_2, df_3 



