import csv, sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect("XOSERVE_DB")
    curs = conn.cursor()
    curs.execute('DROP TABLE IF EXISTS smrt_table01')
    curs.execute("CREATE TABLE  smrt_table01(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno)")
    df=pd.read_csv(r'C:\\Users\\Mangala\\Downloads\\GazpromEnergyDataEngineerCodeTest\\sample_data\\PN000001.SMRT')

    columns = ['HEADR', 'SMRT', 'GAZ', '20191016', '102939', 'PN000001']
    df_data = df[columns]
    records = df_data.values.tolist()
    print(records)

    print("file opened")
    for row in records:
        
            to_db = [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]),str(row[5])]
            print(to_db)
            curs.execute("INSERT INTO smrt_table01 (recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) VALUES (?, ?, ?, ? ,? ,? );", to_db)
            print("data inserted")
            conn.commit()
         

if __name__=='__main__':
    main()
