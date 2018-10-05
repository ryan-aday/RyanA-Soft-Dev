#Ryan Aday, Jared Ash
#SoftDev1 pd7
#HW 16-WHomst
#2018-10-04

import csv, sqlite3    

#filename="peeps.csv"  #Can be changed for any file to be read
DB_FILE="app.db"  #Creates .db file

db=sqlite3.connect(DB_FILE) #Open file if exists, otherwise make db file
c= db.cursor()  #Manipulates rows in a query

def csv_to_db(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")  #Reads the csv file
        header = reader.fieldnames  #Returns list of headers
        table_name = filename.split(".")[0].split("/")[-1]

        query = "CREATE TABLE " + table_name + "(" + ",".join([col + " TEXT" for col in header]) + ")"
        c.execute(query)
        #Creates table via the sqlite command, join fxn joins all of the file names with type for roster

        for row in reader:
            query = "INSERT INTO " + table_name + " VALUES ("  + ",".join(["\"" + val + "\"" for val in row.values()]) + ")"
            c.execute(query)
            #Creates each entry into table, join fxn joins all of the key data with type for roster

csv_to_db("data/courses.csv")
csv_to_db("data/peeps.csv")
#Runs fnx for data files already in folder            

db.commit()
db.close()


#IMPORTANT!  Windows users can only open up SQLite with winpty sqlite3 on their terminal.
#To access data, run winpty sqlite3 discoband.db
#Commands to run are SELECT * from peeps;
#If you want to be fancy, use command .mode columns
