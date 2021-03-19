#df = pd.read_csv('C:\\Users\\Mangala\\Downloads\\GazpromEnergyDataEngineerCodeTest\\sample_data\\PN000001.SMRT')
#df.head()              
# get data file names. 
#Importing CSV file to the postgres Database

#import libraries
#Conda install paycopg2
#pip install paycopg2

import os
import pandas as pd
import glob
import numpy as np
import csv
import sqlite3


# Create the database
connection = sqlite3.connect('XOSERVE_DB')
cursor = connection.cursor()
print("Connected to DB")

# Create the table
cursor.execute('DROP TABLE IF EXISTS smrt_table')
cursor.execute('CREATE TABLE  smrt_table(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) ')
connection.commit()

print("table created")


# Reading the mulitple files 

#path =(r'C:\\Users\\Mangala\\Downloads\\GazpromEnergyDataEngineerCodeTest\\sample_data\\')
df=pd.read_csv(r'C:\\Users\\Mangala\\Downloads\\GazpromEnergyDataEngineerCodeTest\\sample_data\\PN000001.SMRT')
df.head()
#Specify the columns we want to import

columns =df.columns
print(columns)

columns = ['HEADR', 'SMRT', 'GAZ', '20191016', '102939', 'PN000001']
df_data = df[columns]
records = df_data.values.tolist()
print(records)



# Load the CSV file into CSV reader

sql_insert= '''
          INSERT INTO smrt_table (recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) VALUES (?, ?, ?, ? ,? ,? );", records)
'''

try:
     cursor.executemany(sql_insert,records)
     print("records are inserted")

except Exception as e:
     print(e)

finally:
     print("Task is completed")
     cursor.close()
     connection.close() 


