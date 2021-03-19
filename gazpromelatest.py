import csv, sqlite3
import pandas as pd
import os
import glob
from os import listdir
import numpy as np

#def main():
    conn = sqlite3.connect("XOSERVE_DB")
    curs = conn.cursor()
    curs.execute('DROP TABLE IF EXISTS smrt_table02')
    curs.execute("CREATE TABLE  smrt_table02(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno)")
     
         # get data file names
    path =os.getcwd()
    print("This is current working directory " +path)  
    path=path+"/sample_data" 
    filenames = glob.glob(path + "/*.SMRT")
    print(filenames)
   

    # Step 3: Build up DataFrame:
    df = pd.DataFrame()
    for file in filenames:
        frame = pd.read_csv(file)
        df = df.append(frame)
        print(df)    
        columns = ['HEADR', 'SMRT', 'GAZ', '20191016', '102939', 'PN000001']
        df_data = df[columns]
        records = df_data.values.tolist()
        print(records)

        for row in records:
           try:
              to_db = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]),str(row[5])]
              print(to_db)
              curs.execute("INSERT INTO smrt_table02(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) VALUES (?, ?, ?, ? ,? ,? );", to_db)
              print("data inserted")
              conn.commit()
               

#if __name__=='__main__':
   # main()
