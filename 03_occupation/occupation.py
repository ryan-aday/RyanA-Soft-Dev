#import csv

def randOcc():
    #1.  Read file.
    temp=open('occupations.csv', 'rU')
    dat=temp.read()

    #2.  Split file into multiple parts to reorg into dict

    obj=dat.split(',', '\n')
    #obj.split('\n')
    obj.pop(0);
    print(obj)
    for part in obj:
        print(part)
