# List all files in a directory using os.listdir

# Import Module 
import os 
import glob
import io
import sqlite3

# Folder Path 
#path =(r"C:\Users\Mangala\Downloads\GazpromEnergyDataEngineerCodeTest\sample_data")
  
path =os.getcwd()
# Change the directory 
#os.chdir(path) 
path=path+"/sample_data"  


# Read text File 
def read_file(file_path): 
    with open(file_path, 'r',encoding='UTF-8') as f: 
        print(f.read()) 
  
  
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if os.path.isfile(os.path.join(path, file)):
       if file.endswith(".SMRT"): 
        file_path = f"{path}\{file}"
  
        # call read text file function 
        read_file(file_path) 
        print(file)


# Create connection with the database
connection = sqlite3.connect('XOSERVE_DB')
cursor = connection.cursor()
print("Connected to DB")

# Create the table
cursor.execute('DROP TABLE IF EXISTS SMRT_TABLE')
print(" drop the table if already existed")
cursor.execute('CREATE TABLE  SMRT_TABLE(recordid, filetypeid, companyid,filecreationdate,filecreationtime,filegenerationno) ')
connection.commit()

print("table created")


# Iterate through the CSV reader, inserting values into the database
for row in file:
    no_records=0
    print(no_records)
    sql_insert= '''
          INSERT INTO smrt_table 
          VALUES (?,?,?,?,?,?)
'''
    print("insert query executed")
    
       
try:
   cursor.execute(sql_insert)
   connection.commit()
   no_records = no_records+1
   print("No of records inserted "+ no_records)
except Exception as e:
   print(e)

# disconnect from server
connection.close()
print("records inserted")