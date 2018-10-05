#Ryan Aday, Jared Ash
#SoftDev1 pd7
#HW 16-WHomst
#2018-10-04

import csv, sqlite3    

filename="peeps.csv"
DB_FILE="discobandit.db"

db=sqlite3.connect(DB_FILE)
c= db.cursor()

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    header = reader.fieldnames
    table_name = filename.split(".")[0]

    query = "CREATE TABLE " + table_name + "(" + ",".join([col + " TEXT" for col in header]) + ")"
    c.execute(query)

    for row in reader:
        query = "INSERT INTO " + table_name + " VALUES ("  + ",".join(["\"" + val + "\"" for val in row.values()]) + ")"
        c.execute(query)

db.commit()
db.close()
