import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path='Department.csv'
if os.path.isfile(path):
    pass
else:
    f=open('Department.csv','a',newline='')
    w=csv.writer(f)
    w.writerow(['Department ID','Department Name','List of batches'])
    f.close()

def checkdeptid(deptid):
    c=False
    f=open('Department.csv','r')
    r=csv.reader(f)
    for row in r:
        if (deptid in row[0]) == True:
            c=True
            break
    f.close()
    return c

def checkdeptnm(deptnm):
    c=False
    f=open('Department.csv','r')
    r=csv.reader(f)
    for row in r:
        if (deptnm in row[1]) == True:
            c=True
            break
    f.close()
    return c

def studadd(bid):
    li,s1,bmarks=[],0,''
    with open('Batch.csv','r') as f:
        r=csv.reader(f)
        for i in r:
            if i[0]==bid:
                s1=i[4]
                s1=s1[1:(len(s1)-1)]
                s1=s1+','
                x=''
                for j in s1:
                    if j==',':
                        li.append((x.strip()).strip("'"))
                        x=''
                        continue
                    x=x+j
    for i in li:
        c,Tmarks=0,0
        with open('Course.txt','r') as f:
            r=csv.reader(f)
            for j in r:
                if i in j[2]:
                    Tmarks=Tmarks+(eval(j[2]))[i]
                    c=c+1
        bmarks=bmarks+(Tmarks/c)
    return(bmarks/len(li))

def checkbid(bid):
    c=False
    f=open('Department.csv','r')
    r=csv.reader(f)
    for row in r:
        if (bid in row[2]) == True:
            c=True
            break
    f.close()
    return c


def deptonly():
    while True:
        print('a.Create a new Department')
        print('b.View all batches in a department')
        print('c.View average performance of all batches in a departmment')
        print('d.Show department statistics')
        print('e.EXIT')
        ch4=input('Enter your choice:')
        if ch4 in('a','A'):
            while True:
                li=[]
                id=input('Enter Department ID:')
                while checkdeptid(id)==True:
                    print('This department exists.Try again!!!')
                    id=input('Enter Department ID:')
                nm=input('Enter Department Name:')
                while checkdeptnm(nm)==True:
                    print('This department exists.Try again!!!')
                    nm=input('Enter Department Name:')
                n=int(input('Enter no. of batches in this department:'))
                bid=[]
                for i in range(0,n):
                    bnm=input(f'Enter name of Batch {i+1}:')
                    while checkdeptnm(bnm)==True:
                        print('This batch already exists.Try again!!!')
                        bnm=input(f'Enter name of Batch {i+1}:')
                    bid.append(bnm)
                li=[id,nm,bid]
                f=open('Department.csv','a',newline='')
                w=csv.writer(f)
                w.writerow(li)
                f.close()
                sch4=input('Enter more records(y/n):')
                if sch4 in('n','N'):
                    break
        elif ch4 in('b''B'):
            li=[]
            id=input('Enter Department ID:')
            while checkdeptid(id)==False:
                print('This department does not exist.Try again!!!')
                id=input('Enter Department ID:')
            with open('Department.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if id==i[0]:
                        li=i[2]
            print('All The Batches in this Department are:')
            for i in li:
                print(i,end=' ')
            print()
        elif ch4 in('c','C'):
            li=[]
            id=input('Enter Department ID:')
            while checkdeptid(id)==False:
                print('This department does not exist.Try again!!!')
                id=input('Enter Department ID:')
            with open('Department.csv','r') as f:
                r=csv.reader(f)
                for i in r:
                    if id==i[0]:
                        li=i[2]
            for i in li:
                print('Average performance of batch ',i," : ",studadd(bid))
        elif ch4 in('d','D'):
            ypoints = np.array([3, 8, 1, 10])
            plt.plot(ypoints, linestyle = 'dotted')
            plt.show()
        elif ch4 in('e','E'):
            break
        else:
            print("Invalid Choice.Try again!!!")

