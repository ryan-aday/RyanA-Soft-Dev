# Light Nates -- Theodore Peters, Ryan Aday
# SoftDev1 pd7
# k17 -- Average (If you know what I mean...)
# 2018-10-09

import csv, sqlite3    
from random import choice, randint  #Needed for print statement


#filename="peeps.csv"  #Can be changed for any file to be read
DB_FILE="app.db"  #Creates .db file

db=sqlite3.connect(DB_FILE) #Open file if exists, otherwise make db file
c= db.cursor()  #Manipulates rows in a query

c.execute("CREATE TABLE peeps_avg(id INTEGER PRIMARY KEY, average REAL);")

def get_avgs():
    c.execute("DELETE FROM peeps_avg") #Clears peeps_avg table
    c.execute("SELECT id FROM sel_Peeps")  #Takes all data from sel_Peeps table
    stu_dat=c.fetchall()[:] #Grabs all student data from sel_Peeps
    for student in stu_dat:
        c.execute("SELECT mark FROM sel_Courses WHERE sel_Courses.id={};".format(student[0]))
        #Selects marks with id = student's
        grades = c.fetchall()
        avg = 0.0
        for marks in grades:
            avg += marks[0]  #Adds avg to the marks list
        avg /= len(grades)
        c.execute("INSERT INTO peeps_avg VALUES({}, {});".format(student[0], avg))

def add_course(code, mark, stu_id):
    c.execute('INSERT INTO sel_Courses VALUES("{}", {}, {});'.format(code, mark, stu_id))
    
get_avgs()   #Adds avgs to peeps_avg
c.execute("SELECT * FROM peeps_avg;")
print('averages of starting courses: \n\n', c.fetchall(), '\n\n\n')  #Prints everything from peeps_avg
new_classes = ('A', 'B', 'C', 'D', 'D', 'E', 'F', 'G', 'H', 'I')
for i in range(40):
    add_course(choice(new_classes), randint(25, 99), randint(1, 10))  #Makes random marks for each new class
c.execute("SELECT * FROM sel_Courses;")
print('new courses:\n\n', c.fetchall(),'\n\n\n')  #Prints all data from new sel_Courses
get_avgs()  #Updates averages
c.execute("SELECT * FROM peeps_avg;")  
print('new avgs: \n\n', c.fetchall(), '\n\n\n') #Prints everything from new peeps_avg

db.commit()
db.close()


#IMPORTANT!  Windows users can only open up SQLite with winpty sqlite3 on their terminal.
#To access data, run winpty sqlite3 app.db
#Tables to see can be found with .tables
#Commands to run are SELECT * from <table>;
#If you want to be fancy, use command .mode columns
