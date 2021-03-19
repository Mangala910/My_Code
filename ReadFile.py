import glob
import os
import io



# Folder Path 
path =os.getcwd()
print("This is current working directory " +path)  
# Change the directory 
path=path+"/sample_data"
#os.chdir(path) 
  
# Read text File 
   
def read_text_file(file_path): 
    with open(file_path, 'r') as f: 
        print(f.read()) 
  
  
# iterate through all file 
for file in os.listdir(): 
    # Check whether file is in text format or not 
    if os.path.isfile(os.path.join(path, file)):
       if file.endswith(".SMRT"): 
        file_path = f"{path}\{file}"
  
        # call read text file function 
        read_text_file(file_path) 
        print(file)




        # strip whitespace from headers
    df.columns = df.columns.str.strip()




sql="INSERT INTO SMRT_TABLE SMRT_TABLE VALUES (?,?,?,?,?,?), row.split(",") "