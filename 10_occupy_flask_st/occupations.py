#ASTROWORLD - Rubin P., Puneet J., Ryan A.
#K06 - Divine Your Destiny!
#Period 7
#2018-09-13

from random import choices
from random import uniform

def read(CSVfileR):#taken from Intro II hw!Opens a file and returns the contents of the file in a list of strings
    c = open(CSVfileR,"r")
    CSV =  c.readlines()
    c.close()
    return CSV

def parse_data(filename):
    file = open(filename, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    list = raw.split("\n")      #split on new lines

    counter = 0
    while counter < len(list):  #loop thru it, splitting it on commas
        #remove unecessary quotes
        if '"' in list[counter]:        
            list[counter] = list[counter].replace('"', '')

        #splits on the last instance of a comma, once
        list[counter] = list[counter].rsplit(',', 1)
        counter += 1
    
    #make the empty dictionary and loop thru
    #the raw data of the file
    dict = {}
    counter = 1
    while counter < len(list) - 2:
        dict[list[counter][0]] = float(list[counter][1])
        counter += 1

    #print(dict) #diagnostic print statement
    return dict

def pick_job(dict):
    jobs = list(dict.keys()) #list of keys
    values = []              #empty list to be filled with values

    #loop thru the dict to get the weights/values
    for key in jobs:
        values.append(dict[key])

    #diagnostic print statements
    #print(values)
    #print(jobs)

    #uses the choices method in random which allows for one to pick from a list of items
    #and have it be weighted
    job = choices(jobs, values)
    return job[0]

def combine():
    return pick_job( parse_data('occupations.csv'))
#print(pick_job( parse_data('occupations.csv') ))

def main():
    File = read("data/occupations.csv")
    head = File[0]
    head = head[0:len(head) - 1]
    listH = head.split(",")
    h1 = listH[0]
    h2 = listH[1]
    Data = File
    Data = Data[1: len(Data)]
    Data = makeDict(Data)
    totalPercentage = editData(File)#total percentage is stored globally
    Dict = makeDict(File)
    return (randOccupation(Dict,totalPercentage), Data, h1, h2)
