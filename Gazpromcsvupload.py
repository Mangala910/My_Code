import csv, sqlite3
import pandas as pd
import os
import glob
from os import listdir
import numpy as np
from glob import iglob

# create connection to database
conn = sqlite3.connect("XOSERVE_DB")
curs = conn.cursor()
curs.execute('DROP TABLE IF EXISTS smrt_header_table')
curs.execute("CREATE TABLE  smrt_header_table(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno)")

curs.execute('DROP TABLE IF EXISTS smrt_CONSU_table')
curs.execute("CREATE TABLE  smrt_CONSU_table(recordid, meternumber, measurementdate,measurementtime,consumption)")

# get data file names
path =os.getcwd()
print("This is current working directory " +path)  
path=path+"/sample_data" 
filenames = glob.glob(path + "/*.SMRT")
print(filenames)


# Build up DataFrame and iterate through file.
df = pd.DataFrame()
for file in filenames:
    frame = pd.read_csv(file)
    df = df.append(frame)
    df.head() 
    print(df)

    
    columns = ['HEADR', 'SMRT', 'GAZ', '20191016', '102939', 'PN000001']
    df_data = df[columns]
    records = df_data.values.tolist()
    print(records)
    headers = df.values.tolist()
    print(headers)
     
    # print the total number of records 
    rowcount = len(records) #which incudes header row   
    print("Total rows incuding header: " + str(rowcount))
    

    #headers=df.head()
    #print(headers)
    for header in headers:  
        to_db = [str(header[0]), str(header[1]), str(header[2]), str(header[3]), str(header[4]),str(header[5])]
        print(to_db)
        curs.execute("INSERT INTO smrt_header_table(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) VALUES (?, ?, ?, ? ,? ,? );", to_db)
        conn.commit() 
        print("data inserted in smrt_header_table table")
              
    for row in records: 
        try: 
           to_db2 = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])]
           print(to_db2)
           curs.execute("INSERT INTO smrt_CONSU_table(recordid, meternumber, measurementdate,measurementtime,consumption) VALUES (?, ?, ?, ? ,?  );", to_db2)
           conn.commit() 
           print("data inserted in smrt_CONSU_table table")
        except Exception as e:
           print(e)   
         
                    
               