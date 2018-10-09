# Tarkus -- Theodore Peters, Mai Rachlevsky
# SoftDev1 pd7
# k17 -- No Trouble
# 2018-10-05

import csv, sqlite3    

DB_FILE="app.db"  #Creates .db file

db=sqlite3.connect(DB_FILE) #Open file if exists, otherwise make db file
c= db.cursor()  #Manipulates rows in a query

with open("data/peeps.csv") as csvfile:
	c.execute("CREATE TABLE sel_Peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")
	reader = csv.DictReader(csvfile)  #Reads the csv file, no delimiter needed
	for row in reader:
		c.execute("INSERT INTO sel_Peeps VALUES('{}', {}, {});".format(row['name'], row['age'], row['id']))
		#adds data for each row
csvfile.close() #Ends executable

with open("data/courses.csv") as csvfile:
	c.execute("CREATE TABLE sel_Courses(code TEXT, mark INTEGER, id INTEGER);")
	reader = csv.DictReader(csvfile)  #Reads the csv file, no delimiter needed
	for row in reader:
		c.execute("INSERT INTO sel_Courses VALUES('{}', {}, {});".format(row['code'], row['mark'], row['id']))
		#adds row headers
csvfile.close() #Ends executable

db.commit() #Needed to actually confirm tables being made
'''
db = sqlite3.connect('datta.db') #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
c.execute("CREATE TABLE nerds(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

csvfile = open('data/peeps.csv')
reader = csv.DictReader(csvfile)
for row in reader:
    c.execute("INSERT INTO nerds VALUES('{}', {}, {});".format(row['name'], row['age'], row['id']))
csvfile.close()

csvfile = open('data/courses.csv')
c.execute ("CREATE TABLE teacher_reviews(code TEXT, mark INTEGER, id INTEGER);")
reader = csv.DictReader(csvfile)
for row in reader:
    c.execute("INSERT INTO teacher_reviews VALUES('{}', {}, {});".format(row['code'], row['mark'], row['id']))
csvfile.close()
'''
db.commit()
#printTable= str(c.fetchall()).replace("),", "),\n")
#Makes data more legible

#Prints data from both tables
c.execute("SELECT * FROM sel_Peeps;")
print(str(c.fetchall()).replace("),", "),\n"), "\n\n\n")
c.execute("SELECT * FROM sel_Courses;")
print(str(c.fetchall()).replace("),", "),\n"), '\n')
db.close()  #close database
